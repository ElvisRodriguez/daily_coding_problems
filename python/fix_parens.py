'''
This problem was asked by Facebook.

Given a string of parentheses,
 find the balanced string that can be produced from it using the minimum
 number of insertions and deletions.

If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(",
 you could return "()()()()".
'''

# Runtime: O(n) where n is the size of the input string.


def fix_parens(string):
    index = 0
    # Keep track of the current parentheses substring.
    left_parens = []
    right_parens = []
    # Holds all parentheses substrings that have been balanced.
    new_parens = []
    # Sentinal for avoiding an out of bounds array error.
    string_end = False
    while index < len(string):
        # Build a substring of all left parentheses
        while string[index] == '(':
            left_parens.append(string[index])
            index += 1
            if index == len(string):
                string_end = True
                break
        # Build a substring of all right parentheses
        if not string_end:
            while string[index] == ')':
                right_parens.append(string[index])
                index += 1
                if index == len(string):
                    break
        # Balance whichever substring has less parentheses
        if len(left_parens) > len(right_parens):
            diff = len(left_parens) - len(right_parens)
            right_parens.append(')' * diff)
        elif len(left_parens) < len(right_parens):
            diff = len(right_parens) - len(left_parens)
            left_parens.append('(' * diff)
        # Add our newly balanced substrings to the result array
        new_parens.extend(left_parens)
        new_parens.extend(right_parens)
        # Reset our temporary substring container
        left_parens = []
        right_parens = []
    return ''.join(new_parens)


if __name__ == '__main__':
    unbalanced_parens = ['(()', '))()(', ')))))', '((((', '(())', '()()']
    for paren in unbalanced_parens:
        print(fix_parens(paren))
