import pygame


def move1(body, speed):
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

    body.velocity = (vx, vy)


    return body.position
