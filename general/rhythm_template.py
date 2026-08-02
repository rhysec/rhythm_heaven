import raylib as rl
from pyray import *

class Game:
    def __init__(self):
        WIDTH = 1280
        HEIGHT = 720
        init_window(WIDTH, HEIGHT, 'TITLE')
        init_audio_device()
        set_target_fps(60)









        # play_music_stream(MUSIC)

    def import_assets(self):
        self.assets = {}

        self.audio = {}

    def update(self):
        pass

    def draw(self):
        begin_drawing()
        clear_background(RAYWHITE)

        end_drawing()

    def run(self):
        while not window_should_close():
            # update_music_stream(MUSIC)

            self.update()
            self.draw()


if __name__ == '__main__':
    print('r')
    game = Game()
    game.run()