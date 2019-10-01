'''
This problem was asked by Airbnb.

You come across a dictionary of sorted words in a language
 you've never seen before.
Write a program that returns the correct order of letters in this language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'],
 you should return ['x', 'z', 'w', 'y'].
'''

import collections


def find_ordered_letters(words):
    '''
    Time Complexity: O(nmk)
        - n is the size of the words array
        - m is the average word size
        - k is the size of the letters stack
    Space Complexity: O(n)
    '''
    letters = collections.deque()
    temporary_letters = collections.deque()
    visited = set()
    for i in range(len(words) - 1):
        first_word = words[i]
        second_word = words[i+1]
        size = len(first_word) if len(first_word) < len(second_word) else len(second_word)
        for j in range(size):
            first_char = first_word[j]
            second_char = second_word[j]
            if first_char != second_char:
                if first_char not in visited and second_char not in visited:
                    letters.appendleft(second_char)
                    letters.appendleft(first_char)
                    visited.add(first_char)
                    visited.add(second_char)
                elif first_char in visited and second_char not in visited:
                    while letters[0] != first_char:
                        temporary_letters.appendleft(letters.popleft())
                    temporary_letters.appendleft(letters.popleft())
                    letters.appendleft(second_char)
                    while temporary_letters:
                        letters.appendleft(temporary_letters.popleft())
                    visited.add(second_char)
                elif first_char not in visited and second_char in visited:
                    while letters[0] != second_char:
                        temporary_letters.appendleft(letters.popleft())
                    letters.appendleft(first_char)
                    while temporary_letters:
                        letters.appendleft(temporary_letters.popleft())
                    visited.add(first_char)
                break
    return list(letters)


if __name__ == '__main__':
    word_lists = [
        ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'],
        ['abc', 'abd', 'bad', 'cab', 'dab']
    ]
    for words in word_lists:
        print(find_ordered_letters(words))
