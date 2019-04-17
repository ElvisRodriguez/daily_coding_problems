'''
This problem was asked by Amazon.

Implement a stack that has the following methods:
- push(val), which pushes an element onto the stack
- pop(), which pops off and returns the topmost element of the stack.
If there are no elements in the stack, then it should throw an error or return
null.
- max(), which returns the maximum value in the stack currently.
If there are no elements in the stack, then it should throw an error or return
null.
Each method should run in constant time.
'''

import random


class Stack:
    def __init__(self):
        self.top = None
        self._container = []
        self._max = None
        self._second_max = None

    def push(self, val):
        self._container.append(val)
        self.top = val
        if self._max is None:
            self._max = val
        elif val > self._max:
            self._second_max = self._max
            self._max = val

    def pop(self):
        if len(self._container) == 0:
            return None
        return_value = self._container[-1]
        self._container.pop(-1)
        if len(self._container) == 0:
            self.top = None
        else:
            self.top = self._container[-1]
        if self._max == return_value:
            self._max = self._second_max
        return return_value

    def max(self):
        return self._max


if __name__ == '__main__':
    stack = Stack()
    arr = []
    for i in range(10):
        val = i + 1
        stack.push(val)
        arr.append(val)
    print(max(arr))
    print(stack.max())
    print(stack.pop())
    print(stack.max())
