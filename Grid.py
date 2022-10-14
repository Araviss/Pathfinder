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
        self.gridArray[self.prevStartR][self.prevStartC] = 0
        self.gridArray[r][c] = "G"
        self.prevStartR = r
        self.prevStartC = c
        print(self.gridArray)

    def updateEnd(self,r,c):
        self.gridArray[self.prevEndR][self.prevEndC] = 0
        self.gridArray[r][c] = "P"
        self.prevEndR = r
        self.prevEndC = c
        print(self.gridArray)

