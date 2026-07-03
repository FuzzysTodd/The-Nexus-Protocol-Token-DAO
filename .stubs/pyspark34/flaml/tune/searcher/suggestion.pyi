from ..sample import Categorical as Categorical, Domain as Domain, Float as Float, Integer as Integer, LogUniform as LogUniform, Quantized as Quantized, Uniform as Uniform
from ..trial import flatten_dict as flatten_dict, unflatten_dict as unflatten_dict
from .variant_generator import parse_spec_vars as parse_spec_vars
from _typeshed import Incomplete
from collections import defaultdict as defaultdict
from optuna.distributions import BaseDistribution as OptunaDistribution
from optuna.samplers import BaseSampler
from optuna.trial import Trial as OptunaTrial
from typing import Any, Callable, Dict, List, Tuple

logger: Incomplete
UNRESOLVED_SEARCH_SPACE: Incomplete
UNDEFINED_SEARCH_SPACE: Incomplete
UNDEFINED_METRIC_MODE: Incomplete

class Searcher:
    '''Abstract class for wrapping suggesting algorithms.
    Custom algorithms can extend this class easily by overriding the
    `suggest` method provide generated parameters for the trials.
    Any subclass that implements ``__init__`` must also call the
    constructor of this class: ``super(Subclass, self).__init__(...)``.
    To track suggestions and their corresponding evaluations, the method
    `suggest` will be passed a trial_id, which will be used in
    subsequent notifications.
    Not all implementations support multi objectives.
    Args:
        metric (str or list): The training result objective value attribute. If
            list then list of training result objective value attributes
        mode (str or list): If string One of {min, max}. If list then
            list of max and min, determines whether objective is minimizing
            or maximizing the metric attribute. Must match type of metric.

    ```python
    class ExampleSearch(Searcher):
        def __init__(self, metric="mean_loss", mode="min", **kwargs):
            super(ExampleSearch, self).__init__(
                metric=metric, mode=mode, **kwargs)
            self.optimizer = Optimizer()
            self.configurations = {}
        def suggest(self, trial_id):
            configuration = self.optimizer.query()
            self.configurations[trial_id] = configuration
        def on_trial_complete(self, trial_id, result, **kwargs):
            configuration = self.configurations[trial_id]
            if result and self.metric in result:
                self.optimizer.update(configuration, result[self.metric])
    tune.run(trainable_function, search_alg=ExampleSearch())
    ```

    '''
    FINISHED: str
    CKPT_FILE_TMPL: str
    def __init__(self, metric: str | None = None, mode: str | None = None, max_concurrent: int | None = None, use_early_stopped_trials: bool | None = None) -> None: ...
    def set_search_properties(self, metric: str | None, mode: str | None, config: Dict) -> bool:
        '''Pass search properties to searcher.
        This method acts as an alternative to instantiating search algorithms
        with their own specific search spaces. Instead they can accept a
        Tune config through this method. A searcher should return ``True``
        if setting the config was successful, or ``False`` if it was
        unsuccessful, e.g. when the search space has already been set.
        Args:
            metric (str): Metric to optimize
            mode (str): One of ["min", "max"]. Direction to optimize.
            config (dict): Tune config dict.
        '''
    def on_trial_result(self, trial_id: str, result: Dict):
        """Optional notification for result during training.
        Note that by default, the result dict may include NaNs or
        may not include the optimization metric. It is up to the
        subclass implementation to preprocess the result to
        avoid breaking the optimization process.
        Args:
            trial_id (str): A unique string ID for the trial.
            result (dict): Dictionary of metrics for current training progress.
                Note that the result dict may include NaNs or
                may not include the optimization metric. It is up to the
                subclass implementation to preprocess the result to
                avoid breaking the optimization process.
        """
    @property
    def metric(self) -> str:
        """The training result objective value attribute."""
    @property
    def mode(self) -> str:
        """Specifies if minimizing or maximizing the metric."""

