from tkinter import *
from controllers import ParamButtons


class ButtonsPanel:

    def __init__(self, game, master):
        self.master = master
        self.param_buttons_controller = ParamButtons(game, self)
        self.width_text = self.init_entry("Ширина", game.surface.width)
        self.height_text = self.init_entry("Высота", game.surface.height)
        self.alone_size_text = self.init_entry("Минимальное число клеток вокруг", game.alone_size)
        self.over_size_text = self.init_entry("Максимальное число клеток вокруг", game.over_size)
        self.birth_size_text = self.init_entry("Число клеток вокруг для зарождения", game.birth_size)
        self.button_to_start = Button(master, text="Старт", command=self.param_buttons_controller.start_game)
        self.button_to_start.pack()
        self.button_to_start = Button(master, text="Пауза", command=self.param_buttons_controller.pause_game)
        self.button_to_start.pack()

    def init_entry(self, label_text, value):
        Label(self.master, text=label_text).pack()
        entry = Entry(self.master)
        entry.pack()
        var = StringVar()
        var.set(value)
        entry["textvariable"] = var
        return entry

    def pr(self, var):
        print(var)
