'''
This problem was asked by Google.

Given a string, return the first recurring character in it,
or null if there is no recurring character.

For example, given the string "acbbac", return "b".
Given the string "abcdef", return null.
'''


def first_recurring(string):
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    letters = set()
    for char in string:
        if char in letters:
            return char
        letters.add(char)
    return None


if __name__ == '__main__':
    strings = ['acbbac', 'abcdef']
    for string in strings:
        print(string, ':', first_recurring(string))
