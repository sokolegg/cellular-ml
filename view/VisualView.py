from tkinter import *
from .ButtonsPanel import ButtonsPanel
from .GameScreenPanel import GameScreenPanel

master = Tk()


class VisualView:

    def __init__(self, game):
        self.master = master
        self.game = game
        self.buttons_panel = ButtonsPanel(game=game, master=self.master)
        self.game_screen_panel = GameScreenPanel(game=game, master=self.master)
        self.master.update()

    def update_view(self):
        self.game_screen_panel.update_surface()
        self.master.update()
