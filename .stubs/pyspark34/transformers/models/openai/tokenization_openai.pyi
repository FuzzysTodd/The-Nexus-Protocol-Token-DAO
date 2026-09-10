from ...tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Optional, Tuple

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete

def whitespace_tokenize(text):
    """Runs basic whitespace cleaning and splitting on a piece of text."""

class BasicTokenizer:
    """
    Constructs a BasicTokenizer that will run basic tokenization (punctuation splitting, lower casing, etc.).

    Args:
        do_lower_case (`bool`, *optional*, defaults to `True`):
            Whether or not to lowercase the input when tokenizing.
        never_split (`Iterable`, *optional*):
            Collection of tokens which will never be split during tokenization. Only has an effect when
            `do_basic_tokenize=True`
        tokenize_chinese_chars (`bool`, *optional*, defaults to `True`):
            Whether or not to tokenize Chinese characters.

            This should likely be deactivated for Japanese (see this
            [issue](https://github.com/huggingface/transformers/issues/328)).
        strip_accents (`bool`, *optional*):
            Whether or not to strip all accents. If this option is not specified, then it will be determined by the
            value for `lowercase` (as in the original BERT).
    """
    do_lower_case: Incomplete
    never_split: Incomplete
    tokenize_chinese_chars: Incomplete
    strip_accents: Incomplete
    def __init__(self, do_lower_case: bool = True, never_split: Incomplete | None = None, tokenize_chinese_chars: bool = True, strip_accents: Incomplete | None = None) -> None: ...
    def tokenize(self, text, never_split: Incomplete | None = None):
        '''
        Basic Tokenization of a piece of text. Split on "white spaces" only, for sub-word tokenization, see
        WordPieceTokenizer.

        Args:
            never_split (`List[str]`, *optional*)
                Kept for backward compatibility purposes. Now implemented directly at the base class level (see
                [`PreTrainedTokenizer.tokenize`]) List of token not to split.
        '''

def get_pairs(word):
    """
    Return set of symbol pairs in a word. word is represented as tuple of symbols (symbols being variable-length
    strings)
    """
def text_standardize(text):
    """
    fixes some issues the spacy tokenizer had on books corpus also does some whitespace standardization
    """

class OpenAIGPTTokenizer(PreTrainedTokenizer):
    '''
    Construct a GPT Tokenizer. Based on Byte-Pair-Encoding with the following peculiarities:

    - lowercases all inputs,
    - uses `SpaCy` tokenizer and `ftfy` for pre-BPE tokenization if they are installed, fallback to BERT\'s
      `BasicTokenizer` if not.

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
    model_input_names: Incomplete
    nlp: Incomplete
    fix_text: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    bpe_ranks: Incomplete
    cache: Incomplete
    def __init__(self, vocab_file, merges_file, unk_token: str = '<unk>', **kwargs) -> None: ...
    @property
    def do_lower_case(self): ...
    @property
    def vocab_size(self): ...
    def get_vocab(self): ...
    def bpe(self, token): ...
    def convert_tokens_to_string(self, tokens):
        """Converts a sequence of tokens (string) in a single string."""
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
