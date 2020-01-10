import unittest

from queue.dequeue import Dequeue


class MyTestCase(unittest.TestCase):
    def test_dequeue(self):
        deq = Dequeue()
        deq.append(1)
        deq.append(2)
        ##1. test peak
        self.assertEqual(deq.peak() == 1, True)
        self.assertEqual(deq.peakRight() == 2, True)
        ##2. test pop
        self.assertEqual(deq.pop() == 1, True)
        self.assertEqual(deq.pop() == 2, True)

        self.assertEqual(deq.empty(), True)
        self.assertEqual(deq.pop() == None, True)

        deq.append(1)
        deq.appendLeft(2)
        self.assertEqual(deq.pop() == 2, True)

        deq.append(3)

        deq.append(4)

        self.assertEqual(deq.popRight() == 4, True)
        self.assertEqual(deq.pop() == 1, True)
        self.assertEqual(deq.pop() == 3, True)

        adding_e = [1, 2, 3,4,5, 6, 7 ,8,9,10]
        for e in adding_e:
            deq.appendLeft(e)

        idx = 0
        while not deq.empty():
            self.assertEqual(deq.popRight() == adding_e[idx], True)
            idx += 1






if __name__ == '__main__':
    unittest.main()
