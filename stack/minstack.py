#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.minimum:
            self.minimum.append(min(x, self.minimum[-1]))
        else:
            self.minimum.append(x)
            
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minimum.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.minimum:
            return None
        
        return self.minimum[-1]
