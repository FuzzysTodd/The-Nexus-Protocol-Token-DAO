from _typeshed import Incomplete
from optuna import exceptions as exceptions, logging as logging, pruners as pruners, samplers as samplers, storages as storages, trial as trial_module
from optuna._callbacks import MaxTrialsCallback as MaxTrialsCallback
from optuna._dataframe import pd as pd
from optuna._deprecated import deprecated as deprecated
from optuna._experimental import experimental as experimental
from optuna._study_direction import StudyDirection as StudyDirection
from optuna._study_summary import StudySummary as StudySummary
from optuna.distributions import BaseDistribution as BaseDistribution
from optuna.trial import FrozenTrial as FrozenTrial, TrialState as TrialState, create_trial as create_trial
from typing import Any, Callable, Dict, Iterable, List, Sequence, Tuple, Type

ObjectiveFuncType: Incomplete

class BaseStudy:
    def __init__(self, study_id: int, storage: storages.BaseStorage) -> None: ...
    @property
    def best_params(self) -> Dict[str, Any]:
        """Return parameters of the best trial in the study.

        Returns:
            A dictionary containing parameters of the best trial.

        Raises:
            :exc:`RuntimeError`:
                If the study has more than one direction.
        """
    @property
    def best_value(self) -> float:
        """Return the best objective value in the study.

        Returns:
            A float representing the best objective value.

        Raises:
            :exc:`RuntimeError`:
                If the study has more than one direction.
        """
    @property
    def best_trial(self) -> FrozenTrial:
        """Return the best trial in the study.

        Returns:
            A :class:`~optuna.FrozenTrial` object of the best trial.

        Raises:
            :exc:`RuntimeError`:
                If the study has more than one direction.
        """
    @property
    def best_trials(self) -> List[FrozenTrial]:
        """Return trials located at the Pareto front in the study.

        A trial is located at the Pareto front if there are no trials that dominate the trial.
        It's called that a trial ``t0`` dominates another trial ``t1`` if
        ``all(v0 <= v1) for v0, v1 in zip(t0.values, t1.values)`` and
        ``any(v0 < v1) for v0, v1 in zip(t0.values, t1.values)`` are held.

        Returns:
            A list of :class:`~optuna.trial.FrozenTrial` objects.
        """
    @property
    def direction(self) -> StudyDirection:
        """Return the direction of the study.

        Returns:
            A :class:`~optuna.study.StudyDirection` object.

        Raises:
            :exc:`RuntimeError`:
                If the study has more than one direction.
        """
    @property
    def directions(self) -> List[StudyDirection]:
        """Return the directions of the study.

        Returns:
            A list of :class:`~optuna.study.StudyDirection` objects.
        """
    @property
    def trials(self) -> List[FrozenTrial]:
        """Return all trials in the study.

        The returned trials are ordered by trial number.

        This is a short form of ``self.get_trials(deepcopy=True, states=None)``.

        Returns:
            A list of :class:`~optuna.FrozenTrial` objects.
        """
    def get_trials(self, deepcopy: bool = True, states: Tuple[TrialState, ...] | None = None) -> List[FrozenTrial]:
        '''Return all trials in the study.

        The returned trials are ordered by trial number.

        Example:
            .. testcode::

                import optuna


                def objective(trial):
                    x = trial.suggest_float("x", -1, 1)
                    return x ** 2


                study = optuna.create_study()
                study.optimize(objective, n_trials=3)

                trials = study.get_trials()
                assert len(trials) == 3
        Args:
            deepcopy:
                Flag to control whether to apply ``copy.deepcopy()`` to the trials.
                Note that if you set the flag to :obj:`False`, you shouldn\'t mutate
                any fields of the returned trial. Otherwise the internal state of
                the study may corrupt and unexpected behavior may happen.
            states:
                Trial states to filter on. If :obj:`None`, include all states.

        Returns:
            A list of :class:`~optuna.FrozenTrial` objects.
        '''

