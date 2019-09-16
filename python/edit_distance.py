'''
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character
 insertions, deletions, and substitutions required to change one string to the
 other.
For example, the edit distance between “kitten” and “sitting” is three:
 substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
'''


def compute_edit_distance(first_string, second_string):
    '''
    Time Complexity: O(n) where n is the length of the shortest string
    Space Complexity: O(1)
    '''
    # Check for the edge case where a given string is a substring of the other
    # If so, because the substring may appear anywhere in the string, we can't
    #  use the algorithm below to compute the edit distance
    # In this case, the edit distance is merely the difference in string lengths
    if first_string in second_string:
        return len(second_string) - len(first_string)
    if second_string in first_string:
        return len(first_string) - len(second_string)
    first_length = len(first_string)
    second_length = len(second_string)
    # We want to iterate up to the length of the shortest string
    # We add the difference in lengths to the edit distance as that number
    #  represents the amount of characters that must be inserted/deleted
    if first_length < second_length:
        shortest_length = first_length
        difference = second_length - first_length
    else:
        shortest_length = second_length
        difference = first_length - second_length
    edit_distance = 0
    for i in range(shortest_length):
        # Count every instance of differing characters, as those characters
        #  need to be substituted
        if first_string[i] != second_string[i]:
            edit_distance += 1
    return edit_distance + difference


if __name__ == '__main__':
    print(compute_edit_distance('kitten', 'sitting'))
    print(compute_edit_distance('car', 'racecar'))
