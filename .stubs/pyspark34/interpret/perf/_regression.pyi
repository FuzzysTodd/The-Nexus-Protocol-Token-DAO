from ..api.base import ExplainerMixin as ExplainerMixin, ExplanationMixin as ExplanationMixin
from ..utils._clean_simple import clean_dimensions as clean_dimensions
from ..utils._clean_x import preclean_X as preclean_X
from ..utils._explanation import gen_name_from_class as gen_name_from_class
from ..utils._unify_data import unify_data as unify_data
from ..utils._unify_predict import determine_classes as determine_classes, unify_predict_fn as unify_predict_fn
from _typeshed import Incomplete

class RegressionPerf(ExplainerMixin):
    """Produces variety of regression metrics (including RMSE, R^2, etc)."""
    available_explanations: Incomplete
    explainer_type: str
    model: Incomplete
    feature_names: Incomplete
    feature_types: Incomplete
    def __init__(self, model, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None) -> None:
        """Initializes class.

        Args:
            model: model or prediction function of model (predict_proba for classification or predict for regression)
            feature_names: List of feature names.
            feature_types: List of feature types.
        """
    def explain_perf(self, X, y, name: Incomplete | None = None):
        """Produces regression metrics.

        Args:
            X: Numpy array for X to compare predict function against.
            y: Numpy vector for y to compare predict function against.
            name: User-defined explanation name.

        Returns:
            An explanation object.
        """

class RegressionExplanation(ExplanationMixin):
    """Produces explanation specific to regression metrics."""
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
            A Plotly figure.
        """
