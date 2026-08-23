from optuna import distributions as distributions
from optuna.distributions import BaseDistribution as BaseDistribution
from optuna.samplers import BaseSampler as BaseSampler
from optuna.study import Study as Study
from optuna.trial import FrozenTrial as FrozenTrial
from typing import Any, Dict

class RandomSampler(BaseSampler):
    '''Sampler using random sampling.

    This sampler is based on *independent sampling*.
    See also :class:`~optuna.samplers.BaseSampler` for more details of \'independent sampling\'.

    Example:

        .. testcode::

            import optuna
            from optuna.samplers import RandomSampler


            def objective(trial):
                x = trial.suggest_float("x", -5, 5)
                return x ** 2


            study = optuna.create_study(sampler=RandomSampler())
            study.optimize(objective, n_trials=10)

    Args:
        seed: Seed for random number generator.
    '''
    def __init__(self, seed: int | None = None) -> None: ...
    def reseed_rng(self) -> None: ...
    def infer_relative_search_space(self, study: Study, trial: FrozenTrial) -> Dict[str, BaseDistribution]: ...
    def sample_relative(self, study: Study, trial: FrozenTrial, search_space: Dict[str, BaseDistribution]) -> Dict[str, Any]: ...
    def sample_independent(self, study: Study, trial: FrozenTrial, param_name: str, param_distribution: distributions.BaseDistribution) -> Any: ...
