from ..dummy import DummyClassifier as DummyClassifier, DummyRegressor as DummyRegressor
from ..tree._tree import TREE_LEAF as TREE_LEAF
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod

class LossFunction(metaclass=ABCMeta):
    """Abstract base class for various loss functions.

    Parameters
    ----------
    n_classes : int
        Number of classes.

    Attributes
    ----------
    K : int
        The number of regression trees to be induced;
        1 for regression and binary classification;
        ``n_classes`` for multi-class classification.
    """
    is_multi_class: bool
    K: Incomplete
    def __init__(self, n_classes) -> None: ...
    @abstractmethod
    def init_estimator(self):
        """Default ``init`` estimator for loss function."""
    @abstractmethod
    def __call__(self, y, raw_predictions, sample_weight: Incomplete | None = None):
        """Compute the loss.

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            True labels.

        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves).

        sample_weight : ndarray of shape (n_samples,), default=None
            Sample weights.
        """
    @abstractmethod
    def negative_gradient(self, y, raw_predictions, **kargs):
        """Compute the negative gradient.

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            The target labels.

        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves) of the
            tree ensemble at iteration ``i - 1``.
        """
    def update_terminal_regions(self, tree, X, y, residual, raw_predictions, sample_weight, sample_mask, learning_rate: float = 0.1, k: int = 0) -> None:
        """Update the terminal regions (=leaves) of the given tree and
        updates the current predictions of the model. Traverses tree
        and invokes template method `_update_terminal_region`.

        Parameters
        ----------
        tree : tree.Tree
            The tree object.
        X : ndarray of shape (n_samples, n_features)
            The data array.
        y : ndarray of shape (n_samples,)
            The target labels.
        residual : ndarray of shape (n_samples,)
            The residuals (usually the negative gradient).
        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves) of the
            tree ensemble at iteration ``i - 1``.
        sample_weight : ndarray of shape (n_samples,)
            The weight of each sample.
        sample_mask : ndarray of shape (n_samples,)
            The sample mask to be used.
        learning_rate : float, default=0.1
            Learning rate shrinks the contribution of each tree by
             ``learning_rate``.
        k : int, default=0
            The index of the estimator being updated.

        """
    @abstractmethod
    def get_init_raw_predictions(self, X, estimator):
        """Return the initial raw predictions.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            The data array.
        estimator : object
            The estimator to use to compute the predictions.

        Returns
        -------
        raw_predictions : ndarray of shape (n_samples, K)
            The initial raw predictions. K is equal to 1 for binary
            classification and regression, and equal to the number of classes
            for multiclass classification. ``raw_predictions`` is casted
            into float64.
        """

class RegressionLossFunction(LossFunction, metaclass=ABCMeta):
    """Base class for regression loss functions."""
    def __init__(self) -> None: ...
    def check_init_estimator(self, estimator) -> None:
        """Make sure estimator has the required fit and predict methods.

        Parameters
        ----------
        estimator : object
            The init estimator to check.
        """
    def get_init_raw_predictions(self, X, estimator): ...

class LeastSquaresError(RegressionLossFunction):
    """Loss function for least squares (LS) estimation.
    Terminal regions do not need to be updated for least squares.

    Parameters
    ----------
    n_classes : int
        Number of classes.
    """
    def init_estimator(self): ...
    def __call__(self, y, raw_predictions, sample_weight: Incomplete | None = None):
        """Compute the least squares loss.

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            True labels.

        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves).

        sample_weight : ndarray of shape (n_samples,), default=None
            Sample weights.
        """
    def negative_gradient(self, y, raw_predictions, **kargs):
        """Compute half of the negative gradient.

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            The target labels.

        raw_predictions : ndarray of shape (n_samples,)
            The raw predictions (i.e. values from the tree leaves) of the
            tree ensemble at iteration ``i - 1``.
        """
    def update_terminal_regions(self, tree, X, y, residual, raw_predictions, sample_weight, sample_mask, learning_rate: float = 0.1, k: int = 0) -> None:
        """Least squares does not need to update terminal regions.

        But it has to update the predictions.

        Parameters
        ----------
        tree : tree.Tree
            The tree object.
        X : ndarray of shape (n_samples, n_features)
            The data array.
        y : ndarray of shape (n_samples,)
            The target labels.
        residual : ndarray of shape (n_samples,)
            The residuals (usually the negative gradient).
        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves) of the
            tree ensemble at iteration ``i - 1``.
        sample_weight : ndarray of shape (n,)
            The weight of each sample.
        sample_mask : ndarray of shape (n,)
            The sample mask to be used.
        learning_rate : float, default=0.1
            Learning rate shrinks the contribution of each tree by
             ``learning_rate``.
        k : int, default=0
            The index of the estimator being updated.
        """

class LeastAbsoluteError(RegressionLossFunction):
    """Loss function for least absolute deviation (LAD) regression.

    Parameters
    ----------
    n_classes : int
        Number of classes
    """
    def init_estimator(self): ...
    def __call__(self, y, raw_predictions, sample_weight: Incomplete | None = None):
        """Compute the least absolute error.

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            True labels.

        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves).

        sample_weight : ndarray of shape (n_samples,), default=None
            Sample weights.
        """
    def negative_gradient(self, y, raw_predictions, **kargs):
        """Compute the negative gradient.

        1.0 if y - raw_predictions > 0.0 else -1.0

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            The target labels.

        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves) of the
            tree ensemble at iteration ``i - 1``.
        """

