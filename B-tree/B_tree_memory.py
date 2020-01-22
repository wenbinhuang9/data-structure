

## implementation of b+ tree in memory

from bisect import  bisect_right
class Node:
    def __init__(self, m, is_leaf):
        self.keys = [None] * (m)
        self.childs = [None] * (m + 1)
        self.is_leaf = is_leaf
        self.key_nums = 0



## todo always makes m a even number
class BTree:
    def __init__(self, m):
        self.root = None
        self.m = m
        self.t = (m + 1) / 2

    def __init_root(self, key):
        self.root = Node(self.m, True)
        self.root.keys[0] = key
        self.root.key_nums += 1

    def insert(self, key, value):
        if self.root == None:
            self.__init_root(key)
            return

        ## the root keys is full
        if self.root.key_nums == self.m - 1:
            new_root = Node(self.m, False)
            new_root.childs[0] = self.root

            self.split_child(new_root, 0, self.root)
            self.root = new_root

        self.insertNotFull(self.root, key)

    ## todo a bit complex here
    def split_child(self, parent, key_pos_in_parent, split_child):
        mid = (self.m + 1)/2 - 1
        mid_key = split_child.keys[mid]
        total_num = split_child.key_nums
        right_node = Node(self.m, split_child.is_leaf)

        ## copy right part key
        l = 0
        for r in range(mid + 1, total_num):
            right_node.keys[l] = split_child.keys[r]
            split_child.keys[r] = None
            l += 1

        ## copy right part childs
        l = 0
        for r in range(mid + 1, total_num + 1):
            right_node.childs[l] = split_child.childs[r]
            l += 1
            split_child.childs[r] = None

        right_node.key_nums = split_child.key_nums - mid - 1

        split_child.key_nums = mid

        ## deal with the parent part
        ## shifting parents'keys right
        parent_keys_num = parent.key_nums
        for i in range(parent_keys_num - 1, key_pos_in_parent - 1 , -1):
            parent.keys[i + 1] = parent.keys[i]
        parent.keys[key_pos_in_parent] = mid_key

        ## shifting parents' child right
        for i in range(parent_keys_num, key_pos_in_parent, -1):
            parent.childs[i + 1] = parent.childs[i]

        parent.childs[key_pos_in_parent + 1] = right_node

        parent.key_nums += 1



    def __find_insert_index(self, node, key):
        return bisect_right(node.keys, key, 0, node.key_nums)

    def __insert_into_leaf_node(self, index, node, key):
        for i in range(node.key_nums - 1, index - 1, -1):
            node.keys[i + 1] = node.keys[i]
        node.keys[index] = key
        node.key_nums += 1


    def insertNotFull(self, node, key):
        ## insert direcly
        inserted_index = self.__find_insert_index(node, key)
        if node.is_leaf:
            self.__insert_into_leaf_node(inserted_index, node, key)
            return

        inserted_child = node.childs[inserted_index]

        if inserted_child.key_nums == self.m - 1:
            self.split_child(node, inserted_index, inserted_child)

        inserted_child = self.__find_insert_index(node, key)

        self.insertNotFull(node.childs[inserted_child], key)


    ##todo change it to return the value
    def get(self, key):
        if not self.root:
            return False

        return self.__get(self.root, key)

    def __get(self, root, key):
        inserted_index = self.__find_insert_index(root, key)

        if root.is_leaf:
            return inserted_index - 1 >= 0 and root.keys[inserted_index - 1] == key

        ## not leaf
        if inserted_index - 1 >= 0 and root.keys[inserted_index - 1] == key:
            return True

        return self.__get(root.childs[inserted_index], key)

    def delete(self, key):
        self.__delete(self.root, key)
        return

    def __delete(self, root, key):
        idx = self.__get_key_idx(root, key)

        ## key in current node
        if 0 <= idx < root.key_nums and root.keys[idx] == key:
            if root.is_leaf:
                self.removeFromLeaf(root, idx)
            else:
                self.removeFromNonLeaf(root, idx)
        else:
        ## key not in current node, just going down
            if root.is_leaf:
                print(str(key) +" key does not exist here")
                return
            child = root.childs[idx]
            if child.key_nums < self.t:
                self.__fill(root, idx)

            idx = self.__get_key_idx(root, idx)

            self.__delete(root.childs[idx], key)
            ## todo finish here

    def __fill(self, node, idx):
        if idx - 1 >= 0 and node.childs[idx - 1].key_nums >= self.t:
            self.borrow_from_prev(node, idx)
        elif idx + 1 <= node.key_nums and node.childs[idx + 1].key_nums >= self.t:
            self.borrow_from_suc(node, idx)
        else:
            if idx == node.key_nums:
                self.__merge(node, idx - 1)
            else:
                self.__merge(node, idx)

    def borrow_from_prev(self, node, idx):
        child = node.childs[idx]
        left_sibling = node.childs[idx - 1]

        ## shifting the child keys and child pointers
        for i in range(child.key_nums - 1, -1, -1):
            child.keys[i + 1] = child.keys[i]
        if child.is_leaf == False:
            for i in range(child.key_nums, -1, -1):
                child.childs[i + 1] = child.childs[i]
        ## descending the key from parent down to the child.keys[0]
        child.keys[0] = node.keys[idx - 1]
        if child.is_leaf == False:
            child.childs[0] = left_sibling.childs[left_sibling.key_nums]

        node.keys[idx - 1] = left_sibling.keys[left_sibling.key_nums - 1]
        child.key_nums += 1
        left_sibling.key_nums -= 1

        return

    def borrow_from_suc(self, node, idx):
        child = node.childs[idx]
        right_sibling = node.childs[idx + 1]

        ## descending the key from parent down to the child.keys[0]
        child.keys[child.key_nums] = node.keys[idx]
        if child.is_leaf == False:
            child.childs[child.key_nums + 1] = right_sibling.childs[0]

        node.keys[idx] = right_sibling.keys[0]

        ##shiftting the keys and child pointers left
        for i in range(1, right_sibling.key_nums):
            right_sibling.keys[i - 1] = right_sibling.keys[i]

        for i in range(1, right_sibling.key_nums + 1):
            right_sibling.childs[i - 1] = right_sibling.childs[i]

        child.key_nums += 1
        right_sibling.key_nums -= 1

        return


    def __get_key_idx(self, node, key):
        idx = 0
        while idx < node.key_nums and node.keys[idx] < key:
            idx += 1
        return idx

    def removeFromLeaf(self, node, idx):
        for i in range(idx + 1, node.key_nums):
            node.keys[i - 1] = node.keys[i]

        node.key_nums -= 1

    def __get_pre(self, node):
        while node.is_leaf == False:
            node = node.childs[node.key_nums]
        return  node.keys[node.key_nums - 1]

    def __get_suc(self, node):
        while node.is_leaf == False:
            node = node.childs[0]
        return node.keys[0]

    def __merge(self, node, idx):
        k = node.keys[idx]

        leftchild = node.childs[idx]
        if leftchild == None:
            print ("")
        rightchild = node.childs[idx + 1]

        ## 1. merge leftchild, rightchild keys and potiners
        ## 1.1 descend the key of idx to the merged node
        leftchild.keys[self.t - 1] = k
        ## 1.2 merge rightchild keys to leftchild
        for i in range(0, rightchild.key_nums):
            leftchild.keys[i + self.t]  = rightchild.keys[i]
        ## 1.3 merge rightchild child pointers to leftchild
        if rightchild.is_leaf == False:
            for i in range(0, rightchild.key_nums + 1):
                leftchild.childs[i + self.t] = rightchild.childs[i]

        ## 2. shifting the keys and child pointers in node to left
        for i in range(idx + 1, node.key_nums):
            node.keys[i - 1] = node.keys[i]

        for i in range(idx + 2, node.key_nums + 1):
            node.childs[i - 1] = node.childs[i]

        leftchild.key_nums += (rightchild.key_nums + 1)
        node.key_nums -= 1
        rightchild.key_nums = 0

        if node == self.root and node.key_nums == 0:
            self.root = leftchild
        return


    def removeFromNonLeaf(self, node, idx):
        k = node.keys[idx]

        leftchild = node.childs[idx]
        rightchild = node.childs[idx + 1]
        if leftchild.key_nums >= self.t:
            pred_key = self.__get_pre(leftchild)
            node.keys[idx] = pred_key

            self.__delete(leftchild, pred_key)

        elif rightchild.key_nums >= self.t:
            suc_key = self.__get_suc(rightchild)
            node.keys[idx] = suc_key
            self.__delete(rightchild, suc_key)

        else:
            self.__merge(node, idx)
            self.__delete(node.childs[idx], k)

    def sorted_keys(self):
        return self.__sorted_keys(self.root)

    def __sorted_keys(self, node):
        if node.is_leaf:
            return [node.keys[i] for i in range(node.key_nums)]
        res = []

        for i in range(node.key_nums + 1):
            res.extend(self.__sorted_keys(node.childs[i]))
            if i < node.key_nums:
                res.append(node.keys[i])

        return res