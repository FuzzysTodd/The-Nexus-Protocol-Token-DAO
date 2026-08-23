from ..result import TIME_TOTAL_S as TIME_TOTAL_S
from ..space import add_cost_to_space as add_cost_to_space, unflatten_hierarchical as unflatten_hierarchical
from .flow2 import FLOW2 as FLOW2
from .suggestion import Searcher as Searcher
from _typeshed import Incomplete
from typing import Dict

logger: Incomplete

class SearchThread:
    """Class of global or local search thread."""
    cost_best: Incomplete
    cost_best2: int
    obj_best1: Incomplete
    best_result: Incomplete
    eci: Incomplete
    priority: int
    running: int
    cost_attr: Incomplete
    space: Incomplete
    def __init__(self, mode: str = 'min', search_alg: Searcher | None = None, cost_attr: str | None = ..., eps: float | None = 1.0) -> None:
        """When search_alg is omitted, use local search FLOW2."""
    def suggest(self, trial_id: str) -> Dict | None:
        """Use the suggest() of the underlying search algorithm."""
    def update_priority(self, eci: float | None = 0): ...
    speed: Incomplete
    def update_eci(self, metric_target: float, max_speed: float | None = ...): ...
    cost_last: Incomplete
    cost_best1: Incomplete
    obj_best2: Incomplete
    def on_trial_complete(self, trial_id: str, result: Dict | None = None, error: bool = False):
        """Update the statistics of the thread."""
    def on_trial_result(self, trial_id: str, result: Dict): ...
    @property
    def converged(self) -> bool: ...
    @property
    def resource(self) -> float: ...
    def reach(self, thread) -> bool:
        """Whether the incumbent can reach the incumbent of thread."""
    @property
    def can_suggest(self) -> bool:
        """Whether the thread can suggest new configs."""
