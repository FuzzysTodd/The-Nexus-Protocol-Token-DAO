import numpy as np
import optuna
from optuna import distributions as distributions
from optuna._experimental import experimental as experimental
from optuna.distributions import BaseDistribution as BaseDistribution
from optuna.samplers._base import BaseSampler as BaseSampler
from optuna.samplers._random import RandomSampler as RandomSampler
from optuna.samplers._search_space import IntersectionSearchSpace as IntersectionSearchSpace
from optuna.study import StudyDirection as StudyDirection
from typing import Any, Callable, Dict, NamedTuple, Sequence

EPS: float

def default_gamma(x: int) -> int: ...

class _ParzenEstimatorParameters(NamedTuple('_ParzenEstimatorParameters', [('consider_prior', bool), ('prior_weight', float | None), ('consider_magic_clip', bool), ('consider_endpoints', bool), ('weights', Callable[[int], np.ndarray])])): ...

class _ParzenEstimator:
    def __init__(self, mus: np.ndarray, low: float, high: float, parameters: _ParzenEstimatorParameters) -> None: ...

class MOTPESampler(BaseSampler):
    '''Multi-objective sampler using the MOTPE algorithm.

    This sampler is a multiobjective version of :class:`~optuna.samplers.TPESampler`.

    For further information about MOTPE algorithm, please refer to the following paper:

    - `Multiobjective tree-structured parzen estimator for computationally expensive optimization
      problems <https://dl.acm.org/doi/abs/10.1145/3377930.3389817>`_

    Args:
        consider_prior:
            Enhance the stability of Parzen estimator by imposing a Gaussian prior when
            :obj:`True`. The prior is only effective if the sampling distribution is
            either :class:`~optuna.distributions.UniformDistribution`,
            :class:`~optuna.distributions.DiscreteUniformDistribution`,
            :class:`~optuna.distributions.LogUniformDistribution`,
            :class:`~optuna.distributions.IntUniformDistribution`,
            or :class:`~optuna.distributions.IntLogUniformDistribution`.
        prior_weight:
            The weight of the prior. This argument is used in
            :class:`~optuna.distributions.UniformDistribution`,
            :class:`~optuna.distributions.DiscreteUniformDistribution`,
            :class:`~optuna.distributions.LogUniformDistribution`,
            :class:`~optuna.distributions.IntUniformDistribution`,
            :class:`~optuna.distributions.IntLogUniformDistribution`, and
            :class:`~optuna.distributions.CategoricalDistribution`.
        consider_magic_clip:
            Enable a heuristic to limit the smallest variances of Gaussians used in
            the Parzen estimator.
        consider_endpoints:
            Take endpoints of domains into account when calculating variances of Gaussians
            in Parzen estimator. See the original paper for details on the heuristics
            to calculate the variances.
        n_startup_trials:
            The random sampling is used instead of the MOTPE algorithm until the given number
            of trials finish in the same study. 11 * number of variables - 1 is recommended in the
            original paper.
        n_ehvi_candidates:
            Number of candidate samples used to calculate the expected hypervolume improvement.
        gamma:
            A function that takes the number of finished trials and returns the number of trials to
            form a density function for samples with low grains. See the original paper for more
            details.
        weights_above:
            A function that takes the number of finished trials and returns a weight for them. As
            default, weights are automatically calculated by the MOTPE\'s default strategy.
        seed:
            Seed for random number generator.

    .. note::
        Initialization with Latin hypercube sampling may improve optimization performance.
        However, the current implementation only supports initialization with random sampling.

    Example:

        .. testcode::

            import optuna

            seed = 128
            num_variables = 2
            n_startup_trials = 11 * num_variables - 1


            def objective(trial):
                x = []
                for i in range(1, num_variables + 1):
                    x.append(trial.suggest_float(f"x{i}", 0.0, 2.0 * i))
                return x


            sampler = optuna.samplers.MOTPESampler(
                n_startup_trials=n_startup_trials, n_ehvi_candidates=24, seed=seed
            )
            study = optuna.create_study(directions=["minimize"] * num_variables, sampler=sampler)
            study.optimize(objective, n_trials=n_startup_trials + 10)
    '''
    def __init__(self, *, consider_prior: bool = True, prior_weight: float = 1.0, consider_magic_clip: bool = True, consider_endpoints: bool = True, n_startup_trials: int = 10, n_ehvi_candidates: int = 24, gamma: Callable[[int], int] = ..., weights_above: Callable[[int], np.ndarray] = ..., seed: int | None = None) -> None: ...
    def reseed_rng(self) -> None: ...
    def infer_relative_search_space(self, study: optuna.study.Study, trial: optuna.trial.FrozenTrial) -> Dict[str, BaseDistribution]: ...
    def sample_relative(self, study: optuna.study.Study, trial: optuna.trial.FrozenTrial, search_space: Dict[str, BaseDistribution]) -> Dict[str, Any]: ...
    def sample_independent(self, study: optuna.study.Study, trial: optuna.trial.FrozenTrial, param_name: str, param_distribution: BaseDistribution) -> Any: ...
    def after_trial(self, study: optuna.study.Study, trial: optuna.trial.FrozenTrial, state: optuna.trial.TrialState, values: Sequence[float] | None) -> None: ...
