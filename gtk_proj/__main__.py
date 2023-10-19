import gi
gi.require_version('Gtk', '4.0')

from gi.repository import Gtk
from .widgets import Window

class Application(Gtk.Application):

    def on_activate(self, _):
        win = Window(application=self)
        win.set_default_size(800, 800)
        win.set_title("Embedding in GTK4")
        win.set_visible(True)
        self.win = win
        self.connect('activate', self.on_activate)


app = Application(application_id='org.matplotlib.examples.EmbeddingInGTK4')
app.connect('activate', app.on_activate)


def monkeypatch():
    print('haha')


app.monkeypatch = monkeypatch

app.run(None)


# import matplotlib
#
# matplotlib.use('GTK4Agg')  # or 'GTK4Cairo'
# import gi
#
# import matplotlib.pyplot as plt
#
# gi.require_version('Gtk', '4.0')
# from gi.repository import Gtk
#
# fig, ax = plt.subplots()
# ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
# ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
# ax.legend()
#
# manager = fig.canvas.manager
# # you can access the window or vbox attributes this way
# toolbar = manager.toolbar
# vbox = manager.vbox
#
# # now let's add a button to the toolbar
# button = Gtk.Button(label='Click me')
# button.connect('clicked', lambda button: print('hi mom'))
# button.set_tooltip_text('Click me for fun and profit')
# toolbar.append(button)
#
# # now let's add a widget to the vbox
# label = Gtk.Label()
# label.set_markup('Drag mouse over axes for position')
# vbox.insert_child_after(label, fig.canvas)
#
#
# def update(event):
#     if event.xdata is None:
#         label.set_markup('Drag mouse over axes for position')
#     else:
#         label.set_markup(
#             f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')
#
#
# fig.canvas.mpl_connect('motion_notify_event', update)
#
# plt.show()