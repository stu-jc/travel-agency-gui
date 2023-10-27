import tkinter as tk

from model import Model
from view import *
from controller import *


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        model = Model()
        view = View(self)
        controller = Controller(model, view)
        view.set_controller(controller)


if __name__ == '__main__':
    app = Application()
    app.mainloop()
