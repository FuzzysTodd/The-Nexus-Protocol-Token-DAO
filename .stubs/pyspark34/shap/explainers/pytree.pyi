from ..utils._exceptions import ExplainerError as ExplainerError
from _typeshed import Incomplete

class TreeExplainer:
    """ A pure Python (slow) implementation of Tree SHAP.
    """
    model_type: str
    trees: Incomplete
    feature_indexes: Incomplete
    zero_fractions: Incomplete
    one_fractions: Incomplete
    pweights: Incomplete
    def __init__(self, model, **kwargs) -> None: ...
    def shap_values(self, X, tree_limit: int = -1, **kwargs): ...
    def shap_interaction_values(self, X, tree_limit: int = -1, **kwargs): ...
    def tree_shap(self, tree, x, x_missing, phi, condition: int = 0, condition_feature: int = 0) -> None: ...

def extend_path(feature_indexes, zero_fractions, one_fractions, pweights, unique_depth, zero_fraction, one_fraction, feature_index) -> None: ...
def unwind_path(feature_indexes, zero_fractions, one_fractions, pweights, unique_depth, path_index) -> None: ...
def unwound_path_sum(feature_indexes, zero_fractions, one_fractions, pweights, unique_depth, path_index): ...

class Tree:
    children_left: Incomplete
    children_right: Incomplete
    children_default: Incomplete
    features: Incomplete
    thresholds: Incomplete
    values: Incomplete
    node_sample_weight: Incomplete
    max_depth: Incomplete
    def __init__(self, tree, normalize: bool = False) -> None: ...

def compute_expectations(children_left, children_right, node_sample_weight, values, i, depth: int = 0): ...
def tree_shap_recursive(children_left, children_right, children_default, features, thresholds, values, node_sample_weight, x, x_missing, phi, node_index, unique_depth, parent_feature_indexes, parent_zero_fractions, parent_one_fractions, parent_pweights, parent_zero_fraction, parent_one_fraction, parent_feature_index, condition, condition_feature, condition_fraction) -> None: ...
