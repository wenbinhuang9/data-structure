import unittest

from queue.queue import Queue


class MyTestCase(unittest.TestCase):
    def test_queue(self):
        q = Queue()
        q.append(2)
        q.append(3)
        self.assertEqual(q.size() == 2, True)
        val = q.pop()
        self.assertEqual(val == 2, True)
        self.assertEqual(q.size() == 1, True)

        self.assertEqual(q.pop() == 3, True)
        self.assertEqual(q.pop() == None, True)

        val = [1,2,3,4,5]
        for v in val:
            q.append(v)
        for v in val:
            self.assertEqual(q.pop() == v, True)

if __name__ == '__main__':
    unittest.main()
