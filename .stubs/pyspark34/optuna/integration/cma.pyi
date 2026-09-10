from optuna import distributions as distributions, logging as logging
from optuna._deprecated import deprecated as deprecated
from optuna._imports import try_import as try_import
from optuna.distributions import BaseDistribution as BaseDistribution, CategoricalDistribution as CategoricalDistribution, DiscreteUniformDistribution as DiscreteUniformDistribution, IntLogUniformDistribution as IntLogUniformDistribution, IntUniformDistribution as IntUniformDistribution, LogUniformDistribution as LogUniformDistribution, UniformDistribution as UniformDistribution
from optuna.samplers import BaseSampler as BaseSampler
from optuna.study import Study as Study, StudyDirection as StudyDirection
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from typing import Any, Dict, List, Sequence

class PyCmaSampler(BaseSampler):
    '''A Sampler using cma library as the backend.

    Example:

        Optimize a simple quadratic function by using :class:`~optuna.integration.PyCmaSampler`.

        .. testcode::

            import optuna


            def objective(trial):
                x = trial.suggest_float("x", -1, 1)
                y = trial.suggest_int("y", -1, 1)
                return x ** 2 + y


            sampler = optuna.integration.PyCmaSampler()
            study = optuna.create_study(sampler=sampler)
            study.optimize(objective, n_trials=20)

    Note that parallel execution of trials may affect the optimization performance of CMA-ES,
    especially if the number of trials running in parallel exceeds the population size.

    .. note::
        :class:`~optuna.integration.CmaEsSampler` is deprecated and renamed to
        :class:`~optuna.integration.PyCmaSampler` in v2.0.0. Please use
        :class:`~optuna.integration.PyCmaSampler` instead of
        :class:`~optuna.integration.CmaEsSampler`.

    Args:

        x0:
            A dictionary of an initial parameter values for CMA-ES. By default, the mean of ``low``
            and ``high`` for each distribution is used.
            Please refer to cma.CMAEvolutionStrategy_ for further details of ``x0``.

        sigma0:
            Initial standard deviation of CMA-ES. By default, ``sigma0`` is set to
            ``min_range / 6``, where ``min_range`` denotes the minimum range of the distributions
            in the search space. If distribution is categorical, ``min_range`` is
            ``len(choices) - 1``.
            Please refer to cma.CMAEvolutionStrategy_ for further details of ``sigma0``.

        cma_stds:
            A dictionary of multipliers of sigma0 for each parameters. The default value is 1.0.
            Please refer to cma.CMAEvolutionStrategy_ for further details of ``cma_stds``.

        seed:
            A random seed for CMA-ES.

        cma_opts:
            Options passed to the constructor of cma.CMAEvolutionStrategy_ class.

            Note that ``BoundaryHandler``, ``bounds``, ``CMA_stds`` and ``seed`` arguments in
            ``cma_opts`` will be ignored because it is added by
            :class:`~optuna.integration.PyCmaSampler` automatically.

        n_startup_trials:
            The independent sampling is used instead of the CMA-ES algorithm until the given number
            of trials finish in the same study.

        independent_sampler:
            A :class:`~optuna.samplers.BaseSampler` instance that is used for independent
            sampling. The parameters not contained in the relative search space are sampled
            by this sampler.
            The search space for :class:`~optuna.integration.PyCmaSampler` is determined by
            :func:`~optuna.samplers.intersection_search_space()`.

            If :obj:`None` is specified, :class:`~optuna.samplers.RandomSampler` is used
            as the default.

            .. seealso::
                :class:`optuna.samplers` module provides built-in independent samplers
                such as :class:`~optuna.samplers.RandomSampler` and
                :class:`~optuna.samplers.TPESampler`.

        warn_independent_sampling:
            If this is :obj:`True`, a warning message is emitted when
            the value of a parameter is sampled by using an independent sampler.

            Note that the parameters of the first trial in a study are always sampled
            via an independent sampler, so no warning messages are emitted in this case.

    .. _cma.CMAEvolutionStrategy: http://cma.gforge.inria.fr/apidocs-pycma/    cma.evolution_strategy.CMAEvolutionStrategy.html
    '''
    def __init__(self, x0: Dict[str, Any] | None = None, sigma0: float | None = None, cma_stds: Dict[str, float] | None = None, seed: int | None = None, cma_opts: Dict[str, Any] | None = None, n_startup_trials: int = 1, independent_sampler: BaseSampler | None = None, warn_independent_sampling: bool = True) -> None: ...
    def reseed_rng(self) -> None: ...
    def infer_relative_search_space(self, study: Study, trial: FrozenTrial) -> Dict[str, BaseDistribution]: ...
    def sample_independent(self, study: Study, trial: FrozenTrial, param_name: str, param_distribution: BaseDistribution) -> float: ...
    def sample_relative(self, study: Study, trial: FrozenTrial, search_space: Dict[str, BaseDistribution]) -> Dict[str, float]: ...
    def after_trial(self, study: Study, trial: FrozenTrial, state: TrialState, values: Sequence[float] | None) -> None: ...

class _Optimizer:
    def __init__(self, search_space: Dict[str, BaseDistribution], x0: Dict[str, Any], sigma0: float, cma_stds: Dict[str, float] | None, cma_opts: Dict[str, Any]) -> None: ...
    def tell(self, trials: List[FrozenTrial], study_direction: StudyDirection) -> int: ...
    def ask(self, trials: List[FrozenTrial], last_told_trial_number: int) -> Dict[str, Any]: ...

class CmaEsSampler(PyCmaSampler):
    """Wrapper class of PyCmaSampler for backward compatibility."""
    def __init__(self, x0: Dict[str, Any] | None = None, sigma0: float | None = None, cma_stds: Dict[str, float] | None = None, seed: int | None = None, cma_opts: Dict[str, Any] | None = None, n_startup_trials: int = 1, independent_sampler: BaseSampler | None = None, warn_independent_sampling: bool = True) -> None: ...
