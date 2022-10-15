from PyQt5.QtWidgets import QPushButton

#Overrides the QPushButton widget to be able to hover
class MyQPushButton(QPushButton):

    def __init__(self, parent=None):
        super(QPushButton, self).__init__(parent)
        self.setParent(parent)

#Enters into tracking the mouse movement
    def enterEvent(self, event):
        self.prev_text = self.text()
        self.setText('hovering')
        self.setMouseTracking(True)

    def leaveEvent(self, event):
        self.setText(self.prev_text)
        self.setMouseTracking(False)

    def mouseMoveEvent(self, event):
        self.setStyleSheet("background-color: orange")