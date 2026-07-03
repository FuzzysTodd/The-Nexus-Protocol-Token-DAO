from . import shared as shared
from _typeshed import Incomplete
from wandb.sklearn import calculate as calculate, utils as utils

def classifier(model, X_train, X_test, y_train, y_test, y_pred, y_probas, labels, is_binary: bool = False, model_name: str = 'Classifier', feature_names: Incomplete | None = None, log_learning_curve: bool = False) -> None:
    '''Generate all sklearn classifier plots supported by W&B.

    The following plots are generated:
        feature importances, confusion matrix, summary metrics,
        class propotions, calibration curve, roc curve, precision-recall curve.

    Should only be called with a fitted classifer (otherwise an error is thrown).

    Arguments:
        model: (classifier) Takes in a fitted classifier.
        X_train: (arr) Training set features.
        y_train: (arr) Training set labels.
        X_test: (arr) Test set features.
        y_test: (arr) Test set labels.
        y_pred: (arr) Test set predictions by the model passed.
        y_probas: (arr) Test set predicted probabilities by the model passed.
        labels: (list) Named labels for target varible (y). Makes plots easier to
                        read by replacing target values with corresponding index.
                        For example if `labels=[\'dog\', \'cat\', \'owl\']` all 0s are
                        replaced by dog, 1s by cat.
        is_binary: (bool) Is the model passed a binary classifier? Defaults to False
        model_name: (str) Model name. Defaults to \'Classifier\'
        feature_names: (list) Names for features. Makes plots easier to read by
                                replacing feature indexes with corresponding names.
        log_learning_curve: (bool) Whether or not to log the learning curve.
                                    Defaults to False.

    Returns:
        None: To see plots, go to your W&B run page then expand the \'media\' tab
            under \'auto visualizations\'.

    Example:
    ```python
    wandb.sklearn.plot_classifier(
        model,
        X_train,
        X_test,
        y_train,
        y_test,
        y_pred,
        y_probas,
        ["cat", "dog"],
        False,
        "RandomForest",
        ["barks", "drools", "plays_fetch", "breed"],
    )
    ```
    '''
def roc(y_true: Incomplete | None = None, y_probas: Incomplete | None = None, labels: Incomplete | None = None, plot_micro: bool = True, plot_macro: bool = True, classes_to_plot: Incomplete | None = None) -> None:
    """Log the receiver-operating characteristic curve.

    Arguments:
        y_true: (arr) Test set labels.
        y_probas: (arr) Test set predicted probabilities.
        labels: (list) Named labels for target variable (y). Makes plots easier to
                       read by replacing target values with corresponding index.
                       For example if `labels=['dog', 'cat', 'owl']` all 0s are
                       replaced by dog, 1s by cat.

    Returns:
        None: To see plots, go to your W&B run page then expand the 'media' tab
              under 'auto visualizations'.

    Example:
    ```python
    wandb.sklearn.plot_roc(y_true, y_probas, labels)
    ```
    """
def confusion_matrix(y_true: Incomplete | None = None, y_pred: Incomplete | None = None, labels: Incomplete | None = None, true_labels: Incomplete | None = None, pred_labels: Incomplete | None = None, normalize: bool = False) -> None:
    """Log a confusion matrix to W&B.

    Confusion matrices depict the pattern of misclassifications by a model.

    Arguments:
        y_true: (arr) Test set labels.
        y_probas: (arr) Test set predicted probabilities.
        labels: (list) Named labels for target variable (y). Makes plots easier to
                       read by replacing target values with corresponding index.
                       For example if `labels=['dog', 'cat', 'owl']` all 0s are
                       replaced by dog, 1s by cat.

    Returns:
        None: To see plots, go to your W&B run page then expand the 'media' tab
              under 'auto visualizations'.

    Example:
    ```python
    wandb.sklearn.plot_confusion_matrix(y_true, y_probas, labels)
    ```
    """
