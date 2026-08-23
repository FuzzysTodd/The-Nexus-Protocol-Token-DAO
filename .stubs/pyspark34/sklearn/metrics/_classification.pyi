from ..exceptions import UndefinedMetricWarning as UndefinedMetricWarning
from ..preprocessing import LabelBinarizer as LabelBinarizer, LabelEncoder as LabelEncoder
from ..utils import assert_all_finite as assert_all_finite, check_array as check_array, check_consistent_length as check_consistent_length, column_or_1d as column_or_1d
from ..utils._param_validation import Interval as Interval, Options as Options, StrOptions as StrOptions, validate_params as validate_params
from ..utils.multiclass import type_of_target as type_of_target, unique_labels as unique_labels
from ..utils.sparsefuncs import count_nonzero as count_nonzero
from _typeshed import Incomplete

def accuracy_score(y_true, y_pred, *, normalize: bool = True, sample_weight: Incomplete | None = None):
    """Accuracy classification score.

    In multilabel classification, this function computes subset accuracy:
    the set of labels predicted for a sample must *exactly* match the
    corresponding set of labels in y_true.

    Read more in the :ref:`User Guide <accuracy_score>`.

    Parameters
    ----------
    y_true : 1d array-like, or label indicator array / sparse matrix
        Ground truth (correct) labels.

    y_pred : 1d array-like, or label indicator array / sparse matrix
        Predicted labels, as returned by a classifier.

    normalize : bool, default=True
        If ``False``, return the number of correctly classified samples.
        Otherwise, return the fraction of correctly classified samples.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    Returns
    -------
    score : float
        If ``normalize == True``, return the fraction of correctly
        classified samples (float), else returns the number of correctly
        classified samples (int).

        The best performance is 1 with ``normalize == True`` and the number
        of samples with ``normalize == False``.

    See Also
    --------
    balanced_accuracy_score : Compute the balanced accuracy to deal with
        imbalanced datasets.
    jaccard_score : Compute the Jaccard similarity coefficient score.
    hamming_loss : Compute the average Hamming loss or Hamming distance between
        two sets of samples.
    zero_one_loss : Compute the Zero-one classification loss. By default, the
        function will return the percentage of imperfectly predicted subsets.

    Notes
    -----
    In binary classification, this function is equal to the `jaccard_score`
    function.

    Examples
    --------
    >>> from sklearn.metrics import accuracy_score
    >>> y_pred = [0, 2, 1, 3]
    >>> y_true = [0, 1, 2, 3]
    >>> accuracy_score(y_true, y_pred)
    0.5
    >>> accuracy_score(y_true, y_pred, normalize=False)
    2

    In the multilabel case with binary label indicators:

    >>> import numpy as np
    >>> accuracy_score(np.array([[0, 1], [1, 1]]), np.ones((2, 2)))
    0.5
    """
def confusion_matrix(y_true, y_pred, *, labels: Incomplete | None = None, sample_weight: Incomplete | None = None, normalize: Incomplete | None = None):
    '''Compute confusion matrix to evaluate the accuracy of a classification.

    By definition a confusion matrix :math:`C` is such that :math:`C_{i, j}`
    is equal to the number of observations known to be in group :math:`i` and
    predicted to be in group :math:`j`.

    Thus in binary classification, the count of true negatives is
    :math:`C_{0,0}`, false negatives is :math:`C_{1,0}`, true positives is
    :math:`C_{1,1}` and false positives is :math:`C_{0,1}`.

    Read more in the :ref:`User Guide <confusion_matrix>`.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        Ground truth (correct) target values.

    y_pred : array-like of shape (n_samples,)
        Estimated targets as returned by a classifier.

    labels : array-like of shape (n_classes), default=None
        List of labels to index the matrix. This may be used to reorder
        or select a subset of labels.
        If ``None`` is given, those that appear at least once
        in ``y_true`` or ``y_pred`` are used in sorted order.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

        .. versionadded:: 0.18

    normalize : {\'true\', \'pred\', \'all\'}, default=None
        Normalizes confusion matrix over the true (rows), predicted (columns)
        conditions or all the population. If None, confusion matrix will not be
        normalized.

    Returns
    -------
    C : ndarray of shape (n_classes, n_classes)
        Confusion matrix whose i-th row and j-th
        column entry indicates the number of
        samples with true label being i-th class
        and predicted label being j-th class.

    See Also
    --------
    ConfusionMatrixDisplay.from_estimator : Plot the confusion matrix
        given an estimator, the data, and the label.
    ConfusionMatrixDisplay.from_predictions : Plot the confusion matrix
        given the true and predicted labels.
    ConfusionMatrixDisplay : Confusion Matrix visualization.

    References
    ----------
    .. [1] `Wikipedia entry for the Confusion matrix
           <https://en.wikipedia.org/wiki/Confusion_matrix>`_
           (Wikipedia and other references may use a different
           convention for axes).

    Examples
    --------
    >>> from sklearn.metrics import confusion_matrix
    >>> y_true = [2, 0, 2, 2, 0, 1]
    >>> y_pred = [0, 0, 2, 2, 0, 2]
    >>> confusion_matrix(y_true, y_pred)
    array([[2, 0, 0],
           [0, 0, 1],
           [1, 0, 2]])

    >>> y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
    >>> y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]
    >>> confusion_matrix(y_true, y_pred, labels=["ant", "bird", "cat"])
    array([[2, 0, 0],
           [0, 0, 1],
           [1, 0, 2]])

    In the binary case, we can extract true positives, etc. as follows:

    >>> tn, fp, fn, tp = confusion_matrix([0, 1, 0, 1], [1, 1, 1, 0]).ravel()
    >>> (tn, fp, fn, tp)
    (0, 2, 1, 1)
    '''
def multilabel_confusion_matrix(y_true, y_pred, *, sample_weight: Incomplete | None = None, labels: Incomplete | None = None, samplewise: bool = False):
    '''Compute a confusion matrix for each class or sample.

    .. versionadded:: 0.21

    Compute class-wise (default) or sample-wise (samplewise=True) multilabel
    confusion matrix to evaluate the accuracy of a classification, and output
    confusion matrices for each class or sample.

    In multilabel confusion matrix :math:`MCM`, the count of true negatives
    is :math:`MCM_{:,0,0}`, false negatives is :math:`MCM_{:,1,0}`,
    true positives is :math:`MCM_{:,1,1}` and false positives is
    :math:`MCM_{:,0,1}`.

    Multiclass data will be treated as if binarized under a one-vs-rest
    transformation. Returned confusion matrices will be in the order of
    sorted unique labels in the union of (y_true, y_pred).

    Read more in the :ref:`User Guide <multilabel_confusion_matrix>`.

    Parameters
    ----------
    y_true : {array-like, sparse matrix} of shape (n_samples, n_outputs) or             (n_samples,)
        Ground truth (correct) target values.

    y_pred : {array-like, sparse matrix} of shape (n_samples, n_outputs) or             (n_samples,)
        Estimated targets as returned by a classifier.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    labels : array-like of shape (n_classes,), default=None
        A list of classes or column indices to select some (or to force
        inclusion of classes absent from the data).

    samplewise : bool, default=False
        In the multilabel case, this calculates a confusion matrix per sample.

    Returns
    -------
    multi_confusion : ndarray of shape (n_outputs, 2, 2)
        A 2x2 confusion matrix corresponding to each output in the input.
        When calculating class-wise multi_confusion (default), then
        n_outputs = n_labels; when calculating sample-wise multi_confusion
        (samplewise=True), n_outputs = n_samples. If ``labels`` is defined,
        the results will be returned in the order specified in ``labels``,
        otherwise the results will be returned in sorted order by default.

    See Also
    --------
    confusion_matrix : Compute confusion matrix to evaluate the accuracy of a
        classifier.

    Notes
    -----
    The `multilabel_confusion_matrix` calculates class-wise or sample-wise
    multilabel confusion matrices, and in multiclass tasks, labels are
    binarized under a one-vs-rest way; while
    :func:`~sklearn.metrics.confusion_matrix` calculates one confusion matrix
    for confusion between every two classes.

    Examples
    --------
    Multilabel-indicator case:

    >>> import numpy as np
    >>> from sklearn.metrics import multilabel_confusion_matrix
    >>> y_true = np.array([[1, 0, 1],
    ...                    [0, 1, 0]])
    >>> y_pred = np.array([[1, 0, 0],
    ...                    [0, 1, 1]])
    >>> multilabel_confusion_matrix(y_true, y_pred)
    array([[[1, 0],
            [0, 1]],
    <BLANKLINE>
           [[1, 0],
            [0, 1]],
    <BLANKLINE>
           [[0, 1],
            [1, 0]]])

    Multiclass case:

    >>> y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
    >>> y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]
    >>> multilabel_confusion_matrix(y_true, y_pred,
    ...                             labels=["ant", "bird", "cat"])
    array([[[3, 1],
            [0, 2]],
    <BLANKLINE>
           [[5, 0],
            [1, 0]],
    <BLANKLINE>
           [[2, 1],
            [1, 2]]])
    '''
