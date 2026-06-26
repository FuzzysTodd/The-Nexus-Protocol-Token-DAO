from optuna import multi_objective as multi_objective
from optuna._deprecated import deprecated as deprecated
from optuna.distributions import BaseDistribution as BaseDistribution
from optuna.multi_objective.samplers import BaseMultiObjectiveSampler as BaseMultiObjectiveSampler
from typing import Any, Dict

class RandomMultiObjectiveSampler(BaseMultiObjectiveSampler):
    '''Multi-objective sampler using random sampling.

    This sampler is based on *independent sampling*.
    See also :class:`~optuna.multi_objective.samplers.BaseMultiObjectiveSampler`
    for more details of \'independent sampling\'.

    Example:

        .. testcode::

            import optuna
            from optuna.multi_objective.samplers import RandomMultiObjectiveSampler


            def objective(trial):
                x = trial.suggest_float("x", -5, 5)
                y = trial.suggest_float("y", -5, 5)
                return x ** 2, y + 10


            study = optuna.multi_objective.create_study(
                ["minimize", "minimize"], sampler=RandomMultiObjectiveSampler()
            )
            study.optimize(objective, n_trials=10)

        Args:
            seed: Seed for random number generator.
    '''
    def __init__(self, seed: int | None = None) -> None: ...
    def reseed_rng(self) -> None: ...
    def infer_relative_search_space(self, study: multi_objective.study.MultiObjectiveStudy, trial: multi_objective.trial.FrozenMultiObjectiveTrial) -> Dict[str, BaseDistribution]: ...
    def sample_relative(self, study: multi_objective.study.MultiObjectiveStudy, trial: multi_objective.trial.FrozenMultiObjectiveTrial, search_space: Dict[str, BaseDistribution]) -> Dict[str, Any]: ...
    def sample_independent(self, study: multi_objective.study.MultiObjectiveStudy, trial: multi_objective.trial.FrozenMultiObjectiveTrial, param_name: str, param_distribution: BaseDistribution) -> Any: ...
