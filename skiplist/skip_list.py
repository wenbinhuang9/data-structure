import random
class Node:
    def __init__(self, key, value, level):
        self.key = key
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:

    def __create_node(self, key, value, level):
        return Node(key, value, level)

    def __init__(self, max_level, p):
        self.MAX_LEVEL = max_level
        self.P = p
        ## todo default key to the -1
        self.header = self.__create_node(-1, None, self.MAX_LEVEL)

        ## current level of skip list
        self.level = 0

    def insert(self, key, value):

        next_insert = self.__get_insert_place(key)

        current = next_insert[0].forward[0]

        ## find the key, just update the value
        if current != None and current.key == key:
            current.value = value
            return True

        node_level = self.__randomLevel()

        if node_level > self.level:
            for i in range(self.level + 1, node_level + 1):
                next_insert[i] = self.header
            self.level = node_level
        node = self.__create_node(key, value, node_level)

        for i in range(0, node_level + 1):
            node.forward[i] = next_insert[i].forward[i]
            next_insert[i].forward[i] = node

        return True

    def get(self, key):
        insert_place = self.__get_insert_place(key)

        current = insert_place[0].forward[0]
        if current == None or current.key != key:
            return None

        return current.value

    def delete(self, key):
        insert_place = self.__get_insert_place(key)

        current = insert_place[0].forward[0]

        if current == None or current.key != key:
            ## don't exist
            return True

        for i in range(len(current.forward)):
            insert_place[i].forward[i] = current.forward[i]
            current.forward[i] = None

        return True



    def __get_insert_place(self, key):
        current = self.header
        next_insert = [None] * (self.MAX_LEVEL + 1)

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            next_insert[i] = current
        return  next_insert

        # create random level for node

    def __randomLevel(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def displayList(self):

        for l in range(self.level + 1):
            print("Level {}: ".format(l))
            node = self.header.forward[l]
            while node != None:
                print(str(node.key) + " ")
                node = node.forward[l]



