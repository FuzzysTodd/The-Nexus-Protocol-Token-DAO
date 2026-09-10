from .metrics_plotter import MetricsPlotter as MetricsPlotter
from _typeshed import Incomplete
from xgboost.callback import TrainingCallback as XGBTrainingCallback

class XGBTrainingCallback: ...

class XGBPlottingCallback(XGBTrainingCallback):
    """XGBoost callback with metrics plotting widget from CatBoost
    """
    plotter: Incomplete
    total_iterations: Incomplete
    def __init__(self, total_iterations: int) -> None: ...
    def after_iteration(self, model, epoch, evals_log): ...

def lgbm_plotting_callback():
    """LightGBM callback with metrics plotting widget from CatBoost
    """
