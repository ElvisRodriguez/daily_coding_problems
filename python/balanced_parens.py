'''
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return
whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''


def is_balanced(brackets):
    stack = []
    compliments = {}
    for open, close in [('{', '}'), ('(', ')'), ('[', ']')]:
        compliments[open] = close
        compliments[close] = open
    for char in brackets:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if stack is None:
                return False
