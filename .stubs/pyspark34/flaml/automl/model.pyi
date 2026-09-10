from _typeshed import Incomplete
from collections.abc import Generator
from flaml import tune as tune
from flaml.automl.data import group_counts as group_counts
from flaml.automl.spark import DataFrame as DataFrame, Series as Series, psDataFrame as psDataFrame, psSeries as psSeries, sparkDataFrame as sparkDataFrame
from flaml.automl.spark.utils import len_labels as len_labels, to_pandas_on_spark as to_pandas_on_spark
from flaml.automl.task.factory import task_factory as task_factory
from flaml.automl.task.task import NLG_TASKS as NLG_TASKS, SEQCLASSIFICATION as SEQCLASSIFICATION, SEQREGRESSION as SEQREGRESSION, SUMMARIZATION as SUMMARIZATION, TOKENCLASSIFICATION as TOKENCLASSIFICATION, Task as Task
from pandas import to_datetime as to_datetime
from xgboost.callback import TrainingCallback

SKLEARN_VERSION: Incomplete
xgb_callback: bool
TrainingCallback = object
logger: Incomplete

def TimeoutHandler(sig, frame) -> None: ...
def limit_resource(memory_limit, time_limit) -> Generator[None, None, None]: ...

class BaseEstimator:
    """The abstract class for all learners.

    Typical examples:
    * XGBoostEstimator: for regression.
    * XGBoostSklearnEstimator: for classification.
    * LGBMEstimator, RandomForestEstimator, LRL1Classifier, LRL2Classifier:
        for both regression and classification.
    """
    params: Incomplete
    estimator_class: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None:
        """Constructor.

        Args:
            task: A string of the task type, one of
                'binary', 'multiclass', 'regression', 'rank', 'seq-classification',
                'seq-regression', 'token-classification', 'multichoice-classification',
                'summarization', 'ts_forecast', 'ts_forecast_classification'.
            config: A dictionary containing the hyperparameter names, 'n_jobs' as keys.
                n_jobs is the number of parallel threads.
        """
    def get_params(self, deep: bool = False): ...
    @property
    def classes_(self): ...
    @property
    def n_features_in_(self): ...
    @property
    def model(self):
        """Trained model after fit() is called, or None before fit() is called."""
    @property
    def estimator(self):
        """Trained model after fit() is called, or None before fit() is called."""
    @property
    def feature_names_in_(self):
        """
        if self._model has attribute feature_names_in_, return it.
        otherwise, if self._model has attribute feature_name_, return it.
        otherwise, if self._model has attribute feature_names, return it.
        otherwise, if self._model has method get_booster, return the feature names.
        otherwise, return None.
        """
    @property
    def feature_importances_(self):
        """
        if self._model has attribute feature_importances_, return it.
        otherwise, if self._model has attribute coef_, return it.
        otherwise, return None.
        """
    def fit(self, X_train, y_train, budget: Incomplete | None = None, free_mem_ratio: int = 0, **kwargs):
        """Train the model from given training data.

        Args:
            X_train: A numpy array or a dataframe of training data in shape n*m.
            y_train: A numpy array or a series of labels in shape n*1.
            budget: A float of the time budget in seconds.
            free_mem_ratio: A float between 0 and 1 for the free memory ratio to keep during training.

        Returns:
            train_time: A float of the training time in seconds.
        """
    def predict(self, X, **kwargs):
        """Predict label from features.

        Args:
            X: A numpy array or a dataframe of featurized instances, shape n*m.

        Returns:
            A numpy array of shape n*1.
            Each element is the label for a instance.
        """
    def predict_proba(self, X, **kwargs):
        """Predict the probability of each class from features.

        Only works for classification problems

        Args:
            X: A numpy array of featurized instances, shape n*m.

        Returns:
            A numpy array of shape n*c. c is the # classes.
            Each element at (i,j) is the probability for instance i to be in
                class j.
        """
    def score(self, X_val: DataFrame, y_val: Series, **kwargs):
        """Report the evaluation score of a trained estimator.


        Args:
            X_val: A pandas dataframe of the validation input data.
            y_val: A pandas series of the validation label.
            kwargs: keyword argument of the evaluation function, for example:
                - metric: A string of the metric name or a function
                e.g., 'accuracy', 'roc_auc', 'roc_auc_ovr', 'roc_auc_ovo',
                'f1', 'micro_f1', 'macro_f1', 'log_loss', 'mae', 'mse', 'r2',
                'mape'. Default is 'auto'.
                If metric is given, the score will report the user specified metric.
                If metric is not given, the metric is set to accuracy for classification and r2
                for regression.
                You can also pass a customized metric function, for examples on how to pass a
                customized metric function, please check
                [test/nlp/test_autohf_custom_metric.py](https://github.com/microsoft/FLAML/blob/main/test/nlp/test_autohf_custom_metric.py) and
                [test/automl/test_multiclass.py](https://github.com/microsoft/FLAML/blob/main/test/automl/test_multiclass.py).

        Returns:
            The evaluation score on the validation dataset.
        """
    def cleanup(self) -> None: ...
    @classmethod
    def search_space(cls, data_size, task, **params):
        '''[required method] search space.

        Args:
            data_size: A tuple of two integers, number of rows and columns.
            task: A str of the task type, e.g., "binary", "multiclass", "regression".

        Returns:
            A dictionary of the search space.
            Each key is the name of a hyperparameter, and value is a dict with
                its domain (required) and low_cost_init_value, init_value,
                cat_hp_cost (if applicable).
                e.g., ```{\'domain\': tune.randint(lower=1, upper=10), \'init_value\': 1}```.
        '''
    @classmethod
    def size(cls, config: dict) -> float:
        """[optional method] memory size of the estimator in bytes.

        Args:
            config: A dict of the hyperparameter config.

        Returns:
            A float of the memory size required by the estimator to train the
            given config.
        """
    @classmethod
    def cost_relative2lgbm(cls) -> float:
        """[optional method] relative cost compared to lightgbm."""
    @classmethod
    def init(cls) -> None:
        """[optional method] initialize the class."""
    def config2params(self, config: dict) -> dict:
        """[optional method] config dict to params dict

        Args:
            config: A dict of the hyperparameter config.

        Returns:
            A dict that will be passed to self.estimator_class's constructor.
        """

