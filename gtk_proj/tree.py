from gi.repository import Gtk
import json


with open("data.json") as file:
    json_data = json.load(file)

store = Gtk.TreeStore(str)


def add_items(parent_iter, data):
    if isinstance(data, dict):
        for key, value in data.items():
            iter = store.append(parent_iter, [str(key)])
            add_items(iter, value)
    elif isinstance(data, list):
        for item in data:
            iter = store.append(parent_iter, [""])
            add_items(iter, item)
    else:
        store.append(parent_iter, [str(data)])


root_iter = store.append(None, ["JSON"])
print(json_data)
add_items(root_iter, json_data)

view = Gtk.TreeView(model=store)

renderer = Gtk.CellRendererText()
column = Gtk.TreeViewColumn("data", renderer, text=0)
view.append_column(column)