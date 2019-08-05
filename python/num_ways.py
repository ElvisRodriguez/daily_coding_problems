'''
This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s.
Starting from the top left corner,
how many ways are there to reach the bottom right corner?

You can only move right and down.
0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0.
'''


def valid_coordinate(matrix, point):
    if -1 in point:
        return False
    x = point[0]
    y = point[1]
    valid_indices = False
    try:
        new_point = matrix[x][y]
        valid_indices = True
    except IndexError:
        return False
    if matrix[x][y] == 1:
        return False
    return valid_indices


def new_points(matrix, point):
    right = (point[0], point[1]+1)
    down = (point[0]+1, point[1])
    points = [right, down]
    for p in points:
        if not valid_coordinate(matrix, p):
            points.pop(points.index(p))
    return points


def find_path(matrix, point, endpoint):
    if point == endpoint:
        return 1
    points = new_points(matrix, point)
    if not points:
        return 0
    if len(points) == 1:
        return find_path(matrix, points[0], endpoint)
    if len(points) == 2:
        return find_path(matrix, points[0], endpoint) + find_path(matrix, points[0], endpoint)


def find_total_paths(matrix):
    point = (0, 0)
    max_row = len(matrix)
    max_col = len(matrix[0])
    endpoint = (max_row-1, max_col-1)
    return find_path(matrix, point, endpoint)


if __name__ == '__main__':
    matrix = [
        [0, 0, 1],
        [0, 0, 1],
        [1, 0, 0]
    ]
    print(find_total_paths(matrix))
