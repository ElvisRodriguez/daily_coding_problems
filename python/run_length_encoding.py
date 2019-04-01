'''
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic
idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded as
"4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.
'''


def run_length_encode(string):
    result = []
    temp = []
    for char in string:
        if temp and char != temp[-1]:
            result.append(str(len(temp)) + temp[-1])
            temp = []
            temp.append(char)
        else:
            temp.append(char)
    result.append(str(len(temp)) + temp[-1])
    return ''.join(result)


def run_length_decode(string):
    result = []
    temp = 0
    for i in range(len(string)):
        if i % 2 == 0:
            temp = int(string[i])
        else:
            result.append(temp * string[i])
    return ''.join(result)


if __name__ == '__main__':
    print(run_length_encode('AAAABBBCCDAA'))
    print(run_length_decode(run_length_encode('AAAABBBCCDAA')))
