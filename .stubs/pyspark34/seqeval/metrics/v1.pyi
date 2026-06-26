from seqeval.reporters import DictReporter as DictReporter, StringReporter as StringReporter
from seqeval.scheme import Entities as Entities, Token as Token, auto_detect as auto_detect
from typing import List, Tuple, Type

PER_CLASS_SCORES = Tuple[List[float], List[float], List[float], List[int]]
AVERAGE_SCORES = Tuple[float, float, float, int]
SCORES = PER_CLASS_SCORES | AVERAGE_SCORES

def unique_labels(y_true: List[List[str]], y_pred: List[List[str]], scheme: Type[Token], suffix: bool = False) -> List[str]: ...
def check_consistent_length(y_true: List[List[str]], y_pred: List[List[str]]):
    """Check that all arrays have consistent first and second dimensions.

    Checks whether all objects in arrays have the same shape or length.

    Args:
        y_true : 2d array.
        y_pred : 2d array.
    """
def precision_recall_fscore_support(y_true: List[List[str]], y_pred: List[List[str]], *, average: str | None = None, warn_for=('precision', 'recall', 'f-score'), beta: float = 1.0, sample_weight: List[int] | None = None, zero_division: str = 'warn', scheme: Type[Token] | None = None, suffix: bool = False, **kwargs) -> SCORES:
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

        scheme : Token, [IOB2, IOE2, IOBES]

        suffix : bool, False by default.

    Returns:
        precision : float (if average is not None) or array of float, shape = [n_unique_labels]

        recall : float (if average is not None) or array of float, , shape = [n_unique_labels]

        fbeta_score : float (if average is not None) or array of float, shape = [n_unique_labels]

        support : int (if average is not None) or array of int, shape = [n_unique_labels]
            The number of occurrences of each label in ``y_true``.

    Examples:
        >>> from seqeval.metrics.v1 import precision_recall_fscore_support
        >>> from seqeval.scheme import IOB2
        >>> y_true = [[\'O\', \'O\', \'O\', \'B-MISC\', \'I-MISC\', \'I-MISC\', \'O\'], [\'B-PER\', \'I-PER\', \'O\']]
        >>> y_pred = [[\'O\', \'O\', \'B-MISC\', \'I-MISC\', \'I-MISC\', \'I-MISC\', \'O\'], [\'B-PER\', \'I-PER\', \'O\']]
        >>> precision_recall_fscore_support(y_true, y_pred, average=\'macro\', scheme=IOB2)
        (0.5, 0.5, 0.5, 2)
        >>> precision_recall_fscore_support(y_true, y_pred, average=\'micro\', scheme=IOB2)
        (0.5, 0.5, 0.5, 2)
        >>> precision_recall_fscore_support(y_true, y_pred, average=\'weighted\', scheme=IOB2)
        (0.5, 0.5, 0.5, 2)

        It is possible to compute per-label precisions, recalls, F1-scores and
        supports instead of averaging:

        >>> precision_recall_fscore_support(y_true, y_pred, average=None, scheme=IOB2)
        (array([0., 1.]), array([0., 1.]), array([0., 1.]), array([1, 1]))

    Notes:
        When ``true positive + false positive == 0``, precision is undefined;
        When ``true positive + false negative == 0``, recall is undefined.
        In such cases, by default the metric will be set to 0, as will f-score,
        and ``UndefinedMetricWarning`` will be raised. This behavior can be
        modified with ``zero_division``.
    '''
def classification_report(y_true: List[List[str]], y_pred: List[List[str]], *, sample_weight: List[int] | None = None, digits: int = 2, output_dict: bool = False, zero_division: str = 'warn', suffix: bool = False, scheme: Type[Token] = None) -> str | dict:
    '''Build a text report showing the main tagging metrics.

    Args:
        y_true : 2d array. Ground truth (correct) target values.

        y_pred : 2d array. Estimated targets as returned by a classifier.

        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights.

        digits : int. Number of digits for formatting output floating point values.

        output_dict : bool(default=False). If True, return output as dict else str.

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
        >>> from seqeval.metrics.v1 import classification_report
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
