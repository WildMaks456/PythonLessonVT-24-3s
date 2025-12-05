#5 вариант



class BaseButton(ABC):
    @abstractmethod
    def click(self):
        pass
    
    @abstractmethod
    def get_widget(self):
        pass


class SimpleButton(BaseButton):
    def __init__(self, text):
        self.btn = QPushButton(text)
        self.btn.clicked.connect(self.click)
    
    def click(self):
        print("Base button clicked")
    
    def get_widget(self):
        return self.btn


class ButtonDecorator(BaseButton):
    def __init__(self, button):
        self._button = button
    
    def click(self):
        self._button.click()
    
    def get_widget(self):
        return self._button.get_widget()


class CounterDecorator(ButtonDecorator):
    def __init__(self, button):
        super().__init__(button)
        self.count = 0
        self.widget = button.get_widget()
        self.update_text()


    def click(self):
        self.count += 1
        self._button.click()
        self.update_text()
    
    def update_text(self):
        original = self.widget.text()
        base = original.split(' (')[0] if ' (' in original else original
        self.widget.setText(f"{base} ({self.count})")

class LoggingDecorator(ButtonDecorator):
    def click(self):
        print(f"LOG: Button clicked - {self.get_widget().text()}")
        self._button.click()

class StyleDecorator(ButtonDecorator):
    def __init__(self, button, style=""):
        super().__init__(button)
        self.widget = button.get_widget()
        self.style = style or """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """
        self.apply_style()
    
    def apply_style(self):
        self.widget.setStyleSheet(self.style)
    
    def click(self):
        self._button.click()

