# Вариант 10

import sys
from PyQt5.QtWidgets import  QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem

class Converter(QWidget):
    def __init__(self):
        super().__init__()

        self.input = QLineEdit()
        self.btn_m = QPushButton("В метры")
        self.btn_cm = QPushButton("В сантиметры")
        self.btn_dm = QPushButton("В дециметры")
        self.result = QLabel("Результат: ")

        # таблица
        self.table = QTableWidget(3, 2)
        self.table.setHorizontalHeaderLabels(["Мера", "В см"])

        data = [
            ("1 м", "100"),
            ("1 см", "1"),
            ("1 дм", "10"),
        ]

        for r, (name, value) in enumerate(data):
            self.table.setItem(r, 0, QTableWidgetItem(name))
            self.table.setItem(r, 1, QTableWidgetItem(value))

        btns = QHBoxLayout()
        btns.addWidget(self.btn_m)
        btns.addWidget(self.btn_cm)
        btns.addWidget(self.btn_dm)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addLayout(btns)
        layout.addWidget(self.table)
        layout.addWidget(self.result)

        self.setLayout(layout)

        self.btn_m.clicked.connect(self.to_meters)
        self.btn_cm.clicked.connect(self.to_cm)
        self.btn_dm.clicked.connect(self.to_dm)


    def convert(self, unit):
        try:
            value = float(self.input.text())
        except:
            self.result.setText("Ошибка: введите число")
            return

        if unit == "m":
            res = value / 100
        elif unit == "cm":
            res = value
        elif unit == "dm":
            res = value / 10
    

        self.result.setText(f"Результат: {res}")
    
    def to_meters(self):
        self.convert("m")

    def to_cm(self):
        self.convert("cm")

    def to_dm(self):
        self.convert("dm")


if __name__ == "__main__":
    app = QApplication([])
    win = Converter()
    win.setWindowTitle("Задание 2")
    win.show()
    sys.exit(app.exec())