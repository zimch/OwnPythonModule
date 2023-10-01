from .gui.application import Application

def app():
    app = Application([])
    
    quit(app.exec())
        