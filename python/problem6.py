'''
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of
each node holding next and prev fields, it holds a field named both, which is
an XOR of the next node and the previous node. Implement an XOR linked list; it
has an add(element) which adds the element to the end, and a get(index) which
returns the node at index.

If using a language that has no pointers (such as Python), you can assume you
have access to get_pointer and dereference_pointer functions that converts
between nodes and memory addresses.
'''


def xor(a, b):
    return bool(a) ^ bool(b)


class Node:
    def __init__(self, data, both=None):
        self.data = data
        self.both = both


class xor_link_list:
    def __init__(self, element=None):
        self.head = Node(element) if element else None
        self.size = 1 if element else 0

    def add(self, element):
        if self.head is None:
            self.head = Node(element)
        else:
            self.head.both = xor(None ^ Node(element))
        self.size += 1


if __name__ == '__main__':
    new_list = xor_link_list(4)
    print(new_list.head.data)
    print(new_list.head.both)
    new_list.add(5)
    print(new_list.head.both)
