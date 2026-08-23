from .tokenization_utils_base import AddedToken as AddedToken, BatchEncoding as BatchEncoding, ENCODE_KWARGS_DOCSTRING as ENCODE_KWARGS_DOCSTRING, ENCODE_PLUS_ADDITIONAL_KWARGS_DOCSTRING as ENCODE_PLUS_ADDITIONAL_KWARGS_DOCSTRING, EncodedInput as EncodedInput, EncodedInputPair as EncodedInputPair, INIT_TOKENIZER_DOCSTRING as INIT_TOKENIZER_DOCSTRING, PreTokenizedInput as PreTokenizedInput, PreTokenizedInputPair as PreTokenizedInputPair, PreTrainedTokenizerBase as PreTrainedTokenizerBase, TextInput as TextInput, TextInputPair as TextInputPair, TruncationStrategy as TruncationStrategy
from .utils import PaddingStrategy as PaddingStrategy, TensorType as TensorType, add_end_docstrings as add_end_docstrings, logging as logging
from _typeshed import Incomplete
from typing import Any, Dict, List, Optional, Tuple, Union, overload

logger: Incomplete
SPECIAL_TOKENS_MAP_FILE: str
ADDED_TOKENS_FILE: str
TOKENIZER_CONFIG_FILE: str

class Trie:
    """
    Trie in Python. Creates a Trie out of a list of words. The trie is used to split on `added_tokens` in one pass
    Loose reference https://en.wikipedia.org/wiki/Trie
    """
    data: Incomplete
    def __init__(self) -> None: ...
    def add(self, word: str):
        '''
        Passes over every char (utf-8 char) on word and recursively adds it to the internal `data` trie representation.
        The special key `""` is used to represent termination.

        This function is idempotent, adding twice the same word will leave the trie unchanged

        Example:

        ```python
        >>> trie = Trie()
        >>> trie.add("Hello 友達")
        >>> trie.data
        {"H": {"e": {"l": {"l": {"o": {" ": {"友": {"達": {"": 1}}}}}}}}}

        >>> trie.add("Hello")
        >>> trie.data
        {"H": {"e": {"l": {"l": {"o": {"": 1, " ": {"友": {"達": {"": 1}}}}}}}}}
        ```
        '''
    def split(self, text: str) -> List[str]:
        '''
        Will look for the words added to the trie within `text`. Output is the original string splitted along the
        boundaries of the words found.

        This trie will match the longest possible word first !

        Example:

        ```python
        >>> trie = Trie()
        >>> trie.split("[CLS] This is a extra_id_100")
        ["[CLS] This is a extra_id_100"]

        >>> trie.add("[CLS]")
        >>> trie.add("extra_id_1")
        >>> trie.add("extra_id_100")
        >>> trie.split("[CLS] This is a extra_id_100")
        ["[CLS]", " This is a ", "extra_id_100"]
        ```
        '''
    def cut_text(self, text, offsets): ...

class PreTrainedTokenizer(PreTrainedTokenizerBase):
    """
    Base class for all slow tokenizers.

    Inherits from [`~tokenization_utils_base.PreTrainedTokenizerBase`].

    Handle all the shared methods for tokenization and special tokens as well as methods downloading/caching/loading
    pretrained tokenizers as well as adding tokens to the vocabulary.

    This class also contain the added tokens in a unified way on top of all tokenizers so we don't have to handle the
    specific vocabulary augmentation methods of the various underlying dictionary structures (BPE, sentencepiece...).
    """
    added_tokens_encoder: Incomplete
    added_tokens_decoder: Incomplete
    unique_no_split_tokens: Incomplete
    tokens_trie: Incomplete
    def __init__(self, **kwargs) -> None: ...
    @property
    def is_fast(self) -> bool: ...
    @property
    def vocab_size(self) -> int:
        """
        `int`: Size of the base vocabulary (without the added tokens).
        """
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
    def tokenize(self, text: TextInput, **kwargs) -> List[str]:
        """
        Converts a string in a sequence of tokens, using the tokenizer.

        Split in words for word-based vocabulary or sub-words for sub-word-based vocabularies
        (BPE/SentencePieces/WordPieces). Takes care of added tokens.

        Args:
            text (`str`):
                The sequence to be encoded.
            **kwargs (additional keyword arguments):
                Passed along to the model-specific `prepare_for_tokenization` preprocessing method.

        Returns:
            `List[str]`: The list of tokens.
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
    def prepare_for_tokenization(self, text: str, is_split_into_words: bool = False, **kwargs) -> Tuple[str, Dict[str, Any]]:
        """
        Performs any necessary transformations before tokenization.

        This method should pop the arguments from kwargs and return the remaining `kwargs` as well. We test the
        `kwargs` at the end of the encoding process to be sure all the arguments have been used.

        Args:
            text (`str`):
                The text to prepare.
            is_split_into_words (`bool`, *optional*, defaults to `False`):
                Whether or not the input is already pre-tokenized (e.g., split into words). If set to `True`, the
                tokenizer assumes the input is already split into words (for instance, by splitting it on whitespace)
                which it will tokenize. This is useful for NER or token classification.
            kwargs:
                Keyword arguments to use for the tokenization.

        Returns:
            `Tuple[str, Dict[str, Any]]`: The prepared text and the unused kwargs.
        """
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
    @overload
    def convert_ids_to_tokens(self, ids: int, skip_special_tokens: bool = False) -> str: ...
    @overload
    def convert_ids_to_tokens(self, ids: List[int], skip_special_tokens: bool = False) -> List[str]: ...
    def convert_tokens_to_string(self, tokens: List[str]) -> str: ...
