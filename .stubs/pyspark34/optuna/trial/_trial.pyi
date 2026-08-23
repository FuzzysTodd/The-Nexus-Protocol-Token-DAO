import datetime
import optuna
from _typeshed import Incomplete
from optuna import distributions as distributions, logging as logging, pruners as pruners
from optuna.distributions import BaseDistribution as BaseDistribution, CategoricalChoiceType as CategoricalChoiceType, CategoricalDistribution as CategoricalDistribution, DiscreteUniformDistribution as DiscreteUniformDistribution, IntLogUniformDistribution as IntLogUniformDistribution, IntUniformDistribution as IntUniformDistribution, LogUniformDistribution as LogUniformDistribution, UniformDistribution as UniformDistribution
from optuna.trial._base import BaseTrial as BaseTrial
from optuna.trial._state import TrialState as TrialState
from typing import Any, Dict, Sequence

class Trial(BaseTrial):
    """A trial is a process of evaluating an objective function.

    This object is passed to an objective function and provides interfaces to get parameter
    suggestion, manage the trial's state, and set/get user-defined attributes of the trial.

    Note that the direct use of this constructor is not recommended.
    This object is seamlessly instantiated and passed to the objective function behind
    the :func:`optuna.study.Study.optimize()` method; hence library users do not care about
    instantiation of this object.

    Args:
        study:
            A :class:`~optuna.study.Study` object.
        trial_id:
            A trial ID that is automatically generated.

    """
    study: Incomplete
    storage: Incomplete
    def __init__(self, study: optuna.study.Study, trial_id: int) -> None: ...
    def suggest_float(self, name: str, low: float, high: float, *, step: float | None = None, log: bool = False) -> float:
        '''Suggest a value for the floating point parameter.

        Note that this is a wrapper method for :func:`~optuna.trial.Trial.suggest_uniform`,
        :func:`~optuna.trial.Trial.suggest_loguniform` and
        :func:`~optuna.trial.Trial.suggest_discrete_uniform`.

        .. versionadded:: 1.3.0

        .. seealso::
            Please see also :func:`~optuna.trial.Trial.suggest_uniform`,
            :func:`~optuna.trial.Trial.suggest_loguniform` and
            :func:`~optuna.trial.Trial.suggest_discrete_uniform`.

        Example:

            Suggest a momentum, learning rate and scaling factor of learning rate
            for neural network training.

            .. testcode::

                import numpy as np
                from sklearn.datasets import load_iris
                from sklearn.model_selection import train_test_split
                from sklearn.neural_network import MLPClassifier

                import optuna

                X, y = load_iris(return_X_y=True)
                X_train, X_valid, y_train, y_valid = train_test_split(X, y, random_state=0)


                def objective(trial):
                    momentum = trial.suggest_float("momentum", 0.0, 1.0)
                    learning_rate_init = trial.suggest_float(
                        "learning_rate_init", 1e-5, 1e-3, log=True
                    )
                    power_t = trial.suggest_float("power_t", 0.2, 0.8, step=0.1)
                    clf = MLPClassifier(
                        hidden_layer_sizes=(100, 50),
                        momentum=momentum,
                        learning_rate_init=learning_rate_init,
                        solver="sgd",
                        random_state=0,
                        power_t=power_t,
                    )
                    clf.fit(X_train, y_train)

                    return clf.score(X_valid, y_valid)


                study = optuna.create_study(direction="maximize")
                study.optimize(objective, n_trials=3)

        Args:
            name:
                A parameter name.
            low:
                Lower endpoint of the range of suggested values. ``low`` is included in the range.
            high:
                Upper endpoint of the range of suggested values. ``high`` is excluded from the
                range.

                .. note::
                    If ``step`` is specified, ``high`` is included as well as ``low`` because
                    this method falls back to :func:`~optuna.trial.Trial.suggest_discrete_uniform`.

            step:
                A step of discretization.

                .. note::
                    The ``step`` and ``log`` arguments cannot be used at the same time. To set
                    the ``step`` argument to a float number, set the ``log`` argument to ``False``.
            log:
                A flag to sample the value from the log domain or not.
                If ``log`` is true, the value is sampled from the range in the log domain.
                Otherwise, the value is sampled from the range in the linear domain.
                See also :func:`suggest_uniform` and :func:`suggest_loguniform`.

                .. note::
                    The ``step`` and ``log`` arguments cannot be used at the same time. To set
                    the ``log`` argument to ``True``, set the ``step`` argument to ``None``.

        Raises:
            :exc:`ValueError`:
                If ``step is not None`` and ``log = True`` are specified.

        Returns:
            A suggested float value.
        '''
    def suggest_uniform(self, name: str, low: float, high: float) -> float:
        '''Suggest a value for the continuous parameter.

        The value is sampled from the range :math:`[\\mathsf{low}, \\mathsf{high})`
        in the linear domain. When :math:`\\mathsf{low} = \\mathsf{high}`, the value of
        :math:`\\mathsf{low}` will be returned.

        Example:

            Suggest a momentum for neural network training.

            .. testcode::

                import numpy as np
                from sklearn.datasets import load_iris
                from sklearn.model_selection import train_test_split
                from sklearn.neural_network import MLPClassifier

                import optuna

                X, y = load_iris(return_X_y=True)
                X_train, X_valid, y_train, y_valid = train_test_split(X, y)


                def objective(trial):
                    momentum = trial.suggest_uniform("momentum", 0.0, 1.0)
                    clf = MLPClassifier(
                        hidden_layer_sizes=(100, 50),
                        momentum=momentum,
                        solver="sgd",
                        random_state=0,
                    )
                    clf.fit(X_train, y_train)

                    return clf.score(X_valid, y_valid)


                study = optuna.create_study(direction="maximize")
                study.optimize(objective, n_trials=3)

        Args:
            name:
                A parameter name.
            low:
                Lower endpoint of the range of suggested values. ``low`` is included in the range.
            high:
                Upper endpoint of the range of suggested values. ``high`` is excluded from the
                range.

        Returns:
            A suggested float value.
        '''
    def suggest_loguniform(self, name: str, low: float, high: float) -> float:
        '''Suggest a value for the continuous parameter.

        The value is sampled from the range :math:`[\\mathsf{low}, \\mathsf{high})`
        in the log domain. When :math:`\\mathsf{low} = \\mathsf{high}`, the value of
        :math:`\\mathsf{low}` will be returned.

        Example:

            Suggest penalty parameter ``C`` of `SVC <https://scikit-learn.org/stable/modules/
            generated/sklearn.svm.SVC.html>`_.

            .. testcode::

                import numpy as np
                from sklearn.datasets import load_iris
                from sklearn.model_selection import train_test_split
                from sklearn.svm import SVC

                import optuna

                X, y = load_iris(return_X_y=True)
                X_train, X_valid, y_train, y_valid = train_test_split(X, y)


                def objective(trial):
                    c = trial.suggest_loguniform("c", 1e-5, 1e2)
                    clf = SVC(C=c, gamma="scale", random_state=0)
                    clf.fit(X_train, y_train)
                    return clf.score(X_valid, y_valid)


                study = optuna.create_study(direction="maximize")
                study.optimize(objective, n_trials=3)

        Args:
            name:
                A parameter name.
            low:
                Lower endpoint of the range of suggested values. ``low`` is included in the range.
            high:
                Upper endpoint of the range of suggested values. ``high`` is excluded from the
                range.

        Returns:
            A suggested float value.
        '''
    def suggest_discrete_uniform(self, name: str, low: float, high: float, q: float) -> float:
        '''Suggest a value for the discrete parameter.

        The value is sampled from the range :math:`[\\mathsf{low}, \\mathsf{high}]`,
        and the step of discretization is :math:`q`. More specifically,
        this method returns one of the values in the sequence
        :math:`\\mathsf{low}, \\mathsf{low} + q, \\mathsf{low} + 2 q, \\dots,
        \\mathsf{low} + k q \\le \\mathsf{high}`,
        where :math:`k` denotes an integer. Note that :math:`high` may be changed due to round-off
        errors if :math:`q` is not an integer. Please check warning messages to find the changed
        values.

        Example:

            Suggest a fraction of samples used for fitting the individual learners of
            `GradientBoostingClassifier <https://scikit-learn.org/stable/modules/generated/
            sklearn.ensemble.GradientBoostingClassifier.html>`_.

            .. testcode::

                import numpy as np
                from sklearn.datasets import load_iris
                from sklearn.ensemble import GradientBoostingClassifier
                from sklearn.model_selection import train_test_split

                import optuna

                X, y = load_iris(return_X_y=True)
                X_train, X_valid, y_train, y_valid = train_test_split(X, y)


                def objective(trial):
                    subsample = trial.suggest_discrete_uniform("subsample", 0.1, 1.0, 0.1)
                    clf = GradientBoostingClassifier(subsample=subsample, random_state=0)
                    clf.fit(X_train, y_train)
                    return clf.score(X_valid, y_valid)


                study = optuna.create_study(direction="maximize")
                study.optimize(objective, n_trials=3)

        Args:
            name:
                A parameter name.
            low:
                Lower endpoint of the range of suggested values. ``low`` is included in the range.
            high:
                Upper endpoint of the range of suggested values. ``high`` is included in the range.
            q:
                A step of discretization.

        Returns:
            A suggested float value.
        '''
    def suggest_int(self, name: str, low: int, high: int, step: int = 1, log: bool = False) -> int:
        '''Suggest a value for the integer parameter.

        The value is sampled from the integers in :math:`[\\mathsf{low}, \\mathsf{high}]`.

        Example:

            Suggest the number of trees in `RandomForestClassifier <https://scikit-learn.org/
            stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>`_.

            .. testcode::

                import numpy as np
                from sklearn.datasets import load_iris
                from sklearn.ensemble import RandomForestClassifier
                from sklearn.model_selection import train_test_split

                import optuna

                X, y = load_iris(return_X_y=True)
                X_train, X_valid, y_train, y_valid = train_test_split(X, y)


                def objective(trial):
                    n_estimators = trial.suggest_int("n_estimators", 50, 400)
                    clf = RandomForestClassifier(n_estimators=n_estimators, random_state=0)
                    clf.fit(X_train, y_train)
                    return clf.score(X_valid, y_valid)


                study = optuna.create_study(direction="maximize")
                study.optimize(objective, n_trials=3)

        Args:
            name:
                A parameter name.
            low:
                Lower endpoint of the range of suggested values. ``low`` is included in the range.
            high:
                Upper endpoint of the range of suggested values. ``high`` is included in the range.
            step:
                A step of discretization.

                .. note::
                    Note that :math:`\\mathsf{high}` is modified if the range is not divisible by
                    :math:`\\mathsf{step}`. Please check the warning messages to find the changed
                    values.

                .. note::
                    The method returns one of the values in the sequence
                    :math:`\\mathsf{low}, \\mathsf{low} + \\mathsf{step}, \\mathsf{low} + 2 *
                    \\mathsf{step}, \\dots, \\mathsf{low} + k * \\mathsf{step} \\le
                    \\mathsf{high}`, where :math:`k` denotes an integer.

                .. note::
                    The ``step != 1`` and ``log`` arguments cannot be used at the same time.
                    To set the ``step`` argument :math:`\\mathsf{step} \\ge 2`, set the
                    ``log`` argument to ``False``.
            log:
                A flag to sample the value from the log domain or not.

                .. note::
                    If ``log`` is true, at first, the range of suggested values is divided into
                    grid points of width 1. The range of suggested values is then converted to
                    a log domain, from which a value is sampled. The uniformly sampled
                    value is re-converted to the original domain and rounded to the nearest grid
                    point that we just split, and the suggested value is determined.
                    For example, if `low = 2` and `high = 8`, then the range of suggested values is
                    `[2, 3, 4, 5, 6, 7, 8]` and lower values tend to be more sampled than higher
                    values.

                .. note::
                    The ``step != 1`` and ``log`` arguments cannot be used at the same time.
                    To set the ``log`` argument to ``True``, set the ``step`` argument to 1.

        Raises:
            :exc:`ValueError`:
                If ``step != 1`` and ``log = True`` are specified.
        '''
    def suggest_categorical(self, name: str, choices: Sequence[CategoricalChoiceType]) -> CategoricalChoiceType:
        '''Suggest a value for the categorical parameter.

        The value is sampled from ``choices``.

        Example:

            Suggest a kernel function of `SVC <https://scikit-learn.org/stable/modules/generated/
            sklearn.svm.SVC.html>`_.

            .. testcode::

                import numpy as np
                from sklearn.datasets import load_iris
                from sklearn.model_selection import train_test_split
                from sklearn.svm import SVC

                import optuna

                X, y = load_iris(return_X_y=True)
                X_train, X_valid, y_train, y_valid = train_test_split(X, y)


                def objective(trial):
                    kernel = trial.suggest_categorical("kernel", ["linear", "poly", "rbf"])
                    clf = SVC(kernel=kernel, gamma="scale", random_state=0)
                    clf.fit(X_train, y_train)
                    return clf.score(X_valid, y_valid)


                study = optuna.create_study(direction="maximize")
                study.optimize(objective, n_trials=3)


        Args:
            name:
                A parameter name.
            choices:
                Parameter value candidates.

        .. seealso::
            :class:`~optuna.distributions.CategoricalDistribution`.

        Returns:
            A suggested value.
        '''
    def report(self, value: float, step: int) -> None:
        '''Report an objective function value for a given step.

        The reported values are used by the pruners to determine whether this trial should be
        pruned.

        .. seealso::
            Please refer to :class:`~optuna.pruners.BasePruner`.

        .. note::
            The reported value is converted to ``float`` type by applying ``float()``
            function internally. Thus, it accepts all float-like types (e.g., ``numpy.float32``).
            If the conversion fails, a ``TypeError`` is raised.

        Example:

            Report intermediate scores of `SGDClassifier <https://scikit-learn.org/stable/modules/
            generated/sklearn.linear_model.SGDClassifier.html>`_ training.

            .. testcode::

                import numpy as np
                from sklearn.datasets import load_iris
                from sklearn.linear_model import SGDClassifier
                from sklearn.model_selection import train_test_split

                import optuna

                X, y = load_iris(return_X_y=True)
                X_train, X_valid, y_train, y_valid = train_test_split(X, y)


                def objective(trial):
                    clf = SGDClassifier(random_state=0)
                    for step in range(100):
                        clf.partial_fit(X_train, y_train, np.unique(y))
                        intermediate_value = clf.score(X_valid, y_valid)
                        trial.report(intermediate_value, step=step)
                        if trial.should_prune():
                            raise optuna.TrialPruned()

                    return clf.score(X_valid, y_valid)


                study = optuna.create_study(direction="maximize")
                study.optimize(objective, n_trials=3)


        Args:
            value:
                A value returned from the objective function.
            step:
                Step of the trial (e.g., Epoch of neural network training). Note that pruners
                assume that ``step`` starts at zero. For example,
                :class:`~optuna.pruners.MedianPruner` simply checks if ``step`` is less than
                ``n_warmup_steps`` as the warmup mechanism.

        Raises:
            :exc:`NotImplementedError`:
                If trial is being used for multi-objective optimization.
        '''
    def should_prune(self) -> bool:
        """Suggest whether the trial should be pruned or not.

        The suggestion is made by a pruning algorithm associated with the trial and is based on
        previously reported values. The algorithm can be specified when constructing a
        :class:`~optuna.study.Study`.

        .. note::
            If no values have been reported, the algorithm cannot make meaningful suggestions.
            Similarly, if this method is called multiple times with the exact same set of reported
            values, the suggestions will be the same.

        .. seealso::
            Please refer to the example code in :func:`optuna.trial.Trial.report`.

        Returns:
            A boolean value. If :obj:`True`, the trial should be pruned according to the
            configured pruning algorithm. Otherwise, the trial should continue.

        Raises:
            :exc:`NotImplementedError`:
                If trial is being used for multi-objective optimization.
        """
    def set_user_attr(self, key: str, value: Any) -> None:
        '''Set user attributes to the trial.

        The user attributes in the trial can be access via :func:`optuna.trial.Trial.user_attrs`.

        Example:

            Save fixed hyperparameters of neural network training.

            .. testcode::

                import numpy as np
                from sklearn.datasets import load_iris
                from sklearn.model_selection import train_test_split
                from sklearn.neural_network import MLPClassifier

                import optuna

                X, y = load_iris(return_X_y=True)
                X_train, X_valid, y_train, y_valid = train_test_split(X, y, random_state=0)


                def objective(trial):
                    trial.set_user_attr("BATCHSIZE", 128)
                    momentum = trial.suggest_uniform("momentum", 0, 1.0)
                    clf = MLPClassifier(
                        hidden_layer_sizes=(100, 50),
                        batch_size=trial.user_attrs["BATCHSIZE"],
                        momentum=momentum,
                        solver="sgd",
                        random_state=0,
                    )
                    clf.fit(X_train, y_train)

                    return clf.score(X_valid, y_valid)


                study = optuna.create_study(direction="maximize")
                study.optimize(objective, n_trials=3)
                assert "BATCHSIZE" in study.best_trial.user_attrs.keys()
                assert study.best_trial.user_attrs["BATCHSIZE"] == 128


        Args:
            key:
                A key string of the attribute.
            value:
                A value of the attribute. The value should be JSON serializable.
        '''
    def set_system_attr(self, key: str, value: Any) -> None:
        """Set system attributes to the trial.

        Note that Optuna internally uses this method to save system messages such as failure
        reason of trials. Please use :func:`~optuna.trial.Trial.set_user_attr` to set users'
        attributes.

        Args:
            key:
                A key string of the attribute.
            value:
                A value of the attribute. The value should be JSON serializable.
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
    def datetime_start(self) -> datetime.datetime | None:
        """Return start datetime.

        Returns:
            Datetime where the :class:`~optuna.trial.Trial` started.
        """
    @property
    def number(self) -> int:
        """Return trial's number which is consecutive and unique in a study.

        Returns:
            A trial number.
        """
