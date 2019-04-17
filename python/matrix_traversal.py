'''
This problem was asked by Facebook.

There is an N by M matrix of zeroes.
Given N and M, write a function to count the number of ways of starting at
the top-left corner and getting to the bottom-right corner.
You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are
two ways to get to the bottom-right:
- Right, then down
- Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
'''


def matrix_traversal_helper(matrix, row, col):
    if row == len(matrix) - 1 and col == len(matrix) - 1:
        return 1
    if row == len(matrix) - 1:
        return matrix_traversal_helper(matrix, row, col + 1)
    if col == len(matrix) - 1:
        return matrix_traversal_helper(matrix, row + 1, col)
    return matrix_traversal_helper(matrix, row + 1, col) + matrix_traversal_helper(matrix, row, col + 1)


def matrix_traversal(matrix):
    row = 0
    col = 0
    count = matrix_traversal_helper(matrix, row, col)
    return count


def create_matrix(size):
    row = [0] * size
    matrix = []
    for i in range(size):
        matrix.append(row)
    return matrix


if __name__ == '__main__':
    matrix = create_matrix(5)
    print(matrix_traversal(matrix))
