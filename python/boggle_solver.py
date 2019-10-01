'''
This problem was asked by Facebook.

Boggle is a game played on a 4 x 4 grid of letters.
The goal is to find as many words as possible that can be formed by a sequence
 of adjacent letters in the grid, using each cell at most once.
Given a game board and a dictionary of valid words, implement a Boggle solver.
'''


def check_for_valid_words(string, valid_words):
    words_found = []
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            possible_word = string[i:j+1]
            if possible_word in valid_words:
                words_found.append(possible_word)
            if possible_word[::-1] in valid_words:
                words_found.append(possible_word[::-1])
    return words_found


def valid_position(board, row, col):
    if row < 0 or col < 0:
        return False
    try:
        board[row][col]
        return True
    except IndexError:
        return False


def build_letter_strings(board):
    letter_strings = []
    # add each row
    letter_strings.extend(board)
    # add each column
    for i in range(len(board[0])):
        column = [row[i] for row in board]
        letter_strings.append(column)
    # add each diagonal
    starting_positions = []
    for i in range(len(board[0]) - 1):
        starting_positions.append((0, i))
        starting_positions.append((i, 0))
    for position in starting_positions:
        letter_string = []
        while valid_position(board, row, col):
            letter_string.append(board[row][col])
            row += 1
            col += 1
        letter_strings.append(letter_string)
    return letter_strings


def solve_boggle_board(board, valid_words):
    letter_strings = build_letter_strings(board)
    words_found = []
    for string in letter_strings:
        words_found.extend(check_for_valid_words(string, valid_words))
    return words_found
