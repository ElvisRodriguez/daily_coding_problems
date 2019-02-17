'''
Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

Assumptions: cannot use the same value twice, i.e. given [4, 5, 6, 7] and
             k of 8, it is not true to say 4 and 4 make this true.
'''

#Runtime: O(n) where n is the size of the number array.
def two_sum(nums, k):
    #Storing each number in a hash table will allow for O(1) lookup, meaning we
    #only need to iterate through the number array once.
    numbers = {}
    for i in range(len(nums)):
        difference = k - nums[i]
        if difference in numbers:
            return True
        else:
            numbers[nums[i]] = i
    return False

if __name__ == '__main__':
    #Testing example arrays and edge case
    nums = [[10,15,3,7], [2,7,4,4], [2,7,4]]
    k_values = [17,8,8]
    for i in range(len(k_values)):
        print('Given {nums} and k of {k}:'.format(nums=nums[i], k=k_values[i]))
        print('Result is {result}'.format(
            result=two_sum(nums[i], k_values[i])))
