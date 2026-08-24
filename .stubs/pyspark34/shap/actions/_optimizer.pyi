from ..utils._exceptions import ConvergenceError as ConvergenceError, InvalidAction as InvalidAction
from ._action import Action as Action
from _typeshed import Incomplete

class ActionOptimizer:
    model: Incomplete
    action_groups: Incomplete
    def __init__(self, model, actions) -> None: ...
    def __call__(self, *args, max_evals: int = 10000): ...
