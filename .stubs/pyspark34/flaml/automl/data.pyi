import numpy as np
from _typeshed import Incomplete
from flaml.automl.spark import DataFrame as DataFrame, Series as Series, pd as pd, ps as ps, psDataFrame as psDataFrame, psSeries as psSeries
from flaml.automl.task import Task as Task
from flaml.automl.training_log import training_log_reader as training_log_reader

TS_TIMESTAMP_COL: str
TS_VALUE_COL: str

def load_openml_dataset(dataset_id, data_dir: Incomplete | None = None, random_state: int = 0, dataset_format: str = 'dataframe'):
    """Load dataset from open ML.

    If the file is not cached locally, download it from open ML.

    Args:
        dataset_id: An integer of the dataset id in openml.
        data_dir: A string of the path to store and load the data.
        random_state: An integer of the random seed for splitting data.
        dataset_format: A string specifying the format of returned dataset. Default is 'dataframe'.
            Can choose from ['dataframe', 'array'].
            If 'dataframe', the returned dataset will be a Pandas DataFrame.
            If 'array', the returned dataset will be a NumPy array or a SciPy sparse matrix.

    Returns:
        X_train: Training data.
        X_test:  Test data.
        y_train: A series or array of labels for training data.
        y_test:  A series or array of labels for test data.
    """
def load_openml_task(task_id, data_dir):
    """Load task from open ML.

    Use the first fold of the task.
    If the file is not cached locally, download it from open ML.

    Args:
        task_id: An integer of the task id in openml.
        data_dir: A string of the path to store and load the data.

    Returns:
        X_train: A dataframe of training data.
        X_test:  A dataframe of test data.
        y_train: A series of labels for training data.
        y_test:  A series of labels for test data.
    """
def get_output_from_log(filename, time_budget):
    """Get output from log file.

    Args:
        filename: A string of the log file name.
        time_budget: A float of the time budget in seconds.

    Returns:
        search_time_list: A list of the finished time of each logged iter.
        best_error_list: A list of the best validation error after each logged iter.
        error_list: A list of the validation error of each logged iter.
        config_list: A list of the estimator, sample size and config of each logged iter.
        logged_metric_list: A list of the logged metric of each logged iter.
    """
def concat(X1, X2):
    """concatenate two matrices vertically."""
def add_time_idx_col(X): ...

class DataTransformer:
    """Transform input training data."""
    transformer: Incomplete
    label_transformer: Incomplete
    def fit_transform(self, X: DataFrame | np.ndarray, y, task: str | Task):
        """Fit transformer and process the input training data according to the task type.

        Args:
            X: A numpy array or a pandas dataframe of training data.
            y: A numpy array or a pandas series of labels.
            task: An instance of type Task, or a str such as 'classification', 'regression'.

        Returns:
            X: Processed numpy array or pandas dataframe of training data.
            y: Processed numpy array or pandas series of labels.
        """
    def transform(self, X: DataFrame | np.array):
        """Process data using fit transformer.

        Args:
            X: A numpy array or a pandas dataframe of training data.

        Returns:
            X: Processed numpy array or pandas dataframe of training data.
        """

def group_counts(groups): ...