class SparkEstimator(BaseEstimator):
    """The base class for fine-tuning spark models, using pyspark.ml and SynapseML API."""
    df_train: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...
    def fit(self, X_train: psDataFrame, y_train: psSeries = None, budget: Incomplete | None = None, free_mem_ratio: int = 0, index_col: str = 'tmp_index_col', **kwargs):
        """Train the model from given training data.
        Args:
            X_train: A pyspark.pandas DataFrame of training data in shape n*m.
            y_train: A pyspark.pandas Series in shape n*1. None if X_train is a pyspark.pandas
                Dataframe contains y_train.
            budget: A float of the time budget in seconds.
            free_mem_ratio: A float between 0 and 1 for the free memory ratio to keep during training.
        Returns:
            train_time: A float of the training time in seconds.
        """
    def predict(self, X, index_col: str = 'tmp_index_col', return_all: bool = False, **kwargs):
        '''Predict label from features.
        Args:
            X: A pyspark or pyspark.pandas dataframe of featurized instances, shape n*m.
            index_col: A str of the index column name. Default to "tmp_index_col".
            return_all: A bool of whether to return all the prediction results. Default to False.
        Returns:
            A pyspark.pandas series of shape n*1 if return_all is False. Otherwise, a pyspark.pandas dataframe.
        '''
    def predict_proba(self, X, index_col: str = 'tmp_index_col', return_all: bool = False, **kwargs):
        '''Predict the probability of each class from features.
        Only works for classification problems
        Args:
            X: A pyspark or pyspark.pandas dataframe of featurized instances, shape n*m.
            index_col: A str of the index column name. Default to "tmp_index_col".
            return_all: A bool of whether to return all the prediction results. Default to False.
        Returns:
            A pyspark.pandas dataframe of shape n*c. c is the # classes.
            Each element at (i,j) is the probability for instance i to be in
                class j.
        '''
    @property
    def estimator_params(self): ...

