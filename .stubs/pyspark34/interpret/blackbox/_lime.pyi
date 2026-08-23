from ..api.base import ExplainerMixin as ExplainerMixin
from ..api.templates import FeatureValueExplanation as FeatureValueExplanation
from ..utils._clean_simple import clean_dimensions as clean_dimensions, typify_classification as typify_classification
from ..utils._clean_x import preclean_X as preclean_X
from ..utils._explanation import gen_local_selector as gen_local_selector, gen_name_from_class as gen_name_from_class, gen_perf_dicts as gen_perf_dicts
from ..utils._unify_data import unify_data as unify_data
from ..utils._unify_predict import determine_classes as determine_classes, unify_predict_fn as unify_predict_fn
from _typeshed import Incomplete

class LimeTabular(ExplainerMixin):
    """Exposes LIME tabular explainer from lime package, in interpret API form.
    If using this please cite the original authors as can be found here:
    https://github.com/marcotcr/lime/blob/master/citation.bib
    """
    available_explanations: Incomplete
    explainer_type: str
    model: Incomplete
    feature_names: Incomplete
    feature_types: Incomplete
    lime_: Incomplete
    def __init__(self, model, data, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None, **kwargs) -> None:
        """Initializes class.

        Args:
            model: model or prediction function of model (predict_proba for classification or predict for regression)
            data: Data used to initialize LIME with.
            feature_names: List of feature names.
            feature_types: List of feature types.
            **kwargs: Kwargs that will be sent to lime
        """
    def explain_local(self, X, y: Incomplete | None = None, name: Incomplete | None = None, **kwargs):
        """Generates local explanations for provided instances.

        Args:
            X: Numpy array for X to explain.
            y: Numpy vector for y to explain.
            name: User-defined explanation name.
            **kwargs: Kwargs that will be sent to lime

        Returns:
            An explanation object, visualizing feature-value pairs
            for each instance as horizontal bar charts.
        """
