from _typeshed import Incomplete
from lightgbm import Booster
from typing import Any, Callable, Dict, List, NamedTuple

MINIMIZE_METRICS: Incomplete
MAXIMIZE_METRICS: Incomplete

class CallbackEnv(NamedTuple):
    model: Any
    params: Dict
    iteration: int
    begin_interation: int
    end_iteration: int
    evaluation_result_list: List[_EvalResultTuple]

class _WandbCallback:
    """Internal class to handle `wandb_callback` logic.

    This callback is adapted form the LightGBM's `_RecordEvaluationCallback`.
    """
    order: int
    before_iteration: bool
    log_params: Incomplete
    define_metric_bool: Incomplete
    def __init__(self, log_params: bool = True, define_metric: bool = True) -> None: ...
    def __call__(self, env: CallbackEnv) -> None: ...

def wandb_callback(log_params: bool = True, define_metric: bool = True) -> Callable:
    '''Automatically integrates LightGBM with wandb.

    Arguments:
        log_params: (boolean) if True (default) logs params passed to lightgbm.train as W&B config
        define_metric: (boolean) if True (default) capture model performance at the best step, instead of the last step, of training in your `wandb.summary`

    Passing `wandb_callback` to LightGBM will:
      - log params passed to lightgbm.train as W&B config (default).
      - log evaluation metrics collected by LightGBM, such as rmse, accuracy etc to Weights & Biases
      - Capture the best metric in `wandb.summary` when `define_metric=True` (default).

    Use `log_summary` as an extension of this callback.

    Example:
        ```python
        params = {
            "boosting_type": "gbdt",
            "objective": "regression",
        }
        gbm = lgb.train(
            params,
            lgb_train,
            num_boost_round=10,
            valid_sets=lgb_eval,
            valid_names=("validation"),
            callbacks=[wandb_callback()],
        )
        ```
    '''
def log_summary(model: Booster, feature_importance: bool = True, save_model_checkpoint: bool = False) -> None:
    '''Log useful metrics about lightgbm model after training is done.

    Arguments:
        model: (Booster) is an instance of lightgbm.basic.Booster.
        feature_importance: (boolean) if True (default), logs the feature importance plot.
        save_model_checkpoint: (boolean) if True saves the best model and upload as W&B artifacts.

    Using this along with `wandb_callback` will:

    - log `best_iteration` and `best_score` as `wandb.summary`.
    - log feature importance plot.
    - save and upload your best trained model to Weights & Biases Artifacts (when `save_model_checkpoint = True`)

    Example:
        ```python
        params = {
            "boosting_type": "gbdt",
            "objective": "regression",
        }
        gbm = lgb.train(
            params,
            lgb_train,
            num_boost_round=10,
            valid_sets=lgb_eval,
            valid_names=("validation"),
            callbacks=[wandb_callback()],
        )

        log_summary(gbm)
        ```
    '''
