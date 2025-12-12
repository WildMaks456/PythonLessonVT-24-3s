import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QCheckBox
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt
import json
import re


with open('users.json', 'r', encoding='utf-8') as f:
    users = json.load(f)



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.start()
        self.start2()
        self.start3()
        
    def start(self):
        self.setWindowTitle("Фильтрация данных")
        self.setGeometry(300, 200, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Введите текст для фильтрации")

        self.res = ""
        self.label = QLabel("")

        self.layout.addWidget(self.label, Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.input_field)

        self.checkbox = QCheckBox("Учитывать регистр")

    def toggle_button_color(self):
            if self.checkbox.isChecked():
                self.btn_apply.setStyleSheet("background-color: red; color:white; font-weight: bold;")
            else:
                self.btn_apply.setStyleSheet("background-color: green; color:white; font-weight: bold;")

    def start2(self):
        self.checkbox.stateChanged.connect(self.toggle_button_color)
        self.layout.addWidget(self.checkbox)

        self.btn_apply = QPushButton("Применить")
        self.btn_apply.setStyleSheet("background-color: green; color:white; font-weight: bold;")
    
 

        

    def apply_filter(self):
        kluch = self.input_field.text()
        text = ""
        if self.checkbox.isChecked():
            case = "С учётом регистра"
            for user in users:
                name = user.get("name", "")
                if any(kluch in ch for ch in name):
                    text += name + " "

        else:
            case = "Без учёта регистра"
            for user in users:
                name = user.get("name", "")
                if any(kluch.lower() in ch.lower() for ch in name):
                    text += name + " "
            
        self.label.setText(f"Фильтр: {text}\n{case}")

    def start3(self):
        self.btn_apply.clicked.connect(self.apply_filter)
        self.layout.addWidget(self.btn_apply)




app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())