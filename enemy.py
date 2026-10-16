import physic
import DRAW
import random
import math
import pymunk

ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)


def create_enemy(space):
    rec_radius = 25

    r_main_body, r_main_shape = physic.create_box(
        space, position=(900, 400), mass=5, width=rec_radius * 2, height=rec_radius * 2
    )
    barrel_shape = physic.create_barrel(space, r_main_body, rec_radius)
    r_main_shape.collision_type = 1
    return r_main_body, r_main_shape, barrel_shape


def draw_enemy(screen, body, shape, barrel_shape, color):
    DRAW.draw_box(screen, body, shape, color)
    DRAW.draw_box(screen, body, barrel_shape, (200, 200, 200))
