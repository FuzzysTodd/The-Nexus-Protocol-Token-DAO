from ..base import BaseEstimator as BaseEstimator, ClassifierMixin as ClassifierMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..metrics.pairwise import rbf_kernel as rbf_kernel
from ..neighbors import NearestNeighbors as NearestNeighbors
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.validation import check_is_fitted as check_is_fitted
from _typeshed import Incomplete
from abc import ABCMeta

class BaseLabelPropagation(ClassifierMixin, BaseEstimator, metaclass=ABCMeta):
    """Base class for label propagation module.

     Parameters
     ----------
     kernel : {'knn', 'rbf'} or callable, default='rbf'
         String identifier for kernel function to use or the kernel function
         itself. Only 'rbf' and 'knn' strings are valid inputs. The function
         passed should take two inputs, each of shape (n_samples, n_features),
         and return a (n_samples, n_samples) shaped weight matrix.

     gamma : float, default=20
         Parameter for rbf kernel.

     n_neighbors : int, default=7
         Parameter for knn kernel. Need to be strictly positive.

     alpha : float, default=1.0
         Clamping factor.

     max_iter : int, default=30
         Change maximum number of iterations allowed.

     tol : float, default=1e-3
         Convergence tolerance: threshold to consider the system at steady
         state.

    n_jobs : int, default=None
         The number of parallel jobs to run.
         ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
         ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
         for more details.
    """
    max_iter: Incomplete
    tol: Incomplete
    kernel: Incomplete
    gamma: Incomplete
    n_neighbors: Incomplete
    alpha: Incomplete
    n_jobs: Incomplete
    def __init__(self, kernel: str = 'rbf', *, gamma: int = 20, n_neighbors: int = 7, alpha: int = 1, max_iter: int = 30, tol: float = 0.001, n_jobs: Incomplete | None = None) -> None: ...
    def predict(self, X):
        """Perform inductive inference across the model.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The data matrix.

        Returns
        -------
        y : ndarray of shape (n_samples,)
            Predictions for input data.
        """
    def predict_proba(self, X):
        """Predict probability for each possible outcome.

        Compute the probability estimates for each single sample in X
        and each possible outcome seen during training (categorical
        distribution).

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The data matrix.

        Returns
        -------
        probabilities : ndarray of shape (n_samples, n_classes)
            Normalized probability distributions across
            class labels.
        """
    X_: Incomplete
    classes_: Incomplete
    label_distributions_: Incomplete
    transduction_: Incomplete
    def fit(self, X, y):
        """Fit a semi-supervised label propagation model to X.

        The input samples (labeled and unlabeled) are provided by matrix X,
        and target labels are provided by matrix y. We conventionally apply the
        label -1 to unlabeled samples in matrix y in a semi-supervised
        classification.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Training data, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : array-like of shape (n_samples,)
            Target class values with unlabeled points marked as -1.
            All unlabeled samples will be transductively assigned labels
            internally, which are stored in `transduction_`.

        Returns
        -------
        self : object
            Returns the instance itself.
        """

