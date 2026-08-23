from optuna import multi_objective as multi_objective
from optuna.distributions import BaseDistribution as BaseDistribution
from optuna.samplers import BaseSampler as BaseSampler
from optuna.study import Study as Study
from optuna.trial import FrozenTrial as FrozenTrial
from typing import Any, Dict

class _MultiObjectiveSamplerAdapter(BaseSampler):
    """Adapter for to :class:`~optuna.multi_objective.samplers.BaseMultiObjectiveSampler`.

    This class implements the :class:`~optuna.samplers.BaseSampler` interface.
    When a method is invoked, the handling will be delegated to the given
    :class:`~optuna.multi_objective.samplers.BaseMultiObjectiveSampler` instance.
    """
    def __init__(self, mo_sampler: multi_objective.samplers.BaseMultiObjectiveSampler) -> None: ...
    def infer_relative_search_space(self, study: Study, trial: FrozenTrial) -> Dict[str, BaseDistribution]: ...
    def sample_relative(self, study: Study, trial: FrozenTrial, search_space: Dict[str, BaseDistribution]) -> Dict[str, Any]: ...
    def sample_independent(self, study: Study, trial: FrozenTrial, param_name: str, param_distribution: BaseDistribution) -> Any: ...
