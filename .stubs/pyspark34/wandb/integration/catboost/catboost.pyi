from _typeshed import Incomplete
from catboost import CatBoostClassifier, CatBoostRegressor
from types import SimpleNamespace

class WandbCallback:
    '''`WandbCallback` automatically integrates CatBoost with wandb.

    Arguments:
        - metric_period: (int) if you are passing `metric_period` to your CatBoost model please pass the same value here (default=1).

    Passing `WandbCallback` to CatBoost will:
    - log training and validation metrics at every `metric_period`
    - log iteration at every `metric_period`

    Example:
        ```
        train_pool = Pool(train[features], label=train["label"], cat_features=cat_features)
        test_pool = Pool(test[features], label=test["label"], cat_features=cat_features)

        model = CatBoostRegressor(
            iterations=100,
            loss_function="Cox",
            eval_metric="Cox",
        )

        model.fit(
            train_pool,
            eval_set=test_pool,
            callbacks=[WandbCallback()],
        )
        ```
    '''
    metric_period: Incomplete
    def __init__(self, metric_period: int = 1) -> None: ...
    def after_iteration(self, info: SimpleNamespace) -> bool: ...

def log_summary(model: CatBoostClassifier | CatBoostRegressor, log_all_params: bool = True, save_model_checkpoint: bool = False, log_feature_importance: bool = True) -> None:
    '''`log_summary` logs useful metrics about catboost model after training is done.

    Arguments:
        model: it can be CatBoostClassifier or CatBoostRegressor.
        log_all_params: (boolean) if True (default) log the model hyperparameters as W&B config.
        save_model_checkpoint: (boolean) if True saves the model upload as W&B artifacts.
        log_feature_importance: (boolean) if True (default) logs feature importance as W&B bar chart using the default setting of `get_feature_importance`.

    Using this along with `wandb_callback` will:

    - save the hyperparameters as W&B config,
    - log `best_iteration` and `best_score` as `wandb.summary`,
    - save and upload your trained model to Weights & Biases Artifacts (when `save_model_checkpoint = True`)
    - log feature importance plot.

    Example:
        ```python
        train_pool = Pool(train[features], label=train["label"], cat_features=cat_features)
        test_pool = Pool(test[features], label=test["label"], cat_features=cat_features)

        model = CatBoostRegressor(
            iterations=100,
            loss_function="Cox",
            eval_metric="Cox",
        )

        model.fit(
            train_pool,
            eval_set=test_pool,
            callbacks=[WandbCallback()],
        )

        log_summary(model)
        ```
    '''
