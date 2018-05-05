import curses


class KeyListern(object):
    def __init__(self):
        self.handlers = None
        self.setup_handlers()

    def setup_handlers(self):
        self.handlers = {
            curses.KEY_UP: self.h_key_up,
            curses.KEY_DOWN: self.h_key_down
        }

    def key_listen(self, key):
        if key in self.handlers:
            return self.handlers[key](key)

        if hasattr(self, "parent"):
            self.parent.key_listen(key)

    def h_key_up(self, key):
        print "keyup"

    def h_key_down(self, key):
        pass
