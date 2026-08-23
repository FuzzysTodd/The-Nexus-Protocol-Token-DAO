from ..utils._clean_x import preclean_X as preclean_X
from ..utils._shap_common import shap_explain_local as shap_explain_local
from ..utils._unify_data import unify_data as unify_data
from _typeshed import Incomplete
from interpret.api.base import ExplainerMixin as ExplainerMixin

class ShapTree(ExplainerMixin):
    """Exposes tree specific SHAP approximation, in interpret API form.
    If using this please cite the original authors as can be found here: https://github.com/slundberg/shap
    """
    available_explanations: Incomplete
    explainer_type: str
    model: Incomplete
    feature_names: Incomplete
    feature_types: Incomplete
    feature_names_in_: Incomplete
    feature_types_in_: Incomplete
    shap_: Incomplete
    def __init__(self, model, data, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, **kwargs) -> None:
        """Initializes class.

        Args:
            model: A tree object that works with Tree SHAP.
            data: Data used to initialize SHAP with.
            feature_names: List of feature names.
            feature_types: List of feature types.
            **kwargs: Kwargs that will be sent to shap.TreeExplainer
        """
    def explain_local(self, X, y: Incomplete | None = None, name: Incomplete | None = None, **kwargs):
        """Provides local explanations for provided instances.

        Args:
            X: Numpy array for X to explain.
            y: Numpy vector for y to explain.
            name: User-defined explanation name.
            **kwargs: Kwargs that will be sent to SHAP

        Returns:
            An explanation object, visualizing feature-value pairs
            for each instance as horizontal bar charts.
        """
