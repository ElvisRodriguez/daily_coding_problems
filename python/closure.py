'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and
last element of that pair. For example, car(cons(3, 4)) returns 3, and
cdr(cons(3, 4)) returns 4.

Given this implementation of cons:
'''


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


'''
Implement car and cdr.
'''


def car(pair):
    return pair.__closure__[0].cell_contents


def cdr(pair):
    return pair.__closure__[1].cell_contents


if __name__ == '__main__':
    # Can't say I like this question, really requires in depth knowledge of
    # python and not really data structures/algorithms.
    # But hey, I learned a new thing at least!
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))
