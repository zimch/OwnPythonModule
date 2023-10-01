from datetime import datetime

def update_label(self):
    self.input_changed.emit(datetime.now())
    self.label.setText(self.edit.toPlainText())