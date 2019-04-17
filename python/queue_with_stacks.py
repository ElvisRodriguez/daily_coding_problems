'''
This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO
(first-in, first-out) data structure with the following methods:
enqueue, which inserts an element into the queue, and dequeue, which removes it.
'''

import random


class Stack:
    def __init__(self):
        self._container = []
        self.top = None

    def push(self, value):
        self._container.append(value)
        self.top = value

    def pop(self):
        if len(self._container) == 0:
            return None
        if len(self._container) == 1:
            self.top = None
            value = self._container[0]
            self._container.pop(0)
        else:
            value = self._container[-1]
            self._container.pop(-1)
            self.top = self._container[-1]
        return value

    def empty(self):
        return len(self._container) == 0


class Queue:
    def __init__(self):
        self.reversed = Stack()
        self.ordered = Stack()

    def enqueue(self, val):
        self.ordered.push(val)

    def dequeue(self):
        if self.ordered.empty():
            return None
        while not self.ordered.empty():
            self.reversed.push(self.ordered.pop())
        value = self.reversed.pop()
        while not self.reversed.empty():
            self.ordered.push(self.reversed.pop())
        return value

    def empty(self):
        return self.ordered.empty()


if __name__ == '__main__':
    test_arr = [random.randint(1, 25) for x in range(15)]
    q = Queue()
    for number in test_arr:
        q.enqueue(number)
    copied_arr = []
    while not q.empty():
        copied_arr.append(q.dequeue())
    print(test_arr)
    print(copied_arr)
