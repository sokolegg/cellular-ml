import unittest
from models import Surface
from models import GameException
from models import Game


class Tests(unittest.TestCase):

    def setUp(self):
        self.surf = Surface()

    def test_alive(self):
        surface33 = Surface(width=3, height=3)
        surface33.get(0, 0).is_alive = True
        must_be = {(0, 0): 0, (1, 0): 1, (0, 1): 1, (1, 1): 1, (2, 2): 1, (0, 2): 1, (2, 0): 1, (1, 2): 1,
                   (2, 1): 1, (-1, -1): 1, (3, 3): 0, (3, 0): 0, (4, 2): 1, (6, 6): 0}
        for key in must_be.keys():
            self.assertEquals(surface33.alive_cells_around(key[0], key[1]), must_be[key], msg=key)

    def test_game_creation_with_wrong_size(self):
        # [(width, height, alone_size, over_size, birth_size)]
        wrong_cases_for_every = {"width": [-1, 0, 1, 2],
                                 "height": [-1, 0, 1, 2],
                                 "alone_size": [-1, 9, 10],
                                 "over_size": [-1, 9, 10],
                                 "birth_size": [-1, 9, 10]}
        some_of_good_cases = {"width": 3,
                              "height": 3,
                              "alone_size": 0,
                              "over_size": 8,
                              "birth_size": 2}
        without_good = True
        for key in wrong_cases_for_every.keys():
            for var in wrong_cases_for_every[key]:
                pars = some_of_good_cases.copy()
                pars[key] = var
                try:
                    Game(**pars)
                except GameException:
                    continue
                without_good = False
        self.assertTrue(without_good)


def run_test(unittest_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(unittest_class)
    unittest.TextTestRunner(verbosity=2).run(suite)


run_test(Tests)
