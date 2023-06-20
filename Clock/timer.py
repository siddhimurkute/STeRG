import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class TimerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.elapsed_time = 0
        
        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 200, 50)
        
        self.reset_button = QPushButton("Reset", self)
        self.reset_button.setGeometry(10, 70, 80, 30)
        self.reset_button.clicked.connect(self.reset_timer)
        
        self.setWindowTitle("Timer")
        self.setGeometry(100, 100, 220, 110)
        
        self.start_timer()
        
    def start_timer(self):
        self.timer.start(1000)  # 1 second interval
    
    def update_timer(self):
        self.elapsed_time += 1
        self.label.setText("Elapsed Time: {} seconds".format(self.elapsed_time))
    
    def reset_timer(self):
        self.elapsed_time = 0
        self.label.setText("Elapsed Time: 0 seconds")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimerWindow()
    window.show()
    sys.exit(app.exec_())
