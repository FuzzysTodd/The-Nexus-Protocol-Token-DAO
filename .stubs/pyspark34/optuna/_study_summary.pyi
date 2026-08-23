import datetime
from _typeshed import Incomplete
from optuna import logging as logging, trial as trial
from optuna._study_direction import StudyDirection as StudyDirection
from typing import Any, Dict, Sequence

class StudySummary:
    """Basic attributes and aggregated results of a :class:`~optuna.study.Study`.

    See also :func:`optuna.study.get_all_study_summaries`.

    Attributes:
        study_name:
            Name of the :class:`~optuna.study.Study`.
        direction:
            :class:`~optuna.study.StudyDirection` of the :class:`~optuna.study.Study`.

            .. note::
                This attribute is only available during single-objective optimization.
        directions:
            A sequence of :class:`~optuna.study.StudyDirection` objects.
        best_trial:
            :class:`FrozenTrial` with best objective value in the :class:`~optuna.study.Study`.
        user_attrs:
            Dictionary that contains the attributes of the :class:`~optuna.study.Study` set with
            :func:`optuna.study.Study.set_user_attr`.
        system_attrs:
            Dictionary that contains the attributes of the :class:`~optuna.study.Study` internally
            set by Optuna.
        n_trials:
            The number of trials ran in the :class:`~optuna.study.Study`.
        datetime_start:
            Datetime where the :class:`~optuna.study.Study` started.

    """
    study_name: Incomplete
    best_trial: Incomplete
    user_attrs: Incomplete
    system_attrs: Incomplete
    n_trials: Incomplete
    datetime_start: Incomplete
    def __init__(self, study_name: str, direction: StudyDirection | None, best_trial: trial.FrozenTrial | None, user_attrs: Dict[str, Any], system_attrs: Dict[str, Any], n_trials: int, datetime_start: datetime.datetime | None, study_id: int, *, directions: Sequence[StudyDirection] | None = None) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    @property
    def direction(self) -> StudyDirection: ...
    @property
    def directions(self) -> Sequence[StudyDirection]: ...
