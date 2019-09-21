'''
This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run of 1s in
 its binary representation.

For example, given 156, you should return 3.
'''


def longest_consecutive_ones(n):
    '''
    Time Complexity: O(log n)
    Space Complexity: O(1)
    '''
    longest = 0
    count = 0
    while n > 0:
        # If we encounter a 0, check our current count of ones against the
        # longest count recorded, updating longest if count is larger
        if n % 2 == 0:
            if count > longest:
                longest = count
            count = 0
        else:
            # Add the 1 we've seen to our current count
            count += 1
        n //= 2
    return longest


if __name__ == '__main__':
    print(longest_consecutive_ones(156))
