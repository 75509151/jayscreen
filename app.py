import curses
import time
from glo import scr


class App(object):
    def __init__(self):
        scr.refresh()
        curses.noecho()
        curses.cbreak()

    def main_loop(self):
        while True:
            time.sleep(1)


if __name__ == "__main__":
    app = App()
    app.main_loop()
