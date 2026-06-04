from _typeshed import Incomplete
from flaml.onlineml import VowpalWabbitTrial as VowpalWabbitTrial
from flaml.tune import Categorical as Categorical, Float as Float, PolynomialExpansionSet as PolynomialExpansionSet, Trial as Trial
from flaml.tune.searcher import CFO as CFO
from typing import Dict

logger: Incomplete

class BaseSearcher:
    """Abstract class for an online searcher."""
    def __init__(self, metric: str | None = None, mode: str | None = None) -> None: ...
    def set_search_properties(self, metric: str | None = None, mode: str | None = None, config: Dict | None = None): ...
    def next_trial(self) -> None: ...
    def on_trial_result(self, trial_id: str, result: Dict): ...
    def on_trial_complete(self, trial) -> None: ...

class ChampionFrontierSearcher(BaseSearcher):
    """The ChampionFrontierSearcher class.

    NOTE about the correspondence about this code and the research paper:
    [ChaCha for Online AutoML](https://arxiv.org/pdf/2106.04815.pdf).
    This class serves the role of ConfigOralce as described in the paper.
    """
    POLY_EXPANSION_ADDITION_NUM: int
    EXPANSION_ORDER: int
    NUMERICAL_NUM: int
    CFO_SEARCHER_METRIC_NAME: str
    CFO_SEARCHER_LARGE_LOSS: float
    NUM_RANDOM_SEED: int
    CHAMPION_TRIAL_NAME: str
    TRIAL_CLASS = VowpalWabbitTrial
    def __init__(self, init_config: Dict, space: Dict | None = None, metric: str | None = None, mode: str | None = None, random_seed: int | None = 2345, online_trial_args: Dict | None = {}, nonpoly_searcher_name: str | None = 'CFO') -> None:
        """Constructor.

        Args:
            init_config: A dictionary of initial configuration.
            space: A dictionary to specify the search space.
            metric: A string of the metric name to optimize for.
            mode: A string in ['min', 'max'] to specify the objective as
                minimization or maximization.
            random_seed: An integer of the random seed.
            online_trial_args: A dictionary to specify the online trial
                arguments for experimental purpose.
            nonpoly_searcher_name: A string to specify the search algorithm
                for nonpoly hyperparameters.
        """
    def set_search_properties(self, metric: str | None = None, mode: str | None = None, config: Dict | None = {}, setting: Dict | None = {}, init_call: bool | None = False):
        """Construct search space with the given config, and setup the search."""
    def next_trial(self):
        """Return a trial from the _challenger_list."""
