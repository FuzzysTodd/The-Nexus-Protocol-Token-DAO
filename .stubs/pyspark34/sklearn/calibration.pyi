from .base import BaseEstimator as BaseEstimator, ClassifierMixin as ClassifierMixin, MetaEstimatorMixin as MetaEstimatorMixin, RegressorMixin as RegressorMixin, clone as clone
from .isotonic import IsotonicRegression as IsotonicRegression
from .model_selection import check_cv as check_cv, cross_val_predict as cross_val_predict
from .preprocessing import LabelEncoder as LabelEncoder, label_binarize as label_binarize
from .svm import LinearSVC as LinearSVC
from .utils import column_or_1d as column_or_1d, indexable as indexable
from .utils._param_validation import HasMethods as HasMethods, Hidden as Hidden, Interval as Interval, StrOptions as StrOptions, validate_params as validate_params
from .utils._plotting import _BinaryClassifierCurveDisplayMixin
from .utils.metadata_routing import MetadataRouter as MetadataRouter, MethodMapping as MethodMapping, process_routing as process_routing
from .utils.multiclass import check_classification_targets as check_classification_targets
from .utils.parallel import Parallel as Parallel, delayed as delayed
from .utils.validation import check_consistent_length as check_consistent_length, check_is_fitted as check_is_fitted
from _typeshed import Incomplete
from sklearn.utils import Bunch as Bunch

