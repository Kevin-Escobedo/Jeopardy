#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com

class JeopardyBoard:
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

    def update_question(self, row:int, column:int):
        if self.board[row][column] == None:
            self.board[row][column] == True
            
        elif self.board[row][column] == True:
            self.board[row][column] == False

        elif self.board[row][column] == False:
            self.board[row][column] = None

if __name__ == "__main__":
    j = JeopardyBoard()
    #j.show_board()
    print(j.get_score())
