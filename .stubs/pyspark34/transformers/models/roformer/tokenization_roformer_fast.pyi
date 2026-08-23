from ...tokenization_utils_fast import PreTrainedTokenizerFast as PreTrainedTokenizerFast
from ...utils import logging as logging
from .tokenization_roformer import RoFormerTokenizer as RoFormerTokenizer
from .tokenization_utils import JiebaPreTokenizer as JiebaPreTokenizer
from _typeshed import Incomplete
from typing import List, Optional, Tuple

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete
PRETRAINED_INIT_CONFIGURATION: Incomplete

class RoFormerTokenizerFast(PreTrainedTokenizerFast):
    '''
    Construct a "fast" RoFormer tokenizer (backed by HuggingFace\'s *tokenizers* library).

    [`RoFormerTokenizerFast`] is almost identical to [`BertTokenizerFast`] and runs end-to-end tokenization:
    punctuation splitting and wordpiece. There are some difference between them when tokenizing Chinese.

    This tokenizer inherits from [`PreTrainedTokenizerFast`] which contains most of the main methods. Users should
    refer to this superclass for more information regarding those methods.

    Example:

    ```python
    >>> from transformers import RoFormerTokenizerFast

    >>> tokenizer = RoFormerTokenizerFast.from_pretrained("junnyu/roformer_chinese_base")
    >>> tokenizer.tokenize("今天天气非常好。")
    # [\'今\', \'天\', \'天\', \'气\', \'非常\', \'好\', \'。\']
    ```'''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    pretrained_init_configuration = PRETRAINED_INIT_CONFIGURATION
    slow_tokenizer_class = RoFormerTokenizer
    do_lower_case: Incomplete
    def __init__(self, vocab_file: Incomplete | None = None, tokenizer_file: Incomplete | None = None, do_lower_case: bool = True, unk_token: str = '[UNK]', sep_token: str = '[SEP]', pad_token: str = '[PAD]', cls_token: str = '[CLS]', mask_token: str = '[MASK]', tokenize_chinese_chars: bool = True, strip_accents: Incomplete | None = None, **kwargs) -> None: ...
    def build_inputs_with_special_tokens(self, token_ids_0, token_ids_1: Incomplete | None = None):
        """
        Build model inputs from a sequence or a pair of sequence for sequence classification tasks by concatenating and
        adding special tokens. A RoFormer sequence has the following format:

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
    def create_token_type_ids_from_sequences(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None) -> List[int]:
        """
        Create a mask from the two sequences passed to be used in a sequence-pair classification task. A RoFormer
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
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
    def save_pretrained(self, save_directory, legacy_format: Incomplete | None = None, filename_prefix: Incomplete | None = None, push_to_hub: bool = False, **kwargs): ...
