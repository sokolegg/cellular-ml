from .Cell import Cell


def fill(width, height):
    data = {}
    for x in range(0, width):
        for y in range(0, height):
            data[(x, y)] = Cell()
    return data


def normalize_index(index, bound):
    if 0 <= index < bound:
        return index
    if index >= bound:
        return normalize_index(index - bound, bound)
    if index < 0:
        return normalize_index(index + bound, bound)


class Surface:
    def __init__(self, width=20, height=20):
        self.min_size = 3
        self.max_size = 1000
        self.width = 3
        self.height = 3

        if self.min_size < width < self.max_size:
            self.width = width
        if self.min_size < height < self.max_size:
            self.height = height

        self.cells = fill(self.width, self.height)

    def get(self, x, y):
        x = normalize_index(x, self.width)
        y = normalize_index(y, self.height)

        return self.cells[(x, y)]

    def alive_cells_around(self, x, y):
        alive = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                if self.get(i, j).is_alive:
                    alive = alive + 1
        return alive