def cohen_kappa_score(y1, y2, *, labels: Incomplete | None = None, weights: Incomplete | None = None, sample_weight: Incomplete | None = None):
    '''Compute Cohen\'s kappa: a statistic that measures inter-annotator agreement.

    This function computes Cohen\'s kappa [1]_, a score that expresses the level
    of agreement between two annotators on a classification problem. It is
    defined as

    .. math::
        \\kappa = (p_o - p_e) / (1 - p_e)

    where :math:`p_o` is the empirical probability of agreement on the label
    assigned to any sample (the observed agreement ratio), and :math:`p_e` is
    the expected agreement when both annotators assign labels randomly.
    :math:`p_e` is estimated using a per-annotator empirical prior over the
    class labels [2]_.

    Read more in the :ref:`User Guide <cohen_kappa>`.

    Parameters
    ----------
    y1 : array-like of shape (n_samples,)
        Labels assigned by the first annotator.

    y2 : array-like of shape (n_samples,)
        Labels assigned by the second annotator. The kappa statistic is
        symmetric, so swapping ``y1`` and ``y2`` doesn\'t change the value.

    labels : array-like of shape (n_classes,), default=None
        List of labels to index the matrix. This may be used to select a
        subset of labels. If `None`, all labels that appear at least once in
        ``y1`` or ``y2`` are used.

    weights : {\'linear\', \'quadratic\'}, default=None
        Weighting type to calculate the score. `None` means no weighted;
        "linear" means linear weighted; "quadratic" means quadratic weighted.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    Returns
    -------
    kappa : float
        The kappa statistic, which is a number between -1 and 1. The maximum
        value means complete agreement; zero or lower means chance agreement.

    References
    ----------
    .. [1] :doi:`J. Cohen (1960). "A coefficient of agreement for nominal scales".
           Educational and Psychological Measurement 20(1):37-46.
           <10.1177/001316446002000104>`
    .. [2] `R. Artstein and M. Poesio (2008). "Inter-coder agreement for
           computational linguistics". Computational Linguistics 34(4):555-596
           <https://www.mitpressjournals.org/doi/pdf/10.1162/coli.07-034-R2>`_.
    .. [3] `Wikipedia entry for the Cohen\'s kappa
            <https://en.wikipedia.org/wiki/Cohen%27s_kappa>`_.
    '''
def jaccard_score(y_true, y_pred, *, labels: Incomplete | None = None, pos_label: int = 1, average: str = 'binary', sample_weight: Incomplete | None = None, zero_division: str = 'warn'):
    '''Jaccard similarity coefficient score.

    The Jaccard index [1], or Jaccard similarity coefficient, defined as
    the size of the intersection divided by the size of the union of two label
    sets, is used to compare set of predicted labels for a sample to the
    corresponding set of labels in ``y_true``.

    Read more in the :ref:`User Guide <jaccard_similarity_score>`.

    Parameters
    ----------
    y_true : 1d array-like, or label indicator array / sparse matrix
        Ground truth (correct) labels.

    y_pred : 1d array-like, or label indicator array / sparse matrix
        Predicted labels, as returned by a classifier.

    labels : array-like of shape (n_classes,), default=None
        The set of labels to include when ``average != \'binary\'``, and their
        order if ``average is None``. Labels present in the data can be
        excluded, for example to calculate a multiclass average ignoring a
        majority negative class, while labels not present in the data will
        result in 0 components in a macro average. For multilabel targets,
        labels are column indices. By default, all labels in ``y_true`` and
        ``y_pred`` are used in sorted order.

    pos_label : int, float, bool or str, default=1
        The class to report if ``average=\'binary\'`` and the data is binary.
        If the data are multiclass or multilabel, this will be ignored;
        setting ``labels=[pos_label]`` and ``average != \'binary\'`` will report
        scores for that label only.

    average : {\'micro\', \'macro\', \'samples\', \'weighted\',             \'binary\'} or None, default=\'binary\'
        If ``None``, the scores for each class are returned. Otherwise, this
        determines the type of averaging performed on the data:

        ``\'binary\'``:
            Only report results for the class specified by ``pos_label``.
            This is applicable only if targets (``y_{true,pred}``) are binary.
        ``\'micro\'``:
            Calculate metrics globally by counting the total true positives,
            false negatives and false positives.
        ``\'macro\'``:
            Calculate metrics for each label, and find their unweighted
            mean.  This does not take label imbalance into account.
        ``\'weighted\'``:
            Calculate metrics for each label, and find their average, weighted
            by support (the number of true instances for each label). This
            alters \'macro\' to account for label imbalance.
        ``\'samples\'``:
            Calculate metrics for each instance, and find their average (only
            meaningful for multilabel classification).

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    zero_division : "warn", {0.0, 1.0}, default="warn"
        Sets the value to return when there is a zero division, i.e. when there
        there are no negative values in predictions and labels. If set to
        "warn", this acts like 0, but a warning is also raised.

    Returns
    -------
    score : float or ndarray of shape (n_unique_labels,), dtype=np.float64
        The Jaccard score. When `average` is not `None`, a single scalar is
        returned.

    See Also
    --------
    accuracy_score : Function for calculating the accuracy score.
    f1_score : Function for calculating the F1 score.
    multilabel_confusion_matrix : Function for computing a confusion matrix                                  for each class or sample.

    Notes
    -----
    :func:`jaccard_score` may be a poor metric if there are no
    positives for some samples or classes. Jaccard is undefined if there are
    no true or predicted labels, and our implementation will return a score
    of 0 with a warning.

    References
    ----------
    .. [1] `Wikipedia entry for the Jaccard index
           <https://en.wikipedia.org/wiki/Jaccard_index>`_.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.metrics import jaccard_score
    >>> y_true = np.array([[0, 1, 1],
    ...                    [1, 1, 0]])
    >>> y_pred = np.array([[1, 1, 1],
    ...                    [1, 0, 0]])

    In the binary case:

    >>> jaccard_score(y_true[0], y_pred[0])
    0.6666...

    In the 2D comparison case (e.g. image similarity):

    >>> jaccard_score(y_true, y_pred, average="micro")
    0.6

    In the multilabel case:

    >>> jaccard_score(y_true, y_pred, average=\'samples\')
    0.5833...
    >>> jaccard_score(y_true, y_pred, average=\'macro\')
    0.6666...
    >>> jaccard_score(y_true, y_pred, average=None)
    array([0.5, 0.5, 1. ])

    In the multiclass case:

    >>> y_pred = [0, 2, 1, 2]
    >>> y_true = [0, 1, 2, 2]
    >>> jaccard_score(y_true, y_pred, average=None)
    array([1. , 0. , 0.33...])
    '''
def matthews_corrcoef(y_true, y_pred, *, sample_weight: Incomplete | None = None):
    """Compute the Matthews correlation coefficient (MCC).

    The Matthews correlation coefficient is used in machine learning as a
    measure of the quality of binary and multiclass classifications. It takes
    into account true and false positives and negatives and is generally
    regarded as a balanced measure which can be used even if the classes are of
    very different sizes. The MCC is in essence a correlation coefficient value
    between -1 and +1. A coefficient of +1 represents a perfect prediction, 0
    an average random prediction and -1 an inverse prediction.  The statistic
    is also known as the phi coefficient. [source: Wikipedia]

    Binary and multiclass labels are supported.  Only in the binary case does
    this relate to information about true and false positives and negatives.
    See references below.

    Read more in the :ref:`User Guide <matthews_corrcoef>`.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        Ground truth (correct) target values.

    y_pred : array-like of shape (n_samples,)
        Estimated targets as returned by a classifier.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

        .. versionadded:: 0.18

    Returns
    -------
    mcc : float
        The Matthews correlation coefficient (+1 represents a perfect
        prediction, 0 an average random prediction and -1 and inverse
        prediction).

    References
    ----------
    .. [1] :doi:`Baldi, Brunak, Chauvin, Andersen and Nielsen, (2000). Assessing the
       accuracy of prediction algorithms for classification: an overview.
       <10.1093/bioinformatics/16.5.412>`

    .. [2] `Wikipedia entry for the Matthews Correlation Coefficient
       <https://en.wikipedia.org/wiki/Matthews_correlation_coefficient>`_.

    .. [3] `Gorodkin, (2004). Comparing two K-category assignments by a
        K-category correlation coefficient
        <https://www.sciencedirect.com/science/article/pii/S1476927104000799>`_.

    .. [4] `Jurman, Riccadonna, Furlanello, (2012). A Comparison of MCC and CEN
        Error Measures in MultiClass Prediction
        <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0041882>`_.

    Examples
    --------
    >>> from sklearn.metrics import matthews_corrcoef
    >>> y_true = [+1, +1, +1, -1]
    >>> y_pred = [+1, -1, +1, +1]
    >>> matthews_corrcoef(y_true, y_pred)
    -0.33...
    """
