import os

class TerminalView:
    def __init__(self, game, dead_cell_char=' 0 ', alive_cell_char=' # '):
        self.dead_cell_char = dead_cell_char
        self.alive_cell_char = alive_cell_char
        self.game = game

    def update_view(self):
        os.system("cls")
        self.show_info()
        self.show_surface()

    def show_info(self):
        print("Life Game %ix%i" % (self.game.surface.width, self.game.surface.height))
        print("Counter %i / %i" % (self.game.count, self.game.game_time_bound))

    def show_surface(self):
        surface = self.game.surface
        for y in range(0, surface.height):
            row = ""
            for x in range(0, surface.height):
                if surface.get(x, y).is_alive:
                    row = row + self.alive_cell_char
                else:
                    row = row + self.dead_cell_char
            print(row)

    def print_end_msg(self, msg):
        print(msg)
