from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtWidgets import QMessageBox



class BaseButton(QPushButton):
    """Базовый класс кнопки с текстом."""
    def __init__(self, text):
        super().__init__(text)


class DangerButton(BaseButton):
    """Красная опасная кнопка."""
    def __init__(self):
        super().__init__("Опасная кнопка")
        self.setStyleSheet("background: #d9534f; color: white;")


class SuccessButton(BaseButton):
    """Зелёная кнопка успеха."""
    def __init__(self):
        super().__init__("Успех")
        self.setStyleSheet("background: #5cb85c; color: white;")


class DefaultButton(BaseButton):
    """Обычная кнопка."""
    def __init__(self):
        super().__init__("Обычная кнопка")



class ButtonFactory:
    @staticmethod
    def create_button(button_type: str) -> QPushButton:
        t = button_type.lower()
        if t == "опасная":
            return DangerButton()
        elif t == "успех":
            return SuccessButton()
        elif t == "обычная":
            return DefaultButton()
        else:
            return None



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Фабрика кнопок")

        self.layout = QVBoxLayout()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Введите тип: опасная / успех / обычная")

        self.create_btn = QPushButton("Создать")
        self.create_btn.clicked.connect(self.create_button)

        self.info = QLabel("")

        self.layout.addWidget(self.input)
        self.layout.addWidget(self.create_btn)
        self.layout.addWidget(self.info)

        self.setLayout(self.layout)

    def create_button(self):
        btn_type = self.input.text().strip()
        button = ButtonFactory.create_button(btn_type)

        if button is None:
            self.info.setText("Неверный тип кнопки!")
        else:
            self.info.setText("Кнопка добавлена ниже")
            self.layout.addWidget(button)



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()