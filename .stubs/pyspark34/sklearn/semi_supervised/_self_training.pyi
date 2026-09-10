from ..base import BaseEstimator, MetaEstimatorMixin
from _typeshed import Incomplete

__all__ = ['SelfTrainingClassifier']

class SelfTrainingClassifier(MetaEstimatorMixin, BaseEstimator):
    '''Self-training classifier.

    This :term:`metaestimator` allows a given supervised classifier to function as a
    semi-supervised classifier, allowing it to learn from unlabeled data. It
    does this by iteratively predicting pseudo-labels for the unlabeled data
    and adding them to the training set.

    The classifier will continue iterating until either max_iter is reached, or
    no pseudo-labels were added to the training set in the previous iteration.

    Read more in the :ref:`User Guide <self_training>`.

    Parameters
    ----------
    base_estimator : estimator object
        An estimator object implementing `fit` and `predict_proba`.
        Invoking the `fit` method will fit a clone of the passed estimator,
        which will be stored in the `base_estimator_` attribute.

    threshold : float, default=0.75
        The decision threshold for use with `criterion=\'threshold\'`.
        Should be in [0, 1). When using the `\'threshold\'` criterion, a
        :ref:`well calibrated classifier <calibration>` should be used.

    criterion : {\'threshold\', \'k_best\'}, default=\'threshold\'
        The selection criterion used to select which labels to add to the
        training set. If `\'threshold\'`, pseudo-labels with prediction
        probabilities above `threshold` are added to the dataset. If `\'k_best\'`,
        the `k_best` pseudo-labels with highest prediction probabilities are
        added to the dataset. When using the \'threshold\' criterion, a
        :ref:`well calibrated classifier <calibration>` should be used.

    k_best : int, default=10
        The amount of samples to add in each iteration. Only used when
        `criterion=\'k_best\'`.

    max_iter : int or None, default=10
        Maximum number of iterations allowed. Should be greater than or equal
        to 0. If it is `None`, the classifier will continue to predict labels
        until no new pseudo-labels are added, or all unlabeled samples have
        been labeled.

    verbose : bool, default=False
        Enable verbose output.

    Attributes
    ----------
    base_estimator_ : estimator object
        The fitted estimator.

    classes_ : ndarray or list of ndarray of shape (n_classes,)
        Class labels for each output. (Taken from the trained
        `base_estimator_`).

    transduction_ : ndarray of shape (n_samples,)
        The labels used for the final fit of the classifier, including
        pseudo-labels added during fit.

    labeled_iter_ : ndarray of shape (n_samples,)
        The iteration in which each sample was labeled. When a sample has
        iteration 0, the sample was already labeled in the original dataset.
        When a sample has iteration -1, the sample was not labeled in any
        iteration.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    n_iter_ : int
        The number of rounds of self-training, that is the number of times the
        base estimator is fitted on relabeled variants of the training set.

    termination_condition_ : {\'max_iter\', \'no_change\', \'all_labeled\'}
        The reason that fitting was stopped.

        - `\'max_iter\'`: `n_iter_` reached `max_iter`.
        - `\'no_change\'`: no new labels were predicted.
        - `\'all_labeled\'`: all unlabeled samples were labeled before `max_iter`
          was reached.

    See Also
    --------
    LabelPropagation : Label propagation classifier.
    LabelSpreading : Label spreading model for semi-supervised learning.

    References
    ----------
    :doi:`David Yarowsky. 1995. Unsupervised word sense disambiguation rivaling
    supervised methods. In Proceedings of the 33rd annual meeting on
    Association for Computational Linguistics (ACL \'95). Association for
    Computational Linguistics, Stroudsburg, PA, USA, 189-196.
    <10.3115/981658.981684>`

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn import datasets
    >>> from sklearn.semi_supervised import SelfTrainingClassifier
    >>> from sklearn.svm import SVC
    >>> rng = np.random.RandomState(42)
    >>> iris = datasets.load_iris()
    >>> random_unlabeled_points = rng.rand(iris.target.shape[0]) < 0.3
    >>> iris.target[random_unlabeled_points] = -1
    >>> svc = SVC(probability=True, gamma="auto")
    >>> self_training_model = SelfTrainingClassifier(svc)
    >>> self_training_model.fit(iris.data, iris.target)
    SelfTrainingClassifier(...)
    '''
    base_estimator: Incomplete
    threshold: Incomplete
    criterion: Incomplete
    k_best: Incomplete
    max_iter: Incomplete
    verbose: Incomplete
    def __init__(self, base_estimator, threshold: float = 0.75, criterion: str = 'threshold', k_best: int = 10, max_iter: int = 10, verbose: bool = False) -> None: ...
    base_estimator_: Incomplete
    transduction_: Incomplete
    labeled_iter_: Incomplete
    n_iter_: int
    termination_condition_: str
    classes_: Incomplete
    def fit(self, X, y):
        """
        Fit self-training classifier using `X`, `y` as training data.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Array representing the data.

        y : {array-like, sparse matrix} of shape (n_samples,)
            Array representing the labels. Unlabeled samples should have the
            label -1.

        Returns
        -------
        self : object
            Fitted estimator.
        """
    def predict(self, X):
        """Predict the classes of `X`.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Array representing the data.

        Returns
        -------
        y : ndarray of shape (n_samples,)
            Array with predicted labels.
        """
    def predict_proba(self, X):
        """Predict probability for each possible outcome.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Array representing the data.

        Returns
        -------
        y : ndarray of shape (n_samples, n_features)
            Array with prediction probabilities.
        """
    def decision_function(self, X):
        """Call decision function of the `base_estimator`.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Array representing the data.

        Returns
        -------
        y : ndarray of shape (n_samples, n_features)
            Result of the decision function of the `base_estimator`.
        """
    def predict_log_proba(self, X):
        """Predict log probability for each possible outcome.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Array representing the data.

        Returns
        -------
        y : ndarray of shape (n_samples, n_features)
            Array with log prediction probabilities.
        """
    def score(self, X, y):
        """Call score on the `base_estimator`.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Array representing the data.

        y : array-like of shape (n_samples,)
            Array representing the labels.

        Returns
        -------
        score : float
            Result of calling score on the `base_estimator`.
        """
