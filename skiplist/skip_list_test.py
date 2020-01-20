import unittest

from skiplist.skip_list import SkipList

## todo how to test the performance
class MyTestCase(unittest.TestCase):
    def test_insert(self):
        skiplist = SkipList(3, 0.4)

        for i in range(10):
            self.assertEqual(skiplist.insert(i, i), True)
            self.assertEqual(skiplist.get(i) == i, True)

        skiplist = SkipList(3, 0.4)
        for i in range(10):
            key = "helloword" + str(i)
            val = key
            self.assertEqual(skiplist.insert(key, val), True)
            self.assertEqual(skiplist.get(key) == val, True)

    def test_delete(self):
        skiplist = SkipList(3, 0.4)
        for i in range(10):
            key = "helloword" + str(i)
            val = key
            self.assertEqual(skiplist.insert(key, val), True)
            self.assertEqual(skiplist.get(key) == val, True)

            self.assertEqual(skiplist.delete(key), True)
            self.assertEqual(skiplist.get(key) == None, True)



if __name__ == '__main__':
    unittest.main()
