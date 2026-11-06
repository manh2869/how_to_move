import gymnasium as gym
from gymnasium import spaces
import numpy as np
import random


class myenv(gym.Env):

    def __init__(self):
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=1, shape=(5, 5), dtype=np.int32)
        self.state = np.zeros((10, 10), dtype=np.int32)
        self.steps = 0
        self.x = 0
        self.y = 0
        self.Q = np.zeros((10, 10, 4))
        self.alpha = 0.1
        self.gamma = 0.99
        self.epsilon = 0.2

    def reset(self, seed=None, options=None):

        super().reset(seed=seed)

        self.state.fill(0)

        self.steps = 0
        self.x = 0
        self.y = 0

        self.state[self.y][self.x] = 1

        observation = self.state.copy()
        info = {}

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

        return observation, reward, terminated, truncated, {}

    def choose_action(self):
        if np.random.random() < self.epsilon:
            return np.random.randint(4)

        return np.argmax(self.Q[self.y][self.x])

    def Q_table(self):

        for episode in range(10000):

            self.reset()

            while True:

                old_x = self.x
                old_y = self.y

                action = self.choose_action()

                observation, reward, terminated, truncated, info = self.step(action)

                new_x = self.x
                new_y = self.y

                if terminated:
                    future = 0
                else:
                    future = np.max(self.Q[new_y][new_x])

                old_q = self.Q[old_y][old_x][action]

                self.Q[old_y][old_x][action] += self.alpha * (
                    reward + self.gamma * future - old_q
                )

                if terminated or truncated:
                    break


