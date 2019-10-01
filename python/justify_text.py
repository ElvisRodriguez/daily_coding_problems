'''
This problem was asked by Palantir.

Write an algorithm to justify text.
Given a sequence of words and an integer line length k,
 return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word.
Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces,
 if any, distributed starting from the left.

If you can only fit one word on a line,
 then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
 ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
  and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
'''


def fill_spaces(sentence, k):
    if len(''.join(sentence)) == k:
        return ''.join(sentence)
    indices = []
    for i in range(len(sentence)):
        if ' ' in sentence[i]:
            indices.append(i)
    index = 0
    while len(''.join(sentence)) < k:
        sentence[indices[index]] += ' '
        index += 1
        index %= len(indices)
    return ''.join(sentence)


def justify_text(words, k):
    '''
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    '''
    justified_text = []
    sentence = []
    space = ' '
    for word in words:
        if not sentence:
            sentence.append(word)
        else:
            size = len(''.join(sentence))
            if size + len(word) + 1 < k:
                sentence.append(space)
                sentence.append(word)
            elif size + len(word) == k:
                sentence.append(word)
            else:
                justified_text.append(fill_spaces(sentence, k))
                sentence = [word]
    justified_text.append(fill_spaces(sentence, k))
    return justified_text


if __name__ == '__main__':
    words = [
        'the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'
    ]
    justified_text = justify_text(words, k=16)
    print(justified_text)
    print([len(text) for text in justified_text])
