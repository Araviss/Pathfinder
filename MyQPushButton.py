from PyQt5 import Qt, QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMouseEvent, QEnterEvent
from PyQt5.QtWidgets import QPushButton

#Overrides the QPushButton widget to be able to hover
class MyQPushButton(QPushButton):
    mousePressSignal = QtCore.pyqtSignal(QMouseEvent)
    clickPressSignal = QtCore.pyqtSignal(QMouseEvent)
    enterSignal = QtCore.pyqtSignal(QEnterEvent)
    dragstart = False

    def __init__(self, parent=None):
        super(QPushButton, self).__init__(parent)
        self.setParent(parent)
        self.setMouseTracking(False)


#Detects which cell has been entered into
    def enterEvent(self, event):
        if(MyQPushButton.dragstart):
            self.enterSignal.emit(event)



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


