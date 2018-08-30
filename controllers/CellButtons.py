class CellButtons:
    def __init__(self, game, cell_size):
        self.cell_size = cell_size
        self.game = game

    def click(self, event):
        x = int(event.x / self.cell_size)
        y = int(event.y / self.cell_size)
        self.game.change(x, y)
