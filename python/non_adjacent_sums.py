'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def non_adjacent_sum(numbers):
    even_sum = 0
    odd_sum = 0
    for i in range(len(numbers)):
        if numbers[i] > 0:
            if i % 2 == 0:
                even_sum += numbers[i]
            else:
                odd_sum += numbers[i]
    if even_sum > odd_sum:
        return even_sum
    else:
        return odd_sum
