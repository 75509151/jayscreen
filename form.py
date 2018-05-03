from widget import Widget


class Form(Widget):
    def __init__(self, parent, size, pos=None):
        super(Form, self).__init__(parent, size, pos)
        self.active_widget = None

    def show(self):
        self._win.clear()
        for widget in self.widgets:
            widget.show()
            widget._win.refresh()
        self._win.box()
        self._win.refresh()
