'''
This problem was asked by Zillow.

Let's define a "sevenish" number to be one which is either a power of 7,
 or the sum of unique powers of 7.
 The first few sevenish numbers are 1, 7, 8, 49, and so on.
Create an algorithm to find the nth sevenish number.
'''


def is_power_of_7(n):
    if n == 1:
        return True
    copy = n
    while copy > 0:
        copy /= 7
        if not copy.is_integer():
            return False
        if copy == 1:
            return True


def nth_sevenish(n):
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    sevenish_numbers = []
    powers_of_seven = []
    power = 0
    while len(sevenish_numbers) < n:
        new_number = 7 ** power
        sevenish_numbers.append(new_number)
        powers_of_seven.append(new_number)
        for power_of_seven in powers_of_seven:
            if power_of_seven != new_number:
                sevenish_numbers.append(power_of_seven + new_number)
        power += 1
    return sevenish_numbers[n-1]


if __name__ == '__main__':
    for i in range(10):
        print(nth_sevenish(i+1))
