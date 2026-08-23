from .._explainer import Explainer as Explainer
from _typeshed import Incomplete

class TreeGain(Explainer):
    """ Simply returns the global gain/gini feature importances for tree models.

    This is only for benchmark comparisons and is not meant to approximate SHAP values.
    """
    model: Incomplete
    def __init__(self, model) -> None: ...
    def attributions(self, X): ...
