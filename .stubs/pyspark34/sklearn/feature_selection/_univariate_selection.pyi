import abc
from ..base import BaseEstimator as BaseEstimator
from ..preprocessing import LabelBinarizer as LabelBinarizer
from ..utils import as_float_array as as_float_array, check_X_y as check_X_y, check_array as check_array, safe_mask as safe_mask, safe_sqr as safe_sqr
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions, validate_params as validate_params
from ..utils.extmath import row_norms as row_norms, safe_sparse_dot as safe_sparse_dot
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import SelectorMixin as SelectorMixin
from _typeshed import Incomplete

def f_oneway(*args):
    '''Perform a 1-way ANOVA.

    The one-way ANOVA tests the null hypothesis that 2 or more groups have
    the same population mean. The test is applied to samples from two or
    more groups, possibly with differing sizes.

    Read more in the :ref:`User Guide <univariate_feature_selection>`.

    Parameters
    ----------
    *args : {array-like, sparse matrix}
        Sample1, sample2... The sample measurements should be given as
        arguments.

    Returns
    -------
    f_statistic : float
        The computed F-value of the test.
    p_value : float
        The associated p-value from the F-distribution.

    Notes
    -----
    The ANOVA test has important assumptions that must be satisfied in order
    for the associated p-value to be valid.

    1. The samples are independent
    2. Each sample is from a normally distributed population
    3. The population standard deviations of the groups are all equal. This
       property is known as homoscedasticity.

    If these assumptions are not true for a given set of data, it may still be
    possible to use the Kruskal-Wallis H-test (`scipy.stats.kruskal`_) although
    with some loss of power.

    The algorithm is from Heiman[2], pp.394-7.

    See ``scipy.stats.f_oneway`` that should give the same results while
    being less efficient.

    References
    ----------
    .. [1] Lowry, Richard.  "Concepts and Applications of Inferential
           Statistics". Chapter 14.
           http://vassarstats.net/textbook

    .. [2] Heiman, G.W.  Research Methods in Statistics. 2002.
    '''
def f_classif(X, y):
    """Compute the ANOVA F-value for the provided sample.

    Read more in the :ref:`User Guide <univariate_feature_selection>`.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        The set of regressors that will be tested sequentially.

    y : array-like of shape (n_samples,)
        The target vector.

    Returns
    -------
    f_statistic : ndarray of shape (n_features,)
        F-statistic for each feature.

    p_values : ndarray of shape (n_features,)
        P-values associated with the F-statistic.

    See Also
    --------
    chi2 : Chi-squared stats of non-negative features for classification tasks.
    f_regression : F-value between label/feature for regression tasks.
    """
def chi2(X, y):
    '''Compute chi-squared stats between each non-negative feature and class.

    This score can be used to select the `n_features` features with the
    highest values for the test chi-squared statistic from X, which must
    contain only **non-negative features** such as booleans or frequencies
    (e.g., term counts in document classification), relative to the classes.

    Recall that the chi-square test measures dependence between stochastic
    variables, so using this function "weeds out" the features that are the
    most likely to be independent of class and therefore irrelevant for
    classification.

    Read more in the :ref:`User Guide <univariate_feature_selection>`.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        Sample vectors.

    y : array-like of shape (n_samples,)
        Target vector (class labels).

    Returns
    -------
    chi2 : ndarray of shape (n_features,)
        Chi2 statistics for each feature.

    p_values : ndarray of shape (n_features,)
        P-values for each feature.

    See Also
    --------
    f_classif : ANOVA F-value between label/feature for classification tasks.
    f_regression : F-value between label/feature for regression tasks.

    Notes
    -----
    Complexity of this algorithm is O(n_classes * n_features).
    '''
