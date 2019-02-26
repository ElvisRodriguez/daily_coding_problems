'''
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of
all possible query strings, return all strings in the set that have s as a
prefix.

For example, given the query string de and the set of strings [dog, deer, deal],
return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to
speed up queries.
'''


def autocomplete(query_string, string_list):
    for i in range(len(query_string)):
        for string in string_list:
            try:
                if query_string[i] != string[i]:
                    string_list.pop(string_list.index(string))
            except IndexError:
                string_list.pop(string_list.index(string))
    return string_list


if __name__ == '__main__':
    print(autocomplete('de', ['dog', 'deer', 'deal']))
