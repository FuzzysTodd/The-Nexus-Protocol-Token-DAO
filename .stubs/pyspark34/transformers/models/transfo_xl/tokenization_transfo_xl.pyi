from ...tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from ...utils import cached_file as cached_file, is_sacremoses_available as is_sacremoses_available, is_torch_available as is_torch_available, logging as logging, requires_backends as requires_backends, torch_only_method as torch_only_method
from _typeshed import Incomplete
from collections.abc import Generator
from typing import List, Optional, Tuple

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete
PRETRAINED_CORPUS_ARCHIVE_MAP: Incomplete
CORPUS_NAME: str
MATCH_NUMBERS: Incomplete
DETOKENIZE_NUMBERS: Incomplete

def tokenize_numbers(text_array: List[str]) -> List[str]:
    '''
    Splits large comma-separated numbers and floating point values. This is done by replacing commas with \' @,@ \' and
    dots with \' @.@ \'.

    Args:
        text_array: An already tokenized text as list.

    Returns:
        A list of strings with tokenized numbers.

    Example:

    ```python
    >>> tokenize_numbers(["$", "5,000", "1.73", "m"])
    ["$", "5", "@,@", "000", "1", "@.@", "73", "m"]
    ```'''
def detokenize_numbers(text: str) -> str:
    '''
    Inverts the operation of *tokenize_numbers*. This is replacing \' @,@ \' and \' @.@\' by \',\' and \'.\'.

    Args:
        text: A string where the number should be detokenized.

    Returns:
        A detokenized string.

    Example:

    ```python
    >>> detokenize_numbers("$ 5 @,@ 000 1 @.@ 73 m")
    "$ 5,000 1.73 m"
    ```'''

