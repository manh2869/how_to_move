import pygame
import pymunk
import move
import Pymunk
import time
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
r_main_body, r_main_shape = Pymunk.create_box(
    space, position=(100, 600), mass=10, width=rec_radius * 2, height=rec_radius * 2
)

r_body, r_shape = Pymunk.create_box(
    space, position=(900, 400), mass=1, width=rec_radius * 2, height=rec_radius * 2
)

barrel_shape = Pymunk.create_barrel(space, r_main_body, rec_radius)
DRAW.ground(space, W, H)

running = True
speed = 300


bullet = []
while running:
    dt = clock.tick(120) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tip = r_main_body.local_to_world((rec_radius + 40 + 6, 0))
                bullet_body, bullet_shape = Pymunk.create_ball(
                    space, position=tip, mass=1, radius=5
                )
                bullet_body.velocity = pymunk.Vec2d(1200, 0).rotated(r_main_body.angle)
                bullet.append((bullet_body, bullet_shape, time.time()))

    move.move1(r_main_body, 100)
    space.step(1 / 120)
    screen.fill((30, 30, 30))

    for b in bullet:
        pygame.draw.circle(screen, (255, 0, 0), (b[0].position), 5)
        if time.time() - b[2] >= 5:
            space.remove(b[0], b[1])
            bullet.remove(b)

    DRAW.draw_object(screen, r_body, r_shape, r_main_body, r_main_shape, barrel_shape)
    DRAW.draw_bound(screen, W, H)
    pygame.display.flip()

pygame.quit()
