
class Queue:
    def __init__(self):
        self.capacity = 2
        self.__size = 0
        self.queue = [0] * self.capacity
        self.front = 0
        self.rear = 0

    def append(self, e):
        if self.full():
            self.__adjust_capacity()
        self.queue[self.rear] = e
        self.rear = (self.rear + 1) % self.capacity
        self.__size += 1


    def pop(self):
        if self.empty():
            return None

        e = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.__size -= 1

        return e

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
