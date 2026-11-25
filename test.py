import numpy as np
import random

q_table = [[[0 for _ in range(4)] for _ in range(5)] for _ in range(5)]


def policy(state):
    if random.randint(0, 10) < 2:
        return random.randint(0, 4)
    return np.argmax(state)


print(policy(q_table[1][1]))
