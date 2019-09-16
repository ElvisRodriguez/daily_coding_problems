'''
This problem was asked by Microsoft.

Given a string and a pattern,
 find the starting indices of all occurrences of the pattern in the string.
For example, given the string "abracadabra" and the pattern "abr",
 you should return [0, 7].
'''


def find_all_starting_pattern_positions(string, pattern):
    '''
    Time Complexity: O(n) where n is the length of string
    Space Complexity: O(n) where n is the number of pattern positions found
    '''
    positions = []
    # For every index, check the string slice from that index up to the index
    #  plus the length of pattern is equal to the given pattern
    for i in range(len(string) - len(pattern)):
        substring = string[i:i+len(pattern)]
        if substring == pattern:
            positions.append(i)
    return positions


if __name__ == '__main__':
    string = 'abracadabra'
    pattern = 'abr'
    print(find_all_starting_pattern_positions(string, pattern))
