from .. import INCUMBENT_RESULT as INCUMBENT_RESULT
from ..result import TIME_TOTAL_S as TIME_TOTAL_S
from ..sample import choice as choice, loguniform as loguniform, qloguniform as qloguniform, qrandint as qrandint, qrandn as qrandn, quniform as quniform, randint as randint, randn as randn, uniform as uniform
from ..space import add_cost_to_space as add_cost_to_space, define_by_run_func as define_by_run_func, indexof as indexof, normalize as normalize
from ..trial import flatten_dict as flatten_dict, unflatten_dict as unflatten_dict
from .flow2 import FLOW2 as FLOW2
from .search_thread import SearchThread as SearchThread
from .suggestion import Searcher as Searcher
from _typeshed import Incomplete
from nni.tuner import Tuner as NNITuner
from typing import Callable, Dict, List, Tuple

SEARCH_THREAD_EPS: float
PENALTY: float
logger: Incomplete

class BlendSearch(Searcher):
    """class for BlendSearch algorithm."""
    lagrange: str
    LocalSearch = FLOW2
    cost_attr: Incomplete
    penalty: Incomplete
    lexico_objectives: Incomplete
    def __init__(self, metric: str | None = None, mode: str | None = None, space: dict | None = None, low_cost_partial_config: dict | None = None, cat_hp_cost: dict | None = None, points_to_evaluate: List[dict] | None = None, evaluated_rewards: List | None = None, time_budget_s: int | float = None, num_samples: int | None = None, resource_attr: str | None = None, min_resource: float | None = None, max_resource: float | None = None, reduction_factor: float | None = None, global_search_alg: Searcher | None = None, config_constraints: List[Tuple[Callable[[dict], float], str, float]] | None = None, metric_constraints: List[Tuple[str, str, float]] | None = None, seed: int | None = 20, cost_attr: str | None = 'auto', cost_budget: float | None = None, experimental: bool | None = False, lexico_objectives: dict | None = None, use_incumbent_result_in_evaluation: bool = False, allow_empty_config: bool = False) -> None:
        '''Constructor.

        Args:
            metric: A string of the metric name to optimize for.
            mode: A string in [\'min\', \'max\'] to specify the objective as
                minimization or maximization.
            space: A dictionary to specify the search space.
            low_cost_partial_config: A dictionary from a subset of
                controlled dimensions to the initial low-cost values.
                E.g., ```{\'n_estimators\': 4, \'max_leaves\': 4}```.
            cat_hp_cost: A dictionary from a subset of categorical dimensions
                to the relative cost of each choice.
                E.g., ```{\'tree_method\': [1, 1, 2]}```.
                I.e., the relative cost of the three choices of \'tree_method\'
                is 1, 1 and 2 respectively.
            points_to_evaluate: Initial parameter suggestions to be run first.
            evaluated_rewards (list): If you have previously evaluated the
                parameters passed in as points_to_evaluate you can avoid
                re-running those trials by passing in the reward attributes
                as a list so the optimiser can be told the results without
                needing to re-compute the trial. Must be the same or shorter length than
                points_to_evaluate. When provided, `mode` must be specified.
            time_budget_s: int or float | Time budget in seconds.
            num_samples: int | The number of configs to try. -1 means no limit on the
                number of configs to try.
            resource_attr: A string to specify the resource dimension and the best
                performance is assumed to be at the max_resource.
            min_resource: A float of the minimal resource to use for the resource_attr.
            max_resource: A float of the maximal resource to use for the resource_attr.
            reduction_factor: A float of the reduction factor used for
                incremental pruning.
            global_search_alg: A Searcher instance as the global search
                instance. If omitted, Optuna is used. The following algos have
                known issues when used as global_search_alg:
                - HyperOptSearch raises exception sometimes
                - TuneBOHB has its own scheduler
            config_constraints: A list of config constraints to be satisfied.
                E.g., ```config_constraints = [(mem_size, \'<=\', 1024**3)]```.
                `mem_size` is a function which produces a float number for the bytes
                needed for a config.
                It is used to skip configs which do not fit in memory.
            metric_constraints: A list of metric constraints to be satisfied.
                E.g., `[\'precision\', \'>=\', 0.9]`. The sign can be ">=" or "<=".
            seed: An integer of the random seed.
            cost_attr: None or str to specify the attribute to evaluate the cost of different trials.
                Default is "auto", which means that we will automatically choose the cost attribute to use (depending
                on the nature of the resource budget). When cost_attr is set to None, cost differences between different trials will be omitted
                in our search algorithm. When cost_attr is set to a str different from "auto" and "time_total_s",
                this cost_attr must be available in the result dict of the trial.
            cost_budget: A float of the cost budget. Only valid when cost_attr is a str different from "auto" and "time_total_s".
            lexico_objectives: dict, default=None | It specifics information needed to perform multi-objective
                optimization with lexicographic preferences. This is only supported in CFO currently.
                When lexico_objectives is not None, the arguments metric, mode will be invalid.
                This dictionary shall contain the  following fields of key-value pairs:
                - "metrics":  a list of optimization objectives with the orders reflecting the priorities/preferences of the
                objectives.
                - "modes" (optional): a list of optimization modes (each mode either "min" or "max") corresponding to the
                objectives in the metric list. If not provided, we use "min" as the default mode for all the objectives.
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
            experimental: A bool of whether to use experimental features.
        '''
    def set_search_properties(self, metric: str | None = None, mode: str | None = None, config: Dict | None = None, **spec) -> bool: ...
    def save(self, checkpoint_path: str):
        """save states to a checkpoint path."""
    __dict__: Incomplete
    def restore(self, checkpoint_path: str):
        """restore states from checkpoint."""
    @property
    def metric_target(self): ...
    @property
    def is_ls_ever_converged(self): ...
    def on_trial_complete(self, trial_id: str, result: Dict | None = None, error: bool = False):
        """search thread updater and cleaner."""
    def on_trial_result(self, trial_id: str, result: Dict):
        """receive intermediate result."""
    def suggest(self, trial_id: str) -> Dict | None:
        """choose thread, suggest a valid config."""
    @property
    def results(self) -> List[Dict]:
        '''A list of dicts of results for each evaluated configuration.

        Each dict has "config" and metric names as keys.
        The returned dict includes the initial results provided via `evaluated_reward`.
        '''
