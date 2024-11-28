import sys
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtWidgets import QApplication, QMainWindow
from random import randint
from UI import Ui_MainWindow


class Rhodophyta(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.yakut = 0
        self.goida_create_circle.clicked.connect(self.pa)

    def paintEvent(self, event):
        if self.yakut:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        d = randint(1, 1000)
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        qp.drawEllipse(randint(0, 800), randint(0, 600), d // 2, d // 2)

    def pa(self):
        self.yakut = 1
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Rhodophyta()
    ex.show()
    sys.exit(app.exec())