class SparkLGBMEstimator(SparkEstimator):
    """The class for fine-tuning spark version lightgbm models, using SynapseML API."""
    ITER_HP: str
    DEFAULT_ITER: int
    @classmethod
    def search_space(cls, data_size, **params): ...
    def config2params(self, config: dict) -> dict: ...
    @classmethod
    def size(cls, config): ...
    estimator_class: Incomplete
    model_classes_: Incomplete
    model_n_classes_: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...
    def fit(self, X_train, y_train: Incomplete | None = None, budget: Incomplete | None = None, free_mem_ratio: int = 0, index_col: str = 'tmp_index_col', **kwargs): ...

class SparkRandomForestEstimator(SparkEstimator):
    """The SparkEstimator class for Random Forest."""
    nrows: int
    ITER_HP: str
    @classmethod
    def search_space(cls, data_size, task, **params): ...
    estimator_class: Incomplete
    model_classes_: Incomplete
    model_n_classes_: Incomplete
    def __init__(self, task: str = 'classification', **config) -> None: ...
    def fit(self, X_train, y_train: Incomplete | None = None, budget: Incomplete | None = None, free_mem_ratio: int = 0, index_col: str = 'tmp_index_col', **kwargs): ...
    def predict(self, X, index_col: str = 'tmp_index_col', return_all: bool = False, **kwargs):
        '''Predict label from features.
        Args:
            X: A pyspark or pyspark.pandas dataframe of featurized instances, shape n*m.
            index_col: A str of the index column name. Default to "tmp_index_col".
            return_all: A bool of whether to return all the prediction results. Default to False.

        Returns:
            A pyspark.pandas series of shape n*1 if return_all is False. Otherwise, a pyspark.pandas dataframe.
        '''

class TransformersEstimator(BaseEstimator):
    """The class for fine-tuning language models, using huggingface transformers API."""
    ITER_HP: str
    trial_id: Incomplete
    def __init__(self, task: str = 'seq-classification', **config) -> None: ...
    @classmethod
    def search_space(cls, data_size, task, **params): ...
    @property
    def fp16(self): ...
    @property
    def no_cuda(self): ...
    @property
    def num_labels(self): ...
    @property
    def tokenizer(self): ...
    @property
    def data_collator(self): ...
    train_begin_time: Incomplete
    step_begin_time: Incomplete
    time_per_iter: Incomplete
    intermediate_results: Incomplete
    def fit(self, X_train: DataFrame, y_train: Series, budget: Incomplete | None = None, free_mem_ratio: int = 0, X_val: Incomplete | None = None, y_val: Incomplete | None = None, gpu_per_trial: Incomplete | None = None, metric: Incomplete | None = None, **kwargs): ...
    def cleanup(self) -> None: ...
    def predict_proba(self, X, **pred_kwargs): ...
    def score(self, X_val: DataFrame, y_val: Series, **kwargs): ...
    def predict(self, X, **pred_kwargs): ...
    def config2params(self, config: dict) -> dict: ...

class TransformersEstimatorModelSelection(TransformersEstimator):
    def __init__(self, task: str = 'seq-classification', **config) -> None: ...
    @classmethod
    def search_space(cls, data_size, task, **params): ...

class SKLearnEstimator(BaseEstimator):
    """
    The base class for tuning scikit-learn estimators.

    Subclasses can modify the function signature of ``__init__`` to
    ignore the values in ``config`` that are not relevant to the constructor
    of their underlying estimator. For example, some regressors in ``scikit-learn``
    don't accept the ``n_jobs`` parameter contained in ``config``. For these,
    one can add ``n_jobs=None,`` before ``**config`` to make sure ``config`` doesn't
    contain an ``n_jobs`` key.
    """
    def __init__(self, task: str = 'binary', **config) -> None: ...

class LGBMEstimator(BaseEstimator):
    """The class for tuning LGBM, using sklearn API."""
    ITER_HP: str
    HAS_CALLBACK: bool
    DEFAULT_ITER: int
    @classmethod
    def search_space(cls, data_size, **params): ...
    def config2params(self, config: dict) -> dict: ...
    @classmethod
    def size(cls, config): ...
    estimator_class: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...
    def fit(self, X_train, y_train, budget: Incomplete | None = None, free_mem_ratio: int = 0, **kwargs): ...

