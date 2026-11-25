import gymnasium as gym
from gymnasium import spaces
import numpy as np
import random


class myenv(gym.Env):
    def __init__(self):
        super().__init__()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=5, shape=(5, 5), dtype=np.int32)
        self.x = 0
        self.y = 0
        self.goal = (4, 4)
        self.count = 0

        self.q_table = [[[0 for _ in range(4)] for _ in range(5)] for _ in range(5)]

    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed, options=options)
        self.x = 0
        self.y = 0
        return np.array([self.x, self.y], dtype=np.int32), {}

    def step(self, action):

        if action == 0:
            self.y -= 1
        elif action == 1:
            self.y += 1
        elif action == 2:
            self.x -= 1
        elif action == 3:
            self.x += 1

        self.x = np.clip(self.x, 0, 5)
        self.y = np.clip(self.y, 0, 5)
        self.count += 1

        terminated = (self.x, self.y) == self.goal

        reward = 10 if terminated else -1
        state = np.array([self.x, self.y], dtype=np.int32)
        return state, reward, terminated, self.count > 100, {}

    def rollout(self, max_steps=500):
        trajectory = []
        i, j = 0, 0
        for _ in range(max_steps):
            _, reward, done, done, _ = self.step(
                self.policy(self.q_table[self.x][self.y])
            )
            trajectory.append([i, j, action, reward])
            i, j = self.x, self.y
            if done:
                break
        return trajectory

    def policy(self, state):
        if random.randint(0, 10) <= 2:
            return random.randint(0, 4)
        return np.argmax(state)

    def trajectory(self):
        for i in range(100):
            self.step(self.policy())


# def policy():
#     return random.randint(0, 4)


env = myenv()
state, info = env.reset()
while True:
    action = policy()
    state, reward, terminated, truncated, info = env.step(action)
    print(state, reward, terminated, truncated, info)
    if terminated or truncated:
        print("end")
        break
env.close()
