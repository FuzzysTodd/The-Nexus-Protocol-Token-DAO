from ._result import BenchmarkResult as BenchmarkResult
from _typeshed import Incomplete
from shap import Explanation as Explanation, links as links
from shap.maskers import FixedComposite as FixedComposite, Image as Image, Text as Text
from shap.utils import MaskedModel as MaskedModel, safe_isinstance as safe_isinstance

class SequentialMasker:
    inner: Incomplete
    model_args: Incomplete
    batch_size: Incomplete
    def __init__(self, mask_type, sort_order, masker, model, *model_args, batch_size: int = 500) -> None: ...
    def __call__(self, explanation, name, **kwargs): ...

class SequentialPerturbation:
    model: Incomplete
    masker: Incomplete
    sort_order: Incomplete
    perturbation: Incomplete
    linearize_link: Incomplete
    sort_order_map: Incomplete
    data_type: str
    score_values: Incomplete
    score_aucs: Incomplete
    labels: Incomplete
    def __init__(self, model, masker, sort_order, perturbation, linearize_link: bool = False) -> None: ...
    masked_model: Incomplete
    def __call__(self, name, explanation, *model_args, percent: float = 0.01, indices=[], y: Incomplete | None = None, label: Incomplete | None = None, silent: bool = False, debug_mode: bool = False, batch_size: int = 10): ...
    def score(self, explanation, X, percent: float = 0.01, y: Incomplete | None = None, label: Incomplete | None = None, silent: bool = False, debug_mode: bool = False):
        """
        Will be deprecated once MaskedModel is in complete support
        """
    def plot(self, xs, ys, auc) -> None: ...
