from jscreen.app import App
from jscreen.text import Text
from jscreen.form import Form
from jscreen.button import Button
import pudb
import time

class TestForm(Form):

    def __init__(self, size=(50, 60)):
        super(TestForm, self).__init__(None, size=size)

        self.btn = Button(self, "nihao", pos=(1, 5))
        self.add(self.btn)
        btn = Text(self, text="text", pos=(20, 15), size =(10, 10))
        self.add(btn)

if __name__ == "__main__":
    app = App()
    f = TestForm()
    f.show()

    time.sleep(2)
    f.hide()
    time.sleep(2)
    f.show()
    f.btn.get_focus()


    app.main_loop()

if __name__ == "__main__":
    app = App()
    f = TestForm()
    f.show()

    time.sleep(2)
    f.hide()



    app.main_loop()
