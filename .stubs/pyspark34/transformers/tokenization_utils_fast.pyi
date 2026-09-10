from .convert_slow_tokenizer import convert_slow_tokenizer as convert_slow_tokenizer
from .tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from .tokenization_utils_base import AddedToken as AddedToken, BatchEncoding as BatchEncoding, INIT_TOKENIZER_DOCSTRING as INIT_TOKENIZER_DOCSTRING, PreTokenizedInput as PreTokenizedInput, PreTokenizedInputPair as PreTokenizedInputPair, PreTrainedTokenizerBase as PreTrainedTokenizerBase, SpecialTokensMixin as SpecialTokensMixin, TextInput as TextInput, TextInputPair as TextInputPair, TruncationStrategy as TruncationStrategy
from .utils import PaddingStrategy as PaddingStrategy, add_end_docstrings as add_end_docstrings, logging as logging
from _typeshed import Incomplete
from tokenizers import Tokenizer as TokenizerFast
from tokenizers.decoders import Decoder as DecoderFast
from typing import Dict, List, Optional, Union

logger: Incomplete
TOKENIZER_FILE: str
SPECIAL_TOKENS_MAP_FILE: str
TOKENIZER_CONFIG_FILE: str
ADDED_TOKENS_FILE: str
MODEL_TO_TRAINER_MAPPING: Incomplete
VOCAB_FILES_NAMES: Incomplete

class PreTrainedTokenizerFast(PreTrainedTokenizerBase):
    """
    Base class for all fast tokenizers (wrapping HuggingFace tokenizers library).

    Inherits from [`~tokenization_utils_base.PreTrainedTokenizerBase`].

    Handles all the shared methods for tokenization and special tokens, as well as methods for
    downloading/caching/loading pretrained tokenizers, as well as adding tokens to the vocabulary.

    This class also contains the added tokens in a unified way on top of all tokenizers so we don't have to handle the
    specific vocabulary augmentation methods of the various underlying dictionary structures (BPE, sentencepiece...).
    """
    vocab_files_names = VOCAB_FILES_NAMES
    slow_tokenizer_class: PreTrainedTokenizer
    can_save_slow_tokenizer: bool
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def is_fast(self) -> bool: ...
    @property
    def vocab_size(self) -> int:
        """
        `int`: Size of the base vocabulary (without the added tokens).
        """
    def get_vocab(self) -> Dict[str, int]: ...
    @property
    def vocab(self) -> Dict[str, int]: ...
    def get_added_vocab(self) -> Dict[str, int]:
        """
        Returns the added tokens in the vocabulary as a dictionary of token to index.

        Returns:
            `Dict[str, int]`: The added tokens.
        """
    def __len__(self) -> int:
        """
        Size of the full vocabulary with the added tokens.
        """
    @property
    def backend_tokenizer(self) -> TokenizerFast:
        """
        `tokenizers.implementations.BaseTokenizer`: The Rust tokenizer used as a backend.
        """
    @property
    def decoder(self) -> DecoderFast:
        """
        `tokenizers.decoders.Decoder`: The Rust decoder for this tokenizer.
        """
    def convert_tokens_to_ids(self, tokens: Union[str, List[str]]) -> Union[int, List[int]]:
        """
        Converts a token string (or a sequence of tokens) in a single integer id (or a sequence of ids), using the
        vocabulary.

        Args:
            tokens (`str` or `List[str]`): One or several token(s) to convert to token id(s).

        Returns:
            `int` or `List[int]`: The token id or list of token ids.
        """
    def num_special_tokens_to_add(self, pair: bool = False) -> int:
        """
        Returns the number of added tokens when encoding a sequence with special tokens.

        <Tip>

        This encodes a dummy input and checks the number of added tokens, and is therefore not efficient. Do not put
        this inside your training loop.

        </Tip>

        Args:
            pair (`bool`, *optional*, defaults to `False`):
                Whether the number of added tokens should be computed in the case of a sequence pair or a single
                sequence.

        Returns:
            `int`: Number of special tokens added to sequences.
        """
    def convert_ids_to_tokens(self, ids: Union[int, List[int]], skip_special_tokens: bool = False) -> Union[str, List[str]]:
        """
        Converts a single index or a sequence of indices in a token or a sequence of tokens, using the vocabulary and
        added tokens.

        Args:
            ids (`int` or `List[int]`):
                The token id (or token ids) to convert to tokens.
            skip_special_tokens (`bool`, *optional*, defaults to `False`):
                Whether or not to remove special tokens in the decoding.

        Returns:
            `str` or `List[str]`: The decoded token(s).
        """
    def tokenize(self, text: str, pair: Optional[str] = None, add_special_tokens: bool = False, **kwargs) -> List[str]: ...
    def set_truncation_and_padding(self, padding_strategy: PaddingStrategy, truncation_strategy: TruncationStrategy, max_length: int, stride: int, pad_to_multiple_of: Optional[int]):
        """
        Define the truncation and the padding strategies for fast tokenizers (provided by HuggingFace tokenizers
        library) and restore the tokenizer settings afterwards.

        The provided tokenizer has no padding / truncation strategy before the managed section. If your tokenizer set a
        padding / truncation strategy before, then it will be reset to no padding / truncation when exiting the managed
        section.

        Args:
            padding_strategy ([`~utils.PaddingStrategy`]):
                The kind of padding that will be applied to the input
            truncation_strategy ([`~tokenization_utils_base.TruncationStrategy`]):
                The kind of truncation that will be applied to the input
            max_length (`int`):
                The maximum size of a sequence.
            stride (`int`):
                The stride to use when handling overflow.
            pad_to_multiple_of (`int`, *optional*):
                If set will pad the sequence to a multiple of the provided value. This is especially useful to enable
                the use of Tensor Cores on NVIDIA hardware with compute capability `>= 7.5` (Volta).
        """
    def convert_tokens_to_string(self, tokens: List[str]) -> str: ...
    def train_new_from_iterator(self, text_iterator, vocab_size, length: Incomplete | None = None, new_special_tokens: Incomplete | None = None, special_tokens_map: Incomplete | None = None, **kwargs):
        """
        Trains a tokenizer on a new corpus with the same defaults (in terms of special tokens or tokenization pipeline)
        as the current one.

        Args:
            text_iterator (generator of `List[str]`):
                The training corpus. Should be a generator of batches of texts, for instance a list of lists of texts
                if you have everything in memory.
            vocab_size (`int`):
                The size of the vocabulary you want for your tokenizer.
            length (`int`, *optional*):
                The total number of sequences in the iterator. This is used to provide meaningful progress tracking
            new_special_tokens (list of `str` or `AddedToken`, *optional*):
                A list of new special tokens to add to the tokenizer you are training.
            special_tokens_map (`Dict[str, str]`, *optional*):
                If you want to rename some of the special tokens this tokenizer uses, pass along a mapping old special
                token name to new special token name in this argument.
            kwargs:
                Additional keyword arguments passed along to the trainer from the 🤗 Tokenizers library.

        Returns:
            [`PreTrainedTokenizerFast`]: A new tokenizer of the same type as the original one, trained on
            `text_iterator`.

        """
