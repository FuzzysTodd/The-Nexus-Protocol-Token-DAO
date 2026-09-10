import interpret.api.base
from _typeshed import Incomplete

class FeatureValueExplanation(interpret.api.base.ExplanationMixin):
    """Handles explanations that can be visualized as horizontal bar graphs.
    Usually these are feature-value pairs being represented.
    """
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
    def visualize(self, key: Incomplete | None = None, title: Incomplete | None = None):
        """Provides interactive visualizations.

        Args:
            key: Either a scalar or list
                that indexes the internal object for sub-plotting.
                If an overall visualization is requested, pass None.

        Returns:
            A Plotly figure.
        """
