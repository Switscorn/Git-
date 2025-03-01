from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt
import random
import sys


class ShapeRenderer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.setFixedSize(400, 300)
        self.circle_button = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.circle_button.clicked.connect(self.create_circle)
        self.circle_list = []

    def create_circle(self):
        self.circle_list.append(
            (random.randint(0, 400), random.randint(0, 300), random.randint(20, 100))
        )
        self.update()

    def paintEvent(self, event):
        painter_instance = QPainter(self)
        if not painter_instance.isActive():
            painter_instance.begin(self)
        painter_instance.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter_instance.setPen(Qt.PenStyle.NoPen)
        painter_instance.setBrush(QColor(255, 255, 0))
        for x_coord, y_coord, diameter in self.circle_list:
            painter_instance.drawEllipse(x_coord, y_coord, diameter, diameter)
        painter_instance.end()


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    main_window = ShapeRenderer()
    main_window.show()
    sys.exit(application.exec())
