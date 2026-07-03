from ...tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from ...utils import is_sentencepiece_available as is_sentencepiece_available, logging as logging
from _typeshed import Incomplete
from typing import Any, Dict, List, Optional, Tuple

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
SPIECE_UNDERLINE: str
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete
PRETRAINED_INIT_CONFIGURATION: Incomplete

def load_vocab(vocab_file):
    """Loads a vocabulary file into a dictionary."""
def whitespace_tokenize(text):
    """Runs basic whitespace cleaning and splitting on a piece of text."""

class BertJapaneseTokenizer(PreTrainedTokenizer):
    '''
    Construct a BERT tokenizer for Japanese text.

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains most of the main methods. Users should refer
    to: this superclass for more information regarding those methods.

    Args:
        vocab_file (`str`):
            Path to a one-wordpiece-per-line vocabulary file.
        spm_file (`str`, *optional*):
            Path to [SentencePiece](https://github.com/google/sentencepiece) file (generally has a .spm or .model
            extension) that contains the vocabulary.
        do_lower_case (`bool`, *optional*, defaults to `True`):
            Whether to lower case the input. Only has an effect when do_basic_tokenize=True.
        do_word_tokenize (`bool`, *optional*, defaults to `True`):
            Whether to do word tokenization.
        do_subword_tokenize (`bool`, *optional*, defaults to `True`):
            Whether to do subword tokenization.
        word_tokenizer_type (`str`, *optional*, defaults to `"basic"`):
            Type of word tokenizer. Choose from ["basic", "mecab", "sudachi", "jumanpp"].
        subword_tokenizer_type (`str`, *optional*, defaults to `"wordpiece"`):
            Type of subword tokenizer. Choose from ["wordpiece", "character", "sentencepiece",].
        mecab_kwargs (`dict`, *optional*):
            Dictionary passed to the `MecabTokenizer` constructor.
        sudachi_kwargs (`dict`, *optional*):
            Dictionary passed to the `SudachiTokenizer` constructor.
        jumanpp_kwargs (`dict`, *optional*):
            Dictionary passed to the `JumanppTokenizer` constructor.
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    pretrained_init_configuration = PRETRAINED_INIT_CONFIGURATION
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    spm_file: Incomplete
    vocab: Incomplete
    ids_to_tokens: Incomplete
    do_word_tokenize: Incomplete
    word_tokenizer_type: Incomplete
    lower_case: Incomplete
    never_split: Incomplete
    mecab_kwargs: Incomplete
    sudachi_kwargs: Incomplete
    jumanpp_kwargs: Incomplete
    word_tokenizer: Incomplete
    do_subword_tokenize: Incomplete
    subword_tokenizer_type: Incomplete
    subword_tokenizer: Incomplete
    def __init__(self, vocab_file, spm_file: Incomplete | None = None, do_lower_case: bool = False, do_word_tokenize: bool = True, do_subword_tokenize: bool = True, word_tokenizer_type: str = 'basic', subword_tokenizer_type: str = 'wordpiece', never_split: Incomplete | None = None, unk_token: str = '[UNK]', sep_token: str = '[SEP]', pad_token: str = '[PAD]', cls_token: str = '[CLS]', mask_token: str = '[MASK]', mecab_kwargs: Incomplete | None = None, sudachi_kwargs: Incomplete | None = None, jumanpp_kwargs: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def do_lower_case(self): ...
    @property
    def vocab_size(self): ...
    def get_vocab(self): ...
    def convert_tokens_to_string(self, tokens):
        """Converts a sequence of tokens (string) in a single string."""
    def build_inputs_with_special_tokens(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None) -> List[int]:
        """
        Build model inputs from a sequence or a pair of sequence for sequence classification tasks by concatenating and
        adding special tokens. A BERT sequence has the following format:

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
        Create a mask from the two sequences passed to be used in a sequence-pair classification task. A BERT sequence
        pair mask has the following format:

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

class MecabTokenizer:
    """Runs basic tokenization with MeCab morphological parser."""
    do_lower_case: Incomplete
    never_split: Incomplete
    normalize_text: Incomplete
    mecab: Incomplete
    def __init__(self, do_lower_case: bool = False, never_split: Incomplete | None = None, normalize_text: bool = True, mecab_dic: Optional[str] = 'ipadic', mecab_option: Optional[str] = None) -> None:
        '''
        Constructs a MecabTokenizer.

        Args:
            **do_lower_case**: (*optional*) boolean (default True)
                Whether to lowercase the input.
            **never_split**: (*optional*) list of str
                Kept for backward compatibility purposes. Now implemented directly at the base class level (see
                [`PreTrainedTokenizer.tokenize`]) List of tokens not to split.
            **normalize_text**: (*optional*) boolean (default True)
                Whether to apply unicode normalization to text before tokenization.
            **mecab_dic**: (*optional*) string (default "ipadic")
                Name of dictionary to be used for MeCab initialization. If you are using a system-installed dictionary,
                set this option to `None` and modify *mecab_option*.
            **mecab_option**: (*optional*) string
                String passed to MeCab constructor.
        '''
    def tokenize(self, text, never_split: Incomplete | None = None, **kwargs):
        """Tokenizes a piece of text."""

class SudachiTokenizer:
    """Runs basic tokenization with Sudachi morphological parser."""
    do_lower_case: Incomplete
    never_split: Incomplete
    normalize_text: Incomplete
    trim_whitespace: Incomplete
    split_mode: Incomplete
    sudachi: Incomplete
    def __init__(self, do_lower_case: bool = False, never_split: Incomplete | None = None, normalize_text: bool = True, trim_whitespace: bool = False, sudachi_split_mode: str = 'A', sudachi_config_path: Incomplete | None = None, sudachi_resource_dir: Incomplete | None = None, sudachi_dict_type: str = 'core') -> None:
        '''
        Constructs a SudachiTokenizer.

        Args:
            **do_lower_case**: (*optional*) boolean (default True)
                Whether to lowercase the input.
            **never_split**: (*optional*) list of str
                Kept for backward compatibility purposes. Now implemented directly at the base class level (see
                [`PreTrainedTokenizer.tokenize`]) List of tokens not to split.
            **normalize_text**: (*optional*) boolean (default True)
                Whether to apply unicode normalization to text before tokenization.
            **trim_whitespace**: (*optional*) boolean (default False)
                Whether to trim all whitespace, tab, newline from tokens.
            **sudachi_split_mode**: (*optional*) string
                Split mode of sudachi, choose from "A", "B", "C".
            **sudachi_config_path**: (*optional*) string
            **sudachi_resource_dir**: (*optional*) string
            **sudachi_dict_type**: (*optional*) string
                dict type of sudachi, choose from "small", "core", "full".
        '''
    def tokenize(self, text, never_split: Incomplete | None = None, **kwargs):
        """Tokenizes a piece of text."""

class JumanppTokenizer:
    """Runs basic tokenization with jumanpp morphological parser."""
    do_lower_case: Incomplete
    never_split: Incomplete
    normalize_text: Incomplete
    trim_whitespace: Incomplete
    juman: Incomplete
    def __init__(self, do_lower_case: bool = False, never_split: Incomplete | None = None, normalize_text: bool = True, trim_whitespace: bool = False) -> None:
        """
        Constructs a JumanppTokenizer.

        Args:
            **do_lower_case**: (*optional*) boolean (default True)
                Whether to lowercase the input.
            **never_split**: (*optional*) list of str
                Kept for backward compatibility purposes. Now implemented directly at the base class level (see
                [`PreTrainedTokenizer.tokenize`]) List of tokens not to split.
            **normalize_text**: (*optional*) boolean (default True)
                Whether to apply unicode normalization to text before tokenization.
            **trim_whitespace**: (*optional*) boolean (default False)
                Whether to trim all whitespace, tab, newline from tokens.
        """
    def tokenize(self, text, never_split: Incomplete | None = None, **kwargs):
        """Tokenizes a piece of text."""

class CharacterTokenizer:
    """Runs Character tokenization."""
    vocab: Incomplete
    unk_token: Incomplete
    normalize_text: Incomplete
    def __init__(self, vocab, unk_token, normalize_text: bool = True) -> None:
        """
        Constructs a CharacterTokenizer.

        Args:
            **vocab**:
                Vocabulary object.
            **unk_token**: str
                A special symbol for out-of-vocabulary token.
            **normalize_text**: (`optional`) boolean (default True)
                Whether to apply unicode normalization to text before tokenization.
        """
    def tokenize(self, text):
        '''
        Tokenizes a piece of text into characters.

        For example, `input = "apple""` wil return as output `["a", "p", "p", "l", "e"]`.

        Args:
            text: A single token or whitespace separated tokens.
                This should have already been passed through *BasicTokenizer*.

        Returns:
            A list of characters.
        '''

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

class WordpieceTokenizer:
    """Runs WordPiece tokenization."""
    vocab: Incomplete
    unk_token: Incomplete
    max_input_chars_per_word: Incomplete
    def __init__(self, vocab, unk_token, max_input_chars_per_word: int = 100) -> None: ...
    def tokenize(self, text):
        '''
        Tokenizes a piece of text into its word pieces. This uses a greedy longest-match-first algorithm to perform
        tokenization using the given vocabulary.

        For example, `input = "unaffable"` wil return as output `["un", "##aff", "##able"]`.

        Args:
            text: A single token or whitespace separated tokens. This should have
                already been passed through *BasicTokenizer*.

        Returns:
            A list of wordpiece tokens.
        '''

class SentencepieceTokenizer:
    """
    Runs sentencepiece tokenization. Based on transformers.models.albert.tokenization_albert.AlbertTokenizer.
    """
    vocab: Incomplete
    unk_token: Incomplete
    do_lower_case: Incomplete
    remove_space: Incomplete
    keep_accents: Incomplete
    sp_model_kwargs: Incomplete
    sp_model: Incomplete
    def __init__(self, vocab, unk_token, do_lower_case: bool = False, remove_space: bool = True, keep_accents: bool = True, sp_model_kwargs: Optional[Dict[str, Any]] = None) -> None: ...
    def preprocess_text(self, inputs): ...
    def tokenize(self, text):
        """
        Tokenizes text by sentencepiece. Based on [SentencePiece](https://github.com/google/sentencepiece).
        Tokenization needs the given vocabulary.

        Args:
            text: A string needs to be tokenized.

        Returns:
            A list of sentencepiece tokens.
        """
