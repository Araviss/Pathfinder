from PyQt5.QtWidgets import QWidget


class Grid:


    def __init__(self):
        self.columns = 20
        self.rows = 20
        self.click = True
        self.prevStartR =-1
        self.prevStartC = -1
        self.prevEndR = -1
        self.prevEndC = -1
        self.gridArray = [[0 for i in range(self.rows)] for j in range(self.columns)]


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



