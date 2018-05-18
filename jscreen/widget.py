import curses
from key_listern import KeyListern
import styles


class BaseWidget(object):
    _selectable = False

    def __init__(self, parent, size, pos=None, style=styles.NO_STYLE):
        super(BaseWidget, self).__init__()
        self.w = size[0]
        self.h = size[1]
        self.parent = parent
        self.style = style
        self.widgets = []
        self._hide = False
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

    def hided(self):
        return self._hide

    def selectable(self):
        return self._selectable

    def get_focus(self):
        pass

    def lose_focus(self):
        pass

    def __render_style__(self):
        if self.style & styles.HAS_BOX:
            self._win.box()

    def render(self):
        raise NotImplementedError()


class ActionWidget(KeyListern):

    def __init__(self, parent, size, pos=None, style=styles.NO_STYLE):
        super(ActionWidget, self).__init__()
        self.setup_key_handlers()

    def show(self):
        self._hide = False
        self._win.clear()
        self.render()
        self._win.refresh()

    def hide(self):
        if self._hide:
            return
        self._hide = True

        self._win.clear()
        for widget in self.widgets:
            widget.hide()
            widget._win.refresh()
        self._win.refresh()
