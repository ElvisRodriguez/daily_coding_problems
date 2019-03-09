'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
should give 3.

You can modify the input array in-place.
'''


def lowest_positive(nums):
    lowest = nums[0]
    j = 0
    # Find the first number greater than 0
    for i in range(len(nums)):
        if nums[i] > 0:
            lowest = nums[i]
            j = i
            break
    # Use the number found to get the lowest positive number in the array
    for i in range(j, len(nums)):
        # 1 is the lowest number we care about, we can stop if we find it
        if nums[i] == 1:
            lowest = 1
            break
        if nums[i] < lowest and nums[i] > 0:
            lowest = nums[i]
    # Increment 'lowest' until the missing positive number is found
    while True:
        if lowest in nums:
            lowest += 1
        else:
            return lowest


if __name__ == '__main__':
    print(lowest_positive([3, 4, -1, 1]))
    print(lowest_positive([1, 2, 0]))
