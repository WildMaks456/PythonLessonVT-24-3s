# вариант 2 Задание 1
import sys
from abc import ABC, abstractmethod
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel
)
from PyQt5.QtCore import Qt


class LineEditCreator(ABC):
    def create_line_edit(self) -> QLineEdit:
        pass


class HighlightLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("подсветка")
        self._base_style = "padding:4px; border:1px solid #bbb; border-radius:4px;"
        self._focus_style = self._base_style + "background-color: #FFFF00;"
        self.setStyleSheet(self._base_style)

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.setStyleSheet(self._focus_style)

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.setStyleSheet(self._base_style)


class PasswordLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("пароль")
        self.setEchoMode(QLineEdit.Password)
        self.setStyleSheet("padding:4px; border:1px solid #bbb; border-radius:4px;")


class FramedLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("рамка")
        self.setStyleSheet("padding:6px; border:2px solid #4a90e2; border-radius:6px; background-color: white;")

class HighlightCreator(LineEditCreator):
    def create_line_edit(self) -> QLineEdit:
        return HighlightLineEdit()

class PasswordCreator(LineEditCreator):
    def create_line_edit(self) -> QLineEdit:
        return PasswordLineEdit()

class FramedCreator(LineEditCreator):
    def create_line_edit(self) -> QLineEdit:
        return FramedLineEdit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Первое задание")
        self.resize(300, 100)

        self.current_creator: LineEditCreator = HighlightCreator()

        central = QWidget()
        self.setCentralWidget(central)
        self.main_vlayout = QVBoxLayout(central)
        self.main_vlayout.setSpacing(12)

        self.input_area = QVBoxLayout()
        self.main_vlayout.addLayout(self.input_area)

        btn_layout = QHBoxLayout()
        self.btn_highlight = QPushButton("Highlight")
        self.btn_password = QPushButton("Password")
        self.btn_framed = QPushButton("Framed")

        btn_layout.addWidget(self.btn_highlight)
        btn_layout.addWidget(self.btn_password)
        btn_layout.addWidget(self.btn_framed)
        btn_layout.addStretch(1)

        self.main_vlayout.addLayout(btn_layout)

        self.btn_highlight.clicked.connect(self.use_highlight)
        self.btn_password.clicked.connect(self.use_password)
        self.btn_framed.clicked.connect(self.use_framed)

        self._current_line_edit = None
        self.recreate_line_edit()

    def recreate_line_edit(self):
        if self._current_line_edit is not None:
            self.input_area.removeWidget(self._current_line_edit)
            self._current_line_edit.hide()
            self._current_line_edit.deleteLater()
            self._current_line_edit = None

        new_edit = self.current_creator.create_line_edit()
        new_edit.setMinimumHeight(30)
        self.input_area.addWidget(new_edit)
        self._current_line_edit = new_edit
        new_edit.setFocus()

    def use_highlight(self):
        self.current_creator = HighlightCreator()
        self.recreate_line_edit()

    def use_password(self):
        self.current_creator = PasswordCreator()
        self.recreate_line_edit()

    def use_framed(self):
        self.current_creator = FramedCreator()
        self.recreate_line_edit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
