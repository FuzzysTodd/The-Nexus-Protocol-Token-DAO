from .base import BaseStrategy as BaseStrategy
from .utils import dry_run_for_search_space as dry_run_for_search_space, filter_model as filter_model, get_targeted_model as get_targeted_model
from _typeshed import Incomplete
from nni.nas.execution import budget_exhausted as budget_exhausted, query_available_resources as query_available_resources, submit_models as submit_models
from nni.nas.mutable import InvalidMutation as InvalidMutation, Sampler as Sampler
from typing import Any, Dict, List

def grid_generator(search_space: Dict[Any, List[Any]], shuffle: bool = True): ...
def random_generator(search_space: Dict[Any, List[Any]], dedup: bool = True, retries: int = 500): ...

class GridSearch(BaseStrategy):
    """
    Traverse the search space and try all the possible combinations one by one.

    Parameters
    ----------
    shuffle : bool
        Shuffle the order in a candidate list, so that they are tried in a random order. Default: true.
    """
    shuffle: Incomplete
    def __init__(self, shuffle: bool = True) -> None: ...
    def run(self, base_model, applied_mutators) -> None: ...

class _RandomSampler(Sampler):
    def choice(self, candidates, mutator, model, index): ...

class Random(BaseStrategy):
    """
    Random search on the search space.

    Parameters
    ----------
    variational : bool
        Do not dry run to get the full search space. Used when the search space has variational size or candidates. Default: false.
    dedup : bool
        Do not try the same configuration twice. When variational is true, deduplication is not supported. Default: true.
    model_filter: Callable[[Model], bool]
        Feed the model and return a bool. This will filter the models in search space and select which to submit.
    """
    variational: Incomplete
    dedup: Incomplete
    random_sampler: Incomplete
    filter: Incomplete
    def __init__(self, variational: bool = False, dedup: bool = True, model_filter: Incomplete | None = None) -> None: ...
    def run(self, base_model, applied_mutators) -> None: ...
