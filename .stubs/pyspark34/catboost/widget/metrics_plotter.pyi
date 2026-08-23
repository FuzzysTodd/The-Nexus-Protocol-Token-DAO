import typing as tp
from .ipythonwidget import MetricWidget as MetricWidget
from _typeshed import Incomplete
from typing import Any, List

logger: Incomplete

class MetricsWidget(MetricWidget):
    def __init__(self) -> None: ...
    data: Incomplete
    def update_data(self, data: tp.Dict) -> None: ...

class MetricsPlotter:
    """
    Context manager that enables widget with learning curves in 
    JupyterLab / Jupyter Notebook
    """
    passed_iterations: int
    total_iterations: Incomplete
    def __init__(self, train_metrics: List[str | tp.Dict[str, str]], test_metrics: List[str | tp.Dict[str, str]] | None = None, total_iterations: int | None = None) -> None:
        '''
        Constructor that defines metrics to be plotted and total iterations count.

        Parameters
        ----------
        train_metrics : list of str or list of dict
            List of train metrics to be tracked. 
            Each item in list can be either string with metric name or dict 
            with the following format:
            {
                "name": "{metric_name}",
                "best_value": "Max|Min|Undefined",
            }
        
        test_metrics : list of str or list of dict, optional (default=None)
            List of test metrics to be tracked. 
            Has the same format as train_metrics. Equals to train_metrics, if not defined
        
        total_iterations: int, optional (default=None)
            Total number of iterations, allows for remaining time estimation.
        '''
    def __enter__(self) -> MetricsPlotter: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> Any: ...
    @staticmethod
    def construct_metrics_meta(metrics: List[str | tp.Dict[str, str]]) -> List[tp.Dict[str, str]]: ...
    @staticmethod
    def construct_metrics_array(metrics_positions: tp.Dict[str, int], metrics: tp.Dict[str, float]) -> List[float]: ...
    def estimate_remaining_time(self, time_from_start: float) -> float | None: ...
    def log(self, epoch: int, train: bool, metrics: tp.Dict[str, float]) -> None:
        """
        Save metrics at specific training epoch.

        Parameters
        ----------
        epoch : int
            Current epoch
        
        train : bool
            Flag that indicates whether metrics are calculated on train or test data
        
        metrics: dict
            Values for each of metrics defined in `__init__` method of this class
        """
