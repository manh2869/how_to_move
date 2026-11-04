import gymnasium as gym
from gymnasium import spaces
import numpy as np

# import time


class myenv(gym.Env):
    def __init__(self):

        self.action_space = spaces.Discrete(2)

        self.observation_space = spaces.Box(low=0, high=5, shape=(1,), dtype=np.int32)

        self.state = 0
        self.steps = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.state = 0
        self.steps = 0

        observation = np.array([self.state], dtype=np.int32)
        info = {}

        return observation, info

    def step(self, action):

        # Thực hiện hành động
        if action == 0:
            self.state -= 1
        elif action == 1:
            self.state += 1

        self.state = np.clip(self.state, 0, 5)

        self.steps += 1
        terminated = self.state == 5
        truncated = self.steps >= 10 and not terminated

        reward = 10 if terminated else -1

        observation = np.array([self.state], dtype=np.int32)
        info = {}

        return observation, reward, terminated, truncated, info


env = myenv()
env.reset()
for i in range(10):

    action = env.action_space.sample()

    observation, reward, terminated, truncated, info = env.step(action)

    print("Action:", action, "Observation:", observation, "Reward:", reward)

    if terminated or truncated:
        print("Episode kết thúc")
        break
