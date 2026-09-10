from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...onnx import OnnxSeq2SeqConfigWithPast as OnnxSeq2SeqConfigWithPast
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Mapping

logger: Incomplete

class MT5Config(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`MT5Model`] or a [`TFMT5Model`]. It is used to
    instantiate a mT5 model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the mT5
    [google/mt5-small](https://huggingface.co/google/mt5-small) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Arguments:
        vocab_size (`int`, *optional*, defaults to 250112):
            Vocabulary size of the T5 model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`T5Model`] or [`TFT5Model`].
        d_model (`int`, *optional*, defaults to 512):
            Size of the encoder layers and the pooler layer.
        d_kv (`int`, *optional*, defaults to 64):
            Size of the key, query, value projections per attention head. `d_kv` has to be equal to `d_model //
            num_heads`.
        d_ff (`int`, *optional*, defaults to 1024):
            Size of the intermediate feed forward layer in each `T5Block`.
        num_layers (`int`, *optional*, defaults to 8):
            Number of hidden layers in the Transformer encoder.
        num_decoder_layers (`int`, *optional*):
            Number of hidden layers in the Transformer decoder. Will use the same value as `num_layers` if not set.
        num_heads (`int`, *optional*, defaults to 6):
            Number of attention heads for each attention layer in the Transformer encoder.
        relative_attention_num_buckets (`int`, *optional*, defaults to 32):
            The number of buckets to use for each attention layer.
        relative_attention_max_distance (`int`, *optional*, defaults to 128):
            The maximum distance of the longer sequences for the bucket separation.
        dropout_rate (`float`, *optional*, defaults to 0.1):
            The ratio for all dropout layers.
        layer_norm_eps (`float`, *optional*, defaults to 1e-6):
            The epsilon used by the layer normalization layers.
        initializer_factor (`float`, *optional*, defaults to 1):
            A factor for initializing all weight matrices (should be kept to 1, used internally for initialization
            testing).
        feed_forward_proj (`string`, *optional*, defaults to `"gated-gelu"`):
            Type of feed forward layer to be used. Should be one of `"relu"` or `"gated-gelu"`.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models).
    '''
    model_type: str
    keys_to_ignore_at_inference: Incomplete
    vocab_size: Incomplete
    d_model: Incomplete
    d_kv: Incomplete
    d_ff: Incomplete
    num_layers: Incomplete
    num_decoder_layers: Incomplete
    num_heads: Incomplete
    relative_attention_num_buckets: Incomplete
    relative_attention_max_distance: Incomplete
    dropout_rate: Incomplete
    layer_norm_epsilon: Incomplete
    initializer_factor: Incomplete
    feed_forward_proj: Incomplete
    use_cache: Incomplete
    dense_act_fn: Incomplete
    is_gated_act: Incomplete
    def __init__(self, vocab_size: int = 250112, d_model: int = 512, d_kv: int = 64, d_ff: int = 1024, num_layers: int = 8, num_decoder_layers: Incomplete | None = None, num_heads: int = 6, relative_attention_num_buckets: int = 32, relative_attention_max_distance: int = 128, dropout_rate: float = 0.1, layer_norm_epsilon: float = 1e-06, initializer_factor: float = 1.0, feed_forward_proj: str = 'gated-gelu', is_encoder_decoder: bool = True, use_cache: bool = True, tokenizer_class: str = 'T5Tokenizer', tie_word_embeddings: bool = False, pad_token_id: int = 0, eos_token_id: int = 1, decoder_start_token_id: int = 0, **kwargs) -> None: ...
    @property
    def hidden_size(self): ...
    @property
    def num_attention_heads(self): ...
    @property
    def num_hidden_layers(self): ...

class MT5OnnxConfig(OnnxSeq2SeqConfigWithPast):
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def default_onnx_opset(self) -> int: ...
    @property
    def atol_for_validation(self) -> float: ...
