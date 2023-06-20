from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
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
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 48px; font-weight: bold;")

class TimerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.elapsed_time = 0
        self.layout = QVBoxLayout()
        self.label = QLabel()
        self.layout.addWidget(self.label)
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_timer)
        self.layout.addWidget(self.reset_button)
        self.setLayout(self.layout)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.start_timer()

    def start_timer(self):
        self.timer.start(1000)

    def reset_timer(self):
        self.timer.stop()
        self.elapsed_time = 0
        self.update_timer()
        self.start_timer()

    def update_timer(self):
        self.elapsed_time += 1
        minutes = self.elapsed_time // 60
        seconds = self.elapsed_time % 60
        time_text = f"{minutes:02d}:{seconds:02d}"
        self.label.setText(time_text)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 24px; font-weight: bold;")

if __name__ == '__main__':
    app = QApplication([])

    main_widget = QWidget()
    main_layout = QVBoxLayout()
    main_widget.setLayout(main_layout)

    clock = DigitalClock()
    main_layout.addWidget(clock)

    timer1 = TimerWidget()
    main_layout.addWidget(timer1)

    timer2 = TimerWidget()
    main_layout.addWidget(timer2)

    reset_button = QPushButton("Reset All")
    reset_button.clicked.connect(lambda: [timer.reset_timer() for timer in [timer1, timer2]])
    main_layout.addWidget(reset_button)

    main_widget.show()

    app.exec_()
