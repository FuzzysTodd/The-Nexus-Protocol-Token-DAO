import sentencepiece
from ...tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Any, Dict, List, Optional, Tuple, Union

logger: Incomplete
SPIECE_UNDERLINE: str
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
MAX_MODEL_INPUT_SIZES: Incomplete
MUSTC_LANGS: Incomplete
LANGUAGES: Incomplete

class Speech2TextTokenizer(PreTrainedTokenizer):
    '''
    Construct an Speech2Text tokenizer.

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains some of the main methods. Users should refer to
    the superclass for more information regarding such methods.

    Args:
        vocab_file (`str`):
            File containing the vocabulary.
        spm_file (`str`):
            Path to the [SentencePiece](https://github.com/google/sentencepiece) model file
        bos_token (`str`, *optional*, defaults to `"<s>"`):
            The beginning of sentence token.
        eos_token (`str`, *optional*, defaults to `"</s>"`):
            The end of sentence token.
        unk_token (`str`, *optional*, defaults to `"<unk>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        pad_token (`str`, *optional*, defaults to `"<pad>"`):
            The token used for padding, for example when batching sequences of different lengths.
        do_upper_case (`bool`, *optional*, defaults to `False`):
           Whether or not to uppercase the output when decoding.
        do_lower_case (`bool`, *optional*, defaults to `False`):
            Whether or not to lowercase the input when tokenizing.
        tgt_lang (`str`, *optional*):
            A string representing the target language.
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

        **kwargs
            Additional keyword arguments passed along to [`PreTrainedTokenizer`]
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = MAX_MODEL_INPUT_SIZES
    model_input_names: Incomplete
    prefix_tokens: List[int]
    sp_model_kwargs: Incomplete
    do_upper_case: Incomplete
    do_lower_case: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    spm_file: Incomplete
    sp_model: Incomplete
    lang_codes: Incomplete
    langs: Incomplete
    lang_tokens: Incomplete
    lang_code_to_id: Incomplete
    def __init__(self, vocab_file, spm_file, bos_token: str = '<s>', eos_token: str = '</s>', pad_token: str = '<pad>', unk_token: str = '<unk>', do_upper_case: bool = False, do_lower_case: bool = False, tgt_lang: Incomplete | None = None, lang_codes: Incomplete | None = None, sp_model_kwargs: Optional[Dict[str, Any]] = None, **kwargs) -> None: ...
    @property
    def vocab_size(self) -> int: ...
    @property
    def tgt_lang(self) -> str: ...
    @tgt_lang.setter
    def tgt_lang(self, new_tgt_lang) -> None: ...
    def set_tgt_lang_special_tokens(self, tgt_lang: str) -> None:
        """Reset the special tokens to the target language setting. prefix=[eos, tgt_lang_code] and suffix=[eos]."""
    def convert_tokens_to_string(self, tokens: List[str]) -> str:
        """Converts a sequence of tokens (strings for sub-words) in a single string."""
    def build_inputs_with_special_tokens(self, token_ids_0, token_ids_1: Incomplete | None = None) -> List[int]:
        """Build model inputs from a sequence by appending eos_token_id."""
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
    def get_vocab(self) -> Dict: ...
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...

def load_spm(path: str, sp_model_kwargs: Dict[str, Any]) -> sentencepiece.SentencePieceProcessor: ...
def load_json(path: str) -> Union[Dict, List]: ...
def save_json(data, path: str) -> None: ...
