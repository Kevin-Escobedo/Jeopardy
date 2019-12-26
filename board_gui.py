#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
import tkinter
import datetime
import sys
import os
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

        ###200###
        self.button_00 = tkinter.Button(self.root_window, text = "{:4}".format(200), command = self.zerozero)
        self.button_00.config(width = self.button_width, height = self.button_height)
        self.button_00.grid(row = 1, column = 0)

        self.button_01 = tkinter.Button(self.root_window, text = "{:4}".format(200), command = self.zeroone)
        self.button_01.config(width = self.button_width, height = self.button_height)
        self.button_01.grid(row = 1, column = 1)

        self.button_02 = tkinter.Button(self.root_window, text = "{:4}".format(200), command = self.zerotwo)
        self.button_02.config(width = self.button_width, height = self.button_height)
        self.button_02.grid(row = 1, column = 2)

        self.button_03 = tkinter.Button(self.root_window, text = "{:4}".format(200), command = self.zerothree)
        self.button_03.config(width = self.button_width, height = self.button_height)
        self.button_03.grid(row = 1, column = 3)

        self.button_04 = tkinter.Button(self.root_window, text = "{:4}".format(200), command = self.zerofour)
        self.button_04.config(width = self.button_width, height = self.button_height)
        self.button_04.grid(row = 1, column = 4)

        self.button_05 = tkinter.Button(self.root_window, text = "{:4}".format(200), command = self.zerofive)
        self.button_05.config(width = self.button_width, height = self.button_height)
        self.button_05.grid(row = 1, column = 5)

        ###400###
        self.button_10 = tkinter.Button(self.root_window, text = "{:4}".format(400), command = self.onezero)
        self.button_10.grid(row = 2, column = 0)
        self.button_10.config(width = self.button_width, height = self.button_height)

        self.button_11 = tkinter.Button(self.root_window, text = "{:4}".format(400), command = self.oneone)
        self.button_11.grid(row = 2, column = 1)
        self.button_11.config(width = self.button_width, height = self.button_height)

        self.button_12 = tkinter.Button(self.root_window, text = "{:4}".format(400), command = self.onetwo)
        self.button_12.grid(row = 2, column = 2)
        self.button_12.config(width = self.button_width, height = self.button_height)

        self.button_13 = tkinter.Button(self.root_window, text = "{:4}".format(400), command = self.onethree)
        self.button_13.grid(row = 2, column = 3)
        self.button_13.config(width = self.button_width, height = self.button_height)

        self.button_14 = tkinter.Button(self.root_window, text = "{:4}".format(400), command = self.onefour)
        self.button_14.grid(row = 2, column = 4)
        self.button_14.config(width = self.button_width, height = self.button_height)

        self.button_15 = tkinter.Button(self.root_window, text = "{:4}".format(400), command = self.onefive)
        self.button_15.config(width = self.button_width, height = self.button_height)
        self.button_15.grid(row = 2, column = 5)

        ###600###
        self.button_20 = tkinter.Button(self.root_window, text = "{:4}".format(600), command = self.twozero)
        self.button_20.grid(row = 3, column = 0)
        self.button_20.config(width = self.button_width, height = self.button_height)

        self.button_21 = tkinter.Button(self.root_window, text = "{:4}".format(600), command = self.twoone)
        self.button_21.grid(row = 3, column = 1)
        self.button_21.config(width = self.button_width, height = self.button_height)

        self.button_22 = tkinter.Button(self.root_window, text = "{:4}".format(600), command = self.twotwo)
        self.button_22.grid(row = 3, column = 2)
        self.button_22.config(width = self.button_width, height = self.button_height)

        self.button_23 = tkinter.Button(self.root_window, text = "{:4}".format(600), command = self.twothree)
        self.button_23.grid(row = 3, column = 3)
        self.button_23.config(width = self.button_width, height = self.button_height)

        self.button_24 = tkinter.Button(self.root_window, text = "{:4}".format(600), command = self.twofour)
        self.button_24.grid(row = 3, column = 4)
        self.button_24.config(width = self.button_width, height = self.button_height)

        self.button_25 = tkinter.Button(self.root_window, text = "{:4}".format(600), command = self.twofive)
        self.button_25.config(width = self.button_width, height = self.button_height)
        self.button_25.grid(row = 3, column = 5)

        ###800###
        self.button_30 = tkinter.Button(self.root_window, text = "{:4}".format(800), command = self.threezero)
        self.button_30.grid(row = 4, column = 0)
        self.button_30.config(width = self.button_width, height = self.button_height)

        self.button_31 = tkinter.Button(self.root_window, text = "{:4}".format(800), command = self.threeone)
        self.button_31.grid(row = 4, column = 1)
        self.button_31.config(width = self.button_width, height = self.button_height)

        self.button_32 = tkinter.Button(self.root_window, text = "{:4}".format(800), command = self.threetwo)
        self.button_32.grid(row = 4, column = 2)
        self.button_32.config(width = self.button_width, height = self.button_height)

        self.button_33 = tkinter.Button(self.root_window, text = "{:4}".format(800), command = self.threethree)
        self.button_33.grid(row = 4, column = 3)
        self.button_33.config(width = self.button_width, height = self.button_height)

        self.button_34 = tkinter.Button(self.root_window, text = "{:4}".format(800), command = self.threefour)
        self.button_34.grid(row = 4, column = 4)
        self.button_34.config(width = self.button_width, height = self.button_height)

        self.button_35 = tkinter.Button(self.root_window, text = "{:4}".format(800), command = self.threefive)
        self.button_35.config(width = self.button_width, height = self.button_height)
        self.button_35.grid(row = 4, column = 5)

        ###1000###
        self.button_40 = tkinter.Button(self.root_window, text = "{:4}".format(1000), command = self.fourzero)
        self.button_40.grid(row = 5, column = 0)
        self.button_40.config(width = self.button_width, height = self.button_height)

        self.button_41 = tkinter.Button(self.root_window, text = "{:4}".format(1000), command = self.fourone)
        self.button_41.grid(row = 5, column = 1)
        self.button_41.config(width = self.button_width, height = self.button_height)

        self.button_42 = tkinter.Button(self.root_window, text = "{:4}".format(1000), command = self.fourtwo)
        self.button_42.grid(row = 5, column = 2)
        self.button_42.config(width = self.button_width, height = self.button_height)

        self.button_43 = tkinter.Button(self.root_window, text = "{:4}".format(1000), command = self.fourthree)
        self.button_43.grid(row = 5, column = 3)
        self.button_43.config(width = self.button_width, height = self.button_height)

        self.button_44 = tkinter.Button(self.root_window, text = "{:4}".format(1000), command = self.fourfour)
        self.button_44.grid(row = 5, column = 4)
        self.button_44.config(width = self.button_width, height = self.button_height)

        self.button_45 = tkinter.Button(self.root_window, text = "{:4}".format(1000), command = self.fourfive)
        self.button_45.config(width = self.button_width, height = self.button_height)
        self.button_45.grid(row = 5, column = 5)

    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    ###200###
    def zerozero(self):
        if self.game.board[0][0] == None:
            self.button_00.config(bg = self.correct)
            self.game.board[0][0] = True

        elif self.game.board[0][0] == False:
            self.button_00.config(bg = self.blank)
            self.game.board[0][0] = None

        elif self.game.board[0][0] == True:
            self.button_00.config(bg = self.wrong)
            self.game.board[0][0] = False
            
        self.score.set(self.game.get_score())

    def zeroone(self):
        if self.game.board[0][1] == None:
            self.button_01.config(bg = self.correct)
            self.game.board[0][1] = True

        elif self.game.board[0][1] == False:
            self.button_01.config(bg = self.blank)
            self.game.board[0][1] = None

        elif self.game.board[0][1] == True:
            self.button_01.config(bg = self.wrong)
            self.game.board[0][1] = False
            
        self.score.set(self.game.get_score())

    def zerotwo(self):
        if self.game.board[0][2] == None:
            self.button_02.config(bg = self.correct)
            self.game.board[0][2] = True

        elif self.game.board[0][2] == False:
            self.button_02.config(bg = self.blank)
            self.game.board[0][2] = None

        elif self.game.board[0][2] == True:
            self.button_02.config(bg = self.wrong)
            self.game.board[0][2] = False
            
        self.score.set(self.game.get_score())

    def zerothree(self):
        if self.game.board[0][3] == None:
            self.button_03.config(bg = self.correct)
            self.game.board[0][3] = True

        elif self.game.board[0][3] == False:
            self.button_03.config(bg = self.blank)
            self.game.board[0][3] = None

        elif self.game.board[0][3] == True:
            self.button_03.config(bg = self.wrong)
            self.game.board[0][3] = False
            
        self.score.set(self.game.get_score())

    def zerofour(self):
        if self.game.board[0][4] == None:
            self.button_04.config(bg = self.correct)
            self.game.board[0][4] = True

        elif self.game.board[0][4] == False:
            self.button_04.config(bg = self.blank)
            self.game.board[0][4] = None

        elif self.game.board[0][4] == True:
            self.button_04.config(bg = self.wrong)
            self.game.board[0][4] = False
            
        self.score.set(self.game.get_score())

    def zerofive(self):
        if self.game.board[0][5] == None:
            self.button_05.config(bg = self.correct)
            self.game.board[0][5] = True

        elif self.game.board[0][5] == False:
            self.button_05.config(bg = self.blank)
            self.game.board[0][5] = None

        elif self.game.board[0][5] == True:
            self.button_05.config(bg = self.wrong)
            self.game.board[0][5] = False
            
        self.score.set(self.game.get_score())

    ###400###
    def onezero(self):
        if self.game.board[1][0] == None:
            self.button_10.config(bg = self.correct)
            self.game.board[1][0] = True

        elif self.game.board[1][0] == False:
            self.button_10.config(bg = self.blank)
            self.game.board[1][0] = None

        elif self.game.board[1][0] == True:
            self.button_10.config(bg = self.wrong)
            self.game.board[1][0] = False
            
        self.score.set(self.game.get_score())

    def oneone(self):
        if self.game.board[1][1] == None:
            self.button_11.config(bg = self.correct)
            self.game.board[1][1] = True

        elif self.game.board[1][1] == False:
            self.button_11.config(bg = self.blank)
            self.game.board[1][1] = None

        elif self.game.board[1][1] == True:
            self.button_11.config(bg = self.wrong)
            self.game.board[1][1] = False
            
        self.score.set(self.game.get_score())

    def onetwo(self):
        if self.game.board[1][2] == None:
            self.button_12.config(bg = self.correct)
            self.game.board[1][2] = True

        elif self.game.board[1][2] == False:
            self.button_12.config(bg = self.blank)
            self.game.board[1][2] = None

        elif self.game.board[1][2] == True:
            self.button_12.config(bg = self.wrong)
            self.game.board[1][2] = False
            
        self.score.set(self.game.get_score())

    def onethree(self):
        if self.game.board[1][3] == None:
            self.button_13.config(bg = self.correct)
            self.game.board[1][3] = True

        elif self.game.board[1][3] == False:
            self.button_13.config(bg = self.blank)
            self.game.board[1][3] = None

        elif self.game.board[1][3] == True:
            self.button_13.config(bg = self.wrong)
            self.game.board[1][3] = False
            
        self.score.set(self.game.get_score())

    def onefour(self):
        if self.game.board[1][4] == None:
            self.button_14.config(bg = self.correct)
            self.game.board[1][4] = True

        elif self.game.board[1][4] == False:
            self.button_14.config(bg = self.blank)
            self.game.board[1][4] = None

        elif self.game.board[1][4] == True:
            self.button_14.config(bg = self.wrong)
            self.game.board[1][4] = False
            
        self.score.set(self.game.get_score())

    def onefive(self):
        if self.game.board[1][5] == None:
            self.button_15.config(bg = self.correct)
            self.game.board[1][5] = True

        elif self.game.board[1][5] == False:
            self.button_15.config(bg = self.blank)
            self.game.board[1][5] = None

        elif self.game.board[1][5] == True:
            self.button_15.config(bg = self.wrong)
            self.game.board[1][5] = False
            
        self.score.set(self.game.get_score())

    ###600###
    def twozero(self):
        if self.game.board[2][0] == None:
            self.button_20.config(bg = self.correct)
            self.game.board[2][0] = True

        elif self.game.board[2][0] == False:
            self.button_20.config(bg = self.blank)
            self.game.board[2][0] = None

        elif self.game.board[2][0] == True:
            self.button_20.config(bg = self.wrong)
            self.game.board[2][0] = False
            
        self.score.set(self.game.get_score())

    def twoone(self):
        if self.game.board[2][1] == None:
            self.button_21.config(bg = self.correct)
            self.game.board[2][1] = True

        elif self.game.board[2][1] == False:
            self.button_21.config(bg = self.blank)
            self.game.board[2][1] = None

        elif self.game.board[2][1] == True:
            self.button_21.config(bg = self.wrong)
            self.game.board[2][1] = False
            
        self.score.set(self.game.get_score())

    def twotwo(self):
        if self.game.board[2][2] == None:
            self.button_22.config(bg = self.correct)
            self.game.board[2][2] = True

        elif self.game.board[2][2] == False:
            self.button_22.config(bg = self.blank)
            self.game.board[2][2] = None

        elif self.game.board[2][2] == True:
            self.button_22.config(bg = self.wrong)
            self.game.board[2][2] = False
            
        self.score.set(self.game.get_score())

    def twothree(self):
        if self.game.board[2][3] == None:
            self.button_23.config(bg = self.correct)
            self.game.board[2][3] = True

        elif self.game.board[2][3] == False:
            self.button_23.config(bg = self.blank)
            self.game.board[2][3] = None

        elif self.game.board[2][3] == True:
            self.button_23.config(bg = self.wrong)
            self.game.board[2][3] = False
            
        self.score.set(self.game.get_score())

    def twofour(self):
        if self.game.board[2][4] == None:
            self.button_24.config(bg = self.correct)
            self.game.board[2][4] = True

        elif self.game.board[2][4] == False:
            self.button_24.config(bg = self.blank)
            self.game.board[2][4] = None

        elif self.game.board[2][4] == True:
            self.button_24.config(bg = self.wrong)
            self.game.board[2][4] = False
            
        self.score.set(self.game.get_score())

    def twofive(self):
        if self.game.board[2][5] == None:
            self.button_25.config(bg = self.correct)
            self.game.board[2][5] = True

        elif self.game.board[2][5] == False:
            self.button_25.config(bg = self.blank)
            self.game.board[2][5] = None

        elif self.game.board[2][5] == True:
            self.button_25.config(bg = self.wrong)
            self.game.board[2][5] = False
            
        self.score.set(self.game.get_score())

    ###800###
    def threezero(self):
        if self.game.board[3][0] == None:
            self.button_30.config(bg = self.correct)
            self.game.board[3][0] = True

        elif self.game.board[3][0] == False:
            self.button_30.config(bg = self.blank)
            self.game.board[3][0] = None

        elif self.game.board[3][0] == True:
            self.button_30.config(bg = self.wrong)
            self.game.board[3][0] = False
            
        self.score.set(self.game.get_score())

    def threeone(self):
        if self.game.board[3][1] == None:
            self.button_31.config(bg = self.correct)
            self.game.board[3][1] = True

        elif self.game.board[3][1] == False:
            self.button_31.config(bg = self.blank)
            self.game.board[3][1] = None

        elif self.game.board[3][1] == True:
            self.button_31.config(bg = self.wrong)
            self.game.board[3][1] = False
            
        self.score.set(self.game.get_score())

    def threetwo(self):
        if self.game.board[3][2] == None:
            self.button_32.config(bg = self.correct)
            self.game.board[3][2] = True

        elif self.game.board[3][2] == False:
            self.button_32.config(bg = self.blank)
            self.game.board[3][2] = None

        elif self.game.board[3][2] == True:
            self.button_32.config(bg = self.wrong)
            self.game.board[3][2] = False
            
        self.score.set(self.game.get_score())

    def threethree(self):
        if self.game.board[3][3] == None:
            self.button_33.config(bg = self.correct)
            self.game.board[3][3] = True

        elif self.game.board[3][3] == False:
            self.button_33.config(bg = self.blank)
            self.game.board[3][3] = None

        elif self.game.board[3][3] == True:
            self.button_33.config(bg = self.wrong)
            self.game.board[3][3] = False
            
        self.score.set(self.game.get_score())

    def threefour(self):
        if self.game.board[3][4] == None:
            self.button_34.config(bg = self.correct)
            self.game.board[3][4] = True

        elif self.game.board[3][4] == False:
            self.button_34.config(bg = self.blank)
            self.game.board[3][4] = None

        elif self.game.board[3][4] == True:
            self.button_34.config(bg = self.wrong)
            self.game.board[3][4] = False
            
        self.score.set(self.game.get_score())

    def threefive(self):
        if self.game.board[3][5] == None:
            self.button_35.config(bg = self.correct)
            self.game.board[3][5] = True

        elif self.game.board[3][5] == False:
            self.button_35.config(bg = self.blank)
            self.game.board[3][5] = None

        elif self.game.board[3][5] == True:
            self.button_35.config(bg = self.wrong)
            self.game.board[3][5] = False
            
        self.score.set(self.game.get_score())

    ###1000###
    def fourzero(self):
        if self.game.board[4][0] == None:
            self.button_40.config(bg = self.correct)
            self.game.board[4][0] = True

        elif self.game.board[4][0] == False:
            self.button_40.config(bg = self.blank)
            self.game.board[4][0] = None

        elif self.game.board[4][0] == True:
            self.button_40.config(bg = self.wrong)
            self.game.board[4][0] = False
            
        self.score.set(self.game.get_score())

    def fourone(self):
        if self.game.board[4][1] == None:
            self.button_41.config(bg = self.correct)
            self.game.board[4][1] = True

        elif self.game.board[4][1] == False:
            self.button_41.config(bg = self.blank)
            self.game.board[4][1] = None

        elif self.game.board[4][1] == True:
            self.button_41.config(bg = self.wrong)
            self.game.board[4][1] = False
            
        self.score.set(self.game.get_score())

    def fourtwo(self):
        if self.game.board[4][2] == None:
            self.button_42.config(bg = self.correct)
            self.game.board[4][2] = True

        elif self.game.board[4][2] == False:
            self.button_42.config(bg = self.blank)
            self.game.board[4][2] = None

        elif self.game.board[4][2] == True:
            self.button_42.config(bg = self.wrong)
            self.game.board[4][2] = False
            
        self.score.set(self.game.get_score())

    def fourthree(self):
        if self.game.board[4][3] == None:
            self.button_43.config(bg = self.correct)
            self.game.board[4][3] = True

        elif self.game.board[4][3] == False:
            self.button_43.config(bg = self.blank)
            self.game.board[4][3] = None

        elif self.game.board[4][3] == True:
            self.button_43.config(bg = self.wrong)
            self.game.board[4][3] = False
            
        self.score.set(self.game.get_score())

    def fourfour(self):
        if self.game.board[4][4] == None:
            self.button_44.config(bg = self.correct)
            self.game.board[4][4] = True

        elif self.game.board[4][4] == False:
            self.button_44.config(bg = self.blank)
            self.game.board[4][4] = None

        elif self.game.board[4][4] == True:
            self.button_44.config(bg = self.wrong)
            self.game.board[4][4] = False
            
        self.score.set(self.game.get_score())

    def fourfive(self):
        if self.game.board[4][5] == None:
            self.button_45.config(bg = self.correct)
            self.game.board[4][5] = True

        elif self.game.board[4][5] == False:
            self.button_45.config(bg = self.blank)
            self.game.board[4][5] = None

        elif self.game.board[4][5] == True:
            self.button_45.config(bg = self.wrong)
            self.game.board[4][5] = False
            
        self.score.set(self.game.get_score())


    def run(self):
        self.show_score.grid(row = 0, column = 0, columnspan = 6)
        self.export = tkinter.Button(self.root_window, text = "Export", command = self.game.export_board)
        self.export.config(height = self.button_height, width = self.button_width)
        self.export.grid(row = 0, column = 0, sticky = tkinter.W)
        
        
        self.root_window.mainloop()


if __name__ == "__main__":
    b = BoardGUI().run()