def zero_one_loss(y_true, y_pred, *, normalize: bool = True, sample_weight: Incomplete | None = None):
    """Zero-one classification loss.

    If normalize is ``True``, return the fraction of misclassifications
    (float), else it returns the number of misclassifications (int). The best
    performance is 0.

    Read more in the :ref:`User Guide <zero_one_loss>`.

    Parameters
    ----------
    y_true : 1d array-like, or label indicator array / sparse matrix
        Ground truth (correct) labels.

    y_pred : 1d array-like, or label indicator array / sparse matrix
        Predicted labels, as returned by a classifier.

    normalize : bool, default=True
        If ``False``, return the number of misclassifications.
        Otherwise, return the fraction of misclassifications.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    Returns
    -------
    loss : float or int,
        If ``normalize == True``, return the fraction of misclassifications
        (float), else it returns the number of misclassifications (int).

    See Also
    --------
    accuracy_score : Compute the accuracy score. By default, the function will
        return the fraction of correct predictions divided by the total number
        of predictions.
    hamming_loss : Compute the average Hamming loss or Hamming distance between
        two sets of samples.
    jaccard_score : Compute the Jaccard similarity coefficient score.

    Notes
    -----
    In multilabel classification, the zero_one_loss function corresponds to
    the subset zero-one loss: for each sample, the entire set of labels must be
    correctly predicted, otherwise the loss for that sample is equal to one.

    Examples
    --------
    >>> from sklearn.metrics import zero_one_loss
    >>> y_pred = [1, 2, 3, 4]
    >>> y_true = [2, 2, 3, 4]
    >>> zero_one_loss(y_true, y_pred)
    0.25
    >>> zero_one_loss(y_true, y_pred, normalize=False)
    1

    In the multilabel case with binary label indicators:

    >>> import numpy as np
    >>> zero_one_loss(np.array([[0, 1], [1, 1]]), np.ones((2, 2)))
    0.5
    """
def f1_score(y_true, y_pred, *, labels: Incomplete | None = None, pos_label: int = 1, average: str = 'binary', sample_weight: Incomplete | None = None, zero_division: str = 'warn'):
    '''Compute the F1 score, also known as balanced F-score or F-measure.

    The F1 score can be interpreted as a harmonic mean of the precision and
    recall, where an F1 score reaches its best value at 1 and worst score at 0.
    The relative contribution of precision and recall to the F1 score are
    equal. The formula for the F1 score is::

        F1 = 2 * (precision * recall) / (precision + recall)

    In the multi-class and multi-label case, this is the average of
    the F1 score of each class with weighting depending on the ``average``
    parameter.

    Read more in the :ref:`User Guide <precision_recall_f_measure_metrics>`.

    Parameters
    ----------
    y_true : 1d array-like, or label indicator array / sparse matrix
        Ground truth (correct) target values.

    y_pred : 1d array-like, or label indicator array / sparse matrix
        Estimated targets as returned by a classifier.

    labels : array-like, default=None
        The set of labels to include when ``average != \'binary\'``, and their
        order if ``average is None``. Labels present in the data can be
        excluded, for example to calculate a multiclass average ignoring a
        majority negative class, while labels not present in the data will
        result in 0 components in a macro average. For multilabel targets,
        labels are column indices. By default, all labels in ``y_true`` and
        ``y_pred`` are used in sorted order.

        .. versionchanged:: 0.17
           Parameter `labels` improved for multiclass problem.

    pos_label : int, float, bool, str or None, default=1
        The class to report if ``average=\'binary\'`` and the data is binary.
        If the data are multiclass or multilabel, this will be ignored;
        setting ``labels=[pos_label]`` and ``average != \'binary\'`` will report
        scores for that label only.

    average : {\'micro\', \'macro\', \'samples\', \'weighted\', \'binary\'} or None,             default=\'binary\'
        This parameter is required for multiclass/multilabel targets.
        If ``None``, the scores for each class are returned. Otherwise, this
        determines the type of averaging performed on the data:

        ``\'binary\'``:
            Only report results for the class specified by ``pos_label``.
            This is applicable only if targets (``y_{true,pred}``) are binary.
        ``\'micro\'``:
            Calculate metrics globally by counting the total true positives,
            false negatives and false positives.
        ``\'macro\'``:
            Calculate metrics for each label, and find their unweighted
            mean.  This does not take label imbalance into account.
        ``\'weighted\'``:
            Calculate metrics for each label, and find their average weighted
            by support (the number of true instances for each label). This
            alters \'macro\' to account for label imbalance; it can result in an
            F-score that is not between precision and recall.
        ``\'samples\'``:
            Calculate metrics for each instance, and find their average (only
            meaningful for multilabel classification where this differs from
            :func:`accuracy_score`).

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    zero_division : {"warn", 0.0, 1.0, np.nan}, default="warn"
        Sets the value to return when there is a zero division, i.e. when all
        predictions and labels are negative.

        Notes:
        - If set to "warn", this acts like 0, but a warning is also raised.
        - If set to `np.nan`, such values will be excluded from the average.

        .. versionadded:: 1.3
           `np.nan` option was added.

    Returns
    -------
    f1_score : float or array of float, shape = [n_unique_labels]
        F1 score of the positive class in binary classification or weighted
        average of the F1 scores of each class for the multiclass task.

    See Also
    --------
    fbeta_score : Compute the F-beta score.
    precision_recall_fscore_support : Compute the precision, recall, F-score,
        and support.
    jaccard_score : Compute the Jaccard similarity coefficient score.
    multilabel_confusion_matrix : Compute a confusion matrix for each class or
        sample.

    Notes
    -----
    When ``true positive + false positive == 0``, precision is undefined.
    When ``true positive + false negative == 0``, recall is undefined.
    In such cases, by default the metric will be set to 0, as will f-score,
    and ``UndefinedMetricWarning`` will be raised. This behavior can be
    modified with ``zero_division``. Note that if `zero_division` is np.nan,
    scores being `np.nan` will be ignored for averaging.

    References
    ----------
    .. [1] `Wikipedia entry for the F1-score
           <https://en.wikipedia.org/wiki/F1_score>`_.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.metrics import f1_score
    >>> y_true = [0, 1, 2, 0, 1, 2]
    >>> y_pred = [0, 2, 1, 0, 0, 1]
    >>> f1_score(y_true, y_pred, average=\'macro\')
    0.26...
    >>> f1_score(y_true, y_pred, average=\'micro\')
    0.33...
    >>> f1_score(y_true, y_pred, average=\'weighted\')
    0.26...
    >>> f1_score(y_true, y_pred, average=None)
    array([0.8, 0. , 0. ])

    >>> # binary classification
    >>> y_true_empty = [0, 0, 0, 0, 0, 0]
    >>> y_pred_empty = [0, 0, 0, 0, 0, 0]
    >>> f1_score(y_true_empty, y_pred_empty)
    0.0...
    >>> f1_score(y_true_empty, y_pred_empty, zero_division=1.0)
    1.0...
    >>> f1_score(y_true_empty, y_pred_empty, zero_division=np.nan)
    nan...

    >>> # multilabel classification
    >>> y_true = [[0, 0, 0], [1, 1, 1], [0, 1, 1]]
    >>> y_pred = [[0, 0, 0], [1, 1, 1], [1, 1, 0]]
    >>> f1_score(y_true, y_pred, average=None)
    array([0.66666667, 1.        , 0.66666667])
    '''
