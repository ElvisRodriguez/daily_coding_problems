'''
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for
one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13],
return 19.

Do this in O(N) time and O(1) space.
'''

# Runtime: O(n), Space Complexity: O(n)


def find_outlier(numbers):
    number_log = {}
    for number in numbers:
        if number in number_log:
            number_log[number] += 1
        else:
            number_log[number] = 1
    for number in numbers:
        if number_log[number] == 1:
            return number

# Runtime: O(n), Space Complexity: O(1)


def find_outlier2(numbers):
    pass


if __name__ == '__main__':
    print(find_outlier([6, 1, 3, 3, 3, 6, 6]))
    print(find_outlier([13, 19, 13, 13]))
