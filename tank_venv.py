import gymnasium as gym

env = gym.make("Blackjack-v1")

observation, info = env.reset()

print("State:", observation)
print("Actions:", env.action_space)