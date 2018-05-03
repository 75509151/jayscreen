import curses
from widget import Widget


class Button(Widget):
    _selectable = True

    def __init__(self, parent, name, size=None, pos=None):
        if size is None:
            h = len(name.split("\n")) + 2
            w = len(max(name.split("\n"), key=len)) + 2
            size = (w, h)
        super(Button, self).__init__(parent, size, pos)

        self.name = name

    def show(self):
        self._win.box()
        self._win.insstr(1,1, self.name)

