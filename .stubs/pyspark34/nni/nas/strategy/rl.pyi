from ._rl_impl import Actor as Actor, Critic as Critic, ModelEvaluationEnv as ModelEvaluationEnv, MultiThreadEnvWorker as MultiThreadEnvWorker, Preprocessor as Preprocessor
from .base import BaseStrategy as BaseStrategy
from .utils import dry_run_for_search_space as dry_run_for_search_space
from _typeshed import Incomplete
from nni.nas.execution import query_available_resources as query_available_resources
from tianshou.policy import BasePolicy as BasePolicy
from typing import Callable

has_tianshou: bool

class PolicyBasedRL(BaseStrategy):
    """
    Algorithm for policy-based reinforcement learning.
    This is a wrapper of algorithms provided in tianshou (PPO by default),
    and can be easily customized with other algorithms that inherit ``BasePolicy``
    (e.g., `REINFORCE <https://link.springer.com/content/pdf/10.1007/BF00992696.pdf>`__
    as in `this paper <https://arxiv.org/abs/1611.01578>`__).

    Parameters
    ----------
    max_collect : int
        How many times collector runs to collect trials for RL. Default 100.
    trial_per_collect : int
        How many trials (trajectories) each time collector collects.
        After each collect, trainer will sample batch from replay buffer and do the update. Default: 20.
    policy_fn : function
        Takes :class:`ModelEvaluationEnv` as input and return a policy.
        See :meth:`PolicyBasedRL._default_policy_fn` for an example.
    """
    policy_fn: Incomplete
    max_collect: Incomplete
    trial_per_collect: Incomplete
    def __init__(self, max_collect: int = 100, trial_per_collect: int = 20, policy_fn: Callable[[ModelEvaluationEnv], 'BasePolicy'] | None = None) -> None: ...
    def run(self, base_model, applied_mutators): ...
