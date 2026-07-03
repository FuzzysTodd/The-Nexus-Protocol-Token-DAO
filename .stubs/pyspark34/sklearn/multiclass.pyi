from .base import BaseEstimator, ClassifierMixin, MetaEstimatorMixin, MultiOutputMixin
from _typeshed import Incomplete

__all__ = ['OneVsRestClassifier', 'OneVsOneClassifier', 'OutputCodeClassifier']

class _ConstantPredictor(BaseEstimator):
    y_: Incomplete
    def fit(self, X, y): ...
    def predict(self, X): ...
    def decision_function(self, X): ...
    def predict_proba(self, X): ...

class OneVsRestClassifier(MultiOutputMixin, ClassifierMixin, MetaEstimatorMixin, BaseEstimator):
    """One-vs-the-rest (OvR) multiclass strategy.

    Also known as one-vs-all, this strategy consists in fitting one classifier
    per class. For each classifier, the class is fitted against all the other
    classes. In addition to its computational efficiency (only `n_classes`
    classifiers are needed), one advantage of this approach is its
    interpretability. Since each class is represented by one and one classifier
    only, it is possible to gain knowledge about the class by inspecting its
    corresponding classifier. This is the most commonly used strategy for
    multiclass classification and is a fair default choice.

    OneVsRestClassifier can also be used for multilabel classification. To use
    this feature, provide an indicator matrix for the target `y` when calling
    `.fit`. In other words, the target labels should be formatted as a 2D
    binary (0/1) matrix, where [i, j] == 1 indicates the presence of label j
    in sample i. This estimator uses the binary relevance method to perform
    multilabel classification, which involves training one binary classifier
    independently for each label.

    Read more in the :ref:`User Guide <ovr_classification>`.

    Parameters
    ----------
    estimator : estimator object
        A regressor or a classifier that implements :term:`fit`.
        When a classifier is passed, :term:`decision_function` will be used
        in priority and it will fallback to :term:`predict_proba` if it is not
        available.
        When a regressor is passed, :term:`predict` is used.

    n_jobs : int, default=None
        The number of jobs to use for the computation: the `n_classes`
        one-vs-rest problems are computed in parallel.

        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

        .. versionchanged:: 0.20
           `n_jobs` default changed from 1 to None

    verbose : int, default=0
        The verbosity level, if non zero, progress messages are printed.
        Below 50, the output is sent to stderr. Otherwise, the output is sent
        to stdout. The frequency of the messages increases with the verbosity
        level, reporting all iterations at 10. See :class:`joblib.Parallel` for
        more details.

        .. versionadded:: 1.1

    Attributes
    ----------
    estimators_ : list of `n_classes` estimators
        Estimators used for predictions.

    classes_ : array, shape = [`n_classes`]
        Class labels.

    n_classes_ : int
        Number of classes.

    label_binarizer_ : LabelBinarizer object
        Object used to transform multiclass labels to binary labels and
        vice-versa.

    multilabel_ : boolean
        Whether a OneVsRestClassifier is a multilabel classifier.

    n_features_in_ : int
        Number of features seen during :term:`fit`. Only defined if the
        underlying estimator exposes such an attribute when fit.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Only defined if the
        underlying estimator exposes such an attribute when fit.

        .. versionadded:: 1.0

    See Also
    --------
    OneVsOneClassifier : One-vs-one multiclass strategy.
    OutputCodeClassifier : (Error-Correcting) Output-Code multiclass strategy.
    sklearn.multioutput.MultiOutputClassifier : Alternate way of extending an
        estimator for multilabel classification.
    sklearn.preprocessing.MultiLabelBinarizer : Transform iterable of iterables
        to binary indicator matrix.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.multiclass import OneVsRestClassifier
    >>> from sklearn.svm import SVC
    >>> X = np.array([
    ...     [10, 10],
    ...     [8, 10],
    ...     [-5, 5.5],
    ...     [-5.4, 5.5],
    ...     [-20, -20],
    ...     [-15, -20]
    ... ])
    >>> y = np.array([0, 0, 1, 1, 2, 2])
    >>> clf = OneVsRestClassifier(SVC()).fit(X, y)
    >>> clf.predict([[-19, -20], [9, 9], [-5, 5]])
    array([2, 0, 1])
    """
    estimator: Incomplete
    n_jobs: Incomplete
    verbose: Incomplete
    def __init__(self, estimator, *, n_jobs: Incomplete | None = None, verbose: int = 0) -> None: ...
    label_binarizer_: Incomplete
    classes_: Incomplete
    estimators_: Incomplete
    n_features_in_: Incomplete
    feature_names_in_: Incomplete
    def fit(self, X, y):
        """Fit underlying estimators.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Data.

        y : {array-like, sparse matrix} of shape (n_samples,) or (n_samples, n_classes)
            Multi-class targets. An indicator matrix turns on multilabel
            classification.

        Returns
        -------
        self : object
            Instance of fitted estimator.
        """
    def partial_fit(self, X, y, classes: Incomplete | None = None):
        """Partially fit underlying estimators.

        Should be used when memory is inefficient to train all data.
        Chunks of data can be passed in several iteration.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Data.

        y : {array-like, sparse matrix} of shape (n_samples,) or (n_samples, n_classes)
            Multi-class targets. An indicator matrix turns on multilabel
            classification.

        classes : array, shape (n_classes, )
            Classes across all calls to partial_fit.
            Can be obtained via `np.unique(y_all)`, where y_all is the
            target vector of the entire dataset.
            This argument is only required in the first call of partial_fit
            and can be omitted in the subsequent calls.

        Returns
        -------
        self : object
            Instance of partially fitted estimator.
        """
    def predict(self, X):
        """Predict multi-class targets using underlying estimators.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Data.

        Returns
        -------
        y : {array-like, sparse matrix} of shape (n_samples,) or (n_samples, n_classes)
            Predicted multi-class targets.
        """
    def predict_proba(self, X):
        """Probability estimates.

        The returned estimates for all classes are ordered by label of classes.

        Note that in the multilabel case, each sample can have any number of
        labels. This returns the marginal probability that the given sample has
        the label in question. For example, it is entirely consistent that two
        labels both have a 90% probability of applying to a given sample.

        In the single label multiclass case, the rows of the returned matrix
        sum to 1.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Input data.

        Returns
        -------
        T : array-like of shape (n_samples, n_classes)
            Returns the probability of the sample for each class in the model,
            where classes are ordered as they are in `self.classes_`.
        """
    def decision_function(self, X):
        """Decision function for the OneVsRestClassifier.

        Return the distance of each sample from the decision boundary for each
        class. This can only be used with estimators which implement the
        `decision_function` method.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Input data.

        Returns
        -------
        T : array-like of shape (n_samples, n_classes) or (n_samples,) for             binary classification.
            Result of calling `decision_function` on the final estimator.

            .. versionchanged:: 0.19
                output shape changed to ``(n_samples,)`` to conform to
                scikit-learn conventions for binary classification.
        """
    @property
    def multilabel_(self):
        """Whether this is a multilabel classifier."""
    @property
    def n_classes_(self):
        """Number of classes."""

