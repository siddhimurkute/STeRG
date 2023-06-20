import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        self.max_rows = 8  # Maximum number of rows
        self.current_row = 0  # Current row index

        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(self.max_rows)
        self.table_widget.setColumnCount(1)
        self.table_widget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.horizontalHeader().setVisible(False)

        main_layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        main_layout.addWidget(self.table_widget, alignment=Qt.AlignBottom | Qt.AlignRight)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_table)
        self.timer.start(1000)  # 1 second interval

    def update_table(self):
        value = random.randint(0, 100)

        for row in range(self.max_rows - 1, 0, -1):
            item = self.table_widget.item(row - 1, 0)
            if item is not None:
                self.table_widget.setItem(row, 0, QTableWidgetItem(item.text()))
                self.table_widget.item(row, 0).setTextAlignment(Qt.AlignCenter)

        item = QTableWidgetItem(str(value))
        item.setTextAlignment(Qt.AlignCenter)
        self.table_widget.setItem(0, 0, item)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.setGeometry(600, 300, 400, 300)
    main_window.show()

    sys.exit(app.exec_())
