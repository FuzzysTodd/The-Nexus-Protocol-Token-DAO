from _typeshed import Incomplete
from chainermn.communicators.communicator_base import CommunicatorBase as CommunicatorBase
from datetime import datetime
from optuna import TrialPruned as TrialPruned
from optuna._imports import try_import as try_import
from optuna.distributions import BaseDistribution as BaseDistribution, CategoricalChoiceType as CategoricalChoiceType
from optuna.storages import InMemoryStorage as InMemoryStorage, RDBStorage as RDBStorage
from optuna.study import Study as Study
from optuna.trial import BaseTrial as BaseTrial, Trial as Trial
from typing import Any, Callable, Dict, Sequence, Tuple, Type

class _ChainerMNObjectiveFunc:
    """A wrapper of an objective function to incorporate Optuna with ChainerMN.

    Note that this class is not supposed to be used by library users.

    Args:
        func:
            A callable that implements objective function.
        comm:
            A `ChainerMN communicator <https://docs.chainer.org/en/stable/chainermn/reference/
            index.html#communicators>`_.
    """
    comm: Incomplete
    objective: Incomplete
    def __init__(self, func: Callable[[ChainerMNTrial, CommunicatorBase], float], comm: CommunicatorBase) -> None: ...
    def __call__(self, trial: Trial) -> float: ...

class ChainerMNStudy:
    """A wrapper of :class:`~optuna.study.Study` to incorporate Optuna with ChainerMN.

    .. seealso::
        :class:`~optuna.integration.chainermn.ChainerMNStudy` provides the same interface as
        :class:`~optuna.study.Study`. Please refer to :class:`optuna.study.Study` for further
        details.

    See `the example <https://github.com/optuna/optuna-examples/blob/main/
    chainer/chainermn_integration.py>`__
    if you want to optimize an objective function that trains neural network
    written with ChainerMN.

    Args:
        study:
            A :class:`~optuna.study.Study` object.
        comm:
            A `ChainerMN communicator <https://docs.chainer.org/en/stable/chainermn/reference/
            index.html#communicators>`_.
    """
    def __init__(self, study: Study, comm: CommunicatorBase) -> None: ...
    def optimize(self, func: Callable[[ChainerMNTrial, CommunicatorBase], float], n_trials: int | None = None, timeout: float | None = None, catch: Tuple[Type[Exception], ...] = ()) -> None:
        """Optimize an objective function.

        This method provides the same interface as :func:`optuna.study.Study.optimize` except
        the absence of ``n_jobs`` argument.
        """
    def __getattr__(self, attr_name: str) -> Any: ...
    def __setattr__(self, attr_name: str, value: Any) -> None: ...

class ChainerMNTrial(BaseTrial):
    """A wrapper of :class:`~optuna.trial.Trial` to incorporate Optuna with ChainerMN.

    .. seealso::
        :class:`~optuna.integration.chainermn.ChainerMNTrial` provides the same interface as
        :class:`~optuna.trial.Trial`. Please refer to :class:`optuna.trial.Trial` for further
        details.

    Args:
        trial:
            A :class:`~optuna.trial.Trial` object if the caller is rank0 worker,
            :obj:`None` otherwise.
        comm:
            A `ChainerMN communicator <https://docs.chainer.org/en/stable/chainermn/reference/
            index.html#communicators>`_.
    """
    delegate: Incomplete
    comm: Incomplete
    def __init__(self, trial: Trial | None, comm: CommunicatorBase) -> None: ...
    def suggest_float(self, name: str, low: float, high: float, *, step: float | None = None, log: bool = False) -> float: ...
    def suggest_uniform(self, name: str, low: float, high: float) -> float: ...
    def suggest_loguniform(self, name: str, low: float, high: float) -> float: ...
    def suggest_discrete_uniform(self, name: str, low: float, high: float, q: float) -> float: ...
    def suggest_int(self, name: str, low: int, high: int, step: int = 1, log: bool = False) -> int: ...
    def suggest_categorical(self, name: str, choices: Sequence[CategoricalChoiceType]) -> Any: ...
    def report(self, value: float, step: int) -> None: ...
    def should_prune(self) -> bool: ...
    def set_user_attr(self, key: str, value: Any) -> None: ...
    def set_system_attr(self, key: str, value: Any) -> None: ...
    @property
    def number(self) -> int: ...
    @property
    def params(self) -> Dict[str, Any]: ...
    @property
    def distributions(self) -> Dict[str, BaseDistribution]: ...
    @property
    def user_attrs(self) -> Dict[str, Any]: ...
    @property
    def system_attrs(self) -> Dict[str, Any]: ...
    @property
    def datetime_start(self) -> datetime | None: ...