class OneVsOneClassifier(MetaEstimatorMixin, ClassifierMixin, BaseEstimator):
    '''One-vs-one multiclass strategy.

    This strategy consists in fitting one classifier per class pair.
    At prediction time, the class which received the most votes is selected.
    Since it requires to fit `n_classes * (n_classes - 1) / 2` classifiers,
    this method is usually slower than one-vs-the-rest, due to its
    O(n_classes^2) complexity. However, this method may be advantageous for
    algorithms such as kernel algorithms which don\'t scale well with
    `n_samples`. This is because each individual learning problem only involves
    a small subset of the data whereas, with one-vs-the-rest, the complete
    dataset is used `n_classes` times.

    Read more in the :ref:`User Guide <ovo_classification>`.

    Parameters
    ----------
    estimator : estimator object
        A regressor or a classifier that implements :term:`fit`.
        When a classifier is passed, :term:`decision_function` will be used
        in priority and it will fallback to :term:`predict_proba` if it is not
        available.
        When a regressor is passed, :term:`predict` is used.

    n_jobs : int, default=None
        The number of jobs to use for the computation: the `n_classes * (
        n_classes - 1) / 2` OVO problems are computed in parallel.

        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    Attributes
    ----------
    estimators_ : list of ``n_classes * (n_classes - 1) / 2`` estimators
        Estimators used for predictions.

    classes_ : numpy array of shape [n_classes]
        Array containing labels.

    n_classes_ : int
        Number of classes.

    pairwise_indices_ : list, length = ``len(estimators_)``, or ``None``
        Indices of samples used when training the estimators.
        ``None`` when ``estimator``\'s `pairwise` tag is False.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    OneVsRestClassifier : One-vs-all multiclass strategy.
    OutputCodeClassifier : (Error-Correcting) Output-Code multiclass strategy.

    Examples
    --------
    >>> from sklearn.datasets import load_iris
    >>> from sklearn.model_selection import train_test_split
    >>> from sklearn.multiclass import OneVsOneClassifier
    >>> from sklearn.svm import LinearSVC
    >>> X, y = load_iris(return_X_y=True)
    >>> X_train, X_test, y_train, y_test = train_test_split(
    ...     X, y, test_size=0.33, shuffle=True, random_state=0)
    >>> clf = OneVsOneClassifier(
    ...     LinearSVC(dual="auto", random_state=0)).fit(X_train, y_train)
    >>> clf.predict(X_test[:10])
    array([2, 1, 0, 2, 0, 2, 0, 1, 1, 1])
    '''
    estimator: Incomplete
    n_jobs: Incomplete
    def __init__(self, estimator, *, n_jobs: Incomplete | None = None) -> None: ...
    classes_: Incomplete
    estimators_: Incomplete
    pairwise_indices_: Incomplete
    def fit(self, X, y):
        """Fit underlying estimators.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Data.

        y : array-like of shape (n_samples,)
            Multi-class targets.

        Returns
        -------
        self : object
            The fitted underlying estimator.
        """
    n_features_in_: Incomplete
    def partial_fit(self, X, y, classes: Incomplete | None = None):
        """Partially fit underlying estimators.

        Should be used when memory is inefficient to train all data. Chunks
        of data can be passed in several iteration, where the first call
        should have an array of all target variables.

        Parameters
        ----------
        X : {array-like, sparse matrix) of shape (n_samples, n_features)
            Data.

        y : array-like of shape (n_samples,)
            Multi-class targets.

        classes : array, shape (n_classes, )
            Classes across all calls to partial_fit.
            Can be obtained via `np.unique(y_all)`, where y_all is the
            target vector of the entire dataset.
            This argument is only required in the first call of partial_fit
            and can be omitted in the subsequent calls.

        Returns
        -------
        self : object
            The partially fitted underlying estimator.
        """
    def predict(self, X):
        """Estimate the best class label for each sample in X.

        This is implemented as ``argmax(decision_function(X), axis=1)`` which
        will return the label of the class with most votes by estimators
        predicting the outcome of a decision for each possible class pair.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Data.

        Returns
        -------
        y : numpy array of shape [n_samples]
            Predicted multi-class targets.
        """
    def decision_function(self, X):
        """Decision function for the OneVsOneClassifier.

        The decision values for the samples are computed by adding the
        normalized sum of pair-wise classification confidence levels to the
        votes in order to disambiguate between the decision values when the
        votes for all the classes are equal leading to a tie.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Input data.

        Returns
        -------
        Y : array-like of shape (n_samples, n_classes) or (n_samples,)
            Result of calling `decision_function` on the final estimator.

            .. versionchanged:: 0.19
                output shape changed to ``(n_samples,)`` to conform to
                scikit-learn conventions for binary classification.
        """
    @property
    def n_classes_(self):
        """Number of classes."""

