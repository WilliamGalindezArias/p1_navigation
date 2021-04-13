## Navigation - Project 1

#### Agent - Model

The agent that interacts and learned from the environment uses a `QNetwork`that inherits from torch `nn.Module`  

The parameters of the model are:  
- state_size
- action_size
- 3 Neural Network layers
- Relu activation function 

The *forward pass* in the Neural Network maps *state* to *action values*

# Artifacts

1. [Notebook](https://gitlab.com/r-learning/navigation/-/blob/master/01-navigation-wg-delivered.ipynb) with solution
2. Script to run the environment outside jupyter-notebook `navigation.py`(https://gitlab.com/r-learning/navigation/-/blob/master/navigation.py)
3. Weights `checkpoint.pth` of trained model in root folder [Navigation](https://gitlab.com/r-learning/navigation)

#### Agent parameters

```
BUFFER_SIZE = int(1e5)  # replay buffer size  
BATCH_SIZE = 64         # minibatch size
GAMMA = 0.99            # discount factor
TAU = 1e-3              # for soft update of target parameters
LR = 5e-4               # learning rate 
UPDATE_EVERY = 10        # how often to update the network
```

The value `UPDATE_EVERY` was set to 10 to improve the learning in the algorithm. With values < 10 the average score had considerable deviations.

#### Learning

The Environment is solved once it gets a `score > 15` after `766` episodes
![learning](learning.png)

