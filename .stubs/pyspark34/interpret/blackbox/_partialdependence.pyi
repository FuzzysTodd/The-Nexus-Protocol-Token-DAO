from ..api.base import ExplainerMixin as ExplainerMixin, ExplanationMixin as ExplanationMixin
from ..utils._clean_x import preclean_X as preclean_X
from ..utils._explanation import gen_global_selector as gen_global_selector, gen_name_from_class as gen_name_from_class
from ..utils._unify_data import unify_data as unify_data
from ..utils._unify_predict import determine_classes as determine_classes, unify_predict_fn as unify_predict_fn
from _typeshed import Incomplete

class PartialDependence(ExplainerMixin):
    '''Partial dependence plots as defined in Friedman\'s paper on
    "Greedy function approximation: a gradient boosting machine".

    Friedman, Jerome H. "Greedy function approximation: a gradient boosting machine."
    Annals of statistics (2001): 1189-1232.
    '''
    available_explanations: Incomplete
    explainer_type: str
    pdps_: Incomplete
    unique_val_counts_: Incomplete
    def __init__(self, model, data, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, num_points: int = 10, std_coef: float = 1.0) -> None:
        """Initializes class.

        Args:
            model: model or prediction function of model (predict_proba for classification or predict for regression)
            data: Data used to initialize PartialDependence with.
            feature_names: List of feature names.
            feature_types: List of feature types.
            num_points: Number of grid points for the x axis.
            std_coef: Co-efficient for standard deviation.
        """
    def explain_global(self, name: Incomplete | None = None):
        """Provides approximate global explanation for blackbox model.

        Args:
            name: User-defined explanation name.

        Returns:
            An explanation object, visualizes dependence plots.
        """

class PDPExplanation(ExplanationMixin):
    """Visualizes explanation as a partial dependence plot."""
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