def r_regression(X, y, *, center: bool = True, force_finite: bool = True):
    """Compute Pearson's r for each features and the target.

    Pearson's r is also known as the Pearson correlation coefficient.

    Linear model for testing the individual effect of each of many regressors.
    This is a scoring function to be used in a feature selection procedure, not
    a free standing feature selection procedure.

    The cross correlation between each regressor and the target is computed
    as::

        E[(X[:, i] - mean(X[:, i])) * (y - mean(y))] / (std(X[:, i]) * std(y))

    For more on usage see the :ref:`User Guide <univariate_feature_selection>`.

    .. versionadded:: 1.0

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        The data matrix.

    y : array-like of shape (n_samples,)
        The target vector.

    center : bool, default=True
        Whether or not to center the data matrix `X` and the target vector `y`.
        By default, `X` and `y` will be centered.

    force_finite : bool, default=True
        Whether or not to force the Pearson's R correlation to be finite.
        In the particular case where some features in `X` or the target `y`
        are constant, the Pearson's R correlation is not defined. When
        `force_finite=False`, a correlation of `np.nan` is returned to
        acknowledge this case. When `force_finite=True`, this value will be
        forced to a minimal correlation of `0.0`.

        .. versionadded:: 1.1

    Returns
    -------
    correlation_coefficient : ndarray of shape (n_features,)
        Pearson's R correlation coefficients of features.

    See Also
    --------
    f_regression: Univariate linear regression tests returning f-statistic
        and p-values.
    mutual_info_regression: Mutual information for a continuous target.
    f_classif: ANOVA F-value between label/feature for classification tasks.
    chi2: Chi-squared stats of non-negative features for classification tasks.
    """
def f_regression(X, y, *, center: bool = True, force_finite: bool = True):
    """Univariate linear regression tests returning F-statistic and p-values.

    Quick linear model for testing the effect of a single regressor,
    sequentially for many regressors.

    This is done in 2 steps:

    1. The cross correlation between each regressor and the target is computed
       using :func:`r_regression` as::

           E[(X[:, i] - mean(X[:, i])) * (y - mean(y))] / (std(X[:, i]) * std(y))

    2. It is converted to an F score and then to a p-value.

    :func:`f_regression` is derived from :func:`r_regression` and will rank
    features in the same order if all the features are positively correlated
    with the target.

    Note however that contrary to :func:`f_regression`, :func:`r_regression`
    values lie in [-1, 1] and can thus be negative. :func:`f_regression` is
    therefore recommended as a feature selection criterion to identify
    potentially predictive feature for a downstream classifier, irrespective of
    the sign of the association with the target variable.

    Furthermore :func:`f_regression` returns p-values while
    :func:`r_regression` does not.

    Read more in the :ref:`User Guide <univariate_feature_selection>`.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        The data matrix.

    y : array-like of shape (n_samples,)
        The target vector.

    center : bool, default=True
        Whether or not to center the data matrix `X` and the target vector `y`.
        By default, `X` and `y` will be centered.

    force_finite : bool, default=True
        Whether or not to force the F-statistics and associated p-values to
        be finite. There are two cases where the F-statistic is expected to not
        be finite:

        - when the target `y` or some features in `X` are constant. In this
          case, the Pearson's R correlation is not defined leading to obtain
          `np.nan` values in the F-statistic and p-value. When
          `force_finite=True`, the F-statistic is set to `0.0` and the
          associated p-value is set to `1.0`.
        - when a feature in `X` is perfectly correlated (or
          anti-correlated) with the target `y`. In this case, the F-statistic
          is expected to be `np.inf`. When `force_finite=True`, the F-statistic
          is set to `np.finfo(dtype).max` and the associated p-value is set to
          `0.0`.

        .. versionadded:: 1.1

    Returns
    -------
    f_statistic : ndarray of shape (n_features,)
        F-statistic for each feature.

    p_values : ndarray of shape (n_features,)
        P-values associated with the F-statistic.

    See Also
    --------
    r_regression: Pearson's R between label/feature for regression tasks.
    f_classif: ANOVA F-value between label/feature for classification tasks.
    chi2: Chi-squared stats of non-negative features for classification tasks.
    SelectKBest: Select features based on the k highest scores.
    SelectFpr: Select features based on a false positive rate test.
    SelectFdr: Select features based on an estimated false discovery rate.
    SelectFwe: Select features based on family-wise error rate.
    SelectPercentile: Select features based on percentile of the highest
        scores.
    """

