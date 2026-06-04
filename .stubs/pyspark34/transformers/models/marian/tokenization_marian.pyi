import re
import sentencepiece
from ...tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Any, Dict, List, Optional, Tuple, Union

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete
PRETRAINED_INIT_CONFIGURATION: Incomplete

class MarianTokenizer(PreTrainedTokenizer):
    '''
    Construct a Marian tokenizer. Based on [SentencePiece](https://github.com/google/sentencepiece).

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains most of the main methods. Users should refer to
    this superclass for more information regarding those methods.

    Args:
        source_spm (`str`):
            [SentencePiece](https://github.com/google/sentencepiece) file (generally has a .spm extension) that
            contains the vocabulary for the source language.
        target_spm (`str`):
            [SentencePiece](https://github.com/google/sentencepiece) file (generally has a .spm extension) that
            contains the vocabulary for the target language.
        source_lang (`str`, *optional*):
            A string representing the source language.
        target_lang (`str`, *optional*):
            A string representing the target language.
        unk_token (`str`, *optional*, defaults to `"<unk>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        eos_token (`str`, *optional*, defaults to `"</s>"`):
            The end of sequence token.
        pad_token (`str`, *optional*, defaults to `"<pad>"`):
            The token used for padding, for example when batching sequences of different lengths.
        model_max_length (`int`, *optional*, defaults to 512):
            The maximum sentence length the model accepts.
        additional_special_tokens (`List[str]`, *optional*, defaults to `["<eop>", "<eod>"]`):
            Additional special tokens used by the tokenizer.
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

    Examples:

    ```python
    >>> from transformers import MarianTokenizer

    >>> tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-de")
    >>> src_texts = ["I am a small frog.", "Tom asked his teacher for advice."]
    >>> tgt_texts = ["Ich bin ein kleiner Frosch.", "Tom bat seinen Lehrer um Rat."]  # optional
    >>> inputs = tokenizer(src_texts, text_target=tgt_texts, return_tensors="pt", padding=True)
    # keys  [input_ids, attention_mask, labels].

    >>> outputs = model(**inputs)  # should work
    ```'''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    pretrained_init_configuration = PRETRAINED_INIT_CONFIGURATION
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    model_input_names: Incomplete
    language_code_re: re.Pattern
    sp_model_kwargs: Incomplete
    separate_vocabs: Incomplete
    encoder: Incomplete
    target_encoder: Incomplete
    decoder: Incomplete
    supported_language_codes: Incomplete
    source_lang: Incomplete
    target_lang: Incomplete
    spm_files: Incomplete
    spm_source: Incomplete
    spm_target: Incomplete
    current_spm: Incomplete
    current_encoder: Incomplete
    def __init__(self, source_spm, target_spm, vocab, target_vocab_file: Incomplete | None = None, source_lang: Incomplete | None = None, target_lang: Incomplete | None = None, unk_token: str = '<unk>', eos_token: str = '</s>', pad_token: str = '<pad>', model_max_length: int = 512, sp_model_kwargs: Optional[Dict[str, Any]] = None, separate_vocabs: bool = False, **kwargs) -> None: ...
    def normalize(self, x: str) -> str:
        """Cover moses empty string edge case. They return empty list for '' input!"""
    def remove_language_code(self, text: str):
        """Remove language codes like >>fr<< before sentencepiece"""
    def batch_decode(self, sequences, **kwargs):
        """
        Convert a list of lists of token ids into a list of strings by calling decode.

        Args:
            sequences (`Union[List[int], List[List[int]], np.ndarray, torch.Tensor, tf.Tensor]`):
                List of tokenized input ids. Can be obtained using the `__call__` method.
            skip_special_tokens (`bool`, *optional*, defaults to `False`):
                Whether or not to remove special tokens in the decoding.
            clean_up_tokenization_spaces (`bool`, *optional*, defaults to `True`):
                Whether or not to clean up the tokenization spaces.
            use_source_tokenizer (`bool`, *optional*, defaults to `False`):
                Whether or not to use the source tokenizer to decode sequences (only applicable in sequence-to-sequence
                problems).
            kwargs (additional keyword arguments, *optional*):
                Will be passed to the underlying model specific decode method.

        Returns:
            `List[str]`: The list of decoded sentences.
        """
    def decode(self, token_ids, **kwargs):
        """
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
            use_source_tokenizer (`bool`, *optional*, defaults to `False`):
                Whether or not to use the source tokenizer to decode sequences (only applicable in sequence-to-sequence
                problems).
            kwargs (additional keyword arguments, *optional*):
                Will be passed to the underlying model specific decode method.

        Returns:
            `str`: The decoded sentence.
        """
    def convert_tokens_to_string(self, tokens: List[str]) -> str:
        """Uses source spm if _decode_use_source_tokenizer is True, and target spm otherwise"""
    def build_inputs_with_special_tokens(self, token_ids_0, token_ids_1: Incomplete | None = None) -> List[int]:
        """Build model inputs from a sequence by appending eos_token_id."""
    @property
    def vocab_size(self) -> int: ...
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
    def get_vocab(self) -> Dict: ...
    def get_src_vocab(self): ...
    def get_tgt_vocab(self): ...
    def num_special_tokens_to_add(self, *args, **kwargs):
        """Just EOS"""
    def get_special_tokens_mask(self, token_ids_0: List, token_ids_1: Optional[List] = None, already_has_special_tokens: bool = False) -> List[int]:
        """Get list where entries are [1] if a token is [eos] or [pad] else 0."""

def load_spm(path: str, sp_model_kwargs: Dict[str, Any]) -> sentencepiece.SentencePieceProcessor: ...
def save_json(data, path: str) -> None: ...
def load_json(path: str) -> Union[Dict, List]: ...
