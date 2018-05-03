import curses
from glo import scr
from key_listern import KeyListern


class Widget(KeyListern):
    _selectable = False

    def __init__(self, parent, size, pos=None):
        super(Widget, self).__init__()
        self.w = size[0]
        self.h = size[1]
        self.parent = parent
        self.widgets = []
        if pos:
            self.x = pos[0]
            self.y = pos[1]
        else:
            self.x = 0
            self.y = 0
        if not parent:
            self._win = curses.newwin(self.h, self.w, self.y, self.x)
        else:
            self._win = self.parent._win.derwin(self.h, self.w, self.y, self.x)


    def add(self, widget):
        self.widgets.append(widget)

    def get_focus(self):
        pass

    def lose_focus(self):
        pass

    def show(self):
        raise NotImplementedError()

    def hide(self):
        # TODO: how to implete hide
        return
        raise NotImplementedError()

    def selectable(self):
        return self._selectable

