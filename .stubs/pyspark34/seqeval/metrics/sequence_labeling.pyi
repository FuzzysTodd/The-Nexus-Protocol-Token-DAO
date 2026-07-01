from _typeshed import Incomplete
from seqeval.metrics.v1 import SCORES as SCORES
from seqeval.reporters import DictReporter as DictReporter, StringReporter as StringReporter
from seqeval.scheme import Token as Token
from typing import List, Type

def precision_recall_fscore_support(y_true: List[List[str]], y_pred: List[List[str]], *, average: str | None = None, warn_for=('precision', 'recall', 'f-score'), beta: float = 1.0, sample_weight: List[int] | None = None, zero_division: str = 'warn', suffix: bool = False) -> SCORES:
    '''Compute precision, recall, F-measure and support for each class.

    Args:
        y_true : 2d array. Ground truth (correct) target values.

        y_pred : 2d array. Estimated targets as returned by a tagger.

        beta : float, 1.0 by default
            The strength of recall versus precision in the F-score.

        average : string, [None (default), \'micro\', \'macro\', \'weighted\']
            If ``None``, the scores for each class are returned. Otherwise, this
            determines the type of averaging performed on the data:
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

        warn_for : tuple or set, for internal use
            This determines which warnings will be made in the case that this
            function is being used to return only one of its metrics.

        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights.

        zero_division : "warn", 0 or 1, default="warn"
            Sets the value to return when there is a zero division:
               - recall: when there are no positive labels
               - precision: when there are no positive predictions
               - f-score: both

            If set to "warn", this acts as 0, but warnings are also raised.

        suffix : bool, False by default.

    Returns:
        precision : float (if average is not None) or array of float, shape = [n_unique_labels]

        recall : float (if average is not None) or array of float, , shape = [n_unique_labels]

        fbeta_score : float (if average is not None) or array of float, shape = [n_unique_labels]

        support : int (if average is not None) or array of int, shape = [n_unique_labels]
            The number of occurrences of each label in ``y_true``.

    Examples:
        >>> from seqeval.metrics.sequence_labeling import precision_recall_fscore_support
        >>> y_true = [[\'O\', \'O\', \'O\', \'B-MISC\', \'I-MISC\', \'I-MISC\', \'O\'], [\'B-PER\', \'I-PER\', \'O\']]
        >>> y_pred = [[\'O\', \'O\', \'B-MISC\', \'I-MISC\', \'I-MISC\', \'I-MISC\', \'O\'], [\'B-PER\', \'I-PER\', \'O\']]
        >>> precision_recall_fscore_support(y_true, y_pred, average=\'macro\')
        (0.5, 0.5, 0.5, 2)
        >>> precision_recall_fscore_support(y_true, y_pred, average=\'micro\')
        (0.5, 0.5, 0.5, 2)
        >>> precision_recall_fscore_support(y_true, y_pred, average=\'weighted\')
        (0.5, 0.5, 0.5, 2)

        It is possible to compute per-label precisions, recalls, F1-scores and
        supports instead of averaging:

        >>> precision_recall_fscore_support(y_true, y_pred, average=None)
        (array([0., 1.]), array([0., 1.]), array([0., 1.]), array([1, 1]))

    Notes:
        When ``true positive + false positive == 0``, precision is undefined;
        When ``true positive + false negative == 0``, recall is undefined.
        In such cases, by default the metric will be set to 0, as will f-score,
        and ``UndefinedMetricWarning`` will be raised. This behavior can be
        modified with ``zero_division``.
    '''
def get_entities(seq, suffix: bool = False):
    """Gets entities from sequence.

    Args:
        seq (list): sequence of labels.

    Returns:
        list: list of (chunk_type, chunk_start, chunk_end).

    Example:
        >>> from seqeval.metrics.sequence_labeling import get_entities
        >>> seq = ['B-PER', 'I-PER', 'O', 'B-LOC']
        >>> get_entities(seq)
        [('PER', 0, 1), ('LOC', 3, 3)]
    """
def end_of_chunk(prev_tag, tag, prev_type, type_):
    """Checks if a chunk ended between the previous and current word.

    Args:
        prev_tag: previous chunk tag.
        tag: current chunk tag.
        prev_type: previous type.
        type_: current type.

    Returns:
        chunk_end: boolean.
    """
def start_of_chunk(prev_tag, tag, prev_type, type_):
    """Checks if a chunk started between the previous and current word.

    Args:
        prev_tag: previous chunk tag.
        tag: current chunk tag.
        prev_type: previous type.
        type_: current type.

    Returns:
        chunk_start: boolean.
    """