class Study(BaseStudy):
    """A study corresponds to an optimization task, i.e., a set of trials.

    This object provides interfaces to run a new :class:`~optuna.trial.Trial`, access trials'
    history, set/get user-defined attributes of the study itself.

    Note that the direct use of this constructor is not recommended.
    To create and load a study, please refer to the documentation of
    :func:`~optuna.study.create_study` and :func:`~optuna.study.load_study` respectively.

    """
    study_name: Incomplete
    sampler: Incomplete
    pruner: Incomplete
    def __init__(self, study_name: str, storage: str | storages.BaseStorage, sampler: samplers.BaseSampler | None = None, pruner: pruners.BasePruner | None = None) -> None: ...
    @property
    def user_attrs(self) -> Dict[str, Any]:
        '''Return user attributes.

        .. seealso::

            See :func:`~optuna.study.Study.set_user_attr` for related method.

        Example:

            .. testcode::

                import optuna


                def objective(trial):
                    x = trial.suggest_float("x", 0, 1)
                    y = trial.suggest_float("y", 0, 1)
                    return x ** 2 + y ** 2


                study = optuna.create_study()

                study.set_user_attr("objective function", "quadratic function")
                study.set_user_attr("dimensions", 2)
                study.set_user_attr("contributors", ["Akiba", "Sano"])

                assert study.user_attrs == {
                    "objective function": "quadratic function",
                    "dimensions": 2,
                    "contributors": ["Akiba", "Sano"],
                }

        Returns:
            A dictionary containing all user attributes.
        '''
    @property
    def system_attrs(self) -> Dict[str, Any]:
        """Return system attributes.

        Returns:
            A dictionary containing all system attributes.
        """
    def optimize(self, func: ObjectiveFuncType, n_trials: int | None = None, timeout: float | None = None, n_jobs: int = 1, catch: Tuple[Type[Exception], ...] = (), callbacks: List[Callable[[Study, FrozenTrial], None]] | None = None, gc_after_trial: bool = False, show_progress_bar: bool = False) -> None:
        '''Optimize an objective function.

        Optimization is done by choosing a suitable set of hyperparameter values from a given
        range. Uses a sampler which implements the task of value suggestion based on a specified
        distribution. The sampler is specified in :func:`~optuna.study.create_study` and the
        default choice for the sampler is TPE.
        See also :class:`~optuna.samplers.TPESampler` for more details on \'TPE\'.

        Example:

            .. testcode::

                import optuna


                def objective(trial):
                    x = trial.suggest_float("x", -1, 1)
                    return x ** 2


                study = optuna.create_study()
                study.optimize(objective, n_trials=3)

        Args:
            func:
                A callable that implements objective function.
            n_trials:
                The number of trials. If this argument is set to :obj:`None`, there is no
                limitation on the number of trials. If :obj:`timeout` is also set to :obj:`None`,
                the study continues to create trials until it receives a termination signal such
                as Ctrl+C or SIGTERM.
            timeout:
                Stop study after the given number of second(s). If this argument is set to
                :obj:`None`, the study is executed without time limitation. If :obj:`n_trials` is
                also set to :obj:`None`, the study continues to create trials until it receives a
                termination signal such as Ctrl+C or SIGTERM.
            n_jobs:
                The number of parallel jobs. If this argument is set to :obj:`-1`, the number is
                set to CPU count.

                .. note::
                    ``n_jobs`` allows parallelization using :obj:`threading` and may suffer from
                    `Python\'s GIL <https://wiki.python.org/moin/GlobalInterpreterLock>`_.
                    It is recommended to use :ref:`process-based parallelization<distributed>`
                    if ``func`` is CPU bound.

                .. warning::
                    Deprecated in v2.7.0. This feature will be removed in the future.
                    It is recommended to use :ref:`process-based parallelization<distributed>`.
                    The removal of this feature is currently scheduled for v4.0.0, but this
                    schedule is subject to change.
                    See https://github.com/optuna/optuna/releases/tag/v2.7.0.

            catch:
                A study continues to run even when a trial raises one of the exceptions specified
                in this argument. Default is an empty tuple, i.e. the study will stop for any
                exception except for :class:`~optuna.exceptions.TrialPruned`.
            callbacks:
                List of callback functions that are invoked at the end of each trial. Each function
                must accept two parameters with the following types in this order:
                :class:`~optuna.study.Study` and :class:`~optuna.FrozenTrial`.
            gc_after_trial:
                Flag to determine whether to automatically run garbage collection after each trial.
                Set to :obj:`True` to run the garbage collection, :obj:`False` otherwise.
                When it runs, it runs a full collection by internally calling :func:`gc.collect`.
                If you see an increase in memory consumption over several trials, try setting this
                flag to :obj:`True`.

                .. seealso::

                    :ref:`out-of-memory-gc-collect`

            show_progress_bar:
                Flag to show progress bars or not. To disable progress bar, set this ``False``.
                Currently, progress bar is experimental feature and disabled
                when ``n_jobs`` :math:`\\ne 1`.

        Raises:
            RuntimeError:
                If nested invocation of this method occurs.
        '''
    def ask(self, fixed_distributions: Dict[str, BaseDistribution] | None = None) -> trial_module.Trial:
        '''Create a new trial from which hyperparameters can be suggested.

        This method is part of an alternative to :func:`~optuna.study.Study.optimize` that allows
        controlling the lifetime of a trial outside the scope of ``func``. Each call to this
        method should be followed by a call to :func:`~optuna.study.Study.tell` to finish the
        created trial.

        .. seealso::

            The :ref:`ask_and_tell` tutorial provides use-cases with examples.

        Example:

            Getting the trial object with the :func:`~optuna.study.Study.ask` method.

            .. testcode::

                import optuna


                study = optuna.create_study()

                trial = study.ask()

                x = trial.suggest_float("x", -1, 1)

                study.tell(trial, x ** 2)

        Example:

            Passing previously defined distributions to the :func:`~optuna.study.Study.ask`
            method.

            .. testcode::

                import optuna


                study = optuna.create_study()

                distributions = {
                    "optimizer": optuna.distributions.CategoricalDistribution(["adam", "sgd"]),
                    "lr": optuna.distributions.LogUniformDistribution(0.0001, 0.1),
                }

                # You can pass the distributions previously defined.
                trial = study.ask(fixed_distributions=distributions)

                # `optimizer` and `lr` are already suggested and accessible with `trial.params`.
                assert "optimizer" in trial.params
                assert "lr" in trial.params

        Args:
            fixed_distributions:
                A dictionary containing the parameter names and parameter\'s distributions. Each
                parameter in this dictionary is automatically suggested for the returned trial,
                even when the suggest method is not explicitly invoked by the user. If this
                argument is set to :obj:`None`, no parameter is automatically suggested.

        Returns:
            A :class:`~optuna.trial.Trial`.
        '''
    def tell(self, trial: trial_module.Trial | int, values: float | Sequence[float] | None = None, state: TrialState = ...) -> None:
        '''Finish a trial created with :func:`~optuna.study.Study.ask`.

        .. seealso::

            The :ref:`ask_and_tell` tutorial provides use-cases with examples.

        Example:

            .. testcode::

                import optuna
                from optuna.trial import TrialState


                def f(x):
                    return (x - 2) ** 2


                def df(x):
                    return 2 * x - 4


                study = optuna.create_study()

                n_trials = 30

                for _ in range(n_trials):
                    trial = study.ask()

                    lr = trial.suggest_float("lr", 1e-5, 1e-1, log=True)

                    # Iterative gradient descent objective function.
                    x = 3  # Initial value.
                    for step in range(128):
                        y = f(x)

                        trial.report(y, step=step)

                        if trial.should_prune():
                            # Finish the trial with the pruned state.
                            study.tell(trial, state=TrialState.PRUNED)
                            break

                        gy = df(x)
                        x -= gy * lr
                    else:
                        # Finish the trial with the final value after all iterations.
                        study.tell(trial, y)

        Args:
            trial:
                A :class:`~optuna.trial.Trial` object or a trial number.
            values:
                Optional objective value or a sequence of such values in case the study is used
                for multi-objective optimization. Argument must be provided if ``state`` is
                :class:`~optuna.trial.TrialState.COMPLETE` and should be :obj:`None` if ``state``
                is :class:`~optuna.trial.TrialState.FAIL` or
                :class:`~optuna.trial.TrialState.PRUNED`.
            state:
                State to be reported. Must be :class:`~optuna.trial.TrialState.COMPLETE`,
                :class:`~optuna.trial.TrialState.FAIL` or
                :class:`~optuna.trial.TrialState.PRUNED`.

        Raises:
            TypeError:
                If ``trial`` is not a :class:`~optuna.trial.Trial` or an :obj:`int`.
            ValueError:
                If any of the following.
                ``values`` is a sequence but its length does not match the number of objectives
                for its associated study.
                ``state`` is :class:`~optuna.trial.TrialState.COMPLETE` but
                ``values`` is :obj:`None`.
                ``state`` is :class:`~optuna.trial.TrialState.FAIL` or
                :class:`~optuna.trial.TrialState.PRUNED` but
                ``values`` is not :obj:`None`.
                ``state`` is not
                :class:`~optuna.trial.TrialState.COMPLETE`,
                :class:`~optuna.trial.TrialState.FAIL` or
                :class:`~optuna.trial.TrialState.PRUNED`.
                ``trial`` is a trial number but no
                trial exists with that number.
        '''
    def set_user_attr(self, key: str, value: Any) -> None:
        '''Set a user attribute to the study.

        .. seealso::

            See :attr:`~optuna.study.Study.user_attrs` for related attribute.

        Example:

            .. testcode::

                import optuna


                def objective(trial):
                    x = trial.suggest_float("x", 0, 1)
                    y = trial.suggest_float("y", 0, 1)
                    return x ** 2 + y ** 2


                study = optuna.create_study()

                study.set_user_attr("objective function", "quadratic function")
                study.set_user_attr("dimensions", 2)
                study.set_user_attr("contributors", ["Akiba", "Sano"])

                assert study.user_attrs == {
                    "objective function": "quadratic function",
                    "dimensions": 2,
                    "contributors": ["Akiba", "Sano"],
                }

        Args:
            key: A key string of the attribute.
            value: A value of the attribute. The value should be JSON serializable.

        '''
    def set_system_attr(self, key: str, value: Any) -> None:
        """Set a system attribute to the study.

        Note that Optuna internally uses this method to save system messages. Please use
        :func:`~optuna.study.Study.set_user_attr` to set users' attributes.

        Args:
            key: A key string of the attribute.
            value: A value of the attribute. The value should be JSON serializable.

        """
    def trials_dataframe(self, attrs: Tuple[str, ...] = ('number', 'value', 'datetime_start', 'datetime_complete', 'duration', 'params', 'user_attrs', 'system_attrs', 'state'), multi_index: bool = False) -> pd.DataFrame:
        '''Export trials as a pandas DataFrame_.

        The DataFrame_ provides various features to analyze studies. It is also useful to draw a
        histogram of objective values and to export trials as a CSV file.
        If there are no trials, an empty DataFrame_ is returned.

        Example:

            .. testcode::

                import optuna
                import pandas


                def objective(trial):
                    x = trial.suggest_float("x", -1, 1)
                    return x ** 2


                study = optuna.create_study()
                study.optimize(objective, n_trials=3)

                # Create a dataframe from the study.
                df = study.trials_dataframe()
                assert isinstance(df, pandas.DataFrame)
                assert df.shape[0] == 3  # n_trials.

        Args:
            attrs:
                Specifies field names of :class:`~optuna.FrozenTrial` to include them to a
                DataFrame of trials.
            multi_index:
                Specifies whether the returned DataFrame_ employs MultiIndex_ or not. Columns that
                are hierarchical by nature such as ``(params, x)`` will be flattened to
                ``params_x`` when set to :obj:`False`.

        Returns:
            A pandas DataFrame_ of trials in the :class:`~optuna.study.Study`.

        .. _DataFrame: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
        .. _MultiIndex: https://pandas.pydata.org/pandas-docs/stable/advanced.html

        Note:
            If ``value`` is in ``attrs`` during multi-objective optimization, it is implicitly
            replaced with ``values``.
        '''
    def stop(self) -> None:
        '''Exit from the current optimization loop after the running trials finish.

        This method lets the running :meth:`~optuna.study.Study.optimize` method return
        immediately after all trials which the :meth:`~optuna.study.Study.optimize` method
        spawned finishes.
        This method does not affect any behaviors of parallel or successive study processes.

        Example:

            .. testcode::

                import optuna


                def objective(trial):
                    if trial.number == 4:
                        trial.study.stop()
                    x = trial.suggest_float("x", 0, 10)
                    return x ** 2


                study = optuna.create_study()
                study.optimize(objective, n_trials=10)
                assert len(study.trials) == 5

        Raises:
            RuntimeError:
                If this method is called outside an objective function or callback.
        '''
    def enqueue_trial(self, params: Dict[str, Any]) -> None:
        '''Enqueue a trial with given parameter values.

        You can fix the next sampling parameters which will be evaluated in your
        objective function.

        Example:

            .. testcode::

                import optuna


                def objective(trial):
                    x = trial.suggest_float("x", 0, 10)
                    return x ** 2


                study = optuna.create_study()
                study.enqueue_trial({"x": 5})
                study.enqueue_trial({"x": 0})
                study.optimize(objective, n_trials=2)

                assert study.trials[0].params == {"x": 5}
                assert study.trials[1].params == {"x": 0}

        Args:
            params:
                Parameter values to pass your objective function.
        '''
    def add_trial(self, trial: FrozenTrial) -> None:
        '''Add trial to study.

        The trial is validated before being added.

        Example:

            .. testcode::

                import optuna
                from optuna.distributions import UniformDistribution


                def objective(trial):
                    x = trial.suggest_float("x", 0, 10)
                    return x ** 2


                study = optuna.create_study()
                assert len(study.trials) == 0

                trial = optuna.trial.create_trial(
                    params={"x": 2.0},
                    distributions={"x": UniformDistribution(0, 10)},
                    value=4.0,
                )

                study.add_trial(trial)
                assert len(study.trials) == 1

                study.optimize(objective, n_trials=3)
                assert len(study.trials) == 4

                other_study = optuna.create_study()

                for trial in study.trials:
                    other_study.add_trial(trial)
                assert len(other_study.trials) == len(study.trials)

                other_study.optimize(objective, n_trials=2)
                assert len(other_study.trials) == len(study.trials) + 2

        .. seealso::

            This method should in general be used to add already evaluated trials
            (``trial.state.is_finished() == True``). To queue trials for evaluation,
            please refer to :func:`~optuna.study.Study.enqueue_trial`.

        .. seealso::

            See :func:`~optuna.trial.create_trial` for how to create trials.

        Args:
            trial: Trial to add.

        Raises:
            :exc:`ValueError`:
                If trial is an invalid state.

        '''
    def add_trials(self, trials: Iterable[FrozenTrial]) -> None:
        '''Add trials to study.

        The trials are validated before being added.

        Example:

            .. testcode::

                import optuna
                from optuna.distributions import UniformDistribution


                def objective(trial):
                    x = trial.suggest_float("x", 0, 10)
                    return x ** 2


                study = optuna.create_study()
                study.optimize(objective, n_trials=3)
                assert len(study.trials) == 3

                other_study = optuna.create_study()
                other_study.add_trials(study.trials)
                assert len(other_study.trials) == len(study.trials)

                other_study.optimize(objective, n_trials=2)
                assert len(other_study.trials) == len(study.trials) + 2

        .. seealso::

            See :func:`~optuna.study.Study.add_trial` for addition of each trial.

        Args:
            trials: Trials to add.

        Raises:
            :exc:`ValueError`:
                If ``trials`` include invalid trial.
        '''

