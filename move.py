import pygame
import math


def move1(body, speed, dt, turn_speed):
    keys = pygame.key.get_pressed()

    vx = 0

    if keys[pygame.K_w]:
        vx = 1
    if keys[pygame.K_s]:
        vx = -1

    turn = 0
    if keys[pygame.K_d]:
        turn = 1
    if keys[pygame.K_a]:
        turn = -1
    vx1 = math.cos(body.angle) * speed * vx
    vy1 = math.sin(body.angle) * speed * vx
    body.velocity = (vx1, vy1)
    body.angular_velocity = turn * turn_speed
    return body.position