class CalibratedClassifierCV(ClassifierMixin, MetaEstimatorMixin, BaseEstimator):
    '''Probability calibration with isotonic regression or logistic regression.

    This class uses cross-validation to both estimate the parameters of a
    classifier and subsequently calibrate a classifier. With default
    `ensemble=True`, for each cv split it
    fits a copy of the base estimator to the training subset, and calibrates it
    using the testing subset. For prediction, predicted probabilities are
    averaged across these individual calibrated classifiers. When
    `ensemble=False`, cross-validation is used to obtain unbiased predictions,
    via :func:`~sklearn.model_selection.cross_val_predict`, which are then
    used for calibration. For prediction, the base estimator, trained using all
    the data, is used. This is the method implemented when `probabilities=True`
    for :mod:`sklearn.svm` estimators.

    Already fitted classifiers can be calibrated via the parameter
    `cv="prefit"`. In this case, no cross-validation is used and all provided
    data is used for calibration. The user has to take care manually that data
    for model fitting and calibration are disjoint.

    The calibration is based on the :term:`decision_function` method of the
    `estimator` if it exists, else on :term:`predict_proba`.

    Read more in the :ref:`User Guide <calibration>`.

    Parameters
    ----------
    estimator : estimator instance, default=None
        The classifier whose output need to be calibrated to provide more
        accurate `predict_proba` outputs. The default classifier is
        a :class:`~sklearn.svm.LinearSVC`.

        .. versionadded:: 1.2

    method : {\'sigmoid\', \'isotonic\'}, default=\'sigmoid\'
        The method to use for calibration. Can be \'sigmoid\' which
        corresponds to Platt\'s method (i.e. a logistic regression model) or
        \'isotonic\' which is a non-parametric approach. It is not advised to
        use isotonic calibration with too few calibration samples
        ``(<<1000)`` since it tends to overfit.

    cv : int, cross-validation generator, iterable or "prefit",             default=None
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:

        - None, to use the default 5-fold cross-validation,
        - integer, to specify the number of folds.
        - :term:`CV splitter`,
        - An iterable yielding (train, test) splits as arrays of indices.

        For integer/None inputs, if ``y`` is binary or multiclass,
        :class:`~sklearn.model_selection.StratifiedKFold` is used. If ``y`` is
        neither binary nor multiclass, :class:`~sklearn.model_selection.KFold`
        is used.

        Refer to the :ref:`User Guide <cross_validation>` for the various
        cross-validation strategies that can be used here.

        If "prefit" is passed, it is assumed that `estimator` has been
        fitted already and all data is used for calibration.

        .. versionchanged:: 0.22
            ``cv`` default value if None changed from 3-fold to 5-fold.

    n_jobs : int, default=None
        Number of jobs to run in parallel.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors.

        Base estimator clones are fitted in parallel across cross-validation
        iterations. Therefore parallelism happens only when `cv != "prefit"`.

        See :term:`Glossary <n_jobs>` for more details.

        .. versionadded:: 0.24

    ensemble : bool, default=True
        Determines how the calibrator is fitted when `cv` is not `\'prefit\'`.
        Ignored if `cv=\'prefit\'`.

        If `True`, the `estimator` is fitted using training data, and
        calibrated using testing data, for each `cv` fold. The final estimator
        is an ensemble of `n_cv` fitted classifier and calibrator pairs, where
        `n_cv` is the number of cross-validation folds. The output is the
        average predicted probabilities of all pairs.

        If `False`, `cv` is used to compute unbiased predictions, via
        :func:`~sklearn.model_selection.cross_val_predict`, which are then
        used for calibration. At prediction time, the classifier used is the
        `estimator` trained on all the data.
        Note that this method is also internally implemented  in
        :mod:`sklearn.svm` estimators with the `probabilities=True` parameter.

        .. versionadded:: 0.24

    base_estimator : estimator instance
        This parameter is deprecated. Use `estimator` instead.

        .. deprecated:: 1.2
           The parameter `base_estimator` is deprecated in 1.2 and will be
           removed in 1.4. Use `estimator` instead.

    Attributes
    ----------
    classes_ : ndarray of shape (n_classes,)
        The class labels.

    n_features_in_ : int
        Number of features seen during :term:`fit`. Only defined if the
        underlying estimator exposes such an attribute when fit.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Only defined if the
        underlying estimator exposes such an attribute when fit.

        .. versionadded:: 1.0

    calibrated_classifiers_ : list (len() equal to cv or 1 if `cv="prefit"`             or `ensemble=False`)
        The list of classifier and calibrator pairs.

        - When `cv="prefit"`, the fitted `estimator` and fitted
          calibrator.
        - When `cv` is not "prefit" and `ensemble=True`, `n_cv` fitted
          `estimator` and calibrator pairs. `n_cv` is the number of
          cross-validation folds.
        - When `cv` is not "prefit" and `ensemble=False`, the `estimator`,
          fitted on all the data, and fitted calibrator.

        .. versionchanged:: 0.24
            Single calibrated classifier case when `ensemble=False`.

    See Also
    --------
    calibration_curve : Compute true and predicted probabilities
        for a calibration curve.

    References
    ----------
    .. [1] Obtaining calibrated probability estimates from decision trees
           and naive Bayesian classifiers, B. Zadrozny & C. Elkan, ICML 2001

    .. [2] Transforming Classifier Scores into Accurate Multiclass
           Probability Estimates, B. Zadrozny & C. Elkan, (KDD 2002)

    .. [3] Probabilistic Outputs for Support Vector Machines and Comparisons to
           Regularized Likelihood Methods, J. Platt, (1999)

    .. [4] Predicting Good Probabilities with Supervised Learning,
           A. Niculescu-Mizil & R. Caruana, ICML 2005

    Examples
    --------
    >>> from sklearn.datasets import make_classification
    >>> from sklearn.naive_bayes import GaussianNB
    >>> from sklearn.calibration import CalibratedClassifierCV
    >>> X, y = make_classification(n_samples=100, n_features=2,
    ...                            n_redundant=0, random_state=42)
    >>> base_clf = GaussianNB()
    >>> calibrated_clf = CalibratedClassifierCV(base_clf, cv=3)
    >>> calibrated_clf.fit(X, y)
    CalibratedClassifierCV(...)
    >>> len(calibrated_clf.calibrated_classifiers_)
    3
    >>> calibrated_clf.predict_proba(X)[:5, :]
    array([[0.110..., 0.889...],
           [0.072..., 0.927...],
           [0.928..., 0.071...],
           [0.928..., 0.071...],
           [0.071..., 0.928...]])
    >>> from sklearn.model_selection import train_test_split
    >>> X, y = make_classification(n_samples=100, n_features=2,
    ...                            n_redundant=0, random_state=42)
    >>> X_train, X_calib, y_train, y_calib = train_test_split(
    ...        X, y, random_state=42
    ... )
    >>> base_clf = GaussianNB()
    >>> base_clf.fit(X_train, y_train)
    GaussianNB()
    >>> calibrated_clf = CalibratedClassifierCV(base_clf, cv="prefit")
    >>> calibrated_clf.fit(X_calib, y_calib)
    CalibratedClassifierCV(...)
    >>> len(calibrated_clf.calibrated_classifiers_)
    1
    >>> calibrated_clf.predict_proba([[-0.5, 0.5]])
    array([[0.936..., 0.063...]])
    '''
    estimator: Incomplete
    method: Incomplete
    cv: Incomplete
    n_jobs: Incomplete
    ensemble: Incomplete
    base_estimator: Incomplete
    def __init__(self, estimator: Incomplete | None = None, *, method: str = 'sigmoid', cv: Incomplete | None = None, n_jobs: Incomplete | None = None, ensemble: bool = True, base_estimator: str = 'deprecated') -> None: ...
    calibrated_classifiers_: Incomplete
    classes_: Incomplete
    n_features_in_: Incomplete
    feature_names_in_: Incomplete
    def fit(self, X, y, sample_weight: Incomplete | None = None, **fit_params):
        """Fit the calibrated model.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training data.

        y : array-like of shape (n_samples,)
            Target values.

        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights. If None, then samples are equally weighted.

        **fit_params : dict
            Parameters to pass to the `fit` method of the underlying
            classifier.

        Returns
        -------
        self : object
            Returns an instance of self.
        """
    def predict_proba(self, X):
        """Calibrated probabilities of classification.

        This function returns calibrated probabilities of classification
        according to each class on an array of test vectors X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The samples, as accepted by `estimator.predict_proba`.

        Returns
        -------
        C : ndarray of shape (n_samples, n_classes)
            The predicted probas.
        """
    def predict(self, X):
        """Predict the target of new samples.

        The predicted class is the class that has the highest probability,
        and can thus be different from the prediction of the uncalibrated classifier.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The samples, as accepted by `estimator.predict`.

        Returns
        -------
        C : ndarray of shape (n_samples,)
            The predicted class.
        """
    def get_metadata_routing(self):
        """Get metadata routing of this object.

        Please check :ref:`User Guide <metadata_routing>` on how the routing
        mechanism works.

        Returns
        -------
        routing : MetadataRouter
            A :class:`~utils.metadata_routing.MetadataRouter` encapsulating
            routing information.
        """

