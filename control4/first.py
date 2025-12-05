from PyQt5 import QtWidgets
from abc import ABC, abstractmethod

class FormProduct:
    def __init__(self):
        self.layout = QtWidgets.QVBoxLayout()

    def add_widget(self, widget):
        self.layout.addWidget(widget)

class FormBuilder(ABC):
    @abstractmethod
    def add_title(self, title):
        pass

    @abstractmethod
    def add_inputs(self):
        pass

    @abstractmethod
    def add_controls(self):
        pass

class MiniFormBuilder(FormBuilder):
    def __init__(self):
        self.__form = FormProduct()

    def add_title(self, title):
        label = QtWidgets.QLabel(title)
        self.__form.add_widget(label)
    
    def add_inputs(self):
        input = QtWidgets.QLineEdit()
        self.__form.add_widget(input)
    
    def add_controls(self):
        OkBtn = QtWidgets.QPushButton("OK")
        self.__form.add_widget(OkBtn)
        
    def get_form(self):
        return self.__form

class FullFormBuilder(FormBuilder):
    def __init__(self):
        self.__form = FormProduct()

    def add_title(self, title):
        label = QtWidgets.QLabel(title)
        self.__form.add_widget(label)
        
    def add_inputs(self):
        input1 = QtWidgets.QLineEdit()
        input2 = QtWidgets.QLineEdit()
        self.__form.add_widget(input1)
        self.__form.add_widget(input2)
    
    def add_controls(self):
        OkBtn = QtWidgets.QPushButton("OK")
        Option1Btn = QtWidgets.QPushButton("Option 1")
        Option2Btn = QtWidgets.QPushButton("Option 2")
        self.__form.add_widget(OkBtn)
        self.__form.add_widget(Option1Btn)
        self.__form.add_widget(Option2Btn)
    
    def get_form(self):
        return self.__form

class FormDirector:
    def __init__(self, builder):
        self.builder = builder
    
    def build_form(self, title):
        self.builder.add_title(title)
        self.builder.add_inputs()
        self.builder.add_controls()
        return self.builder.get_form()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        widget.setLayout(layout)
        miniFormDirector = FormDirector(MiniFormBuilder())
        fullFormDirector = FormDirector(FullFormBuilder())
        miniForm = miniFormDirector.build_form("Form 1")
        fullForm = fullFormDirector.build_form("Form 2")
        miniFormWidget = QtWidgets.QWidget()
        fullFormWidget = QtWidgets.QWidget()
        miniFormWidget.setLayout(miniForm.layout)
        fullFormWidget.setLayout(fullForm.layout)
        layout.addWidget(miniFormWidget)
        layout.addWidget(fullFormWidget)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()