class LabelPropagation(BaseLabelPropagation):
    """Label Propagation classifier.

    Read more in the :ref:`User Guide <label_propagation>`.

    Parameters
    ----------
    kernel : {'knn', 'rbf'} or callable, default='rbf'
        String identifier for kernel function to use or the kernel function
        itself. Only 'rbf' and 'knn' strings are valid inputs. The function
        passed should take two inputs, each of shape (n_samples, n_features),
        and return a (n_samples, n_samples) shaped weight matrix.

    gamma : float, default=20
        Parameter for rbf kernel.

    n_neighbors : int, default=7
        Parameter for knn kernel which need to be strictly positive.

    max_iter : int, default=1000
        Change maximum number of iterations allowed.

    tol : float, 1e-3
        Convergence tolerance: threshold to consider the system at steady
        state.

    n_jobs : int, default=None
        The number of parallel jobs to run.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    Attributes
    ----------
    X_ : {array-like, sparse matrix} of shape (n_samples, n_features)
        Input array.

    classes_ : ndarray of shape (n_classes,)
        The distinct labels used in classifying instances.

    label_distributions_ : ndarray of shape (n_samples, n_classes)
        Categorical distribution for each item.

    transduction_ : ndarray of shape (n_samples)
        Label assigned to each item during :term:`fit`.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    n_iter_ : int
        Number of iterations run.

    See Also
    --------
    BaseLabelPropagation : Base class for label propagation module.
    LabelSpreading : Alternate label propagation strategy more robust to noise.

    References
    ----------
    Xiaojin Zhu and Zoubin Ghahramani. Learning from labeled and unlabeled data
    with label propagation. Technical Report CMU-CALD-02-107, Carnegie Mellon
    University, 2002 http://pages.cs.wisc.edu/~jerryzhu/pub/CMU-CALD-02-107.pdf

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn import datasets
    >>> from sklearn.semi_supervised import LabelPropagation
    >>> label_prop_model = LabelPropagation()
    >>> iris = datasets.load_iris()
    >>> rng = np.random.RandomState(42)
    >>> random_unlabeled_points = rng.rand(len(iris.target)) < 0.3
    >>> labels = np.copy(iris.target)
    >>> labels[random_unlabeled_points] = -1
    >>> label_prop_model.fit(iris.data, labels)
    LabelPropagation(...)
    """
    def __init__(self, kernel: str = 'rbf', *, gamma: int = 20, n_neighbors: int = 7, max_iter: int = 1000, tol: float = 0.001, n_jobs: Incomplete | None = None) -> None: ...
    def fit(self, X, y):
        """Fit a semi-supervised label propagation model to X.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Training data, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : array-like of shape (n_samples,)
            Target class values with unlabeled points marked as -1.
            All unlabeled samples will be transductively assigned labels
            internally, which are stored in `transduction_`.

        Returns
        -------
        self : object
            Returns the instance itself.
        """

class LabelSpreading(BaseLabelPropagation):
    """LabelSpreading model for semi-supervised learning.

    This model is similar to the basic Label Propagation algorithm,
    but uses affinity matrix based on the normalized graph Laplacian
    and soft clamping across the labels.

    Read more in the :ref:`User Guide <label_propagation>`.

    Parameters
    ----------
    kernel : {'knn', 'rbf'} or callable, default='rbf'
        String identifier for kernel function to use or the kernel function
        itself. Only 'rbf' and 'knn' strings are valid inputs. The function
        passed should take two inputs, each of shape (n_samples, n_features),
        and return a (n_samples, n_samples) shaped weight matrix.

    gamma : float, default=20
      Parameter for rbf kernel.

    n_neighbors : int, default=7
      Parameter for knn kernel which is a strictly positive integer.

    alpha : float, default=0.2
      Clamping factor. A value in (0, 1) that specifies the relative amount
      that an instance should adopt the information from its neighbors as
      opposed to its initial label.
      alpha=0 means keeping the initial label information; alpha=1 means
      replacing all initial information.

    max_iter : int, default=30
      Maximum number of iterations allowed.

    tol : float, default=1e-3
      Convergence tolerance: threshold to consider the system at steady
      state.

    n_jobs : int, default=None
        The number of parallel jobs to run.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    Attributes
    ----------
    X_ : ndarray of shape (n_samples, n_features)
        Input array.

    classes_ : ndarray of shape (n_classes,)
        The distinct labels used in classifying instances.

    label_distributions_ : ndarray of shape (n_samples, n_classes)
        Categorical distribution for each item.

    transduction_ : ndarray of shape (n_samples,)
        Label assigned to each item during :term:`fit`.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    n_iter_ : int
        Number of iterations run.

    See Also
    --------
    LabelPropagation : Unregularized graph based semi-supervised learning.

    References
    ----------
    `Dengyong Zhou, Olivier Bousquet, Thomas Navin Lal, Jason Weston,
    Bernhard Schoelkopf. Learning with local and global consistency (2004)
    <https://citeseerx.ist.psu.edu/doc_view/pid/d74c37aabf2d5cae663007cbd8718175466aea8c>`_

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn import datasets
    >>> from sklearn.semi_supervised import LabelSpreading
    >>> label_prop_model = LabelSpreading()
    >>> iris = datasets.load_iris()
    >>> rng = np.random.RandomState(42)
    >>> random_unlabeled_points = rng.rand(len(iris.target)) < 0.3
    >>> labels = np.copy(iris.target)
    >>> labels[random_unlabeled_points] = -1
    >>> label_prop_model.fit(iris.data, labels)
    LabelSpreading(...)
    """
    def __init__(self, kernel: str = 'rbf', *, gamma: int = 20, n_neighbors: int = 7, alpha: float = 0.2, max_iter: int = 30, tol: float = 0.001, n_jobs: Incomplete | None = None) -> None: ...
