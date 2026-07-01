from . import accuracy_score as accuracy_score, average_precision_score as average_precision_score, balanced_accuracy_score as balanced_accuracy_score, brier_score_loss as brier_score_loss, class_likelihood_ratios as class_likelihood_ratios, explained_variance_score as explained_variance_score, f1_score as f1_score, jaccard_score as jaccard_score, log_loss as log_loss, matthews_corrcoef as matthews_corrcoef, max_error as max_error, mean_absolute_error as mean_absolute_error, mean_absolute_percentage_error as mean_absolute_percentage_error, mean_gamma_deviance as mean_gamma_deviance, mean_poisson_deviance as mean_poisson_deviance, mean_squared_error as mean_squared_error, mean_squared_log_error as mean_squared_log_error, median_absolute_error as median_absolute_error, precision_score as precision_score, r2_score as r2_score, recall_score as recall_score, roc_auc_score as roc_auc_score, top_k_accuracy_score as top_k_accuracy_score
from ..base import is_regressor as is_regressor
from ..utils import Bunch as Bunch
from ..utils._param_validation import HasMethods as HasMethods, StrOptions as StrOptions, validate_params as validate_params
from ..utils.metadata_routing import MetadataRequest as MetadataRequest, MetadataRouter as MetadataRouter, _MetadataRequester, get_routing_for_object as get_routing_for_object, process_routing as process_routing
from ..utils.multiclass import type_of_target as type_of_target
from .cluster import adjusted_mutual_info_score as adjusted_mutual_info_score, adjusted_rand_score as adjusted_rand_score, completeness_score as completeness_score, fowlkes_mallows_score as fowlkes_mallows_score, homogeneity_score as homogeneity_score, mutual_info_score as mutual_info_score, normalized_mutual_info_score as normalized_mutual_info_score, rand_score as rand_score, v_measure_score as v_measure_score
from _typeshed import Incomplete

class _MultimetricScorer:
    """Callable for multimetric scoring used to avoid repeated calls
    to `predict_proba`, `predict`, and `decision_function`.

    `_MultimetricScorer` will return a dictionary of scores corresponding to
    the scorers in the dictionary. Note that `_MultimetricScorer` can be
    created with a dictionary with one key  (i.e. only one actual scorer).

    Parameters
    ----------
    scorers : dict
        Dictionary mapping names to callable scorers.

    raise_exc : bool, default=True
        Whether to raise the exception in `__call__` or not. If set to `False`
        a formatted string of the exception details is passed as result of
        the failing scorer.
    """
    def __init__(self, *, scorers, raise_exc: bool = True) -> None: ...
    def __call__(self, estimator, *args, **kwargs):
        """Evaluate predicted target values."""
    def get_metadata_routing(self):
        """Get metadata routing of this object.

        Please check :ref:`User Guide <metadata_routing>` on how the routing
        mechanism works.

        .. versionadded:: 1.3

        Returns
        -------
        routing : MetadataRouter
            A :class:`~utils.metadata_routing.MetadataRouter` encapsulating
            routing information.
        """

class _BaseScorer(_MetadataRequester):
    def __init__(self, score_func, sign, kwargs) -> None: ...
    def __call__(self, estimator, X, y_true, sample_weight: Incomplete | None = None, **kwargs):
        """Evaluate predicted target values for X relative to y_true.

        Parameters
        ----------
        estimator : object
            Trained estimator to use for scoring. Must have a predict_proba
            method; the output of that is used to compute the score.

        X : {array-like, sparse matrix}
            Test data that will be fed to estimator.predict.

        y_true : array-like
            Gold standard target values for X.

        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights.

        **kwargs : dict
            Other parameters passed to the scorer. Refer to
            :func:`set_score_request` for more details.

            Only available if `enable_metadata_routing=True`. See the
            :ref:`User Guide <metadata_routing>`.

            .. versionadded:: 1.3

        Returns
        -------
        score : float
            Score function applied to prediction of estimator on X.
        """
    def set_score_request(self, **kwargs):
        """Set requested parameters by the scorer.

        Please see :ref:`User Guide <metadata_routing>` on how the routing
        mechanism works.

        .. versionadded:: 1.3

        Parameters
        ----------
        kwargs : dict
            Arguments should be of the form ``param_name=alias``, and `alias`
            can be one of ``{True, False, None, str}``.
        """

