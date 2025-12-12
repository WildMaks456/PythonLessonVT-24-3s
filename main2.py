import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QCheckBox, QFrame, QGroupBox
)
from PyQt5.QtCore import Qt


class LabelComponent:
    def get_widget(self):
        raise NotImplementedError


class BaseLabel(LabelComponent):
    def __init__(self, text: str):
        self.label = QLabel(text)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMinimumHeight(40)

    def get_widget(self):
        return self.label


class LabelDecorator(LabelComponent):
    def __init__(self, component: LabelComponent):
        self.component = component

    def get_widget(self):
        return self.component.get_widget()


class TextPrefixDecorator(LabelDecorator):
    def __init__(self, component: LabelComponent, prefix: str):
        super().__init__(component)
        self.prefix = prefix

    def get_widget(self):
        w = self.component.get_widget()
        w.setText(self.prefix + w.text())
        return w


class BackgroundDecorator(LabelDecorator):
    def __init__(self, component: LabelComponent, color: str):
        super().__init__(component)
        self.color = color

    def get_widget(self):
        w = self.component.get_widget()
        w.setStyleSheet(f"background: {self.color}; padding: 5px;")
        return w


class FrameDecorator(LabelDecorator):
    def __init__(self, component: LabelComponent):
        super().__init__(component)

    def get_widget(self):
        label = self.component.get_widget()

        label.setParent(None)

        frame = QFrame()
        frame.setFrameShape(QFrame.Box)
        frame.setLineWidth(2)

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.addWidget(label)

        return frame


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Паттерн Декоратор — Label")
        self.resize(500, 300)

        layout = QVBoxLayout(self)

        self.base = BaseLabel("Пример текста")

        self.output = QVBoxLayout()
        self._update_output(self.base.get_widget())

        cb_group = QGroupBox("Выберите декораторы")
        cb_layout = QHBoxLayout(cb_group)

        self.cb_prefix = QCheckBox("Префикс '>> '")
        self.cb_bg = QCheckBox("Фон (жёлтый)")
        self.cb_frame = QCheckBox("Рамка")

        cb_layout.addWidget(self.cb_prefix)
        cb_layout.addWidget(self.cb_bg)
        cb_layout.addWidget(self.cb_frame)

        btn = QPushButton("Обновить Label")
        btn.clicked.connect(self.apply_decorators)

        reset = QPushButton("Сбросить")
        reset.clicked.connect(self.reset)

        layout.addWidget(cb_group)
        layout.addWidget(btn)
        layout.addWidget(reset)
        layout.addLayout(self.output)

    def _update_output(self, widget):
        while self.output.count():
            item = self.output.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()
        self.output.addWidget(widget)

    def apply_decorators(self):
        comp = BaseLabel("Пример текста")

        if self.cb_prefix.isChecked():
            comp = TextPrefixDecorator(comp, ">> ")

        if self.cb_bg.isChecked():
            comp = BackgroundDecorator(comp, "#FFFF99")

        if self.cb_frame.isChecked():
            comp = FrameDecorator(comp)

        widget = comp.get_widget()
        self._update_output(widget)

    def reset(self):
        self.cb_prefix.setChecked(False)
        self.cb_bg.setChecked(False)
        self.cb_frame.setChecked(False)
        self._update_output(BaseLabel("Пример текста").get_widget())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
