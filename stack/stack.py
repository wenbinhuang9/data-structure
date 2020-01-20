

class Stack():
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)


    def pop(self):
        """
        :rtype: None
        """
        e = self.stack.pop()
        return e
    
    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None

        return self.stack[-1]
