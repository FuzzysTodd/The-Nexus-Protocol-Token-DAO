from ...tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from _typeshed import Incomplete
from typing import Any, Dict, Optional, Tuple

PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete
PRETRAINED_INIT_CONFIGURATION: Incomplete
VOCAB_FILES_NAMES: Incomplete

class DebertaV2Tokenizer(PreTrainedTokenizer):
    '''
    Constructs a DeBERTa-v2 tokenizer. Based on [SentencePiece](https://github.com/google/sentencepiece).

    Args:
        vocab_file (`str`):
            [SentencePiece](https://github.com/google/sentencepiece) file (generally has a *.spm* extension) that
            contains the vocabulary necessary to instantiate a tokenizer.
        do_lower_case (`bool`, *optional*, defaults to `False`):
            Whether or not to lowercase the input when tokenizing.
        bos_token (`string`, *optional*, defaults to `"[CLS]"`):
            The beginning of sequence token that was used during pre-training. Can be used a sequence classifier token.
            When building a sequence using special tokens, this is not the token that is used for the beginning of
            sequence. The token used is the `cls_token`.
        eos_token (`string`, *optional*, defaults to `"[SEP]"`):
            The end of sequence token. When building a sequence using special tokens, this is not the token that is
            used for the end of sequence. The token used is the `sep_token`.
        unk_token (`str`, *optional*, defaults to `"[UNK]"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        sep_token (`str`, *optional*, defaults to `"[SEP]"`):
            The separator token, which is used when building a sequence from multiple sequences, e.g. two sequences for
            sequence classification or for a text and a question for question answering. It is also used as the last
            token of a sequence built with special tokens.
        pad_token (`str`, *optional*, defaults to `"[PAD]"`):
            The token used for padding, for example when batching sequences of different lengths.
        cls_token (`str`, *optional*, defaults to `"[CLS]"`):
            The classifier token which is used when doing sequence classification (classification of the whole sequence
            instead of per-token classification). It is the first token of the sequence when built with special tokens.
        mask_token (`str`, *optional*, defaults to `"[MASK]"`):
            The token used for masking values. This is the token used when training this model with masked language
            modeling. This is the token which the model will try to predict.
        sp_model_kwargs (`dict`, *optional*):
            Will be passed to the `SentencePieceProcessor.__init__()` method. The [Python wrapper for
            SentencePiece](https://github.com/google/sentencepiece/tree/master/python) can be used, among other things,
            to set:

            - `enable_sampling`: Enable subword regularization.
            - `nbest_size`: Sampling parameters for unigram. Invalid for BPE-Dropout.

              - `nbest_size = {0,1}`: No sampling is performed.
              - `nbest_size > 1`: samples from the nbest_size results.
              - `nbest_size < 0`: assuming that nbest_size is infinite and samples from the all hypothesis (lattice)
                using forward-filtering-and-backward-sampling algorithm.

            - `alpha`: Smoothing parameter for unigram sampling, and dropout probability of merge operations for
              BPE-dropout.
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    pretrained_init_configuration = PRETRAINED_INIT_CONFIGURATION
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    sp_model_kwargs: Incomplete
    do_lower_case: Incomplete
    split_by_punct: Incomplete
    vocab_file: Incomplete
    def __init__(self, vocab_file, do_lower_case: bool = False, split_by_punct: bool = False, bos_token: str = '[CLS]', eos_token: str = '[SEP]', unk_token: str = '[UNK]', sep_token: str = '[SEP]', pad_token: str = '[PAD]', cls_token: str = '[CLS]', mask_token: str = '[MASK]', sp_model_kwargs: Optional[Dict[str, Any]] = None, **kwargs) -> None: ...
    @property
    def vocab_size(self): ...
    @property
    def vocab(self): ...
    def get_vocab(self): ...
    def convert_tokens_to_string(self, tokens):
        """Converts a sequence of tokens (string) in a single string."""
    def build_inputs_with_special_tokens(self, token_ids_0, token_ids_1: Incomplete | None = None):
        """
        Build model inputs from a sequence or a pair of sequence for sequence classification tasks by concatenating and
        adding special tokens. A DeBERTa sequence has the following format:

        - single sequence: [CLS] X [SEP]
        - pair of sequences: [CLS] A [SEP] B [SEP]

        Args:
            token_ids_0 (`List[int]`):
                List of IDs to which the special tokens will be added.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.

        Returns:
            `List[int]`: List of [input IDs](../glossary#input-ids) with the appropriate special tokens.
        """
    def get_special_tokens_mask(self, token_ids_0, token_ids_1: Incomplete | None = None, already_has_special_tokens: bool = False):
        """
        Retrieves sequence ids from a token list that has no special tokens added. This method is called when adding
        special tokens using the tokenizer `prepare_for_model` or `encode_plus` methods.

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
    def create_token_type_ids_from_sequences(self, token_ids_0, token_ids_1: Incomplete | None = None):
        """
        Create a mask from the two sequences passed to be used in a sequence-pair classification task. A DeBERTa
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
    def prepare_for_tokenization(self, text, is_split_into_words: bool = False, **kwargs): ...
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...

class SPMTokenizer:
    """
    Constructs a tokenizer based on [SentencePiece](https://github.com/google/sentencepiece).

    Args:
        vocab_file (`str`):
            [SentencePiece](https://github.com/google/sentencepiece) file (generally has a *.spm* extension) that
            contains the vocabulary necessary to instantiate a tokenizer.
        sp_model_kwargs (`dict`, *optional*):
            Will be passed to the `SentencePieceProcessor.__init__()` method. The [Python wrapper for
            SentencePiece](https://github.com/google/sentencepiece/tree/master/python) can be used, among other things,
            to set:

            - `enable_sampling`: Enable subword regularization.
            - `nbest_size`: Sampling parameters for unigram. Invalid for BPE-Dropout.

              - `nbest_size = {0,1}`: No sampling is performed.
              - `nbest_size > 1`: samples from the nbest_size results.
              - `nbest_size < 0`: assuming that nbest_size is infinite and samples from the all hypothesis (lattice)
                using forward-filtering-and-backward-sampling algorithm.

            - `alpha`: Smoothing parameter for unigram sampling, and dropout probability of merge operations for
              BPE-dropout.
    """
    split_by_punct: Incomplete
    vocab_file: Incomplete
    sp_model_kwargs: Incomplete
    vocab: Incomplete
    ids_to_tokens: Incomplete
    spm: Incomplete
    special_tokens: Incomplete
    def __init__(self, vocab_file, special_tokens, split_by_punct: bool = False, sp_model_kwargs: Optional[Dict[str, Any]] = None) -> None: ...
    def tokenize(self, text): ...
    def convert_ids_to_tokens(self, ids): ...
    def decode(self, tokens, start: int = -1, end: int = -1, raw_text: Incomplete | None = None): ...
    def add_special_token(self, token): ...
    def part_of_whole_word(self, token, is_bos: bool = False): ...
    def pad(self): ...
    def bos(self): ...
    def eos(self): ...
    def unk(self): ...
    def mask(self): ...
    def sym(self, id): ...
    def id(self, sym): ...
    def split_to_words(self, text): ...
    def save_pretrained(self, path: str, filename_prefix: str = None): ...

def convert_to_unicode(text):
    """Converts `text` to Unicode (if it's not already), assuming utf-8 input."""
