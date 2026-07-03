import numpy as np
from _typeshed import Incomplete
from flaml.automl.data import group_counts as group_counts
from flaml.automl.model import BaseEstimator as BaseEstimator, TransformersEstimator as TransformersEstimator
from flaml.automl.spark import DataFrame as DataFrame, Series as Series, psDataFrame as psDataFrame, psSeries as psSeries
from flaml.automl.spark.metrics import spark_metric_loss_score as spark_metric_loss_score
from flaml.automl.task.task import Task as Task
from flaml.automl.time_series import TimeSeriesDataset as TimeSeriesDataset
from flaml.internal._autofe import Featurization as Featurization
from typing import Callable, Tuple, TypeVar

logger: Incomplete
EstimatorSubclass = TypeVar('EstimatorSubclass', bound=BaseEstimator)
sklearn_metric_name_set: Incomplete
huggingface_metric_to_mode: Incomplete
huggingface_submetric_to_metric: Incomplete

def metric_loss_score(metric_name: str, y_processed_predict, y_processed_true, labels: Incomplete | None = None, sample_weight: Incomplete | None = None, groups: Incomplete | None = None): ...
def is_in_sklearn_metric_name_set(metric_name: str): ...
def is_min_metric(metric_name: str): ...
def sklearn_metric_loss_score(metric_name: str, y_predict, y_true, labels: Incomplete | None = None, sample_weight: Incomplete | None = None, groups: Incomplete | None = None):
    """Loss using the specified metric.

    Args:
        metric_name: A string of the metric name, one of
            'r2', 'rmse', 'mae', 'mse', 'accuracy', 'roc_auc', 'roc_auc_ovr',
            'roc_auc_ovo', 'roc_auc_weighted', 'roc_auc_ovo_weighted', 'roc_auc_ovr_weighted',
            'log_loss', 'mape', 'f1', 'ap', 'ndcg', 'micro_f1', 'macro_f1'.
        y_predict: A 1d or 2d numpy array of the predictions which can be
            used to calculate the metric. E.g., 2d for log_loss and 1d
            for others.
        y_true: A 1d numpy array of the true labels.
        labels: A list or an array of the unique labels.
        sample_weight: A 1d numpy array of the sample weight.
        groups: A 1d numpy array of the group labels.

    Returns:
        score: A float number of the loss, the lower the better.
    """
def get_y_pred(estimator, X, eval_metric, task: Task): ...
def to_numpy(x): ...
def compute_estimator(X_train, y_train, X_val, y_val, weight_val, groups_val, budget, kf, config_dic: dict, task: str | Task, estimator_name: str, eval_method: str, eval_metric: str | Callable, best_val_loss=..., n_jobs: int | None = 1, estimator_class: EstimatorSubclass | None = None, cv_score_agg_func: callable | None = None, log_training_metric: bool | None = False, fit_kwargs: dict | None = None, free_mem_ratio: int = 0): ...
def train_estimator(config_dic: dict, X_train, y_train, task: str, estimator_name: str, n_jobs: int | None = 1, estimator_class: EstimatorSubclass | None = None, budget: Incomplete | None = None, fit_kwargs: dict | None = None, eval_metric: Incomplete | None = None, free_mem_ratio: int = 0) -> Tuple[EstimatorSubclass, float]: ...
def norm_confusion_matrix(y_true: np.array | Series, y_pred: np.array | Series):
    """normalized confusion matrix.

    Args:
        estimator: A multi-class classification estimator.
        y_true: A numpy array or a pandas series of true labels.
        y_pred: A numpy array or a pandas series of predicted labels.

    Returns:
        A normalized confusion matrix.
    """
def multi_class_curves(y_true: np.array | Series, y_pred_proba: np.array | Series, curve_func: Callable):
    """Binarize the data for multi-class tasks and produce ROC or precision-recall curves.

    Args:
        y_true: A numpy array or a pandas series of true labels.
        y_pred_proba: A numpy array or a pandas dataframe of predicted probabilites.
        curve_func: A function to produce a curve (e.g., roc_curve or precision_recall_curve).

    Returns:
        A tuple of two dictionaries with the same set of keys (class indices).
        The first dictionary curve_x stores the x coordinates of each curve, e.g.,
            curve_x[0] is an 1D array of the x coordinates of class 0.
        The second dictionary curve_y stores the y coordinates of each curve, e.g.,
            curve_y[0] is an 1D array of the y coordinates of class 0.
    """
def get_val_loss(config, estimator, X_train, y_train, X_val, y_val, weight_val, groups_val, eval_metric, task, labels: Incomplete | None = None, budget: Incomplete | None = None, log_training_metric: bool = False, fit_kwargs={}, free_mem_ratio: int = 0): ...
def default_cv_score_agg_func(val_loss_folds, log_metrics_folds): ...
