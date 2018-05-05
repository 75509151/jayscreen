from widget import Widget
import styles


class Form(Widget):
    def __init__(self, parent, size, pos=None, style=styles.HAS_BOX):
        super(Form, self).__init__(parent, size, pos, style)
        self.active_widget = None

    def render(self):
        self.__render_style__()

    def show(self):
        super(Form, self).show()
        for widget in self.widgets:
            widget.show()

