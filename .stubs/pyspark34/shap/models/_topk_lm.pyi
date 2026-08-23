from .._serializable import Deserializer as Deserializer, Serializer as Serializer
from ..utils import safe_isinstance as safe_isinstance
from ..utils.transformers import MODELS_FOR_CAUSAL_LM as MODELS_FOR_CAUSAL_LM, getattr_silent as getattr_silent
from ._model import Model as Model
from _typeshed import Incomplete

class TopKLM(Model):
    """ Generates scores (log odds) for the top-k tokens for Causal/Masked LM.
    """
    tokenizer: Incomplete
    k: Incomplete
    batch_size: Incomplete
    device: Incomplete
    X: Incomplete
    topk_token_ids: Incomplete
    output_names: Incomplete
    model_type: Incomplete
    inner_model: Incomplete
    def __init__(self, model, tokenizer, k: int = 10, generate_topk_token_ids: Incomplete | None = None, batch_size: int = 128, device: Incomplete | None = None) -> None:
        """ Take Causal/Masked LM model and tokenizer and build a log odds output model for the top-k tokens.

        Parameters
        ----------
        model: object or function
            A object of any pretrained transformer model which is to be explained.

        tokenizer: object
            A tokenizer object(PreTrainedTokenizer/PreTrainedTokenizerFast).

        generation_function_for_topk_token_ids: function
            A function which is used to generate top-k token ids. Log odds will be generated for these custom token ids.

        batch_size: int
            Batch size for model inferencing and computing logodds (default=128).

        device: str
            By default, it infers if system has a gpu and accordingly sets device. Should be 'cpu' or 'cuda' or pytorch models.

        Returns
        -------
        numpy.ndarray
            The scores (log odds) of generating top-k token ids using the model.
        """
    def __call__(self, masked_X, X):
        """ Computes log odds scores for a given batch of masked inputs for the top-k tokens for Causal/Masked LM.

        Parameters
        ----------
        masked_X: numpy.ndarray
            An array containing a list of masked inputs.

        X: numpy.ndarray
            An array containing a list of original inputs

        Returns
        -------
        numpy.ndarray
            A numpy array of log odds scores for top-k tokens for every input pair (masked_X, X)
        """
    def update_cache_X(self, X) -> None:
        """ The function updates original input(X) and top-k token ids for the Causal/Masked LM.

        It mimics the caching mechanism to update the original input and topk token ids
        that are to be explained and which updates for every new row of explanation.

        Parameters
        ----------
        X: np.ndarray
            Input(Text) for an explanation row.
        """
    def get_output_names_and_update_topk_token_ids(self, X):
        """ Gets the token names for top-k token ids for Causal/Masked LM.

        Parameters
        ----------
        X: np.ndarray
            Input(Text) for an explanation row.

        Returns
        -------
        list
            A list of output tokens.
        """
    def get_logodds(self, logits):
        """ Calculates log odds from logits.

        This function passes the logits through softmax and then computes log odds for the top-k token ids.

        Parameters
        ----------
        logits: numpy.ndarray
            An array of logits generated from the model.

        Returns
        -------
        numpy.ndarray
            Computes log odds for corresponding top-k token ids.
        """
    def get_inputs(self, X, padding_side: str = 'right'):
        ''' The function tokenizes source sentence.

        Parameters
        ----------
        X: numpy.ndarray
            X is a batch of text.

        Returns
        -------
        dict
            Dictionary of padded source sentence ids and attention mask as tensors("pt" or "tf" based on similarity_model_type).
        '''
    def generate_topk_token_ids(self, X):
        """ Generates top-k token ids for Causal/Masked LM.

        Parameters
        ----------
        X: numpy.ndarray
            X is the original input sentence for an explanation row.

        Returns
        -------
        np.ndarray
            An array of top-k token ids.
        """
    def get_lm_logits(self, X):
        """ Evaluates a Causal/Masked LM model and returns logits corresponding to next word/masked word.

        Parameters
        ----------
        X: numpy.ndarray
            An array containing a list of masked inputs.

        Returns
        -------
        numpy.ndarray
            Logits corresponding to next word/masked word.
        """
    def save(self, out_file) -> None: ...
    @classmethod
    def load(cls, in_file, instantiate: bool = True): ...
