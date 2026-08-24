from ...tokenization_utils_base import AddedToken as AddedToken, BatchEncoding as BatchEncoding, EncodedInput as EncodedInput
from ...tokenization_utils_fast import PreTrainedTokenizerFast as PreTrainedTokenizerFast
from ...utils import PaddingStrategy as PaddingStrategy, logging as logging
from .tokenization_led import LEDTokenizer as LEDTokenizer
from _typeshed import Incomplete
from typing import List, Optional, Tuple

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete

class LEDTokenizerFast(PreTrainedTokenizerFast):
    '''
    Construct a "fast" LED tokenizer (backed by HuggingFace\'s *tokenizers* library), derived from the GPT-2 tokenizer,
    using byte-level Byte-Pair-Encoding.

    This tokenizer has been trained to treat spaces like parts of the tokens (a bit like sentencepiece) so a word will
    be encoded differently whether it is at the beginning of the sentence (without space) or not:

    ```
    >>> from transformers import LEDTokenizerFast
    >>> tokenizer = LEDTokenizerFast.from_pretrained("allenai/led-base-16384")
    >>> tokenizer("Hello world")[\'input_ids\']
    [0, 31414, 232, 2]
    >>> tokenizer(" Hello world")[\'input_ids\']
    [0, 20920, 232, 2]
    ```

    You can get around that behavior by passing `add_prefix_space=True` when instantiating this tokenizer or when you
    call it on some text, but since the model was not pretrained this way, it might yield a decrease in performance.

    <Tip>

    When used with `is_split_into_words=True`, this tokenizer needs to be instantiated with `add_prefix_space=True`.

    </Tip>

    This tokenizer inherits from [`PreTrainedTokenizerFast`] which contains most of the main methods. Users should
    refer to this superclass for more information regarding those methods.

    Args:
        vocab_file (`str`):
            Path to the vocabulary file.
        merges_file (`str`):
            Path to the merges file.
        errors (`str`, *optional*, defaults to `"replace"`):
            Paradigm to follow when decoding bytes to UTF-8. See
            [bytes.decode](https://docs.python.org/3/library/stdtypes.html#bytes.decode) for more information.
        bos_token (`str`, *optional*, defaults to `"<s>"`):
            The beginning of sequence token that was used during pretraining. Can be used a sequence classifier token.

            <Tip>

            When building a sequence using special tokens, this is not the token that is used for the beginning of
            sequence. The token used is the `cls_token`.

            </Tip>

        eos_token (`str`, *optional*, defaults to `"</s>"`):
            The end of sequence token.

            <Tip>

            When building a sequence using special tokens, this is not the token that is used for the end of sequence.
            The token used is the `sep_token`.

            </Tip>

        sep_token (`str`, *optional*, defaults to `"</s>"`):
            The separator token, which is used when building a sequence from multiple sequences, e.g. two sequences for
            sequence classification or for a text and a question for question answering. It is also used as the last
            token of a sequence built with special tokens.
        cls_token (`str`, *optional*, defaults to `"<s>"`):
            The classifier token which is used when doing sequence classification (classification of the whole sequence
            instead of per-token classification). It is the first token of the sequence when built with special tokens.
        unk_token (`str`, *optional*, defaults to `"<unk>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        pad_token (`str`, *optional*, defaults to `"<pad>"`):
            The token used for padding, for example when batching sequences of different lengths.
        mask_token (`str`, *optional*, defaults to `"<mask>"`):
            The token used for masking values. This is the token used when training this model with masked language
            modeling. This is the token which the model will try to predict.
        add_prefix_space (`bool`, *optional*, defaults to `False`):
            Whether or not to add an initial space to the input. This allows to treat the leading word just as any
            other word. (LED tokenizer detect beginning of words by the preceding space).
        trim_offsets (`bool`, *optional*, defaults to `True`):
            Whether the post processing step should trim offsets to avoid including whitespaces.
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    slow_tokenizer_class = LEDTokenizer
    model_input_names: Incomplete
    add_prefix_space: Incomplete
    def __init__(self, vocab_file: Incomplete | None = None, merges_file: Incomplete | None = None, tokenizer_file: Incomplete | None = None, errors: str = 'replace', bos_token: str = '<s>', eos_token: str = '</s>', sep_token: str = '</s>', cls_token: str = '<s>', unk_token: str = '<unk>', pad_token: str = '<pad>', mask_token: str = '<mask>', add_prefix_space: bool = False, trim_offsets: bool = True, **kwargs) -> None: ...
    @property
    def mask_token(self) -> str:
        """
        `str`: Mask token, to use when training a model with masked-language modeling. Log an error if used while not
        having been set.

        LED tokenizer has a special mask token to be usable in the fill-mask pipeline. The mask token will greedily
        comprise the space before the *<mask>*.
        """
    @mask_token.setter
    def mask_token(self, value) -> None:
        """
        Overriding the default behavior of the mask token to have it eat the space before it.

        This is needed to preserve backward compatibility with all the previously used models based on LED.
        """
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
    def build_inputs_with_special_tokens(self, token_ids_0, token_ids_1: Incomplete | None = None): ...
    def create_token_type_ids_from_sequences(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None) -> List[int]:
        """
        Create a mask from the two sequences passed to be used in a sequence-pair classification task. LED does not
        make use of token type ids, therefore a list of zeros is returned.

        Args:
            token_ids_0 (`List[int]`):
                List of IDs.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.

        Returns:
            `List[int]`: List of zeros.
        """
