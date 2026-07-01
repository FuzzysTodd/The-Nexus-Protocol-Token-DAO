import os
import tensorflow as tf
from .tokenization_gpt2 import GPT2Tokenizer as GPT2Tokenizer
from _typeshed import Incomplete
from typing import Dict, List, Union

class TFGPT2Tokenizer(tf.keras.layers.Layer):
    """
    This is an in-graph tokenizer for GPT2. It should be initialized similarly to other tokenizers, using the
    `from_pretrained()` method. It can also be initialized with the `from_tokenizer()` method, which imports settings
    from an existing standard tokenizer object.

    In-graph tokenizers, unlike other Hugging Face tokenizers, are actually Keras layers and are designed to be run
    when the model is called, rather than during preprocessing. As a result, they have somewhat more limited options
    than standard tokenizer classes. They are most useful when you want to create an end-to-end model that goes
    straight from `tf.string` inputs to outputs.

    Args:
        vocab (Dict[str, int]): Vocabulary dict for Byte Pair Tokenizer
        merges (List[str]): Merges list for Byte Pair Tokenizer
    """
    pad_token_id: Incomplete
    max_length: Incomplete
    vocab: Incomplete
    merges: Incomplete
    tf_tokenizer: Incomplete
    def __init__(self, vocab: Dict[str, int], merges: List[str], max_length: int = None, pad_token_id: int = None) -> None: ...
    @classmethod
    def from_tokenizer(cls, tokenizer: GPT2Tokenizer, *args, **kwargs):
        '''Creates TFGPT2Tokenizer from GPT2Tokenizer

        Args:
            tokenizer (GPT2Tokenizer)

        Examples:

        ```python
        from transformers import AutoTokenizer, TFGPT2Tokenizer

        tokenizer = AutoTokenizer.from_pretrained("gpt2")
        tf_tokenizer = TFGPT2Tokenizer.from_tokenizer(tokenizer)
        ```
        '''
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], *init_inputs, **kwargs):
        '''Creates TFGPT2Tokenizer from pretrained GPT2Tokenizer

        Args:
            pretrained_model_name_or_path (Union[str, os.PathLike]): Path to pretrained model

        Examples:

        ```python
        from transformers import TFGPT2Tokenizer

        tf_tokenizer = TFGPT2Tokenizer.from_pretrained("gpt2")
        ```
        '''
    @classmethod
    def from_config(cls, config):
        """Creates TFGPT2Tokenizer from configurations

        Args:
            config (Dict): Dictionary with keys such as stated in `get_config`.
        """
    def get_config(self): ...
    def call(self, x, max_length: int = None): ...
