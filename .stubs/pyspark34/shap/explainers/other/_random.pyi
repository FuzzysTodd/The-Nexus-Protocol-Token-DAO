from .._explainer import Explainer as Explainer
from _typeshed import Incomplete
from shap import links as links
from shap.models import Model as Model
from shap.utils import MaskedModel as MaskedModel

class Random(Explainer):
    """ Simply returns random (normally distributed) feature attributions.

    This is only for benchmark comparisons. It supports both fully random attributions and random
    attributions that are constant across all explainations.
    """
    model: Incomplete
    constant: Incomplete
    constant_attributions: Incomplete
    def __init__(self, model, masker, link=..., feature_names: Incomplete | None = None, linearize_link: bool = True, constant: bool = False, **call_args) -> None: ...
    def explain_row(self, *row_args, max_evals, main_effects, error_bounds, batch_size, outputs, silent):
        """ Explains a single row.
        """
