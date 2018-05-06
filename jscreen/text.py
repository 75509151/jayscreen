from widget import Widget
import styles


class StaticText(Widget):
    _selectable = False

    def __init__(self, parent, text="", size=None, pos=None,
                 style=styles.NO_STYLE):
        if size is None:
            h = len(text.split("\n")) + 2
            w = len(max(text.split("\n"), key=len)) + 2
            size = (w, h)
        super(StaticText, self).__init__(parent, size, pos)
        self.text = text

    def render(self):
        self.__render_style__()
        self._win.insstr(1, 1, self.text)



class Text(StaticText):
    _selectable = True

    def __init__(self, parent, text="", size=None, pos=None,
                 style=styles.NO_STYLE):
        super(Text, self).__init__(parent, text, size, pos)
