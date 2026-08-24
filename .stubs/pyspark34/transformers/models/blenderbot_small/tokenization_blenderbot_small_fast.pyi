from ...tokenization_utils_fast import PreTrainedTokenizerFast as PreTrainedTokenizerFast
from ...utils import logging as logging
from .tokenization_blenderbot_small import BlenderbotSmallTokenizer as BlenderbotSmallTokenizer
from _typeshed import Incomplete
from typing import List, Optional

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete

class BlenderbotSmallTokenizerFast(PreTrainedTokenizerFast):
    '''
    Construct a "fast" BlenderbotSmall tokenizer (backed by HuggingFace\'s *tokenizers* library).

    Args:
        vocab_file (`str`):
            Path to the vocabulary file.
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    slow_tokenizer_class = BlenderbotSmallTokenizer
    add_prefix_space: Incomplete
    def __init__(self, vocab_file: Incomplete | None = None, merges_file: Incomplete | None = None, unk_token: str = '<|endoftext|>', bos_token: str = '<|endoftext|>', eos_token: str = '<|endoftext|>', add_prefix_space: bool = False, trim_offsets: bool = True, **kwargs) -> None: ...
    def build_inputs_with_special_tokens(self, token_ids_0, token_ids_1: Incomplete | None = None): ...
    def create_token_type_ids_from_sequences(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None) -> List[int]:
        """
        Create a mask from the two sequences passed to be used in a sequence-pair classification task. BlenderbotSmall
        does not make use of token type ids, therefore a list of zeros is returned.

        Args:
            token_ids_0 (`List[int]`):
                List of IDs.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.

        Returns:
            `List[int]`: List of zeros.
        """
