#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
import tkinter
import sys
import os
from tkinter import filedialog
from tkinter import messagebox
from board_class import JeopardyBoard
    
class BoardGUI:
    def __init__(self, height = 336, width = 648):
        '''GUI constructor'''
        self.root_window = tkinter.Tk()
        self.height = height
        self.width = width
        self.button_width = 14
        self.button_height = 3
        self.root_window.geometry("{}x{}".format(self.width, self.height))
        self.root_window.iconbitmap(self.resource_path("jeopardy.ico"))
        self.root_window.title("Jeopardy Board")
        self.root_window.resizable(False, False)
        self.score = tkinter.StringVar()
        self.show_score = tkinter.Label(self.root_window, textvariable = self.score, height = self.button_height, width = self.button_width)
        self.game = JeopardyBoard()
        self.score.set(str(self.game.get_score()))

        self.correct = "#33FF3C"
        self.blank = "#F0F0ED"
        self.wrong = "#F03320"

        self.double_button = tkinter.Button(self.root_window, text = "Double", command = self.invert_double)
        self.double_button.config(height = self.button_height, width = self.button_width)
        self.double_button.grid(row = 0, column = 1)

        self.final_button = tkinter.Button(self.root_window, text = "Final", command = self.final_jeopardy)
        self.final_button.config(height = self.button_height, width = self.button_width)
        self.final_button.grid(row = 0, column = 5)

        self.daily_button = tkinter.Button(self.root_window, text = "Daily", command = self.daily_double)
        self.daily_button.config(height = self.button_height, width = self.button_width)
        self.daily_button.grid(row = 0, column = 4)


        for i in range(self.game.rows):
            for j in range(self.game.columns):
                button_code = """
self.button_{r}{c} = tkinter.Button(self.root_window, text = '{value:4}', command = lambda: update(b, {r}, {c}))
self.button_{r}{c}.config(width = self.button_width, height = self.button_height)
self.button_{r}{c}.grid(row = {r}+1, column = {c})""".format(r=i, c=j, value = self.game.values[i])
                exec(button_code)


    def update(self, r:int, c:int): #Useless now, I suppose
        code = """
    if self.game.board[{row}][{col}] == None:
        self.button_{row}{col}.config(bg = self.correct)
        self.game.board[{row}][{col}] = True

    elif self.game.board[{row}][{col}] == False:
        self.button_{row}{col}.config(bg = self.blank)
        self.game.board[{row}][{col}] = None

    elif self.game.board[{row}][{col}] == True:
        self.button_{row}{col}.config(bg = self.wrong)
        self.game.board[{row}][{col}] = False
        """.format(row = r, col = c)

        exec(code)
                
        self.score.set(self.game.get_score())
    
    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def get_board(self):
        file_path = filedialog.askopenfilename()
        file_name = file_path.split("/")[-1]
        self.game.import_board(file_name)
        self.renew_board()

    def renew_board(self):
        '''Used to update the board to reflect the imported board'''
        for i in range(self.game.rows):
            for j in range(self.game.columns):
                code = """
if self.game.board[{row}][{col}] == None:
    self.button_{row}{col}.config(bg = self.blank)

elif self.game.board[{row}][{col}] == False:
    self.button_{row}{col}.config(bg = self.wrong)

elif self.game.board[{row}][{col}] == True:
    self.button_{row}{col}.config(bg = self.correct)
    """.format(row = i, col = j)

                exec(code)
                
        self.score.set(self.game.score)

    def invert_double(self):
        '''Changes the status of Jeopardy'''
        if not self.game.double:
            self.game.double = not self.game.double
            self.game.reset_board()
            self.score.set(self.game.get_score())
            self.double_button.config(bg = self.correct)
            for i in range(self.game.rows):
                    for j in range(self.game.columns):
                        code = """
self.button_{row}{col}.config(text = self.game.d_values[{row}], bg = self.blank)""".format(row = i, col = j)

                        exec(code)
        else:
            pass
        self.score.set(self.game.get_score())
        

    def get_wager(self):
        '''Gets the wager inputted in Final Jeopardy!'''
        current_score = self.game.get_score()
        try:
            wager = int(self.enter_wager.get())
            if wager < 0 or wager > current_score or wager in [69, 666, 14, 88, 1488]:
                raise ValueError
            return wager
        except ValueError:
            messagebox.showinfo("Error", message = "Wager must be between $0 and ${} and cannot be $69, $666, $14, $88, or $1488".format(current_score))

    def get_daily_wager(self):
        '''Gets the wager inputted in Final Jeopardy!'''
        current_score = self.game.get_score()
        try:
            wager = int(self.enter_wager.get())
            if wager < 5 or wager > current_score or wager in [69, 666, 14, 88, 1488]:
                raise ValueError
            return wager
        except ValueError:
            messagebox.showinfo("Error", message = "Wager must be between $5 and ${} and cannot be $69, $666, $14, $88, or $1488".format(current_score))
            

    def final_correct(self, window):
        wager = self.get_wager()
        
        if wager != None:
            self.score.set(self.game.final_jeopardy(wager, 1))
            self.game.export_final(self.enter_cat.get().strip(), wager, self.response_wager.get().strip(), 1)
            window.destroy()

    def final_wrong(self, window):
        wager = self.get_wager()

        if wager != None:
            self.score.set(self.game.final_jeopardy(wager, 0))
            self.game.export_final(self.enter_cat.get().strip(), wager, self.response_wager.get().strip(), 0)
            window.destroy()

    def daily_correct(self, window):
        wager = self.get_daily_wager()
        
        if wager != None:
            self.score.set(self.game.final_jeopardy(wager, 1))
            window.destroy()

    def daily_wrong(self, window):
        wager = self.get_daily_wager()

        if wager != None:
            self.score.set(self.game.final_jeopardy(wager, 0))
            window.destroy()

    def final_jeopardy(self):
        window = tkinter.Toplevel(self.root_window)
        window.geometry("400x225")
        window.resizable(0,0)
        window.iconbitmap(self.resource_path("jeopardy.ico"))
        window.title("Final Jeopardy")
        window.focus()
        
        self.cat_label = tkinter.Label(window, text = "Category", height = self.button_height, width = self.button_width)
        self.cat_label.grid(row = 0, column = 0)
        self.enter_cat = tkinter.Entry(window, width = self.button_width * 3)
        self.enter_cat.grid(row = 0, column = 1)
        
        self.wager_label = tkinter.Label(window, text = "Wager", height = self.button_height, width = self.button_width)
        self.wager_label.grid(row = 1, column = 0)
        self.enter_wager = tkinter.Entry(window, width = self.button_width * 3)
        self.enter_wager.grid(row = 1, column = 1)

        self.response_label = tkinter.Label(window, text = "Answer", height = self.button_height, width = self.button_width)
        self.response_label.grid(row = 2, column = 0)
        self.response_wager = tkinter.Entry(window, width = self.button_width * 3)
        self.response_wager.grid(row = 2, column = 1)

        self.correct_button = tkinter.Button(window, text = "Correct", height = self.button_height, width = self.button_width, bg = self.correct, command = lambda: self.final_correct(window))
        self.correct_button.grid(row = 3, column = 0, columnspan = 2, sticky = tkinter.W, padx = 50)

        self.correct_button = tkinter.Button(window, text = "Wrong", height = self.button_height, width = self.button_width, bg = self.wrong, command = lambda: self.final_wrong(window))
        self.correct_button.grid(row = 3, column = 1, columnspan = 2, sticky = tkinter.E)

    def daily_double(self):
        window = tkinter.Toplevel(self.root_window)
        window.geometry("400x150")
        window.resizable(0,0)
        window.iconbitmap(self.resource_path("jeopardy.ico"))
        window.title("Daily Double")
        window.focus()
        
        self.wager_label = tkinter.Label(window, text = "Wager", height = self.button_height, width = self.button_width)
        self.wager_label.grid(row = 0, column = 0)
        self.enter_wager = tkinter.Entry(window, width = self.button_width * 3)
        self.enter_wager.grid(row = 0, column = 1)

        #self.response_label = tkinter.Label(window, text = "Answer", height = self.button_height, width = self.button_width)
        #self.response_label.grid(row = 1, column = 0)
        #self.response_wager = tkinter.Entry(window, width = self.button_width * 3)
        #self.response_wager.grid(row = 1, column = 1)

        self.correct_button = tkinter.Button(window, text = "Correct", height = self.button_height, width = self.button_width, bg = self.correct, command = lambda: self.daily_correct(window))
        self.correct_button.grid(row = 1, column = 0, columnspan = 2, sticky = tkinter.W, padx = 50)

        self.correct_button = tkinter.Button(window, text = "Wrong", height = self.button_height, width = self.button_width, bg = self.wrong, command = lambda: self.daily_wrong(window))
        self.correct_button.grid(row = 1, column = 1, columnspan = 2, sticky = tkinter.E)
        

            
    def run(self):
        self.show_score.grid(row = 0, column = 0, columnspan = 6)
        self.export = tkinter.Button(self.root_window, text = "Export", command = self.game.export_board)
        self.export.config(height = self.button_height, width = self.button_width)
        self.export.grid(row = 0, column = 0, sticky = tkinter.N)

        #self.import_board = tkinter.Button(self.root_window, text = "Import", command = self.get_board)
        #self.import_board.config(height = int(self.button_height/2), width = self.button_width)
        #self.import_board.grid(row = 0, column = 0, sticky = tkinter.S)

        
        
        self.root_window.mainloop()

        

def update(b: JeopardyBoard, r:int, c:int): #Bad practice, but won't work with update() as a method
        code = """
if b.game.board[{row}][{col}] == None:
    b.button_{row}{col}.config(bg = b.correct)
    b.game.board[{row}][{col}] = True
elif b.game.board[{row}][{col}] == False:
    b.button_{row}{col}.config(bg = b.blank)
    b.game.board[{row}][{col}] = None
elif b.game.board[{row}][{col}] == True:
    b.button_{row}{col}.config(bg = b.wrong)
    b.game.board[{row}][{col}] = False
    """.format(row = r, col = c)

        exec(code)
        b.score.set(b.game.get_score())


if __name__ == "__main__":
    b = BoardGUI()
    b.run()
