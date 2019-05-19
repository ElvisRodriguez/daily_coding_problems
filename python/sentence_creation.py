'''
This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple lines such
that each line has a length of k or less. You must break it up so that words
don't break across lines. Each line has to have the maximum possible amount of
words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that
there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog"
and k = 10, you should return: ["the quick", "brown fox", "jumps over",
"the lazy", "dog"]. No string in the list has a length of more than 10.
'''


def create_sentence(string, k):
    words = string.split(' ')
    sentence = []
    line = ''
    for word in words:
        if len(line) + len(word) <= k:
            line += word + ' '
        else:
            line = line.strip()
            sentence.append(line)
            line = word + ' '
    sentence.append(line.strip())
    return sentence


if __name__ == '__main__':
    string = 'the quick brown fox jumps over the lazy dog'
    k = 10
    print(create_sentence(string, k))
