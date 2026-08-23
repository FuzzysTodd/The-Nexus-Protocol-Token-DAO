from ...tokenization_utils_fast import PreTrainedTokenizerFast as PreTrainedTokenizerFast
from ...utils import is_sentencepiece_available as is_sentencepiece_available, logging as logging
from .tokenization_reformer import ReformerTokenizer as ReformerTokenizer
from _typeshed import Incomplete
from typing import Optional, Tuple

logger: Incomplete
SPIECE_UNDERLINE: str
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete

class ReformerTokenizerFast(PreTrainedTokenizerFast):
    '''
    Construct a "fast" Reformer tokenizer (backed by HuggingFace\'s *tokenizers* library). Based on
    [Unigram](https://huggingface.co/docs/tokenizers/python/latest/components.html?highlight=unigram#models).

    This tokenizer inherits from [`PreTrainedTokenizerFast`] which contains most of the main methods. Users should
    refer to this superclass for more information regarding those methods.

    Args:
        vocab_file (`str`):
            [SentencePiece](https://github.com/google/sentencepiece) file (generally has a *.spm* extension) that
            contains the vocabulary necessary to instantiate a tokenizer.
        eos_token (`str`, *optional*, defaults to `"</s>"`):
            The end of sequence token.

            <Tip>

            When building a sequence using special tokens, this is not the token that is used for the end of sequence.
            The token used is the `sep_token`.

            </Tip>

        unk_token (`str`, *optional*, defaults to `"<unk>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        pad_token (`str`, *optional*, defaults to `"<pad>"`):
            The token used for padding, for example when batching sequences of different lengths.
        additional_special_tokens (`List[str]`, *optional*):
            Additional special tokens used by the tokenizer.
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    model_input_names: Incomplete
    slow_tokenizer_class = ReformerTokenizer
    vocab_file: Incomplete
    can_save_slow_tokenizer: Incomplete
    def __init__(self, vocab_file: Incomplete | None = None, tokenizer_file: Incomplete | None = None, eos_token: str = '</s>', unk_token: str = '<unk>', additional_special_tokens=[], **kwargs) -> None: ...
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
