# Вариант 10

import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow, QLabel, QInputDialog

class ExternalUser:
    def __init__(self, name):
        self.name = name

    def rename(self, new_name):
        self.name = new_name

    def get_info(self):
        return f"User: {self.name}"


class UserAdapter:
    def __init__(self, external_user, label: QLabel):
        self.user = external_user
        self.label = label
        self.update_label()

    def update_label(self):
        self.label.setText(self.user.get_info())

    def change_name(self):
        new_name, ok = QInputDialog.getText(None, "Изменить имя", "Новое имя:")
        if ok and new_name.strip():
            self.user.rename(new_name.strip())
            self.update_label()


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.btn = QPushButton("Изменить имя")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        self.setLayout(layout)

        user = ExternalUser("Никита")

        self.adapter = UserAdapter(user, self.label)

        self.btn.clicked.connect(self.adapter.change_name)





if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.setWindowTitle("Задание 1")
    win.show()
    sys.exit(app.exec())