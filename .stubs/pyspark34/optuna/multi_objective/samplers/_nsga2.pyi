from optuna import multi_objective as multi_objective
from optuna._deprecated import deprecated as deprecated
from optuna.distributions import BaseDistribution as BaseDistribution
from optuna.multi_objective.samplers import BaseMultiObjectiveSampler as BaseMultiObjectiveSampler
from typing import Any, Dict

class NSGAIIMultiObjectiveSampler(BaseMultiObjectiveSampler):
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

    '''
    def __init__(self, population_size: int = 50, mutation_prob: float | None = None, crossover_prob: float = 0.9, swapping_prob: float = 0.5, seed: int | None = None) -> None: ...
    def reseed_rng(self) -> None: ...
    def infer_relative_search_space(self, study: multi_objective.study.MultiObjectiveStudy, trial: multi_objective.trial.FrozenMultiObjectiveTrial) -> Dict[str, BaseDistribution]: ...
    def sample_relative(self, study: multi_objective.study.MultiObjectiveStudy, trial: multi_objective.trial.FrozenMultiObjectiveTrial, search_space: Dict[str, BaseDistribution]) -> Dict[str, Any]: ...
    def sample_independent(self, study: multi_objective.study.MultiObjectiveStudy, trial: multi_objective.trial.FrozenMultiObjectiveTrial, param_name: str, param_distribution: BaseDistribution) -> Any: ...
