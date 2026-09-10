from ...tokenization_utils_fast import PreTrainedTokenizerFast as PreTrainedTokenizerFast
from ...utils import is_sentencepiece_available as is_sentencepiece_available, logging as logging
from .tokenization_t5 import T5Tokenizer as T5Tokenizer
from _typeshed import Incomplete
from typing import List, Optional, Tuple

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete

class T5TokenizerFast(PreTrainedTokenizerFast):
    '''
    Construct a "fast" T5 tokenizer (backed by HuggingFace\'s *tokenizers* library). Based on
    [Unigram](https://huggingface.co/docs/tokenizers/python/latest/components.html?highlight=unigram#models).

    This tokenizer inherits from [`PreTrainedTokenizerFast`] which contains most of the main methods. Users should
    refer to this superclass for more information regarding those methods.

    Args:
        vocab_file (`str`):
            [SentencePiece](https://github.com/google/sentencepiece) file (generally has a *.spm* extension) that
            contains the vocabulary necessary to instantiate a tokenizer.
        eos_token (`str`, *optional*, defaults to `"</s>"`):
            The end of sequence token.

            <Tip>

            When building a sequence using special tokens, this is not the token that is used for the end of sequence.
            The token used is the `sep_token`.

            </Tip>

        unk_token (`str`, *optional*, defaults to `"<unk>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        pad_token (`str`, *optional*, defaults to `"<pad>"`):
            The token used for padding, for example when batching sequences of different lengths.
        extra_ids (`int`, *optional*, defaults to 100):
            Add a number of extra ids added to the vocabulary for use as sentinels. These tokens are accessible as
            "<extra_id_{%d}>" where "{%d}" is a number between 0 and extra_ids-1. These tokens can be retrieved by
            calling get_sentinel_tokens method and token ids can be by calling get_sentinel_token_ids method
        additional_special_tokens (`List[str]`, *optional*):
            Additional special tokens used by the tokenizer.
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    model_input_names: Incomplete
    slow_tokenizer_class = T5Tokenizer
    prefix_tokens: List[int]
    vocab_file: Incomplete
    can_save_slow_tokenizer: Incomplete
    def __init__(self, vocab_file: Incomplete | None = None, tokenizer_file: Incomplete | None = None, eos_token: str = '</s>', unk_token: str = '<unk>', pad_token: str = '<pad>', extra_ids: int = 100, additional_special_tokens: Incomplete | None = None, **kwargs) -> None: ...
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
    def build_inputs_with_special_tokens(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None) -> List[int]:
        """
        Build model inputs from a sequence or a pair of sequence for sequence classification tasks by concatenating and
        adding special tokens. A sequence has the following format:

        - single sequence: `X </s>`
        - pair of sequences: `A </s> B </s>`

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
        Create a mask from the two sequences passed to be used in a sequence-pair classification task. T5 does not make
        use of token type ids, therefore a list of zeros is returned.

        Args:
            token_ids_0 (`List[int]`):
                List of IDs.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.

        Returns:
            `List[int]`: List of zeros.
        """
    def get_sentinel_tokens(self): ...
    def get_sentinel_token_ids(self): ...