def fbeta_score(y_true, y_pred, *, beta, labels: Incomplete | None = None, pos_label: int = 1, average: str = 'binary', sample_weight: Incomplete | None = None, zero_division: str = 'warn'):
    '''Compute the F-beta score.

    The F-beta score is the weighted harmonic mean of precision and recall,
    reaching its optimal value at 1 and its worst value at 0.

    The `beta` parameter represents the ratio of recall importance to
    precision importance. `beta > 1` gives more weight to recall, while
    `beta < 1` favors precision. For example, `beta = 2` makes recall twice
    as important as precision, while `beta = 0.5` does the opposite.
    Asymptotically, `beta -> +inf` considers only recall, and `beta -> 0`
    only precision.

    Read more in the :ref:`User Guide <precision_recall_f_measure_metrics>`.

    Parameters
    ----------
    y_true : 1d array-like, or label indicator array / sparse matrix
        Ground truth (correct) target values.

    y_pred : 1d array-like, or label indicator array / sparse matrix
        Estimated targets as returned by a classifier.

    beta : float
        Determines the weight of recall in the combined score.

    labels : array-like, default=None
        The set of labels to include when ``average != \'binary\'``, and their
        order if ``average is None``. Labels present in the data can be
        excluded, for example to calculate a multiclass average ignoring a
        majority negative class, while labels not present in the data will
        result in 0 components in a macro average. For multilabel targets,
        labels are column indices. By default, all labels in ``y_true`` and
        ``y_pred`` are used in sorted order.

        .. versionchanged:: 0.17
           Parameter `labels` improved for multiclass problem.

    pos_label : int, float, bool or str, default=1
        The class to report if ``average=\'binary\'`` and the data is binary.
        If the data are multiclass or multilabel, this will be ignored;
        setting ``labels=[pos_label]`` and ``average != \'binary\'`` will report
        scores for that label only.

    average : {\'micro\', \'macro\', \'samples\', \'weighted\', \'binary\'} or None,             default=\'binary\'
        This parameter is required for multiclass/multilabel targets.
        If ``None``, the scores for each class are returned. Otherwise, this
        determines the type of averaging performed on the data:

        ``\'binary\'``:
            Only report results for the class specified by ``pos_label``.
            This is applicable only if targets (``y_{true,pred}``) are binary.
        ``\'micro\'``:
            Calculate metrics globally by counting the total true positives,
            false negatives and false positives.
        ``\'macro\'``:
            Calculate metrics for each label, and find their unweighted
            mean.  This does not take label imbalance into account.
        ``\'weighted\'``:
            Calculate metrics for each label, and find their average weighted
            by support (the number of true instances for each label). This
            alters \'macro\' to account for label imbalance; it can result in an
            F-score that is not between precision and recall.
        ``\'samples\'``:
            Calculate metrics for each instance, and find their average (only
            meaningful for multilabel classification where this differs from
            :func:`accuracy_score`).

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    zero_division : {"warn", 0.0, 1.0, np.nan}, default="warn"
        Sets the value to return when there is a zero division, i.e. when all
        predictions and labels are negative.

        Notes:
        - If set to "warn", this acts like 0, but a warning is also raised.
        - If set to `np.nan`, such values will be excluded from the average.

        .. versionadded:: 1.3
           `np.nan` option was added.

    Returns
    -------
    fbeta_score : float (if average is not None) or array of float, shape =        [n_unique_labels]
        F-beta score of the positive class in binary classification or weighted
        average of the F-beta score of each class for the multiclass task.

    See Also
    --------
    precision_recall_fscore_support : Compute the precision, recall, F-score,
        and support.
    multilabel_confusion_matrix : Compute a confusion matrix for each class or
        sample.

    Notes
    -----
    When ``true positive + false positive == 0`` or
    ``true positive + false negative == 0``, f-score returns 0 and raises
    ``UndefinedMetricWarning``. This behavior can be
    modified with ``zero_division``.

    References
    ----------
    .. [1] R. Baeza-Yates and B. Ribeiro-Neto (2011).
           Modern Information Retrieval. Addison Wesley, pp. 327-328.

    .. [2] `Wikipedia entry for the F1-score
           <https://en.wikipedia.org/wiki/F1_score>`_.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.metrics import fbeta_score
    >>> y_true = [0, 1, 2, 0, 1, 2]
    >>> y_pred = [0, 2, 1, 0, 0, 1]
    >>> fbeta_score(y_true, y_pred, average=\'macro\', beta=0.5)
    0.23...
    >>> fbeta_score(y_true, y_pred, average=\'micro\', beta=0.5)
    0.33...
    >>> fbeta_score(y_true, y_pred, average=\'weighted\', beta=0.5)
    0.23...
    >>> fbeta_score(y_true, y_pred, average=None, beta=0.5)
    array([0.71..., 0.        , 0.        ])
    >>> y_pred_empty = [0, 0, 0, 0, 0, 0]
    >>> fbeta_score(y_true, y_pred_empty,
    ...             average="macro", zero_division=np.nan, beta=0.5)
    0.38...
    '''
def precision_recall_fscore_support(y_true, y_pred, *, beta: float = 1.0, labels: Incomplete | None = None, pos_label: int = 1, average: Incomplete | None = None, warn_for=('precision', 'recall', 'f-score'), sample_weight: Incomplete | None = None, zero_division: str = 'warn'):
    '''Compute precision, recall, F-measure and support for each class.

    The precision is the ratio ``tp / (tp + fp)`` where ``tp`` is the number of
    true positives and ``fp`` the number of false positives. The precision is
    intuitively the ability of the classifier not to label a negative sample as
    positive.

    The recall is the ratio ``tp / (tp + fn)`` where ``tp`` is the number of
    true positives and ``fn`` the number of false negatives. The recall is
    intuitively the ability of the classifier to find all the positive samples.

    The F-beta score can be interpreted as a weighted harmonic mean of
    the precision and recall, where an F-beta score reaches its best
    value at 1 and worst score at 0.

    The F-beta score weights recall more than precision by a factor of
    ``beta``. ``beta == 1.0`` means recall and precision are equally important.

    The support is the number of occurrences of each class in ``y_true``.

    If ``pos_label is None`` and in binary classification, this function
    returns the average precision, recall and F-measure if ``average``
    is one of ``\'micro\'``, ``\'macro\'``, ``\'weighted\'`` or ``\'samples\'``.

    Read more in the :ref:`User Guide <precision_recall_f_measure_metrics>`.

    Parameters
    ----------
    y_true : 1d array-like, or label indicator array / sparse matrix
        Ground truth (correct) target values.

    y_pred : 1d array-like, or label indicator array / sparse matrix
        Estimated targets as returned by a classifier.

    beta : float, default=1.0
        The strength of recall versus precision in the F-score.

    labels : array-like, default=None
        The set of labels to include when ``average != \'binary\'``, and their
        order if ``average is None``. Labels present in the data can be
        excluded, for example to calculate a multiclass average ignoring a
        majority negative class, while labels not present in the data will
        result in 0 components in a macro average. For multilabel targets,
        labels are column indices. By default, all labels in ``y_true`` and
        ``y_pred`` are used in sorted order.

    pos_label : int, float, bool or str, default=1
        The class to report if ``average=\'binary\'`` and the data is binary.
        If the data are multiclass or multilabel, this will be ignored;
        setting ``labels=[pos_label]`` and ``average != \'binary\'`` will report
        scores for that label only.

    average : {\'binary\', \'micro\', \'macro\', \'samples\', \'weighted\'},             default=None
        If ``None``, the scores for each class are returned. Otherwise, this
        determines the type of averaging performed on the data:

        ``\'binary\'``:
            Only report results for the class specified by ``pos_label``.
            This is applicable only if targets (``y_{true,pred}``) are binary.
        ``\'micro\'``:
            Calculate metrics globally by counting the total true positives,
            false negatives and false positives.
        ``\'macro\'``:
            Calculate metrics for each label, and find their unweighted
            mean.  This does not take label imbalance into account.
        ``\'weighted\'``:
            Calculate metrics for each label, and find their average weighted
            by support (the number of true instances for each label). This
            alters \'macro\' to account for label imbalance; it can result in an
            F-score that is not between precision and recall.
        ``\'samples\'``:
            Calculate metrics for each instance, and find their average (only
            meaningful for multilabel classification where this differs from
            :func:`accuracy_score`).

    warn_for : list, tuple or set, for internal use
        This determines which warnings will be made in the case that this
        function is being used to return only one of its metrics.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    zero_division : {"warn", 0.0, 1.0, np.nan}, default="warn"
        Sets the value to return when there is a zero division:
           - recall: when there are no positive labels
           - precision: when there are no positive predictions
           - f-score: both

        Notes:
        - If set to "warn", this acts like 0, but a warning is also raised.
        - If set to `np.nan`, such values will be excluded from the average.

        .. versionadded:: 1.3
           `np.nan` option was added.

    Returns
    -------
    precision : float (if average is not None) or array of float, shape =        [n_unique_labels]
        Precision score.

    recall : float (if average is not None) or array of float, shape =        [n_unique_labels]
        Recall score.

    fbeta_score : float (if average is not None) or array of float, shape =        [n_unique_labels]
        F-beta score.

    support : None (if average is not None) or array of int, shape =        [n_unique_labels]
        The number of occurrences of each label in ``y_true``.

    Notes
    -----
    When ``true positive + false positive == 0``, precision is undefined.
    When ``true positive + false negative == 0``, recall is undefined.
    In such cases, by default the metric will be set to 0, as will f-score,
    and ``UndefinedMetricWarning`` will be raised. This behavior can be
    modified with ``zero_division``.

    References
    ----------
    .. [1] `Wikipedia entry for the Precision and recall
           <https://en.wikipedia.org/wiki/Precision_and_recall>`_.

    .. [2] `Wikipedia entry for the F1-score
           <https://en.wikipedia.org/wiki/F1_score>`_.

    .. [3] `Discriminative Methods for Multi-labeled Classification Advances
           in Knowledge Discovery and Data Mining (2004), pp. 22-30 by Shantanu
           Godbole, Sunita Sarawagi
           <http://www.godbole.net/shantanu/pubs/multilabelsvm-pakdd04.pdf>`_.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.metrics import precision_recall_fscore_support
    >>> y_true = np.array([\'cat\', \'dog\', \'pig\', \'cat\', \'dog\', \'pig\'])
    >>> y_pred = np.array([\'cat\', \'pig\', \'dog\', \'cat\', \'cat\', \'dog\'])
    >>> precision_recall_fscore_support(y_true, y_pred, average=\'macro\')
    (0.22..., 0.33..., 0.26..., None)
    >>> precision_recall_fscore_support(y_true, y_pred, average=\'micro\')
    (0.33..., 0.33..., 0.33..., None)
    >>> precision_recall_fscore_support(y_true, y_pred, average=\'weighted\')
    (0.22..., 0.33..., 0.26..., None)

    It is possible to compute per-label precisions, recalls, F1-scores and
    supports instead of averaging:

    >>> precision_recall_fscore_support(y_true, y_pred, average=None,
    ... labels=[\'pig\', \'dog\', \'cat\'])
    (array([0.        , 0.        , 0.66...]),
     array([0., 0., 1.]), array([0. , 0. , 0.8]),
     array([2, 2, 2]))
    '''
