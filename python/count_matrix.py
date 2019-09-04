'''
This problem was asked by Google.

Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2,
 compute the number of elements of M smaller than M[i1, j1]
 and larger than M[i2, j2].

For example, given the following matrix:

[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]

And i1 = 1, j1 = 1, i2 = 3, j2 = 3,
 return 14 as there are 14 numbers in the matrix
 smaller than 6 or greater than 23.
'''

# Runtime O(C + 2R)
# Where C is the number of cells that are either smaller than Matrix[i1, j1]
#   or larger than Matrix[i2, j2] and R is the number of rows.


def count_cells(i1, i2, j1, j2, matrix):
    smaller = matrix[i1][j1]
    larger = matrix[i2][j2]
    count = 0
    for row in matrix:
        for cell in row:
            if cell < smaller:
                count += 1
            else:
                break
    for row in matrix:
        for i in range(len(row) - 1, -1, -1):
            if row[i] > larger:
                count += 1
            else:
                break
    return count


if __name__ == '__main__':
    matrix = [
        [1, 3, 7, 10, 15, 20],
        [2, 6, 9, 14, 22, 25],
        [3, 8, 10, 15, 25, 30],
        [10, 11, 12, 23, 30, 35],
        [20, 25, 30, 35, 40, 45]
    ]
    print(count_cells(1, 3, 1, 3, matrix))
