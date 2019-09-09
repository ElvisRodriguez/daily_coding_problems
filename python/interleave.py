'''
This problem was asked by Google.

Given a stack of N elements,
    interleave the first half of the stack with the second half reversed using only
    one other queue. This should be done in-place.

Recall that you can only push or pop from a stack,
    and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3].
If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
'''

# Created a Stack and Queue class for readability


class Stack:
    def __init__(self, container=[]):
        self._container = container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop(-1)

    def empty(self):
        return len(self._container) == 0


class Queue:
    def __init__(self, container=[]):
        self._container = container

    def enqueue(self, item):
        self._container.append(item)

    def dequeue(self):
        return self._container.pop(0)

    def empty(self):
        return len(self._container) == 0

# Runtime: O(n^2) where n is the size of the stack.
# Space Complexity: O(n) where n is the size of the stack.


def interleave(stack, n):
    queue = Queue()
    # We decrement n because we want to leave the first value of the
    #  stack untouched, as it's already in it's interleaved position.
    n -= 1
    while n > 0:
        for i in range(n):
            queue.enqueue(stack.pop())
        for i in range(n):
            stack.push(queue.dequeue())
        n -= 1
    return stack._container


if __name__ == '__main__':
    stack = Stack([1, 2, 3, 4, 5])
    print(interleave(stack, 5))
    stack = Stack([1, 2, 3, 4])
    print(interleave(stack, 4))
