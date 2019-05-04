'''
This problem was asked by Google.

On our special chessboard, two bishops attack each other if they share the same
diagonal. This includes bishops that have another bishop located between them,
i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M
chessboard. Write a function to count the number of pairs of bishops that
attack each other. The ordering of the pair doesn't matter: (1, 2) is
considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other, as well as
bishops 3 and 4.
'''


def are_diagonal(pairA, pairB):
    if pairA[0] == pairA[1]:
        if pairB[0] == pairB[1]:
            return True
    if pairA[0] < pairB[0]:
        row = pairA[0]
        col = pairA[1]
        while row < pairB[0] + 1:
            if row == pairB[0] and col == pairB[1]:
                return True
            row += 1
            col -= 1
    if pairA[0] > pairB[0]:
        row = pairA[0]
        col = pairA[1]
        while row > pairB[0] - 1:
            if row == pairB[0] and col == pairB[1]:
                return True
            row -= 1
            col += 1
    return False


def check_bishops(m, coordinates):
    interactions = []
    attacks = 0
    for pairA in range(len(coordinates)):
        for pairB in range(1, len(coordinates)):
            if are_diagonal(coordinates[pairA], coordinates[pairB]) and coordinates[pairA] != coordinates[pairB]:
                if tuple(sorted([coordinates[pairA], coordinates[pairB]])) not in interactions:
                    attacks += 1
                    interactions.append(
                        tuple(sorted([coordinates[pairA], coordinates[pairB]])))
    return attacks


if __name__ == '__main__':
    m = 5
    coordinates = [
        (0, 0),
        (1, 2),
        (2, 2),
        (4, 0)
    ]
    print(check_bishops(m, coordinates))