class _CalibratedClassifier:
    """Pipeline-like chaining a fitted classifier and its fitted calibrators.

    Parameters
    ----------
    estimator : estimator instance
        Fitted classifier.

    calibrators : list of fitted estimator instances
        List of fitted calibrators (either 'IsotonicRegression' or
        '_SigmoidCalibration'). The number of calibrators equals the number of
        classes. However, if there are 2 classes, the list contains only one
        fitted calibrator.

    classes : array-like of shape (n_classes,)
        All the prediction classes.

    method : {'sigmoid', 'isotonic'}, default='sigmoid'
        The method to use for calibration. Can be 'sigmoid' which
        corresponds to Platt's method or 'isotonic' which is a
        non-parametric approach based on isotonic regression.
    """
    estimator: Incomplete
    calibrators: Incomplete
    classes: Incomplete
    method: Incomplete
    def __init__(self, estimator, calibrators, *, classes, method: str = 'sigmoid') -> None: ...
    def predict_proba(self, X):
        """Calculate calibrated probabilities.

        Calculates classification calibrated probabilities
        for each class, in a one-vs-all manner, for `X`.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            The sample data.

        Returns
        -------
        proba : array, shape (n_samples, n_classes)
            The predicted probabilities. Can be exact zeros.
        """

class _SigmoidCalibration(RegressorMixin, BaseEstimator):
    """Sigmoid regression model.

    Attributes
    ----------
    a_ : float
        The slope.

    b_ : float
        The intercept.
    """
    def fit(self, X, y, sample_weight: Incomplete | None = None):
        """Fit the model using X, y as training data.

        Parameters
        ----------
        X : array-like of shape (n_samples,)
            Training data.

        y : array-like of shape (n_samples,)
            Training target.

        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights. If None, then samples are equally weighted.

        Returns
        -------
        self : object
            Returns an instance of self.
        """
    def predict(self, T):
        """Predict new data by linear interpolation.

        Parameters
        ----------
        T : array-like of shape (n_samples,)
            Data to predict from.

        Returns
        -------
        T_ : ndarray of shape (n_samples,)
            The predicted data.
        """

