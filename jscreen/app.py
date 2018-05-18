import curses
import time
import glo


class App(object):
    SCR = curses.initscr()

    def __init__(self):
        self.exit = False
        self.forms = []

        self.SCR.refresh()
        curses.start_color()
        # curses.init_pair(1, curses.COLOR_BLACK)
        # curses.init_color(2, curses.COLOR_WHITE)
        # curses.init_color(3, curses.COLOR_BLUE)
        # curses.init_color(4, curses.COLOR_YELLOW)

        curses.noecho()
        curses.cbreak()

    def add_form(self, form):
        self.forms.append(form)

    def main_loop(self):
        while not self.exit:
            for form in self.forms:
                if not form.hided():
                    form.render()


glo.glo_app = App()

if __name__ == "__main__":
    app = App()
    app.main_loop()
