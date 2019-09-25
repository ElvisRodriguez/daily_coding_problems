'''
This problem was asked by Square.

In front of you is a row of N coins, with values v1, v1, ..., vn.

You are asked to play the following game.
You and an opponent take turns choosing either the first or last coin
from the row, removing it from the row, and receiving the value of the coin.

Write a program that returns the maximum amount of money you can
win with certainty, if you move first, assuming your opponent plays optimally.

'''

def max_coins(coins):
    result = 0
    player_turn = True
    while coins:
        if player_turn:
            player_turn = not player_turn
            if coins[0] > coins[-1]:
                result += coins[0]
                coins.pop(0)
            else:
                result += coins[-1]
                coins.pop(-1)
        else:
            player_turn = not player_turn
            if coins[0] > coins[-1]:
                coins.pop(0)
            else:
                coins.pop(-1)
    return result


if __name__ == '__main__':
    coins = [3, 4, 2, 2, 6, 7, 7]
    print(max_coins(coins))