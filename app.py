import curses
import time
from glo import scr


class App(object):
    def __init__(self):
        scr.refresh()
        curses.start_color()
        # curses.init_pair(1, curses.COLOR_BLACK)
        # curses.init_color(2, curses.COLOR_WHITE)
        # curses.init_color(3, curses.COLOR_BLUE)
        # curses.init_color(4, curses.COLOR_YELLOW)


        curses.noecho()
        curses.cbreak()

    def main_loop(self):
        while True:
            time.sleep(1)


if __name__ == "__main__":
    app = App()
    app.main_loop()
