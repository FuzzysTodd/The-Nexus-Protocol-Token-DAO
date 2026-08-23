from _typeshed import Incomplete
from flaml.automl.data import DataTransformer as DataTransformer
from flaml.automl.task.factory import task_factory as task_factory
from flaml.automl.task.generic_task import len_labels as len_labels
from flaml.automl.task.task import CLASSIFICATION as CLASSIFICATION, get_classification_objective as get_classification_objective
from flaml.version import __version__ as __version__

LOCATION: Incomplete
logger: Incomplete
CONFIG_PREDICTORS: Incomplete

def meta_feature(task, X_train, y_train, meta_feature_names): ...
def load_config_predictor(estimator_name, task, location: Incomplete | None = None): ...
def suggest_config(task, X, y, estimator_or_predictor, location: Incomplete | None = None, k: Incomplete | None = None, meta_feature_fn=...):
    """Suggest a list of configs for the given task and training data.

    The returned configs can be used as starting points for AutoML.fit().
    `FLAML_sample_size` is removed from the configs.
    """
def suggest_learner(task, X, y, estimator_or_predictor: str = 'all', estimator_list: Incomplete | None = None, location: Incomplete | None = None):
    """Suggest best learner within estimator_list."""
def suggest_hyperparams(task, X, y, estimator_or_predictor, location: Incomplete | None = None):
    '''Suggest hyperparameter configurations and an estimator class.

    The configurations can be used to initialize the estimator class like lightgbm.LGBMRegressor.

    Example:

    ```python
    hyperparams, estimator_class = suggest_hyperparams("regression", X_train, y_train, "lgbm")
    model = estimator_class(**hyperparams)  # estimator_class is LGBMRegressor
    model.fit(X_train, y_train)
    ```

    Args:
        task: A string of the task type, e.g.,
            \'classification\', \'regression\', \'ts_forecast\', \'rank\',
            \'seq-classification\', \'seq-regression\'.
        X: A dataframe of training data in shape n*m.
            For \'ts_forecast\' task, the first column of X_train
            must be the timestamp column (datetime type). Other
            columns in the dataframe are assumed to be exogenous
            variables (categorical or numeric).
        y: A series of labels in shape n*1.
        estimator_or_predictor: A str of the learner name or a dict of the learned config predictor.
            If a dict, it contains:
            - "version": a str of the version number.
            - "preprocessing": a dictionary containing:
                * "center": a list of meta feature value offsets for normalization.
                * "scale": a list of meta feature scales to normalize each dimension.
            - "neighbors": a list of dictionaries. Each dictionary contains:
                * "features": a list of the normalized meta features for a neighbor.
                * "choice": an integer of the configuration id in the portfolio.
            - "portfolio": a list of dictionaries, each corresponding to a configuration:
                * "class": a str of the learner name.
                * "hyperparameters": a dict of the config. The key "FLAML_sample_size" will be ignored.
        location: (Optional) A str of the location containing mined portfolio file.
            Only valid when the portfolio is a str, by default the location is flaml/default.

    Returns:
        hyperparams: A dict of the hyperparameter configurations.
        estiamtor_class: A class of the underlying estimator, e.g., lightgbm.LGBMClassifier.
    '''

class AutoMLTransformer:
    def __init__(self, model, data_transformer) -> None: ...
    def transform(self, X): ...

def preprocess_and_suggest_hyperparams(task, X, y, estimator_or_predictor, location: Incomplete | None = None):
    '''Preprocess the data and suggest hyperparameters.

    Example:

    ```python
    hyperparams, estimator_class, X, y, feature_transformer, label_transformer =         preprocess_and_suggest_hyperparams("classification", X_train, y_train, "xgb_limitdepth")
    model = estimator_class(**hyperparams)  # estimator_class is XGBClassifier
    model.fit(X, y)
    X_test = feature_transformer.transform(X_test)
    y_pred = label_transformer.inverse_transform(pd.Series(model.predict(X_test).astype(int)))
    ```

    Args:
        task: A string of the task type, e.g.,
            \'classification\', \'regression\', \'ts_forecast\', \'rank\',
            \'seq-classification\', \'seq-regression\'.
        X: A dataframe of training data in shape n*m.
            For \'ts_forecast\' task, the first column of X_train
            must be the timestamp column (datetime type). Other
            columns in the dataframe are assumed to be exogenous
            variables (categorical or numeric).
        y: A series of labels in shape n*1.
        estimator_or_predictor: A str of the learner name or a dict of the learned config predictor.
            "choose_xgb" means choosing between xgb_limitdepth and xgboost.
            If a dict, it contains:
            - "version": a str of the version number.
            - "preprocessing": a dictionary containing:
                * "center": a list of meta feature value offsets for normalization.
                * "scale": a list of meta feature scales to normalize each dimension.
            - "neighbors": a list of dictionaries. Each dictionary contains:
                * "features": a list of the normalized meta features for a neighbor.
                * "choice": a integer of the configuration id in the portfolio.
            - "portfolio": a list of dictionaries, each corresponding to a configuration:
                * "class": a str of the learner name.
                * "hyperparameters": a dict of the config. They key "FLAML_sample_size" will be ignored.
        location: (Optional) A str of the location containing mined portfolio file.
            Only valid when the portfolio is a str, by default the location is flaml/default.

    Returns:
        hyperparams: A dict of the hyperparameter configurations.
        estiamtor_class: A class of the underlying estimator, e.g., lightgbm.LGBMClassifier.
        X: the preprocessed X.
        y: the preprocessed y.
        feature_transformer: a data transformer that can be applied to X_test.
        label_transformer: a label transformer that can be applied to y_test.
    '''