class TransfoXLTokenizer(PreTrainedTokenizer):
    '''
    Construct a Transformer-XL tokenizer adapted from Vocab class in [the original
    code](https://github.com/kimiyoung/transformer-xl). The Transformer-XL tokenizer is a word-level tokenizer (no
    sub-word tokenization).

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains most of the main methods. Users should refer to
    this superclass for more information regarding those methods.

    Args:
        special (`List[str]`, *optional*):
            A list of special tokens (to be treated by the original implementation of this tokenizer).
        min_freq (`int`, *optional*, defaults to 0):
            The minimum number of times a token has to be present in order to be kept in the vocabulary (otherwise it
            will be mapped to `unk_token`).
        max_size (`int`, *optional*):
            The maximum size of the vocabulary. If left unset, it will default to the size of the vocabulary found
            after excluding the tokens according to the `min_freq` rule.
        lower_case (`bool`, *optional*, defaults to `False`):
            Whether or not to lowercase the input when tokenizing.
        delimiter (`str`, *optional*):
            The delimiter used between tokens.
        vocab_file (`str`, *optional*):
            File containing the vocabulary (from the original implementation).
        pretrained_vocab_file (`str`, *optional*):
            File containing the vocabulary as saved with the `save_pretrained()` method.
        never_split (`List[str]`, *optional*):
            List of tokens that should never be split. If no list is specified, will simply use the existing special
            tokens.
        unk_token (`str`, *optional*, defaults to `"<unk>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        eos_token (`str`, *optional*, defaults to `"<eos>"`):
            The end of sequence token.
        additional_special_tokens (`List[str]`, *optional*, defaults to `["<formula>"]`):
            A list of additional special tokens (for the HuggingFace functionality).
        language (`str`, *optional*, defaults to `"en"`):
            The language of this tokenizer (used for mose preprocessing).
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    model_input_names: Incomplete
    counter: Incomplete
    special: Incomplete
    min_freq: Incomplete
    max_size: Incomplete
    lower_case: Incomplete
    delimiter: Incomplete
    vocab_file: Incomplete
    never_split: Incomplete
    punctuation_symbols: str
    punction_without_space_before_pattern: Incomplete
    punctuation_with_space_around_pattern: Incomplete
    language: Incomplete
    moses_punct_normalizer: Incomplete
    moses_tokenizer: Incomplete
    moses_detokenizer: Incomplete
    def __init__(self, special: Incomplete | None = None, min_freq: int = 0, max_size: Incomplete | None = None, lower_case: bool = False, delimiter: Incomplete | None = None, vocab_file: Incomplete | None = None, pretrained_vocab_file: str = None, never_split: Incomplete | None = None, unk_token: str = '<unk>', eos_token: str = '<eos>', additional_special_tokens=['<formula>'], language: str = 'en', **kwargs) -> None: ...
    @property
    def do_lower_case(self): ...
    def count_file(self, path, verbose: bool = False, add_eos: bool = False): ...
    def count_sents(self, sents, verbose: bool = False) -> None:
        """
        sents : a list of sentences, each a list of tokenized symbols
        """
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
    idx2sym: Incomplete
    sym2idx: Incomplete
    def build_vocab(self) -> None: ...
    def encode_file(self, path, ordered: bool = False, verbose: bool = False, add_eos: bool = True, add_double_eos: bool = False): ...
    def encode_sents(self, sents, ordered: bool = False, verbose: bool = False): ...
    def add_special(self, sym) -> None: ...
    def add_symbol(self, sym) -> None: ...
    def move_added_token(self, token: str, target_idx: int):
        """
        Moves an added token to a specific position in the vocab. This method should be used when resizing an embedding
        layer other than the last one in the `AdaptiveEmbedding` in order to move the token in the tokenizer from the
        default position (at the very end) to the desired one.

        Args:
            token: The token to move to a specific position in the vocab.
            target_idx: The position where the token should be moved to.
        """
    def moses_punct_norm(self, text): ...
    def moses_tokenize(self, text): ...
    def moses_pipeline(self, text: str) -> List[str]:
        '''
        Does basic tokenization using [`sacremoses.MosesPunctNormalizer`] and [`sacremoses.MosesTokenizer`] with
        *aggressive_dash_splits=True* (see [`sacremoses.tokenize.MosesTokenizer.tokenize`]). Additionally, large
        comma-separated numbers and floating point values are split. E.g. "23,000 people are 1.80m tall" -> "23 @,@ 000
        people are 1 @.@ 80m tall"

        Args:
            text: Text to be tokenize

        Returns:
            A list of tokenized string

        Example:

        ```python
        >>> tokenizer = TransfoXLTokenizer.from_pretrained("transfo-xl-wt103")
        >>> tokenizer.moses_pipeline("23,000 people are 1.80 m tall")
        [\'23\', \'@,@\', \'000\', \'people\', \'are\', \'1\', \'@.@\', \'80\', \'m\', \'tall\']
        ```'''
    def convert_tokens_to_string(self, tokens):
        """
        Converts a sequence of tokens (string) in a single string. Additionally, the split numbers are converted back
        into it's original form.
        """
    def convert_to_tensor(self, symbols): ...
    @property
    def vocab_size(self): ...
    def get_vocab(self): ...

class LMOrderedIterator:
    bsz: Incomplete
    bptt: Incomplete
    ext_len: Incomplete
    device: Incomplete
    n_step: Incomplete
    data: Incomplete
    n_batch: Incomplete
    def __init__(self, data, bsz, bptt, device: str = 'cpu', ext_len: Incomplete | None = None) -> None:
        """
        data -- LongTensor -- the LongTensor is strictly ordered
        """
    def get_batch(self, i, bptt: Incomplete | None = None): ...
    def get_fixlen_iter(self, start: int = 0) -> Generator[Incomplete, None, None]: ...
    def get_varlen_iter(self, start: int = 0, std: int = 5, min_len: int = 5, max_deviation: int = 3) -> Generator[Incomplete, None, None]: ...
    def __iter__(self): ...

class LMShuffledIterator:
    data: Incomplete
    bsz: Incomplete
    bptt: Incomplete
    ext_len: Incomplete
    device: Incomplete
    shuffle: Incomplete
    def __init__(self, data, bsz, bptt, device: str = 'cpu', ext_len: Incomplete | None = None, shuffle: bool = False) -> None:
        """
        data -- list[LongTensor] -- there is no order among the LongTensors
        """
    def get_sent_stream(self) -> Generator[Incomplete, None, None]: ...
    def stream_iterator(self, sent_stream) -> Generator[Incomplete, None, None]: ...
    def __iter__(self): ...

class LMMultiFileIterator(LMShuffledIterator):
    paths: Incomplete
    vocab: Incomplete
    bsz: Incomplete
    bptt: Incomplete
    ext_len: Incomplete
    device: Incomplete
    shuffle: Incomplete
    def __init__(self, paths, vocab, bsz, bptt, device: str = 'cpu', ext_len: Incomplete | None = None, shuffle: bool = False) -> None: ...
    def get_sent_stream(self, path): ...
    def __iter__(self): ...

class TransfoXLCorpus:
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, cache_dir: Incomplete | None = None, *inputs, **kwargs):
        """
        Instantiate a pre-processed corpus.
        """
    vocab: Incomplete
    dataset: Incomplete
    train: Incomplete
    valid: Incomplete
    test: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def build_corpus(self, path, dataset) -> None: ...
    def get_iterator(self, split, *args, **kwargs): ...

def get_lm_corpus(datadir, dataset): ...
