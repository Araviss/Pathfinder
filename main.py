from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPalette, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QGridLayout, QLabel

from Grid import Grid

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
    if(g.click):
        gridElem.setStyleSheet("background-color: green")
        g.click = False
        if (g.prevStartR >= 0):
            gr.itemAtPosition(g.prevStartR, g.prevStartC).widget().setStyleSheet("background-color: white")
        g.prevStartR = r
        g.prevStartC = c
    else:
        gridElem.setStyleSheet("background-color: purple")
        g.click = True
        if (g.prevEndR >= 0):
            gr.itemAtPosition(g.prevEndR, g.prevEndC).widget().setStyleSheet("background-color: white")
        g.prevEndR = r
        g.prevEndC = c


    print(r,c)


def set_grid():
    for i in range(0, g.columns+1):
        for j in range(0,g.rows +1):
            button = QPushButton()
            button.resize(38, 21)
            button.setStyleSheet(("border: 1px solid black;"))
            button.setFixedHeight(100)
            button.setFixedHeight(38)
            grid.addWidget(button,i,j)
            button.clicked.connect(lambda _, r=i, c=j: tell_me(r, c, grid,button))




window.setLayout((grid))
set_grid()
window.show()
app.exec()

#Set alternating Goal and endpoint
#resize grid when window expands