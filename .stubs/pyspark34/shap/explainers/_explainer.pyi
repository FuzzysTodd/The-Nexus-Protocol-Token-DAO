from .. import explainers as explainers, links as links, maskers as maskers, models as models
from .._explanation import Explanation as Explanation
from .._serializable import Deserializer as Deserializer, Serializable as Serializable, Serializer as Serializer
from ..maskers import Masker as Masker
from ..models import Model as Model
from ..utils import safe_isinstance as safe_isinstance, show_progress as show_progress
from ..utils._exceptions import InvalidAlgorithmError as InvalidAlgorithmError
from ..utils.transformers import is_transformers_lm as is_transformers_lm
from _typeshed import Incomplete

class Explainer(Serializable):
    """ Uses Shapley values to explain any machine learning model or python function.

    This is the primary explainer interface for the SHAP library. It takes any combination
    of a model and masker and returns a callable subclass object that implements
    the particular estimation algorithm that was chosen.
    """
    model: Incomplete
    output_names: Incomplete
    feature_names: Incomplete
    masker: Incomplete
    link: Incomplete
    linearize_link: Incomplete
    __class__: Incomplete
    def __init__(self, model, masker: Incomplete | None = None, link=..., algorithm: str = 'auto', output_names: Incomplete | None = None, feature_names: Incomplete | None = None, linearize_link: bool = True, seed: Incomplete | None = None, **kwargs) -> None:
        ''' Build a new explainer for the passed model.

        Parameters
        ----------
        model : object or function
            User supplied function or model object that takes a dataset of samples and
            computes the output of the model for those samples.

        masker : function, numpy.array, pandas.DataFrame, tokenizer, None, or a list of these for each model input
            The function used to "mask" out hidden features of the form `masked_args = masker(*model_args, mask=mask)`.
            It takes input in the same form as the model, but for just a single sample with a binary
            mask, then returns an iterable of masked samples. These
            masked samples will then be evaluated using the model function and the outputs averaged.
            As a shortcut for the standard masking using by SHAP you can pass a background data matrix
            instead of a function and that matrix will be used for masking. Domain specific masking
            functions are available in shap such as shap.ImageMasker for images and shap.TokenMasker
            for text. In addition to determining how to replace hidden features, the masker can also
            constrain the rules of the cooperative game used to explain the model. For example
            shap.TabularMasker(data, hclustering="correlation") will enforce a hierarchical clustering
            of coalitions for the game (in this special case the attributions are known as the Owen values).

        link : function
            The link function used to map between the output units of the model and the SHAP value units. By
            default it is shap.links.identity, but shap.links.logit can be useful so that expectations are
            computed in probability units while explanations remain in the (more naturally additive) log-odds
            units. For more details on how link functions work see any overview of link functions for generalized
            linear models.

        algorithm : "auto", "permutation", "partition", "tree", or "linear"
            The algorithm used to estimate the Shapley values. There are many different algorithms that
            can be used to estimate the Shapley values (and the related value for constrained games), each
            of these algorithms have various tradeoffs and are preferable in different situations. By
            default the "auto" options attempts to make the best choice given the passed model and masker,
            but this choice can always be overridden by passing the name of a specific algorithm. The type of
            algorithm used will determine what type of subclass object is returned by this constructor, and
            you can also build those subclasses directly if you prefer or need more fine grained control over
            their options.

        output_names : None or list of strings
            The names of the model outputs. For example if the model is an image classifier, then output_names would
            be the names of all the output classes. This parameter is optional. When output_names is None then
            the Explanation objects produced by this explainer will not have any output_names, which could effect
            downstream plots.

        seed: None or int
            seed for reproducibility

        '''
    def __call__(self, *args, max_evals: str = 'auto', main_effects: bool = False, error_bounds: bool = False, batch_size: str = 'auto', outputs: Incomplete | None = None, silent: bool = False, **kwargs):
        """ Explains the output of model(*args), where args is a list of parallel iteratable datasets.

        Note this default version could be an abstract method that is implemented by each algorithm-specific
        subclass of Explainer. Descriptions of each subclasses' __call__ arguments
        are available in their respective doc-strings.
        """
    def explain_row(self, *row_args, max_evals, main_effects, error_bounds, outputs, silent, **kwargs):
        """ Explains a single row and returns the tuple (row_values, row_expected_values, row_mask_shapes, main_effects).

        This is an abstract method meant to be implemented by each subclass.

        Returns
        -------
        tuple
            A tuple of (row_values, row_expected_values, row_mask_shapes), where row_values is an array of the
            attribution values for each sample, row_expected_values is an array (or single value) representing
            the expected value of the model for each sample (which is the same for all samples unless there
            are fixed inputs present, like labels when explaining the loss), and row_mask_shapes is a list
            of all the input shapes (since the row_values is always flattened),
        """
    @staticmethod
    def supports_model_with_masker(model, masker):
        """ Determines if this explainer can handle the given model.

        This is an abstract static method meant to be implemented by each subclass.
        """
    def save(self, out_file, model_saver: str = '.save', masker_saver: str = '.save') -> None:
        """ Write the explainer to the given file stream.
        """
    @classmethod
    def load(cls, in_file, model_loader=..., masker_loader=..., instantiate: bool = True):
        """ Load an Explainer from the given file stream.

        Parameters
        ----------
        in_file : The file stream to load objects from.
        """

def pack_values(values):
    """ Used the clean up arrays before putting them into an Explanation object.
    """
