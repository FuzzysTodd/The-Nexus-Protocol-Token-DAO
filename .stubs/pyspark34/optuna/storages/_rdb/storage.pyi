import optuna
from _typeshed import Incomplete
from optuna import distributions as distributions, version as version
from optuna._study_direction import StudyDirection as StudyDirection
from optuna._study_summary import StudySummary as StudySummary
from optuna.storages._base import BaseStorage as BaseStorage, DEFAULT_STUDY_NAME_PREFIX as DEFAULT_STUDY_NAME_PREFIX
from optuna.storages._rdb import models as models
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState
from sqlalchemy import orm
from sqlalchemy.engine import Engine as Engine
from typing import Any, Callable, Dict, List, Sequence, Tuple

class RDBStorage(BaseStorage):
    '''Storage class for RDB backend.

    Note that library users can instantiate this class, but the attributes
    provided by this class are not supposed to be directly accessed by them.

    Example:

        Create an :class:`~optuna.storages.RDBStorage` instance with customized
        ``pool_size`` and ``timeout`` settings.

        .. testcode::

            import optuna


            def objective(trial):
                x = trial.suggest_float("x", -100, 100)
                return x ** 2


            storage = optuna.storages.RDBStorage(
                url="sqlite:///:memory:",
                engine_kwargs={"pool_size": 20, "connect_args": {"timeout": 10}},
            )

            study = optuna.create_study(storage=storage)
            study.optimize(objective, n_trials=10)

    Args:
        url: URL of the storage.
        engine_kwargs:
            A dictionary of keyword arguments that is passed to
            `sqlalchemy.engine.create_engine`_ function.
        skip_compatibility_check:
            Flag to skip schema compatibility check if set to True.
        heartbeat_interval:
            Interval to record the heartbeat. It is recorded every ``interval`` seconds.
        grace_period:
            Grace period before a running trial is failed from the last heartbeat.
            If it is :obj:`None`, the grace period will be `2 * heartbeat_interval`.
        failed_trial_callback:
            A callback function that is invoked after failing each stale trial.
            The function must accept two parameters with the following types in this order:
            :class:`~optuna.study.Study` and :class:`~optuna.FrozenTrial`.

            .. note::
                The procedure to fail existing stale trials is called just before asking the
                study for a new trial.

    .. _sqlalchemy.engine.create_engine:
        https://docs.sqlalchemy.org/en/latest/core/engines.html#sqlalchemy.create_engine

    .. note::
        If you use MySQL, `pool_pre_ping`_ will be set to :obj:`True` by default to prevent
        connection timeout. You can turn it off with ``engine_kwargs[\'pool_pre_ping\']=False``, but
        it is recommended to keep the setting if execution time of your objective function is
        longer than the `wait_timeout` of your MySQL configuration.

    .. _pool_pre_ping:
        https://docs.sqlalchemy.org/en/13/core/engines.html#sqlalchemy.create_engine.params.
        pool_pre_ping

    Raises:
        :exc:`ValueError`:
            If the given `heartbeat_interval` or `grace_period` is not a positive integer.
        :exc:`RuntimeError`:
            If the a process that was failed by heartbeat but was actually running.
    '''
    engine_kwargs: Incomplete
    url: Incomplete
    skip_compatibility_check: Incomplete
    heartbeat_interval: Incomplete
    grace_period: Incomplete
    failed_trial_callback: Incomplete
    engine: Incomplete
    scoped_session: Incomplete
    def __init__(self, url: str, engine_kwargs: Dict[str, Any] | None = None, skip_compatibility_check: bool = False, *, heartbeat_interval: int | None = None, grace_period: int | None = None, failed_trial_callback: Callable[[optuna.Study, FrozenTrial], None] | None = None) -> None: ...
    def create_new_study(self, study_name: str | None = None) -> int: ...
    def delete_study(self, study_id: int) -> None: ...
    def set_study_directions(self, study_id: int, directions: Sequence[StudyDirection]) -> None: ...
    def set_study_user_attr(self, study_id: int, key: str, value: Any) -> None: ...
    def set_study_system_attr(self, study_id: int, key: str, value: Any) -> None: ...
    def get_study_id_from_name(self, study_name: str) -> int: ...
    def get_study_id_from_trial_id(self, trial_id: int) -> int: ...
    def get_study_name_from_id(self, study_id: int) -> str: ...
    def get_study_directions(self, study_id: int) -> List[StudyDirection]: ...
    def get_study_user_attrs(self, study_id: int) -> Dict[str, Any]: ...
    def get_study_system_attrs(self, study_id: int) -> Dict[str, Any]: ...
    def get_trial_user_attrs(self, trial_id: int) -> Dict[str, Any]: ...
    def get_trial_system_attrs(self, trial_id: int) -> Dict[str, Any]: ...
    def get_all_study_summaries(self) -> List[StudySummary]: ...
    def create_new_trial(self, study_id: int, template_trial: FrozenTrial | None = None) -> int: ...
    def set_trial_state(self, trial_id: int, state: TrialState) -> bool: ...
    def set_trial_param(self, trial_id: int, param_name: str, param_value_internal: float, distribution: distributions.BaseDistribution) -> None: ...
    def get_trial_param(self, trial_id: int, param_name: str) -> float: ...
    def set_trial_values(self, trial_id: int, values: Sequence[float]) -> None: ...
    def set_trial_intermediate_value(self, trial_id: int, step: int, intermediate_value: float) -> None: ...
    def set_trial_user_attr(self, trial_id: int, key: str, value: Any) -> None: ...
    def set_trial_system_attr(self, trial_id: int, key: str, value: Any) -> None: ...
    def get_trial_id_from_study_id_trial_number(self, study_id: int, trial_number: int) -> int: ...
    def get_trial_number_from_id(self, trial_id: int) -> int: ...
    def get_trial(self, trial_id: int) -> FrozenTrial: ...
    def get_all_trials(self, study_id: int, deepcopy: bool = True, states: Tuple[TrialState, ...] | None = None) -> List[FrozenTrial]: ...
    def get_best_trial(self, study_id: int) -> FrozenTrial: ...
    def read_trials_from_remote_storage(self, study_id: int) -> None: ...
    def remove_session(self) -> None:
        """Removes the current session.

        A session is stored in SQLAlchemy's ThreadLocalRegistry for each thread. This method
        closes and removes the session which is associated to the current thread. Particularly,
        under multi-thread use cases, it is important to call this method *from each thread*.
        Otherwise, all sessions and their associated DB connections are destructed by a thread
        that occasionally invoked the garbage collector. By default, it is not allowed to touch
        a SQLite connection from threads other than the thread that created the connection.
        Therefore, we need to explicitly close the connection from each thread.

        """
    def upgrade(self) -> None:
        """Upgrade the storage schema."""
    def get_current_version(self) -> str:
        """Return the schema version currently used by this storage."""
    def get_head_version(self) -> str:
        """Return the latest schema version."""
    def get_all_versions(self) -> List[str]:
        """Return the schema version list."""
    def record_heartbeat(self, trial_id: int) -> None: ...
    def fail_stale_trials(self, study_id: int) -> List[int]: ...
    def get_heartbeat_interval(self) -> int | None: ...
    def get_failed_trial_callback(self) -> Callable[[optuna.Study, FrozenTrial], None] | None: ...

class _VersionManager:
    url: Incomplete
    engine: Incomplete
    scoped_session: Incomplete
    def __init__(self, url: str, engine: Engine, scoped_session: orm.scoped_session) -> None: ...
    def check_table_schema_compatibility(self) -> None: ...
    def get_current_version(self) -> str: ...
    def get_head_version(self) -> str: ...
    def get_all_versions(self) -> List[str]: ...
    def upgrade(self) -> None: ...

def escape_alembic_config_value(value: str) -> str: ...
