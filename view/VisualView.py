from tkinter import *


class VisualView:
    def __init__(self, game, dead_cell_color="black", alive_cell_color="red"):

        self.game = game
        self.master = Tk()


        self.start_button = Button(self.master)



    def update_view(self):
        self.show_surface()
        self.master.update()

    def show_info(self):
        print("Life Game %ix%i" % (self.game.surface.width, self.game.surface.height))
        print("Counter %i / %i" % (self.game.count, self.game.game_time_bound))







    def print_end_msg(self, msg):
        print(msg)
