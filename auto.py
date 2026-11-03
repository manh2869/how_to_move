import math
import tank
import random

ACTIONS = [0, 1, 2, 3]
A = ["R", "L", "U", "D"]
MOVE = [[1, 0], [-1, 0], [0, 1], [0, -1]]
rng = random.Random(1)

c = [0, 0, 0, 0]
n = [-math.inf, -math.inf, -math.inf, -math.inf]


def grid(inf):
    m = []
    for i in range(tank.H // 50):
        row = []
        for j in range(tank.W // 50):
            row.append(inf.copy())
        m.append(row)
    return m


def step(i, j, action, player_pos):
    if [i, j] == player_pos:
        return i, j, 0.0, True
    dr, dc = MOVE[action]

    nr = min(max(i + dr, 0), tank.W // 50 - 1)
    nc = min(max(j + dc, 0), tank.H // 50 - 1)
    return nr, nc, -1.0, [nr, nc] == player_pos


def rollout(m, i, j, player_pos, max_steps=1000):
    trajectory = []
    for _ in range(max_steps):
        if rng.random() < 0.2:
            action = rng.choice(ACTIONS)
        else:
            action = m[i][j].index(max(m[i][j]))
        if max(m[i][j]) == 0:
            action = rng.choice(ACTIONS)
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
    m = grid(c)
    count = grid(c)
    for _ in range(1000):
        for i, j, a, G in episode_cost(
            rollout(
                m,
                int(player_pos.position.x // 50 - 1),
                int(player_pos.position.y // 50 - 1),
                [
                    int(enemy_body.position.x // 50 - 1),
                    int(enemy_body.position.y // 50 - 1),
                ],
            )
        ):
            count[i][j][a] += 1
            m[i][j][a] += (G - m[i][j][a]) / count[i][j][a]
    return m


def pick_max(enemy_body, player_pos):
    a = improve_policy(enemy_body, player_pos)
    for i in a:
        for j in i:
            x = MOVE[j.index(max(j))][1] * 200
            y = MOVE[j.index(max(j))][0] * 200
            print(j.index(max(j)))
    enemy_body.velocity = (x, y)