def precision_recall(y_true: Incomplete | None = None, y_probas: Incomplete | None = None, labels: Incomplete | None = None, plot_micro: bool = True, classes_to_plot: Incomplete | None = None) -> None:
    """Log a precision-recall curve to W&B.

    Precision-recall curves depict the tradeoff between positive predictive value (precision)
    and true positive rate (recall) as the threshold of a classifier is shifted.

    Arguments:
        y_true: (arr) Test set labels.
        y_probas: (arr) Test set predicted probabilities.
        labels: (list) Named labels for target variable (y). Makes plots easier to
                       read by replacing target values with corresponding index.
                       For example if `labels=['dog', 'cat', 'owl']` all 0s are
                       replaced by dog, 1s by cat.

    Returns:
        None: To see plots, go to your W&B run page then expand the 'media' tab
              under 'auto visualizations'.

    Example:
    ```python
    wandb.sklearn.plot_precision_recall(y_true, y_probas, labels)
    ```
    """
def feature_importances(model: Incomplete | None = None, feature_names: Incomplete | None = None, title: str = 'Feature Importance', max_num_features: int = 50) -> None:
    '''Log a plot depicting the relative importance of each feature for a classifier\'s decisions.

    Should only be called with a fitted classifer (otherwise an error is thrown).
    Only works with classifiers that have a feature_importances_ attribute, like trees.

    Arguments:
        model: (clf) Takes in a fitted classifier.
        feature_names: (list) Names for features. Makes plots easier to read by
                              replacing feature indexes with corresponding names.

    Returns:
        None: To see plots, go to your W&B run page then expand the \'media\' tab
              under \'auto visualizations\'.

    Example:
    ```python
    wandb.sklearn.plot_feature_importances(model, ["width", "height", "length"])
    ```
    '''
def class_proportions(y_train: Incomplete | None = None, y_test: Incomplete | None = None, labels: Incomplete | None = None) -> None:
    '''Plot the distribution of target classses in training and test sets.

    Useful for detecting imbalanced classes.

    Arguments:
        y_train: (arr) Training set labels.
        y_test: (arr) Test set labels.
        labels: (list) Named labels for target variable (y). Makes plots easier to
                       read by replacing target values with corresponding index.
                       For example if `labels=[\'dog\', \'cat\', \'owl\']` all 0s are
                       replaced by dog, 1s by cat.

    Returns:
        None: To see plots, go to your W&B run page then expand the \'media\' tab
              under \'auto visualizations\'.

    Example:
    ```python
    wandb.sklearn.plot_class_proportions(y_train, y_test, ["dog", "cat", "owl"])
    ```
    '''
def calibration_curve(clf: Incomplete | None = None, X: Incomplete | None = None, y: Incomplete | None = None, clf_name: str = 'Classifier') -> None:
    '''Log a plot depicting how well-calibrated the predicted probabilities of a classifier are.

    Also suggests how to calibrate an uncalibrated classifier. Compares estimated predicted
    probabilities by a baseline logistic regression model, the model passed as
    an argument, and by both its isotonic calibration and sigmoid calibrations.
    The closer the calibration curves are to a diagonal the better.
    A sine wave like curve represents an overfitted classifier, while a cosine
    wave like curve represents an underfitted classifier.
    By training isotonic and sigmoid calibrations of the model and comparing
    their curves we can figure out whether the model is over or underfitting and
    if so which calibration (sigmoid or isotonic) might help fix this.
    For more details, see https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html.

    Should only be called with a fitted classifer (otherwise an error is thrown).

    Please note this function fits variations of the model on the training set when called.

    Arguments:
        clf: (clf) Takes in a fitted classifier.
        X: (arr) Training set features.
        y: (arr) Training set labels.
        model_name: (str) Model name. Defaults to \'Classifier\'

    Returns:
        None: To see plots, go to your W&B run page then expand the \'media\' tab
              under \'auto visualizations\'.

    Example:
    ```python
    wandb.sklearn.plot_calibration_curve(clf, X, y, "RandomForestClassifier")
    ```
    '''
