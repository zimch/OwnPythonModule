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
        self._input_one = QLineEdit()
        self._input_two = QLineEdit()
        
        self._combobox = QComboBox()
        self._combobox.addItems(['+', '-', '/', "*"])

        self._btn = QPushButton("Count", self)
        self._btn.clicked.connect(self.count_math)
        
        self._result = QLabel()

        self._layout = QVBoxLayout()
        self._layout.addWidget(self._input_one)
        self._layout.addWidget(self._input_two)
        self._layout.addWidget(self._combobox)
        self._layout.addWidget(self._btn)
        self._layout.addWidget(self._result)

        _container = QWidget()
        _container.setLayout(self._layout)

        self.setCentralWidget(_container)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Math Helper')
        self.show()

    @pyqtSlot()
    def count_math(self):
        print('clicked')
        
        helper = MathHelper()
        
        try:
            num_one = int(self._input_one.text())
            num_two = int(self._input_two.text())
        except:
            self._result.setText('Some problem...')
        
        try:
            match self._combobox.currentText():
                case '+':
                    self._result.setText(str(helper.plus(num_one, num_two)))
                case '-':
                    self._result.setText(str(helper.minus(num_one, num_two)))
                case '*':
                    self._result.setText(str(helper.multiply(num_one, num_two)))
                case '/':
                    self._result.setText(str(helper.division(num_one, num_two)))
                    
        except:
            self._result.setText('Some problem...')
    