def class_likelihood_ratios(y_true, y_pred, *, labels: Incomplete | None = None, sample_weight: Incomplete | None = None, raise_warning: bool = True):
    '''Compute binary classification positive and negative likelihood ratios.

    The positive likelihood ratio is `LR+ = sensitivity / (1 - specificity)`
    where the sensitivity or recall is the ratio `tp / (tp + fn)` and the
    specificity is `tn / (tn + fp)`. The negative likelihood ratio is `LR- = (1
    - sensitivity) / specificity`. Here `tp` is the number of true positives,
    `fp` the number of false positives, `tn` is the number of true negatives and
    `fn` the number of false negatives. Both class likelihood ratios can be used
    to obtain post-test probabilities given a pre-test probability.

    `LR+` ranges from 1 to infinity. A `LR+` of 1 indicates that the probability
    of predicting the positive class is the same for samples belonging to either
    class; therefore, the test is useless. The greater `LR+` is, the more a
    positive prediction is likely to be a true positive when compared with the
    pre-test probability. A value of `LR+` lower than 1 is invalid as it would
    indicate that the odds of a sample being a true positive decrease with
    respect to the pre-test odds.

    `LR-` ranges from 0 to 1. The closer it is to 0, the lower the probability
    of a given sample to be a false negative. A `LR-` of 1 means the test is
    useless because the odds of having the condition did not change after the
    test. A value of `LR-` greater than 1 invalidates the classifier as it
    indicates an increase in the odds of a sample belonging to the positive
    class after being classified as negative. This is the case when the
    classifier systematically predicts the opposite of the true label.

    A typical application in medicine is to identify the positive/negative class
    to the presence/absence of a disease, respectively; the classifier being a
    diagnostic test; the pre-test probability of an individual having the
    disease can be the prevalence of such disease (proportion of a particular
    population found to be affected by a medical condition); and the post-test
    probabilities would be the probability that the condition is truly present
    given a positive test result.

    Read more in the :ref:`User Guide <class_likelihood_ratios>`.

    Parameters
    ----------
    y_true : 1d array-like, or label indicator array / sparse matrix
        Ground truth (correct) target values.

    y_pred : 1d array-like, or label indicator array / sparse matrix
        Estimated targets as returned by a classifier.

    labels : array-like, default=None
        List of labels to index the matrix. This may be used to select the
        positive and negative classes with the ordering `labels=[negative_class,
        positive_class]`. If `None` is given, those that appear at least once in
        `y_true` or `y_pred` are used in sorted order.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    raise_warning : bool, default=True
        Whether or not a case-specific warning message is raised when there is a
        zero division. Even if the error is not raised, the function will return
        nan in such cases.

    Returns
    -------
    (positive_likelihood_ratio, negative_likelihood_ratio) : tuple
        A tuple of two float, the first containing the Positive likelihood ratio
        and the second the Negative likelihood ratio.

    Warns
    -----
    When `false positive == 0`, the positive likelihood ratio is undefined.
    When `true negative == 0`, the negative likelihood ratio is undefined.
    When `true positive + false negative == 0` both ratios are undefined.
    In such cases, `UserWarning` will be raised if raise_warning=True.

    References
    ----------
    .. [1] `Wikipedia entry for the Likelihood ratios in diagnostic testing
           <https://en.wikipedia.org/wiki/Likelihood_ratios_in_diagnostic_testing>`_.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.metrics import class_likelihood_ratios
    >>> class_likelihood_ratios([0, 1, 0, 1, 0], [1, 1, 0, 0, 0])
    (1.5, 0.75)
    >>> y_true = np.array(["non-cat", "cat", "non-cat", "cat", "non-cat"])
    >>> y_pred = np.array(["cat", "cat", "non-cat", "non-cat", "non-cat"])
    >>> class_likelihood_ratios(y_true, y_pred)
    (1.33..., 0.66...)
    >>> y_true = np.array(["non-zebra", "zebra", "non-zebra", "zebra", "non-zebra"])
    >>> y_pred = np.array(["zebra", "zebra", "non-zebra", "non-zebra", "non-zebra"])
    >>> class_likelihood_ratios(y_true, y_pred)
    (1.5, 0.75)

    To avoid ambiguities, use the notation `labels=[negative_class,
    positive_class]`

    >>> y_true = np.array(["non-cat", "cat", "non-cat", "cat", "non-cat"])
    >>> y_pred = np.array(["cat", "cat", "non-cat", "non-cat", "non-cat"])
    >>> class_likelihood_ratios(y_true, y_pred, labels=["non-cat", "cat"])
    (1.5, 0.75)
    '''