class _PredictScorer(_BaseScorer): ...
class _ProbaScorer(_BaseScorer): ...
class _ThresholdScorer(_BaseScorer): ...

def get_scorer(scoring):
    """Get a scorer from string.

    Read more in the :ref:`User Guide <scoring_parameter>`.
    :func:`~sklearn.metrics.get_scorer_names` can be used to retrieve the names
    of all available scorers.

    Parameters
    ----------
    scoring : str, callable or None
        Scoring method as string. If callable it is returned as is.
        If None, returns None.

    Returns
    -------
    scorer : callable
        The scorer.

    Notes
    -----
    When passed a string, this function always returns a copy of the scorer
    object. Calling `get_scorer` twice for the same scorer results in two
    separate scorer objects.
    """

class _PassthroughScorer:
    def __init__(self, estimator) -> None: ...
    def __call__(self, estimator, *args, **kwargs):
        """Method that wraps estimator.score"""
    def get_metadata_routing(self):
        """Get requested data properties.

        Please check :ref:`User Guide <metadata_routing>` on how the routing
        mechanism works.

        .. versionadded:: 1.3

        Returns
        -------
        routing : MetadataRouter
            A :class:`~utils.metadata_routing.MetadataRouter` encapsulating
            routing information.
        """

def make_scorer(score_func, *, greater_is_better: bool = True, needs_proba: bool = False, needs_threshold: bool = False, **kwargs):
    """Make a scorer from a performance metric or loss function.

    This factory function wraps scoring functions for use in
    :class:`~sklearn.model_selection.GridSearchCV` and
    :func:`~sklearn.model_selection.cross_val_score`.
    It takes a score function, such as :func:`~sklearn.metrics.accuracy_score`,
    :func:`~sklearn.metrics.mean_squared_error`,
    :func:`~sklearn.metrics.adjusted_rand_score` or
    :func:`~sklearn.metrics.average_precision_score`
    and returns a callable that scores an estimator's output.
    The signature of the call is `(estimator, X, y)` where `estimator`
    is the model to be evaluated, `X` is the data and `y` is the
    ground truth labeling (or `None` in the case of unsupervised models).

    Read more in the :ref:`User Guide <scoring>`.

    Parameters
    ----------
    score_func : callable
        Score function (or loss function) with signature
        ``score_func(y, y_pred, **kwargs)``.

    greater_is_better : bool, default=True
        Whether `score_func` is a score function (default), meaning high is
        good, or a loss function, meaning low is good. In the latter case, the
        scorer object will sign-flip the outcome of the `score_func`.

    needs_proba : bool, default=False
        Whether `score_func` requires `predict_proba` to get probability
        estimates out of a classifier.

        If True, for binary `y_true`, the score function is supposed to accept
        a 1D `y_pred` (i.e., probability of the positive class, shape
        `(n_samples,)`).

    needs_threshold : bool, default=False
        Whether `score_func` takes a continuous decision certainty.
        This only works for binary classification using estimators that
        have either a `decision_function` or `predict_proba` method.

        If True, for binary `y_true`, the score function is supposed to accept
        a 1D `y_pred` (i.e., probability of the positive class or the decision
        function, shape `(n_samples,)`).

        For example `average_precision` or the area under the roc curve
        can not be computed using discrete predictions alone.

    **kwargs : additional arguments
        Additional parameters to be passed to `score_func`.

    Returns
    -------
    scorer : callable
        Callable object that returns a scalar score; greater is better.

    Notes
    -----
    If `needs_proba=False` and `needs_threshold=False`, the score
    function is supposed to accept the output of :term:`predict`. If
    `needs_proba=True`, the score function is supposed to accept the
    output of :term:`predict_proba` (For binary `y_true`, the score function is
    supposed to accept probability of the positive class). If
    `needs_threshold=True`, the score function is supposed to accept the
    output of :term:`decision_function` or :term:`predict_proba` when
    :term:`decision_function` is not present.

    Examples
    --------
    >>> from sklearn.metrics import fbeta_score, make_scorer
    >>> ftwo_scorer = make_scorer(fbeta_score, beta=2)
    >>> ftwo_scorer
    make_scorer(fbeta_score, beta=2)
    >>> from sklearn.model_selection import GridSearchCV
    >>> from sklearn.svm import LinearSVC
    >>> grid = GridSearchCV(LinearSVC(), param_grid={'C': [1, 10]},
    ...                     scoring=ftwo_scorer)
    """

