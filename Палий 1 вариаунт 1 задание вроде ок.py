"""1 Варинат 1 Задание Палий ВТ-24-3С"""

from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout

class BaseButton(QPushButton):
    def __init__(self, name):
        super().__init__(name)


class DangerButton(BaseButton):
    def __init__(self, name="Опасная кнопка"):
        super().__init__(name)
        self.setStyleSheet("background: #d9534f; color: white;")


class SuccessButton(BaseButton):
    def __init__(self, name="Успех"):
        super().__init__(name)
        self.setStyleSheet("background: #5cb85c; color: white;")


class DefaultButton(BaseButton):
    def __init__(self, name="Обычная кнопка"):
        super().__init__(name)

BUTTON_STYLES = {
    "danger": "background:#d9534f; color:white;",
    "success": "background:#5cb85c; color:white;",
    "default": ""
}

class StyledButton(QPushButton):
    def __init__(self, name, style="default"):
        super().__init__(name)
        self.setStyleSheet(BUTTON_STYLES[style])
