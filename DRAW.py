import pygame
import physic


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


def draw_grid(screen,W,H, cell_size):
    color = (60, 60, 60)
    for x in range(0, W, cell_size):
        pygame.draw.line(screen, color, (x, 0), (x, H))
    for y in range(0, H, cell_size):
        pygame.draw.line(screen, color, (0, y), (W, y))