def f1_score(y_true: List[List[str]], y_pred: List[List[str]], *, average: str | None = 'micro', suffix: bool = False, mode: str | None = None, sample_weight: List[int] | None = None, zero_division: str = 'warn', scheme: Type[Token] | None = None):
    '''Compute the F1 score.

    The F1 score can be interpreted as a weighted average of the precision and
    recall, where an F1 score reaches its best value at 1 and worst score at 0.
    The relative contribution of precision and recall to the F1 score are
    equal. The formula for the F1 score is::

        F1 = 2 * (precision * recall) / (precision + recall)

    Args:
        y_true : 2d array. Ground truth (correct) target values.

        y_pred : 2d array. Estimated targets as returned by a tagger.

        average : string, [None, \'micro\' (default), \'macro\', \'weighted\']
            If ``None``, the scores for each class are returned. Otherwise, this
            determines the type of averaging performed on the data:
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

        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights.

        zero_division : "warn", 0 or 1, default="warn"
            Sets the value to return when there is a zero division:
               - recall: when there are no positive labels
               - precision: when there are no positive predictions
               - f-score: both

            If set to "warn", this acts as 0, but warnings are also raised.

        mode : str, [None (default), `strict`].
            if ``None``, the score is compatible with conlleval.pl. Otherwise,
            the score is calculated strictly.

        scheme : Token, [IOB2, IOE2, IOBES]

        suffix : bool, False by default.

    Returns:
        score : float or array of float, shape = [n_unique_labels].

    Example:
        >>> from seqeval.metrics import f1_score
        >>> y_true = [[\'O\', \'O\', \'B-MISC\', \'I-MISC\', \'B-MISC\', \'O\', \'O\'], [\'B-PER\', \'I-PER\', \'O\']]
        >>> y_pred = [[\'O\', \'O\', \'B-MISC\', \'I-MISC\', \'B-MISC\', \'I-MISC\', \'O\'], [\'B-PER\', \'I-PER\', \'O\']]
        >>> f1_score(y_true, y_pred, average=\'micro\')
        0.6666666666666666
        >>> f1_score(y_true, y_pred, average=\'macro\')
        0.75
        >>> f1_score(y_true, y_pred, average=\'weighted\')
        0.6666666666666666
        >>> f1_score(y_true, y_pred, average=None)
        array([0.5, 1. ])
    '''
def accuracy_score(y_true, y_pred):
    """Accuracy classification score.

    In multilabel classification, this function computes subset accuracy:
    the set of labels predicted for a sample must *exactly* match the
    corresponding set of labels in y_true.

    Args:
        y_true : 2d array. Ground truth (correct) target values.
        y_pred : 2d array. Estimated targets as returned by a tagger.

    Returns:
        score : float.

    Example:
        >>> from seqeval.metrics import accuracy_score
        >>> y_true = [['O', 'O', 'O', 'B-MISC', 'I-MISC', 'I-MISC', 'O'], ['B-PER', 'I-PER', 'O']]
        >>> y_pred = [['O', 'O', 'B-MISC', 'I-MISC', 'I-MISC', 'I-MISC', 'O'], ['B-PER', 'I-PER', 'O']]
        >>> accuracy_score(y_true, y_pred)
        0.80
    """
def precision_score(y_true: List[List[str]], y_pred: List[List[str]], *, average: str | None = 'micro', suffix: bool = False, mode: str | None = None, sample_weight: List[int] | None = None, zero_division: str = 'warn', scheme: Type[Token] | None = None):
    '''Compute the precision.

    The precision is the ratio ``tp / (tp + fp)`` where ``tp`` is the number of
    true positives and ``fp`` the number of false positives. The precision is
    intuitively the ability of the classifier not to label as positive a sample.

    The best value is 1 and the worst value is 0.

    Args:
        y_true : 2d array. Ground truth (correct) target values.

        y_pred : 2d array. Estimated targets as returned by a tagger.

        average : string, [None, \'micro\' (default), \'macro\', \'weighted\']
            If ``None``, the scores for each class are returned. Otherwise, this
            determines the type of averaging performed on the data:
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

        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights.

        zero_division : "warn", 0 or 1, default="warn"
            Sets the value to return when there is a zero division:
               - recall: when there are no positive labels
               - precision: when there are no positive predictions
               - f-score: both

            If set to "warn", this acts as 0, but warnings are also raised.

        mode : str, [None (default), `strict`].
            if ``None``, the score is compatible with conlleval.pl. Otherwise,
            the score is calculated strictly.

        scheme : Token, [IOB2, IOE2, IOBES]

        suffix : bool, False by default.

    Returns:
        score : float or array of float, shape = [n_unique_labels].

    Example:
        >>> from seqeval.metrics import precision_score
        >>> y_true = [[\'O\', \'O\', \'B-MISC\', \'I-MISC\', \'B-MISC\', \'O\', \'O\'], [\'B-PER\', \'I-PER\', \'O\']]
        >>> y_pred = [[\'O\', \'O\', \'B-MISC\', \'I-MISC\', \'B-MISC\', \'I-MISC\', \'O\'], [\'B-PER\', \'I-PER\', \'O\']]
        >>> precision_score(y_true, y_pred, average=None)
        array([0.5, 1. ])
        >>> precision_score(y_true, y_pred, average=\'micro\')
        0.6666666666666666
        >>> precision_score(y_true, y_pred, average=\'macro\')
        0.75
        >>> precision_score(y_true, y_pred, average=\'weighted\')
        0.6666666666666666
    '''
