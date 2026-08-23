from optuna.distributions import BaseDistribution as BaseDistribution
from optuna.logging import get_logger as get_logger
from optuna.samplers import BaseSampler as BaseSampler
from optuna.study import Study as Study
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from typing import Any, Dict, List, Mapping, Sequence

GridValueType = str | float | int | bool | None
SortableParamValueSequenceType = List[str] | List[float] | List[int] | List[bool]

class GridSampler(BaseSampler):
    '''Sampler using grid search.

    With :class:`~optuna.samplers.GridSampler`, the trials suggest all combinations of parameters
    in the given search space during the study.

    Example:

        .. testcode::

            import optuna


            def objective(trial):
                x = trial.suggest_float("x", -100, 100)
                y = trial.suggest_int("y", -100, 100)
                return x ** 2 + y ** 2


            search_space = {"x": [-50, 0, 50], "y": [-99, 0, 99]}
            study = optuna.create_study(sampler=optuna.samplers.GridSampler(search_space))
            study.optimize(objective)

    Note:

        :class:`~optuna.samplers.GridSampler` automatically stops the optimization if all
        combinations in the passed ``search_space`` have already been evaluated, internally
        invoking the :func:`~optuna.study.Study.stop` method.

    Note:

        :class:`~optuna.samplers.GridSampler` does not take care of a parameter\'s quantization
        specified by discrete suggest methods but just samples one of values specified in the
        search space. E.g., in the following code snippet, either of ``-0.5`` or ``0.5`` is
        sampled as ``x`` instead of an integer point.

        .. testcode::

            import optuna


            def objective(trial):
                # The following suggest method specifies integer points between -5 and 5.
                x = trial.suggest_float("x", -5, 5, step=1)
                return x ** 2


            # Non-int points are specified in the grid.
            search_space = {"x": [-0.5, 0.5]}
            study = optuna.create_study(sampler=optuna.samplers.GridSampler(search_space))
            study.optimize(objective, n_trials=2)

    Note:
        A parameter configuration in the grid is not considered finished until its trial is
        finished. Therefore, during distributed optimization where trials run concurrently,
        different workers will occasionally suggest the same parameter configuration.
        The total number of actual trials may therefore exceed the size of the grid.

    Note:
        The grid is randomly shuffled and the order in which parameter configurations are
        suggested may vary. This is to reduce duplicate suggestions during distributed
        optimization.

    Args:
        search_space:
            A dictionary whose key and value are a parameter name and the corresponding candidates
            of values, respectively.
    '''
    def __init__(self, search_space: Mapping[str, Sequence[GridValueType]]) -> None: ...
    def infer_relative_search_space(self, study: Study, trial: FrozenTrial) -> Dict[str, BaseDistribution]: ...
    def sample_relative(self, study: Study, trial: FrozenTrial, search_space: Dict[str, BaseDistribution]) -> Dict[str, Any]: ...
    def sample_independent(self, study: Study, trial: FrozenTrial, param_name: str, param_distribution: BaseDistribution) -> Any: ...
    def after_trial(self, study: Study, trial: FrozenTrial, state: TrialState, values: Sequence[float] | None) -> None: ...
