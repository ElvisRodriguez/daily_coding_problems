'''
This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome.
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome.
Do not convert the integer into a string.
'''


def is_palindrome(integer):
    numbers = []
    while integer > 10:
        numbers.append(integer % 10)
        integer //= 10
    numbers.append(integer)
    return numbers == numbers[::-1]


if __name__ == '__main__':
    integers = [121, 888, 678]
    for integer in integers:
        print(is_palindrome(integer))
