from ...tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Dict, List, Optional, Tuple

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
BPE_TOKEN_MERGES: str
BPE_TOKEN_VOCAB: str

def get_pairs(word):
    """
    Return set of symbol pairs in a word. word is represented as tuple of symbols (symbols being variable-length
    strings)
    """

PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete

class Speech2Text2Tokenizer(PreTrainedTokenizer):
    '''
    Constructs a Speech2Text2Tokenizer.

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains some of the main methods. Users should refer to
    the superclass for more information regarding such methods.

    Args:
        vocab_file (`str`):
            File containing the vocabulary.
        bos_token (`str`, *optional*, defaults to `"<s>"`):
            The beginning of sentence token.
        eos_token (`str`, *optional*, defaults to `"</s>"`):
            The end of sentence token.
        unk_token (`str`, *optional*, defaults to `"<unk>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        pad_token (`str`, *optional*, defaults to `"<pad>"`):
            The token used for padding, for example when batching sequences of different lengths.

        **kwargs
            Additional keyword arguments passed along to [`PreTrainedTokenizer`]
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    model_input_names: Incomplete
    do_lower_case: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    bpe_ranks: Incomplete
    cache: Incomplete
    def __init__(self, vocab_file, bos_token: str = '<s>', pad_token: str = '<pad>', eos_token: str = '</s>', unk_token: str = '<unk>', do_lower_case: bool = False, merges_file: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def vocab_size(self) -> int: ...
    def get_vocab(self) -> Dict: ...
    def bpe(self, token): ...
    def convert_tokens_to_string(self, tokens: List[str]) -> str:
        """
        Converts a list of output tokens into a single string.
        """
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