def recall_score(y_true: List[List[str]], y_pred: List[List[str]], *, average: str | None = 'micro', suffix: bool = False, mode: str | None = None, sample_weight: List[int] | None = None, zero_division: str = 'warn', scheme: Type[Token] | None = None):
    '''Compute the recall.

    The recall is the ratio ``tp / (tp + fn)`` where ``tp`` is the number of
    true positives and ``fn`` the number of false negatives. The recall is
    intuitively the ability of the classifier to find all the positive samples.

    The best value is 1 and the worst value is 0.

    Args:
        y_true : 2d array. Ground truth (correct) target values.

        y_pred : 2d array. Estimated targets as returned by a tagger.

        average : string, [None, \'micro\' (default), \'macro\', \'weighted\']
            If ``None``, the scores for each class are returned. Otherwise, this
            determines the type of averaging performed on the data:
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

        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights.

        zero_division : "warn", 0 or 1, default="warn"
            Sets the value to return when there is a zero division:
               - recall: when there are no positive labels
               - precision: when there are no positive predictions
               - f-score: both

            If set to "warn", this acts as 0, but warnings are also raised.

        mode : str, [None (default), `strict`].
            if ``None``, the score is compatible with conlleval.pl. Otherwise,
            the score is calculated strictly.

        scheme : Token, [IOB2, IOE2, IOBES]

        suffix : bool, False by default.

    Returns:
        score : float.

    Example:
        >>> from seqeval.metrics import recall_score
        >>> y_true = [[\'O\', \'O\', \'B-MISC\', \'I-MISC\', \'B-MISC\', \'O\', \'O\'], [\'B-PER\', \'I-PER\', \'O\']]
        >>> y_pred = [[\'O\', \'O\', \'B-MISC\', \'I-MISC\', \'B-MISC\', \'I-MISC\', \'O\'], [\'B-PER\', \'I-PER\', \'O\']]
        >>> recall_score(y_true, y_pred, average=None)
        array([0.5, 1. ])
        >>> recall_score(y_true, y_pred, average=\'micro\')
        0.6666666666666666
        >>> recall_score(y_true, y_pred, average=\'macro\')
        0.75
        >>> recall_score(y_true, y_pred, average=\'weighted\')
        0.6666666666666666
    '''
def performance_measure(y_true, y_pred):
    """
    Compute the performance metrics: TP, FP, FN, TN

    Args:
        y_true : 2d array. Ground truth (correct) target values.
        y_pred : 2d array. Estimated targets as returned by a tagger.

    Returns:
        performance_dict : dict

    Example:
        >>> from seqeval.metrics import performance_measure
        >>> y_true = [['O', 'O', 'O', 'B-MISC', 'I-MISC', 'O', 'B-ORG'], ['B-PER', 'I-PER', 'O', 'B-PER']]
        >>> y_pred = [['O', 'O', 'B-MISC', 'I-MISC', 'I-MISC', 'O', 'O'], ['B-PER', 'I-PER', 'O', 'B-MISC']]
        >>> performance_measure(y_true, y_pred)
        {'TP': 3, 'FP': 3, 'FN': 1, 'TN': 4}
    """
def classification_report(y_true, y_pred, digits: int = 2, suffix: bool = False, output_dict: bool = False, mode: Incomplete | None = None, sample_weight: Incomplete | None = None, zero_division: str = 'warn', scheme: Incomplete | None = None):
    '''Build a text report showing the main classification metrics.

    Args:
        y_true : 2d array. Ground truth (correct) target values.

        y_pred : 2d array. Estimated targets as returned by a classifier.

        digits : int. Number of digits for formatting output floating point values.

        output_dict : bool(default=False). If True, return output as dict else str.

        mode : str, [None (default), `strict`].
            if ``None``, the score is compatible with conlleval.pl. Otherwise,
            the score is calculated strictly.

        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights.

        zero_division : "warn", 0 or 1, default="warn"
            Sets the value to return when there is a zero division:
               - recall: when there are no positive labels
               - precision: when there are no positive predictions
               - f-score: both

            If set to "warn", this acts as 0, but warnings are also raised.

        scheme : Token, [IOB2, IOE2, IOBES]

        suffix : bool, False by default.

    Returns:
        report : string/dict. Summary of the precision, recall, F1 score for each class.

    Examples:
        >>> from seqeval.metrics import classification_report
        >>> y_true = [[\'O\', \'O\', \'O\', \'B-MISC\', \'I-MISC\', \'I-MISC\', \'O\'], [\'B-PER\', \'I-PER\', \'O\']]
        >>> y_pred = [[\'O\', \'O\', \'B-MISC\', \'I-MISC\', \'I-MISC\', \'I-MISC\', \'O\'], [\'B-PER\', \'I-PER\', \'O\']]
        >>> print(classification_report(y_true, y_pred))
                     precision    recall  f1-score   support
        <BLANKLINE>
               MISC       0.00      0.00      0.00         1
                PER       1.00      1.00      1.00         1
        <BLANKLINE>
          micro avg       0.50      0.50      0.50         2
          macro avg       0.50      0.50      0.50         2
       weighted avg       0.50      0.50      0.50         2
        <BLANKLINE>
    '''