class HuberLossFunction(RegressionLossFunction):
    """Huber loss function for robust regression.

    M-Regression proposed in Friedman 2001.

    Parameters
    ----------
    alpha : float, default=0.9
        Percentile at which to extract score.

    References
    ----------
    J. Friedman, Greedy Function Approximation: A Gradient Boosting
    Machine, The Annals of Statistics, Vol. 29, No. 5, 2001.
    """
    alpha: Incomplete
    gamma: Incomplete
    def __init__(self, alpha: float = 0.9) -> None: ...
    def init_estimator(self): ...
    def __call__(self, y, raw_predictions, sample_weight: Incomplete | None = None):
        """Compute the Huber loss.

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            True labels.

        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves) of the
            tree ensemble.

        sample_weight : ndarray of shape (n_samples,), default=None
            Sample weights.
        """
    def negative_gradient(self, y, raw_predictions, sample_weight: Incomplete | None = None, **kargs):
        """Compute the negative gradient.

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            The target labels.

        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves) of the
            tree ensemble at iteration ``i - 1``.

        sample_weight : ndarray of shape (n_samples,), default=None
            Sample weights.
        """

class QuantileLossFunction(RegressionLossFunction):
    """Loss function for quantile regression.

    Quantile regression allows to estimate the percentiles
    of the conditional distribution of the target.

    Parameters
    ----------
    alpha : float, default=0.9
        The percentile.
    """
    alpha: Incomplete
    percentile: Incomplete
    def __init__(self, alpha: float = 0.9) -> None: ...
    def init_estimator(self): ...
    def __call__(self, y, raw_predictions, sample_weight: Incomplete | None = None):
        """Compute the Quantile loss.

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            True labels.

        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves) of the
            tree ensemble.

        sample_weight : ndarray of shape (n_samples,), default=None
            Sample weights.
        """
    def negative_gradient(self, y, raw_predictions, **kargs):
        """Compute the negative gradient.

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            The target labels.

        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves) of the
            tree ensemble at iteration ``i - 1``.
        """

class ClassificationLossFunction(LossFunction, metaclass=ABCMeta):
    """Base class for classification loss functions."""
    def check_init_estimator(self, estimator) -> None:
        """Make sure estimator has fit and predict_proba methods.

        Parameters
        ----------
        estimator : object
            The init estimator to check.
        """

class BinomialDeviance(ClassificationLossFunction):
    """Binomial deviance loss function for binary classification.

    Binary classification is a special case; here, we only need to
    fit one tree instead of ``n_classes`` trees.

    Parameters
    ----------
    n_classes : int
        Number of classes.
    """
    def __init__(self, n_classes) -> None: ...
    def init_estimator(self): ...
    def __call__(self, y, raw_predictions, sample_weight: Incomplete | None = None):
        """Compute the deviance (= 2 * negative log-likelihood).

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            True labels.

        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves) of the
            tree ensemble.

        sample_weight : ndarray of shape (n_samples,), default=None
            Sample weights.
        """
    def negative_gradient(self, y, raw_predictions, **kargs):
        """Compute half of the negative gradient.

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            True labels.

        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves) of the
            tree ensemble at iteration ``i - 1``.
        """
    def get_init_raw_predictions(self, X, estimator): ...

class MultinomialDeviance(ClassificationLossFunction):
    """Multinomial deviance loss function for multi-class classification.

    For multi-class classification we need to fit ``n_classes`` trees at
    each stage.

    Parameters
    ----------
    n_classes : int
        Number of classes.
    """
    is_multi_class: bool
    def __init__(self, n_classes) -> None: ...
    def init_estimator(self): ...
    def __call__(self, y, raw_predictions, sample_weight: Incomplete | None = None):
        """Compute the Multinomial deviance.

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            True labels.

        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves) of the
            tree ensemble.

        sample_weight : ndarray of shape (n_samples,), default=None
            Sample weights.
        """
    def negative_gradient(self, y, raw_predictions, k: int = 0, **kwargs):
        """Compute negative gradient for the ``k``-th class.

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            The target labels.

        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves) of the
            tree ensemble at iteration ``i - 1``.

        k : int, default=0
            The index of the class.
        """
    def get_init_raw_predictions(self, X, estimator): ...

class ExponentialLoss(ClassificationLossFunction):
    """Exponential loss function for binary classification.

    Same loss as AdaBoost.

    Parameters
    ----------
    n_classes : int
        Number of classes.

    References
    ----------
    Greg Ridgeway, Generalized Boosted Models: A guide to the gbm package, 2007
    """
    def __init__(self, n_classes) -> None: ...
    def init_estimator(self): ...
    def __call__(self, y, raw_predictions, sample_weight: Incomplete | None = None):
        """Compute the exponential loss

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            True labels.

        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves) of the
            tree ensemble.

        sample_weight : ndarray of shape (n_samples,), default=None
            Sample weights.
        """
    def negative_gradient(self, y, raw_predictions, **kargs):
        """Compute the residual (= negative gradient).

        Parameters
        ----------
        y : ndarray of shape (n_samples,)
            True labels.

        raw_predictions : ndarray of shape (n_samples, K)
            The raw predictions (i.e. values from the tree leaves) of the
            tree ensemble at iteration ``i - 1``.
        """
    def get_init_raw_predictions(self, X, estimator): ...

LOSS_FUNCTIONS: Incomplete
