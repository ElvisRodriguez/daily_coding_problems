'''
This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12

'''


def spiral(matrix, n, m):
    row_min = 0
    col_min = 0
    row_max = n - 1
    col_max = m - 1
    row = 0
    col = 0
    nodes = []
    while len(nodes) < n * m:
        while col < col_max:
            nodes.append(matrix[row][col])
            col += 1
        col_max -= 1
        while row < row_max:
            nodes.append(matrix[row][col])
            row += 1
        row_max -= 1
        while col > col_min:
            nodes.append(matrix[row][col])
            col -= 1
        col_min += 1
        while row > row_min:
            nodes.append(matrix[row][col])
            row -= 1
        row_min += 1
        row = row_min
        col = col_min
    return nodes


if __name__ == '__main__':
    matrix = [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
    print(spiral(matrix, n=len(matrix), m=len(matrix[0])))