class ConcurrencyLimiter(Searcher):
    '''A wrapper algorithm for limiting the number of concurrent trials.
    Args:
        searcher (Searcher): Searcher object that the
            ConcurrencyLimiter will manage.
        max_concurrent (int): Maximum concurrent samples from the underlying
            searcher.
        batch (bool): Whether to wait for all concurrent samples
            to finish before updating the underlying searcher.
    Example:
    ```python
    from ray.tune.suggest import ConcurrencyLimiter  # ray version < 2
    search_alg = HyperOptSearch(metric="accuracy")
    search_alg = ConcurrencyLimiter(search_alg, max_concurrent=2)
    tune.run(trainable, search_alg=search_alg)
    ```
    '''
    searcher: Incomplete
    max_concurrent: Incomplete
    batch: Incomplete
    live_trials: Incomplete
    cached_results: Incomplete
    def __init__(self, searcher: Searcher, max_concurrent: int, batch: bool = False) -> None: ...
    def suggest(self, trial_id: str) -> Dict | None: ...
    def on_trial_complete(self, trial_id: str, result: Dict | None = None, error: bool = False): ...
    def get_state(self) -> Dict: ...
    def set_state(self, state: Dict): ...
    def save(self, checkpoint_path: str): ...
    def restore(self, checkpoint_path: str): ...
    def on_pause(self, trial_id: str): ...
    def on_unpause(self, trial_id: str): ...
    def set_search_properties(self, metric: str | None, mode: str | None, config: Dict) -> bool: ...

DEFAULT_METRIC: str
TRAINING_ITERATION: str
DEFINE_BY_RUN_WARN_THRESHOLD_S: int

def validate_warmstart(parameter_names: List[str], points_to_evaluate: List[List | Dict], evaluated_rewards: List, validate_point_name_lengths: bool = True):
    """Generic validation of a Searcher's warm start functionality.
    Raises exceptions in case of type and length mismatches between
    parameters.
    If ``validate_point_name_lengths`` is False, the equality of lengths
    between ``points_to_evaluate`` and ``parameter_names`` will not be
    validated.
    """

class _OptunaTrialSuggestCaptor:
    """Utility to capture returned values from Optuna's suggest_ methods.

    This will wrap around the ``optuna.Trial` object and decorate all
    `suggest_` callables with a function capturing the returned value,
    which will be saved in the ``captured_values`` dict.
    """
    ot_trial: Incomplete
    captured_values: Incomplete
    def __init__(self, ot_trial: OptunaTrial) -> None: ...
    def __getattr__(self, item_name: str) -> Any: ...

