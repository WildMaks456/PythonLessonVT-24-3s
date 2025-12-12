import sys
from PyQt5.QtWidgets import *
# dawdawdaw

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout1 = QVBoxLayout()
        self.layout2 = QHBoxLayout()

        self.label_number = QLabel("Цена:")
        self.input_number = QLineEdit()

        self.label_percent = QLabel("Процент:")
        self.input_percent = QLineEdit()

        self.calculate_button = QPushButton("Посчитать")
        self.calculate_button.clicked.connect(self.calculate_discount)

        self.label_result = QLabel("Результат:")
        self.output_result = QLineEdit()

        self.layout2.addWidget(self.label_number)


        self.layout1.addWidget(self.input_number)
        self.layout1.addWidget(self.label_percent)
        self.layout1.addWidget(self.input_percent)
        self.layout1.addWidget(self.calculate_button)
        self.layout1.addWidget(self.label_result)
        self.layout1.addWidget(self.output_result)

        self.layout1.addLayout(self.layout2)
        
        self.setLayout(self.layout1)

    def calculate_discount(self):
            number = float(self.input_number.text())
            percent = float(self.input_percent.text())
            
            result = number * (1 - percent / 100)
            
            self.output_result.setText(f"{result:.2f}")
            


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 600, 800, 800)
        self.setWindowTitle("Калькуляторррр")
        
        calculator = Calculator()

        
        self.setCentralWidget(calculator)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

