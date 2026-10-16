import physic
import DRAW
import random
import math
import pymunk


def create_enemy(space):
    rec_radius = 25

    r_main_body, r_main_shape = physic.create_box(
        space, position=(900, 400), mass=5, width=rec_radius * 2, height=rec_radius * 2
    )
    barrel_shape = physic.create_barrel(space, r_main_body, rec_radius)
    return r_main_body, r_main_shape, barrel_shape


def draw_enemy(screen, body, shape, barrel_shape, color):
    DRAW.draw_box(screen, body, shape, color)
    DRAW.draw_box(screen, body, barrel_shape, (200, 200, 200))


