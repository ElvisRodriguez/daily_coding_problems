'''
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get:
[10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)
    Do this in O(n) time and O(k) space.
    You can modify the input array in-place and you do not need to store the
    results. You can simply print them out as you compute them.
'''


def partial_max(nums, k):
    i = 0
    while i < len(nums) and k <= len(nums):
        print(max(nums[i:k]))
        i += 1
        k += 1


def partial_max2(nums, k):
    pass


if __name__ == '__main__':
    partial_max(nums=[10, 5, 2, 7, 8, 7], k=3)
