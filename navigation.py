from unityagents import UnityEnvironment
from dqn_agent import Agent
import numpy as np
import torch

env = UnityEnvironment(file_name="Banana.app")
brain_name = env.brain_names[0]
brain = env.brains[brain_name]

env_info = env.reset(train_mode=True)[brain_name]

action_size = brain.vector_action_space_size
 
state = env_info.vector_observations[0]

state_size = len(state)

SEED=0

agent = Agent(state_size=state_size, action_size=action_size, seed=SEED)
agent.qnetwork_local.load_state_dict(torch.load('checkpoint.pth'))

env_info = env.reset(train_mode=False)[brain_name]

state = env_info.vector_observations[0]
score = 0

print("Playing the environment...")

while True:
    action = agent.act(state)
    env_info = env.step(action)[brain_name]
    next_state = env_info.vector_observations[0]
    reward = env_info.rewards[0]
    done = env_info.local_done[0]
    score += reward
    state = next_state
    if done:
        break
print("Score: {}".format(score))
env.close()