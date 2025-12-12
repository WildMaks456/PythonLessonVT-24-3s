# 8 вариант

import sys
import re
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer

class EmailChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Проверка EMAIL")
        self.resize(400, 300)

        self.main = QVBoxLayout(self)

        self.group = QGroupBox("Введите email")
        self.hbox = QHBoxLayout(self.group)

        self.txt = QLineEdit()
        self.txt.setPlaceholderText("example")

        self.combo = QComboBox()
        self.combo.addItem(".kz")
        self.combo.addItem(".com")
        self.combo.addItem(".ru")

        self.hbox.addWidget(self.txt)
        self.hbox.addWidget(self.combo)

        self.btnCheck = QPushButton("Проверить")
        self.btnClear = QPushButton("Очистить")

        self.buttons = QHBoxLayout()
        self.buttons.addWidget(self.btnCheck)
        self.buttons.addWidget(self.btnClear)

        self.progress = QProgressBar()
        self.progress.setValue(0)

        self.status = QLabel("Статус проверки")
        self.status.setAlignment(Qt.AlignCenter)

        self.result = QLabel("")
        self.result.setAlignment(Qt.AlignCenter)

        self.main.addWidget(self.group)
        self.main.addLayout(self.buttons)
        self.main.addWidget(self.progress)
        self.main.addWidget(self.status)
        self.main.addWidget(self.result)

        self.timer = QTimer()
        self.timer.timeout.connect(self.load)

        self.btnCheck.clicked.connect(self.start)
        self.btnClear.clicked.connect(self.doClear)

    def start(self):
        self.progress.setValue(0)
        self.status.setText("Проверка...")
        self.result.setText("")
        self.btnCheck.setEnabled(False)
        self.txt.setStyleSheet("background-color: yellow")

        self.timer.start(30)

    def load(self):
        val = self.progress.value()
        if val >= 100:
            self.timer.stop()
            self.finishCheck()
        else:
            self.progress.setValue(val + 5)

    def finishCheck(self):
        self.btnCheck.setEnabled(True)
        self.txt.setStyleSheet("")
        email = self.txt.text()

        if email != "" and ".." not in email and not email.startswith(".") and not email.endswith("."):
            if re.fullmatch(r"[A-Za-z0-9._\-]+", email):
                self.result.setText("корректно — " + email + self.combo.currentText())
                self.result.setStyleSheet("color: green;")
            else:
                self.result.setText("некорректно")
                self.result.setStyleSheet("color: red;")
        else:
            self.result.setText("некорректно")
            self.result.setStyleSheet("color: red;")

        self.status.setText("Проверка завершена")

    def doClear(self):
        self.txt.clear()
        self.progress.setValue(0)
        self.status.setText("Статус проверки")
        self.result.setText("")
        self.txt.setStyleSheet("")
        self.btnCheck.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = EmailChecker()
    w.show()
    sys.exit(app.exec_())