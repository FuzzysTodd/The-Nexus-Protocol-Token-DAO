from optuna._experimental import ExperimentalWarning as ExperimentalWarning
from optuna.distributions import BaseDistribution as BaseDistribution
from optuna.samplers._base import BaseSampler as BaseSampler
from optuna.samplers._random import RandomSampler as RandomSampler
from optuna.study import Study as Study, StudyDirection as StudyDirection
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from typing import Any, Callable, Dict, Sequence

class NSGAIISampler(BaseSampler):
    '''Multi-objective sampler using the NSGA-II algorithm.

    NSGA-II stands for "Nondominated Sorting Genetic Algorithm II",
    which is a well known, fast and elitist multi-objective genetic algorithm.

    For further information about NSGA-II, please refer to the following paper:

    - `A fast and elitist multiobjective genetic algorithm: NSGA-II
      <https://ieeexplore.ieee.org/document/996017>`_

    Args:
        population_size:
            Number of individuals (trials) in a generation.

        mutation_prob:
            Probability of mutating each parameter when creating a new individual.
            If :obj:`None` is specified, the value ``1.0 / len(parent_trial.params)`` is used
            where ``parent_trial`` is the parent trial of the target individual.

        crossover_prob:
            Probability that a crossover (parameters swapping between parents) will occur
            when creating a new individual.

        swapping_prob:
            Probability of swapping each parameter of the parents during crossover.

        seed:
            Seed for random number generator.

        constraints_func:
            An optional function that computes the objective constraints. It must take a
            :class:`~optuna.trial.FrozenTrial` and return the constraints. The return value must
            be a sequence of :obj:`float` s. A value strictly larger than 0 means that a
            constraints is violated. A value equal to or smaller than 0 is considered feasible.
            If constraints_func returns more than one value for a trial, that trial is considered
            feasible if and only if all values are equal to 0 or smaller.

            The constraints are handled by the constrained domination. A trial x is said to
            constrained-dominate a trial y, if any of the following conditions is true:

            1. Trial x is feasible and trial y is not.
            2. Trial x and y are both infeasible, but trial x has a smaller overall violation.
            3. Trial x and y are feasible and trial x dominates trial y.

            .. note::
                Added in v2.5.0 as an experimental feature. The interface may change in newer
                versions without prior notice. See
                https://github.com/optuna/optuna/releases/tag/v2.5.0.

    '''
    def __init__(self, *, population_size: int = 50, mutation_prob: float | None = None, crossover_prob: float = 0.9, swapping_prob: float = 0.5, seed: int | None = None, constraints_func: Callable[[FrozenTrial], Sequence[float]] | None = None) -> None: ...
    def reseed_rng(self) -> None: ...
    def infer_relative_search_space(self, study: Study, trial: FrozenTrial) -> Dict[str, BaseDistribution]: ...
    def sample_relative(self, study: Study, trial: FrozenTrial, search_space: Dict[str, BaseDistribution]) -> Dict[str, Any]: ...
    def sample_independent(self, study: Study, trial: FrozenTrial, param_name: str, param_distribution: BaseDistribution) -> Any: ...
    def after_trial(self, study: Study, trial: FrozenTrial, state: TrialState, values: Sequence[float] | None) -> None: ...
