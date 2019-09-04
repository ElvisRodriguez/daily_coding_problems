'''
This problem was asked by Google.

You are given an array of arrays of integers,
 where each array corresponds to a row in a triangle of numbers.
For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:
  1
 2 3
1 5 1
We define a path in the triangle to start at the top
 and go down one row at a time to an adjacent value,
  eventually ending with an entry on the bottom row.
 For example, 1 -> 3 -> 5.
 The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
'''


def max_triangle_weight(triangle):
    max_weight = 0
    for row in triangle:
        max_weight += max(row)
    return max_weight


if __name__ == '__main__':
    triangle = [[1], [2, 3], [1, 5, 1]]
    print(max_triangle_weight(triangle))
