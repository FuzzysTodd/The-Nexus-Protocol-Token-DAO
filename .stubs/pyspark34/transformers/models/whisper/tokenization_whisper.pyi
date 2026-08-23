from ...tokenization_utils import AddedToken as AddedToken, PreTrainedTokenizer as PreTrainedTokenizer
from ...utils import logging as logging
from .english_normalizer import EnglishTextNormalizer as EnglishTextNormalizer
from _typeshed import Incomplete
from typing import List, Optional, Tuple

VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
MAX_MODEL_INPUT_SIZES: Incomplete

def bytes_to_unicode():
    """
    Returns list of utf-8 byte and a mapping to unicode strings. We specifically avoids mapping to whitespace/control
    characters the bpe code barfs on.

    The reversible bpe codes work on unicode strings. This means you need a large # of unicode characters in your vocab
    if you want to avoid UNKs. When you're at something like a 10B token dataset you end up needing around 5K for
    decent coverage. This is a significant percentage of your normal, say, 32K bpe vocab. To avoid that, we want lookup
    tables between utf-8 bytes and unicode strings.
    """

logger: Incomplete

def get_pairs(word):
    """
    Return set of symbol pairs in a word.

    Word is represented as tuple of symbols (symbols being variable-length strings).
    """

LANGUAGES: Incomplete
TO_LANGUAGE_CODE: Incomplete
TASK_IDS: Incomplete

class WhisperTokenizer(PreTrainedTokenizer):
    '''
    Construct a Whisper tokenizer.

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains some of the main methods. Users should refer to
    the superclass for more information regarding such methods.

     Args:
        vocab_file (`str`):
            Path to the vocabulary file.
        merges_file (`str`):
            Path to the merges file.
        normalizer_file (`str`, *optional*, defaults to `None`):
            Path to the normalizer_file file.
        errors (`str`, *optional*, defaults to `"replace"`):
            Paradigm to follow when decoding bytes to UTF-8. See
            [bytes.decode](https://docs.python.org/3/library/stdtypes.html#bytes.decode) for more information.
        unk_token (`str`, *optional*, defaults to `"<|endoftext|>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        bos_token (`str`, *optional*, defaults to `"<|startoftranscript|>"`):
            The beginning of sequence token.
        eos_token (`str`, *optional*, defaults to `"<|endoftext|>"`):
            The end of sequence token.
        add_prefix_space (`bool`, *optional*, defaults to `False`):
            Whether or not to add an initial space to the input. This allows to treat the leading word just as any
            other word.
        language (`str`, *optional*):
            The language of the transcription text. The corresponding language id token is appended to the start of the
            sequence for multilingual speech recognition and speech translation tasks, e.g. for Spanish the token
            `"<|es|>"` is appended to the start of sequence. This should be used for multilingual fine-tuning only.
        task (`str`, *optional*):
            Task identifier to append at the start of sequence (if any). This should be used for mulitlingual
            fine-tuning, with `"transcribe"` for speech recognition and `"translate"` for speech translation.
        predict_timestamps (`bool`, *optional*, defaults to `False`):
            Whether to omit the `<|notimestamps|>` token at the start of the sequence.
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = MAX_MODEL_INPUT_SIZES
    model_input_names: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    errors: Incomplete
    byte_encoder: Incomplete
    byte_decoder: Incomplete
    bpe_ranks: Incomplete
    cache: Incomplete
    add_prefix_space: Incomplete
    english_spelling_normalizer: Incomplete
    pat: Incomplete
    language: Incomplete
    task: Incomplete
    predict_timestamps: Incomplete
    def __init__(self, vocab_file, merges_file, normalizer_file: Incomplete | None = None, errors: str = 'replace', unk_token: str = '<|endoftext|>', bos_token: str = '<|startoftranscript|>', eos_token: str = '<|endoftext|>', pad_token: Incomplete | None = None, add_prefix_space: bool = False, language: Incomplete | None = None, task: Incomplete | None = None, predict_timestamps: bool = False, **kwargs) -> None: ...
    def get_vocab(self): ...
    @property
    def vocab_size(self) -> int: ...
    def bpe(self, token): ...
    def set_prefix_tokens(self, language: str = None, task: str = None, predict_timestamps: bool = None):
        '''
        Override the prefix tokens appended to the start of the label sequence. This method can be used standalone to
        update the prefix tokens as required when fine-tuning. Example:

        ```python
        >>> # instantiate the tokenizer and set the prefix token to Spanish
        >>> tokenizer = WhisperTokenizer.from_pretrained("openai/whisper-tiny", language="spanish")
        >>> # now switch the prefix token from Spanish to French
        >>> tokenizer.set_prefix_tokens(language="french")
        ```

        Args:
            language (`str`, *optional*, defaults to `None`):
                The language of the transcription text.
            task (`str`, *optional*, defaults to `None`):
                Task identifier to append at the start of sequence (if any).
            predict_timestamps (`bool`, *optional*, defaults to `None`):
                Whether to omit the `<|notimestamps|>` token at the start of the sequence.
        '''
    @property
    def prefix_tokens(self) -> List[int]: ...
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
    def decode(self, token_ids, skip_special_tokens: bool = False, clean_up_tokenization_spaces: bool = True, output_offsets: bool = False, time_precision: float = 0.02, **kwargs) -> str:
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
            kwargs (additional keyword arguments, *optional*):
                Will be passed to the underlying model specific decode method.

        Returns:
            `str`: The decoded sentence.
        """
    def convert_tokens_to_string(self, tokens):
        """Converts a sequence of tokens (string) in a single string."""
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
    def prepare_for_tokenization(self, text, is_split_into_words: bool = False, **kwargs): ...
    def get_decoder_prompt_ids(self, task: Incomplete | None = None, language: Incomplete | None = None, no_timestamps: bool = True): ...
