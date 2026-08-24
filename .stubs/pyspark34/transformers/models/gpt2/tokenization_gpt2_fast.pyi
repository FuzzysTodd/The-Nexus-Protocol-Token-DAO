from ...tokenization_utils_base import BatchEncoding as BatchEncoding
from ...tokenization_utils_fast import PreTrainedTokenizerFast as PreTrainedTokenizerFast
from ...utils import logging as logging
from .tokenization_gpt2 import GPT2Tokenizer as GPT2Tokenizer
from _typeshed import Incomplete
from transformers.pipelines.conversational import Conversation as Conversation
from typing import Optional, Tuple

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete

class GPT2TokenizerFast(PreTrainedTokenizerFast):
    '''
    Construct a "fast" GPT-2 tokenizer (backed by HuggingFace\'s *tokenizers* library). Based on byte-level
    Byte-Pair-Encoding.

    This tokenizer has been trained to treat spaces like parts of the tokens (a bit like sentencepiece) so a word will
    be encoded differently whether it is at the beginning of the sentence (without space) or not:

    ```
    >>> from transformers import GPT2TokenizerFast
    >>> tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    >>> tokenizer("Hello world")[\'input_ids\']
    [15496, 995]
    >>> tokenizer(" Hello world")[\'input_ids\']
    [18435, 995]
    ```

    You can get around that behavior by passing `add_prefix_space=True` when instantiating this tokenizer, but since
    the model was not pretrained this way, it might yield a decrease in performance.

    <Tip>

    When used with `is_split_into_words=True`, this tokenizer needs to be instantiated with `add_prefix_space=True`.

    </Tip>

    This tokenizer inherits from [`PreTrainedTokenizerFast`] which contains most of the main methods. Users should
    refer to this superclass for more information regarding those methods.

    Args:
        vocab_file (`str`):
            Path to the vocabulary file.
        merges_file (`str`):
            Path to the merges file.
        errors (`str`, *optional*, defaults to `"replace"`):
            Paradigm to follow when decoding bytes to UTF-8. See
            [bytes.decode](https://docs.python.org/3/library/stdtypes.html#bytes.decode) for more information.
        unk_token (`str`, *optional*, defaults to `<|endoftext|>`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        bos_token (`str`, *optional*, defaults to `<|endoftext|>`):
            The beginning of sequence token.
        eos_token (`str`, *optional*, defaults to `<|endoftext|>`):
            The end of sequence token.
        add_prefix_space (`bool`, *optional*, defaults to `False`):
            Whether or not to add an initial space to the input. This allows to treat the leading word just as any
            other word. (GPT2 tokenizer detect beginning of words by the preceding space).
        trim_offsets (`bool`, *optional*, defaults to `True`):
            Whether or not the post-processing step should trim offsets to avoid including whitespaces.
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    model_input_names: Incomplete
    slow_tokenizer_class = GPT2Tokenizer
    add_bos_token: Incomplete
    add_prefix_space: Incomplete
    def __init__(self, vocab_file: Incomplete | None = None, merges_file: Incomplete | None = None, tokenizer_file: Incomplete | None = None, unk_token: str = '<|endoftext|>', bos_token: str = '<|endoftext|>', eos_token: str = '<|endoftext|>', add_prefix_space: bool = False, **kwargs) -> None: ...
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
