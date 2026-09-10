from ..base import BaseEstimator as BaseEstimator, ClassifierMixin as ClassifierMixin
from ..utils._metadata_requests import RequestMethod as RequestMethod
from .metaestimators import available_if as available_if
from .validation import check_array as check_array, check_is_fitted as check_is_fitted
from _typeshed import Incomplete

class ArraySlicingWrapper:
    """
    Parameters
    ----------
    array
    """
    array: Incomplete
    def __init__(self, array) -> None: ...
    def __getitem__(self, aslice): ...

class MockDataFrame:
    """
    Parameters
    ----------
    array
    """
    array: Incomplete
    values: Incomplete
    shape: Incomplete
    ndim: Incomplete
    iloc: Incomplete
    def __init__(self, array) -> None: ...
    def __len__(self) -> int: ...
    def __array__(self, dtype: Incomplete | None = None): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def take(self, indices, axis: int = 0): ...

class CheckingClassifier(ClassifierMixin, BaseEstimator):
    '''Dummy classifier to test pipelining and meta-estimators.

    Checks some property of `X` and `y`in fit / predict.
    This allows testing whether pipelines / cross-validation or metaestimators
    changed the input.

    Can also be used to check if `fit_params` are passed correctly, and
    to force a certain score to be returned.

    Parameters
    ----------
    check_y, check_X : callable, default=None
        The callable used to validate `X` and `y`. These callable should return
        a bool where `False` will trigger an `AssertionError`.

    check_y_params, check_X_params : dict, default=None
        The optional parameters to pass to `check_X` and `check_y`.

    methods_to_check : "all" or list of str, default="all"
        The methods in which the checks should be applied. By default,
        all checks will be done on all methods (`fit`, `predict`,
        `predict_proba`, `decision_function` and `score`).

    foo_param : int, default=0
        A `foo` param. When `foo > 1`, the output of :meth:`score` will be 1
        otherwise it is 0.

    expected_sample_weight : bool, default=False
        Whether to check if a valid `sample_weight` was passed to `fit`.

    expected_fit_params : list of str, default=None
        A list of the expected parameters given when calling `fit`.

    Attributes
    ----------
    classes_ : int
        The classes seen during `fit`.

    n_features_in_ : int
        The number of features seen during `fit`.

    Examples
    --------
    >>> from sklearn.utils._mocking import CheckingClassifier

    This helper allow to assert to specificities regarding `X` or `y`. In this
    case we expect `check_X` or `check_y` to return a boolean.

    >>> from sklearn.datasets import load_iris
    >>> X, y = load_iris(return_X_y=True)
    >>> clf = CheckingClassifier(check_X=lambda x: x.shape == (150, 4))
    >>> clf.fit(X, y)
    CheckingClassifier(...)

    We can also provide a check which might raise an error. In this case, we
    expect `check_X` to return `X` and `check_y` to return `y`.

    >>> from sklearn.utils import check_array
    >>> clf = CheckingClassifier(check_X=check_array)
    >>> clf.fit(X, y)
    CheckingClassifier(...)
    '''
    check_y: Incomplete
    check_y_params: Incomplete
    check_X: Incomplete
    check_X_params: Incomplete
    methods_to_check: Incomplete
    foo_param: Incomplete
    expected_sample_weight: Incomplete
    expected_fit_params: Incomplete
    def __init__(self, *, check_y: Incomplete | None = None, check_y_params: Incomplete | None = None, check_X: Incomplete | None = None, check_X_params: Incomplete | None = None, methods_to_check: str = 'all', foo_param: int = 0, expected_sample_weight: Incomplete | None = None, expected_fit_params: Incomplete | None = None) -> None: ...
    n_features_in_: Incomplete
    classes_: Incomplete
    def fit(self, X, y, sample_weight: Incomplete | None = None, **fit_params):
        """Fit classifier.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training vector, where `n_samples` is the number of samples and
            `n_features` is the number of features.

        y : array-like of shape (n_samples, n_outputs) or (n_samples,),                 default=None
            Target relative to X for classification or regression;
            None for unsupervised learning.

        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights. If None, then samples are equally weighted.

        **fit_params : dict of string -> object
            Parameters passed to the ``fit`` method of the estimator

        Returns
        -------
        self
        """
    def predict(self, X):
        """Predict the first class seen in `classes_`.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input data.

        Returns
        -------
        preds : ndarray of shape (n_samples,)
            Predictions of the first class seens in `classes_`.
        """
    def predict_proba(self, X):
        """Predict probabilities for each class.

        Here, the dummy classifier will provide a probability of 1 for the
        first class of `classes_` and 0 otherwise.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input data.

        Returns
        -------
        proba : ndarray of shape (n_samples, n_classes)
            The probabilities for each sample and class.
        """
    def decision_function(self, X):
        """Confidence score.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input data.

        Returns
        -------
        decision : ndarray of shape (n_samples,) if n_classes == 2                else (n_samples, n_classes)
            Confidence score.
        """
    def score(self, X: Incomplete | None = None, Y: Incomplete | None = None):
        """Fake score.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Input data, where `n_samples` is the number of samples and
            `n_features` is the number of features.

        Y : array-like of shape (n_samples, n_output) or (n_samples,)
            Target relative to X for classification or regression;
            None for unsupervised learning.

        Returns
        -------
        score : float
            Either 0 or 1 depending of `foo_param` (i.e. `foo_param > 1 =>
            score=1` otherwise `score=0`).
        """

class NoSampleWeightWrapper(BaseEstimator):
    """Wrap estimator which will not expose `sample_weight`.

    Parameters
    ----------
    est : estimator, default=None
        The estimator to wrap.
    """
    est: Incomplete
    def __init__(self, est: Incomplete | None = None) -> None: ...
    def fit(self, X, y): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...

class _MockEstimatorOnOffPrediction(BaseEstimator):
    '''Estimator for which we can turn on/off the prediction methods.

    Parameters
    ----------
    response_methods: list of             {"predict", "predict_proba", "decision_function"}, default=None
        List containing the response implemented by the estimator. When, the
        response is in the list, it will return the name of the response method
        when called. Otherwise, an `AttributeError` is raised. It allows to
        use `getattr` as any conventional estimator. By default, no response
        methods are mocked.
    '''
    response_methods: Incomplete
    def __init__(self, response_methods: Incomplete | None = None) -> None: ...
    classes_: Incomplete
    def fit(self, X, y): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def decision_function(self, X): ...
