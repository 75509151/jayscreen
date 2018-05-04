from app import App
from text import Text
from form import Form
from button import Button
import pudb
import time

class TestForm(Form):

    def __init__(self, size=(50, 60)):
        super(TestForm, self).__init__(None, size=size)

        btn = Button(self, "nihao", pos=(1, 5))
        self.add(btn)
        btn = Text(self, "text", pos=(20, 15))
        self.add(btn)

if __name__ == "__main__":
    app = App()
    f = TestForm()
    f.show()

    time.sleep(2)
    f.hide()
    time.sleep(2)
    f.show()



    app.main_loop()

if __name__ == "__main__":
    app = App()
    f = TestForm()
    f.show()

    time.sleep(2)
    f.hide()



    app.main_loop()
