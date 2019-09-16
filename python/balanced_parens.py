'''
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return
whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

# Time Complexity: O(n) where n is the length of the brackets string
# Space Complexity: O(n) where n is up to the length of the brackets string


def is_balanced(brackets):
    # Create a stack to store opening characters, popping their compliments
    stack = []
    # Keep a map of all the parenthesis/braces/brackets as keys with their
    # complimenting characters as values
    compliments = {}
    for open, close in [('{', '}'), ('(', ')'), ('[', ']')]:
        compliments[open] = close
        compliments[close] = open
    for char in brackets:
        # Simply add an opening character to the stack
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            # If our stack is empty when we encounter a closing character, then
            #  the string is unbalanced.
            # If the stack is not empty, but the top character is not the
            #  current character's compliment, the string is unbalanced
            if stack is None or stack[-1] != compliments[char]:
                return False
            else:
                stack.pop(-1)
    # If our string had more opening characters than closing, the stack would
    # not be empty, meaning the string is unbalanced.
    return len(stack) == 0


if __name__ == '__main__':
    strings = ['([])[]({})', '([)]', '((()']
    for string in strings:
        print(is_balanced(string))