def precision_score(y_true, y_pred, *, labels: Incomplete | None = None, pos_label: int = 1, average: str = 'binary', sample_weight: Incomplete | None = None, zero_division: str = 'warn'):
    '''Compute the precision.

    The precision is the ratio ``tp / (tp + fp)`` where ``tp`` is the number of
    true positives and ``fp`` the number of false positives. The precision is
    intuitively the ability of the classifier not to label as positive a sample
    that is negative.

    The best value is 1 and the worst value is 0.

    Read more in the :ref:`User Guide <precision_recall_f_measure_metrics>`.

    Parameters
    ----------
    y_true : 1d array-like, or label indicator array / sparse matrix
        Ground truth (correct) target values.

    y_pred : 1d array-like, or label indicator array / sparse matrix
        Estimated targets as returned by a classifier.

    labels : array-like, default=None
        The set of labels to include when ``average != \'binary\'``, and their
        order if ``average is None``. Labels present in the data can be
        excluded, for example to calculate a multiclass average ignoring a
        majority negative class, while labels not present in the data will
        result in 0 components in a macro average. For multilabel targets,
        labels are column indices. By default, all labels in ``y_true`` and
        ``y_pred`` are used in sorted order.

        .. versionchanged:: 0.17
           Parameter `labels` improved for multiclass problem.

    pos_label : int, float, bool or str, default=1
        The class to report if ``average=\'binary\'`` and the data is binary.
        If the data are multiclass or multilabel, this will be ignored;
        setting ``labels=[pos_label]`` and ``average != \'binary\'`` will report
        scores for that label only.

    average : {\'micro\', \'macro\', \'samples\', \'weighted\', \'binary\'} or None,             default=\'binary\'
        This parameter is required for multiclass/multilabel targets.
        If ``None``, the scores for each class are returned. Otherwise, this
        determines the type of averaging performed on the data:

        ``\'binary\'``:
            Only report results for the class specified by ``pos_label``.
            This is applicable only if targets (``y_{true,pred}``) are binary.
        ``\'micro\'``:
            Calculate metrics globally by counting the total true positives,
            false negatives and false positives.
        ``\'macro\'``:
            Calculate metrics for each label, and find their unweighted
            mean.  This does not take label imbalance into account.
        ``\'weighted\'``:
            Calculate metrics for each label, and find their average weighted
            by support (the number of true instances for each label). This
            alters \'macro\' to account for label imbalance; it can result in an
            F-score that is not between precision and recall.
        ``\'samples\'``:
            Calculate metrics for each instance, and find their average (only
            meaningful for multilabel classification where this differs from
            :func:`accuracy_score`).

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    zero_division : {"warn", 0.0, 1.0, np.nan}, default="warn"
        Sets the value to return when there is a zero division.

        Notes:
        - If set to "warn", this acts like 0, but a warning is also raised.
        - If set to `np.nan`, such values will be excluded from the average.

        .. versionadded:: 1.3
           `np.nan` option was added.

    Returns
    -------
    precision : float (if average is not None) or array of float of shape                 (n_unique_labels,)
        Precision of the positive class in binary classification or weighted
        average of the precision of each class for the multiclass task.

    See Also
    --------
    precision_recall_fscore_support : Compute precision, recall, F-measure and
        support for each class.
    recall_score :  Compute the ratio ``tp / (tp + fn)`` where ``tp`` is the
        number of true positives and ``fn`` the number of false negatives.
    PrecisionRecallDisplay.from_estimator : Plot precision-recall curve given
        an estimator and some data.
    PrecisionRecallDisplay.from_predictions : Plot precision-recall curve given
        binary class predictions.
    multilabel_confusion_matrix : Compute a confusion matrix for each class or
        sample.

    Notes
    -----
    When ``true positive + false positive == 0``, precision returns 0 and
    raises ``UndefinedMetricWarning``. This behavior can be
    modified with ``zero_division``.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.metrics import precision_score
    >>> y_true = [0, 1, 2, 0, 1, 2]
    >>> y_pred = [0, 2, 1, 0, 0, 1]
    >>> precision_score(y_true, y_pred, average=\'macro\')
    0.22...
    >>> precision_score(y_true, y_pred, average=\'micro\')
    0.33...
    >>> precision_score(y_true, y_pred, average=\'weighted\')
    0.22...
    >>> precision_score(y_true, y_pred, average=None)
    array([0.66..., 0.        , 0.        ])
    >>> y_pred = [0, 0, 0, 0, 0, 0]
    >>> precision_score(y_true, y_pred, average=None)
    array([0.33..., 0.        , 0.        ])
    >>> precision_score(y_true, y_pred, average=None, zero_division=1)
    array([0.33..., 1.        , 1.        ])
    >>> precision_score(y_true, y_pred, average=None, zero_division=np.nan)
    array([0.33...,        nan,        nan])

    >>> # multilabel classification
    >>> y_true = [[0, 0, 0], [1, 1, 1], [0, 1, 1]]
    >>> y_pred = [[0, 0, 0], [1, 1, 1], [1, 1, 0]]
    >>> precision_score(y_true, y_pred, average=None)
    array([0.5, 1. , 1. ])
    '''
def recall_score(y_true, y_pred, *, labels: Incomplete | None = None, pos_label: int = 1, average: str = 'binary', sample_weight: Incomplete | None = None, zero_division: str = 'warn'):
    '''Compute the recall.

    The recall is the ratio ``tp / (tp + fn)`` where ``tp`` is the number of
    true positives and ``fn`` the number of false negatives. The recall is
    intuitively the ability of the classifier to find all the positive samples.

    The best value is 1 and the worst value is 0.

    Read more in the :ref:`User Guide <precision_recall_f_measure_metrics>`.

    Parameters
    ----------
    y_true : 1d array-like, or label indicator array / sparse matrix
        Ground truth (correct) target values.

    y_pred : 1d array-like, or label indicator array / sparse matrix
        Estimated targets as returned by a classifier.

    labels : array-like, default=None
        The set of labels to include when ``average != \'binary\'``, and their
        order if ``average is None``. Labels present in the data can be
        excluded, for example to calculate a multiclass average ignoring a
        majority negative class, while labels not present in the data will
        result in 0 components in a macro average. For multilabel targets,
        labels are column indices. By default, all labels in ``y_true`` and
        ``y_pred`` are used in sorted order.

        .. versionchanged:: 0.17
           Parameter `labels` improved for multiclass problem.

    pos_label : int, float, bool or str, default=1
        The class to report if ``average=\'binary\'`` and the data is binary.
        If the data are multiclass or multilabel, this will be ignored;
        setting ``labels=[pos_label]`` and ``average != \'binary\'`` will report
        scores for that label only.

    average : {\'micro\', \'macro\', \'samples\', \'weighted\', \'binary\'} or None,             default=\'binary\'
        This parameter is required for multiclass/multilabel targets.
        If ``None``, the scores for each class are returned. Otherwise, this
        determines the type of averaging performed on the data:

        ``\'binary\'``:
            Only report results for the class specified by ``pos_label``.
            This is applicable only if targets (``y_{true,pred}``) are binary.
        ``\'micro\'``:
            Calculate metrics globally by counting the total true positives,
            false negatives and false positives.
        ``\'macro\'``:
            Calculate metrics for each label, and find their unweighted
            mean.  This does not take label imbalance into account.
        ``\'weighted\'``:
            Calculate metrics for each label, and find their average weighted
            by support (the number of true instances for each label). This
            alters \'macro\' to account for label imbalance; it can result in an
            F-score that is not between precision and recall. Weighted recall
            is equal to accuracy.
        ``\'samples\'``:
            Calculate metrics for each instance, and find their average (only
            meaningful for multilabel classification where this differs from
            :func:`accuracy_score`).

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    zero_division : {"warn", 0.0, 1.0, np.nan}, default="warn"
        Sets the value to return when there is a zero division.

        Notes:
        - If set to "warn", this acts like 0, but a warning is also raised.
        - If set to `np.nan`, such values will be excluded from the average.

        .. versionadded:: 1.3
           `np.nan` option was added.

    Returns
    -------
    recall : float (if average is not None) or array of float of shape              (n_unique_labels,)
        Recall of the positive class in binary classification or weighted
        average of the recall of each class for the multiclass task.

    See Also
    --------
    precision_recall_fscore_support : Compute precision, recall, F-measure and
        support for each class.
    precision_score : Compute the ratio ``tp / (tp + fp)`` where ``tp`` is the
        number of true positives and ``fp`` the number of false positives.
    balanced_accuracy_score : Compute balanced accuracy to deal with imbalanced
        datasets.
    multilabel_confusion_matrix : Compute a confusion matrix for each class or
        sample.
    PrecisionRecallDisplay.from_estimator : Plot precision-recall curve given
        an estimator and some data.
    PrecisionRecallDisplay.from_predictions : Plot precision-recall curve given
        binary class predictions.

    Notes
    -----
    When ``true positive + false negative == 0``, recall returns 0 and raises
    ``UndefinedMetricWarning``. This behavior can be modified with
    ``zero_division``.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.metrics import recall_score
    >>> y_true = [0, 1, 2, 0, 1, 2]
    >>> y_pred = [0, 2, 1, 0, 0, 1]
    >>> recall_score(y_true, y_pred, average=\'macro\')
    0.33...
    >>> recall_score(y_true, y_pred, average=\'micro\')
    0.33...
    >>> recall_score(y_true, y_pred, average=\'weighted\')
    0.33...
    >>> recall_score(y_true, y_pred, average=None)
    array([1., 0., 0.])
    >>> y_true = [0, 0, 0, 0, 0, 0]
    >>> recall_score(y_true, y_pred, average=None)
    array([0.5, 0. , 0. ])
    >>> recall_score(y_true, y_pred, average=None, zero_division=1)
    array([0.5, 1. , 1. ])
    >>> recall_score(y_true, y_pred, average=None, zero_division=np.nan)
    array([0.5, nan, nan])

    >>> # multilabel classification
    >>> y_true = [[0, 0, 0], [1, 1, 1], [0, 1, 1]]
    >>> y_pred = [[0, 0, 0], [1, 1, 1], [1, 1, 0]]
    >>> recall_score(y_true, y_pred, average=None)
    array([1. , 1. , 0.5])
    '''
