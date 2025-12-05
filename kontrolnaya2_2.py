# вариант 2 Задание 2
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel, QSizePolicy
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Второе задание")
        self.resize(300, 100)

        self.left_first = QLineEdit()
        self.left_first.setPlaceholderText("login")
        self.left_second = QLineEdit()
        self.left_second.setPlaceholderText("password")

        self.left_third = QPushButton("войти")
        self.left_third.setFixedWidth(100)

        self.right_first = QLabel("label")
        self.right_first.setAlignment(Qt.AlignCenter)
        self.right_first.setFixedWidth(100)

        self.right_second = QPushButton("регистрация")
        self.right_second.setFixedWidth(140)

        self.vb_left = QVBoxLayout()
        self.vb_left.setSpacing(12)
        self.vb_left.addWidget(self.left_first)
        self.vb_left.addWidget(self.left_second)
        self.vb_left.addWidget(self.left_third)
        self.vb_left.addStretch(1)

        self.vb_right = QVBoxLayout()
        self.vb_right.setSpacing(12)
        self.vb_right.addWidget(self.right_first)
        self.vb_right.addWidget(self.right_second)
        self.vb_right.addStretch(1)

        self.mlayout = QHBoxLayout()
        self.mlayout.setSpacing(20)
        self.mlayout.addLayout(self.vb_left)
        self.mlayout.addLayout(self.vb_right)

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.mlayout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())