from ...tokenization_utils import AddedToken as AddedToken, PreTrainedTokenizer as PreTrainedTokenizer
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Dict, List, Optional

logger: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete
UNICODE_VOCAB_SIZE: int
PAD: int
CLS: int
SEP: int
BOS: int
MASK: int
RESERVED: int
SPECIAL_CODEPOINTS: Dict[int, str]
SPECIAL_CODEPOINTS_BY_NAME: Dict[str, int]

class CanineTokenizer(PreTrainedTokenizer):
    """
    Construct a CANINE tokenizer (i.e. a character splitter). It turns text into a sequence of characters, and then
    converts each character into its Unicode code point.

    [`CanineTokenizer`] inherits from [`PreTrainedTokenizer`].

    Refer to superclass [`PreTrainedTokenizer`] for usage examples and documentation concerning parameters.

    Args:
        model_max_length (`int`, *optional*, defaults to 2048):
                The maximum sentence length the model accepts.
    """
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    def __init__(self, bos_token=..., eos_token=..., sep_token=..., cls_token=..., pad_token=..., mask_token=..., add_prefix_space: bool = False, model_max_length: int = 2048, **kwargs) -> None: ...
    @property
    def vocab_size(self) -> int: ...
    def convert_tokens_to_string(self, tokens): ...
    def build_inputs_with_special_tokens(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None) -> List[int]:
        """
        Build model inputs from a sequence or a pair of sequence for sequence classification tasks by concatenating and
        adding special tokens. A CANINE sequence has the following format:

        - single sequence: `[CLS] X [SEP]`
        - pair of sequences: `[CLS] A [SEP] B [SEP]`

        Args:
            token_ids_0 (`List[int]`):
                List of IDs to which the special tokens will be added.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.

        Returns:
            `List[int]`: List of [input IDs](../glossary#input-ids) with the appropriate special tokens.
        """
    def get_special_tokens_mask(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None, already_has_special_tokens: bool = False) -> List[int]:
        """
        Retrieve sequence ids from a token list that has no special tokens added. This method is called when adding
        special tokens using the tokenizer `prepare_for_model` method.

        Args:
            token_ids_0 (`List[int]`):
                List of IDs.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.
            already_has_special_tokens (`bool`, *optional*, defaults to `False`):
                Whether or not the token list is already formatted with special tokens for the model.

        Returns:
            `List[int]`: A list of integers in the range [0, 1]: 1 for a special token, 0 for a sequence token.
        """
    def create_token_type_ids_from_sequences(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None) -> List[int]:
        """
        Create a mask from the two sequences passed to be used in a sequence-pair classification task. A CANINE
        sequence pair mask has the following format:

        ```
        0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1
        | first sequence    | second sequence |
        ```

        If `token_ids_1` is `None`, this method only returns the first portion of the mask (0s).

        Args:
            token_ids_0 (`List[int]`):
                List of IDs.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.

        Returns:
            `List[int]`: List of [token type IDs](../glossary#token-type-ids) according to the given sequence(s).
        """
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None): ...
