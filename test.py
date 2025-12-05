import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
#3 вариант



class FromProduct:
    
    def __init__(self):
        self.layout = QVBoxLayout()

    def add_widget(self,widget):
        self.layout.addWidget(widget)

    class FromDirector:

        def __init__(self,builder):
            self.builder = builder

        def build_form(self):
            self.builder.add_title()
            self.builder.add_inputs()
            self.builder.add_controls()
            return self.builder.get_result()
        
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()