import torch.nn as nn
from .memory import SequentialMemory as SequentialMemory
from _typeshed import Incomplete

criterion: Incomplete
USE_CUDA: Incomplete

def to_numpy(var): ...
def to_tensor(ndarray, requires_grad: bool = False): ...

class Actor(nn.Module):
    fc1: Incomplete
    fc2: Incomplete
    fc3: Incomplete
    relu: Incomplete
    sigmoid: Incomplete
    def __init__(self, nb_states, nb_actions, hidden1: int = 400, hidden2: int = 300) -> None: ...
    def forward(self, x): ...

class Critic(nn.Module):
    fc11: Incomplete
    fc12: Incomplete
    fc2: Incomplete
    fc3: Incomplete
    relu: Incomplete
    def __init__(self, nb_states, nb_actions, hidden1: int = 400, hidden2: int = 300) -> None: ...
    def forward(self, xs): ...

class DDPG(nn.Module):
    ddpg_params: Incomplete
    nb_states: Incomplete
    nb_actions: Incomplete
    actor: Incomplete
    actor_target: Incomplete
    actor_optim: Incomplete
    critic: Incomplete
    critic_target: Incomplete
    critic_optim: Incomplete
    memory: Incomplete
    batch_size: Incomplete
    tau: Incomplete
    discount: Incomplete
    depsilon: Incomplete
    lbound: float
    rbound: float
    init_delta: Incomplete
    delta_decay: Incomplete
    warmup: Incomplete
    epsilon: float
    is_training: bool
    moving_average: Incomplete
    moving_alpha: float
    def __init__(self, nb_states, nb_actions, args) -> None: ...
    def update_policy(self) -> None: ...
    def observe(self, r_t, s_t, s_t1, a_t, done) -> None: ...
    def random_action(self): ...
    def select_action(self, s_t, episode): ...
    def load_weights(self, output) -> None: ...
    def save_model(self, output) -> None: ...
    def soft_update(self, target, source) -> None: ...
    def hard_update(self, target, source) -> None: ...
    def sample_from_truncated_normal_distribution(self, lower, upper, mu, sigma, size: int = 1): ...
