from PyQt5.QtWidgets import (
    QMainWindow,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QComboBox,
)
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject

from my_module.math_module import MathHelper


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()
    
    def init_ui(self):    
        self.input_one = QLineEdit()
        self.input_two = QLineEdit()
        
        self.combobox = QComboBox()
        self.combobox.addItems(['+', '-', '/', "*"])

        self.btn = QPushButton("Count", self)
        self.btn.clicked.connect(self.count_math)
        
        self.result = QLabel()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.input_one)
        self.layout.addWidget(self.input_two)
        self.layout.addWidget(self.combobox)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.result)

        container = QWidget()
        container.setLayout(self.layout)

        self.setCentralWidget(container)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Math Helper')
        self.show()

    @pyqtSlot()
    def count_math(self):
        print('clicked')
        
        helper = MathHelper()
        
        try:
            num_one = int(self.input_one.text())
            num_two = int(self.input_two.text())
        except:
            print('lalala')
            self.result.setText('Some problem...')
        
        try:
            match self.combobox.currentText():
                case '+':
                    self.result.setText(str(helper.plus(num_one, num_two)))
                case '-':
                    self.result.setText(str(helper.minus(num_one, num_two)))
                case '*':
                    self.result.setText(str(helper.multiply(num_one, num_two)))
                case '/':
                    self.result.setText(str(helper.division(num_one, num_two)))
                    
        except:
            print('lalala1')
            self.result.setText('Some problem...')
    