class XGBoostEstimator(SKLearnEstimator):
    """The class for tuning XGBoost regressor, not using sklearn API."""
    DEFAULT_ITER: int
    @classmethod
    def search_space(cls, data_size, **params): ...
    @classmethod
    def size(cls, config): ...
    @classmethod
    def cost_relative2lgbm(cls): ...
    def config2params(self, config: dict) -> dict: ...
    def __init__(self, task: str = 'regression', **config) -> None: ...
    def fit(self, X_train, y_train, budget: Incomplete | None = None, free_mem_ratio: int = 0, **kwargs): ...
    def predict(self, X, **kwargs): ...

class XGBoostSklearnEstimator(SKLearnEstimator, LGBMEstimator):
    """The class for tuning XGBoost with unlimited depth, using sklearn API."""
    DEFAULT_ITER: int
    @classmethod
    def search_space(cls, data_size, **params): ...
    @classmethod
    def cost_relative2lgbm(cls): ...
    def config2params(self, config: dict) -> dict: ...
    estimator_class: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...
    def fit(self, X_train, y_train, budget: Incomplete | None = None, free_mem_ratio: int = 0, **kwargs): ...

class XGBoostLimitDepthEstimator(XGBoostSklearnEstimator):
    """The class for tuning XGBoost with limited depth, using sklearn API."""
    @classmethod
    def search_space(cls, data_size, **params): ...
    @classmethod
    def cost_relative2lgbm(cls): ...

class RandomForestEstimator(SKLearnEstimator, LGBMEstimator):
    """The class for tuning Random Forest."""
    HAS_CALLBACK: bool
    nrows: int
    @classmethod
    def search_space(cls, data_size, task, **params): ...
    @classmethod
    def cost_relative2lgbm(cls): ...
    def config2params(self, config: dict) -> dict: ...
    estimator_class: Incomplete
    def __init__(self, task: Task, **params) -> None: ...

class ExtraTreesEstimator(RandomForestEstimator):
    """The class for tuning Extra Trees."""
    @classmethod
    def cost_relative2lgbm(cls): ...
    estimator_class: Incomplete
    def __init__(self, task: str = 'binary', **params) -> None: ...

class LRL1Classifier(SKLearnEstimator):
    """The class for tuning Logistic Regression with L1 regularization."""
    @classmethod
    def search_space(cls, **params): ...
    @classmethod
    def cost_relative2lgbm(cls): ...
    def config2params(self, config: dict) -> dict: ...
    estimator_class: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...

class LRL2Classifier(SKLearnEstimator):
    """The class for tuning Logistic Regression with L2 regularization."""
    limit_resource: bool
    @classmethod
    def search_space(cls, **params): ...
    @classmethod
    def cost_relative2lgbm(cls): ...
    def config2params(self, config: dict) -> dict: ...
    estimator_class: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...

class CatBoostEstimator(BaseEstimator):
    """The class for tuning CatBoost."""
    ITER_HP: str
    DEFAULT_ITER: int
    @classmethod
    def search_space(cls, data_size, **params): ...
    @classmethod
    def size(cls, config): ...
    @classmethod
    def cost_relative2lgbm(cls): ...
    def config2params(self, config: dict) -> dict: ...
    estimator_class: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...
    def fit(self, X_train, y_train, budget: Incomplete | None = None, free_mem_ratio: int = 0, **kwargs): ...

class KNeighborsEstimator(BaseEstimator):
    @classmethod
    def search_space(cls, data_size, **params): ...
    @classmethod
    def cost_relative2lgbm(cls): ...
    def config2params(self, config: dict) -> dict: ...
    estimator_class: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...

class SVCEstimator(SKLearnEstimator):
    """The class for tuning Linear Support Vector Machine Classifier."""
    ITER_HP: str
    @classmethod
    def search_space(cls, **params): ...
    def config2params(self, config: dict) -> dict: ...
    estimator_class: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...
    def predict_proba(self, X, **kwargs):
        """Predict the probability of each class from features.

        Only works for classification problems

        Args:
            X: A numpy array of featurized instances, shape n*m.

        Returns:
            A numpy array of shape n*c. c is the # classes.
            Each element at (i,j) is the probability for instance i to be in
                class j.
        """