explained_variance_scorer: Incomplete
r2_scorer: Incomplete
max_error_scorer: Incomplete
neg_mean_squared_error_scorer: Incomplete
neg_mean_squared_log_error_scorer: Incomplete
neg_mean_absolute_error_scorer: Incomplete
neg_mean_absolute_percentage_error_scorer: Incomplete
neg_median_absolute_error_scorer: Incomplete
neg_root_mean_squared_error_scorer: Incomplete
neg_mean_poisson_deviance_scorer: Incomplete
neg_mean_gamma_deviance_scorer: Incomplete
accuracy_scorer: Incomplete
balanced_accuracy_scorer: Incomplete
matthews_corrcoef_scorer: Incomplete

def positive_likelihood_ratio(y_true, y_pred): ...
def negative_likelihood_ratio(y_true, y_pred): ...

positive_likelihood_ratio_scorer: Incomplete
neg_negative_likelihood_ratio_scorer: Incomplete
top_k_accuracy_scorer: Incomplete
roc_auc_scorer: Incomplete
average_precision_scorer: Incomplete
roc_auc_ovo_scorer: Incomplete
roc_auc_ovo_weighted_scorer: Incomplete
roc_auc_ovr_scorer: Incomplete
roc_auc_ovr_weighted_scorer: Incomplete
neg_log_loss_scorer: Incomplete
neg_brier_score_scorer: Incomplete
brier_score_loss_scorer: Incomplete
adjusted_rand_scorer: Incomplete
rand_scorer: Incomplete
homogeneity_scorer: Incomplete
completeness_scorer: Incomplete
v_measure_scorer: Incomplete
mutual_info_scorer: Incomplete
adjusted_mutual_info_scorer: Incomplete
normalized_mutual_info_scorer: Incomplete
fowlkes_mallows_scorer: Incomplete

def get_scorer_names():
    """Get the names of all available scorers.

    These names can be passed to :func:`~sklearn.metrics.get_scorer` to
    retrieve the scorer object.

    Returns
    -------
    list of str
        Names of all available scorers.
    """

qualified_name: Incomplete

def check_scoring(estimator, scoring: Incomplete | None = None, *, allow_none: bool = False):
    """Determine scorer from user options.

    A TypeError will be thrown if the estimator cannot be scored.

    Parameters
    ----------
    estimator : estimator object implementing 'fit'
        The object to use to fit the data.

    scoring : str or callable, default=None
        A string (see model evaluation documentation) or
        a scorer callable object / function with signature
        ``scorer(estimator, X, y)``.
        If None, the provided estimator object's `score` method is used.

    allow_none : bool, default=False
        If no scoring is specified and the estimator has no score function, we
        can either return None or raise an exception.

    Returns
    -------
    scoring : callable
        A scorer callable object / function with signature
        ``scorer(estimator, X, y)``.
    """
