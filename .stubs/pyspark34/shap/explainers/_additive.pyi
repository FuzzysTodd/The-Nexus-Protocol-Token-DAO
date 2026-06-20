from ..utils import MaskedModel as MaskedModel, safe_isinstance as safe_isinstance
from ._explainer import Explainer as Explainer
from _typeshed import Incomplete

class Additive(Explainer):
    """ Computes SHAP values for generalized additive models.

    This assumes that the model only has first-order effects. Extending this to
    second- and third-order effects is future work (if you apply this to those models right now
    you will get incorrect answers that fail additivity).
    """
    model: Incomplete
    def __init__(self, model, masker, link: Incomplete | None = None, feature_names: Incomplete | None = None, linearize_link: bool = True) -> None:
        ''' Build an Additive explainer for the given model using the given masker object.

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
            game structure you can pass a shap.maskers.Tabular(data, hclustering="correlation") object, but
            note that this structure information has no effect on the explanations of additive models.
        '''
    def __call__(self, *args, max_evals: Incomplete | None = None, silent: bool = False):
        """ Explains the output of model(*args), where args represents one or more parallel iterable args.
        """
    @staticmethod
    def supports_model_with_masker(model, masker):
        """ Determines if this explainer can handle the given model.

        This is an abstract static method meant to be implemented by each subclass.
        """
    def explain_row(self, *row_args, max_evals, main_effects, error_bounds, batch_size, outputs, silent):
        """ Explains a single row and returns the tuple (row_values, row_expected_values, row_mask_shapes).
        """
