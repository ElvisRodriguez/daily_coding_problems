'''
Given a 2-D matrix representing an image,
a location of a pixel in the screen and a color C,
replace the color of the given pixel and all adjacent same colored pixels with C

For example, given the following matrix, and location pixel of (2, 2),
and 'G' for green:

B B W
W W W
W W W
B B B

Becomes

B B G
G G G
G G G
B B B
'''


def pretty_print(matrix):
    output = []
    for row in matrix:
        output.append(''.join(row))
        output.append('\n')
    output.pop(-1)
    print(''.join(output))


def valid_direction(matrix, direction):
    if -1 in direction:
        return False
    x = direction[0]
    y = direction[1]
    try:
        point = matrix[x][y]
        return True
    except IndexError:
        return False


def compute_directions(matrix, point, symbol):
    x = point[0]
    y = point[1]
    directions = [(x+1, y), (x, y+1), (x-1, y), (x, y-1), (x+1, y+1), (x-1, y-1),
                  (x+1, y-1), (x-1, y+1)]
    valid_directions = []
    for direction in directions:
        if valid_direction(matrix, direction):
            if matrix[direction[0]][direction[1]] == symbol:
                valid_directions.append(direction)
    return valid_directions


def change_pixels(matrix, point, new_symbol):
    old_symbol = matrix[point[0]][point[1]]
    queue = [point]
    points_to_change = []
    visited = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            x = node[0]
            y = node[1]
            if matrix[x][y] == old_symbol:
                points_to_change.append(node)
                directions = compute_directions(matrix, node, old_symbol)
                queue.extend(directions)
    for point in points_to_change:
        x = point[0]
        y = point[1]
        matrix[x][y] = new_symbol
    return matrix


if __name__ == '__main__':
    matrix = [
        ['B', 'B', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['B', 'B', 'B']
    ]
    point = (2, 2)
    new_symbol = 'G'
    pretty_print(matrix)
    print('---------')
    pretty_print(change_pixels(matrix, point, new_symbol))
