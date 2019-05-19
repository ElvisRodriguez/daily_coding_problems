'''
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible
reconstruction, return any of them. If there is no possible reconstruction,
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
['bedbath', 'and', 'beyond'].
'''
# Substrings? Partial ones to be exact


def create_sentence(words, string):
    sentence = []
    for word in words:
        if word in string:
            sentence.append(word)
            string = string[len(word) - 1:]
    return sentence


if __name__ == '__main__':
    words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
    string = 'bedbathandbeyond'
    print(create_sentence(words, string))
