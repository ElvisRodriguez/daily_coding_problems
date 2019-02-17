'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i 
of the new array is the product of all the numbers in the original array except
the one at i.

For example, if our input was [1,2,3,4,5], the expected output would be,
[120,60,40,30,24].
If our input was [3,2,1], the expected output would be [2,3,6].

Follow-up: What if you can't use division?
'''

#Runtime: O(n) where n is the size of the array.
def product_swap(array):
    #Find product total of array
    product = 1
    for value in array:
        product *= value
    #Reassign each value it's new value by dividing the product total by
    #the original value
    for i in range(len(array)):
        array[i] = product // array[i]
    return array

#Since division is just repeated subtraction, we can acheive the same result
#as the method above using a helper method.

#Runtime: O(n) where n is the dividend divided by the divisor
def divide(dividend, divisor):
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return quotient

#Now we can implement the same solution as above using our new helper method.

#Runtime: O(nm) where n is the size of the array and m is a variable, dependent
#on the inputs given to the divide helper method
def product_swap_no_division(array):
    product = 1
    for value in array:
        product *= value
    for i in range(len(array)):
        array[i] = divide(product, array[i])
    return array


if __name__ == '__main__':
    #Testing first solution with examples given.
    assert(product_swap([1,2,3,4,5]) == [120,60,40,30,24])
    assert(product_swap([3,2,1]) == [2,3,6])

    #Testing second solution with examples given.
    assert(product_swap_no_division([1,2,3,4,5]) == [120,60,40,30,24])
    assert(product_swap_no_division([1,2,3,4,5]) == [120,60,40,30,24])
    print('Tests Passed')
