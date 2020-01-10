
## implment a queue with extra min function where returns the minimum of the element in the queue
## todo using default capacity, if the capacity is not enough, just make it larger
from queue import Queue
from dequeue import Dequeue


class MinQueue():
    def __init__(self):
        self.capacity = 2
        self.__size = 0
        self.queue = [0] * self.capacity
        self.front = 0
        self.rear = 0
        ## a monotonic dequeue to maintain the min value , the val in decreasing order in the dequeue
        self.__min_dequeue = Dequeue()

    def append(self, e):
        if self.full():
            self.__adjust_capacity()
        idx = self.rear
        self.queue[self.rear] = e
        self.rear = (self.rear + 1) % self.capacity
        self.__size += 1

        self.__add_to_min_queue(idx)

    def pop(self):
        if self.empty():
            return None

        e = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.__size -= 1

        while not self.__min_dequeue.empty() and self.__isvalid_index(self.__min_dequeue.peak()) == False:
            self.__min_dequeue.pop()
        return e

    def __isvalid_index(self, idx):
        if self.empty():
            return False
        if self.full():
            return True

        if self.rear > self.front:
            return True if self.front <= idx < self.rear else False
        if self.rear < self.front:
            return True if (idx >= self.front or idx < self.rear) else False

        return False

    def __add_to_min_queue(self, idx):
        while not self.__min_dequeue.empty() and self.queue[idx] <= self.queue[self.__min_dequeue.peakRight()]:
            self.__min_dequeue.popRight()
        self.__min_dequeue.append(idx)

    def min(self):
        if self.empty():
            return None
        return self.queue[self.__min_dequeue.peak()]


    def peek(self):
        return None if self.empty() else  self.queue[self.rear]


    def empty(self):
        return self.__size == 0

    def full(self):
        return self.__size == self.capacity

    def size(self):
        return self.__size

    def __adjust_capacity(self):
        if not self.full():
            return
        new_capacity = self.capacity * 2
        new_queue = [0] * new_capacity
        idx_in_queue = self.front
        idx_in_new_queue = 0

        e = self.queue[idx_in_queue]
        new_queue[idx_in_new_queue] = e
        idx_in_queue = (idx_in_queue + 1) % self.capacity
        idx_in_new_queue += 1

        while idx_in_queue != self.front:
            e = self.queue[idx_in_queue]
            new_queue[idx_in_new_queue] = e
            idx_in_queue = (idx_in_queue + 1) % self.capacity
            idx_in_new_queue += 1
        self.queue = new_queue
        self.front = 0
        self.rear = self.capacity
        self.capacity = new_capacity

