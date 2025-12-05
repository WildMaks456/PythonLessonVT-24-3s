from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
import sys

class ProfileForm(QWidget):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Создание профиля")

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Имя")

        self.surname_input = QLineEdit()
        self.surname_input.setPlaceholderText("Фамилия")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.save_btn = QPushButton("Сохранить")
        self.save_btn.clicked.connect(self.save)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.name_input)
        left_layout.addWidget(self.surname_input)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.email_input)
        right_layout.addWidget(self.save_btn)

        main = QHBoxLayout()
        main.addLayout(left_layout)
        main.addLayout(right_layout)

        self.setLayout(main)

    def save(self):
        name = self.name_input.text()
        surname = self.surname_input.text()
        email = self.email_input.text()
        QMessageBox.information(self, "Сохранено",
                                f"Имя: {name}\nФамилия: {surname}\nEmail: {email}")

app = QApplication(sys.argv)
w = ProfileForm()
w.show()
sys.exit(app.exec_())
