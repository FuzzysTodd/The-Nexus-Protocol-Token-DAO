import dataclasses
from .base import BaseStrategy as BaseStrategy
from .utils import dry_run_for_search_space as dry_run_for_search_space, filter_model as filter_model, get_targeted_model as get_targeted_model
from _typeshed import Incomplete
from nni.nas.execution import query_available_resources as query_available_resources, submit_models as submit_models
from nni.nas.execution.common import Model as Model, ModelStatus as ModelStatus

@dataclasses.dataclass
class Individual:
    """
    A class that represents an individual.
    Holds two attributes, where ``x`` is the model and ``y`` is the metric (e.g., accuracy).
    """
    x: dict
    y: float
    def __init__(self, x, y) -> None: ...

class RegularizedEvolution(BaseStrategy):
    '''
    Algorithm for regularized evolution (i.e. aging evolution).
    Follows "Algorithm 1" in Real et al. "Regularized Evolution for Image Classifier Architecture Search".

    Parameters
    ----------
    optimize_mode : str
        Can be one of "maximize" and "minimize". Default: maximize.
    population_size : int
        The number of individuals to keep in the population. Default: 100.
    cycles : int
        The number of cycles (trials) the algorithm should run for. Default: 20000.
    sample_size : int
        The number of individuals that should participate in each tournament. Default: 25.
    mutation_prob : float
        Probability that mutation happens in each dim. Default: 0.05
    dedup : bool
        Do not try the same configuration twice. Default: true.
    dedup_retries : int
        If dedup is true, retry the same configuration up to dedup_retries times. Default: 500.
    on_failure : str
        Can be one of "ignore" and "worst". If "ignore", simply give up the model and find a new one.
        If "worst", mark the model as -inf (if maximize, inf if minimize), so that the algorithm "learns" to avoid such model.
        Default: ignore.
    model_filter: Callable[[Model], bool]
        Feed the model and return a bool. This will filter the models in search space and select which to submit.
    '''
    optimize_mode: Incomplete
    population_size: Incomplete
    sample_size: Incomplete
    cycles: Incomplete
    mutation_prob: Incomplete
    dedup: Incomplete
    dedup_retries: Incomplete
    on_failure: Incomplete
    filter: Incomplete
    def __init__(self, optimize_mode: str = 'maximize', population_size: int = 100, sample_size: int = 25, cycles: int = 20000, mutation_prob: float = 0.05, dedup: bool = False, dedup_retries: int = 500, on_failure: str = 'ignore', model_filter: Incomplete | None = None) -> None: ...
    def random(self, search_space): ...
    def mutate(self, parent, search_space): ...
    def best_parent(self): ...
    def repeat_until_new_config(self, generator): ...
    def run(self, base_model, applied_mutators): ...
