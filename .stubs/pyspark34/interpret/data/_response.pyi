from ..api.base import ExplainerMixin as ExplainerMixin, ExplanationMixin as ExplanationMixin
from ..utils._clean_simple import clean_dimensions as clean_dimensions, typify_classification as typify_classification
from ..utils._clean_x import preclean_X as preclean_X
from ..utils._explanation import gen_global_selector as gen_global_selector, gen_name_from_class as gen_name_from_class
from ..utils._unify_data import unify_data as unify_data
from _typeshed import Incomplete

class Marginal(ExplainerMixin):
    """Provides a marginal plot for provided data."""
    available_explanations: Incomplete
    explainer_type: str
    feature_names: Incomplete
    feature_types: Incomplete
    max_scatter_samples: Incomplete
    def __init__(self, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, max_scatter_samples: int = 400) -> None:
        """Initializes class.

        Args:
            feature_names: List of feature names.
            feature_types: List of feature types.
            max_scatter_samples: Number of sample points in visualization.
        """
    def explain_data(self, X, y, name: Incomplete | None = None):
        """Explains data as visualizations.

        Args:
            X: Numpy array for X to explain.
            y: Numpy vector for y to explain.
            name: User-defined explanation name.

        Returns:
            An explanation object.
        """

class MarginalExplanation(ExplanationMixin):
    """Explanation object specific to marginal explainer."""
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

class ClassHistogram(ExplainerMixin):
    """Provides histogram visualizations for classification problems."""
    available_explanations: Incomplete
    explainer_type: str
    feature_names: Incomplete
    feature_types: Incomplete
    def __init__(self, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None) -> None:
        """Initializes class.

        Args:
            feature_names: List of feature names.
            feature_types: List of feature types.
        """
    def explain_data(self, X, y, name: Incomplete | None = None):
        """Generates data explanations (exploratory data analysis)

        Args:
            X: Numpy array for X to explain.
            y: Numpy vector for y to explain.
            name: User-defined explanation name.

        Returns:
            An explanation object.
        """

class ClassHistogramExplanation(ExplanationMixin):
    """Explanation object specific to class histogram explainer."""
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
