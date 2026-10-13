import pygame
import pymunk
import move
import physics

pygame.init()

W = 1200
H = 900

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Pygame + Pymunk")

clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 980)

b_body, b_shape = physics.create_ball(space, position=(300, 100), mass=1, radius=25)

r_body, r_shape = physics.create_box(
    space, position=(500, 600), mass=1, width=80, height=80
)

ground_shape = physics.create_ground(space, width=W, y=700, radius=10)

running = True
speed = 300

while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    move.move1(b_body, speed)

    space.step(dt)

    screen.fill((30, 30, 30))

    b_x, b_y = b_body.position

    pygame.draw.circle(screen, (80, 180, 255), (int(b_x), int(b_y)), 25)

    r_x, r_y = r_body.position

    pygame.draw.rect(screen, (100, 100, 100), (int(r_x - 40), int(r_y - 40), 80, 80))

    pygame.draw.line(screen, (200, 200, 200), (0, 700), (W, 700), 20)
    
    pygame.display.flip()

pygame.quit()