class _BaseFilter(SelectorMixin, BaseEstimator, metaclass=abc.ABCMeta):
    """Initialize the univariate feature selection.

    Parameters
    ----------
    score_func : callable
        Function taking two arrays X and y, and returning a pair of arrays
        (scores, pvalues) or a single array with scores.
    """
    score_func: Incomplete
    def __init__(self, score_func) -> None: ...
    pvalues_: Incomplete
    scores_: Incomplete
    def fit(self, X, y):
        """Run score function on (X, y) and get the appropriate features.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The training input samples.

        y : array-like of shape (n_samples,)
            The target values (class labels in classification, real numbers in
            regression).

        Returns
        -------
        self : object
            Returns the instance itself.
        """

class SelectPercentile(_BaseFilter):
    '''Select features according to a percentile of the highest scores.

    Read more in the :ref:`User Guide <univariate_feature_selection>`.

    Parameters
    ----------
    score_func : callable, default=f_classif
        Function taking two arrays X and y, and returning a pair of arrays
        (scores, pvalues) or a single array with scores.
        Default is f_classif (see below "See Also"). The default function only
        works with classification tasks.

        .. versionadded:: 0.18

    percentile : int, default=10
        Percent of features to keep.

    Attributes
    ----------
    scores_ : array-like of shape (n_features,)
        Scores of features.

    pvalues_ : array-like of shape (n_features,)
        p-values of feature scores, None if `score_func` returned only scores.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    f_classif : ANOVA F-value between label/feature for classification tasks.
    mutual_info_classif : Mutual information for a discrete target.
    chi2 : Chi-squared stats of non-negative features for classification tasks.
    f_regression : F-value between label/feature for regression tasks.
    mutual_info_regression : Mutual information for a continuous target.
    SelectKBest : Select features based on the k highest scores.
    SelectFpr : Select features based on a false positive rate test.
    SelectFdr : Select features based on an estimated false discovery rate.
    SelectFwe : Select features based on family-wise error rate.
    GenericUnivariateSelect : Univariate feature selector with configurable
        mode.

    Notes
    -----
    Ties between features with equal scores will be broken in an unspecified
    way.

    Examples
    --------
    >>> from sklearn.datasets import load_digits
    >>> from sklearn.feature_selection import SelectPercentile, chi2
    >>> X, y = load_digits(return_X_y=True)
    >>> X.shape
    (1797, 64)
    >>> X_new = SelectPercentile(chi2, percentile=10).fit_transform(X, y)
    >>> X_new.shape
    (1797, 7)
    '''
    percentile: Incomplete
    def __init__(self, score_func=..., *, percentile: int = 10) -> None: ...

class SelectKBest(_BaseFilter):
    '''Select features according to the k highest scores.

    Read more in the :ref:`User Guide <univariate_feature_selection>`.

    Parameters
    ----------
    score_func : callable, default=f_classif
        Function taking two arrays X and y, and returning a pair of arrays
        (scores, pvalues) or a single array with scores.
        Default is f_classif (see below "See Also"). The default function only
        works with classification tasks.

        .. versionadded:: 0.18

    k : int or "all", default=10
        Number of top features to select.
        The "all" option bypasses selection, for use in a parameter search.

    Attributes
    ----------
    scores_ : array-like of shape (n_features,)
        Scores of features.

    pvalues_ : array-like of shape (n_features,)
        p-values of feature scores, None if `score_func` returned only scores.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    f_classif: ANOVA F-value between label/feature for classification tasks.
    mutual_info_classif: Mutual information for a discrete target.
    chi2: Chi-squared stats of non-negative features for classification tasks.
    f_regression: F-value between label/feature for regression tasks.
    mutual_info_regression: Mutual information for a continuous target.
    SelectPercentile: Select features based on percentile of the highest
        scores.
    SelectFpr : Select features based on a false positive rate test.
    SelectFdr : Select features based on an estimated false discovery rate.
    SelectFwe : Select features based on family-wise error rate.
    GenericUnivariateSelect : Univariate feature selector with configurable
        mode.

    Notes
    -----
    Ties between features with equal scores will be broken in an unspecified
    way.

    Examples
    --------
    >>> from sklearn.datasets import load_digits
    >>> from sklearn.feature_selection import SelectKBest, chi2
    >>> X, y = load_digits(return_X_y=True)
    >>> X.shape
    (1797, 64)
    >>> X_new = SelectKBest(chi2, k=20).fit_transform(X, y)
    >>> X_new.shape
    (1797, 20)
    '''
    k: Incomplete
    def __init__(self, score_func=..., *, k: int = 10) -> None: ...

