from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPalette, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QGridLayout, QLabel

from Grid import Grid
from MyQPushButton import MyQPushButton

app = QApplication([])
app.setStyle('Fusion')
window = QWidget()

#Instantiating grid layout

grid = QGridLayout()
grid.setSpacing(0)
g = Grid()
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
    else:
        gridElem.setStyleSheet("background-color: purple")
        g.click = True
        if (g.prevEndR >= 0):
            gr.itemAtPosition(g.prevEndR, g.prevEndC).widget().setStyleSheet("background-color: white")
        g.updateEnd(r,c)
    print(r,c)


def drag_update(r, c,grid,b):
    gridElem = grid.itemAtPosition(r,c).widget()
    gridElem.setStyleSheet("background-color: red")


#This sets up the grid and events for cell
def move_update(r, c, grid, button):
    gridElem = grid.itemAtPosition(r, c).widget()
    gridElem.setStyleSheet("background-color: red")
    g.gridArray[r][c] = "x"
    for e in g.gridArray:
        print("".join(map(str,e)))


def set_grid():
    for i in range(0, g.rows+1):
        for j in range(0,g.columns +1):
            button = MyQPushButton()
            button.resize(38, 21)
            button.setStyleSheet(("border: 1px solid black;"))
            button.setFixedHeight(100)
            button.setFixedHeight(38)
            grid.addWidget(button,i,j)
            button.clickPressSignal.connect(lambda event, r=i, c=j: drag_update(r, c, grid, button))
            button.mousePressSignal.connect(lambda event, r=i, c=j: tell_me(r, c, grid,button))
            button.enterSignal.connect(lambda event, r=i, c=j: move_update(r, c, grid,button))






window.setLayout((grid))
set_grid()
window.show()
app.exec()

#resize grid when window expands
#determine mouse drag