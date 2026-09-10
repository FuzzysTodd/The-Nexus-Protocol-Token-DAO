import pandas as pd
from mlflow.exceptions import BAD_REQUEST as BAD_REQUEST, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, MlflowException as MlflowException
from mlflow.recipes.cards import pandas_renderer as pandas_renderer
from mlflow.utils.databricks_utils import get_databricks_runtime as get_databricks_runtime, is_in_databricks_runtime as is_in_databricks_runtime, is_running_in_ipython_environment as is_running_in_ipython_environment
from typing import Dict, Iterable, List, Tuple

def get_merged_eval_metrics(eval_metrics: Dict[str, Dict], ordered_metric_names: List[str] = None):
    """Returns a merged Pandas DataFrame from a map of dataset to evaluation metrics.
    Optionally, the rows in the DataFrame are ordered by input ordered metric names.

    :param eval_metrics: Dict maps from dataset name to a Dict of evaluation metrics, which itself
                         is a map from metric name to metric value.
    :param ordered_metric_names: List containing metric names. The ordering of the output is
                                 determined by this list, if provided.
    :return: Pandas DataFrame containing evaluation metrics. The DataFrame is indexed by metric
             name. Columns are dataset names.
    """
def display_html(html_data: str = None, html_file_path: str = None) -> None: ...
def get_pandas_data_profiles(inputs: Iterable[Tuple[str, pd.DataFrame]]) -> str:
    '''
    Returns a data profiling string over input data frame.

    :param inputs: Either a single "glimpse" DataFrame that contains the statistics, or a
    collection of (title, DataFrame) pairs where each pair names a separate "glimpse"
    and they are all visualized in comparison mode.
    :return: a data profiling string such as Pandas profiling ProfileReport.
    '''
def truncate_pandas_data_profile(title: str, data_frame) -> str:
    """Returns a data profiling string over input data frame.

    :param title: String, the title of the data profile.
    :param data_frame: DataFrame, contains data to be profiled.
    :return: a data profiling string such as Pandas profiling ProfileReport.
    """
def validate_classification_config(task: str, positive_class: str, input_df: pd.DataFrame, target_col: str):
    """

    :param task:
    :param positive_class:
    :param input_df:
    :param target_col:
    """