class OutputCodeClassifier(MetaEstimatorMixin, ClassifierMixin, BaseEstimator):
    '''(Error-Correcting) Output-Code multiclass strategy.

    Output-code based strategies consist in representing each class with a
    binary code (an array of 0s and 1s). At fitting time, one binary
    classifier per bit in the code book is fitted.  At prediction time, the
    classifiers are used to project new points in the class space and the class
    closest to the points is chosen. The main advantage of these strategies is
    that the number of classifiers used can be controlled by the user, either
    for compressing the model (0 < `code_size` < 1) or for making the model more
    robust to errors (`code_size` > 1). See the documentation for more details.

    Read more in the :ref:`User Guide <ecoc>`.

    Parameters
    ----------
    estimator : estimator object
        An estimator object implementing :term:`fit` and one of
        :term:`decision_function` or :term:`predict_proba`.

    code_size : float, default=1.5
        Percentage of the number of classes to be used to create the code book.
        A number between 0 and 1 will require fewer classifiers than
        one-vs-the-rest. A number greater than 1 will require more classifiers
        than one-vs-the-rest.

    random_state : int, RandomState instance, default=None
        The generator used to initialize the codebook.
        Pass an int for reproducible output across multiple function calls.
        See :term:`Glossary <random_state>`.

    n_jobs : int, default=None
        The number of jobs to use for the computation: the multiclass problems
        are computed in parallel.

        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    Attributes
    ----------
    estimators_ : list of `int(n_classes * code_size)` estimators
        Estimators used for predictions.

    classes_ : ndarray of shape (n_classes,)
        Array containing labels.

    code_book_ : ndarray of shape (n_classes, code_size)
        Binary array containing the code of each class.

    n_features_in_ : int
        Number of features seen during :term:`fit`. Only defined if the
        underlying estimator exposes such an attribute when fit.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Only defined if the
        underlying estimator exposes such an attribute when fit.

        .. versionadded:: 1.0

    See Also
    --------
    OneVsRestClassifier : One-vs-all multiclass strategy.
    OneVsOneClassifier : One-vs-one multiclass strategy.

    References
    ----------

    .. [1] "Solving multiclass learning problems via error-correcting output
       codes",
       Dietterich T., Bakiri G.,
       Journal of Artificial Intelligence Research 2,
       1995.

    .. [2] "The error coding method and PICTs",
       James G., Hastie T.,
       Journal of Computational and Graphical statistics 7,
       1998.

    .. [3] "The Elements of Statistical Learning",
       Hastie T., Tibshirani R., Friedman J., page 606 (second-edition)
       2008.

    Examples
    --------
    >>> from sklearn.multiclass import OutputCodeClassifier
    >>> from sklearn.ensemble import RandomForestClassifier
    >>> from sklearn.datasets import make_classification
    >>> X, y = make_classification(n_samples=100, n_features=4,
    ...                            n_informative=2, n_redundant=0,
    ...                            random_state=0, shuffle=False)
    >>> clf = OutputCodeClassifier(
    ...     estimator=RandomForestClassifier(random_state=0),
    ...     random_state=0).fit(X, y)
    >>> clf.predict([[0, 0, 0, 0]])
    array([1])
    '''
    estimator: Incomplete
    code_size: Incomplete
    random_state: Incomplete
    n_jobs: Incomplete
    def __init__(self, estimator, *, code_size: float = 1.5, random_state: Incomplete | None = None, n_jobs: Incomplete | None = None) -> None: ...
    classes_: Incomplete
    code_book_: Incomplete
    estimators_: Incomplete
    n_features_in_: Incomplete
    feature_names_in_: Incomplete
    def fit(self, X, y):
        """Fit underlying estimators.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Data.

        y : array-like of shape (n_samples,)
            Multi-class targets.

        Returns
        -------
        self : object
            Returns a fitted instance of self.
        """
    def predict(self, X):
        """Predict multi-class targets using underlying estimators.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Data.

        Returns
        -------
        y : ndarray of shape (n_samples,)
            Predicted multi-class targets.
        """
