from optuna._experimental import experimental as experimental
from optuna.distributions import BaseDistribution as BaseDistribution
from optuna.samplers import BaseSampler as BaseSampler
from optuna.study import Study as Study
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from typing import Any, Dict, Sequence

class PartialFixedSampler(BaseSampler):
    '''Sampler with partially fixed parameters.

        .. versionadded:: 2.4.0

    Example:

         After several steps of optimization, you can fix the value of ``y`` and re-optimize it.

        .. testcode::

            import optuna


            def objective(trial):
                x = trial.suggest_float("x", -1, 1)
                y = trial.suggest_int("y", -1, 1)
                return x ** 2 + y


            study = optuna.create_study()
            study.optimize(objective, n_trials=10)

            best_params = study.best_params
            fixed_params = {"y": best_params["y"]}
            partial_sampler = optuna.samplers.PartialFixedSampler(fixed_params, study.sampler)

            study.sampler = partial_sampler
            study.optimize(objective, n_trials=10)

    Args:

        fixed_params:
            A dictionary of parameters to be fixed.

        base_sampler:
            A sampler which samples unfixed parameters.

    '''
    def __init__(self, fixed_params: Dict[str, Any], base_sampler: BaseSampler) -> None: ...
    def reseed_rng(self) -> None: ...
    def infer_relative_search_space(self, study: Study, trial: FrozenTrial) -> Dict[str, BaseDistribution]: ...
    def sample_relative(self, study: Study, trial: FrozenTrial, search_space: Dict[str, BaseDistribution]) -> Dict[str, Any]: ...
    def sample_independent(self, study: Study, trial: FrozenTrial, param_name: str, param_distribution: BaseDistribution) -> Any: ...
    def after_trial(self, study: Study, trial: FrozenTrial, state: TrialState, values: Sequence[float] | None) -> None: ...
