import numpy as np
import pandas as pd
from _typeshed import Incomplete
from numbers import Number
from optuna import TrialPruned as TrialPruned, distributions as distributions, logging as logging, samplers as samplers, study as study_module
from optuna._experimental import experimental as experimental
from optuna._imports import try_import as try_import
from optuna.study import StudyDirection as StudyDirection
from optuna.trial import FrozenTrial as FrozenTrial, Trial as Trial
from sklearn.base import BaseEstimator
from sklearn.model_selection import BaseCrossValidator as BaseCrossValidator
from typing import Any, Callable, Dict, Iterable, List, Mapping

BaseEstimator = object
ArrayLikeType: Incomplete
OneDimArrayLikeType: Incomplete
TwoDimArrayLikeType: Incomplete
IterableType: Incomplete
IndexableType = Iterable | None

class _Objective:
    """Callable that implements objective function.

    Args:
        estimator:
            Object to use to fit the data. This is assumed to implement the
            scikit-learn estimator interface. Either this needs to provide
            ``score``, or ``scoring`` must be passed.

        param_distributions:
            Dictionary where keys are parameters and values are distributions.
            Distributions are assumed to implement the optuna distribution
            interface.

        X:
            Training data.

        y:
            Target variable.

        cv:
            Cross-validation strategy.

        enable_pruning:
            If :obj:`True`, pruning is performed in the case where the
            underlying estimator supports ``partial_fit``.

        error_score:
            Value to assign to the score if an error occurs in fitting. If
            'raise', the error is raised. If numeric,
            ``sklearn.exceptions.FitFailedWarning`` is raised. This does not
            affect the refit step, which will always raise the error.

        fit_params:
            Parameters passed to ``fit`` one the estimator.

        groups:
            Group labels for the samples used while splitting the dataset into
            train/validation set.

        max_iter:
            Maximum number of epochs. This is only used if the underlying
            estimator supports ``partial_fit``.

        return_train_score:
            If :obj:`True`, training scores will be included. Computing
            training scores is used to get insights on how different
            hyperparameter settings impact the overfitting/underfitting
            trade-off. However computing training scores can be
            computationally expensive and is not strictly required to select
            the hyperparameters that yield the best generalization
            performance.

        scoring:
            Scorer function.
    """
    cv: Incomplete
    enable_pruning: Incomplete
    error_score: Incomplete
    estimator: Incomplete
    fit_params: Incomplete
    groups: Incomplete
    max_iter: Incomplete
    param_distributions: Incomplete
    return_train_score: Incomplete
    scoring: Incomplete
    X: Incomplete
    y: Incomplete
    def __init__(self, estimator: BaseEstimator, param_distributions: Mapping[str, distributions.BaseDistribution], X: TwoDimArrayLikeType, y: OneDimArrayLikeType | TwoDimArrayLikeType | None, cv: BaseCrossValidator, enable_pruning: bool, error_score: Number | float | str, fit_params: Dict[str, Any], groups: OneDimArrayLikeType | None, max_iter: int, return_train_score: bool, scoring: Callable[..., Number]) -> None: ...
    def __call__(self, trial: Trial) -> float: ...

