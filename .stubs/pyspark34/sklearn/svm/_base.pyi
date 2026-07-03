from ..base import BaseEstimator as BaseEstimator, ClassifierMixin as ClassifierMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning, NotFittedError as NotFittedError
from ..preprocessing import LabelEncoder as LabelEncoder
from ..utils import check_array as check_array, check_random_state as check_random_state, column_or_1d as column_or_1d, compute_class_weight as compute_class_weight
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..utils.metaestimators import available_if as available_if
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.validation import check_consistent_length as check_consistent_length, check_is_fitted as check_is_fitted
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod

LIBSVM_IMPL: Incomplete

class BaseLibSVM(BaseEstimator, metaclass=ABCMeta):
    """Base class for estimators that use libsvm as backing library.

    This implements support vector machine classification and regression.

    Parameter documentation is in the derived `SVC` class.
    """
    kernel: Incomplete
    degree: Incomplete
    gamma: Incomplete
    coef0: Incomplete
    tol: Incomplete
    C: Incomplete
    nu: Incomplete
    epsilon: Incomplete
    shrinking: Incomplete
    probability: Incomplete
    cache_size: Incomplete
    class_weight: Incomplete
    verbose: Incomplete
    max_iter: Incomplete
    random_state: Incomplete
    @abstractmethod
    def __init__(self, kernel, degree, gamma, coef0, tol, C, nu, epsilon, shrinking, probability, cache_size, class_weight, verbose, max_iter, random_state): ...
    shape_fit_: Incomplete
    dual_coef_: Incomplete
    n_iter_: Incomplete
    def fit(self, X, y, sample_weight: Incomplete | None = None):
        '''Fit the SVM model according to the given training data.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)                 or (n_samples, n_samples)
            Training vectors, where `n_samples` is the number of samples
            and `n_features` is the number of features.
            For kernel="precomputed", the expected shape of X is
            (n_samples, n_samples).

        y : array-like of shape (n_samples,)
            Target values (class labels in classification, real numbers in
            regression).

        sample_weight : array-like of shape (n_samples,), default=None
            Per-sample weights. Rescale C per sample. Higher weights
            force the classifier to put more emphasis on these points.

        Returns
        -------
        self : object
            Fitted estimator.

        Notes
        -----
        If X and y are not C-ordered and contiguous arrays of np.float64 and
        X is not a scipy.sparse.csr_matrix, X and/or y may be copied.

        If X is a dense array, then the other methods will not support sparse
        matrices as input.
        '''
    def predict(self, X):
        '''Perform regression on samples in X.

        For an one-class model, +1 (inlier) or -1 (outlier) is returned.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            For kernel="precomputed", the expected shape of X is
            (n_samples_test, n_samples_train).

        Returns
        -------
        y_pred : ndarray of shape (n_samples,)
            The predicted values.
        '''
    @property
    def coef_(self):
        '''Weights assigned to the features when `kernel="linear"`.

        Returns
        -------
        ndarray of shape (n_features, n_classes)
        '''
    @property
    def n_support_(self):
        """Number of support vectors for each class."""

class BaseSVC(ClassifierMixin, BaseLibSVM, metaclass=ABCMeta):
    """ABC for LibSVM-based classifiers."""
    decision_function_shape: Incomplete
    break_ties: Incomplete
    @abstractmethod
    def __init__(self, kernel, degree, gamma, coef0, tol, C, nu, shrinking, probability, cache_size, class_weight, verbose, max_iter, decision_function_shape, random_state, break_ties): ...
    def decision_function(self, X):
        """Evaluate the decision function for the samples in X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input samples.

        Returns
        -------
        X : ndarray of shape (n_samples, n_classes * (n_classes-1) / 2)
            Returns the decision function of the sample for each class
            in the model.
            If decision_function_shape='ovr', the shape is (n_samples,
            n_classes).

        Notes
        -----
        If decision_function_shape='ovo', the function values are proportional
        to the distance of the samples X to the separating hyperplane. If the
        exact distances are required, divide the function values by the norm of
        the weight vector (``coef_``). See also `this question
        <https://stats.stackexchange.com/questions/14876/
        interpreting-distance-from-hyperplane-in-svm>`_ for further details.
        If decision_function_shape='ovr', the decision function is a monotonic
        transformation of ovo decision function.
        """
    def predict(self, X):
        '''Perform classification on samples in X.

        For an one-class model, +1 or -1 is returned.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features) or                 (n_samples_test, n_samples_train)
            For kernel="precomputed", the expected shape of X is
            (n_samples_test, n_samples_train).

        Returns
        -------
        y_pred : ndarray of shape (n_samples,)
            Class labels for samples in X.
        '''
    def predict_proba(self, X):
        '''Compute probabilities of possible outcomes for samples in X.

        The model need to have probability information computed at training
        time: fit with attribute `probability` set to True.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            For kernel="precomputed", the expected shape of X is
            (n_samples_test, n_samples_train).

        Returns
        -------
        T : ndarray of shape (n_samples, n_classes)
            Returns the probability of the sample for each class in
            the model. The columns correspond to the classes in sorted
            order, as they appear in the attribute :term:`classes_`.

        Notes
        -----
        The probability model is created using cross validation, so
        the results can be slightly different than those obtained by
        predict. Also, it will produce meaningless results on very small
        datasets.
        '''
    def predict_log_proba(self, X):
        '''Compute log probabilities of possible outcomes for samples in X.

        The model need to have probability information computed at training
        time: fit with attribute `probability` set to True.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features) or                 (n_samples_test, n_samples_train)
            For kernel="precomputed", the expected shape of X is
            (n_samples_test, n_samples_train).

        Returns
        -------
        T : ndarray of shape (n_samples, n_classes)
            Returns the log-probabilities of the sample for each class in
            the model. The columns correspond to the classes in sorted
            order, as they appear in the attribute :term:`classes_`.

        Notes
        -----
        The probability model is created using cross validation, so
        the results can be slightly different than those obtained by
        predict. Also, it will produce meaningless results on very small
        datasets.
        '''
    @property
    def probA_(self):
        """Parameter learned in Platt scaling when `probability=True`.

        Returns
        -------
        ndarray of shape  (n_classes * (n_classes - 1) / 2)
        """
    @property
    def probB_(self):
        """Parameter learned in Platt scaling when `probability=True`.

        Returns
        -------
        ndarray of shape  (n_classes * (n_classes - 1) / 2)
        """
