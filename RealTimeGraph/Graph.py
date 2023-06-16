import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QTimer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class RealTimeGraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Real-Time Graph")
        self.setGeometry(100, 100, 800, 600)

        # Create the Matplotlib Figure and Canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.setCentralWidget(self.canvas)

        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Random Number')
        self.ax.set_title('Real-Time Random Number Graph')
        self.line, = self.ax.plot([], [], color='b')

        self.x_data = []
        self.y_data = []

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(500)  # 500 milliseconds = 0.5 seconds

        # Create the QLabel for displaying random numbers
        self.random_number_label = QLabel(self)
        self.random_number_label.setGeometry(10, 10, 200, 20)

    def update_graph(self):
        random_number = random.randint(1, 100)
        self.x_data.append(len(self.x_data))
        self.y_data.append(random_number)

        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()

        self.canvas.draw()

        self.random_number_label.setText(f"Random Number: {random_number}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RealTimeGraphWindow()
    window.show()
    sys.exit(app.exec_())
