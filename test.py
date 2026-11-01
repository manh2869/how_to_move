import random
from collections import defaultdict

GRID = 3
TERMINAL = (GRID - 1, GRID - 1)
ACTIONS = ("up", "down", "left", "right")
DELTAS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
rng = random.Random(1)


def grid():
    return [[0 for _ in range(GRID)] for _ in range(GRID)]


def step(i, j, action):
    if (i, j) == TERMINAL:
        return i, j, 0.0, True
    dr, dc = DELTAS[action]
    r, c = i, j
    nr = min(max(r + dr, 0), GRID - 1)
    nc = min(max(c + dc, 0), GRID - 1)
    return nr, nc, -1.0, (nr, nc) == TERMINAL


def rollout(Q, max_steps=500):
    trajectory = []
    i, j = 0, 0
    for _ in range(max_steps):
        if rng.random() < 0.2 or (i, j) not in Q:
            action = rng.choice(ACTIONS)
        else:
            action = max(Q[(i, j)], key=Q[(i, j)].get)
        x, y, reward, done = step(i, j, action)
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


def improve_policy():
    Q = defaultdict(lambda: {a: 0.0 for a in ACTIONS})
    counts = defaultdict(lambda: {a: 0 for a in ACTIONS})
    for _ in range(10000):
        for i, j, a, G in episode_cost(rollout(Q)):
            counts[(i, j)][a] += 1
            Q[(i, j)][a] += (G - Q[(i, j)][a]) / counts[(i, j)][a]
    return Q.items()


def move():
    m = grid()
    for Q in improve_policy():
        m[Q[0][0]][Q[0][1]] = max(Q[1], key=Q[1].get)
    return m


print(move())
