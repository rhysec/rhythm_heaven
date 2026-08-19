import raylib as rl
from pyray import *
import math

class Sprite:
    def __init__(self, texture, pos, scale):
        self.texture = texture
        self.pos = pos
        self.scale = scale

    def draw(self):
        draw_texture_ex(self.texture, self.pos, 0, self.scale, WHITE)


class Hoop(Sprite):
    def __init__(self, texture, pos, scale, rotation):
        super().__init__(texture, pos, scale)
        self.rotation = rotation
        self.alpha = 255
        self.hoop_texture = load_texture_from_image(self.texture)
        self.poly_mesh = gen_mesh_plane(2.5, 2.5, 1, 1)
        self.poly_model = load_model_from_mesh(self.poly_mesh)
        self.poly_model.materials[0].maps[rl.MATERIAL_MAP_ALBEDO].texture = self.hoop_texture

    def draw(self):
        self.poly_model.transform = matrix_rotate_xyz(Vector3(self.rotation, 0, 3 * math.pi / 2))
        draw_model(self.poly_model, self.pos, self.scale, Color(255,255,255,self.alpha))

    def update(self):
        self.pos.x -= 0.15
        self.rotation -= 0.01

        if self.pos.x < -15 and self.alpha > 10:
            self.alpha -= 10

class Trundlorb(Sprite):
    def __init__(self, texture, pos, scale):
        super().__init__(texture, pos, scale)
    def update(self):
        pass