import pymunk
import pygame
import physics


def ground(space,H,W):

    ground_shape = physics.create_wall(space, 0, H, W, H, 10)
    ground_shape = physics.create_wall(space, 0, 0, 0, H, 10)
    ground_shape = physics.create_wall(space, W, 0, W, H, 10)
    ground_shape = physics.create_wall(space, 0, 0, W, 0, 10)
