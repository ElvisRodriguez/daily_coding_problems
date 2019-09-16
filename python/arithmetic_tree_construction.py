'''
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree.
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.
Given the root to such a tree, write a function to evaluate it.
For example, given the following tree:

        *
      /   \
     +     +
    / \   / \
   3   2 4   5

You should return 45, as it is (3 + 2) * (4 + 5).
'''


class Node(object):
    # Simple Node class to use for our binary tree
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree(object):
    # Binary Tree class used for print debugging as well as easily adding nodes
    def __init__(self, root):
        self.root = root

    def __str__(self):
        queue = [self.root]
        all_nodes = []
        while queue:
            node = queue.pop(0)
            all_nodes.append(str(node.data))
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return ''.join(all_nodes)

    # Nodes are added from left to right until a level is filled
    # This is not a binary search tree implementation, so no need to perform
    #  node comparisons to determine where a new node should be placed.
    def add_node(self, data):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = Node(data)
                return
            else:
                queue.append(node.left)
            if node.right is None:
                node.right = Node(data)
                return
            else:
                queue.append(node.right)


# Helper method to compute the sub equations in the binary tree
def parse_equation(left_operand, operation, right_operand):
    if operation == '+':
        return left_operand + right_operand
    if operation == '-':
        return left_operand - right_operand
    if operation == '*':
        return left_operand * right_operand
    if operation == '/':
        return left_operand / right_operand


# Time Complexity: O(log(n)) where n is the number of nodes in the tree
# Space Complexity: O(1), operators and integers are unchanging containers
def compute_nodes(node):
    operators = ['+', '-', '*', '/']
    integers = [x for x in range(10)]
    # If the node is an operator, we have no reached the leaf nodes
    # We call the method again for the left and right nodes
    #  until we reach a leaf node
    if node.data in operators:
        return parse_equation(
            compute_nodes(node.left), node.data, compute_nodes(node.right)
        )
    # If the node is an integer, it's also a lead node, meaning we can simply
    #  return the integer to be computed by our parse_equation method
    if node.data in integers:
        return node.data


if __name__ == '__main__':
    new_root = Node('*')
    binary_tree = BinaryTree(new_root)
    for data in ['+', '+', 3, 2, 4, 5]:
        binary_tree.add_node(data)
    print(compute_nodes(new_root))
