from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import sys

class AppState:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AppState, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.counter = 0
            self._initialized = True 

    def inc(self):
        self.counter += 1

    def get(self):
        return self.counter

class Window1(QWidget):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Окно 1")
        self.resize(450, 300)
        self.state = AppState() 
        self.btn = QPushButton("Увеличить счётчик")
        self.btn.setMinimumHeight(40)
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        self.setLayout(layout)
        self.btn.clicked.connect(self.increase)

    def increase(self):
        self.state.inc()


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно 2")
        self.resize(350, 220)
        self.state = AppState()
        self.label = QLabel(f"Текущее значение: {self.state.get()}")
        self.label.setStyleSheet("font-size: 20px;")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def update_label(self):
        self.label.setText(f"Текущее значение: {self.state.get()}")


class App(QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.w1 = Window1()
        self.w2 = Window2()
        self.w1.btn.clicked.connect(self.w2.update_label)
        
        self.w1.move(100, 100)
        self.w2.move(600, 100)

        self.w1.show()
        self.w2.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
