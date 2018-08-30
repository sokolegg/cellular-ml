from models import Game


class App:

    def __init__(self):
        self.game = Game(app=self)
        self.need_to_update = False
        self.run()

    def run(self):
        while True:
            if not self.game.is_pause:
                self.game.start()
            self.game.view.update_view()
            self.check_for_new_game_and_update()

    def check_for_new_game_and_update(self):
        game = self.game
        old_game = {
            "width": game.surface.width,
            "height": game.surface.height,
            "alone_size": game.alone_size,
            "over_size": game.over_size,
            "birth_size": game.birth_size}

        try:
            new_game = self.check_buttons()
            if self.need_to_update:
                self.game.rebuild(**new_game)
        except Exception:
            self.game.rebuild(**old_game)
        self.need_to_update = False

    def check_buttons(self):
        panel = self.game.view.buttons_panel
        game = self.game
        new_values = {"width": self.add_new(game.surface.width, panel.width_text.get()),
                      "height": self.add_new(game.surface.height, panel.height_text.get()),
                      "alone_size": self.add_new(game.alone_size, panel.alone_size_text.get()),
                      "over_size": self.add_new(game.over_size, panel.over_size_text.get()),
                      "birth_size": self.add_new(game.birth_size, panel.birth_size_text.get())}
        return new_values

    def add_new(self, old_value, new_value):
        new_value = int(new_value)
        print(old_value, new_value)
        if not old_value == new_value:
            self.need_to_update = True
            self.game.pause()
        return new_value


if __name__ == "__main__":
    App()
