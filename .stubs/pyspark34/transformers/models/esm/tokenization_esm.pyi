from ...tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from ...tokenization_utils_base import AddedToken as AddedToken
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import List, Optional

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete

def load_vocab_file(vocab_file): ...

class EsmTokenizer(PreTrainedTokenizer):
    """
    Constructs an ESM tokenizer.
    """
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    model_input_names: Incomplete
    all_tokens: Incomplete
    unk_token: str
    cls_token: str
    pad_token: str
    mask_token: str
    eos_token: str
    unique_no_split_tokens: Incomplete
    def __init__(self, vocab_file, **kwargs) -> None: ...
    def get_vocab_size(self, with_added_tokens: bool = False): ...
    def get_vocab(self): ...
    def token_to_id(self, token: str) -> int: ...
    def id_to_token(self, index: int) -> str: ...
    def build_inputs_with_special_tokens(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None) -> List[int]: ...
    def get_special_tokens_mask(self, token_ids_0: List, token_ids_1: Optional[List] = None, already_has_special_tokens: bool = False) -> List[int]:
        """
        Retrieves sequence ids from a token list that has no special tokens added. This method is called when adding
        special tokens using the tokenizer `prepare_for_model` or `encode_plus` methods.

        Args:
            token_ids_0 (`List[int]`):
                List of ids of the first sequence.
            token_ids_1 (`List[int]`, *optional*):
                List of ids of the second sequence.
            already_has_special_tokens (`bool`, *optional*, defaults to `False`):
                Whether or not the token list is already formatted with special tokens for the model.

        Returns:
            A list of integers in the range [0, 1]: 1 for a special token, 0 for a sequence token.
        """
    def save_vocabulary(self, save_directory, filename_prefix): ...
    @property
    def vocab_size(self) -> int: ...
