#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
import datetime
class Jeopardy_Board:
    '''Class that represents a board'''
    def __init__(self, rows = 5, columns = 6):
        '''Initializes a 2D board'''
        self.rows = rows
        self.columns = columns
        self.board = self.make_board()
        self.values = {0: 200, 1: 400, 2: 600, 3: 800, 4: 1000}

    def make_board(self) -> [[bool]]:
        '''Makes a 2D list with each value initialized to 0'''
        board = []
        for i in range(self.rows):
            board.append([])
            for j in range(self.columns):
                board[-1].append(0)
        return board

    def get_score(self, double: bool = False) -> int:
        '''Calculates the current score'''
        total = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j]:
                    if double:
                        total += 2 * self.values[i]
                    else:
                        total += self.values[i]
        return total

    def show_board(self) -> None:
        '''Shows the current board'''
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.board[i][j], end = ' ')
            print()



