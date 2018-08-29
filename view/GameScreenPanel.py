from tkinter import *


class GameScreenPanel:

    def __init__(self, game, master):

        self.game = game

        self.canvas_size = 1000
        self.canvas = Canvas(master, width=self.canvas_size, height=self.canvas_size)
        self.canvas.pack()

        self.dead_cell_color = "black"
        self.alive_cell_color = "red"
        self.cell_size = 10
        self.cell_border = 1

        self.cells = self.init_cells(game.surface.width, game.surface.height)

    def init_cells(self, width, height):
        cells = {}
        for x in range(0, width):
            for y in range(0, height):
                cells[(x, y)] = self.create_cell(x, y, "black")
        return cells

    def create_cell(self, x, y, color):
        border = self.cell_border
        left = x * self.cell_size
        right = (x + 1) * self.cell_size
        top = y * self.cell_size
        bottom = (y + 1) * self.cell_size
        sq = self.canvas.create_rectangle(left + border, top + border,
                                          right - border, bottom - border, fill=color, tag='cell')
        return sq

    def update_surface(self):
        surface = self.game.surface
        for y in range(0, surface.height):
            for x in range(0, surface.height):
                cell_id = self.cells[(x, y)]
                if surface.get(x, y).is_alive:
                    self.canvas.itemconfig(cell_id, fill=self.alive_cell_color)
                else:
                    self.canvas.itemconfig(cell_id, fill=self.dead_cell_color)
