from optuna import distributions as distributions, samplers as samplers
from optuna._imports import try_import as try_import
from optuna._study_direction import StudyDirection as StudyDirection
from optuna.exceptions import ExperimentalWarning as ExperimentalWarning
from optuna.samplers import BaseSampler as BaseSampler
from optuna.study import Study as Study
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from typing import Any, Dict, List, Sequence

class SkoptSampler(BaseSampler):
    '''Sampler using Scikit-Optimize as the backend.

    Example:

        Optimize a simple quadratic function by using :class:`~optuna.integration.SkoptSampler`.

        .. testcode::

            import optuna


            def objective(trial):
                x = trial.suggest_float("x", -10, 10)
                y = trial.suggest_int("y", 0, 10)
                return x ** 2 + y


            sampler = optuna.integration.SkoptSampler()
            study = optuna.create_study(sampler=sampler)
            study.optimize(objective, n_trials=10)

    Args:
        independent_sampler:
            A :class:`~optuna.samplers.BaseSampler` instance that is used for independent
            sampling. The parameters not contained in the relative search space are sampled
            by this sampler.
            The search space for :class:`~optuna.integration.SkoptSampler` is determined by
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

        skopt_kwargs:
            Keyword arguments passed to the constructor of
            `skopt.Optimizer <https://scikit-optimize.github.io/#skopt.Optimizer>`_
            class.

            Note that ``dimensions`` argument in ``skopt_kwargs`` will be ignored
            because it is added by :class:`~optuna.integration.SkoptSampler` automatically.

        n_startup_trials:
            The independent sampling is used until the given number of trials finish in the
            same study.

        consider_pruned_trials:
            If this is :obj:`True`, the PRUNED trials are considered for sampling.

            .. note::
                Added in v2.0.0 as an experimental feature. The interface may change in newer
                versions without prior notice. See
                https://github.com/optuna/optuna/releases/tag/v2.0.0.

            .. note::
                As the number of trials :math:`n` increases, each sampling takes longer and longer
                on a scale of :math:`O(n^3)`. And, if this is :obj:`True`, the number of trials
                will increase. So, it is suggested to set this flag :obj:`False` when each
                evaluation of the objective function is relatively faster than each sampling. On
                the other hand, it is suggested to set this flag :obj:`True` when each evaluation
                of the objective function is relatively slower than each sampling.
    '''
    def __init__(self, independent_sampler: BaseSampler | None = None, warn_independent_sampling: bool = True, skopt_kwargs: Dict[str, Any] | None = None, n_startup_trials: int = 1, *, consider_pruned_trials: bool = False) -> None: ...
    def reseed_rng(self) -> None: ...
    def infer_relative_search_space(self, study: Study, trial: FrozenTrial) -> Dict[str, distributions.BaseDistribution]: ...
    def sample_relative(self, study: Study, trial: FrozenTrial, search_space: Dict[str, distributions.BaseDistribution]) -> Dict[str, Any]: ...
    def sample_independent(self, study: Study, trial: FrozenTrial, param_name: str, param_distribution: distributions.BaseDistribution) -> Any: ...
    def after_trial(self, study: Study, trial: FrozenTrial, state: TrialState, values: Sequence[float] | None) -> None: ...

class _Optimizer:
    def __init__(self, search_space: Dict[str, distributions.BaseDistribution], skopt_kwargs: Dict[str, Any]) -> None: ...
    def tell(self, study: Study, complete_trials: List[FrozenTrial]) -> None: ...
    def ask(self) -> Dict[str, Any]: ...
