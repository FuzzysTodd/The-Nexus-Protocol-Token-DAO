from .. import links as links
from ..models import Model as Model
from ..utils import MaskedModel as MaskedModel, partition_tree_shuffle as partition_tree_shuffle
from ._explainer import Explainer as Explainer
from _typeshed import Incomplete

class Permutation(Explainer):
    """ This method approximates the Shapley values by iterating through permutations of the inputs.

    This is a model agnostic explainer that guarantees local accuracy (additivity) by iterating completely
    through an entire permutation of the features in both forward and reverse directions (antithetic sampling).
    If we do this once, then we get the exact SHAP values for models with up to second order interaction effects.
    We can iterate this many times over many random permutations to get better SHAP value estimates for models
    with higher order interactions. This sequential ordering formulation also allows for easy reuse of
    model evaluations and the ability to efficiently avoid evaluating the model when the background values
    for a feature are the same as the current input value. We can also account for hierarchical data
    structures with partition trees, something not currently implemented for KernalExplainer or SamplingExplainer.
    """
    model: Incomplete
    __class__: Incomplete
    def __init__(self, model, masker, link=..., feature_names: Incomplete | None = None, linearize_link: bool = True, seed: Incomplete | None = None, **call_args) -> None:
        ''' Build an explainers.Permutation object for the given model using the given masker object.

        Parameters
        ----------
        model : function
            A callable python object that executes the model given a set of input data samples.

        masker : function or numpy.array or pandas.DataFrame
            A callable python object used to "mask" out hidden features of the form `masker(binary_mask, x)`.
            It takes a single input sample and a binary mask and returns a matrix of masked samples. These
            masked samples are evaluated using the model function and the outputs are then averaged.
            As a shortcut for the standard masking using by SHAP you can pass a background data matrix
            instead of a function and that matrix will be used for masking. To use a clustering
            game structure you can pass a shap.maskers.Tabular(data, clustering="correlation") object.

        seed: None or int
            Seed for reproducibility

        **call_args : valid argument to the __call__ method
            These arguments are saved and passed to the __call__ method as the new default values for these arguments.
        '''
    def __call__(self, *args, max_evals: int = 500, main_effects: bool = False, error_bounds: bool = False, batch_size: str = 'auto', outputs: Incomplete | None = None, silent: bool = False):
        """ Explain the output of the model on the given arguments.
        """
    def explain_row(self, *row_args, max_evals, main_effects, error_bounds, batch_size, outputs, silent):
        """ Explains a single row and returns the tuple (row_values, row_expected_values, row_mask_shapes).
        """
    def shap_values(self, X, npermutations: int = 10, main_effects: bool = False, error_bounds: bool = False, batch_evals: bool = True, silent: bool = False):
        """ Legacy interface to estimate the SHAP values for a set of samples.

        Parameters
        ----------
        X : numpy.array or pandas.DataFrame or any scipy.sparse matrix
            A matrix of samples (# samples x # features) on which to explain the model's output.

        npermutations : int
            Number of times to cycle through all the features, re-evaluating the model at each step.
            Each cycle evaluates the model function 2 * (# features + 1) times on a data matrix of
            (# background data samples) rows. An exception to this is when PermutationExplainer can
            avoid evaluating the model because a feature's value is the same in X and the background
            dataset (which is common for example with sparse features).

        Returns
        -------
        array or list
            For models with a single output this returns a matrix of SHAP values
            (# samples x # features). Each row sums to the difference between the model output for that
            sample and the expected value of the model output (which is stored as expected_value
            attribute of the explainer). For models with vector outputs this returns a list
            of such matrices, one for each output.
        """
