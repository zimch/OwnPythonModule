from gi.repository import Gtk

from matplotlib.backends.backend_gtk4agg import \
    FigureCanvasGTK4Agg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
import numpy as np

from .model import PlotData


class Window(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        Gtk.ApplicationWindow.__init__(self, *args, **kwargs)
        app = kwargs['application']

        self.is_anim_active = False

        self.fig = Figure(figsize=(5, 4), dpi=100, constrained_layout=False)
        self.ax = self.fig.add_subplot()
        self.line = None

        color = (0.96, 0.96, 0.96)
        self.fig.set_facecolor(color)
        self.ax.set_facecolor(color)

        sw = Gtk.ScrolledWindow(margin_top=10, margin_bottom=10,
                            margin_start=10, margin_end=10)

        self.set_child(sw)
        self.ani = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, )
        sw.set_child(vbox)

        box = Gtk.Box(spacing=5)
        vbox.append(box)

        button_add_point = Gtk.Button()
        button_add_point.set_label("Добавить")

        button_add_point.connect('clicked', self.add_point)

        button_show_anim = Gtk.Button()
        button_show_anim.set_label("Анимация")

        button_show_anim.connect('clicked', self.show_animated_plot)

        self.data = PlotData()

        self.edit_x = Gtk.SpinButton(name="X", value=0)
        self.edit_y = Gtk.SpinButton(name="Y", value=0)

        for edit in {self.edit_x, self.edit_y}:
            edit.set_adjustment(Gtk.Adjustment(upper=100, step_increment=1, page_increment=10))

        button_quit = Gtk.Button()
        button_quit.set_label("Выйти")
        button_quit.connect('clicked', lambda x: app.quit())

        controls = (button_add_point, self.edit_x, self.edit_y, button_quit, button_show_anim)
        for c in controls:
            box.append(c)

        self.canvas = FigureCanvas(self.fig)
        self.canvas.set_size_request(800, 600)
        vbox.append(self.canvas)

    def add_point(self, *args, **kwargs):
        self.data.add_point(self.edit_x.get_value(), self.edit_y.get_value())
        if self.line is not None:
            self.line.remove()

        self.line, = self.ax.plot(*self.data)
        self.canvas.draw()

    def show_animated_plot(self, *args, **kwargs):
        if self.is_anim_active:
            self.ani.event_source.stop()
            self.ax.cla()
            self.ax.plot(*self.data)
            self.canvas.draw()
            self.is_anim_active = False

        else:
            t = np.linspace(0, 3, 40)
            g = -9.81

            v0 = 12
            z = g * t ** 2 / 2 + v0 * t

            v02 = 5
            z2 = g * t ** 2 / 2 + v02 * t

            scat = self.ax.scatter(t[0], z[0], c="b", s=5)
            line2 = self.ax.plot(t[0], z2[0])[0]

            self.is_anim_active = True

            def update(frame):
                x = t[:frame]
                y = z[:frame]
                data = np.stack([x, y]).T
                scat.set_offsets(data)
                line2.set_xdata(t[:frame])
                line2.set_ydata(z2[:frame])
                return [scat, line2]

            self.ani = animation.FuncAnimation(fig=self.fig, func=update, frames=40, interval=30)

            self.canvas.draw()

