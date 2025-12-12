# 8 вариант

import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QComboBox, QVBoxLayout, QHBoxLayout, QProgressBar, QGroupBox
)
from PyQt5.QtCore import Qt, QTimer


class EmailChecker(QWidget):
    def __init__(self):
        super().__init__()  
        self.setWindowTitle("Проверка email")
        self.resize(500, 300)

        layout = QVBoxLayout(self)

        input_box = QGroupBox("Введите email (часть без домена)")
        input_layout = QHBoxLayout(input_box)

        self.input_user = QLineEdit()
        self.input_user.setPlaceholderText("например: ivan.ivanov")

        self.combo = QComboBox()
        self.combo.addItems([".kz", ".com", ".ru"])

        input_layout.addWidget(self.input_user)
        input_layout.addWidget(self.combo)

        btn_layout = QHBoxLayout()
        self.btn_check = QPushButton("Проверить")
        self.btn_clear = QPushButton("Очистить")

        btn_layout.addWidget(self.btn_check)
        btn_layout.addWidget(self.btn_clear)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)

        self.status = QLabel("Статус проверки")
        self.status.setAlignment(Qt.AlignCenter)

        self.result = QLabel("")
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setStyleSheet("font-weight: bold;")

        layout.addWidget(input_box)
        layout.addLayout(btn_layout)
        layout.addWidget(self.progress)
        layout.addWidget(self.status)
        layout.addWidget(self.result)

        self.timer = QTimer()
        self.timer.timeout.connect(self._animate)

        self.btn_check.clicked.connect(self.start_check)
        self.btn_clear.clicked.connect(self.clear)

    def start_check(self):
        self.btn_check.setEnabled(False)
        self.progress.setValue(0)
        self.status.setText("Проверка...")
        self.result.setText("")
        self.input_user.setStyleSheet("background: yellow;")

        self.timer.start(20)

    def _animate(self):
        v = self.progress.value()
        if v >= 100:
            self.timer.stop()
            self.finish()
        else:
            self.progress.setValue(v + 2)

    def finish(self):
        self.btn_check.setEnabled(True)
        self.input_user.setStyleSheet("")
        user = self.input_user.text().strip()

        if self._valid(user):
            full = f"{user}{self.combo.currentText()}"
            self.result.setText(f"корректно — {full}")
            self.result.setStyleSheet("color: green; font-weight: bold;")
        else:
            self.result.setText("некорректно")
            self.result.setStyleSheet("color: red; font-weight: bold;")

        self.status.setText("Проверка завершена")

    def _valid(self, txt):
        if not txt:
            return False
        if ".." in txt:
            return False
        if txt.startswith(".") or txt.endswith("."):
            return False
        return bool(re.fullmatch(r"[A-Za-z0-9._\-]+", txt))

    def clear(self):
        self.input_user.clear()
        self.progress.setValue(0)
        self.result.setText("")
        self.status.setText("Статус проверки")
        self.input_user.setStyleSheet("")
        self.btn_check.setEnabled(True)


if __name__ == "__main__": 
    app = QApplication(sys.argv)
    w = EmailChecker()
    w.show()
    sys.exit(app.exec_())
