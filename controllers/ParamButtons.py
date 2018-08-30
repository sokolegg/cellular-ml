
class ParamButtons:
    def __init__(self, game, buttons_panel):
        self.buttons_panel = buttons_panel
        self.game = game

    def start_game(self):
        self.game.start()

    def pause_game(self):
        self.game.pause()

