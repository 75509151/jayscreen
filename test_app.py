from app import App
from widget import Widget

if __name__ == "__main__":
    app = App()
    a = Widget(None, size=(10, 20))
    app.main_loop()
