from .._serializable import Deserializer as Deserializer, Serializer as Serializer
from ..utils import safe_isinstance as safe_isinstance
from ._model import Model as Model
from _typeshed import Incomplete

class TextGeneration(Model):
    """ Generates target sentence/ids using a base model.

    It generates target sentence/ids for a model (a pretrained transformer model or a function).
    """
    explanation_row: int
    inner_model: Incomplete
    tokenizer: Incomplete
    device: Incomplete
    model_agnostic: bool
    model_type: str
    X: Incomplete
    target_X: Incomplete
    def __init__(self, model: Incomplete | None = None, tokenizer: Incomplete | None = None, target_sentences: Incomplete | None = None, device: Incomplete | None = None) -> None:
        """ Create a text generator model from a pretrained transformer model or a function.

        For a pretrained transformer model, a tokenizer should be passed.

        Parameters
        ----------
        model: object or function
            A object of any pretrained transformer model or function for which target sentence/ids are to be generated.

        tokenizer: object
            A tokenizer object(PreTrainedTokenizer/PreTrainedTokenizerFast) which is used to tokenize sentence.

        target_sentences: list
            A target sentence for every explanation row.

        device: str
            By default, it infers if system has a gpu and accordingly sets device. Should be 'cpu' or 'cuda' or pytorch models.

        Returns
        -------
        numpy.ndarray
            Array of target sentence/ids.
        """
    def __call__(self, X):
        """ Generates target sentence/ids from X.

        Parameters
        ----------
        X: str or numpy.ndarray
            Input in the form of text or image.

        Returns
        -------
        numpy.ndarray
            Array of target sentence/ids.
        """
    def get_inputs(self, X, padding_side: str = 'right'):
        ''' The function tokenizes source sentences.

        In model agnostic case, the function calls model(X) which is expected to
        return a batch of output sentences which is tokenized to compute inputs.

        Parameters
        ----------
        X: numpy.ndarray
            X is a batch of sentences.

        Returns
        -------
        dict
            Dictionary of padded source sentence ids and attention mask as tensors("pt" or "tf" based on model_type).
        '''
    def model_generate(self, X):
        """ This function performs text generation for tensorflow and pytorch models.

        Parameters
        ----------
        X: dict
            Dictionary of padded source sentence ids and attention mask as tensors.

        Returns
        -------
        numpy.ndarray
            Returns target sentence ids.
        """
    def parse_prefix_suffix_for_model_generate_output(self, output):
        """ Calculates if special tokens are present in the begining/end of the model generated output.

        Parameters
        ----------
        output: list
            A list of output token ids.

        Returns
        -------
        dict
            Dictionary of prefix and suffix lengths concerning special tokens in output ids.
        """
    def save(self, out_file) -> None: ...
    @classmethod
    def load(cls, in_file, instantiate: bool = True): ...
