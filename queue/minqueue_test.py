import unittest


from queue.minqueue import MinQueue
class MyTestCase(unittest.TestCase):
    def test_minqueue(self):
        minqueue = MinQueue()

        val = [1, 2, 3, 4, 5]
        for v in val:
            minqueue.append(v)

        for v in val:
            self.assertEqual(minqueue.min() == v, True)
            self.assertEqual(minqueue.pop() == v, True)

        self.assertEqual(minqueue.min() == None, True)
        self.assertEqual(minqueue.pop() == None, True)

        val = [5,4,3,2,1]

        for v in val:
            minqueue.append(v)

        for v in val:
            self.assertEqual(minqueue.min() == 1, True)

if __name__ == '__main__':
    unittest.main()
