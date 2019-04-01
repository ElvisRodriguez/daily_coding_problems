'''
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''

def rgb_sort(rgb_values):
    position = 0
    for i in range(len(rgb_values)):
        if rgb_values[i] == 'R':
            rgb_values[i], rgb_values[position] = rgb_values[position], rgb_values[i]
            position += 1
    position = -1
    for i in range(len(rgb_values) - 1, -1, -1):
        if rgb_values[i] == 'B':
            rgb_values[i], rgb_values[position], = rgb_values[position], rgb_values[i]
            position -= 1


if __name__ == '__main__':
    test_values = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    rgb_sort(test_values)
    print(test_values)
