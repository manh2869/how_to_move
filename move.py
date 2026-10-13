import pygame


def move1(body, speed, turn_speed=1):
    keys = pygame.key.get_pressed()

    vx = 0
    vy = 0

    if keys[pygame.K_w]:
        vy = -speed
    if keys[pygame.K_s]:
        vy = speed
    if keys[pygame.K_a]:
        vx = -speed
    if keys[pygame.K_d]:
        vx = speed

    turn = 0
    if keys[pygame.K_UP]:
        turn = -1
    if keys[pygame.K_DOWN]:
        turn = 1

    body.velocity = (vx, vy)
    body.angular_velocity = turn * turn_speed
    return body.position