def calibration_curve(y_true, y_prob, *, pos_label: Incomplete | None = None, n_bins: int = 5, strategy: str = 'uniform'):
    """Compute true and predicted probabilities for a calibration curve.

    The method assumes the inputs come from a binary classifier, and
    discretize the [0, 1] interval into bins.

    Calibration curves may also be referred to as reliability diagrams.

    Read more in the :ref:`User Guide <calibration>`.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True targets.

    y_prob : array-like of shape (n_samples,)
        Probabilities of the positive class.

    pos_label : int, float, bool or str, default=None
        The label of the positive class.

        .. versionadded:: 1.1

    n_bins : int, default=5
        Number of bins to discretize the [0, 1] interval. A bigger number
        requires more data. Bins with no samples (i.e. without
        corresponding values in `y_prob`) will not be returned, thus the
        returned arrays may have less than `n_bins` values.

    strategy : {'uniform', 'quantile'}, default='uniform'
        Strategy used to define the widths of the bins.

        uniform
            The bins have identical widths.
        quantile
            The bins have the same number of samples and depend on `y_prob`.

    Returns
    -------
    prob_true : ndarray of shape (n_bins,) or smaller
        The proportion of samples whose class is the positive class, in each
        bin (fraction of positives).

    prob_pred : ndarray of shape (n_bins,) or smaller
        The mean predicted probability in each bin.

    References
    ----------
    Alexandru Niculescu-Mizil and Rich Caruana (2005) Predicting Good
    Probabilities With Supervised Learning, in Proceedings of the 22nd
    International Conference on Machine Learning (ICML).
    See section 4 (Qualitative Analysis of Predictions).

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.calibration import calibration_curve
    >>> y_true = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])
    >>> y_pred = np.array([0.1, 0.2, 0.3, 0.4, 0.65, 0.7, 0.8, 0.9,  1.])
    >>> prob_true, prob_pred = calibration_curve(y_true, y_pred, n_bins=3)
    >>> prob_true
    array([0. , 0.5, 1. ])
    >>> prob_pred
    array([0.2  , 0.525, 0.85 ])
    """

