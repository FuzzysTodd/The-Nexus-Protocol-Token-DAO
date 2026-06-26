import datetime
from _typeshed import Incomplete
from optuna import distributions as distributions, logging as logging
from optuna._experimental import experimental as experimental
from optuna.distributions import BaseDistribution as BaseDistribution, CategoricalDistribution as CategoricalDistribution, DiscreteUniformDistribution as DiscreteUniformDistribution, IntLogUniformDistribution as IntLogUniformDistribution, IntUniformDistribution as IntUniformDistribution, LogUniformDistribution as LogUniformDistribution, UniformDistribution as UniformDistribution
from optuna.trial._base import BaseTrial as BaseTrial
from optuna.trial._state import TrialState as TrialState
from typing import Any, Dict, Sequence

CategoricalChoiceType = None | bool | int | float | str

class FrozenTrial(BaseTrial):
    '''Status and results of a :class:`~optuna.trial.Trial`.

    This object has the same methods as :class:`~optuna.trial.Trial`, and it suggests best
    parameter values among performed trials. In contrast to :class:`~optuna.trial.Trial`,
    :class:`~optuna.trial.FrozenTrial` does not depend on :class:`~optuna.study.Study`, and it is
    useful for deploying optimization results.

    Example:

        Re-evaluate an objective function with parameter values optimized study.

        .. testcode::

            import optuna


            def objective(trial):
                x = trial.suggest_uniform("x", -1, 1)
                return x ** 2


            study = optuna.create_study()
            study.optimize(objective, n_trials=3)

            assert objective(study.best_trial) == study.best_value

    .. note::
        Attributes are set in :func:`optuna.Study.optimize`,
        but several attributes can be updated after the optimization.
        That means such attributes are overwritten by the re-evaluation
        if your objective updates attributes of :class:`~optuna.trial.Trial`.


        Example:

            Overwritten attributes.

            .. testcode::

                import copy
                import datetime

                import optuna


                def objective(trial):
                    x = trial.suggest_uniform("x", -1, 1)

                    # this user attribute always differs
                    trial.set_user_attr("evaluation time", datetime.datetime.now())

                    return x ** 2


                study = optuna.create_study()
                study.optimize(objective, n_trials=3)

                best_trial = study.best_trial
                best_trial_copy = copy.deepcopy(best_trial)

                # re-evaluate
                objective(best_trial)

                # the user attribute is overwritten by re-evaluation
                assert best_trial.user_attrs != best_trial_copy.user_attrs

    .. note::
        Please refer to :class:`~optuna.trial.Trial` for details of methods and properties.


    Attributes:
        number:
            Unique and consecutive number of :class:`~optuna.trial.Trial` for each
            :class:`~optuna.study.Study`. Note that this field uses zero-based numbering.
        state:
            :class:`TrialState` of the :class:`~optuna.trial.Trial`.
        value:
            Objective value of the :class:`~optuna.trial.Trial`.
        values:
            Sequence of objective values of the :class:`~optuna.trial.Trial`.
            The length is greater than 1 if the problem is multi-objective optimization.
        datetime_start:
            Datetime where the :class:`~optuna.trial.Trial` started.
        datetime_complete:
            Datetime where the :class:`~optuna.trial.Trial` finished.
        params:
            Dictionary that contains suggested parameters.
        user_attrs:
            Dictionary that contains the attributes of the :class:`~optuna.trial.Trial` set with
            :func:`optuna.trial.Trial.set_user_attr`.
        intermediate_values:
            Intermediate objective values set with :func:`optuna.trial.Trial.report`.

    Raises:
        :exc:`ValueError`:
            If both ``value`` and ``values`` are specified.
    '''
    state: Incomplete
    datetime_complete: Incomplete
    intermediate_values: Incomplete
    def __init__(self, number: int, state: TrialState, value: float | None, datetime_start: datetime.datetime | None, datetime_complete: datetime.datetime | None, params: Dict[str, Any], distributions: Dict[str, BaseDistribution], user_attrs: Dict[str, Any], system_attrs: Dict[str, Any], intermediate_values: Dict[int, float], trial_id: int, *, values: Sequence[float] | None = None) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def suggest_float(self, name: str, low: float, high: float, *, step: float | None = None, log: bool = False) -> float: ...
    def suggest_uniform(self, name: str, low: float, high: float) -> float: ...
    def suggest_loguniform(self, name: str, low: float, high: float) -> float: ...
    def suggest_discrete_uniform(self, name: str, low: float, high: float, q: float) -> float: ...
    def suggest_int(self, name: str, low: int, high: int, step: int = 1, log: bool = False) -> int: ...
    def suggest_categorical(self, name: str, choices: Sequence[CategoricalChoiceType]) -> CategoricalChoiceType: ...
    def report(self, value: float, step: int) -> None:
        """Interface of report function.

        Since :class:`~optuna.trial.FrozenTrial` is not pruned,
        this report function does nothing.

        .. seealso::
            Please refer to :func:`~optuna.trial.FrozenTrial.should_prune`.

        Args:
            value:
                A value returned from the objective function.
            step:
                Step of the trial (e.g., Epoch of neural network training). Note that pruners
                assume that ``step`` starts at zero. For example,
                :class:`~optuna.pruners.MedianPruner` simply checks if ``step`` is less than
                ``n_warmup_steps`` as the warmup mechanism.
        """
    def should_prune(self) -> bool:
        """Suggest whether the trial should be pruned or not.

        The suggestion is always :obj:`False` regardless of a pruning algorithm.

        .. note::
            :class:`~optuna.trial.FrozenTrial` only samples one combination of parameters.

        Returns:
            :obj:`False`.
        """
    def set_user_attr(self, key: str, value: Any) -> None: ...
    def set_system_attr(self, key: str, value: Any) -> None: ...
    @property
    def number(self) -> int: ...
    @number.setter
    def number(self, value: int) -> None: ...
    @property
    def value(self) -> float | None: ...
    @value.setter
    def value(self, v: float | None) -> None: ...
    values: Incomplete
    @property
    def datetime_start(self) -> datetime.datetime | None: ...
    @datetime_start.setter
    def datetime_start(self, value: datetime.datetime | None) -> None: ...
    @property
    def params(self) -> Dict[str, Any]: ...
    @params.setter
    def params(self, params: Dict[str, Any]) -> None: ...
    @property
    def distributions(self) -> Dict[str, BaseDistribution]:
        """Dictionary that contains the distributions of :attr:`params`."""
    @distributions.setter
    def distributions(self, value: Dict[str, BaseDistribution]) -> None: ...
    @property
    def user_attrs(self) -> Dict[str, Any]: ...
    @user_attrs.setter
    def user_attrs(self, value: Dict[str, Any]) -> None: ...
    @property
    def system_attrs(self) -> Dict[str, Any]: ...
    @system_attrs.setter
    def system_attrs(self, value: Dict[str, Any]) -> None: ...
    @property
    def last_step(self) -> int | None:
        """Return the maximum step of `intermediate_values` in the trial.

        Returns:
            The maximum step of intermediates.
        """
    @property
    def duration(self) -> datetime.timedelta | None:
        """Return the elapsed time taken to complete the trial.

        Returns:
            The duration.
        """

