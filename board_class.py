#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
from name_files import get_file_name
from datetime import datetime

class JeopardyBoard:
    '''Class that represents a board'''
    def __init__(self, rows = 5, columns = 6):
        '''Initializes a 2D board'''
        self.rows = rows
        self.columns = columns
        self.board = [[None] * self.columns for i in range(self.rows)]
        self.values = {0: 200, 1: 400, 2: 600, 3: 800, 4: 1000}

    def make_board(self) -> [[bool]]:
        '''Makes a 2D list with each value initialized to 0'''
        board = []
        for i in range(self.rows):
            board.append([])
            for j in range(self.columns):
                board[-1].append(None)
        return board

    def get_score(self, double: bool = False) -> int:
        '''Calculates the current score'''
        total = 0

        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] == True:
                    if double:
                        total += 2 * self.values[i]
                    else:
                        total += self.values[i]

                if self.board[i][j] == False:
                    if double:
                        total -= 2 * self.values[i]
                    else:
                        total -= self.values[i]
        return total

    def show_board(self) -> None:
        '''Shows the current board'''
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.board[i][j], end = ' ')
            print()

    def export_board(self, double:bool = False) -> None:
        '''Exports the board into a file'''
        now = datetime.now()
        file_name = "jeopardy_board-{}-{}-{}.bor".format(now.month, now.day, now.year)
        if double:
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
        if double:
            file.write("Total Score: {}".format(self.get_score(True)))
        else:
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

if __name__ == "__main__":
    j = JeopardyBoard()
