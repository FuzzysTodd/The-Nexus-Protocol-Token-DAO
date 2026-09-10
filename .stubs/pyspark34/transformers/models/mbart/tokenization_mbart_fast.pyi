from ...tokenization_utils import AddedToken as AddedToken, BatchEncoding as BatchEncoding
from ...tokenization_utils_fast import PreTrainedTokenizerFast as PreTrainedTokenizerFast
from ...utils import is_sentencepiece_available as is_sentencepiece_available, logging as logging
from .tokenization_mbart import MBartTokenizer as MBartTokenizer
from _typeshed import Incomplete
from typing import List, Optional, Tuple

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete
FAIRSEQ_LANGUAGE_CODES: Incomplete

class MBartTokenizerFast(PreTrainedTokenizerFast):
    '''
    Construct a "fast" MBART tokenizer (backed by HuggingFace\'s *tokenizers* library). Based on
    [BPE](https://huggingface.co/docs/tokenizers/python/latest/components.html?highlight=BPE#models).

    This tokenizer inherits from [`PreTrainedTokenizerFast`] which contains most of the main methods. Users should
    refer to this superclass for more information regarding those methods.

    The tokenization method is `<tokens> <eos> <language code>` for source language documents, and `<language code>
    <tokens> <eos>` for target language documents.

    Examples:

    ```python
    >>> from transformers import MBartTokenizerFast

    >>> tokenizer = MBartTokenizerFast.from_pretrained(
    ...     "facebook/mbart-large-en-ro", src_lang="en_XX", tgt_lang="ro_RO"
    ... )
    >>> example_english_phrase = " UN Chief Says There Is No Military Solution in Syria"
    >>> expected_translation_romanian = "Şeful ONU declară că nu există o soluţie militară în Siria"
    >>> inputs = tokenizer(example_english_phrase, text_target=expected_translation_romanian, return_tensors="pt")
    ```'''
    vocab_files_names = VOCAB_FILES_NAMES
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    model_input_names: Incomplete
    slow_tokenizer_class = MBartTokenizer
    prefix_tokens: List[int]
    suffix_tokens: List[int]
    vocab_file: Incomplete
    can_save_slow_tokenizer: Incomplete
    lang_code_to_id: Incomplete
    cur_lang_code: Incomplete
    tgt_lang: Incomplete
    def __init__(self, vocab_file: Incomplete | None = None, tokenizer_file: Incomplete | None = None, bos_token: str = '<s>', eos_token: str = '</s>', sep_token: str = '</s>', cls_token: str = '<s>', unk_token: str = '<unk>', pad_token: str = '<pad>', mask_token: str = '<mask>', src_lang: Incomplete | None = None, tgt_lang: Incomplete | None = None, additional_special_tokens: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def src_lang(self) -> str: ...
    @src_lang.setter
    def src_lang(self, new_src_lang: str) -> None: ...
    def build_inputs_with_special_tokens(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None) -> List[int]:
        """
        Build model inputs from a sequence or a pair of sequence for sequence classification tasks by concatenating and
        adding special tokens. The special tokens depend on calling set_lang.

        An MBART sequence has the following format, where `X` represents the sequence:

        - `input_ids` (for encoder) `X [eos, src_lang_code]`
        - `decoder_input_ids`: (for decoder) `X [eos, tgt_lang_code]`

        BOS is never used. Pairs of sequences are not the expected use case, but they will be handled without a
        separator.

        Args:
            token_ids_0 (`List[int]`):
                List of IDs to which the special tokens will be added.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.

        Returns:
            `List[int]`: list of [input IDs](../glossary#input-ids) with the appropriate special tokens.
        """
    def create_token_type_ids_from_sequences(self, token_ids_0: List[int], token_ids_1: Optional[List[int]] = None) -> List[int]:
        """
        Create a mask from the two sequences passed to be used in a sequence-pair classification task. mBART does not
        make use of token type ids, therefore a list of zeros is returned.

        Args:
            token_ids_0 (`List[int]`):
                List of IDs.
            token_ids_1 (`List[int]`, *optional*):
                Optional second list of IDs for sequence pairs.

        Returns:
            `List[int]`: List of zeros.

        """
    def prepare_seq2seq_batch(self, src_texts: List[str], src_lang: str = 'en_XX', tgt_texts: Optional[List[str]] = None, tgt_lang: str = 'ro_RO', **kwargs) -> BatchEncoding: ...
    def set_src_lang_special_tokens(self, src_lang) -> None:
        """Reset the special tokens to the source lang setting. No prefix and suffix=[eos, src_lang_code]."""
    def set_tgt_lang_special_tokens(self, lang: str) -> None:
        """Reset the special tokens to the target language setting. No prefix and suffix=[eos, tgt_lang_code]."""
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
