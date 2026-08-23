from ._result import BenchmarkResult as BenchmarkResult
from _typeshed import Incomplete
from shap import Explanation as Explanation, links as links
from shap.maskers import FixedComposite as FixedComposite, Image as Image, Text as Text
from shap.utils import MaskedModel as MaskedModel, partition_tree_shuffle as partition_tree_shuffle, safe_isinstance as safe_isinstance

class ExplanationError:
    """ A measure of the explanation error relative to a model's actual output.

    This benchmark metric measures the discrepancy between the output of the model predicted by an
    attribution explanation vs. the actual output of the model. This discrepancy is measured over
    many masking patterns drawn from permutations of the input features.

    For explanations (like Shapley values) that explain the difference between one alternative and another
    (for example a current sample and typical background feature values) there is possible explanation error
    for every pattern of mixing foreground and background, or other words every possible masking pattern.
    In this class we compute the standard deviation over these explanation errors where masking patterns
    are drawn from prefixes of random feature permutations. This seems natural, and aligns with Shapley value
    computations, but of course you could choose to summarize explanation errors in others ways as well.
    """
    masker: Incomplete
    model: Incomplete
    model_args: Incomplete
    num_permutations: Incomplete
    link: Incomplete
    linearize_link: Incomplete
    batch_size: Incomplete
    seed: Incomplete
    data_type: str
    def __init__(self, masker, model, *model_args, batch_size: int = 500, num_permutations: int = 10, link=..., linearize_link: bool = True, seed: int = 38923) -> None:
        """ Build a new explanation error benchmarker with the given masker, model, and model args.

        Parameters
        ----------
        masker : function or shap.Masker
            The masker defines how we hide features during the perturbation process.

        model : function or shap.Model
            The model we want to evaluate explanations against.

        model_args : ...
            The list of arguments we will give to the model that we will have explained. When we later call this benchmark
            object we should pass explanations that have been computed on this same data.

        batch_size : int
            The maximum batch size we should use when calling the model. For some large NLP models this needs to be set
            lower (at say 1) to avoid running out of GPU memory.

        num_permutations : int
            How many permutations we will use to estimate the average explanation error for each sample. If you are running
            this benchmark on a large dataset with many samples then you can reduce this value since the final result is
            averaged over samples as well and the averages of both directly combine to reduce variance. So for 10k samples
            num_permutations=1 is appropreiate.

        link : function
            Allows for a non-linear link function to be used to bringe between the model output space and the explanation
            space.

        linearize_link : bool
            Non-linear links can destroy additive separation in generalized linear models, so by linearizing the link we can
            retain additive separation. See upcoming paper/doc for details.
        """
    def __call__(self, explanation, name, step_fraction: float = 0.01, indices=[], silent: bool = False):
        """ Run this benchmark on the given explanation.
        """