def create_study(storage: str | storages.BaseStorage | None = None, sampler: samplers.BaseSampler | None = None, pruner: pruners.BasePruner | None = None, study_name: str | None = None, direction: str | StudyDirection | None = None, load_if_exists: bool = False, *, directions: Sequence[str | StudyDirection] | None = None) -> Study:
    '''Create a new :class:`~optuna.study.Study`.

    Example:

        .. testcode::

            import optuna


            def objective(trial):
                x = trial.suggest_float("x", 0, 10)
                return x ** 2


            study = optuna.create_study()
            study.optimize(objective, n_trials=3)

    Args:
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
            If :obj:`None` is specified, :class:`~optuna.samplers.TPESampler` is used during
            single-objective optimization and :class:`~optuna.samplers.NSGAIISampler` during
            multi-objective optimization. See also :class:`~optuna.samplers`.
        pruner:
            A pruner object that decides early stopping of unpromising trials. If :obj:`None`
            is specified, :class:`~optuna.pruners.MedianPruner` is used as the default. See
            also :class:`~optuna.pruners`.
        study_name:
            Study\'s name. If this argument is set to None, a unique name is generated
            automatically.
        direction:
            Direction of optimization. Set ``minimize`` for minimization and ``maximize`` for
            maximization. You can also pass the corresponding :class:`~optuna.study.StudyDirection`
            object.

            .. note::
                If none of `direction` and `directions` are specified, the direction of the study
                is set to "minimize".
        load_if_exists:
            Flag to control the behavior to handle a conflict of study names.
            In the case where a study named ``study_name`` already exists in the ``storage``,
            a :class:`~optuna.exceptions.DuplicatedStudyError` is raised if ``load_if_exists`` is
            set to :obj:`False`.
            Otherwise, the creation of the study is skipped, and the existing one is returned.
        directions:
            A sequence of directions during multi-objective optimization.

    Returns:
        A :class:`~optuna.study.Study` object.

    Raises:
        :exc:`ValueError`:
            If the length of ``directions`` is zero.
            Or, if ``direction`` is neither \'minimize\' nor \'maximize\' when it is a string.
            Or, if the element of ``directions`` is neither `minimize` nor `maximize`.
            Or, if both ``direction`` and ``directions`` are specified.

    See also:
        :func:`optuna.create_study` is an alias of :func:`optuna.study.create_study`.

    '''
