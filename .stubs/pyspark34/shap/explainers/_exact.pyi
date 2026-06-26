from .. import links as links
from ..models import Model as Model
from ..utils import MaskedModel as MaskedModel, delta_minimization_order as delta_minimization_order, make_masks as make_masks, shapley_coefficients as shapley_coefficients
from ._explainer import Explainer as Explainer
from _typeshed import Incomplete

log: Incomplete

class Exact(Explainer):
    """ Computes SHAP values via an optimized exact enumeration.

    This works well for standard Shapley value maskers for models with less than ~15 features that vary
    from the background per sample. It also works well for Owen values from hclustering structured
    maskers when there are less than ~100 features that vary from the background per sample. This
    explainer minimizes the number of function evaluations needed by ordering the masking sets to
    minimize sequential differences. This is done using gray codes for standard Shapley values
    and a greedy sorting method for hclustering structured maskers.
    """
    model: Incomplete
    def __init__(self, model, masker, link=..., linearize_link: bool = True, feature_names: Incomplete | None = None) -> None:
        ''' Build an explainers.Exact object for the given model using the given masker object.

        Parameters
        ----------
        model : function
            A callable python object that executes the model given a set of input data samples.

        masker : function or numpy.array or pandas.DataFrame
            A callable python object used to "mask" out hidden features of the form `masker(mask, *fargs)`.
            It takes a single a binary mask and an input sample and returns a matrix of masked samples. These
            masked samples are evaluated using the model function and the outputs are then averaged.
            As a shortcut for the standard masking used by SHAP you can pass a background data matrix
            instead of a function and that matrix will be used for masking. To use a clustering
            game structure you can pass a shap.maskers.TabularPartitions(data) object.

        link : function
            The link function used to map between the output units of the model and the SHAP value units. By
            default it is shap.links.identity, but shap.links.logit can be useful so that expectations are
            computed in probability units while explanations remain in the (more naturally additive) log-odds
            units. For more details on how link functions work see any overview of link functions for generalized
            linear models.

        linearize_link : bool
            If we use a non-linear link function to take expectations then models that are additive with respect to that
            link function for a single background sample will no longer be additive when using a background masker with
            many samples. This for example means that a linear logistic regression model would have interaction effects
            that arise from the non-linear changes in expectation averaging. To retain the additively of the model with
            still respecting the link function we linearize the link function by default.
        '''
    def __call__(self, *args, max_evals: int = 100000, main_effects: bool = False, error_bounds: bool = False, batch_size: str = 'auto', interactions: int = 1, silent: bool = False):
        """ Explains the output of model(*args), where args represents one or more parallel iterators.
        """
    def explain_row(self, *row_args, max_evals, main_effects, error_bounds, batch_size, outputs, interactions, silent):
        """ Explains a single row and returns the tuple (row_values, row_expected_values, row_mask_shapes).
        """

def partition_delta_indexes(partition_tree, all_masks):
    """ Return an delta index encoded array of all the masks possible while following the given partition tree.
    """
def partition_masks(partition_tree):
    """ Return an array of all the masks possible while following the given partition tree.
    """
def gray_code_masks(nbits):
    """ Produces an array of all binary patterns of size nbits in gray code order.

    This is based on code from: http://code.activestate.com/recipes/576592-gray-code-generatoriterator/
    """
def gray_code_indexes(nbits):
    """ Produces an array of which bits flip at which position.

    We assume the masks start at all zero and -1 means don't do a flip.
    This is a more efficient representation of the gray_code_masks version.
    """
