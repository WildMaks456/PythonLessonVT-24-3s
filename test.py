import sys
from PyQt5.QtWidgets import *
#3 задание 1 ☺

class FormProduct:
    def __init__(self):
        self.layout = QVBoxLayout()

    def add_widget(self, widget):
        self.layout.addWidget(widget)


class FormBuilder:
    def __init__(self):
        self.product = FormProduct()
    
    def add_title(self):
        pass
    
    def add_inputs(self):
        pass
    
    def add_controls(self):
        pass
    
    def get_result(self):
        return self.product


class MiniFormBuilder(FormBuilder):
    def add_title(self):
        label = QLabel("Мини-форма")
        self.product.add_widget(label)
    
    def add_inputs(self):
        edit = QLineEdit()
        edit.setPlaceholderText("мини ввод")
        self.product.add_widget(edit)
    
    def add_controls(self):
        btn = QPushButton("посчитать")
        self.product.add_widget(btn)


class FullFormBuilder(FormBuilder):
    def add_title(self):
        label = QLabel("Расширенная форма")
        self.product.add_widget(label)
    
    def add_inputs(self):
        self.product.add_widget(QLabel("Цена:"))
        self.product.add_widget(QLineEdit())
        self.product.add_widget(QLabel("Процент:"))
        self.product.add_widget(QLineEdit())
    
    def add_controls(self):
        hbox = QHBoxLayout()
        hbox.addWidget(QPushButton("Посчитать"))
        
        widget = QWidget()
        widget.setLayout(hbox)
        self.product.add_widget(widget)


class FormDirector:
    def __init__(self, builder):
        self.builder = builder
    
    def build_form(self):
        self.builder.add_title()
        self.builder.add_inputs()
        self.builder.add_controls()
        return self.builder.get_result()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("bob the builder")
        self.setGeometry(100, 100, 400, 400)
        
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("миНИ"))
        mini_builder = MiniFormBuilder()
        director = FormDirector(mini_builder)
        mini_product = director.build_form()
        mini_widget = QWidget()
        mini_widget.setLayout(mini_product.layout)
        layout.addWidget(mini_widget)
        
        layout.addWidget(QLabel(" Расширенная форма"))
        full_builder = FullFormBuilder()
        director = FormDirector(full_builder)
        full_product = director.build_form()
        full_widget = QWidget()
        full_widget.setLayout(full_product.layout)
        layout.addWidget(full_widget)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())










