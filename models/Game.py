from .Surface import Surface
from view import VisualView
import time


class Game:

    def __init__(self, width=20, height=20, tick_time=0.1, game_time_bound=1000,
                 alone_size=2, over_size=3, birth_size=3):
        self.surface = Surface(width, height)
        self.tick_time = tick_time
        self.game_time_bound = game_time_bound
        self.change_log = []
        self.is_end = False
        self.is_pause = True
        self.alone_size = alone_size
        self.over_size = over_size
        self.birth_size = birth_size
        self.count = 0
        self.view = VisualView(game=self)

    def change_cells(self, places):
        self.change_log.append(places)
        for place in places:
            cell = self.surface.get(x=place[0], y=place[1])
            cell.is_alive = not cell.is_alive
        self.view.update_view()

    def change(self, x, y):
        self.change_cells([(x, y)])

    def stop(self, msg):
        self.is_end = True
        self.view.print_end_msg(msg)

    def start(self):
        while not self.is_end:
            self.count = self.count + 1
            self.do_one_time()
            self.check_times()
            self.check_periodic()
            self.check_all_dead()

    def do_one_time(self):
        time.sleep(self.tick_time)

        cells_to_change = []
        for x in range(0, self.surface.width):
            for y in range(0, self.surface.height):
                if self.should_change(x, y):
                    cells_to_change.append((x, y))
        self.change_cells(cells_to_change)

    def should_change(self, x, y):
        around = self.surface.alive_cells_around(x, y)
        if self.surface.get(x, y).is_alive:
            return not (self.alone_size <= around <= self.over_size)
        else:
            return around == self.birth_size

    def check_times(self):
        if self.count > self.game_time_bound:
            self.stop("Time end!")

    def check_periodic(self):
        pass

    def check_all_dead(self):
        all_dead = True
        for x in range(0, self.surface.width):
            for y in range(0, self.surface.height):
                if self.surface.get(x, y).is_alive:
                    all_dead = False
                    break
        if all_dead:
            self.stop("All cells are dead")
