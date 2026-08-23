import datetime
from optuna import distributions as distributions
from optuna.distributions import BaseDistribution as BaseDistribution, CategoricalChoiceType as CategoricalChoiceType, CategoricalDistribution as CategoricalDistribution, DiscreteUniformDistribution as DiscreteUniformDistribution, IntLogUniformDistribution as IntLogUniformDistribution, IntUniformDistribution as IntUniformDistribution, LogUniformDistribution as LogUniformDistribution, UniformDistribution as UniformDistribution
from optuna.trial._base import BaseTrial as BaseTrial
from typing import Any, Dict, Sequence

class FixedTrial(BaseTrial):
    '''A trial class which suggests a fixed value for each parameter.

    This object has the same methods as :class:`~optuna.trial.Trial`, and it suggests pre-defined
    parameter values. The parameter values can be determined at the construction of the
    :class:`~optuna.trial.FixedTrial` object. In contrast to :class:`~optuna.trial.Trial`,
    :class:`~optuna.trial.FixedTrial` does not depend on :class:`~optuna.study.Study`, and it is
    useful for deploying optimization results.

    Example:

        Evaluate an objective function with parameter values given by a user.

        .. testcode::

            import optuna


            def objective(trial):
                x = trial.suggest_uniform("x", -100, 100)
                y = trial.suggest_categorical("y", [-1, 0, 1])
                return x ** 2 + y


            assert objective(optuna.trial.FixedTrial({"x": 1, "y": 0})) == 1


    .. note::
        Please refer to :class:`~optuna.trial.Trial` for details of methods and properties.

    Args:
        params:
            A dictionary containing all parameters.
        number:
            A trial number. Defaults to ``0``.

    '''
    def __init__(self, params: Dict[str, Any], number: int = 0) -> None: ...
    def suggest_float(self, name: str, low: float, high: float, *, step: float | None = None, log: bool = False) -> float: ...
    def suggest_uniform(self, name: str, low: float, high: float) -> float: ...
    def suggest_loguniform(self, name: str, low: float, high: float) -> float: ...
    def suggest_discrete_uniform(self, name: str, low: float, high: float, q: float) -> float: ...
    def suggest_int(self, name: str, low: int, high: int, step: int = 1, log: bool = False) -> int: ...
    def suggest_categorical(self, name: str, choices: Sequence[CategoricalChoiceType]) -> CategoricalChoiceType: ...
    def report(self, value: float, step: int) -> None: ...
    def should_prune(self) -> bool: ...
    def set_user_attr(self, key: str, value: Any) -> None: ...
    def set_system_attr(self, key: str, value: Any) -> None: ...
    @property
    def params(self) -> Dict[str, Any]: ...
    @property
    def distributions(self) -> Dict[str, BaseDistribution]: ...
    @property
    def user_attrs(self) -> Dict[str, Any]: ...
    @property
    def system_attrs(self) -> Dict[str, Any]: ...
    @property
    def datetime_start(self) -> datetime.datetime | None: ...
    @property
    def number(self) -> int: ...
