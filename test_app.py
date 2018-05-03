from app import App
from form import Form
from button import Button
import pudb

class TestForm(Form):

    def __init__(self, size=(50, 60)):
        super(TestForm, self).__init__(None, size=size)

        btn = Button(self, "nihao", pos=(1, 5))
        self.add(btn)

if __name__ == "__main__":
    app = App()
    f = TestForm()
    f.show()


    app.main_loop()
