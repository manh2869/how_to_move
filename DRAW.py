import pygame
import Pymunk


def ground(space, W, H):

    ground_shape = Pymunk.create_wall(space, 0, H, W, H, 10)
    ground_shape = Pymunk.create_wall(space, 0, 0, 0, H, 10)
    ground_shape = Pymunk.create_wall(space, W, 0, W, H, 10)
    ground_shape = Pymunk.create_wall(space, 0, 0, W, 0, 10)


def draw_bound(screen, W, H):
    pygame.draw.line(screen, (200, 200, 200), (0, H), (W, H), 20)
    pygame.draw.line(screen, (200, 200, 200), (0, 0), (0, H), 20)
    pygame.draw.line(screen, (200, 200, 200), (W, 0), (W, H), 20)
    pygame.draw.line(screen, (200, 200, 200), (0, 0), (W, 0), 20)


def draw_box(screen, body, shape, color):
    points = [body.local_to_world(v) for v in shape.get_vertices()]
    points = [(int(p.x), int(p.y)) for p in points]
    pygame.draw.polygon(screen, color, points)


def draw_object(screen, r_body, r_shape, r_main_body, r_main_shape, barrel_shape):
    draw_box(screen, r_body, r_shape, (100, 100, 100))
    draw_box(screen, r_main_body, r_main_shape, (100, 200, 100))
    draw_box(screen, r_main_body, barrel_shape, (200, 200, 200))
