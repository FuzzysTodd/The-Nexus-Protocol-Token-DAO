from ..api.base import ExplainerMixin as ExplainerMixin
from ..api.templates import FeatureValueExplanation as FeatureValueExplanation
from ..utils._clean_simple import clean_dimensions as clean_dimensions, typify_classification as typify_classification
from ..utils._clean_x import preclean_X as preclean_X
from ..utils._explanation import gen_local_selector as gen_local_selector, gen_name_from_class as gen_name_from_class, gen_perf_dicts as gen_perf_dicts
from ..utils._unify_data import unify_data as unify_data
from ..utils._unify_predict import determine_classes as determine_classes, unify_predict_fn as unify_predict_fn
from _typeshed import Incomplete

class TreeInterpreter(ExplainerMixin):
    """Provides 'Tree Explainer' algorithm for specific sklearn trees.

    Wrapper around andosa/treeinterpreter github package.

    https://github.com/andosa/treeinterpreter

    Currently supports (copied from README.md):

    - DecisionTreeRegressor
    - DecisionTreeClassifier
    - ExtraTreeRegressor
    - ExtraTreeClassifier
    - RandomForestRegressor
    - RandomForestClassifier
    - ExtraTreesRegressor
    - ExtraTreesClassifier

    """
    available_explanations: Incomplete
    explainer_type: str
    model: Incomplete
    feature_names: Incomplete
    feature_types: Incomplete
    feature_names_in_: Incomplete
    feature_types_in_: Incomplete
    def __init__(self, model, data: Incomplete | None = None, feature_names: Incomplete | None = None, feature_types: Incomplete | None = None) -> None:
        """Initializes class.

        Args:
            model: A scikit-learn tree object
            data: mostly ignored. Only included for conformance to the greybox API
                  if data is provided though we use it to determine the feature names and types
            feature_names: List of feature names.
            feature_types: List of feature types.
        """
    def explain_local(self, X, y: Incomplete | None = None, name: Incomplete | None = None, **kwargs):
        """Provides local explanations for provided instances.

        Args:
            X: Numpy array for X to explain.
            y: Numpy vector for y to explain.
            name: User-defined explanation name.
            **kwargs: Kwargs that will be sent to treeinterpreter

        Returns:
            An explanation object, visualizing feature-value pairs
            for each instance as horizontal bar charts.
        """
