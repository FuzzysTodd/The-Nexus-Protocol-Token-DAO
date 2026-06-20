from .suggest import preprocess_and_suggest_hyperparams as preprocess_and_suggest_hyperparams
from _typeshed import Incomplete
from flaml.automl.task.task import CLASSIFICATION as CLASSIFICATION

DEFAULT_LOCATION: str

def flamlize_estimator(super_class, name: str, task: str, alternatives: Incomplete | None = None):
    '''Enhance an estimator class with flaml\'s data-dependent default hyperparameter settings.

    Example:

    ```python
    import sklearn.ensemble as ensemble
    RandomForestRegressor = flamlize_estimator(
        ensemble.RandomForestRegressor, "rf", "regression"
    )
    ```

    Args:
        super_class: an scikit-learn compatible estimator class.
        name: a str of the estimator\'s name.
        task: a str of the task type.
        alternatives: (Optional) a list for alternative estimator names. For example,
            ```[("max_depth", 0, "xgboost")]``` means if the "max_depth" is set to 0
            in the constructor, then look for the learned defaults for estimator "xgboost".
    '''

RandomForestClassifier: Incomplete

RandomForestRegressor: Incomplete

ExtraTreesClassifier: Incomplete

ExtraTreesRegressor: Incomplete
LGBMRegressor: Incomplete
LGBMClassifier: Incomplete
XGBClassifier: Incomplete
XGBRegressor: Incomplete
