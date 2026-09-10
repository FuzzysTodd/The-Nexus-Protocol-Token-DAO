from _typeshed import Incomplete
from optuna import logging as logging, multi_objective as multi_objective
from optuna._deprecated import deprecated as deprecated
from optuna._study_direction import StudyDirection as StudyDirection
from optuna.pruners import NopPruner as NopPruner
from optuna.storages import BaseStorage as BaseStorage
from optuna.study import Study as Study
from optuna.trial import FrozenTrial as FrozenTrial, Trial as Trial, TrialState as TrialState
from typing import Any, Dict, List, Tuple, Type

ObjectiveFuncType: Incomplete
CallbackFuncType: Incomplete

def create_study(directions: List[str], study_name: str | None = None, storage: str | BaseStorage | None = None, sampler: multi_objective.samplers.BaseMultiObjectiveSampler | None = None, load_if_exists: bool = False) -> multi_objective.study.MultiObjectiveStudy:
    '''Create a new :class:`~optuna.multi_objective.study.MultiObjectiveStudy`.

    Example:

        .. testcode::

            import optuna


            def objective(trial):
                # Binh and Korn function.
                x = trial.suggest_float("x", 0, 5)
                y = trial.suggest_float("y", 0, 3)

                v0 = 4 * x ** 2 + 4 * y ** 2
                v1 = (x - 5) ** 2 + (y - 5) ** 2
                return v0, v1


            study = optuna.multi_objective.create_study(["minimize", "minimize"])
            study.optimize(objective, n_trials=3)

    Args:
        directions:
            Optimization direction for each objective value.
            Set ``minimize`` for minimization and ``maximize`` for maximization.
        study_name:
            Study\'s name. If this argument is set to None, a unique name is generated
            automatically.
        storage:
            Database URL. If this argument is set to None, in-memory storage is used, and the
            :class:`~optuna.study.Study` will not be persistent.

            .. note::
                When a database URL is passed, Optuna internally uses `SQLAlchemy`_ to handle
                the database. Please refer to `SQLAlchemy\'s document`_ for further details.
                If you want to specify non-default options to `SQLAlchemy Engine`_, you can
                instantiate :class:`~optuna.storages.RDBStorage` with your desired options and
                pass it to the ``storage`` argument instead of a URL.

             .. _SQLAlchemy: https://www.sqlalchemy.org/
             .. _SQLAlchemy\'s document:
                 https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls
             .. _SQLAlchemy Engine: https://docs.sqlalchemy.org/en/latest/core/engines.html

        sampler:
            A sampler object that implements background algorithm for value suggestion.
            If :obj:`None` is specified,
            :class:`~optuna.multi_objective.samplers.NSGAIIMultiObjectiveSampler` is used
            as the default. See also :class:`~optuna.multi_objective.samplers`.
        load_if_exists:
            Flag to control the behavior to handle a conflict of study names.
            In the case where a study named ``study_name`` already exists in the ``storage``,
            a :class:`~optuna.exceptions.DuplicatedStudyError` is raised if ``load_if_exists`` is
            set to :obj:`False`.
            Otherwise, the creation of the study is skipped, and the existing one is returned.

    Returns:
        A :class:`~optuna.multi_objective.study.MultiObjectiveStudy` object.
    '''
def load_study(study_name: str, storage: str | BaseStorage, sampler: multi_objective.samplers.BaseMultiObjectiveSampler | None = None) -> multi_objective.study.MultiObjectiveStudy:
    '''Load the existing :class:`MultiObjectiveStudy` that has the specified name.

    Example:

        .. testsetup::

            import os

            if os.path.exists("example.db"):
                raise RuntimeError("\'example.db\' already exists. Please remove it.")

        .. testcode::

            import optuna


            def objective(trial):
                # Binh and Korn function.
                x = trial.suggest_float("x", 0, 5)
                y = trial.suggest_float("y", 0, 3)

                v0 = 4 * x ** 2 + 4 * y ** 2
                v1 = (x - 5) ** 2 + (y - 5) ** 2
                return v0, v1


            study = optuna.multi_objective.create_study(
                directions=["minimize", "minimize"],
                study_name="my_study",
                storage="sqlite:///example.db",
            )
            study.optimize(objective, n_trials=3)

            loaded_study = optuna.multi_objective.study.load_study(
                study_name="my_study", storage="sqlite:///example.db"
            )
            assert len(loaded_study.trials) == len(study.trials)

        .. testcleanup::

            os.remove("example.db")

    Args:
        study_name:
            Study\'s name. Each study has a unique name as an identifier.
        storage:
            Database URL such as ``sqlite:///example.db``. Please see also the documentation of
            :func:`~optuna.multi_objective.study.create_study` for further details.
        sampler:
            A sampler object that implements background algorithm for value suggestion.
            If :obj:`None` is specified,
            :class:`~optuna.multi_objective.samplers.RandomMultiObjectiveSampler` is used
            as the default. See also :class:`~optuna.multi_objective.samplers`.

    Returns:
        A :class:`~optuna.multi_objective.study.MultiObjectiveStudy` object.
    '''

