from ...tokenization_utils_fast import PreTrainedTokenizerFast as PreTrainedTokenizerFast
from ...utils import logging as logging
from .tokenization_splinter import SplinterTokenizer as SplinterTokenizer
from _typeshed import Incomplete
from typing import List, Optional, Tuple

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete
PRETRAINED_INIT_CONFIGURATION: Incomplete

class SplinterTokenizerFast(PreTrainedTokenizerFast):
    '''
    Construct a "fast" Splinter tokenizer (backed by HuggingFace\'s *tokenizers* library). Based on WordPiece.

    This tokenizer inherits from [`PreTrainedTokenizerFast`] which contains most of the main methods. Users should
    refer to this superclass for more information regarding those methods.

    Args:
        vocab_file (`str`):
            File containing the vocabulary.
        do_lower_case (`bool`, *optional*, defaults to `True`):
            Whether or not to lowercase the input when tokenizing.
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
        question_token (`str`, *optional*, defaults to `"[QUESTION]"`):
            The token used for constructing question representations.
        clean_text (`bool`, *optional*, defaults to `True`):
            Whether or not to clean the text before tokenization by removing any control characters and replacing all
            whitespaces by the classic one.
        tokenize_chinese_chars (`bool`, *optional*, defaults to `True`):
            Whether or not to tokenize Chinese characters. This should likely be deactivated for Japanese (see [this
            issue](https://github.com/huggingface/transformers/issues/328)).
        strip_accents (`bool`, *optional*):
            Whether or not to strip all accents. If this option is not specified, then it will be determined by the
            value for `lowercase` (as in the original BERT).
        wordpieces_prefix (`str`, *optional*, defaults to `"##"`):
            The prefix for subwords.
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    pretrained_init_configuration = PRETRAINED_INIT_CONFIGURATION
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    slow_tokenizer_class = SplinterTokenizer
    do_lower_case: Incomplete
    def __init__(self, vocab_file: Incomplete | None = None, tokenizer_file: Incomplete | None = None, do_lower_case: bool = True, unk_token: str = '[UNK]', sep_token: str = '[SEP]', pad_token: str = '[PAD]', cls_token: str = '[CLS]', mask_token: str = '[MASK]', question_token: str = '[QUESTION]', tokenize_chinese_chars: bool = True, strip_accents: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def question_token_id(self):
        """
        `Optional[int]`: Id of the question token in the vocabulary, used to condition the answer on a question
        representation.
        """
    def build_inputs_with_special_tokens(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None) -> List[int]:
        """
        Build model inputs from a pair of sequence for question answering tasks by concatenating and adding special
        tokens. A Splinter sequence has the following format:

        - single sequence: `[CLS] X [SEP]`
        - pair of sequences for question answering: `[CLS] question_tokens [QUESTION] . [SEP] context_tokens [SEP]`

        Args:
            token_ids_0 (`List[int]`):
                The question token IDs if pad_on_right, else context tokens IDs
            token_ids_1 (`List[int]`, *optional*):
                The context token IDs if pad_on_right, else question token IDs

        Returns:
            `List[int]`: List of [input IDs](../glossary#input-ids) with the appropriate special tokens.
        """
    def create_token_type_ids_from_sequences(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None) -> List[int]:
        """
        Create the token type IDs corresponding to the sequences passed. [What are token type
        IDs?](../glossary#token-type-ids)

        Should be overridden in a subclass if the model has a special way of building those.

        Args:
            token_ids_0 (`List[int]`): The first tokenized sequence.
            token_ids_1 (`List[int]`, *optional*): The second tokenized sequence.

        Returns:
            `List[int]`: The token type ids.
        """
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
