import numpy as np
from optuna import multi_objective as multi_objective
from optuna._deprecated import deprecated as deprecated
from optuna.distributions import BaseDistribution as BaseDistribution
from optuna.exceptions import ExperimentalWarning as ExperimentalWarning
from optuna.multi_objective.samplers import BaseMultiObjectiveSampler as BaseMultiObjectiveSampler
from optuna.pruners import NopPruner as NopPruner
from optuna.samplers import MOTPESampler as MOTPESampler
from optuna.samplers._tpe.multi_objective_sampler import default_gamma as default_gamma
from optuna.study import create_study as create_study
from optuna.trial import FrozenTrial as FrozenTrial, create_trial as create_trial
from typing import Any, Callable, Dict

class MOTPEMultiObjectiveSampler(BaseMultiObjectiveSampler):
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
            num_variables = 9
            n_startup_trials = 11 * num_variables - 1


            def objective(trial):
                x = []
                for i in range(1, num_variables + 1):
                    x.append(trial.suggest_float(f"x{i}", 0.0, 2.0 * i))
                return x


            sampler = optuna.multi_objective.samplers.MOTPEMultiObjectiveSampler(
                n_startup_trials=n_startup_trials, n_ehvi_candidates=24, seed=seed
            )
            study = optuna.multi_objective.create_study(
                ["minimize"] * num_variables, sampler=sampler
            )
            study.optimize(objective, n_trials=250)
    '''
    def __init__(self, consider_prior: bool = True, prior_weight: float = 1.0, consider_magic_clip: bool = True, consider_endpoints: bool = True, n_startup_trials: int = 10, n_ehvi_candidates: int = 24, gamma: Callable[[int], int] = ..., weights_above: Callable[[int], np.ndarray] = ..., seed: int | None = None) -> None: ...
    def reseed_rng(self) -> None: ...
    def infer_relative_search_space(self, study: multi_objective.study.MultiObjectiveStudy, trial: multi_objective.trial.FrozenMultiObjectiveTrial) -> Dict[str, BaseDistribution]: ...
    def sample_relative(self, study: multi_objective.study.MultiObjectiveStudy, trial: multi_objective.trial.FrozenMultiObjectiveTrial, search_space: Dict[str, BaseDistribution]) -> Dict[str, Any]: ...
    def sample_independent(self, study: multi_objective.study.MultiObjectiveStudy, trial: multi_objective.trial.FrozenMultiObjectiveTrial, param_name: str, param_distribution: BaseDistribution) -> Any: ...