class OptunaSearchCV(BaseEstimator):
    '''Hyperparameter search with cross-validation.

    Args:
        estimator:
            Object to use to fit the data. This is assumed to implement the
            scikit-learn estimator interface. Either this needs to provide
            ``score``, or ``scoring`` must be passed.

        param_distributions:
            Dictionary where keys are parameters and values are distributions.
            Distributions are assumed to implement the optuna distribution
            interface.

        cv:
            Cross-validation strategy. Possible inputs for cv are:

            - integer to specify the number of folds in a CV splitter,
            - a CV splitter,
            - an iterable yielding (train, validation) splits as arrays of indices.

            For integer, if :obj:`estimator` is a classifier and :obj:`y` is
            either binary or multiclass,
            ``sklearn.model_selection.StratifiedKFold`` is used. otherwise,
            ``sklearn.model_selection.KFold`` is used.

        enable_pruning:
            If :obj:`True`, pruning is performed in the case where the
            underlying estimator supports ``partial_fit``.

        error_score:
            Value to assign to the score if an error occurs in fitting. If
            \'raise\', the error is raised. If numeric,
            ``sklearn.exceptions.FitFailedWarning`` is raised. This does not
            affect the refit step, which will always raise the error.

        max_iter:
            Maximum number of epochs. This is only used if the underlying
            estimator supports ``partial_fit``.

        n_jobs:
            Number of :obj:`threading` based parallel jobs. :obj:`-1` means
            using the number is set to CPU count.

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

        n_trials:
            Number of trials. If :obj:`None`, there is no limitation on the
            number of trials. If :obj:`timeout` is also set to :obj:`None`,
            the study continues to create trials until it receives a
            termination signal such as Ctrl+C or SIGTERM. This trades off
            runtime vs quality of the solution.

        random_state:
            Seed of the pseudo random number generator. If int, this is the
            seed used by the random number generator. If
            ``numpy.random.RandomState`` object, this is the random number
            generator. If :obj:`None`, the global random state from
            ``numpy.random`` is used.

        refit:
            If :obj:`True`, refit the estimator with the best found
            hyperparameters. The refitted estimator is made available at the
            ``best_estimator_`` attribute and permits using ``predict``
            directly.

        return_train_score:
            If :obj:`True`, training scores will be included. Computing
            training scores is used to get insights on how different
            hyperparameter settings impact the overfitting/underfitting
            trade-off. However computing training scores can be
            computationally expensive and is not strictly required to select
            the hyperparameters that yield the best generalization
            performance.

        scoring:
            String or callable to evaluate the predictions on the validation data.
            If :obj:`None`, ``score`` on the estimator is used.

        study:
            Study corresponds to the optimization task. If :obj:`None`, a new
            study is created.

        subsample:
            Proportion of samples that are used during hyperparameter search.

            - If int, then draw ``subsample`` samples.
            - If float, then draw ``subsample`` * ``X.shape[0]`` samples.

        timeout:
            Time limit in seconds for the search of appropriate models. If
            :obj:`None`, the study is executed without time limitation. If
            :obj:`n_trials` is also set to :obj:`None`, the study continues to
            create trials until it receives a termination signal such as
            Ctrl+C or SIGTERM. This trades off runtime vs quality of the
            solution.

        verbose:
            Verbosity level. The higher, the more messages.

    Attributes:
        best_estimator_:
            Estimator that was chosen by the search. This is present only if
            ``refit`` is set to :obj:`True`.

        n_splits_:
            Number of cross-validation splits.

        refit_time_:
            Time for refitting the best estimator. This is present only if
            ``refit`` is set to :obj:`True`.

        sample_indices_:
            Indices of samples that are used during hyperparameter search.

        scorer_:
            Scorer function.

        study_:
            Actual study.

    Examples:

        .. testcode::

            import optuna
            from sklearn.datasets import load_iris
            from sklearn.svm import SVC

            clf = SVC(gamma="auto")
            param_distributions = {"C": optuna.distributions.LogUniformDistribution(1e-10, 1e10)}
            optuna_search = optuna.integration.OptunaSearchCV(clf, param_distributions)
            X, y = load_iris(return_X_y=True)
            optuna_search.fit(X, y)
            y_pred = optuna_search.predict(X)
    '''
    @property
    def best_index_(self) -> int:
        """Index which corresponds to the best candidate parameter setting."""
    @property
    def best_params_(self) -> Dict[str, Any]:
        """Parameters of the best trial in the :class:`~optuna.study.Study`."""
    @property
    def best_score_(self) -> float:
        """Mean cross-validated score of the best estimator."""
    @property
    def best_trial_(self) -> FrozenTrial:
        """Best trial in the :class:`~optuna.study.Study`."""
    @property
    def classes_(self) -> OneDimArrayLikeType:
        """Class labels."""
    @property
    def n_trials_(self) -> int:
        """Actual number of trials."""
    @property
    def trials_(self) -> List[FrozenTrial]:
        """All trials in the :class:`~optuna.study.Study`."""
    @property
    def user_attrs_(self) -> Dict[str, Any]:
        """User attributes in the :class:`~optuna.study.Study`."""
    @property
    def decision_function(self) -> Callable[..., OneDimArrayLikeType | TwoDimArrayLikeType]:
        """Call ``decision_function`` on the best estimator.

        This is available only if the underlying estimator supports
        ``decision_function`` and ``refit`` is set to :obj:`True`.
        """
    @property
    def inverse_transform(self) -> Callable[..., TwoDimArrayLikeType]:
        """Call ``inverse_transform`` on the best estimator.

        This is available only if the underlying estimator supports
        ``inverse_transform`` and ``refit`` is set to :obj:`True`.
        """
    @property
    def predict(self) -> Callable[..., OneDimArrayLikeType | TwoDimArrayLikeType]:
        """Call ``predict`` on the best estimator.

        This is available only if the underlying estimator supports ``predict``
        and ``refit`` is set to :obj:`True`.
        """
    @property
    def predict_log_proba(self) -> Callable[..., TwoDimArrayLikeType]:
        """Call ``predict_log_proba`` on the best estimator.

        This is available only if the underlying estimator supports
        ``predict_log_proba`` and ``refit`` is set to :obj:`True`.
        """
    @property
    def predict_proba(self) -> Callable[..., TwoDimArrayLikeType]:
        """Call ``predict_proba`` on the best estimator.

        This is available only if the underlying estimator supports
        ``predict_proba`` and ``refit`` is set to :obj:`True`.
        """
    @property
    def score_samples(self) -> Callable[..., OneDimArrayLikeType]:
        """Call ``score_samples`` on the best estimator.

        This is available only if the underlying estimator supports
        ``score_samples`` and ``refit`` is set to :obj:`True`.
        """
    @property
    def set_user_attr(self) -> Callable[..., None]:
        """Call ``set_user_attr`` on the :class:`~optuna.study.Study`."""
    @property
    def transform(self) -> Callable[..., TwoDimArrayLikeType]:
        """Call ``transform`` on the best estimator.

        This is available only if the underlying estimator supports
        ``transform`` and ``refit`` is set to :obj:`True`.
        """
    @property
    def trials_dataframe(self) -> Callable[..., 'pd.DataFrame']:
        """Call ``trials_dataframe`` on the :class:`~optuna.study.Study`."""
    cv: Incomplete
    enable_pruning: Incomplete
    error_score: Incomplete
    estimator: Incomplete
    max_iter: Incomplete
    n_trials: Incomplete
    n_jobs: Incomplete
    param_distributions: Incomplete
    random_state: Incomplete
    refit: Incomplete
    return_train_score: Incomplete
    scoring: Incomplete
    study: Incomplete
    subsample: Incomplete
    timeout: Incomplete
    verbose: Incomplete
    def __init__(self, estimator: BaseEstimator, param_distributions: Mapping[str, distributions.BaseDistribution], cv: BaseCrossValidator | int | None = 5, enable_pruning: bool = False, error_score: Number | float | str = ..., max_iter: int = 1000, n_jobs: int = 1, n_trials: int = 10, random_state: int | np.random.RandomState | None = None, refit: bool = True, return_train_score: bool = False, scoring: Callable[..., float] | str | None = None, study: study_module.Study | None = None, subsample: float | int = 1.0, timeout: float | None = None, verbose: int = 0) -> None: ...
    sample_indices_: Incomplete
    n_splits_: Incomplete
    scorer_: Incomplete
    study_: Incomplete
    def fit(self, X: TwoDimArrayLikeType, y: OneDimArrayLikeType | TwoDimArrayLikeType | None = None, groups: OneDimArrayLikeType | None = None, **fit_params: Any) -> OptunaSearchCV:
        """Run fit with all sets of parameters.

        Args:
            X:
                Training data.

            y:
                Target variable.

            groups:
                Group labels for the samples used while splitting the dataset
                into train/validation set.

            **fit_params:
                Parameters passed to ``fit`` on the estimator.

        Returns:
            self:
                Return self.
        """
    def score(self, X: TwoDimArrayLikeType, y: OneDimArrayLikeType | TwoDimArrayLikeType | None = None) -> float:
        """Return the score on the given data.

        Args:
            X:
                Data.

            y:
                Target variable.

        Returns:
            score:
                Scaler score.
        """
