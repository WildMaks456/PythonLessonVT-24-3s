# вариант 2
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Минимальный шаблон")
        self.resize(300, 150)

        self.x_edit = QLineEdit()
        self.x_edit.setPlaceholderText("Логин")

        self.y_edit = QLineEdit()
        self.y_edit.setPlaceholderText("Пароль")
        self.y_edit.setEchoMode(QLineEdit.Password)

        self.btn1 = QPushButton("Войти")
        self.big_button = QPushButton("Регистрация")

        self.label = QLabel("Поясняющий Label")
        self.label.setAlignment(Qt.AlignCenter)

        col = QVBoxLayout()
        col.addWidget(self.x_edit)
        col.addWidget(self.y_edit)
        col.addWidget(self.btn1)
        col.addWidget(self.big_button)

        top_layout = QHBoxLayout()
        top_layout.addStretch(1)
        top_layout.addLayout(col)
        top_layout.addStretch(1)

        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch(1)
        bottom_layout.addWidget(self.label)
        bottom_layout.addStretch(1)

        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
