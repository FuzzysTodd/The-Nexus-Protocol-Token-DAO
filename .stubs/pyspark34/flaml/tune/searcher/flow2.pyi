import numpy as np
from ..space import complete_config as complete_config, denormalize as denormalize, generate_variants_compatible as generate_variants_compatible, normalize as normalize
from ..trial import flatten_dict as flatten_dict, unflatten_dict as unflatten_dict
from .suggestion import Searcher as Searcher
from _typeshed import Incomplete
from flaml.config import SAMPLE_MULTIPLY_FACTOR as SAMPLE_MULTIPLY_FACTOR
from flaml.tune import sample as sample
from typing import Dict, Tuple

logger: Incomplete

class FLOW2(Searcher):
    """Local search algorithm FLOW2, with adaptive step size."""
    STEPSIZE: float
    STEP_LOWER_BOUND: float
    metric_op: float
    space: Incomplete
    rs_random: Incomplete
    seed: Incomplete
    init_config: Incomplete
    best_config: Incomplete
    resource_attr: Incomplete
    min_resource: Incomplete
    lexico_objectives: Incomplete
    resource_multiple_factor: Incomplete
    cost_attr: Incomplete
    max_resource: Incomplete
    def __init__(self, init_config: dict, metric: str | None = None, mode: str | None = None, space: dict | None = None, resource_attr: str | None = None, min_resource: float | None = None, max_resource: float | None = None, resource_multiple_factor: float | None = None, cost_attr: str | None = 'time_total_s', seed: int | None = 20, lexico_objectives: Incomplete | None = None) -> None:
        '''Constructor.

        Args:
            init_config: a dictionary of a partial or full initial config,
                e.g., from a subset of controlled dimensions
                to the initial low-cost values.
                E.g., {\'epochs\': 1}.
            metric: A string of the metric name to optimize for.
            mode: A string in [\'min\', \'max\'] to specify the objective as
                minimization or maximization.
            space: A dictionary to specify the search space.
            resource_attr: A string to specify the resource dimension and the best
                performance is assumed to be at the max_resource.
            min_resource: A float of the minimal resource to use for the resource_attr.
            max_resource: A float of the maximal resource to use for the resource_attr.
            resource_multiple_factor: A float of the multiplicative factor
                used for increasing resource.
            cost_attr: A string of the attribute used for cost.
            seed: An integer of the random seed.
            lexico_objectives: dict, default=None | It specifics information needed to perform multi-objective
                optimization with lexicographic preferences. When lexico_objectives is not None, the arguments metric,
                mode will be invalid. This dictionary shall contain the following fields of key-value pairs:
                - "metrics":  a list of optimization objectives with the orders reflecting the priorities/preferences of the
                objectives.
                - "modes" (optional): a list of optimization modes (each mode either "min" or "max") corresponding to the
                objectives in the metric list. If not provided, we use "min" as the default mode for all the objectives
                - "targets" (optional): a dictionary to specify the optimization targets on the objectives. The keys are the
                metric names (provided in "metric"), and the values are the numerical target values.
                - "tolerances" (optional): a dictionary to specify the optimality tolerances on objectives. The keys are the metric names (provided in "metrics"), and the values are the absolute/percentage tolerance in the form of numeric/string.
                E.g.,
                ```python
                lexico_objectives = {
                    "metrics": ["error_rate", "pred_time"],
                    "modes": ["min", "min"],
                    "tolerances": {"error_rate": 0.01, "pred_time": 0.0},
                    "targets": {"error_rate": 0.0},
                }
                ```
                We also support percentage tolerance.
                E.g.,
                ```python
                lexico_objectives = {
                    "metrics": ["error_rate", "pred_time"],
                    "modes": ["min", "min"],
                    "tolerances": {"error_rate": "5%", "pred_time": "0%"},
                    "targets": {"error_rate": 0.0},
                   }
                ```
        '''
    @property
    def step_lower_bound(self) -> float: ...
    @property
    def resource(self) -> float: ...
    def rand_vector_gaussian(self, dim, std: float = 1.0): ...
    def complete_config(self, partial_config: Dict, lower: Dict | None = None, upper: Dict | None = None) -> Tuple[Dict, Dict]:
        """Generate a complete config from the partial config input.

        Add minimal resource to config if available.
        """
    def create(self, init_config: Dict, obj: float, cost: float, space: Dict) -> Searcher: ...
    def normalize(self, config, recursive: bool = False) -> Dict:
        """normalize each dimension in config to [0,1]."""
    def denormalize(self, config):
        """denormalize each dimension in config from [0,1]."""
    def set_search_properties(self, metric: str | None = None, mode: str | None = None, config: Dict | None = None) -> bool: ...
    def update_fbest(self) -> None: ...
    def lexico_compare(self, result) -> bool: ...
    best_obj: Incomplete
    incumbent: Incomplete
    cost_incumbent: Incomplete
    step: Incomplete
    def on_trial_complete(self, trial_id: str, result: Dict | None = None, error: bool = False):
        """
        Compare with incumbent.
        If better, move, reset num_complete and num_proposed.
        If not better and num_complete >= 2*dim, num_allowed += 2.
        """
    def on_trial_result(self, trial_id: str, result: Dict):
        """Early update of incumbent."""
    def rand_vector_unit_sphere(self, dim, trunc: int = 0) -> np.ndarray: ...
    def suggest(self, trial_id: str) -> Dict | None:
        """Suggest a new config, one of the following cases:
        1. same incumbent, increase resource.
        2. same resource, move from the incumbent to a random direction.
        3. same resource, move from the incumbent to the opposite direction.
        """
    @property
    def can_suggest(self) -> bool:
        """Can't suggest if 2*dim configs have been proposed for the incumbent
        while fewer are completed.
        """
    def config_signature(self, config, space: Dict = None) -> tuple:
        """Return the signature tuple of a config."""
    @property
    def converged(self) -> bool:
        """Whether the local search has converged."""
    def reach(self, other: Searcher) -> bool:
        """whether the incumbent can reach the incumbent of other."""