class SelectFpr(_BaseFilter):
    '''Filter: Select the pvalues below alpha based on a FPR test.

    FPR test stands for False Positive Rate test. It controls the total
    amount of false detections.

    Read more in the :ref:`User Guide <univariate_feature_selection>`.

    Parameters
    ----------
    score_func : callable, default=f_classif
        Function taking two arrays X and y, and returning a pair of arrays
        (scores, pvalues).
        Default is f_classif (see below "See Also"). The default function only
        works with classification tasks.

    alpha : float, default=5e-2
        Features with p-values less than `alpha` are selected.

    Attributes
    ----------
    scores_ : array-like of shape (n_features,)
        Scores of features.

    pvalues_ : array-like of shape (n_features,)
        p-values of feature scores.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    f_classif : ANOVA F-value between label/feature for classification tasks.
    chi2 : Chi-squared stats of non-negative features for classification tasks.
    mutual_info_classif: Mutual information for a discrete target.
    f_regression : F-value between label/feature for regression tasks.
    mutual_info_regression : Mutual information for a continuous target.
    SelectPercentile : Select features based on percentile of the highest
        scores.
    SelectKBest : Select features based on the k highest scores.
    SelectFdr : Select features based on an estimated false discovery rate.
    SelectFwe : Select features based on family-wise error rate.
    GenericUnivariateSelect : Univariate feature selector with configurable
        mode.

    Examples
    --------
    >>> from sklearn.datasets import load_breast_cancer
    >>> from sklearn.feature_selection import SelectFpr, chi2
    >>> X, y = load_breast_cancer(return_X_y=True)
    >>> X.shape
    (569, 30)
    >>> X_new = SelectFpr(chi2, alpha=0.01).fit_transform(X, y)
    >>> X_new.shape
    (569, 16)
    '''
    alpha: Incomplete
    def __init__(self, score_func=..., *, alpha: float = 0.05) -> None: ...

class SelectFdr(_BaseFilter):
    '''Filter: Select the p-values for an estimated false discovery rate.

    This uses the Benjamini-Hochberg procedure. ``alpha`` is an upper bound
    on the expected false discovery rate.

    Read more in the :ref:`User Guide <univariate_feature_selection>`.

    Parameters
    ----------
    score_func : callable, default=f_classif
        Function taking two arrays X and y, and returning a pair of arrays
        (scores, pvalues).
        Default is f_classif (see below "See Also"). The default function only
        works with classification tasks.

    alpha : float, default=5e-2
        The highest uncorrected p-value for features to keep.

    Attributes
    ----------
    scores_ : array-like of shape (n_features,)
        Scores of features.

    pvalues_ : array-like of shape (n_features,)
        p-values of feature scores.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    f_classif : ANOVA F-value between label/feature for classification tasks.
    mutual_info_classif : Mutual information for a discrete target.
    chi2 : Chi-squared stats of non-negative features for classification tasks.
    f_regression : F-value between label/feature for regression tasks.
    mutual_info_regression : Mutual information for a continuous target.
    SelectPercentile : Select features based on percentile of the highest
        scores.
    SelectKBest : Select features based on the k highest scores.
    SelectFpr : Select features based on a false positive rate test.
    SelectFwe : Select features based on family-wise error rate.
    GenericUnivariateSelect : Univariate feature selector with configurable
        mode.

    References
    ----------
    https://en.wikipedia.org/wiki/False_discovery_rate

    Examples
    --------
    >>> from sklearn.datasets import load_breast_cancer
    >>> from sklearn.feature_selection import SelectFdr, chi2
    >>> X, y = load_breast_cancer(return_X_y=True)
    >>> X.shape
    (569, 30)
    >>> X_new = SelectFdr(chi2, alpha=0.01).fit_transform(X, y)
    >>> X_new.shape
    (569, 16)
    '''
    alpha: Incomplete
    def __init__(self, score_func=..., *, alpha: float = 0.05) -> None: ...

