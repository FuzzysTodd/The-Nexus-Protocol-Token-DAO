from _typeshed import Incomplete
from flaml import tune as tune
from flaml.automl.model import SKLearnEstimator as SKLearnEstimator
from flaml.automl.task import Task as Task

class HistGradientBoostingEstimator(SKLearnEstimator):
    """The class for tuning Histogram Gradient Boosting."""
    ITER_HP: str
    HAS_CALLBACK: bool
    DEFAULT_ITER: int
    @classmethod
    def search_space(cls, data_size: int, task, **params) -> dict: ...
    def config2params(self, config: dict) -> dict: ...
    estimator_class: Incomplete
    def __init__(self, task: Task, **config) -> None: ...