NNITuner = object

class BlendSearchTuner(BlendSearch, NNITuner):
    """Tuner class for NNI."""
    def receive_trial_result(self, parameter_id, parameters, value, **kwargs) -> None:
        """Receive trial's final result.

        Args:
            parameter_id: int.
            parameters: object created by `generate_parameters()`.
            value: final metrics of the trial, including default metric.
        """
    def generate_parameters(self, parameter_id, **kwargs) -> Dict:
        """Returns a set of trial (hyper-)parameters, as a serializable object.

        Args:
            parameter_id: int.
        """
    def update_search_space(self, search_space) -> None:
        """Required by NNI.

        Tuners are advised to support updating search space at run-time.
        If a tuner can only set search space once before generating first hyper-parameters,
        it should explicitly document this behaviour.

        Args:
            search_space: JSON object created by experiment owner.
        """

class CFO(BlendSearchTuner):
    """class for CFO algorithm."""
    def suggest(self, trial_id: str) -> Dict | None: ...
    def on_trial_complete(self, trial_id: str, result: Dict | None = None, error: bool = False): ...

class RandomSearch(CFO):
    """Class for random search."""
    def suggest(self, trial_id: str) -> Dict | None: ...
    def on_trial_complete(self, trial_id: str, result: Dict | None = None, error: bool = False): ...
    def on_trial_result(self, trial_id: str, result: Dict): ...
