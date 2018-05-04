from widget import Widget
import styles


class Form(Widget):
    def __init__(self, parent, size, pos=None, style=styles.HAS_BOX):
        super(Form, self).__init__(parent, size, pos, style)
        self.active_widget = None

    def show(self):
        super(Form, self).show()
        self._win.clear()
        for widget in self.widgets:
            widget.show()
            widget._win.refresh()

        self._show_according_style()
        self._win.refresh()