class SparkNaiveBayesEstimator(SparkEstimator):
    """The class for tuning Naive Bayes Classifier."""
    ITER_HP: str
    @classmethod
    def search_space(cls, data_size, task, **params): ...
    estimator_class: Incomplete
    model_classes_: Incomplete
    model_n_classes_: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...

class SGDEstimator(SKLearnEstimator):
    """The class for tuning Stoachastic Gradient Descent model."""
    ITER_HP: str
    @classmethod
    def search_space(cls, task, **params): ...
    def config2params(self, config: dict) -> dict: ...
    estimator_class: Incomplete
    normalizer: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...
    def predict_proba(self, X, **kwargs):
        """Predict the probability of each class from features.

        Only works for classification problems

        Args:
            X: A numpy array of featurized instances, shape n*m.

        Returns:
            A numpy array of shape n*c. c is the # classes.
            Each element at (i,j) is the probability for instance i to be in
                class j.
        """

class ElasticNetEstimator(SKLearnEstimator):
    """The class for tuning Elastic Net regression model."""
    ITER_HP: str
    @classmethod
    def search_space(cls, **params): ...
    def config2params(self, config: dict) -> dict: ...
    estimator_class: Incomplete
    def __init__(self, task: str = 'regression', **config) -> None: ...

class LassoLarsEstimator(SKLearnEstimator):
    """The class for tuning Lasso model fit with Least Angle Regression a.k.a. Lars."""
    ITER_HP: str
    @classmethod
    def search_space(cls, task: Incomplete | None = None, **params): ...
    def config2params(self, config: dict) -> dict: ...
    estimator_class: Incomplete
    def __init__(self, task: str = 'regression', **config) -> None: ...
    def predict(self, X, **kwargs): ...

class SparkGLREstimator(SparkEstimator):
    """The class for tuning Generalized Linear Regression PySpark model."""
    ITER_HP: str
    @classmethod
    def search_space(cls, data_size, task, **params): ...
    def config2params(self, config): ...
    estimator_class: Incomplete
    model_classes_: Incomplete
    model_n_classes_: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...

class SparkLinearRegressionEstimator(SparkEstimator):
    """The class for tuning Linear Regression PySpark model."""
    ITER_HP: str
    @classmethod
    def search_space(cls, data_size, task, **params): ...
    estimator_class: Incomplete
    model_classes_: Incomplete
    model_n_classes_: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...
    def config2params(self, config): ...

class SparkLinearSVCEstimator(SparkEstimator):
    """The class for tuning Linear SVC PySpark model."""
    ITER_HP: str
    @classmethod
    def search_space(cls, data_size, task, **params): ...
    estimator_class: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...

class SparkGBTEstimator(SparkEstimator):
    """The class for tuning GBT PySpark model."""
    ITER_HP: str
    @classmethod
    def search_space(cls, data_size, task, **params): ...
    estimator_class: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...

class SparkAFTSurvivalRegressionEstimator(SparkEstimator):
    """The class for tuning AFTSurvivalRegression PySpark model."""
    ITER_HP: str
    @classmethod
    def search_space(cls, data_size, task, **params): ...
    estimator_class: Incomplete
    def __init__(self, task: str = 'binary', **config) -> None: ...

class BaseResourceLimit:
    start_time: Incomplete
    deadline: Incomplete
    free_mem_ratio: Incomplete
    def __init__(self, start_time, deadline, free_mem_ratio) -> None: ...
    def check_resource_limits(self, current_time, current_iteration, mllib): ...
    def after_iteration(self, *args, **kwargs) -> bool: ...

class XGBoostResourceLimit(BaseResourceLimit, TrainingCallback):
    def after_iteration(self, model, epoch, evals_log) -> bool: ...

class CatBoostResourceLimit(BaseResourceLimit):
    def after_iteration(self, info) -> bool: ...

class suppress_stdout_stderr:
    null_fds: Incomplete
    save_fds: Incomplete
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *_) -> None: ...
