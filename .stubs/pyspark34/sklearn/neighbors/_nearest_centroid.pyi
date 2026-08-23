from ..base import BaseEstimator as BaseEstimator, ClassifierMixin as ClassifierMixin
from ..metrics.pairwise import pairwise_distances_argmin as pairwise_distances_argmin
from ..preprocessing import LabelEncoder as LabelEncoder
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.sparsefuncs import csc_median_axis_0 as csc_median_axis_0
from ..utils.validation import check_is_fitted as check_is_fitted
from _typeshed import Incomplete

class NearestCentroid(ClassifierMixin, BaseEstimator):
    '''Nearest centroid classifier.

    Each class is represented by its centroid, with test samples classified to
    the class with the nearest centroid.

    Read more in the :ref:`User Guide <nearest_centroid_classifier>`.

    Parameters
    ----------
    metric : str or callable, default="euclidean"
        Metric to use for distance computation. See the documentation of
        `scipy.spatial.distance
        <https://docs.scipy.org/doc/scipy/reference/spatial.distance.html>`_ and
        the metrics listed in
        :class:`~sklearn.metrics.pairwise.distance_metrics` for valid metric
        values. Note that "wminkowski", "seuclidean" and "mahalanobis" are not
        supported.

        The centroids for the samples corresponding to each class is
        the point from which the sum of the distances (according to the metric)
        of all samples that belong to that particular class are minimized.
        If the `"manhattan"` metric is provided, this centroid is the median
        and for all other metrics, the centroid is now set to be the mean.

        .. deprecated:: 1.3
            Support for metrics other than `euclidean` and `manhattan` and for
            callables was deprecated in version 1.3 and will be removed in
            version 1.5.

        .. versionchanged:: 0.19
            `metric=\'precomputed\'` was deprecated and now raises an error

    shrink_threshold : float, default=None
        Threshold for shrinking centroids to remove features.

    Attributes
    ----------
    centroids_ : array-like of shape (n_classes, n_features)
        Centroid of each class.

    classes_ : array of shape (n_classes,)
        The unique classes labels.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    KNeighborsClassifier : Nearest neighbors classifier.

    Notes
    -----
    When used for text classification with tf-idf vectors, this classifier is
    also known as the Rocchio classifier.

    References
    ----------
    Tibshirani, R., Hastie, T., Narasimhan, B., & Chu, G. (2002). Diagnosis of
    multiple cancer types by shrunken centroids of gene expression. Proceedings
    of the National Academy of Sciences of the United States of America,
    99(10), 6567-6572. The National Academy of Sciences.

    Examples
    --------
    >>> from sklearn.neighbors import NearestCentroid
    >>> import numpy as np
    >>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    >>> y = np.array([1, 1, 1, 2, 2, 2])
    >>> clf = NearestCentroid()
    >>> clf.fit(X, y)
    NearestCentroid()
    >>> print(clf.predict([[-0.8, -1]]))
    [1]
    '''
    metric: Incomplete
    shrink_threshold: Incomplete
    def __init__(self, metric: str = 'euclidean', *, shrink_threshold: Incomplete | None = None) -> None: ...
    classes_: Incomplete
    centroids_: Incomplete
    def fit(self, X, y):
        """
        Fit the NearestCentroid model according to the given training data.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Training vector, where `n_samples` is the number of samples and
            `n_features` is the number of features.
            Note that centroid shrinking cannot be used with sparse matrices.
        y : array-like of shape (n_samples,)
            Target values.

        Returns
        -------
        self : object
            Fitted estimator.
        """
    def predict(self, X):
        '''Perform classification on an array of test vectors `X`.

        The predicted class `C` for each sample in `X` is returned.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Test samples.

        Returns
        -------
        C : ndarray of shape (n_samples,)
            The predicted classes.

        Notes
        -----
        If the metric constructor parameter is `"precomputed"`, `X` is assumed
        to be the distance matrix between the data to be predicted and
        `self.centroids_`.
        '''
