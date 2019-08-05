'''
This problem was asked by Google.

Given a string, return the first recurring character in it,
or null if there is no recurring character.

For example, given the string "acbbac", return "b".
Given the string "abcdef", return null.
'''


def first_recurring(string):
    letters = {}
    is_recurring = False
    for char in string:
        try:
            letters[char] += 1
            is_recurring = True
            return char
        except KeyError:
            letters[char] = 1
    if not is_recurring:
        return None


if __name__ == '__main__':
    strings = ['acbbac', 'abcdef']
    for string in strings:
        print(string, ':', first_recurring(string))
