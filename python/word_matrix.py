'''
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that
returns whether the word can be found in the matrix by going left-to-right, or
up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost
column. Similarly, given the target word 'MASS', you should return true,
since it's the last row.
'''


def find_word(matrix, target):
    for i in range(len(matrix)):
        lr_word = ''.join(matrix[i])
        if target in lr_word or target == lr_word:
            return True
        ud_word = ''.join([matrix[j][i] for j in range(len(matrix))])
        if target in ud_word or target == ud_word:
            return True
    return False


if __name__ == '__main__':
    matrix = [
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']
    ]
    print(find_word(matrix, 'FOAM'))
    print(find_word(matrix, 'MASS'))
