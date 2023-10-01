from pytestqt.qt_compat import qt_api

from my_module.gui.widgets import Window

def test_warning(qtbot):
    window = Window()
    window.show()
    qtbot.addWidget(window)
    
    window._input_one.clear()
    window._input_one.setText("2")
    
    window._input_two.clear()
    window._input_two.setText("2")
    
    window._combobox.clear()
    window._combobox.setCurrentText('+')
    
    window._btn.click()
    
    assert window._result.text() == "4"