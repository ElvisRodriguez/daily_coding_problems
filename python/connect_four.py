'''
This problem was asked by Salesforce.

Connect 4 is a game where opponents take turns dropping red or black discs into
a 7 x 6 vertically suspended grid.
The game ends either when one player creates a line of four consecutive discs
of their color (horizontally, vertically, or diagonally),
or when there are no more spots left in the grid.

Design and implement Connect 4.
'''

ROWS = 7
COLS = 6

class ConnectFour(object):
    def __init__(self):
        self.board = self.__create_board()
        self.current_plays = 0
        self.max_plays = ROWS * COLS
        self.possible_plays = ['R', 'B']
        self.winner_red = 'RRRR'
        self.winner_black = 'BBBB'

    def __create_board(self):
        '''
        Create a ROW x COL 2D array.
        '''
        grid = []
        for _ in range(ROWS):
            new_row = ['E' for _ in range(COLS)]
            grid.append(new_row)
        return grid

    def print_board(self):
        '''
        Prints self.board
        '''
        for row in self.board:
            print(row)

    def insert_disc(self, disc_color, column):
        '''
        Updates board at given position with disc_color
        '''
        if disc_color not in self.possible_pays:
            print('Must insert either a red or black disc')
            return False
        if column not in range(COLS):
            print('Invalid column')
            return False
        positon = [-1, column]
        for i in range(len(self.board)):
            row = self.board[i]
            if row[column] != 'E':
                position[0] = i - 1
                break
        if position[0] < 0:
            print('Column {col} is full'.format(col=column))
            return False
        row, col = position
        self.board[row][col] = disc_color
        self.current_plays += 1
        return True

    def __check_for_diagonal_winner(self):
        south_east_positions = [(3,0), (2,0), (1,0), (0,0), (0,1), (0,2)]
        north_east_positions = [(3,0), (4,0), (5,0), (6,0), (6,1), (6,2)]
        for position in south_east_positions:
            cells = []
            i, j = position
            while i < ROWS and j < COLS:
                cells.append(self.board[i][j])
                i += 1
                j += 1
            if self.winner_red in ''.join(cells):
                return 'RED HAS WON'
            if self.winner_black in ''.join(cells):
                return 'BLACK HAS WON'
        for position in north_east_positions:
            cells = []
            i, j = position
            while i >= 0 and j < COLS:
                cells.append(self.board[i][j])
                i -= 1
                j += 1
            if self.winner_red in ''.join(cells):
                return 'RED HAS WON'
            if self.winner_black in ''.join(cells):
                return 'BLACK HAS WON'
        return 'NO WINNER'


    def check_game_state(self):
        # Check for a horizontal winner.
        for row in self.board:
            if self.winner_red in ''.join(row):
                return 'RED HAS WON'
            if self.winner_black in ''.join(row):
                return 'BLACK HAS WON'
        # Check for a vertial winner.
        for i in range(COLS):
            segment = ''.join([row[i] for row in self.board])
            if self.winner_red in segment:
                return 'RED HAS WON'
            if self.winner_black in segment:
                return 'BLACK HAS WON'
        outcome = self.__check_for_diagonal_winner()
        if outcome == 'NO WINNER'  and self.current_plays == self.max_plays:
            return 'DRAW'
        if outcome == 'NO WINNER':
            return 'GAME NOT OVER'
        return outcome

def start_game():
    game = ConnectFour()
    red = 'R'
    black = 'B'
    red_player_turn = True
    print('Connect Four!\n\n')
    while True:
        game.print_board()
        if red_player_turn:
            print('Red\'s turn')
            column = str(input('Enter a column to place disc: '))
            if game.insert_disc(disc_color=red, column=column):
                red_player_turn = not red_player_turn
        else:
            print('Black\'s turn')
            column = str(input('Enter a column to place disc: '))
            if game.insert_disc(disc_colot=black, column=column):
                red_player_turn = not red_player_turn
        print('\n\tChecking game state...\n')
        game_state = game.check_game_state()
        if game_state in ['RED HAS WON', 'BLACK HAS WON', 'DRAW']:
            print(game_state)
            break


if __name__ == '__main__':
    start_game()
