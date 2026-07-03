import xgboost as xgb
from _typeshed import Incomplete
from typing import Callable, List, NamedTuple
from xgboost import Booster as Booster

MINIMIZE_METRICS: Incomplete
MAXIMIZE_METRICS: Incomplete

class CallbackEnv(NamedTuple):
    evaluation_result_list: List

def wandb_callback() -> Callable:
    """Old style callback that will be deprecated in favor of WandbCallback. Please try the new logger for more features."""

class WandbCallback(xgb.callback.TrainingCallback):
    '''`WandbCallback` automatically integrates XGBoost with wandb.

    Arguments:
        log_model: (boolean) if True save and upload the model to Weights & Biases Artifacts
        log_feature_importance: (boolean) if True log a feature importance bar plot
        importance_type: (str) one of {weight, gain, cover, total_gain, total_cover} for tree model. weight for linear model.
        define_metric: (boolean) if True (default) capture model performance at the best step, instead of the last step, of training in your `wandb.summary`.

    Passing `WandbCallback` to XGBoost will:

    - log the booster model configuration to Weights & Biases
    - log evaluation metrics collected by XGBoost, such as rmse, accuracy etc. to Weights & Biases
    - log training metric collected by XGBoost (if you provide training data to eval_set)
    - log the best score and the best iteration
    - save and upload your trained model to Weights & Biases Artifacts (when `log_model = True`)
    - log feature importance plot when `log_feature_importance=True` (default).
    - Capture the best eval metric in `wandb.summary` when `define_metric=True` (default).

    Example:
        ```python
        bst_params = dict(
            objective="reg:squarederror",
            colsample_bytree=0.3,
            learning_rate=0.1,
            max_depth=5,
            alpha=10,
            n_estimators=10,
            tree_method="hist",
            callbacks=[WandbCallback()],
        )

        xg_reg = xgb.XGBRegressor(**bst_params)
        xg_reg.fit(
            X_train,
            y_train,
            eval_set=[(X_test, y_test)],
        )
        ```
    '''
    log_model: Incomplete
    log_feature_importance: Incomplete
    importance_type: Incomplete
    define_metric: Incomplete
    def __init__(self, log_model: bool = False, log_feature_importance: bool = True, importance_type: str = 'gain', define_metric: bool = True) -> None: ...
    def before_training(self, model: Booster) -> Booster:
        """Run before training is finished."""
    def after_training(self, model: Booster) -> Booster:
        """Run after training is finished."""
    def after_iteration(self, model: Booster, epoch: int, evals_log: dict) -> bool:
        """Run after each iteration. Return True when training should stop."""
