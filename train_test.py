import gymnasium as gym
from gymnasium import spaces
import numpy as np


class myenv(gym.Env):
    def __init__(self):
        super().__init__()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=5, shape=(5, 5), dtype=np.int32)
        self.x = 0
        self.y = 0
        self.goal = [4, 4]

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

        terminated = (self.x, self.y) == self.goal

        reward = 10 if terminated else -1
        state = np.array([self.x, self.y], dtype=np.int32)
        return state, reward, terminated, False, {}

    def policy(self):
        if self.x < 5:
            self.x += 1
        if self.y < 5:
            self.y += 1


env = myenv()
state, info = env.reset()
while True:
    env.policy()
