import numpy as np
from flaml.automl.data import DataFrame as DataFrame, Series as Series
from flaml.automl.task.task import TS_FORECAST as TS_FORECAST, Task as Task

def task_factory(task_name: str, X_train: np.ndarray | DataFrame | None = None, y_train: np.ndarray | DataFrame | Series | None = None) -> Task: ...
