import pygame
import pymunk
import move
import physic
import DRAW

pygame.init()

W = 1200
H = 900

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("tank")

clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 0)
space.damping = 0.6

rec_radius = 25

r_main_body, r_main_shape = physic.create_box(
    space, position=(100, 600), mass=10, width=rec_radius * 2, height=rec_radius * 2
)

r_body, r_shape = physic.create_box(
    space, position=(900, 400), mass=1, width=rec_radius * 2, height=rec_radius * 2
)

barrel_shape = physic.create_barrel(space, r_main_body, rec_radius)

physic.create_ground(space, W, H)
running = True
speed = 150


bullet = []
while running:
    dt = clock.tick(120) / 1000.0
    screen.fill((30, 30, 30))
    running = physic.shoot(space, screen, r_main_body, bullet, rec_radius, running)
    move.move1(r_main_body, speed, dt)
    space.step(dt)
    DRAW.draw_object(screen, r_body, r_shape, r_main_body, r_main_shape, barrel_shape)
    DRAW.draw_bound(screen, W, H)
    DRAW.draw_grid(screen, W, H, 50)
    pygame.display.flip()

pygame.quit()
