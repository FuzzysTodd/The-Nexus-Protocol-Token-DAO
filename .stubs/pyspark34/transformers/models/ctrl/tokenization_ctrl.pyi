from ...tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Optional, Tuple

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete
CONTROL_CODES: Incomplete

def get_pairs(word):
    """
    Return set of symbol pairs in a word.

    Word is represented as tuple of symbols (symbols being variable-length strings).
    """

class CTRLTokenizer(PreTrainedTokenizer):
    '''
    Construct a CTRL tokenizer. Based on Byte-Pair-Encoding.

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains most of the main methods. Users should refer to
    this superclass for more information regarding those methods.

    Args:
        vocab_file (`str`):
            Path to the vocabulary file.
        merges_file (`str`):
            Path to the merges file.
        unk_token (`str`, *optional*, defaults to `"<unk>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    control_codes = CONTROL_CODES
    encoder: Incomplete
    decoder: Incomplete
    bpe_ranks: Incomplete
    cache: Incomplete
    def __init__(self, vocab_file, merges_file, unk_token: str = '<unk>', **kwargs) -> None: ...
    @property
    def vocab_size(self): ...
    def get_vocab(self): ...
    def bpe(self, token): ...
    def convert_tokens_to_string(self, tokens):
        """Converts a sequence of tokens (string) in a single string."""
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