class OptunaSearch(Searcher):
    '''A wrapper around Optuna to provide trial suggestions.

    `Optuna <https://optuna.org/>`_ is a hyperparameter optimization library.
    In contrast to other libraries, it employs define-by-run style
    hyperparameter definitions.

    This Searcher is a thin wrapper around Optuna\'s search algorithms.
    You can pass any Optuna sampler, which will be used to generate
    hyperparameter suggestions.

    Multi-objective optimization is supported.

    Args:
        space: Hyperparameter search space definition for
            Optuna\'s sampler. This can be either a dict with
            parameter names as keys and ``optuna.distributions`` as values,
            or a Callable - in which case, it should be a define-by-run
            function using ``optuna.trial`` to obtain the hyperparameter
            values. The function should return either a dict of
            constant values with names as keys, or None.
            For more information, see https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/002_configurations.html.

            Warning - No actual computation should take place in the define-by-run
            function. Instead, put the training logic inside the function
            or class trainable passed to ``tune.run``.

        metric: The training result objective value attribute. If
            None but a mode was passed, the anonymous metric ``_metric``
            will be used per default. Can be a list of metrics for
            multi-objective optimization.
        mode: One of {min, max}. Determines whether objective is
            minimizing or maximizing the metric attribute. Can be a list of
            modes for multi-objective optimization (corresponding to
            ``metric``).
        points_to_evaluate: Initial parameter suggestions to be run
            first. This is for when you already have some good parameters
            you want to run first to help the algorithm make better suggestions
            for future parameters. Needs to be a list of dicts containing the
            configurations.
        sampler: Optuna sampler used to
            draw hyperparameter configurations. Defaults to ``MOTPESampler``
            for multi-objective optimization with Optuna<2.9.0, and
            ``TPESampler`` in every other case.

            Warning: Please note that with Optuna 2.10.0 and earlier
                default ``MOTPESampler``/``TPESampler`` suffer
                from performance issues when dealing with a large number of
                completed trials (approx. >100). This will manifest as
                a delay when suggesting new configurations.
                This is an Optuna issue and may be fixed in a future
                Optuna release.

        seed: Seed to initialize sampler with. This parameter is only
            used when ``sampler=None``. In all other cases, the sampler
            you pass should be initialized with the seed already.
        evaluated_rewards: If you have previously evaluated the
            parameters passed in as points_to_evaluate you can avoid
            re-running those trials by passing in the reward attributes
            as a list so the optimiser can be told the results without
            needing to re-compute the trial. Must be the same length as
            points_to_evaluate.

            Warning - When using ``evaluated_rewards``, the search space ``space``
            must be provided as a dict with parameter names as
            keys and ``optuna.distributions`` instances as values. The
            define-by-run search space definition is not yet supported with
            this functionality.

    Tune automatically converts search spaces to Optuna\'s format:

    ```python
    from ray.tune.suggest.optuna import OptunaSearch

    config = {
        "a": tune.uniform(6, 8)
        "b": tune.loguniform(1e-4, 1e-2)
    }

    optuna_search = OptunaSearch(
        metric="loss",
        mode="min")

    tune.run(trainable, config=config, search_alg=optuna_search)
    ```

    If you would like to pass the search space manually, the code would
    look like this:

    ```python
    from ray.tune.suggest.optuna import OptunaSearch
    import optuna

    space = {
        "a": optuna.distributions.UniformDistribution(6, 8),
        "b": optuna.distributions.LogUniformDistribution(1e-4, 1e-2),
    }

    optuna_search = OptunaSearch(
        space,
        metric="loss",
        mode="min")

    tune.run(trainable, search_alg=optuna_search)

    # Equivalent Optuna define-by-run function approach:

    def define_search_space(trial: optuna.Trial):
        trial.suggest_float("a", 6, 8)
        trial.suggest_float("b", 1e-4, 1e-2, log=True)
        # training logic goes into trainable, this is just
        # for search space definition

    optuna_search = OptunaSearch(
        define_search_space,
        metric="loss",
        mode="min")

    tune.run(trainable, search_alg=optuna_search)
    ```

    Multi-objective optimization is supported:

    ```python
    from ray.tune.suggest.optuna import OptunaSearch
    import optuna

    space = {
        "a": optuna.distributions.UniformDistribution(6, 8),
        "b": optuna.distributions.LogUniformDistribution(1e-4, 1e-2),
    }

    # Note you have to specify metric and mode here instead of
    # in tune.run
    optuna_search = OptunaSearch(
        space,
        metric=["loss1", "loss2"],
        mode=["min", "max"])

    # Do not specify metric and mode here!
    tune.run(
        trainable,
        search_alg=optuna_search
    )
    ```

    You can pass configs that will be evaluated first using
    ``points_to_evaluate``:

    ```python
    from ray.tune.suggest.optuna import OptunaSearch
    import optuna

    space = {
        "a": optuna.distributions.UniformDistribution(6, 8),
        "b": optuna.distributions.LogUniformDistribution(1e-4, 1e-2),
    }

    optuna_search = OptunaSearch(
        space,
        points_to_evaluate=[{"a": 6.5, "b": 5e-4}, {"a": 7.5, "b": 1e-3}]
        metric="loss",
        mode="min")

    tune.run(trainable, search_alg=optuna_search)
    ```

    Avoid re-running evaluated trials by passing the rewards together with
    `points_to_evaluate`:

    ```python
    from ray.tune.suggest.optuna import OptunaSearch
    import optuna

    space = {
        "a": optuna.distributions.UniformDistribution(6, 8),
        "b": optuna.distributions.LogUniformDistribution(1e-4, 1e-2),
    }

    optuna_search = OptunaSearch(
        space,
        points_to_evaluate=[{"a": 6.5, "b": 5e-4}, {"a": 7.5, "b": 1e-3}]
        evaluated_rewards=[0.89, 0.42]
        metric="loss",
        mode="min")

    tune.run(trainable, search_alg=optuna_search)
    ```

    '''
    def __init__(self, space: Dict[str, 'OptunaDistribution'] | List[Tuple] | Callable[[OptunaTrial], Dict[str, Any] | None] | None = None, metric: str | List[str] | None = None, mode: str | List[str] | None = None, points_to_evaluate: List[Dict] | None = None, sampler: BaseSampler | None = None, seed: int | None = None, evaluated_rewards: List | None = None) -> None: ...
    def set_search_properties(self, metric: str | None, mode: str | None, config: Dict, **spec) -> bool: ...
    def suggest(self, trial_id: str) -> Dict | None: ...
    def on_trial_result(self, trial_id: str, result: Dict): ...
    def on_trial_complete(self, trial_id: str, result: Dict | None = None, error: bool = False): ...
    def add_evaluated_point(self, parameters: Dict, value: float, error: bool = False, pruned: bool = False, intermediate_values: List[float] | None = None): ...
    def save(self, checkpoint_path: str): ...
    def restore(self, checkpoint_path: str): ...
    @staticmethod
    def convert_search_space(spec: Dict) -> Dict[str, Any]: ...
