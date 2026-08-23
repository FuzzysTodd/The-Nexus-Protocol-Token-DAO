from .._explainer import Explainer as Explainer
from _typeshed import Incomplete

class Coefficent(Explainer):
    """ Simply returns the model coefficients as the feature attributions.

    This is only for benchmark comparisons and does not approximate SHAP values in a
    meaningful way.
    """
    model: Incomplete
    def __init__(self, model) -> None: ...
    def attributions(self, X): ...
