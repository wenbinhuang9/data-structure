import unittest
from random import  randrange
from B_tree_memory import Node, BTree
class MyTestCase(unittest.TestCase):
    def test_split_child(self):

        parent = Node(4, False)

        parent.keys[0], parent.keys[1] = 10, 20
        parent.key_nums = 2

        child1 = Node(4, True)
        child1.keys[0], child1.keys[1], child1.keys[2], child1.keys[3] = 1,5,6, 9
        child1.key_nums = 4

        child2 = Node(4, True)
        child2.keys[0], child2.keys[1] = 11,19
        child2.key_nums = 2

        child3 = Node(4, True)
        child3.keys[0], child3.keys[1] = 21,29
        child3.key_nums = 2
        parent.childs[0] = child1
        parent.childs[1] = child2
        parent.childs[2] = child3

        btree = BTree(4)

        btree.split_child(parent, 0, child1)

        parent_correct_nums  = [5,10,20]
        for i, key in enumerate(parent_correct_nums):
            self.assertEqual( key == parent.keys[i], True)

        self.assertEqual(parent.key_nums == 3, True)

        c1_keys = [1]
        c2_keys = [6, 9]
        c3_keys = [11, 19]
        c4_keys = [21,29]
        correct_child_res = [c1_keys, c2_keys, c3_keys, c4_keys]
        for i in range(parent.key_nums + 1):
            child = parent.childs[i]
            correct_child = correct_child_res[i]
            for i, key in enumerate(correct_child):
                self.assertEqual(key == child.keys[i] , True)
            self.assertEqual(child.key_nums == len(correct_child), True)



    def test_BTree_insert(self):
        btree =BTree(4)

        for i in range(10000):

            btree.insert(i, i)
            res = btree.get(i)
            self.assertEqual(res == True, True)
        for i in range(10000):
            self.assertEqual(btree.get(i) == True, True)


    def test_BTree_delete(self):
        btree =BTree(4)

        num = 2000
        for i in range(num):
            btree.insert(i, i)
            res = btree.get(i)
            self.assertEqual(res == True, True)
        for i in range(num):
            btree.delete(i)
            self.assertEqual(btree.get(i) == False, True)

        for i in range(num):
            btree.insert(i, i)
            res = btree.get(i)
            self.assertEqual(res == True, True)
        for i in range(num):
            btree.delete(i)
            self.assertEqual(btree.get(i) == False, True)


        print (btree.sorted_keys())

if __name__ == '__main__':
    unittest.main()
