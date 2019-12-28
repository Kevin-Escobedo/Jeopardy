#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
from name_files import get_file_name
from datetime import datetime

class JeopardyBoard:
    '''Class that represents a board'''
    def __init__(self, rows = 5, columns = 6, double = False):
        '''Initializes a 2D board'''
        self.rows = rows
        self.columns = columns
        self.score = 0
        self.board = [[None] * self.columns for i in range(self.rows)]
        self.values = {0: 200, 1: 400, 2: 600, 3: 800, 4: 1000}
        self.double = double
        self.d_values = {0: 400, 1: 800, 2: 1200, 3: 1600, 4: 2000}

    def make_board(self) -> [[bool]]:
        '''Makes a 2D list with each value initialized to 0'''
        board = []
        for i in range(self.rows):
            board.append([])
            for j in range(self.columns):
                board[-1].append(None)
        return board

    def get_score(self) -> int:
        '''Calculates the current score'''
        total = self.score

        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] == True:
                    if self.double:
                        total += self.d_values[i]
                    else:
                        total += self.values[i]

                if self.board[i][j] == False:
                    if self.double:
                        total -= self.d_values[i]
                    else:
                        total -= self.values[i]
        return total

    def show_board(self) -> None:
        '''Shows the current board'''
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.board[i][j], end = ' ')
            print()

    def export_board(self) -> None:
        '''Exports the board into a file'''
        now = datetime.now()
        file_name = "jeopardy_board-{}-{}-{}.txt".format(now.month, now.day, now.year)
        if self.double:
            file_name = "double_{}".format(file_name)
        file = open(get_file_name(file_name), "w")
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] == None:
                    file.write(" 0 ")
                elif self.board[i][j] == True:
                    file.write(" + ")
                else:
                    file.write(" - ")
            file.write("\n")
        file.write("Total Score: {}".format(self.get_score()))
        file.flush()
        file.close()

    def import_board(self, file_name:str):
        '''Reads a board from an exported board file'''
        try:
            file = open(file_name, "r")
            info = file.readlines()
            file.close()
            info = info[:-1]
            for i, data in enumerate(info):
                data = data.strip().split()
                for j, score in enumerate(data):
                    if score == "0":
                        self.board[i][j] = None
                    elif score == "+":
                        self.board[i][j] = True
                    else:
                        self.board[i][j] = False
        except FileNotFoundError:
            pass

    def final_jeopardy(self, wager:int = 0, correct:bool = 0):
        '''Handles Final Jeopardy scoring'''
        if correct:
            score = self.get_score() + wager
        else:
            score = self.get_score() - wager
        return score

    def reset_board(self):
        self.score += int(self.get_score()/2)
        self.board = self.make_board()

if __name__ == "__main__":
    j = JeopardyBoard()