class MultiObjectiveStudy:
    """A study corresponds to a multi-objective optimization task, i.e., a set of trials.

    This object provides interfaces to run a new
    :class:`~optuna.multi_objective.trial.Trial`, access trials'
    history, set/get user-defined attributes of the study itself.

    Note that the direct use of this constructor is not recommended.
    To create and load a study, please refer to the documentation of
    :func:`~optuna.multi_objective.study.create_study` and
    :func:`~optuna.multi_objective.study.load_study` respectively.
    """
    def __init__(self, study: Study) -> None: ...
    @property
    def n_objectives(self) -> int:
        """Return the number of objectives.

        Returns:
            Number of objectives.
        """
    @property
    def directions(self) -> List[StudyDirection]:
        """Return the optimization direction list.

        Returns:
            A list that contains the optimization direction for each objective value.
        """
    @property
    def sampler(self) -> multi_objective.samplers.BaseMultiObjectiveSampler:
        """Return the sampler.

        Returns:
            A :class:`~multi_objective.samplers.BaseMultiObjectiveSampler` object.
        """
    def optimize(self, objective: ObjectiveFuncType, timeout: int | None = None, n_trials: int | None = None, n_jobs: int = 1, catch: Tuple[Type[Exception], ...] = (), callbacks: List[CallbackFuncType] | None = None, gc_after_trial: bool = True, show_progress_bar: bool = False) -> None:
        '''Optimize an objective function.

        This method is the same as :func:`optuna.study.Study.optimize` except for
        taking an objective function that returns multi-objective values as the argument.

        Please refer to the documentation of :func:`optuna.study.Study.optimize`
        for further details.

        Example:

            .. testcode::

                import optuna


                def objective(trial):
                    # Binh and Korn function.
                    x = trial.suggest_float("x", 0, 5)
                    y = trial.suggest_float("y", 0, 3)

                    v0 = 4 * x ** 2 + 4 * y ** 2
                    v1 = (x - 5) ** 2 + (y - 5) ** 2
                    return v0, v1


                study = optuna.multi_objective.create_study(["minimize", "minimize"])
                study.optimize(objective, n_trials=3)
        '''
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
    def set_user_attr(self, key: str, value: Any) -> None:
        """Set a user attribute to the study.

        Args:
            key: A key string of the attribute.
            value: A value of the attribute. The value should be JSON serializable.
        """
    def set_system_attr(self, key: str, value: Any) -> None:
        """Set a system attribute to the study.

        Note that Optuna internally uses this method to save system messages. Please use
        :func:`~optuna.multi_objective.study.MultiObjectiveStudy.set_user_attr`
        to set users' attributes.

        Args:
            key: A key string of the attribute.
            value: A value of the attribute. The value should be JSON serializable.

        """
    def enqueue_trial(self, params: Dict[str, Any]) -> None:
        """Enqueue a trial with given parameter values.

        You can fix the next sampling parameters which will be evaluated in your
        objective function.

        Please refer to the documentation of :func:`optuna.study.Study.enqueue_trial`
        for further details.

        Args:
            params:
                Parameter values to pass your objective function.
        """
    @property
    def trials(self) -> List['multi_objective.trial.FrozenMultiObjectiveTrial']:
        """Return all trials in the study.

        The returned trials are ordered by trial number.

        This is a short form of ``self.get_trials(deepcopy=True, states=None)``.

        Returns:
            A list of :class:`~optuna.multi_objective.trial.FrozenMultiObjectiveTrial` objects.
        """
    def get_trials(self, deepcopy: bool = True, states: Tuple[TrialState, ...] | None = None) -> List['multi_objective.trial.FrozenMultiObjectiveTrial']:
        """Return all trials in the study.

        The returned trials are ordered by trial number.

        Args:
            deepcopy:
                Flag to control whether to apply ``copy.deepcopy()`` to the trials.
                Note that if you set the flag to :obj:`False`, you shouldn't mutate
                any fields of the returned trial. Otherwise the internal state of
                the study may corrupt and unexpected behavior may happen.
            states:
                Trial states to filter on. If :obj:`None`, include all states.

        Returns:
            A list of :class:`~optuna.multi_objective.trial.FrozenMultiObjectiveTrial` objects.
        """
    def get_pareto_front_trials(self) -> List['multi_objective.trial.FrozenMultiObjectiveTrial']:
        """Return trials located at the pareto front in the study.

        A trial is located at the pareto front if there are no trials that dominate the trial.
        It's called that a trial ``t0`` dominates another trial ``t1`` if
        ``all(v0 <= v1) for v0, v1 in zip(t0.values, t1.values)`` and
        ``any(v0 < v1) for v0, v1 in zip(t0.values, t1.values)`` are held.

        Returns:
            A list of :class:`~optuna.multi_objective.trial.FrozenMultiObjectiveTrial` objects.
        """
