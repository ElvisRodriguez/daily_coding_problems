'''
This problem was asked by Google.

You're given a string consisting solely of (, ), and *.
* can represent either a (, ), or an empty string.
Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
'''


def is_balanced(paren_string):
    counter = 0
    for char in paren_string:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
        if counter < 0:
            return False
    return counter == 0


def new_parens(paren_string, token):
    parens = []
    used = False
    for char in paren_string:
        if char == '*' and not used:
            parens.append(token)
        else:
            parens.append(char)
    return parens


def check_valid_parens(paren_strings):
    new_strings = []
    bools = []
    for paren_string in paren_strings:
        if '*' in paren_string:
            modded_string = paren_string
            i = modded_string.index('*')
            temp = new_parens(paren_string, '(')
            new_strings.append(temp)
            temp = new_parens(paren_string, ')')
            new_strings.append(temp)
            modded_string.pop(i)
            new_strings.append(modded_string)
        else:
            bools.append(is_balanced(paren_string))
    if True in bools:
        return True
    if not new_strings:
        return False
    return check_valid_parens(new_strings)


value = [list('***)))')]
print(check_valid_parens(value))