class CalibrationDisplay(_BinaryClassifierCurveDisplayMixin):
    """Calibration curve (also known as reliability diagram) visualization.

    It is recommended to use
    :func:`~sklearn.calibration.CalibrationDisplay.from_estimator` or
    :func:`~sklearn.calibration.CalibrationDisplay.from_predictions`
    to create a `CalibrationDisplay`. All parameters are stored as attributes.

    Read more about calibration in the :ref:`User Guide <calibration>` and
    more about the scikit-learn visualization API in :ref:`visualizations`.

    .. versionadded:: 1.0

    Parameters
    ----------
    prob_true : ndarray of shape (n_bins,)
        The proportion of samples whose class is the positive class (fraction
        of positives), in each bin.

    prob_pred : ndarray of shape (n_bins,)
        The mean predicted probability in each bin.

    y_prob : ndarray of shape (n_samples,)
        Probability estimates for the positive class, for each sample.

    estimator_name : str, default=None
        Name of estimator. If None, the estimator name is not shown.

    pos_label : int, float, bool or str, default=None
        The positive class when computing the calibration curve.
        By default, `estimators.classes_[1]` is considered as the
        positive class.

        .. versionadded:: 1.1

    Attributes
    ----------
    line_ : matplotlib Artist
        Calibration curve.

    ax_ : matplotlib Axes
        Axes with calibration curve.

    figure_ : matplotlib Figure
        Figure containing the curve.

    See Also
    --------
    calibration_curve : Compute true and predicted probabilities for a
        calibration curve.
    CalibrationDisplay.from_predictions : Plot calibration curve using true
        and predicted labels.
    CalibrationDisplay.from_estimator : Plot calibration curve using an
        estimator and data.

    Examples
    --------
    >>> from sklearn.datasets import make_classification
    >>> from sklearn.model_selection import train_test_split
    >>> from sklearn.linear_model import LogisticRegression
    >>> from sklearn.calibration import calibration_curve, CalibrationDisplay
    >>> X, y = make_classification(random_state=0)
    >>> X_train, X_test, y_train, y_test = train_test_split(
    ...     X, y, random_state=0)
    >>> clf = LogisticRegression(random_state=0)
    >>> clf.fit(X_train, y_train)
    LogisticRegression(random_state=0)
    >>> y_prob = clf.predict_proba(X_test)[:, 1]
    >>> prob_true, prob_pred = calibration_curve(y_test, y_prob, n_bins=10)
    >>> disp = CalibrationDisplay(prob_true, prob_pred, y_prob)
    >>> disp.plot()
    <...>
    """
    prob_true: Incomplete
    prob_pred: Incomplete
    y_prob: Incomplete
    estimator_name: Incomplete
    pos_label: Incomplete
    def __init__(self, prob_true, prob_pred, y_prob, *, estimator_name: Incomplete | None = None, pos_label: Incomplete | None = None) -> None: ...
    line_: Incomplete
    def plot(self, *, ax: Incomplete | None = None, name: Incomplete | None = None, ref_line: bool = True, **kwargs):
        """Plot visualization.

        Extra keyword arguments will be passed to
        :func:`matplotlib.pyplot.plot`.

        Parameters
        ----------
        ax : Matplotlib Axes, default=None
            Axes object to plot on. If `None`, a new figure and axes is
            created.

        name : str, default=None
            Name for labeling curve. If `None`, use `estimator_name` if
            not `None`, otherwise no labeling is shown.

        ref_line : bool, default=True
            If `True`, plots a reference line representing a perfectly
            calibrated classifier.

        **kwargs : dict
            Keyword arguments to be passed to :func:`matplotlib.pyplot.plot`.

        Returns
        -------
        display : :class:`~sklearn.calibration.CalibrationDisplay`
            Object that stores computed values.
        """
    @classmethod
    def from_estimator(cls, estimator, X, y, *, n_bins: int = 5, strategy: str = 'uniform', pos_label: Incomplete | None = None, name: Incomplete | None = None, ref_line: bool = True, ax: Incomplete | None = None, **kwargs):
        """Plot calibration curve using a binary classifier and data.

        A calibration curve, also known as a reliability diagram, uses inputs
        from a binary classifier and plots the average predicted probability
        for each bin against the fraction of positive classes, on the
        y-axis.

        Extra keyword arguments will be passed to
        :func:`matplotlib.pyplot.plot`.

        Read more about calibration in the :ref:`User Guide <calibration>` and
        more about the scikit-learn visualization API in :ref:`visualizations`.

        .. versionadded:: 1.0

        Parameters
        ----------
        estimator : estimator instance
            Fitted classifier or a fitted :class:`~sklearn.pipeline.Pipeline`
            in which the last estimator is a classifier. The classifier must
            have a :term:`predict_proba` method.

        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Input values.

        y : array-like of shape (n_samples,)
            Binary target values.

        n_bins : int, default=5
            Number of bins to discretize the [0, 1] interval into when
            calculating the calibration curve. A bigger number requires more
            data.

        strategy : {'uniform', 'quantile'}, default='uniform'
            Strategy used to define the widths of the bins.

            - `'uniform'`: The bins have identical widths.
            - `'quantile'`: The bins have the same number of samples and depend
              on predicted probabilities.

        pos_label : int, float, bool or str, default=None
            The positive class when computing the calibration curve.
            By default, `estimators.classes_[1]` is considered as the
            positive class.

            .. versionadded:: 1.1

        name : str, default=None
            Name for labeling curve. If `None`, the name of the estimator is
            used.

        ref_line : bool, default=True
            If `True`, plots a reference line representing a perfectly
            calibrated classifier.

        ax : matplotlib axes, default=None
            Axes object to plot on. If `None`, a new figure and axes is
            created.

        **kwargs : dict
            Keyword arguments to be passed to :func:`matplotlib.pyplot.plot`.

        Returns
        -------
        display : :class:`~sklearn.calibration.CalibrationDisplay`.
            Object that stores computed values.

        See Also
        --------
        CalibrationDisplay.from_predictions : Plot calibration curve using true
            and predicted labels.

        Examples
        --------
        >>> import matplotlib.pyplot as plt
        >>> from sklearn.datasets import make_classification
        >>> from sklearn.model_selection import train_test_split
        >>> from sklearn.linear_model import LogisticRegression
        >>> from sklearn.calibration import CalibrationDisplay
        >>> X, y = make_classification(random_state=0)
        >>> X_train, X_test, y_train, y_test = train_test_split(
        ...     X, y, random_state=0)
        >>> clf = LogisticRegression(random_state=0)
        >>> clf.fit(X_train, y_train)
        LogisticRegression(random_state=0)
        >>> disp = CalibrationDisplay.from_estimator(clf, X_test, y_test)
        >>> plt.show()
        """
    @classmethod
    def from_predictions(cls, y_true, y_prob, *, n_bins: int = 5, strategy: str = 'uniform', pos_label: Incomplete | None = None, name: Incomplete | None = None, ref_line: bool = True, ax: Incomplete | None = None, **kwargs):
        """Plot calibration curve using true labels and predicted probabilities.

        Calibration curve, also known as reliability diagram, uses inputs
        from a binary classifier and plots the average predicted probability
        for each bin against the fraction of positive classes, on the
        y-axis.

        Extra keyword arguments will be passed to
        :func:`matplotlib.pyplot.plot`.

        Read more about calibration in the :ref:`User Guide <calibration>` and
        more about the scikit-learn visualization API in :ref:`visualizations`.

        .. versionadded:: 1.0

        Parameters
        ----------
        y_true : array-like of shape (n_samples,)
            True labels.

        y_prob : array-like of shape (n_samples,)
            The predicted probabilities of the positive class.

        n_bins : int, default=5
            Number of bins to discretize the [0, 1] interval into when
            calculating the calibration curve. A bigger number requires more
            data.

        strategy : {'uniform', 'quantile'}, default='uniform'
            Strategy used to define the widths of the bins.

            - `'uniform'`: The bins have identical widths.
            - `'quantile'`: The bins have the same number of samples and depend
              on predicted probabilities.

        pos_label : int, float, bool or str, default=None
            The positive class when computing the calibration curve.
            By default, `estimators.classes_[1]` is considered as the
            positive class.

            .. versionadded:: 1.1

        name : str, default=None
            Name for labeling curve.

        ref_line : bool, default=True
            If `True`, plots a reference line representing a perfectly
            calibrated classifier.

        ax : matplotlib axes, default=None
            Axes object to plot on. If `None`, a new figure and axes is
            created.

        **kwargs : dict
            Keyword arguments to be passed to :func:`matplotlib.pyplot.plot`.

        Returns
        -------
        display : :class:`~sklearn.calibration.CalibrationDisplay`.
            Object that stores computed values.

        See Also
        --------
        CalibrationDisplay.from_estimator : Plot calibration curve using an
            estimator and data.

        Examples
        --------
        >>> import matplotlib.pyplot as plt
        >>> from sklearn.datasets import make_classification
        >>> from sklearn.model_selection import train_test_split
        >>> from sklearn.linear_model import LogisticRegression
        >>> from sklearn.calibration import CalibrationDisplay
        >>> X, y = make_classification(random_state=0)
        >>> X_train, X_test, y_train, y_test = train_test_split(
        ...     X, y, random_state=0)
        >>> clf = LogisticRegression(random_state=0)
        >>> clf.fit(X_train, y_train)
        LogisticRegression(random_state=0)
        >>> y_prob = clf.predict_proba(X_test)[:, 1]
        >>> disp = CalibrationDisplay.from_predictions(y_test, y_prob)
        >>> plt.show()
        """
