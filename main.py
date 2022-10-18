from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPalette, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QGridLayout, QLabel, \
    QHBoxLayout

import Search
from Grid import Grid
from MyQPushButton import MyQPushButton

app = QApplication([])
app.setStyle('Fusion')
window = QWidget()

#Instantiating grid layout
vbox = QVBoxLayout()
vbox.addStretch(1)

hbox = QHBoxLayout()
hbox.addStretch(1)
startButton = QPushButton()
startButton.setText("Refresh")
hbox.addWidget(startButton)

grid = QGridLayout()
grid.setSpacing(0)
vbox.addLayout(hbox)
vbox.addLayout(grid)


g = Grid()
s = Search.Search()
print(g)



def tell_me(r, c,gr,b):
    gridElem = gr.itemAtPosition(r,c).widget()
   #Helps to alternate between End and Beginning
    if(g.click):
        gridElem.setStyleSheet("background-color: green")
        g.click = False
        if (g.prevStartR >= 0):
            gr.itemAtPosition(g.prevStartR, g.prevStartC).widget().setStyleSheet("background-color: white")
        g.updateStart(r,c)
        s.start = (r,c)
        print(s.start)
    else:
        gridElem.setStyleSheet("background-color: purple")
        g.click = True
        if (g.prevEndR >= 0):
            gr.itemAtPosition(g.prevEndR, g.prevEndC).widget().setStyleSheet("background-color: white")
        g.updateEnd(r,c)
        s.end = (r,c)
        print(s.end)
    #updates the maze in Algorithm file
    s.maze = g.gridArray


def drag_update(r, c,grid,b):
    gridElem = grid.itemAtPosition(r,c).widget()
    g.gridArray[r][c] = "X"
    gridElem.setStyleSheet("background-color: red")


#This sets up the grid and events for cell
def move_update(r, c, grid, button):
    gridElem = grid.itemAtPosition(r, c).widget()
    gridElem.setStyleSheet("background-color: red")
    g.gridArray[r][c] = "X"
    s.maze = g.gridArray
    for e in s.maze:
        print("".join(map(str,e)))


def start_search():
    s.iterative()
    print("Bitch")

def set_grid():
    for i in range(0, g.rows-1):
        for j in range(0,g.columns -1):
            button = MyQPushButton()
            button.resize(38, 21)
            button.setStyleSheet(("border: 1px solid black;"))
            button.setFixedHeight(100)
            button.setFixedHeight(38)
            grid.addWidget(button,i,j)
            button.clickPressSignal.connect(lambda event, r=i, c=j: drag_update(r, c, grid, button))
            button.mousePressSignal.connect(lambda event, r=i, c=j: tell_me(r, c, grid,button))
            button.enterSignal.connect(lambda event, r=i, c=j: move_update(r, c, grid,button))

        s.R = g.rows
        s.C = g.columns





startButton.clicked.connect(lambda event: start_search())
window.setLayout((vbox))
set_grid()


window.show()
app.exec()

#resize grid when window expands
#Get Algorithm to take grid
#Get UI to show algorithm in play