class SelectFwe(_BaseFilter):
    '''Filter: Select the p-values corresponding to Family-wise error rate.

    Read more in the :ref:`User Guide <univariate_feature_selection>`.

    Parameters
    ----------
    score_func : callable, default=f_classif
        Function taking two arrays X and y, and returning a pair of arrays
        (scores, pvalues).
        Default is f_classif (see below "See Also"). The default function only
        works with classification tasks.

    alpha : float, default=5e-2
        The highest uncorrected p-value for features to keep.

    Attributes
    ----------
    scores_ : array-like of shape (n_features,)
        Scores of features.

    pvalues_ : array-like of shape (n_features,)
        p-values of feature scores.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    f_classif : ANOVA F-value between label/feature for classification tasks.
    chi2 : Chi-squared stats of non-negative features for classification tasks.
    f_regression : F-value between label/feature for regression tasks.
    SelectPercentile : Select features based on percentile of the highest
        scores.
    SelectKBest : Select features based on the k highest scores.
    SelectFpr : Select features based on a false positive rate test.
    SelectFdr : Select features based on an estimated false discovery rate.
    GenericUnivariateSelect : Univariate feature selector with configurable
        mode.

    Examples
    --------
    >>> from sklearn.datasets import load_breast_cancer
    >>> from sklearn.feature_selection import SelectFwe, chi2
    >>> X, y = load_breast_cancer(return_X_y=True)
    >>> X.shape
    (569, 30)
    >>> X_new = SelectFwe(chi2, alpha=0.01).fit_transform(X, y)
    >>> X_new.shape
    (569, 15)
    '''
    alpha: Incomplete
    def __init__(self, score_func=..., *, alpha: float = 0.05) -> None: ...

class GenericUnivariateSelect(_BaseFilter):
    '''Univariate feature selector with configurable strategy.

    Read more in the :ref:`User Guide <univariate_feature_selection>`.

    Parameters
    ----------
    score_func : callable, default=f_classif
        Function taking two arrays X and y, and returning a pair of arrays
        (scores, pvalues). For modes \'percentile\' or \'kbest\' it can return
        a single array scores.

    mode : {\'percentile\', \'k_best\', \'fpr\', \'fdr\', \'fwe\'}, default=\'percentile\'
        Feature selection mode.

    param : "all", float or int, default=1e-5
        Parameter of the corresponding mode.

    Attributes
    ----------
    scores_ : array-like of shape (n_features,)
        Scores of features.

    pvalues_ : array-like of shape (n_features,)
        p-values of feature scores, None if `score_func` returned scores only.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    f_classif : ANOVA F-value between label/feature for classification tasks.
    mutual_info_classif : Mutual information for a discrete target.
    chi2 : Chi-squared stats of non-negative features for classification tasks.
    f_regression : F-value between label/feature for regression tasks.
    mutual_info_regression : Mutual information for a continuous target.
    SelectPercentile : Select features based on percentile of the highest
        scores.
    SelectKBest : Select features based on the k highest scores.
    SelectFpr : Select features based on a false positive rate test.
    SelectFdr : Select features based on an estimated false discovery rate.
    SelectFwe : Select features based on family-wise error rate.

    Examples
    --------
    >>> from sklearn.datasets import load_breast_cancer
    >>> from sklearn.feature_selection import GenericUnivariateSelect, chi2
    >>> X, y = load_breast_cancer(return_X_y=True)
    >>> X.shape
    (569, 30)
    >>> transformer = GenericUnivariateSelect(chi2, mode=\'k_best\', param=20)
    >>> X_new = transformer.fit_transform(X, y)
    >>> X_new.shape
    (569, 20)
    '''
    mode: Incomplete
    param: Incomplete
    def __init__(self, score_func=..., *, mode: str = 'percentile', param: float = 1e-05) -> None: ...
