from .. import Explanation as Explanation, links as links
from ..models import Model as Model
from ..utils import MaskedModel as MaskedModel, OpChain as OpChain, make_masks as make_masks, safe_isinstance as safe_isinstance
from ._explainer import Explainer as Explainer
from _typeshed import Incomplete

class Partition(Explainer):
    input_shape: Incomplete
    model: Incomplete
    expected_value: Incomplete
    __class__: Incomplete
    def __init__(self, model, masker, *, output_names: Incomplete | None = None, link=..., linearize_link: bool = True, feature_names: Incomplete | None = None, **call_args) -> None:
        ''' Uses the Partition SHAP method to explain the output of any function.

        Partition SHAP computes Shapley values recursively through a hierarchy of features, this
        hierarchy defines feature coalitions and results in the Owen values from game theory. The
        PartitionExplainer has two particularly nice properties: 1) PartitionExplainer is
        model-agnostic but when using a balanced partition tree only has quadradic exact runtime
        (in term of the number of input features). This is in contrast to the exponential exact
        runtime of KernelExplainer or SamplingExplainer. 2) PartitionExplainer always assigns to groups of
        correlated features the credit that set of features would have had if treated as a group. This
        means if the hierarchical clustering given to PartitionExplainer groups correlated features
        together, then feature correlations are "accounted for" ... in the sense that the total credit assigned
        to a group of tightly dependent features does net depend on how they behave if their correlation
        structure was broken during the explanation\'s perterbation process. Note that for linear models
        the Owen values that PartitionExplainer returns are the same as the standard non-hierarchical
        Shapley values.


        Parameters
        ----------
        model : function
            User supplied function that takes a matrix of samples (# samples x # features) and
            computes the output of the model for those samples.

        masker : function or numpy.array or pandas.DataFrame or tokenizer
            The function used to "mask" out hidden features of the form `masker(mask, x)`. It takes a
            single input sample and a binary mask and returns a matrix of masked samples. These
            masked samples will then be evaluated using the model function and the outputs averaged.
            As a shortcut for the standard masking using by SHAP you can pass a background data matrix
            instead of a function and that matrix will be used for masking. Domain specific masking
            functions are available in shap such as shap.maksers.Image for images and shap.maskers.Text
            for text.

        partition_tree : None or function or numpy.array
            A hierarchical clustering of the input features represented by a matrix that follows the format
            used by scipy.cluster.hierarchy (see the notebooks_html/partition_explainer directory an example).
            If this is a function then the function produces a clustering matrix when given a single input
            example. If you are using a standard SHAP masker object then you can pass masker.clustering
            to use that masker\'s built-in clustering of the features, or if partition_tree is None then
            masker.clustering will be used by default.

        Examples
        --------
        See `Partition explainer examples <https://shap.readthedocs.io/en/latest/api_examples/explainers/Partition.html>`_
        '''
    def __call__(self, *args, max_evals: int = 500, fixed_context: Incomplete | None = None, main_effects: bool = False, error_bounds: bool = False, batch_size: str = 'auto', outputs: Incomplete | None = None, silent: bool = False):
        """ Explain the output of the model on the given arguments.
        """
    values: Incomplete
    dvalues: Incomplete
    def explain_row(self, *row_args, max_evals, main_effects, error_bounds, batch_size, outputs, silent, fixed_context: str = 'auto'):
        """ Explains a single row and returns the tuple (row_values, row_expected_values, row_mask_shapes).
        """
    last_eval_count: Incomplete
    def owen(self, fm, f00, f11, max_evals, output_indexes, fixed_context, batch_size, silent):
        """ Compute a nested set of recursive Owen values based on an ordering recursion.
        """
    def owen3(self, fm, f00, f11, max_evals, output_indexes, fixed_context, batch_size, silent):
        """ Compute a nested set of recursive Owen values based on an ordering recursion.
        """

def output_indexes_len(output_indexes): ...
def lower_credit(i, value, M, values, clustering) -> None: ...
