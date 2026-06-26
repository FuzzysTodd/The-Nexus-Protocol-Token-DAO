from _typeshed import Incomplete
from datetime import datetime
from optuna import multi_objective as multi_objective
from optuna._deprecated import deprecated as deprecated
from optuna._study_direction import StudyDirection as StudyDirection
from optuna.distributions import BaseDistribution as BaseDistribution
from optuna.trial import FrozenTrial as FrozenTrial, Trial as Trial, TrialState as TrialState
from typing import Any, Dict, Sequence

CategoricalChoiceType = None | bool | int | float | str

class MultiObjectiveTrial:
    """A trial is a process of evaluating an objective function.

    This object is passed to an objective function and provides interfaces to get parameter
    suggestion, manage the trial's state, and set/get user-defined attributes of the trial.

    Note that the direct use of this constructor is not recommended.
    This object is seamlessly instantiated and passed to the objective function behind
    the :func:`optuna.multi_objective.study.MultiObjectiveStudy.optimize()` method;
    hence library users do not care about instantiation of this object.

    Args:
        trial:
            A :class:`~optuna.trial.Trial` object.
    """
    def __init__(self, trial: Trial) -> None: ...
    def suggest_float(self, name: str, low: float, high: float, *, step: float | None = None, log: bool = False) -> float:
        """Suggest a value for the floating point parameter.

        Please refer to the documentation of :func:`optuna.trial.Trial.suggest_float`
        for further details.
        """
    def suggest_uniform(self, name: str, low: float, high: float) -> float:
        """Suggest a value for the continuous parameter.

        Please refer to the documentation of :func:`optuna.trial.Trial.suggest_uniform`
        for further details.
        """
    def suggest_loguniform(self, name: str, low: float, high: float) -> float:
        """Suggest a value for the continuous parameter.

        Please refer to the documentation of :func:`optuna.trial.Trial.suggest_loguniform`
        for further details.
        """
    def suggest_discrete_uniform(self, name: str, low: float, high: float, q: float) -> float:
        """Suggest a value for the discrete parameter.

        Please refer to the documentation of :func:`optuna.trial.Trial.suggest_discrete_uniform`
        for further details.
        """
    def suggest_int(self, name: str, low: int, high: int, step: int = 1, log: bool = False) -> int:
        """Suggest a value for the integer parameter.

        Please refer to the documentation of :func:`optuna.trial.Trial.suggest_int`
        for further details.
        """
    def suggest_categorical(self, name: str, choices: Sequence[CategoricalChoiceType]) -> CategoricalChoiceType:
        """Suggest a value for the categorical parameter.

        Please refer to the documentation of :func:`optuna.trial.Trial.suggest_categorical`
        for further details.
        """
    def report(self, values: Sequence[float], step: int) -> None:
        """Report intermediate objective function values for a given step.

        The reported values are used by the pruners to determine whether this trial should be
        pruned.

        .. seealso::
            Please refer to :class:`~optuna.pruners.BasePruner`.

        .. note::
            The reported values are converted to ``float`` type by applying ``float()``
            function internally. Thus, it accepts all float-like types (e.g., ``numpy.float32``).
            If the conversion fails, a ``TypeError`` is raised.

        Args:
            values:
                Intermediate objective function values for a given step.
            step:
                Step of the trial (e.g., Epoch of neural network training).
        """
    def set_user_attr(self, key: str, value: Any) -> None:
        """Set user attributes to the trial.

        Please refer to the documentation of :func:`optuna.trial.Trial.set_user_attr`
        for further details.
        """
    def set_system_attr(self, key: str, value: Any) -> None:
        """Set system attributes to the trial.

        Please refer to the documentation of :func:`optuna.trial.Trial.set_system_attr`
        for further details.
        """
    @property
    def number(self) -> int:
        """Return trial's number which is consecutive and unique in a study.

        Returns:
            A trial number.
        """
    @property
    def params(self) -> Dict[str, Any]:
        """Return parameters to be optimized.

        Returns:
            A dictionary containing all parameters.
        """
    @property
    def distributions(self) -> Dict[str, BaseDistribution]:
        """Return distributions of parameters to be optimized.

        Returns:
            A dictionary containing all distributions.
        """
    @property
    def user_attrs(self) -> Dict[str, Any]:
        """Return user attributes.

        Returns:
            A dictionary containing all user attributes.
        """
    @property
    def system_attrs(self) -> Dict[str, Any]:
        """Return system attributes.

        Returns:
            A dictionary containing all system attributes.
        """
    @property
    def datetime_start(self) -> datetime | None:
        """Return start datetime.

        Returns:
            Datetime where the :class:`~optuna.trial.Trial` started.
        """

class FrozenMultiObjectiveTrial:
    """Status and results of a :class:`~optuna.multi_objective.trial.MultiObjectiveTrial`.

    Attributes:
        number:
            Unique and consecutive number of
            :class:`~optuna.multi_objective.trial.MultiObjectiveTrial` for each
            :class:`~optuna.multi_objective.study.MultiObjectiveStudy`.
            Note that this field uses zero-based numbering.
        state:
            :class:`~optuna.trial.TrialState` of the
            :class:`~optuna.multi_objective.trial.MultiObjectiveTrial`.
        values:
            Objective values of the :class:`~optuna.multi_objective.trial.MultiObjectiveTrial`.
        datetime_start:
            Datetime where the :class:`~optuna.multi_objective.trial.MultiObjectiveTrial` started.
        datetime_complete:
            Datetime where the :class:`~optuna.multi_objective.trial.MultiObjectiveTrial` finished.
        params:
            Dictionary that contains suggested parameters.
        distributions:
            Dictionary that contains the distributions of :attr:`params`.
        user_attrs:
            Dictionary that contains the attributes of the
            :class:`~optuna.multi_objective.trial.MultiObjectiveTrial` set with
            :func:`optuna.multi_objective.trial.MultiObjectiveTrial.set_user_attr`.
        intermediate_values:
            Intermediate objective values set with
            :func:`optuna.multi_objective.trial.MultiObjectiveTrial.report`.
    """
    n_objectives: Incomplete
    values: Incomplete
    intermediate_values: Incomplete
    def __init__(self, n_objectives: int, trial: FrozenTrial) -> None: ...
    @property
    def number(self) -> int: ...
    @property
    def state(self) -> TrialState: ...
    @property
    def datetime_start(self) -> datetime | None: ...
    @property
    def datetime_complete(self) -> datetime | None: ...
    @property
    def params(self) -> Dict[str, Any]: ...
    @property
    def user_attrs(self) -> Dict[str, Any]: ...
    @property
    def system_attrs(self) -> Dict[str, Any]: ...
    @property
    def last_step(self) -> int | None: ...
    @property
    def distributions(self) -> Dict[str, BaseDistribution]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
