import time
import pudb
from jscreen.app import App
from jscreen.text import Text
from jscreen.form import Form
from jscreen.button import Button

class TestForm(Form):

    def __init__(self, size=(50, 60)):
        super(TestForm, self).__init__(None, size=size)

        self.btn = Button(self, "nihao", pos=(1, 5))
        self.add(self.btn)
        btn = Text(self, text="text", pos=(20, 15), size =(10, 10))
        self.add(btn)


if __name__ == "__main__":
    # pudb.set_trace()
    app = App()
    f = TestForm()
    f.show()

    f.display()
    while True:
        ch = f._win.getch()
        f.key_listen(ch)

    # ch = curses.get
    app.main_loop()


