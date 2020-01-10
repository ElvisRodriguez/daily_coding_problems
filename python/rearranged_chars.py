'''
This problem was asked by IBM.

Given a string with repeated characters,
 rearrange the string so that no two adjacent characters are the same.
If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
'''


def rearrange_chars(string):
    count_of_each_char = {}
    for char in string:
        if char in count_of_each_char:
            count_of_each_char[char] += 1
        else:
            count_of_each_char[char] = 1
    unique_chars = list(count_of_each_char.keys())
    new_string = ['']
    index = 0
    while unique_chars:
        char = unique_chars[index]
        if count_of_each_char[char] > 0:
            if char == new_string[-1]:
                return None
            new_string.append(char)
            count_of_each_char[char] -= 1
            index += 1
            index %= len(unique_chars)
        else:
            unique_chars.pop(index)
            if len(unique_chars) == 0:
                break
            index %= len(unique_chars)
    return ''.join(new_string)


if __name__ == '__main__':
    strings = ['aaaabbc', 'aaab', 'a']
    for string in strings:
        print(rearrange_chars(string))
