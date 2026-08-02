import raylib as rl
from pyray import *
import math

class Game:
    def __init__(self):
        screen_width = 1280
        screen_height = 720
        init_window(screen_width, screen_height, 'Hoop Trundling')


        init_audio_device()
        set_target_fps(60)

        self.import_assets()
        set_window_icon(self.assets['icon'])
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
        self.map_index = 0

    # level map
        self.level_map = [
            0, 0, 0, 0,   0, 0, 0, 0,      0, 0, 0, 0,   0, 0, 0, 0,
            0, 0, 0, 0,   0, 0, 0, 0,      0, 0, 0, 0,   0, 0, 0, 0,

            0, 0, 1, 2,   3, 4, 5, 0,      0, 0, 0, 0,   0, 0, 0, 0,
            0, 0, 1, 2,   3, 4, 5, 0,      0, 0, 0, 0,   0, 0, 0, 0,

            0, 0, 1, 2,   3, 4, 5, 0,      0, 0, 1, 2,   3, 4, 5, 0,
            0, 0, 0, 0,   0, 0, 0, 0,      1, 2, 3, 4,   5, 0, 0, 0,

            0, 0, 1, 2,   3, 4, 5, 0,      0, 0, 1, 2,   3, 4, 5, 0,
            0, 0, 0, 0,   0, 0, 0, 0,      1, 2, 3, 4,   5, 0, 0, 0,

            0, 0, 1, 2,   3, 4, 5, 0,      0, 0, 0, 0,   0, 0, 0, 0,
            1, 2, 3, 4,   5, 0, 0, 0,      1, 2, 3, 4,   5, 0, 0, 0,

            0, 0, 1, 2,   3, 4, 5, 0,      0, 0, 0, 0,   0, 0, 0, 0,
            1, 2, 3, 4,   5, 0, 0, 1,      2, 3, 4, 5,   1, 2, 3, 4,

            5, 0, 0, 1,   2, 3, 4, 5,      0, 0, 1, 2,   3, 4, 5, 0,
            0, 0, 0, 0,   1, 2, 3, 4,      5, 0, 0, 0,   1, 2, 3, 4,

            5, 0, 0, 1,   2, 3, 4, 5,      0, 0, 1, 2,   3, 4, 5, 0,
            0, 0, 0, 0,   0, 0, 0, 0,      0, 0, 0, 0,   0, 0, 0, 0,

            0, 0, 0, 0,   0, 0, 0, 0,      0, 0, 0, 0,   0, 0, 0, 0,
            0, 0, 0, 0,   0, 0, 0, 0,      0, 0, 0, 0,   0, 0, 0, 0,

            0, 0, 0, 0,   0, 0, 0, 0,      0, 0, 0, 0,   0, 0, 0, 0,
            0, 0, 0, 0,   0, 0, 0, 0,      0, 0, 0, 0,   0, 0, 0, 0,

            0, 0, 0, 0,   0, 0, 0, 0,      0, 0, 0, 0,   0, 0, 0, 0,
            0, 0, 0, 0,   0, 0, 0, 0,      0, 0, 0, 0,   0, 0, 0, 0,

            0, 0, 0, 0,   0, 0, 0, 0,      0, 0, 0, 0,   0, 0, 0, 0,
            0, 0, 0, 0,   0, 0, 0, 0,      0, 0, 0, 0,   0, 0, 0, 0,

            0, 0, 0, 0,   0, 0, 0, 0,      0, 0, 0, 0,   0, 0, 0, 0,
            0, 0, 0, 0,   0, 0, 0, 0,      0, 0, 0, 0,   0, 0, 0, 0,


        ]

    def import_assets(self):
        self.assets = { 'icon' : load_image('C:/Users/rhyse/PycharmProjects/rhythm_heaven/hoop_trundling/assets/icon.png'),
                        }

        self.audio = { 'music' : load_music_stream('C:/Users/rhyse/PycharmProjects/rhythm_heaven/hoop_trundling/audio/Hoop Trundling.mp3'),
                       'sound' : load_sound('C:/Users/rhyse/PycharmProjects/rhythm_heaven/hoop_trundling/audio/sound.ogg'),
                       'pa' : load_sound('C:/Users/rhyse/PycharmProjects/rhythm_heaven/hoop_trundling/audio/pa.ogg'),
                       'pe': load_sound('C:/Users/rhyse/PycharmProjects/rhythm_heaven/hoop_trundling/audio/pe.ogg'),
                       'pi': load_sound('C:/Users/rhyse/PycharmProjects/rhythm_heaven/hoop_trundling/audio/pi.ogg'),
                       'po': load_sound('C:/Users/rhyse/PycharmProjects/rhythm_heaven/hoop_trundling/audio/po.ogg'),
                       'pu': load_sound('C:/Users/rhyse/PycharmProjects/rhythm_heaven/hoop_trundling/audio/pu.ogg'),
                       'hop': load_sound('C:/Users/rhyse/PycharmProjects/rhythm_heaven/hoop_trundling/audio/hop.ogg'),
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

                if self.level_map[self.map_index] != 0:
                    play_sound(self.audio['hop'])

                if self.level_map[self.map_index] == 1:
                    play_sound(self.audio['pa'])
                if self.level_map[self.map_index] == 2:
                    play_sound(self.audio['pi'])
                if self.level_map[self.map_index] == 3:
                    play_sound(self.audio['pu'])
                if self.level_map[self.map_index] == 4:
                    play_sound(self.audio['pe'])
                if self.level_map[self.map_index] == 5:
                    play_sound(self.audio['po'])
                if self.level_map[self.map_index] == 6:
                    play_sound(self.audio['hop'])

                self.map_index += 1


            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()