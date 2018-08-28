from tkinter import *


class VisualView:
    def __init__(self, game, dead_cell_color="black", alive_cell_color="red"):
        self.dead_cell_color = dead_cell_color
        self.alive_cell_color = alive_cell_color
        self.game = game
        self.master = Tk()
        self.canvas_size = 1000
        self.canvas = Canvas(self.master, width=self.canvas_size, height=self.canvas_size)
        self.canvas.pack()
        self.cell_size = 10
        self.cells = self.init_cells(self.game.surface.width, self.game.surface.height)

    def init_cells(self, width, height):
        cells = {}
        for x in range(0, width):
            for y in range(0, height):
                cells[(x, y)] = self.create_cell(x, y, "black")
        return cells

    def update_view(self):
        self.show_surface()
        self.master.update()

    def show_info(self):
        print("Life Game %ix%i" % (self.game.surface.width, self.game.surface.height))
        print("Counter %i / %i" % (self.game.count, self.game.game_time_bound))

    def show_surface(self):
        surface = self.game.surface
        for y in range(0, surface.height):
            for x in range(0, surface.height):
                cell_id = self.cells[(x, y)]
                if surface.get(x, y).is_alive:
                    self.canvas.itemconfig(cell_id, fill=self.alive_cell_color)
                else:
                    self.canvas.itemconfig(cell_id, fill=self.dead_cell_color)

    def create_cell(self, x, y, color):
        border = 1
        left = x * self.cell_size
        right = (x + 1) * self.cell_size
        top = y * self.cell_size
        bottom = (y + 1) * self.cell_size
        sq = self.canvas.create_rectangle(left + border, top + border,
                                          right - border, bottom - border, fill=color, tag='cell')
        return sq

    def print_end_msg(self, msg):
        print(msg)
