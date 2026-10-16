import pygame
import math


def move1(body, speed, dt, turn_speed=1):
    keys = pygame.key.get_pressed()

    vx = 0
    
    if keys[pygame.K_w]:
        vx = speed
    if keys[pygame.K_s]:
        vx = -speed

    turn = 0
    if keys[pygame.K_d]:
        turn = 1
    if keys[pygame.K_a]:
        turn = -1
    vx1 = math.cos(body.angle) * speed * vx * dt
    vy1 = math.sin(body.angle) * speed * vx * dt
    body.velocity = (vx1, vy1)
    body.angular_velocity = turn * turn_speed
    return body.position
