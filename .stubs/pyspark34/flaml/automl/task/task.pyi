import abc
import flaml
import numpy as np
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from flaml.automl.data import DataFrame as DataFrame, Series as Series, psDataFrame as psDataFrame, psSeries as psSeries
from typing import List, Tuple

SEQCLASSIFICATION: str
MULTICHOICECLASSIFICATION: str
TOKENCLASSIFICATION: str
SEQREGRESSION: str
TS_FORECASTREGRESSION: Incomplete
REGRESSION: Incomplete
TS_FORECASTCLASSIFICATION: str
TS_FORECASTPANEL: str
TS_FORECAST: Incomplete
CLASSIFICATION: Incomplete
RANK: Incomplete
SUMMARIZATION: str
NLG_TASKS: Incomplete
NLU_TASKS: Incomplete
NLP_TASKS: Incomplete

def get_classification_objective(num_labels: int) -> str: ...

class Task(ABC, metaclass=abc.ABCMeta):
    """
    Abstract base class for a machine learning task.

    Class definitions should implement abstract methods and provide a non-empty dictionary of estimator classes.
    A Task can be suitable to be used for multiple machine-learning tasks (e.g. classification or regression) or be
    implemented specifically for a single one depending on the generality of data validation and model evaluation methods
    implemented. The implementation of a Task may optionally use the training data and labels to determine data and task
    specific details, such as in determining if a problem is single-label or multi-label.

    FLAML evaluates at runtime how to behave exactly, relying on the task instance to provide implementations of
    operations which vary between tasks.
    """
    name: Incomplete
    def __init__(self, task_name: str, X_train: np.ndarray | DataFrame | psDataFrame | None = None, y_train: np.ndarray | DataFrame | Series | psSeries | None = None) -> None:
        """Constructor.

        Args:
            task_name: String name for this type of task. Used when the Task can be generic and implement a number of
                types of sub-task.
            X_train: Optional. Some Task types may use the data shape or features to determine details of their usage,
                such as in binary vs multilabel classification.
            y_train: Optional. Some Task types may use the data shape or features to determine details of their usage,
                such as in binary vs multilabel classification.
        """
    @abstractmethod
    def evaluate_model_CV(self, config: dict, estimator: flaml.automl.ml.BaseEstimator, X_train_all: np.ndarray | DataFrame | psDataFrame, y_train_all: np.ndarray | DataFrame | Series | psSeries, budget: int, kf, eval_metric: str, best_val_loss: float, log_training_metric: bool = False, fit_kwargs: dict | None = {}) -> Tuple[float, float, float, float]:
        """Evaluate the model using cross-validation.

        Args:
            config: configuration used in the evaluation of the metric.
            estimator: Estimator class of the model.
            X_train_all: Complete training feature data.
            y_train_all: Complete training target data.
            budget: Training time budget.
            kf: Cross-validation index generator.
            eval_metric: Metric name to be used for evaluation.
            best_val_loss: Best current validation-set loss.
            log_training_metric: Bool defaults False. Enables logging of the training metric.
            fit_kwargs: Additional kwargs passed to the estimator's fit method.

        Returns:
            validation loss, metric value, train time, prediction time
        """
    @abstractmethod
    def validate_data(self, automl: flaml.automl.automl.AutoML, state: flaml.automl.state.AutoMLState, X_train_all: np.ndarray | DataFrame | psDataFrame | None, y_train_all: np.ndarray | DataFrame | Series | psSeries | None, dataframe: DataFrame | None, label: str, X_val: np.ndarray | DataFrame | psDataFrame | None = None, y_val: np.ndarray | DataFrame | Series | psSeries | None = None, groups_val: List[str] | None = None, groups: List[str] | None = None):
        """Validate that the data is suitable for this task type.

        Args:
            automl: The AutoML instance from which this task has been constructed.
            state: The AutoMLState instance for this run.
            X_train_all: The complete data set or None if dataframe is supplied.
            y_train_all: The complete target set or None if dataframe is supplied.
            dataframe: A dataframe constaining the complete data set with targets.
            label: The name of the target column in dataframe.
            X_val: Optional. A data set for validation.
            y_val: Optional. A target vector corresponding to X_val for validation.
            groups_val: Group labels (with matching length to y_val) or group counts (with sum equal to length of y_val)
                for validation data. Need to be consistent with groups.
            groups: Group labels (with matching length to y_train) or groups counts (with sum equal to length of y_train)
                for training data.

        Raises:
            AssertionError: The data provided is invalid for this task type and configuration.
        """
    @abstractmethod
    def prepare_data(self, state: flaml.automl.state.AutoMLState, X_train_all: np.ndarray | DataFrame | psDataFrame, y_train_all: np.ndarray | DataFrame | Series | psSeries | None, auto_augment: bool, eval_method: str, split_type: str, split_ratio: float, n_splits: int, data_is_df: bool, sample_weight_full: List[float] | None = None):
        '''Prepare the data for fitting or inference.

        Args:
            automl: The AutoML instance from which this task has been constructed.
            state: The AutoMLState instance for this run.
            X_train_all: The complete data set or None if dataframe is supplied. Must
                contain the target if y_train_all is None
            y_train_all: The complete target set or None if supplied in X_train_all.
            auto_augment: If true, task-specific data augmentations will be applied.
            eval_method: A string of resampling strategy, one of [\'auto\', \'cv\', \'holdout\'].
            split_type: str or splitter object, default="auto" | the data split type.
                * A valid splitter object is an instance of a derived class of scikit-learn
                [KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold)
                and have ``split`` and ``get_n_splits`` methods with the same signatures.
                Set eval_method to "cv" to use the splitter object.
                * Valid str options depend on different tasks.
                For classification tasks, valid choices are
                    ["auto", \'stratified\', \'uniform\', \'time\', \'group\']. "auto" -> stratified.
                For regression tasks, valid choices are ["auto", \'uniform\', \'time\'].
                    "auto" -> uniform.
                For time series forecast tasks, must be "auto" or \'time\'.
                For ranking task, must be "auto" or \'group\'.
            split_ratio: A float of the valiation data percentage for holdout.
            n_splits: An integer of the number of folds for cross - validation.
            data_is_df: True if the data was provided as a DataFrame else False.
            sample_weight_full: A 1d arraylike of the sample weight.

        Raises:
            AssertionError: The configuration provided is invalid for this task type and data.
        '''
    @abstractmethod
    def decide_split_type(self, split_type: str, y_train_all: np.ndarray | DataFrame | Series | psSeries | None, fit_kwargs: dict, groups: List[str] | None = None) -> str:
        """Choose an appropriate data split type for this data and task.

        If split_type is 'auto' then this is determined based on the task type and data.
        If a specific split_type is requested then the choice is validated to be appropriate.

        Args:
            split_type: Either 'auto' or a task appropriate split type.
            y_train_all: The complete set of targets.
            fit_kwargs: Additional kwargs passed to the estimator's fit method.
            groups: Optional. Group labels (with matching length to y_train) or groups counts (with sum equal to length
                of y_train) for training data.

        Returns:
            The determined appropriate split type.

        Raises:
            AssertionError: The requested split_type is invalid for this task, configuration and data.
        """
    @abstractmethod
    def preprocess(self, X: np.ndarray | DataFrame | psDataFrame, transformer: flaml.automl.data.DataTransformer | None = None) -> np.ndarray | DataFrame:
        """Preprocess the data ready for fitting or inference with this task type.

        Args:
            X: The data set to process.
            transformer: A DataTransformer instance to be used in processing.

        Returns:
            The preprocessed data set having the same type as the input.
        """
    @abstractmethod
    def default_estimator_list(self, estimator_list: List[str] | str = 'auto', is_spark_dataframe: bool = False) -> List[str]:
        """Return the list of default estimators registered for this task type.

        If 'auto' is provided then the default list is returned, else the provided list will be validated given this task
        type.

        Args:
            estimator_list: Either 'auto' or a list of estimator names to be validated.
            is_spark_dataframe: True if the data is a spark dataframe.

        Returns:
            A list of valid estimator names for this task type.
        """
    @abstractmethod
    def default_metric(self, metric: str) -> str:
        """Return the default metric for this task type.

        If 'auto' is provided then the default metric for this task will be returned. Otherwise, the provided metric name
        is validated for this task type.

        Args:
            metric: The name of a metric to be used in evaluation of models during fitting or validation.

        Returns:
            The default metric, or the provided metric if it is valid for this task type.
        """
    def is_ts_forecast(self) -> bool: ...
    def is_ts_forecastpanel(self) -> bool: ...
    def is_ts_forecastregression(self) -> bool: ...
    def is_nlp(self) -> bool: ...
    def is_nlg(self) -> bool: ...
    def is_classification(self) -> bool: ...
    def is_rank(self) -> bool: ...
    def is_binary(self) -> bool: ...
    def is_seq_regression(self) -> bool: ...
    def is_seq_classification(self) -> bool: ...
    def is_token_classification(self) -> bool: ...
    def is_summarization(self) -> bool: ...
    def is_multiclass(self) -> bool: ...
    def is_regression(self) -> bool: ...
    def __eq__(self, other: str) -> bool:
        """For backward compatibility with all the string comparisons to task"""
    def estimator_class_from_str(self, estimator_name: str) -> flaml.automl.ml.BaseEstimator:
        """Determine the estimator class corresponding to the provided name.

        Args:
            estimator_name: Name of the desired estimator.

        Returns:
            The estimator class corresponding to the provided name.

        Raises:
            ValueError: The provided estimator_name has not been registered for this task type.
        """
