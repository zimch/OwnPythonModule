from gi.repository import Gtk
from matplotlib.backends.backend_gtk4agg import \
    FigureCanvasGTK4Agg as FigureCanvas
from matplotlib.figure import Figure
from .tree import view
from .model import PlotData


class Notebook(Gtk.Notebook):
    pass

class Confirmation(Gtk.MessageDialog):
    def __init__(self):
        Gtk.MessageDialog.__init__(self)
        self.set_markup('<b>Вы уверены?</b>')
        self.add_button('да', 1)
        self.add_button('нет', 0)

class Window(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        Gtk.ApplicationWindow.__init__(self, *args, **kwargs)
        app = kwargs['application']

        self.notebook = Notebook()

        intro = Gtk.ScrolledWindow()
        box = Gtk.Box()
        tab_label = Gtk.Label()
        tab_label.set_text("График")
        self.notebook.append_page(intro, tab_label)

        tab_label = Gtk.Label()
        tab_label.set_text("Список")

        fig = Figure(figsize=(5, 4), dpi=100, constrained_layout=True)
        self.ax = fig.add_subplot()
        self.line = None

        self.set_child(intro)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, )
        intro.set_child(vbox)

        box = Gtk.Box(spacing=5)
        vbox.append(box)

        button_add_point = Gtk.Button()
        button_add_point.set_label("Добавить")

        button_add_point.connect('clicked', self.add_point)

        self.data = PlotData()

        self.edit_x = Gtk.SpinButton(name="X", value=0)
        self.edit_y = Gtk.SpinButton(name="Y", value=0)

        for edit in {self.edit_x, self.edit_y}:
            edit.set_adjustment(Gtk.Adjustment(upper=100, step_increment=1, page_increment=10))

        button_quit = Gtk.Button()
        button_quit.set_label("Выйти")
        button_quit.connect('clicked', lambda x: app.quit())

        controls = (button_add_point, self.edit_x, self.edit_y, button_quit)
        for c in controls:
            box.append(c)

        self.canvas = FigureCanvas(fig)
        self.canvas.set_size_request(800, 600)
        vbox.append(self.canvas)

        self.notebook.append_page(view, tab_label)

        view.show()

        curr_page = 0

        try:
            with open("user_cache_dir.toml", "r") as f:
                curr_page = int(*f)
        except Exception:
            pass

        self.notebook.set_current_page(curr_page)

        self.set_child(self.notebook)
        self.show()

        self.app = kwargs['application']

        self.connect('close-request', self.handle_exit)

    def add_point(self, *args, **kwargs):
        self.data.add_point(self.edit_x.get_value(), self.edit_y.get_value())
        if self.line is not None:
            self.line.remove()

        self.line, = self.ax.plot(*self.data)
        self.canvas.draw()

    def handle_exit(self, _):
        dialog = Confirmation()
        dialog.set_transient_for(self)
        dialog.show()
        dialog.connect('response', self.exit)
        return True

    def exit(self, widget, response):
        with open("user_cache_dir.toml", "w") as f:
            f.write(str(self.notebook.get_current_page()))

        if response == 1:
            self.app.quit()
        widget.destroy()