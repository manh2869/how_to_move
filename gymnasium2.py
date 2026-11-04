import gymnasium as gym
from gymnasium import spaces
import numpy as np

# import time


class myenv(gym.Env):
    def __init__(self):

        self.action_space = spaces.Discrete(4)

        self.observation_space = spaces.Box(
            low=0, high=20, shape=(5, 5), dtype=np.int32
        )

        self.state = np.zeros((5, 5), dtype=np.int32)
        self.steps = 0
        self.x = 0
        self.y = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.state[0][0] = 0
        self.steps = 0

        observation = np.array([self.state], dtype=np.int32)
        info = {}
        self.x = 0
        self.y = 0

        self.state[self.y][self.x] = 1

        return observation, info

    def step(self, action):

        self.state[self.y][self.x] = 0

        if action == 0:
            self.y -= 1
        elif action == 1:
            self.y += 1
        elif action == 2:
            self.x -= 1
        elif action == 3:
            self.x += 1

        self.x = np.clip(self.x, 0, 4)
        self.y = np.clip(self.y, 0, 4)

        self.state[self.y][self.x] = 1

        self.steps += 1

        terminated = self.x == 4 and self.y == 4
        truncated = self.steps >= 1000

        reward = 10 if terminated else -1

        observation = self.state.copy()
        info = {}

        return observation, reward, terminated, truncated, info


env = myenv()
env.reset()
for i in range(1000):

    action = env.action_space.sample()

    observation, reward, terminated, truncated, info = env.step(action)

    print("Action:", action)
    print("Observation:\n", observation)
    print("Reward:", reward)

    if terminated or truncated:
        observation, info = env.reset()
        print("end")