def balanced_accuracy_score(y_true, y_pred, *, sample_weight: Incomplete | None = None, adjusted: bool = False):
    """Compute the balanced accuracy.

    The balanced accuracy in binary and multiclass classification problems to
    deal with imbalanced datasets. It is defined as the average of recall
    obtained on each class.

    The best value is 1 and the worst value is 0 when ``adjusted=False``.

    Read more in the :ref:`User Guide <balanced_accuracy_score>`.

    .. versionadded:: 0.20

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        Ground truth (correct) target values.

    y_pred : array-like of shape (n_samples,)
        Estimated targets as returned by a classifier.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    adjusted : bool, default=False
        When true, the result is adjusted for chance, so that random
        performance would score 0, while keeping perfect performance at a score
        of 1.

    Returns
    -------
    balanced_accuracy : float
        Balanced accuracy score.

    See Also
    --------
    average_precision_score : Compute average precision (AP) from prediction
        scores.
    precision_score : Compute the precision score.
    recall_score : Compute the recall score.
    roc_auc_score : Compute Area Under the Receiver Operating Characteristic
        Curve (ROC AUC) from prediction scores.

    Notes
    -----
    Some literature promotes alternative definitions of balanced accuracy. Our
    definition is equivalent to :func:`accuracy_score` with class-balanced
    sample weights, and shares desirable properties with the binary case.
    See the :ref:`User Guide <balanced_accuracy_score>`.

    References
    ----------
    .. [1] Brodersen, K.H.; Ong, C.S.; Stephan, K.E.; Buhmann, J.M. (2010).
           The balanced accuracy and its posterior distribution.
           Proceedings of the 20th International Conference on Pattern
           Recognition, 3121-24.
    .. [2] John. D. Kelleher, Brian Mac Namee, Aoife D'Arcy, (2015).
           `Fundamentals of Machine Learning for Predictive Data Analytics:
           Algorithms, Worked Examples, and Case Studies
           <https://mitpress.mit.edu/books/fundamentals-machine-learning-predictive-data-analytics>`_.

    Examples
    --------
    >>> from sklearn.metrics import balanced_accuracy_score
    >>> y_true = [0, 1, 0, 0, 1, 0]
    >>> y_pred = [0, 1, 0, 0, 0, 1]
    >>> balanced_accuracy_score(y_true, y_pred)
    0.625
    """
def classification_report(y_true, y_pred, *, labels: Incomplete | None = None, target_names: Incomplete | None = None, sample_weight: Incomplete | None = None, digits: int = 2, output_dict: bool = False, zero_division: str = 'warn'):
    '''Build a text report showing the main classification metrics.

    Read more in the :ref:`User Guide <classification_report>`.

    Parameters
    ----------
    y_true : 1d array-like, or label indicator array / sparse matrix
        Ground truth (correct) target values.

    y_pred : 1d array-like, or label indicator array / sparse matrix
        Estimated targets as returned by a classifier.

    labels : array-like of shape (n_labels,), default=None
        Optional list of label indices to include in the report.

    target_names : array-like of shape (n_labels,), default=None
        Optional display names matching the labels (same order).

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    digits : int, default=2
        Number of digits for formatting output floating point values.
        When ``output_dict`` is ``True``, this will be ignored and the
        returned values will not be rounded.

    output_dict : bool, default=False
        If True, return output as dict.

        .. versionadded:: 0.20

    zero_division : {"warn", 0.0, 1.0, np.nan}, default="warn"
        Sets the value to return when there is a zero division. If set to
        "warn", this acts as 0, but warnings are also raised.

        .. versionadded:: 1.3
           `np.nan` option was added.

    Returns
    -------
    report : str or dict
        Text summary of the precision, recall, F1 score for each class.
        Dictionary returned if output_dict is True. Dictionary has the
        following structure::

            {\'label 1\': {\'precision\':0.5,
                         \'recall\':1.0,
                         \'f1-score\':0.67,
                         \'support\':1},
             \'label 2\': { ... },
              ...
            }

        The reported averages include macro average (averaging the unweighted
        mean per label), weighted average (averaging the support-weighted mean
        per label), and sample average (only for multilabel classification).
        Micro average (averaging the total true positives, false negatives and
        false positives) is only shown for multi-label or multi-class
        with a subset of classes, because it corresponds to accuracy
        otherwise and would be the same for all metrics.
        See also :func:`precision_recall_fscore_support` for more details
        on averages.

        Note that in binary classification, recall of the positive class
        is also known as "sensitivity"; recall of the negative class is
        "specificity".

    See Also
    --------
    precision_recall_fscore_support: Compute precision, recall, F-measure and
        support for each class.
    confusion_matrix: Compute confusion matrix to evaluate the accuracy of a
        classification.
    multilabel_confusion_matrix: Compute a confusion matrix for each class or sample.

    Examples
    --------
    >>> from sklearn.metrics import classification_report
    >>> y_true = [0, 1, 2, 2, 2]
    >>> y_pred = [0, 0, 2, 2, 1]
    >>> target_names = [\'class 0\', \'class 1\', \'class 2\']
    >>> print(classification_report(y_true, y_pred, target_names=target_names))
                  precision    recall  f1-score   support
    <BLANKLINE>
         class 0       0.50      1.00      0.67         1
         class 1       0.00      0.00      0.00         1
         class 2       1.00      0.67      0.80         3
    <BLANKLINE>
        accuracy                           0.60         5
       macro avg       0.50      0.56      0.49         5
    weighted avg       0.70      0.60      0.61         5
    <BLANKLINE>
    >>> y_pred = [1, 1, 0]
    >>> y_true = [1, 1, 1]
    >>> print(classification_report(y_true, y_pred, labels=[1, 2, 3]))
                  precision    recall  f1-score   support
    <BLANKLINE>
               1       1.00      0.67      0.80         3
               2       0.00      0.00      0.00         0
               3       0.00      0.00      0.00         0
    <BLANKLINE>
       micro avg       1.00      0.67      0.80         3
       macro avg       0.33      0.22      0.27         3
    weighted avg       1.00      0.67      0.80         3
    <BLANKLINE>
    '''
def hamming_loss(y_true, y_pred, *, sample_weight: Incomplete | None = None):
    """Compute the average Hamming loss.

    The Hamming loss is the fraction of labels that are incorrectly predicted.

    Read more in the :ref:`User Guide <hamming_loss>`.

    Parameters
    ----------
    y_true : 1d array-like, or label indicator array / sparse matrix
        Ground truth (correct) labels.

    y_pred : 1d array-like, or label indicator array / sparse matrix
        Predicted labels, as returned by a classifier.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

        .. versionadded:: 0.18

    Returns
    -------
    loss : float or int
        Return the average Hamming loss between element of ``y_true`` and
        ``y_pred``.

    See Also
    --------
    accuracy_score : Compute the accuracy score. By default, the function will
        return the fraction of correct predictions divided by the total number
        of predictions.
    jaccard_score : Compute the Jaccard similarity coefficient score.
    zero_one_loss : Compute the Zero-one classification loss. By default, the
        function will return the percentage of imperfectly predicted subsets.

    Notes
    -----
    In multiclass classification, the Hamming loss corresponds to the Hamming
    distance between ``y_true`` and ``y_pred`` which is equivalent to the
    subset ``zero_one_loss`` function, when `normalize` parameter is set to
    True.

    In multilabel classification, the Hamming loss is different from the
    subset zero-one loss. The zero-one loss considers the entire set of labels
    for a given sample incorrect if it does not entirely match the true set of
    labels. Hamming loss is more forgiving in that it penalizes only the
    individual labels.

    The Hamming loss is upperbounded by the subset zero-one loss, when
    `normalize` parameter is set to True. It is always between 0 and 1,
    lower being better.

    References
    ----------
    .. [1] Grigorios Tsoumakas, Ioannis Katakis. Multi-Label Classification:
           An Overview. International Journal of Data Warehousing & Mining,
           3(3), 1-13, July-September 2007.

    .. [2] `Wikipedia entry on the Hamming distance
           <https://en.wikipedia.org/wiki/Hamming_distance>`_.

    Examples
    --------
    >>> from sklearn.metrics import hamming_loss
    >>> y_pred = [1, 2, 3, 4]
    >>> y_true = [2, 2, 3, 4]
    >>> hamming_loss(y_true, y_pred)
    0.25

    In the multilabel case with binary label indicators:

    >>> import numpy as np
    >>> hamming_loss(np.array([[0, 1], [1, 1]]), np.zeros((2, 2)))
    0.75
    """
