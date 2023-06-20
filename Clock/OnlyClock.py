from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QFont

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Digital Clock')
        self.layout = QVBoxLayout()
        self.label = QLabel()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

    def update_time(self):
        current_time = QTime.currentTime()
        time_text = current_time.toString('hh:mm:ss')
        self.label.setText(time_text)
        font = QFont('Arial', 48, QFont.Bold)
        self.label.setFont(font)

if __name__ == '__main__':
    app = QApplication([])
    clock = DigitalClock()
    clock.show()
    app.exec_()
