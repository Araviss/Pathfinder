from PyQt5 import Qt, QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QPushButton

#Overrides the QPushButton widget to be able to hover
class MyQPushButton(QPushButton):
    mousePressSignal = QtCore.pyqtSignal(QMouseEvent)
    clickPressSignal = QtCore.pyqtSignal(QMouseEvent)
    dragstart = False

    def __init__(self, parent=None):
        super(QPushButton, self).__init__(parent)
        self.setParent(parent)
        self.setMouseTracking(False)


#Only activates when something already clicked
    def enterEvent(self, event):
        if(MyQPushButton.dragstart):
            self.setText('hovering')



    def mouseMoveEvent(self, event):
        self.setStyleSheet("background-color: orange")


    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            self.mousePressSignal.emit(QMouseEvent)
        #Determines whether 1st or 2nd right click
        elif QMouseEvent.button() == QtCore.Qt.RightButton:
            if MyQPushButton.dragstart:
                MyQPushButton.dragstart = False
            elif MyQPushButton.dragstart == False:
                MyQPushButton.dragstart = True
                self.clickPressSignal.emit(QMouseEvent)




#Get the grid coordinates


