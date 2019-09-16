'''
This problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding for its columns:
 "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id.
 For example, given 1, return "A". Given 27, return "AA".
'''


def compute_column_id(column_number):
    '''
    Time Complexity: O(1)
    Space Complexity: O(1)
    '''
    # Decrease column number to work with 0-indexed array
    column_number -= 1
    # Generate an uppercase alphabet using corresponding ascii values
    uppercase_alphabet = [chr(i).upper() for i in range(97, 123)]
    # Calculate how many times a character has to be repeated
    repetitions = column_number // len(uppercase_alphabet)
    # Find the corresponding index of column numbers greater than 26
    index = column_number % len(uppercase_alphabet)
    return uppercase_alphabet[index] + (uppercase_alphabet[index] * repetitions)
