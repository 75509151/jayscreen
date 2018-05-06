import curses


class KeyListern(object):
    def __init__(self):
        self.key_handlers = None
        self.action_handlers = {}
        self.setup_key_handlers()

    def setup_key_handlers(self):
        self.key_handlers = {
            curses.KEY_UP: self.h_key_up,
            curses.KEY_DOWN: self.h_key_down
        }

    def key_listen(self, key):
        child_widgets = getattr(self, "widgets", [])
        for child in child_widgets:
            if child.key_listen(key):
                return True

        if key in self.key_handlers:
            if self.key_handlers[key](key):
                return True
        if key in self.action_handlers:
            return self.action_handlers[key](key)
        print "key:", key

        return False


    def h_key_up(self, key):
        print "keyup"

    def h_key_down(self, key):
        print "key_down"
