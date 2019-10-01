'''
This problem was asked by Google.

Given an array of elements,
 return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1],
 return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1]
'''


def is_distinct(subarray):
    return len(subarray) == len(set(subarray))


def longest_distinct_subarray(array):
    start = 0
    end = 1
    longest_subarray = []
    while end != len(array) + 1:
        subarray = array[start:end]
        if is_distinct(subarray) and len(subarray) > len(longest_subarray):
            longest_subarray = subarray
        while not is_distinct(subarray):
            start += 1
            if start == end:
                break
            subarray = array[start:end]
        end += 1
    return len(longest_subarray)


if __name__ == '__main__':
    array = [5, 1, 3, 5, 2, 3, 4, 1]
    print(longest_distinct_subarray(array))
