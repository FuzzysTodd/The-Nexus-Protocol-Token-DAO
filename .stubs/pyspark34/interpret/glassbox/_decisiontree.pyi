import abc
from ..api.base import ExplainerMixin as ExplainerMixin, ExplanationMixin as ExplanationMixin
from ..utils._clean_simple import clean_dimensions as clean_dimensions, typify_classification as typify_classification
from ..utils._clean_x import preclean_X as preclean_X
from ..utils._explanation import gen_global_selector as gen_global_selector, gen_local_selector as gen_local_selector, gen_name_from_class as gen_name_from_class, gen_perf_dicts as gen_perf_dicts
from ..utils._unify_data import unify_data as unify_data
from _typeshed import Incomplete
from sklearn.base import ClassifierMixin, RegressorMixin

COLORS: Incomplete

class TreeExplanation(ExplanationMixin):
    """Explanation object specific to trees."""
    explanation_type: Incomplete
    feature_names: Incomplete
    feature_types: Incomplete
    name: Incomplete
    selector: Incomplete
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
    def data(self, key: Incomplete | None = None):
        """Provides specific explanation data.

        Args:
            key: A number/string that references a specific data item.

        Returns:
            A serializable dictionary.
        """
    def visualize(self, key: Incomplete | None = None):
        """Provides interactive visualizations.

        Args:
            key: Either a scalar or list
                that indexes the internal object for sub-plotting.
                If an overall visualization is requested, pass None.

        Returns:
            A Dash Cytoscape object.
        """

class BaseShallowDecisionTree(metaclass=abc.ABCMeta):
    """Shallow Decision Tree (low depth).

    Currently wrapper around DecisionTreeClassifier or DecisionTreeRegressor in scikit-learn.
    To keep the tree shallow, max depth is defaulted to 3.

    https://github.com/scikit-learn/scikit-learn

    """
    available_explanations: Incomplete
    explainer_type: str
    feature_names: Incomplete
    feature_types: Incomplete
    max_depth: Incomplete
    kwargs: Incomplete
    def __init__(self, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, max_depth: int = 3, **kwargs) -> None:
        """Initializes tree with low depth.

        Args:
            feature_names: List of feature names.
            feature_types: List of feature types.
            max_depth: Max depth of tree.
            **kwargs: Kwargs sent to __init__() method of tree.
        """
    global_selector_: Incomplete
    n_samples_: Incomplete
    n_features_in_: Incomplete
    classes_: Incomplete
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
    def explain_global(self, name: Incomplete | None = None):
        """Provides global explanation for model.

        Args:
            name: User-defined explanation name.

        Returns:
            An explanation object,
            visualizing feature-value pairs as horizontal bar chart.
        """
    def explain_local(self, X, y: Incomplete | None = None, name: Incomplete | None = None):
        """Provides local explanations for provided instances.

        Args:
            X: Numpy array for X to explain.
            y: Numpy vector for y to explain.
            name: User-defined explanation name.

        Returns:
            An explanation object.
        """

class RegressionTree(BaseShallowDecisionTree, RegressorMixin, ExplainerMixin):
    """Regression tree with shallow depth."""
    def __init__(self, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, max_depth: int = 3, **kwargs) -> None:
        """Initializes tree with low depth.

        Args:
            feature_names: List of feature names.
            feature_types: List of feature types.
            max_depth: Max depth of tree.
            **kwargs: Kwargs sent to __init__() method of tree.
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

class ClassificationTree(BaseShallowDecisionTree, ClassifierMixin, ExplainerMixin):
    """Classification tree with shallow depth."""
    def __init__(self, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, max_depth: int = 3, **kwargs) -> None:
        """Initializes tree with low depth.

        Args:
            feature_names: List of feature names.
            feature_types: List of feature types.
            max_depth: Max depth of tree.
            **kwargs: Kwargs sent to __init__() method of tree.
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
