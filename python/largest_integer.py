'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Given a list of numbers, create
 an algorithm that arranges them in order to form the largest possible integer.
For example, given [10, 7, 76, 415], you should return 77641510.
'''

import collections


def generate_largest_integer(integers):
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    rearranged_integers = []
    while integers:
        largest_first_digit = int(str(integers[0])[0])
        next_integer = integers[0]
        index = 0
        for i in range(len(integers)):
            integer = integers[i]
            first_digit = int(str(integer)[0])
            if first_digit > largest_first_digit:
                largest_first_digit = first_digit
                next_integer = integer
                index = i
        integers.pop(index)
        rearranged_integers.append(next_integer)
    return int(''.join([str(integer) for integer in rearranged_integers]))


if __name__ == '__main__':
    integers = [10, 7, 76, 415]
    print(generate_largest_integer(integers))
