from PyQt5.QtWidgets import QWidget


class Grid:
    columns = 20
    rows = 20
    gridArray = [[0] * columns] * rows
    def __init__(self):

        self.click = True
        self.prevStartR =-1
        self.prevStartC = -1
        self.prevEndR = -1
        self.prevEndC = -1


    def updateStart(self,r,c):
        self.gridArray[self.prevStartR][self.prevStartC] = None
        self.gridArray[r][c] = "G"

    def updateEnd(self,r,c):
        self.gridArray[self.prevEndR][self.prevEndC] = None
        self.gridArray[r][c] = "P"


    def updateGrid(self):
        pass
