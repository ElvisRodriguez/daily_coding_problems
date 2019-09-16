'''
This problem was asked by YouTube.

Write a program that computes the length of the longest common subsequence of
 three given strings.

For example, given "epidemiologist", "refrigeration", and
 "supercalifragilisticexpialodocious", it should return 5,
  since the longest common subsequence is "eieio".
'''

# Time Complexity: O(nm)
# - n is the size of first_string
# - m is the size of second_string
# Space Complexity: O(n)
# - n is the size of second_string


def find_common_chars_slow(first_string, second_string):
    # Make a mutable representation of the second string
    # We'll be deleting characters, so we need a mutable container
    second_string_list = list(second_string)
    # Store the longest common subsequence amongst the two strings
    common_chars = []
    for char in first_string:
        if char in second_string_list:
            common_chars.append(char)
            # Grab the index of the char in the second string
            # so that we can resize second_string_list
            index = second_string_list.index(char)
            # We slice the string list so that we don't have false
            # multiples of characters
            second_string_list = second_string_list[index+1:]
    return ''.join(common_chars)


# Time Complexity: O(nm)
# - n is the size of the first_string
# - m is the average number of indices lower than the current max_index
# Space Complexity: O(n)
# - n is the size of second_string
# A note about the m in the runtime:
#   Typically this method can be considered linear in runtime, if the strings
#   represent real words, however, the runtime approaches O(n^2) as the strings
#   become very large (think millions of characters long)
def find_common_chars(first_string, second_string):
    # Keep track of all characters and their indices in second_string
    # This allows for lookups in constant time
    # We'll use the indices to make sure we avoid false multiple characters
    character_map = {}
    for i in range(len(second_string)):
        char = second_string[i]
        if char in character_map:
            character_map[char].append(i)
        else:
            character_map[char] = [i]
    common_chars = []
    # Keeps track of where we are in second_string, again, to avoid
    # false multiple characters
    max_index = 0
    for char in first_string:
        if char in character_map:
            # start at -1 so that we don't accidentally omit entries
            index = -1
            # We want to throw out indices that we've past with max_index
            # This will keep a count of indices to discard
            new_starting_index = 0
            for i in character_map[char]:
                if i > max_index:
                    index = i
                    # no need to check other indices if we've found an index
                    # greater than max_index
                    break
                else:
                    new_starting_index += 1
            if index > max_index:
                # Jump to the next index in second_string
                max_index = index
                # Remove all index values lower than max_index
                # We're not interested in these indices as they represent
                # characters not in sequence
                character_map[char] = character_map[char][new_starting_index:]
                if len(character_map[char]) == 0:
                    # Remove a character key if it has no indices left
                    # This is equivalent to no longer seeing this character in
                    # the current portion of the string
                    del character_map[char]
                common_chars.append(char)
    return ''.join(common_chars)


def longest_common_subsequence(strings):
    # Find the longest common substring between the first two strings
    common_substring = find_common_chars(strings[0], strings[1])
    # Check if the third string contains the same common substring
    # that was found, or a shorter substring.
    longest_common_substring = find_common_chars(common_substring, strings[2])
    return len(longest_common_substring)


if __name__ == '__main__':
    strings = [
        'epidemiologist', 'refrigeration', 'supercalifragilisticexpialodocious'
    ]
    print(longest_common_subsequence(strings))
