import pygame
import pymunk
import move
import physics
import time
import DRAW


def draw_box(screen, body, shape, color):
    points = [body.local_to_world(v) for v in shape.get_vertices()]
    points = [(int(p.x), int(p.y)) for p in points]
    pygame.draw.polygon(screen, color, points)


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
r_main_body, r_main_shape = physics.create_box(
    space, position=(100, 600), mass=10, width=rec_radius * 2, height=rec_radius * 2
)

r_body, r_shape = physics.create_box(
    space, position=(900, 400), mass=1, width=rec_radius * 2, height=rec_radius * 2
)

barrel_len = 40
barrel_w = 10

barrel_shape = pymunk.Poly(
    r_main_body,
    [
        (rec_radius, -barrel_w / 2),
        (rec_radius + barrel_len, -barrel_w / 2),
        (rec_radius + barrel_len, barrel_w / 2),
        (rec_radius, barrel_w / 2),
    ],
)

space.add(barrel_shape)
DRAW.ground(space, H, W)

running = True
speed = 300
attack = False

bullet = []

while running:
    dt = clock.tick(120) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tip = r_main_body.local_to_world((rec_radius + barrel_len + 6, 0))
                bullet_body, bullet_shape = physics.create_ball(
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

    r_x, r_y = r_body.position
    r_main_x, r_main_y = r_main_body.position

    draw_box(screen, r_body, r_shape, (100, 100, 100))
    draw_box(screen, r_main_body, r_main_shape, (100, 200, 100))
    draw_box(screen, r_main_body, barrel_shape, (200, 200, 200))
    pygame.draw.line(screen, (200, 200, 200), (0, H), (W, H), 20)
    pygame.draw.line(screen, (200, 200, 200), (0, 0), (0, H), 20)
    pygame.draw.line(screen, (200, 200, 200), (W, 0), (W, H), 20)
    pygame.draw.line(screen, (200, 200, 200), (0, 0), (W, 0), 20)
    pygame.display.flip()
pygame.quit()
