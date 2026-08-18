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
        image_format(self.assets['icon'],rl.PIXELFORMAT_UNCOMPRESSED_R8G8B8A8)
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
            0, 0, 0, 0,   1, 2, 3, 4,      5, 0, 0, 0,   1, 2, 3, 4,

            5, 0, 0, 1,   2, 3, 4, 5,      0, 0, 0, 0,   1, 2, 3, 4,
            5, 0, 0, 0,   1, 2, 3, 4,      5, 0, 0, 0,   1, 2, 3, 4,

            5, 0, 0, 0,   0, 0, 0, 0,      0, 0, 1, 2,   3, 4, 5, 0,
            0, 0, 0, 0,   0, 0, 0, 0,      0, 0, 1, 2,   3, 4, 5, 0,

            0, 0, 1, 2,   3, 4, 5, 0,      0, 0, 0, 0,   1, 2, 3, 4,
            5, 0, 0, 0,   0, 0, 0, 0,      0, 0, 1, 2,   3, 4, 5, 0,

            0, 0, 1, 2,   3, 4, 5, 0,      0, 0, 0, 0,   1, 2, 3, 4,
            5, 0, 0, 0,   0, 0, 0, 0,      0, 0, 0, 0,   0, 0, 0, 0

        ]

    # 3D camera
        self.camera = Camera3D()
        self.camera.position = Vector3(2,1,6)
        self.camera.target = Vector3(-4,2,0)
        self.camera.up = Vector3(0,1,0)
        self.camera.fovy = 45.0
        self.camera.projection = rl.CAMERA_PERSPECTIVE

    # test objects
        self.mesh_sphere = gen_mesh_sphere(1,100,100)
        self.model_sphere = load_model_from_mesh(self.mesh_sphere)
        gradient_image_sphere = gen_image_gradient_linear(256,256,90,RED,WHITE)
        texture_sphere = load_texture_from_image(gradient_image_sphere)
        self.model_sphere.materials[0].maps[rl.MATERIAL_MAP_ALBEDO].texture = texture_sphere

        self.object_offset = 0

        self.mesh_cylinder = gen_mesh_cylinder(2, 0.001, 100)
        self.model_cylinder = load_model_from_mesh(self.mesh_cylinder)
        gradient_image_cylinder = gen_image_gradient_linear(256, 256, 90, RED, WHITE)
        texture_cylinder = load_texture_from_image(gradient_image_cylinder)
        self.model_cylinder.materials[0].maps[rl.MATERIAL_MAP_ALBEDO].texture = texture_cylinder


        self.model_cylinder.transform = matrix_rotate_z(1.5708)



    def draw(self):
        begin_drawing()
        clear_background(RAYWHITE)
        begin_mode_3d(self.camera)
        draw_grid(100,1)

        draw_model(self.model_sphere, Vector3(math.sin(self.object_offset), 0, math.sin(self.object_offset / 2)), 1, WHITE)
        draw_model(self.model_cylinder, Vector3(self.object_offset, 2.2, 0), 1, WHITE)

        end_mode_3d()
        end_drawing()




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

    def run(self):
        while not window_should_close():
            #update_music_stream(self.music)

            self.previous_beat = self.current_beat
            self.elapsed_time = get_music_time_played(self.music) + 0.03 # number of seconds of music played (+ beat offset)
            self.current_beat = math.floor(self.elapsed_time / self.beat_duration * 2) / 2 # last half beat played

            if self.current_beat != self.previous_beat: # whenever a new half beat is reached
                #play_sound(self.sound)

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


            # Test
            self.object_offset -= 0.1



            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()