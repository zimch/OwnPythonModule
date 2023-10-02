from pytestqt.qt_compat import qt_api

from my_module.gui.widgets import Window
from my_module.gui.application import Application

import PyQt5.QtCore
print(PyQt5.QtCore)

class TestGUI:
    def test_warning(self, qtbot):
        # app = Application([])
        window = Window()
        window.show()
        qtbot.addWidget(window)
        
        window.input_one.setText("2")
        window.input_two.setText("2")
        window.combobox.setCurrentText('+')
        
        qtbot.mouseClick(window.btn, qt_api.QtCore.Qt.MouseButton.LeftButton)
        
        assert window.result.text() == "4"