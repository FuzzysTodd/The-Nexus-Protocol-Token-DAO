import optuna
import xgboost as xgb
from _typeshed import Incomplete
from typing import Any

use_callback_cls: bool
xgboost_version: Incomplete
xgboost_major_version: Incomplete
xgboost_minor_version: Incomplete

class XGBoostPruningCallback(xgb.callback.TrainingCallback):
    __doc__: Incomplete
    def __init__(self, trial: optuna.trial.Trial, observation_key: str) -> None: ...
    def before_training(self, model: Any) -> Any: ...
    def after_iteration(self, model: Any, epoch: int, evals_log: dict) -> bool: ...

class XGBoostPruningCallback:
    __doc__: Incomplete
    def __init__(self, trial: optuna.trial.Trial, observation_key: str) -> None: ...
    def __call__(self, env: xgb.core.CallbackEnv) -> None: ...

class XGBoostPruningCallback:
    __doc__: Incomplete
    def __init__(self, trial: optuna.trial.Trial, observation_key: str) -> None: ...
