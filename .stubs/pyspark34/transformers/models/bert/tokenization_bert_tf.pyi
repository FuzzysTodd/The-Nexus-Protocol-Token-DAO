import os
import tensorflow as tf
from .tokenization_bert import BertTokenizer as BertTokenizer
from _typeshed import Incomplete
from typing import List, Union

class TFBertTokenizer(tf.keras.layers.Layer):
    '''
    This is an in-graph tokenizer for BERT. It should be initialized similarly to other tokenizers, using the
    `from_pretrained()` method. It can also be initialized with the `from_tokenizer()` method, which imports settings
    from an existing standard tokenizer object.

    In-graph tokenizers, unlike other Hugging Face tokenizers, are actually Keras layers and are designed to be run
    when the model is called, rather than during preprocessing. As a result, they have somewhat more limited options
    than standard tokenizer classes. They are most useful when you want to create an end-to-end model that goes
    straight from `tf.string` inputs to outputs.

    Args:
        vocab_list (`list`):
            List containing the vocabulary.
        do_lower_case (`bool`, *optional*, defaults to `True`):
            Whether or not to lowercase the input when tokenizing.
        cls_token_id (`str`, *optional*, defaults to `"[CLS]"`):
            The classifier token which is used when doing sequence classification (classification of the whole sequence
            instead of per-token classification). It is the first token of the sequence when built with special tokens.
        sep_token_id (`str`, *optional*, defaults to `"[SEP]"`):
            The separator token, which is used when building a sequence from multiple sequences, e.g. two sequences for
            sequence classification or for a text and a question for question answering. It is also used as the last
            token of a sequence built with special tokens.
        pad_token_id (`str`, *optional*, defaults to `"[PAD]"`):
            The token used for padding, for example when batching sequences of different lengths.
        padding (`str`, defaults to `"longest"`):
            The type of padding to use. Can be either `"longest"`, to pad only up to the longest sample in the batch,
            or `"max_length", to pad all inputs to the maximum length supported by the tokenizer.
        truncation (`bool`, *optional*, defaults to `True`):
            Whether to truncate the sequence to the maximum length.
        max_length (`int`, *optional*, defaults to `512`):
            The maximum length of the sequence, used for padding (if `padding` is "max_length") and/or truncation (if
            `truncation` is `True`).
        pad_to_multiple_of (`int`, *optional*, defaults to `None`):
            If set, the sequence will be padded to a multiple of this value.
        return_token_type_ids (`bool`, *optional*, defaults to `True`):
            Whether to return token_type_ids.
        return_attention_mask (`bool`, *optional*, defaults to `True`):
            Whether to return the attention_mask.
        use_fast_bert_tokenizer (`bool`, *optional*, defaults to `True`):
            If set to false will use standard TF Text BertTokenizer, making it servable by TF Serving.
    '''
    tf_tokenizer: Incomplete
    vocab_list: Incomplete
    do_lower_case: Incomplete
    cls_token_id: Incomplete
    sep_token_id: Incomplete
    pad_token_id: Incomplete
    paired_trimmer: Incomplete
    max_length: Incomplete
    padding: Incomplete
    truncation: Incomplete
    pad_to_multiple_of: Incomplete
    return_token_type_ids: Incomplete
    return_attention_mask: Incomplete
    def __init__(self, vocab_list: List, do_lower_case: bool, cls_token_id: int = None, sep_token_id: int = None, pad_token_id: int = None, padding: str = 'longest', truncation: bool = True, max_length: int = 512, pad_to_multiple_of: int = None, return_token_type_ids: bool = True, return_attention_mask: bool = True, use_fast_bert_tokenizer: bool = True) -> None: ...
    @classmethod
    def from_tokenizer(cls, tokenizer: PreTrainedTokenizerBase, **kwargs):
        '''
        Initialize a `TFBertTokenizer` from an existing `Tokenizer`.

        Args:
            tokenizer (`PreTrainedTokenizerBase`):
                The tokenizer to use to initialize the `TFBertTokenizer`.

        Examples:

        ```python
        from transformers import AutoTokenizer, TFBertTokenizer

        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        tf_tokenizer = TFBertTokenizer.from_tokenizer(tokenizer)
        ```
        '''
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], *init_inputs, **kwargs):
        '''
        Instantiate a `TFBertTokenizer` from a pre-trained tokenizer.

        Args:
            pretrained_model_name_or_path (`str` or `os.PathLike`):
                The name or path to the pre-trained tokenizer.

        Examples:

        ```python
        from transformers import TFBertTokenizer

        tf_tokenizer = TFBertTokenizer.from_pretrained("bert-base-uncased")
        ```
        '''
    def unpaired_tokenize(self, texts): ...
    def call(self, text, text_pair: Incomplete | None = None, padding: Incomplete | None = None, truncation: Incomplete | None = None, max_length: Incomplete | None = None, pad_to_multiple_of: Incomplete | None = None, return_token_type_ids: Incomplete | None = None, return_attention_mask: Incomplete | None = None): ...
    def get_config(self): ...
