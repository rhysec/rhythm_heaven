import raylib as rl
from pyray import *
import math

class Game:
    def __init__(self):
        screen_width = 1280
        screen_height = 720
        init_window(screen_width, screen_height, 'TITLE')
        init_audio_device()
        set_target_fps(60)

        self.import_assets()
        self.music = self.audio['music']
        self.sound = self.audio['sound']

    # configure rhythm
        play_music_stream(self.music)
        self.BPM = 106
        self.beat_duration = 60.0/self.BPM
        self.hit_window = 0.10

    # initialise rhythm variables
        self.current_beat = 0
        self.previous_beat = -1
        self.elapsed_time = 0

    def import_assets(self):
        self.assets = {}

        self.audio = { 'music' : load_music_stream('C:/Users/rhyse/PycharmProjects/rhythm_heaven/general/Hoop Trundling.mp3'),
                       'sound' : load_sound('C:/Users/rhyse/PycharmProjects/rhythm_heaven/general/sound.ogg')
                       }

    def update(self):
        pass

    def draw(self):
        begin_drawing()
        clear_background(RAYWHITE)

        end_drawing()

    def run(self):
        while not window_should_close():
            update_music_stream(self.music)

            self.previous_beat = self.current_beat
            self.elapsed_time = get_music_time_played(self.music) # number of seconds of music played
            self.current_beat = math.floor(self.elapsed_time / self.beat_duration * 2) / 2 # records last played beat

            if self.current_beat != self.previous_beat: # whenever a new beat is reached
                play_sound(self.sound)
                print(self.current_beat)

            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()