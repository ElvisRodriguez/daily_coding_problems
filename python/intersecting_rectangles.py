'''
This problem was asked by Google.

Given two rectangles on a 2D graph, return the area of their intersection.
If the rectangles don't intersect, return 0.

For example, given the following rectangles:
{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.
'''


def generate_rectangle(top_left, dimensions):
    rectangle = {
        'top_left': top_left,
        'dimensions': dimensions
    }
    return rectangle


def generate_all_rectangle_points(rectangle):
    points = []
    x, y = rectangle['dimensions']
    starting_point = rectangle['top_left']
    for i in range(x):
        for j in range(y):
            point = (starting_point[0] + i, starting_point[1] - j)
            points.append(point)
    return points


def find_area(rectangle_a, rectangle_b):
    a_points = generate_all_rectangle_points(rectangle_a)
    b_points = generate_all_rectangle_points(rectangle_b)
    area = 0
    for point in a_points:
        if point in b_points:
            area += 1
    return area


if __name__ == '__main__':
    rectangle_a = generate_rectangle((1, 4), (3, 3))
    rectangle_b = generate_rectangle((0, 5), (4, 3))
    area = find_area(rectangle_a, rectangle_b)
    print(area)
