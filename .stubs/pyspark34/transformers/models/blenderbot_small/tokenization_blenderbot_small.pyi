from ...tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Dict, List, Optional, Tuple

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete

def get_pairs(word):
    """
    Return set of symbol pairs in a word.

    Word is represented as tuple of symbols (symbols being variable-length strings).
    """

class BlenderbotSmallTokenizer(PreTrainedTokenizer):
    '''
    Constructs a Blenderbot-90M tokenizer based on BPE (Byte-Pair-Encoding)

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains most of the main methods. Users should refer to
    the superclass for more information regarding methods.

    Args:
        vocab_file (`str`):
            File containing the vocabulary.
        merges_file (`str`):
            Path to the merges file.
        bos_token (`str`, *optional*, defaults to `"__start__"`):
            The beginning of sentence token.
        eos_token (`str`, *optional*, defaults to `"__end__"`):
            The end of sentence token.
        unk_token (`str`, *optional*, defaults to `"__unk__"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        pad_token (`str`, *optional*, defaults to `"__pad__"`):
            The token used for padding, for example when batching sequences of different lengths.
        **kwargs
            Additional keyword arguments passed along to [`PreTrainedTokenizer`]
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    model_input_names: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    bpe_ranks: Incomplete
    cache: Incomplete
    def __init__(self, vocab_file, merges_file, bos_token: str = '__start__', eos_token: str = '__end__', unk_token: str = '__unk__', pad_token: str = '__null__', **kwargs) -> None: ...
    @property
    def vocab_size(self) -> int: ...
    def get_vocab(self) -> Dict: ...
    def bpe(self, token: str) -> str: ...
    def convert_tokens_to_string(self, tokens: List[str]) -> str:
        """Converts a sequence of tokens in a single string."""
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