def create_trial(*, state: TrialState = ..., value: float | None = None, values: Sequence[float] | None = None, params: Dict[str, Any] | None = None, distributions: Dict[str, BaseDistribution] | None = None, user_attrs: Dict[str, Any] | None = None, system_attrs: Dict[str, Any] | None = None, intermediate_values: Dict[int, float] | None = None) -> FrozenTrial:
    '''Create a new :class:`~optuna.trial.FrozenTrial`.

    Example:

        .. testcode::

            import optuna
            from optuna.distributions import CategoricalDistribution
            from optuna.distributions import UniformDistribution

            trial = optuna.trial.create_trial(
                params={"x": 1.0, "y": 0},
                distributions={
                    "x": UniformDistribution(0, 10),
                    "y": CategoricalDistribution([-1, 0, 1]),
                },
                value=5.0,
            )

            assert isinstance(trial, optuna.trial.FrozenTrial)
            assert trial.value == 5.0
            assert trial.params == {"x": 1.0, "y": 0}

    .. seealso::

        See :func:`~optuna.study.Study.add_trial` for how this function can be used to create a
        study from existing trials.

    .. note::

        Please note that this is a low-level API. In general, trials that are passed to objective
        functions are created inside :func:`~optuna.study.Study.optimize`.

    .. note::
        When ``state`` is ``TrialState.COMPLETE``, the following parameters are
        required:
        * ``params``
        * ``distributions``
        * ``value`` or ``values``

    Args:
        state:
            Trial state.
        value:
            Trial objective value. Must be specified if ``state`` is ``None``
            or :class:`TrialState.COMPLETE`.
        values:
            Sequence of the trial objective values. The length is greater than 1 if the problem is
            multi-objective optimization.
            Must be specified if ``state`` is ``None`` or :class:`TrialState.COMPLETE`.
        params:
            Dictionary with suggested parameters of the trial.
        distributions:
            Dictionary with parameter distributions of the trial.
        user_attrs:
            Dictionary with user attributes.
        system_attrs:
            Dictionary with system attributes. Should not have to be used for most users.
        intermediate_values:
            Dictionary with intermediate objective values of the trial.

    Returns:
        Created trial.

    Raises:
        :exc:`ValueError`:
            If both ``value`` and ``values`` are specified.
    '''
