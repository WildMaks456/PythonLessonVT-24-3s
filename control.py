# Вариант 4

import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow, QLabel

class Singleton:
    def __init__ (self):
        self.count = 0
    
    def increment(self):
        self.count = self.count + 1

    def getCount(self):
        return self.count

class Win1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Win1")
        self.setGeometry(400, 400, 400, 400)

        layuot = QVBoxLayout()

        self.button = QPushButton("counter +1")
        self.button.clicked.connect(self.open_second_window)
        container = QWidget()
        container.setLayout(layuot)
        self.setCentralWidget(container)
        layuot.addWidget(self.button)
        self.incr = Singleton()
        self.incr.increment()

    def open_second_window(self):
        self.second_window = Win2()
        self.second_window.show()


class Win2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Win2")
        self.setGeometry(400, 400, 400, 400)

        self.count = Singleton()

        self.label = QLabel(f"Count {self.count.getCount()}")
        layuot = QVBoxLayout()
        container = QWidget()
        container.setLayout(layuot)
        self.setCentralWidget(container)
        layuot.addWidget(self.label)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Win1()
    second_win = Win2()
    main_win.show()
    second_win.show()
    sys.exit(app.exec())