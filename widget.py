from glo import scr
import curses

class Widget(object):
    def __init__(self, parent, size, pos=None, can_focus=False):
        super(Widget, self).__init__()
        self.w = size[0]
        self.h = size[1]
        self.parent = parent
        self.widgets = []
        self.can_focus = can_focus
        if pos:
            self.x = pos[0]
            self.y = pos[1]
        else:
            self.x = 0
            self.y = 0
        if not parent:
            self.win = curses.newwin(self.h, self.w, self.y, self.x)
        else:
            self.parent.win.derwin(self.h, self.w, self.y, self.x)


    def add_widget(self, widget):
        self.widgets.append(widget)

    def get_focus(self):
        pass

    def lose_focus(self):
        pass

    def bind(self, action, widget, callback):
        print "widget: %s, action: %s, callback: %s " % (widget, action, callback)

    def key_listern(self):
        pass

    def show(self):
        raise NotImplementedError()

