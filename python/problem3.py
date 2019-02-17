'''
This problem was asked by Google.

Given the root to a binary tree, implment serialize(root), which
serializes the tree into a string, and deserialize(s), which
deserializes the string back into the tree.

For example, given the following Node class
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
The tests in the main should pass.
'''


#Helper Method to traverse the Binary Tree in order.

#Runtime: O(log(n)) where n is the number of nodes in the tree.
def traverse(root, nodes=[]):
    if root:
        nodes = traverse(root.left, nodes)
        nodes.append(root.val)
        nodes = traverse(root.right, nodes)
    return nodes

#Helper Method to build a Binary Tree from an array.


def serialize(root):
    pass

def deserialize(s):
    pass


if __name__ == '__main__':
    #node = Node('root', Node('left', Node('left.left')), Node('right'))
    #assert(deserialize(serialize(node)).left.left.val == 'left.left')

    node = Node(val=4, left=Node(val=3, left=Node(1), right=Node(2)), right=Node(val=5, right=Node(6)))
    print(traverse(node))
