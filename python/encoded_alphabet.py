'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not
allowed.
'''


def take_pieces(string, size):
    result = []
    string_list = list(string)
    while string_list:
        result.append(''.join(string_list[:size]))
        string_list = string_list[size:]
    return result


def combinations(numeric_string, result=[], partion=1):
    if partion == len(numeric_string):
        result.append(numeric_string.split())
        return result
    else:
        pass


if __name__ == '__main__':
    print(take_pieces('11334', 5))
