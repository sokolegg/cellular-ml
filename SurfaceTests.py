import unittest
from models import Surface
from models import Game


class SurfaceTests(unittest.TestCase):

    def setUp(self):
        self.surf = Surface()

    def test_alive(self):
        surface33 = Surface(width=3, height=3)
        surface33.get(0, 0).is_alive = True
        must_be = {(0, 0): 0, (1, 0): 1, (0, 1): 1, (1, 1): 1, (2, 2): 1, (0, 2): 1, (2, 0): 1, (1, 2): 1,
                   (2, 1): 1, (-1, -1): 1, (3, 3): 0, (3, 0): 0, (4, 2): 1, (6, 6): 0}
        for key in must_be.keys():
            self.assertEquals(surface33.alive_cells_around(key[0], key[1]), must_be[key], msg=key)

    def test_basic_game(self):
        import random
        size = 100
        game = Game(width=size, height=size, tick_time=0)
        places = [(random.randint(0, size), random.randint(0, size)) for i in range(0, int(size*size/2))]
        game.change_cells(places)
        game.start()


def run_test(unittest_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(unittest_class)
    unittest.TextTestRunner(verbosity=2).run(suite)


run_test(SurfaceTests)
