import abc
from ..api.base import ExplainerMixin as ExplainerMixin
from ..api.templates import FeatureValueExplanation as FeatureValueExplanation
from ..utils._clean_simple import clean_dimensions as clean_dimensions, typify_classification as typify_classification
from ..utils._clean_x import preclean_X as preclean_X
from ..utils._explanation import gen_global_selector as gen_global_selector, gen_local_selector as gen_local_selector, gen_name_from_class as gen_name_from_class, gen_perf_dicts as gen_perf_dicts
from ..utils._unify_data import unify_data as unify_data
from _typeshed import Incomplete
from sklearn.base import ClassifierMixin, RegressorMixin

class BaseLinear(metaclass=abc.ABCMeta):
    """Base linear model.

    Currently wrapper around linear models in scikit-learn.

    https://github.com/scikit-learn/scikit-learn

    """
    available_explanations: Incomplete
    explainer_type: str
    feature_names: Incomplete
    feature_types: Incomplete
    linear_class: Incomplete
    kwargs: Incomplete
    def __init__(self, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, linear_class=..., **kwargs) -> None:
        """Initializes class.

        Args:
            feature_names: List of feature names.
            feature_types: List of feature types.
            linear_class: A scikit-learn linear class.
            **kwargs: Kwargs pass to linear class at initialization time.
        """
    n_features_in_: Incomplete
    classes_: Incomplete
    X_mins_: Incomplete
    X_maxs_: Incomplete
    categorical_uniq_: Incomplete
    global_selector_: Incomplete
    has_fitted_: bool
    def fit(self, X, y):
        """Fits model to provided instances.

        Args:
            X: Numpy array for training instances.
            y: Numpy array as training labels.

        Returns:
            Itself.
        """
    def predict(self, X):
        """Predicts on provided instances.

        Args:
            X: Numpy array for instances.

        Returns:
            Predicted class label per instance.
        """
    def explain_local(self, X, y: Incomplete | None = None, name: Incomplete | None = None):
        """Provides local explanations for provided instances.

        Args:
            X: Numpy array for X to explain.
            y: Numpy vector for y to explain.
            name: User-defined explanation name.

        Returns:
            An explanation object, visualizing feature-value pairs
            for each instance as horizontal bar charts.
        """
    def explain_global(self, name: Incomplete | None = None):
        """Provides global explanation for model.

        Args:
            name: User-defined explanation name.

        Returns:
            An explanation object,
            visualizing feature-value pairs as horizontal bar chart.
        """

class LinearExplanation(FeatureValueExplanation):
    """Visualizes specifically for Linear methods."""
    explanation_type: Incomplete
    def __init__(self, explanation_type, internal_obj, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, name: Incomplete | None = None, selector: Incomplete | None = None) -> None:
        """Initializes class.

        Args:
            explanation_type:  Type of explanation.
            internal_obj: A jsonable object that backs the explanation.
            feature_names: List of feature names.
            feature_types: List of feature types.
            name: User-defined name of explanation.
            selector: A dataframe whose indices correspond to explanation entries.
        """
    def visualize(self, key: Incomplete | None = None):
        """Provides interactive visualizations.

        Args:
            key: Either a scalar or list
                that indexes the internal object for sub-plotting.
                If an overall visualization is requested, pass None.

        Returns:
            A Plotly figure.
        """

class LinearRegression(BaseLinear, RegressorMixin, ExplainerMixin):
    """Linear regression.

    Currently wrapper around linear models in scikit-learn: https://github.com/scikit-learn/scikit-learn
    """
    def __init__(self, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, linear_class=..., **kwargs) -> None:
        """Initializes class.

        Args:
            feature_names: List of feature names.
            feature_types: List of feature types.
            linear_class: A scikit-learn linear class.
            **kwargs: Kwargs pass to linear class at initialization time.
        """
    sk_model_: Incomplete
    def fit(self, X, y):
        """Fits model to provided instances.

        Args:
            X: Numpy array for training instances.
            y: Numpy array as training labels.

        Returns:
            Itself.
        """

class LogisticRegression(BaseLinear, ClassifierMixin, ExplainerMixin):
    """Logistic regression.

    Currently wrapper around linear models in scikit-learn: https://github.com/scikit-learn/scikit-learn
    """
    def __init__(self, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, linear_class=..., **kwargs) -> None:
        """Initializes class.

        Args:
            feature_names: List of feature names.
            feature_types: List of feature types.
            linear_class: A scikit-learn linear class.
            **kwargs: Kwargs pass to linear class at initialization time.
        """
    sk_model_: Incomplete
    def fit(self, X, y):
        """Fits model to provided instances.

        Args:
            X: Numpy array for training instances.
            y: Numpy array as training labels.

        Returns:
            Itself.
        """
    def predict_proba(self, X):
        """Probability estimates on provided instances.

        Args:
            X: Numpy array for instances.

        Returns:
            Probability estimate of instance for each class.
        """