def load_study(study_name: str | None, storage: str | storages.BaseStorage, sampler: samplers.BaseSampler | None = None, pruner: pruners.BasePruner | None = None) -> Study:
    '''Load the existing :class:`~optuna.study.Study` that has the specified name.

    Example:

        .. testsetup::

            import os

            if os.path.exists("example.db"):
                raise RuntimeError("\'example.db\' already exists. Please remove it.")

        .. testcode::

            import optuna


            def objective(trial):
                x = trial.suggest_float("x", 0, 10)
                return x ** 2


            study = optuna.create_study(storage="sqlite:///example.db", study_name="my_study")
            study.optimize(objective, n_trials=3)

            loaded_study = optuna.load_study(study_name="my_study", storage="sqlite:///example.db")
            assert len(loaded_study.trials) == len(study.trials)

        .. testcleanup::

            os.remove("example.db")

    Args:
        study_name:
            Study\'s name. Each study has a unique name as an identifier. If :obj:`None`, checks
            whether the storage contains a single study, and if so loads that study.
        storage:
            Database URL such as ``sqlite:///example.db``. Please see also the documentation of
            :func:`~optuna.study.create_study` for further details.
        sampler:
            A sampler object that implements background algorithm for value suggestion.
            If :obj:`None` is specified, :class:`~optuna.samplers.TPESampler` is used
            as the default. See also :class:`~optuna.samplers`.
        pruner:
            A pruner object that decides early stopping of unpromising trials.
            If :obj:`None` is specified, :class:`~optuna.pruners.MedianPruner` is used
            as the default. See also :class:`~optuna.pruners`.

    Raises:
        :exc:`ValueError`:
            If ``study_name`` is :obj:`None` and the storage contains more than 1 study.

    See also:
        :func:`optuna.load_study` is an alias of :func:`optuna.study.load_study`.

    '''
