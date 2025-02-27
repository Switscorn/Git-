from PyQt6 import QtWidgets, QtGui, QtCore
import random
import sys


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.button = QtWidgets.QPushButton(
            "Добавить окружность", self.centralwidget)
        self.button.setGeometry(140, 250, 120, 30)


class CircleDrawer(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        color = QtGui.QColor(random.randint(
            0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((random.randint(0, 300), random.randint(
            0, 200), random.randint(20, 100), color))
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        for x, y, d, color in self.circles:
            painter.setBrush(color)
            painter.setPen(QtCore.Qt.PenStyle.NoPen)
            painter.drawEllipse(x, y, d, d)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())
