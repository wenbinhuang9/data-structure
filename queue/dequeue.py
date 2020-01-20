
## both directional queue
class Dequeue():
    def __init__(self):
        self.capacity = 2
        self.__size = 0
        self.queue = [0] * self.capacity
        self.front = 0
        self.rear = 0


    def append(self,e):
        if self.__full():
            self.__adjust_capacity()
        self.queue[self.rear] = e
        self.__size += 1
        self.rear = (self.rear + 1) % self.capacity


    def appendLeft(self, e):
        if self.__full():
            self.__adjust_capacity()

        self.front = (self.front - 1) % self.capacity

        self.queue[self.front] = e
        self.__size += 1


    def peak(self):
        return None if self.empty() else self.queue[self.front]

    def peakRight(self):
        return None if self.empty() else self.queue[(self.rear - 1) % self.capacity]
    def pop(self):
        if self.empty():
            return None

        e = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.__size -= 1
        return e

    def popRight(self):
        if self.empty():
            return None
        self.rear = (self.rear - 1) % self.capacity
        e = self.queue[self.rear]
        self.__size -= 1
        return e


    def __adjust_capacity(self):
        if not self.__full():
            return
        double_capacity = 2 * self.capacity
        copy_queue = [0] * double_capacity
        old_pointer = self.front
        first_element = self.queue[old_pointer]
        old_pointer = (old_pointer + 1) % self.capacity
        new_pointer = 0
        copy_queue[new_pointer] = first_element
        new_pointer += 1
        while old_pointer != self.front:
            element = self.queue[old_pointer]
            old_pointer = (old_pointer + 1) % self.capacity
            copy_queue[new_pointer] = element
            new_pointer += 1

        self.queue = copy_queue
        self.front = 0
        self.rear = self.capacity
        self.capacity = double_capacity

        return

    def size(self):
        return self.__size

    def empty(self):
        return self.__size == 0

    def __full(self):
        return self.__size == self.capacity
