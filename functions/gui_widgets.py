from PyQt5 import QtWidgets, QtCore


class QDoublePushButton(QtWidgets.QToolButton):
    doubleClicked = QtCore.pyqtSignal()
    clicked = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        QtWidgets.QToolButton.__init__(self, *args, **kwargs)

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()

    def mousePressEvent(self, event):
        self.clicked.emit()
