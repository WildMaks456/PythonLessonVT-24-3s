from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QLabel
)
from PyQt5.QtCore import Qt


class AddProductForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Добавление товара")

        layout = QVBoxLayout()

    
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введите название товара")
     
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Введите цену")
        self.price_input.setValidator(None) 


        self.save_btn = QPushButton("Сохранить")
        self.save_btn.clicked.connect(self.save_product)

        self.hint_label = QLabel("Заполните все поля")
        self.hint_label.setAlignment(Qt.AlignCenter)
        self.hint_label.setStyleSheet("color: gray;")

        layout.addWidget(self.name_input)
        layout.addWidget(self.price_input)
        layout.addWidget(self.save_btn)
        layout.addWidget(self.hint_label)

        self.setLayout(layout)

    def save_product(self):
        name = self.name_input.text().strip()
        price = self.price_input.text().strip()

        if not name or not price:
            self.hint_label.setText("Все поля должны быть заполнены")
            self.hint_label.setStyleSheet("color: red;")
        else:
            self.hint_label.setText("Товар сохранён")
            self.hint_label.setStyleSheet("color: green;")

if __name__ == "__main__":
    app = QApplication([])
    window = AddProductForm()
    window.show()
    app.exec_()