def delete_study(study_name: str, storage: str | storages.BaseStorage) -> None:
    '''Delete a :class:`~optuna.study.Study` object.

    Example:

        .. testsetup::

            import os

            if os.path.exists("example.db"):
                raise RuntimeError("\'example.db\' already exists. Please remove it.")

        .. testcode::

            import optuna


            def objective(trial):
                x = trial.suggest_float("x", -10, 10)
                return (x - 2) ** 2


            study = optuna.create_study(study_name="example-study", storage="sqlite:///example.db")
            study.optimize(objective, n_trials=3)

            optuna.delete_study(study_name="example-study", storage="sqlite:///example.db")

        .. testcleanup::

            os.remove("example.db")

    Args:
        study_name:
            Study\'s name.
        storage:
            Database URL such as ``sqlite:///example.db``. Please see also the documentation of
            :func:`~optuna.study.create_study` for further details.

    See also:
        :func:`optuna.delete_study` is an alias of :func:`optuna.study.delete_study`.

    '''
def copy_study(from_study_name: str, from_storage: str | storages.BaseStorage, to_storage: str | storages.BaseStorage, to_study_name: str | None = None) -> None:
    '''Copy study from one storage to another.

    The direction(s) of the objective(s) in the study, trials, user attributes and system
    attributes are copied.

    Example:

        .. testsetup::

            import os

            if os.path.exists("example.db"):
                raise RuntimeError("\'example.db\' already exists. Please remove it.")
            if os.path.exists("example_copy.db"):
                raise RuntimeError("\'example_copy.db\' already exists. Please remove it.")

        .. testcode::

            import optuna


            def objective(trial):
                x = trial.suggest_float("x", -10, 10)
                return (x - 2) ** 2


            study = optuna.create_study(
                study_name="example-study",
                storage="sqlite:///example.db",
            )
            study.optimize(objective, n_trials=3)

            optuna.copy_study(
                from_study_name="example-study",
                from_storage="sqlite:///example.db",
                to_storage="sqlite:///example_copy.db",
            )

            study = optuna.load_study(
                study_name=None,
                storage="sqlite:///example_copy.db",
            )

        .. testcleanup::

            os.remove("example.db")
            os.remove("example_copy.db")

    Args:
        from_study_name:
            Name of study.
        from_storage:
            Source database URL such as ``sqlite:///example.db``. Please see also the
            documentation of :func:`~optuna.study.create_study` for further details.
        to_storage:
            Destination database URL.
        to_study_name:
            Name of the created study. If omitted, ``from_study_name`` is used.

    Raises:
        :class:`~optuna.exceptions.DuplicatedStudyError`:
            If a study with a conflicting name already exists in the destination storage.

    '''
def get_all_study_summaries(storage: str | storages.BaseStorage) -> List[StudySummary]:
    '''Get all history of studies stored in a specified storage.

    Example:

        .. testsetup::

            import os

            if os.path.exists("example.db"):
                raise RuntimeError("\'example.db\' already exists. Please remove it.")

        .. testcode::

            import optuna


            def objective(trial):
                x = trial.suggest_float("x", -10, 10)
                return (x - 2) ** 2


            study = optuna.create_study(study_name="example-study", storage="sqlite:///example.db")
            study.optimize(objective, n_trials=3)

            study_summaries = optuna.study.get_all_study_summaries(storage="sqlite:///example.db")
            assert len(study_summaries) == 1

            study_summary = study_summaries[0]
            assert study_summary.study_name == "example-study"

        .. testcleanup::

            os.remove("example.db")

    Args:
        storage:
            Database URL such as ``sqlite:///example.db``. Please see also the documentation of
            :func:`~optuna.study.create_study` for further details.

    Returns:
        List of study history summarized as :class:`~optuna.study.StudySummary` objects.

    See also:
        :func:`optuna.get_all_study_summaries` is an alias of
        :func:`optuna.study.get_all_study_summaries`.

    '''
