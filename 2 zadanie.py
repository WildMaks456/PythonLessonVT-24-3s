#5 вариант


import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt


class ControlPanel(QMainWindow):
    """Панель управления"""
    def __init__(self):
        super().__init__()
        self.is_running = False
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Панель управления')
        self.setGeometry(100, 100, 400, 200)
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        
        self.status_label = QLabel("Ожидание")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.update_status_style()
        layout.addWidget(self.status_label)
        
        param_layout = QHBoxLayout()
        param_label = QLabel("Параметр:")
        self.param_input = QLineEdit()
        self.param_input.setPlaceholderText("Введите значение...")
        param_layout.addWidget(param_label)
        param_layout.addWidget(self.param_input)
        layout.addLayout(param_layout)
        
        buttons_layout = QHBoxLayout()
        
        self.start_btn = QPushButton("Старт")
        self.start_btn.clicked.connect(self.start_action)
        buttons_layout.addWidget(self.start_btn)
        
        self.stop_btn = QPushButton("Стоп")
        self.stop_btn.clicked.connect(self.stop_action)
        self.stop_btn.setEnabled(False)
        buttons_layout.addWidget(self.stop_btn)
        
        layout.addLayout(buttons_layout)
        layout.addStretch()
        
        self.apply_styles()
    
    def apply_styles(self):
        """Применение стилей ко всем виджетам"""
        self.start_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                padding: 8px 20px;
                border-radius: 4px;
                border: none;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        
        self.stop_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                font-size: 14px;
                padding: 8px 20px;
                border-radius: 4px;
                border: none;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
    
    def update_status_style(self):
        """Обновление стиля статуса в зависимости от состояния"""
        if self.is_running:
            self.status_label.setStyleSheet("""
                QLabel {
                    font-size: 16px;
                    font-weight: bold;
                    padding: 10px;
                    background-color: #d4edda;
                    color: #155724;
                    border-radius: 5px;
                    border: 1px solid #c3e6cb;
                }
            """)
        else:
            self.status_label.setStyleSheet("""
                QLabel {
                    font-size: 16px;
                    font-weight: bold;
                    padding: 10px;
                    background-color: #f8f9fa;
                    color: #6c757d;
                    border-radius: 5px;
                    border: 1px solid #e9ecef;
                }
            """)
    
    def start_action(self):
        param = self.param_input.text().strip()
        if param:
            self.status_label.setText(f"Работает (параметр: {param})")
            self.is_running = True
            self.update_status_style()
            
            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
            self.param_input.setEnabled(False)
        else:
            QMessageBox.warning(self, "Внимание", "Введите значение параметра!")
    
    def stop_action(self):
        self.status_label.setText("Ожидание")
        self.is_running = False
        self.update_status_style()
        
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.param_input.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ControlPanel()
    window.show()
    sys.exit(app.exec_())