from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QGridLayout, QLabel, \
    QHBoxLayout, QComboBox
import Search
from Grid import Grid
from MyQPushButton import MyQPushButton

app = QApplication([])
app.setStyle('Fusion')
window = QWidget()




g = Grid()
s = Search.Search()



def set_endpoints(r, c,gr,b):
    gridElem = gr.itemAtPosition(r,c).widget()
   #Helps to alternate between End and Beginning
    if(g.click):
        gridElem.setStyleSheet("background-color: green")
        g.click = False
        if (g.prevStartR >= 0):
            gr.itemAtPosition(g.prevStartR, g.prevStartC).widget().setStyleSheet("background-color: white")
        g.updateStart(r,c)
        s.set_start((r,c))
        print(s.get_start())
    else:
        gridElem.setStyleSheet("background-color: purple")
        g.click = True
        if (g.prevEndR >= 0 ):
            gr.itemAtPosition(g.prevEndR, g.prevEndC).widget().setStyleSheet("background-color: white")
        g.updateEnd(r,c)
        s.set_end((r,c))
        print(s.get_end())
    #updates the maze in Algorithm file
    s.maze = g.gridArray

#Updates start coloring cell red on first right click
def drag_update(r, c,grid,b):
    gridElem = grid.itemAtPosition(r,c).widget()
    g.gridArray[r][c] = "X"
    gridElem.setStyleSheet("background-color: red")


#This sets up the grid and events for cell
def move_update(r, c, grid, button):
    gridElem = grid.itemAtPosition(r, c).widget()
    gridElem.setStyleSheet("background-color: red")
    g.gridArray[r][c] = "X"
    s.wallList.append((r,c))
    s.maze = g.gridArray
    for e in s.maze:
        print("".join(map(str,e)))


def clear_grid():
    end = s.get_end()
    start = s.get_start()
    for i in range(0, g.rows - 1):
        for j in range(0, g.columns - 1):
                g.gridArray[i][j] = 0
                gridElem = grid.itemAtPosition(i, j).widget()
                QApplication.processEvents()
                gridElem.setStyleSheet("background-color: light gray")
    s.set_end((0, 0))
    s.set_start((0, 0))
# Clear grid when Algorithm Changed.
# The "if" Operator makes sure that it doesn't clear the
# start, end, or wall
def clear_color_path():
    end = s.get_end()
    start = s.get_start()
    for i in range(0, g.rows - 1):
        for j in range(0, g.columns - 1):
            if((i,j) != end
                    and (i,j) != start
                    and (i,j)  not in s.wallList):
                gridElem = grid.itemAtPosition(i, j).widget()
                QApplication.processEvents()
                gridElem.setStyleSheet("background-color: light gray")





# Use this method to animate the cells sequentially
#This way we don't have to delay processing
#Instead we can have animation slowed down
def color_path():
    while (s.fifo):
        cell = s.fifo.popleft()
        gridElem = grid.itemAtPosition(cell[0], cell[1])
        if gridElem != None and (cell[0],cell[1]) != s.get_end() \
                and (cell[0],cell[1]) != s.get_start():
            print(s.get_start())
            print(s.get_end())
            QApplication.processEvents()
            gridElem.widget().setStyleSheet("background-color: turquoise")


# Determines which algorithm in the combBox was chosen
def start_search():
    if comboBox.currentIndex() == 0:
        s.astar()
    elif comboBox.currentIndex() == 1:
        clear_color_path()
        s.depth_first()
    elif comboBox.currentIndex() == 2:
        clear_color_path()
        s.greedy()
    elif comboBox.currentIndex() == 3:
        clear_color_path()
        s.iterative()
    color_path()


# Sets up grid configuration and sets signals
# Must iterate through each grid coordinate to add
# and configure button
def set_grid():
    for i in range(0, g.rows-1):
        for j in range(0,g.columns -1):
            button = MyQPushButton()
            button.resize(38, 21)
            button.setStyleSheet(("border: 1px solid black;"))
            button.setFixedHeight(38)
            button.setStyleSheet("background-color: light gray")
            grid.addWidget(button,i,j)

            button.clickPressSignal.connect(lambda event, r=i, c=j: drag_update(r, c, grid, button))
            button.mousePressSignal.connect(lambda event, r=i, c=j: set_endpoints(r, c, grid,button))
            button.enterSignal.connect(lambda event, r=i, c=j: move_update(r, c, grid,button))
        s.R = g.rows
        s.C = g.columns

#Instantiating grid layout
comboBox = QComboBox()
comboBox.addItem('A*')
comboBox.addItem('Depth')
comboBox.addItem('Greedy ')
comboBox.addItem('Iterative')
comboBox.currentIndexChanged.connect(start_search)

vbox = QVBoxLayout()
vbox.addStretch(1)

hbox = QHBoxLayout()
hbox.addStretch(1)
startButton = QPushButton()
startButton.setText("Start")
clearButton = QPushButton()
clearButton.setText("Clear Grid")
hbox.addWidget(startButton)
hbox.addWidget(comboBox)
hbox.addWidget((clearButton))

grid = QGridLayout()
grid.setSpacing(0)
vbox.addLayout(hbox)
vbox.addLayout(grid)


clearButton.clicked.connect(lambda event: clear_grid())
startButton.clicked.connect(lambda event: start_search())
window.setLayout((vbox))
set_grid()


window.show()
app.exec()



# TO DO LIST
#resize grid when window expands
#Set Animations