# To print random numbers at a frequency of 0.5 seconds. 
#PyQt5
#random


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QTimer, Qt
from random import randint


class RandomNumberDisplay(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Number Display")
        self.setGeometry(100, 100, 200, 100)

        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 180, 80)
        self.label.setAlignment(Qt.AlignCenter)  # Use Qt.AlignCenter instead

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_display)
        self.timer.start(500)  # 500 milliseconds = 0.5 seconds

    def update_display(self):
        random_number = randint(1, 100)
        self.label.setText(str(random_number))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RandomNumberDisplay()
    window.show()
    sys.exit(app.exec_())
