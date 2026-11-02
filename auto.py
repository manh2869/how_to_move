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


def rollout(m, i, j, player_pos, max_steps=10000):
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
    for _ in range(10000):
        for i, j, a, G in episode_cost(rollout(m, 0, 0, [10, 10])):
            count[i][j][a] += 1
            m[i][j][a] += (G - m[i][j][a]) / count[i][j][a]
    return m


# print(improve_policy(None,None))


def pick_max():
    m = []
    a = improve_policy(None, None)
    for i in a:
        t = []
        for j in i:
            t.append(j.index(max(j)))
        m.append(t)
    return m


def act():
    for i in len(pick_max()[0]):
        for j in len(pick_max()):
            for a in ACTIONS:
                if pick_max()[i][j] == a:
                    pick_max()[i][j] = A[a]
    return pick_max()


print(act())