def log_loss(y_true, y_pred, *, eps: str = 'auto', normalize: bool = True, sample_weight: Incomplete | None = None, labels: Incomplete | None = None):
    '''Log loss, aka logistic loss or cross-entropy loss.

    This is the loss function used in (multinomial) logistic regression
    and extensions of it such as neural networks, defined as the negative
    log-likelihood of a logistic model that returns ``y_pred`` probabilities
    for its training data ``y_true``.
    The log loss is only defined for two or more labels.
    For a single sample with true label :math:`y \\in \\{0,1\\}` and
    a probability estimate :math:`p = \\operatorname{Pr}(y = 1)`, the log
    loss is:

    .. math::
        L_{\\log}(y, p) = -(y \\log (p) + (1 - y) \\log (1 - p))

    Read more in the :ref:`User Guide <log_loss>`.

    Parameters
    ----------
    y_true : array-like or label indicator matrix
        Ground truth (correct) labels for n_samples samples.

    y_pred : array-like of float, shape = (n_samples, n_classes) or (n_samples,)
        Predicted probabilities, as returned by a classifier\'s
        predict_proba method. If ``y_pred.shape = (n_samples,)``
        the probabilities provided are assumed to be that of the
        positive class. The labels in ``y_pred`` are assumed to be
        ordered alphabetically, as done by
        :class:`preprocessing.LabelBinarizer`.

    eps : float or "auto", default="auto"
        Log loss is undefined for p=0 or p=1, so probabilities are
        clipped to `max(eps, min(1 - eps, p))`. The default will depend on the
        data type of `y_pred` and is set to `np.finfo(y_pred.dtype).eps`.

        .. versionadded:: 1.2

        .. versionchanged:: 1.2
           The default value changed from `1e-15` to `"auto"` that is
           equivalent to `np.finfo(y_pred.dtype).eps`.

        .. deprecated:: 1.3
           `eps` is deprecated in 1.3 and will be removed in 1.5.

    normalize : bool, default=True
        If true, return the mean loss per sample.
        Otherwise, return the sum of the per-sample losses.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    labels : array-like, default=None
        If not provided, labels will be inferred from y_true. If ``labels``
        is ``None`` and ``y_pred`` has shape (n_samples,) the labels are
        assumed to be binary and are inferred from ``y_true``.

        .. versionadded:: 0.18

    Returns
    -------
    loss : float
        Log loss, aka logistic loss or cross-entropy loss.

    Notes
    -----
    The logarithm used is the natural logarithm (base-e).

    References
    ----------
    C.M. Bishop (2006). Pattern Recognition and Machine Learning. Springer,
    p. 209.

    Examples
    --------
    >>> from sklearn.metrics import log_loss
    >>> log_loss(["spam", "ham", "ham", "spam"],
    ...          [[.1, .9], [.9, .1], [.8, .2], [.35, .65]])
    0.21616...
    '''
def hinge_loss(y_true, pred_decision, *, labels: Incomplete | None = None, sample_weight: Incomplete | None = None):
    '''Average hinge loss (non-regularized).

    In binary class case, assuming labels in y_true are encoded with +1 and -1,
    when a prediction mistake is made, ``margin = y_true * pred_decision`` is
    always negative (since the signs disagree), implying ``1 - margin`` is
    always greater than 1.  The cumulated hinge loss is therefore an upper
    bound of the number of mistakes made by the classifier.

    In multiclass case, the function expects that either all the labels are
    included in y_true or an optional labels argument is provided which
    contains all the labels. The multilabel margin is calculated according
    to Crammer-Singer\'s method. As in the binary case, the cumulated hinge loss
    is an upper bound of the number of mistakes made by the classifier.

    Read more in the :ref:`User Guide <hinge_loss>`.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True target, consisting of integers of two values. The positive label
        must be greater than the negative label.

    pred_decision : array-like of shape (n_samples,) or (n_samples, n_classes)
        Predicted decisions, as output by decision_function (floats).

    labels : array-like, default=None
        Contains all the labels for the problem. Used in multiclass hinge loss.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    Returns
    -------
    loss : float
        Average hinge loss.

    References
    ----------
    .. [1] `Wikipedia entry on the Hinge loss
           <https://en.wikipedia.org/wiki/Hinge_loss>`_.

    .. [2] Koby Crammer, Yoram Singer. On the Algorithmic
           Implementation of Multiclass Kernel-based Vector
           Machines. Journal of Machine Learning Research 2,
           (2001), 265-292.

    .. [3] `L1 AND L2 Regularization for Multiclass Hinge Loss Models
           by Robert C. Moore, John DeNero
           <https://storage.googleapis.com/pub-tools-public-publication-data/pdf/37362.pdf>`_.

    Examples
    --------
    >>> from sklearn import svm
    >>> from sklearn.metrics import hinge_loss
    >>> X = [[0], [1]]
    >>> y = [-1, 1]
    >>> est = svm.LinearSVC(dual="auto", random_state=0)
    >>> est.fit(X, y)
    LinearSVC(dual=\'auto\', random_state=0)
    >>> pred_decision = est.decision_function([[-2], [3], [0.5]])
    >>> pred_decision
    array([-2.18...,  2.36...,  0.09...])
    >>> hinge_loss([-1, 1, 1], pred_decision)
    0.30...

    In the multiclass case:

    >>> import numpy as np
    >>> X = np.array([[0], [1], [2], [3]])
    >>> Y = np.array([0, 1, 2, 3])
    >>> labels = np.array([0, 1, 2, 3])
    >>> est = svm.LinearSVC(dual="auto")
    >>> est.fit(X, Y)
    LinearSVC(dual=\'auto\')
    >>> pred_decision = est.decision_function([[-1], [2], [3]])
    >>> y_true = [0, 2, 3]
    >>> hinge_loss(y_true, pred_decision, labels=labels)
    0.56...
    '''
def brier_score_loss(y_true, y_prob, *, sample_weight: Incomplete | None = None, pos_label: Incomplete | None = None):
    '''Compute the Brier score loss.

    The smaller the Brier score loss, the better, hence the naming with "loss".
    The Brier score measures the mean squared difference between the predicted
    probability and the actual outcome. The Brier score always
    takes on a value between zero and one, since this is the largest
    possible difference between a predicted probability (which must be
    between zero and one) and the actual outcome (which can take on values
    of only 0 and 1). It can be decomposed as the sum of refinement loss and
    calibration loss.

    The Brier score is appropriate for binary and categorical outcomes that
    can be structured as true or false, but is inappropriate for ordinal
    variables which can take on three or more values (this is because the
    Brier score assumes that all possible outcomes are equivalently
    "distant" from one another). Which label is considered to be the positive
    label is controlled via the parameter `pos_label`, which defaults to
    the greater label unless `y_true` is all 0 or all -1, in which case
    `pos_label` defaults to 1.

    Read more in the :ref:`User Guide <brier_score_loss>`.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True targets.

    y_prob : array-like of shape (n_samples,)
        Probabilities of the positive class.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    pos_label : int, float, bool or str, default=None
        Label of the positive class. `pos_label` will be inferred in the
        following manner:

        * if `y_true` in {-1, 1} or {0, 1}, `pos_label` defaults to 1;
        * else if `y_true` contains string, an error will be raised and
          `pos_label` should be explicitly specified;
        * otherwise, `pos_label` defaults to the greater label,
          i.e. `np.unique(y_true)[-1]`.

    Returns
    -------
    score : float
        Brier score loss.

    References
    ----------
    .. [1] `Wikipedia entry for the Brier score
            <https://en.wikipedia.org/wiki/Brier_score>`_.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.metrics import brier_score_loss
    >>> y_true = np.array([0, 1, 1, 0])
    >>> y_true_categorical = np.array(["spam", "ham", "ham", "spam"])
    >>> y_prob = np.array([0.1, 0.9, 0.8, 0.3])
    >>> brier_score_loss(y_true, y_prob)
    0.037...
    >>> brier_score_loss(y_true, 1-y_prob, pos_label=0)
    0.037...
    >>> brier_score_loss(y_true_categorical, y_prob, pos_label="ham")
    0.037...
    >>> brier_score_loss(y_true, np.array(y_prob) > 0.5)
    0.0
    '''
