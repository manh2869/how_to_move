import pygame
import math
import tank

# player_body.position  Vec2d(161.75453397682008, 551.3755459330841)
# player_body.angle   -12.694999999999558

ACTIONS = ["up", "down", "left", "right"]


def grid():
    return [[0 for _ in range(tank.W / 50)] for _ in range(tank.H / 50)]


print(grid)


# def step(i, j, action):
#     if (i, j) == TERMINAL:
#         return i, j, 0.0, True
#     dr, dc = DELTAS[action]
#     r, c = i, j
#     nr = min(max(r + dr, 0), GRID - 1)
#     nc = min(max(c + dc, 0), GRID - 1)
#     return nr, nc, -1.0, (nr, nc) == TERMINAL


# def enemy_move(body, player_body, speed, turn_speed):
#     TERMINAL = [player_body.positon.x, player_body.positon.y]

    # keys = pygame.key.get_pressed()

    # vx = 0

    # if keys[pygame.K_w]:
    #     vx = 1
    # if keys[pygame.K_s]:
    #     vx = -1

    # turn = 0
    # if keys[pygame.K_d]:
    #     turn = 1
    # if keys[pygame.K_a]:
    #     turn = -1
    # vx1 = math.cos(body.angle) * speed * vx
    # vy1 = math.sin(body.angle) * speed * vx
    # body.velocity = (vx1, vy1)
    # body.angular_velocity = turn * turn_speed
