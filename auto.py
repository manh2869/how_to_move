import pygame
import math
import tank
import random
from collections import defaultdict

# player_body.position  Vec2d(161.75453397682008, 551.3755459330841)
# player_body.angle   -12.694999999999558

ACTIONS = [0, 1, 2, 3]
MOVE = [[1, 0], [-1, 0], [0, 1], [0, -1]]
rng = random.Random()


def grid():
    return [[0 for _ in range(tank.W // 50)] for _ in range(tank.H // 50)]


def step(i, j, action, player_pos):
    if [i, j] == player_pos:
        return i, j, 0.0, True
    dr, dc = MOVE[action]
    r, c = i, j
    nr = min(max(r + dr, 0), tank.W // 50)
    nc = min(max(c + dc, 0), tank.H // 50)
    return nr, nc, -1.0, (nr, nc) == player_pos


def rollout(Q, i, j, player_pos, max_steps=5000):
    trajectory = []
    for _ in range(max_steps):
        if rng.random() < 0.2 or (i, j) not in Q:
            action = rng.choice(ACTIONS)
        else:
            action = max(Q[(i, j)], key=Q[(i, j)].get)
        # action = random.randint(0, 3)
        x, y, reward, done = step(i, j, action, player_pos)
        trajectory.append([i, j, action, reward])
        i, j = x, y
        if done:
            break
    return trajectory


def episode_cost(trajectory, gamma=0.99):
    cost = []
    G = 0.0
    for i, j, a, r in reversed(trajectory):
        G = r + gamma * G
        cost.append([i, j, a, G])
    cost.reverse()
    return cost


def improve_policy(enemy_body, player_pos):
    Q = defaultdict(lambda: {a: 0.0 for a in ACTIONS})
    counts = defaultdict(lambda: {a: 0 for a in ACTIONS})
    for _ in range(10000):
        for i, j, a, G in episode_cost(
            # rollout(Q, enemy_body.position.x, enemy_body.position.y, player_pos)
            rollout(Q, 200, 200, [700, 700])
        ):
            counts[(i, j)][a] += 1
            Q[(i, j)][a] += (G - Q[(i, j)][a]) / counts[(i, j)][a]
    return Q.items()


print(improve_policy(None, None))

# def enemy_move(enemy_body, player_body, speed, turn_speed):
#     TERMINAL = [player_body.positon.x, player_body.positon.y]
#     episode_cost(rollout())

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
