import numpy as np
import tensorflow as tf
import torch
from ...tokenization_utils import AddedToken as AddedToken, PreTrainedTokenizer as PreTrainedTokenizer
from ...utils import is_tf_available as is_tf_available, is_torch_available as is_torch_available, logging as logging
from _typeshed import Incomplete
from typing import List, Optional, Tuple, Union

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete

def bytes_to_unicode():
    """
    Returns list of utf-8 byte and a mapping to unicode strings. We specifically avoids mapping to whitespace/control
    characters the bpe code barfs on.

    The reversible bpe codes work on unicode strings. This means you need a large # of unicode characters in your vocab
    if you want to avoid UNKs. When you're at something like a 10B token dataset you end up needing around 5K for
    decent coverage. This is a significant percentage of your normal, say, 32K bpe vocab. To avoid that, we want lookup
    tables between utf-8 bytes and unicode strings.
    """
def get_pairs(word):
    """
    Return set of symbol pairs in a word.

    Word is represented as tuple of symbols (symbols being variable-length strings).
    """

class CodeGenTokenizer(PreTrainedTokenizer):
    '''
    Construct a CodeGen tokenizer. Based on byte-level Byte-Pair-Encoding.

    This tokenizer has been trained to treat spaces like parts of the tokens (a bit like sentencepiece) so a word will
    be encoded differently whether it is at the beginning of the sentence (without space) or not:

    ```
    >>> from transformers import CodeGenTokenizer
    >>> tokenizer = CodeGenTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
    >>> tokenizer("Hello world")[\'input_ids\']
    [15496, 995]
    >>> tokenizer(" Hello world")[\'input_ids\']
    [18435, 995]
    ```

    You can get around that behavior by passing `add_prefix_space=True` when instantiating this tokenizer or when you
    call it on some text, but since the model was not pretrained this way, it might yield a decrease in performance.

    <Tip>

    When used with `is_split_into_words=True`, this tokenizer will add a space before each word (even the first one).

    </Tip>

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains most of the main methods. Users should refer to
    this superclass for more information regarding those methods.

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
            other word. (CodeGen tokenizer detect beginning of words by the preceding space).
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    model_input_names: Incomplete
    add_bos_token: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    errors: Incomplete
    byte_encoder: Incomplete
    byte_decoder: Incomplete
    bpe_ranks: Incomplete
    cache: Incomplete
    add_prefix_space: Incomplete
    pat: Incomplete
    def __init__(self, vocab_file, merges_file, errors: str = 'replace', unk_token: str = '<|endoftext|>', bos_token: str = '<|endoftext|>', eos_token: str = '<|endoftext|>', pad_token: Incomplete | None = None, add_prefix_space: bool = False, add_bos_token: bool = False, **kwargs) -> None: ...
    @property
    def vocab_size(self): ...
    def get_vocab(self): ...
    def bpe(self, token): ...
    def build_inputs_with_special_tokens(self, token_ids_0, token_ids_1: Incomplete | None = None): ...
    def convert_tokens_to_string(self, tokens):
        """Converts a sequence of tokens (string) in a single string."""
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
    def prepare_for_tokenization(self, text, is_split_into_words: bool = False, **kwargs): ...
    def decode(self, token_ids: Union[int, List[int], 'np.ndarray', 'torch.Tensor', 'tf.Tensor'], skip_special_tokens: bool = False, clean_up_tokenization_spaces: bool = True, truncate_before_pattern: Optional[List[str]] = None, **kwargs) -> str:
        '''
        Converts a sequence of ids in a string, using the tokenizer and vocabulary with options to remove special
        tokens and clean up tokenization spaces.

        Similar to doing `self.convert_tokens_to_string(self.convert_ids_to_tokens(token_ids))`.

        Args:
            token_ids (`Union[int, List[int], np.ndarray, torch.Tensor, tf.Tensor]`):
                List of tokenized input ids. Can be obtained using the `__call__` method.
            skip_special_tokens (`bool`, *optional*, defaults to `False`):
                Whether or not to remove special tokens in the decoding.
            clean_up_tokenization_spaces (`bool`, *optional*, defaults to `True`):
                Whether or not to clean up the tokenization spaces.
            truncate_before_pattern (`List[str]`, *optional*, defaults to `None`):
                A list of regular expression strings that will be used to truncate the returned string. This can be
                used to remove extra pieces of code (e.g. truncate if observing a comment symbol "#" at the beginning
                of a new line). An example pattern could be `["^#", re.escape("<|endoftext|>"), "^\'\'\'", "


"]`.
            kwargs (additional keyword arguments, *optional*):
                Will be passed to the underlying model specific decode method.

        Returns:
            `str`: The decoded sentence.
        '''
    def truncate(self, completion, truncate_before_pattern): ...
