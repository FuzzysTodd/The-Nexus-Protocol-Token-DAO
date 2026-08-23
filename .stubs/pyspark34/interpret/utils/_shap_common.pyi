from ..api.templates import FeatureValueExplanation as FeatureValueExplanation
from ..utils._clean_simple import clean_dimensions as clean_dimensions, typify_classification as typify_classification
from ..utils._clean_x import preclean_X as preclean_X
from ..utils._unify_data import unify_data as unify_data
from ..utils._unify_predict import determine_classes as determine_classes, unify_predict_fn as unify_predict_fn
from ._explanation import gen_local_selector as gen_local_selector, gen_name_from_class as gen_name_from_class, gen_perf_dicts as gen_perf_dicts

def shap_explain_local(explainer, X, y, name, is_treeshap, **kwargs): ...
