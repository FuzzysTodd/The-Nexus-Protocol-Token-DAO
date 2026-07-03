from _typeshed import Incomplete
from flaml import tune as tune
from flaml.automl.model import BaseEstimator as BaseEstimator
from flaml.automl.task.task import Task as Task
from flaml.automl.time_series.ts_data import TimeSeriesDataset as TimeSeriesDataset
from sklearn.base import BaseEstimator as SKLearnBaseEstimator, TransformerMixin
from sklearn.feature_selection import SelectorMixin
from typing import Any, Dict, List, Tuple

logger: Incomplete

def get_transformer(stage: str, method: str) -> TransformerMixin:
    """
    Get the transformer object based on the specified stage and method.

    Args:
        stage: The stage of the transformation.
        method: The method of the transformation.

    Returns:
        transformer: The transformer object, should be a sklearn.base.TransformerMixin object.

    Raises:
        ValueError: If the specified stage or method is not avaliable.
    """
def parse_autofe_config(raw_config: str | Dict, data: Any, task: Task, learner_class: BaseEstimator) -> Dict[str, Dict[str, tune.sample.Categorical]]:
    """Handle the autofe config.

    Args:
        raw_config: Source config to handle, should be a dict or a string.
        data: Training data. Could be any type that flaml supports.
        task: The flaml Task object, to determine what methods are avaliable.
        learner_class: The flaml Estimator class, to determine what methods are avaliable.

    Raises:
        ValueError: Unsupported config.

    Returns:
        search_space: a FLAML search space.
    """

class Featurization(SKLearnBaseEstimator, TransformerMixin):
    """A class to implement the featurization pipeline."""
    pipeline: Incomplete
    flaml_transformer: Incomplete
    task: Incomplete
    detail_config: Incomplete
    ts_dataset: Incomplete
    def __init__(self, params: Dict | None = None, task: Task | None = None, config: List[Dict] | None = None) -> None:
        """Init the Featurization class.

        Args:
            params: Init based on a hyperparameter config.
            task: The flaml Task object, to determine implementation detail.
            config: Init based on a config.

        Raises:
            ValueError: If neither params nor config is provided.
        """
    @property
    def config(self) -> List[Dict]:
        """Get the config of the featurization pipeline. Could be use for reconstruct. Also an alias for self.detail_config"""
    @property
    def params(self) -> Dict:
        """Get the hyperparameter config of the featurization pipeline. Could be use for reconstruct."""
    def standalone_init(self, config: List[Dict]) -> Dict:
        """Init function for reconstruct.

        Args:
            config: The config to init the Featurization class.

        Raises:
            ValueError: Unknown stage or method.

        Returns:
            config: The inner config inside the Featurization class.
        """
    def static_preprocess(self, X, y):
        """General static preprocess function before all featurization stages.

        Args:
            X: Training data.
            y: Training label.

        Returns:
            X: Processed training data.
            y: Processed training label.
            categorical_features: a list of names of categorical features in the X.
            numerical_features: a list of names of numerical features in the X.
        """
    def build_transformer(self, stage: str, features: List[str]) -> Tuple[TransformerMixin, List[str], Dict]:
        """
        Build a transformer object based on the specified stage and features.

        Args:
            stage: The stage of the transformation.
            features: The list of features to be transformed.

        Returns:
            encoder: The transformer object, should be a sklearn.base.TransformerMixin object.
            features: The list of features to be transformed.
            detail_config: The config of the transformer object.

        """
    def fit(self, X, y: Incomplete | None = None):
        """Fit the featurization pipeline."""
    def transform(self, X, time_col: Incomplete | None = None): ...
    def show_transformations(self) -> None:
        """Print the featurization pipeline."""

class CardinalitySelector(SelectorMixin, SKLearnBaseEstimator):
    """Class to drop columns with high cardinality."""
    threshold: Incomplete
    support_: Incomplete
    def __init__(self, threshold: float = 0.6) -> None: ...
    def fit(self, X, y: Incomplete | None = None): ...

avaliable_methods: Incomplete
