from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
SWITCH_TRANSFORMERS_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class SwitchTransformersConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`SwitchTransformersModel`]. It is used to
    instantiate a SwitchTransformers model according to the specified arguments, defining the model architecture.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the
    SwitchTransformers [google/switch-base-8](https://huggingface.co/google/switch-base-8) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Arguments:
        vocab_size (`int`, *optional*, defaults to 32128):
            Vocabulary size of the SwitchTransformers model. Defines the number of different tokens that can be
            represented by the `inputs_ids` passed when calling [`SwitchTransformersModel`].
        d_model (`int`, *optional*, defaults to 512):
            Size of the encoder layers and the pooler layer.
        d_kv (`int`, *optional*, defaults to 64):
            Size of the key, query, value projections per attention head. `d_kv` has to be equal to `d_model //
            num_heads`.
        d_ff (`int`, *optional*, defaults to 2048):
            Size of the intermediate feed forward layer in each `SwitchTransformersBlock`.
        expert_capacity (`int`, *optional*, defaults to 64):
            Number of tokens that can be stored in each expert. If set to 1, the model will behave like a regular
            Transformer.
        num_layers (`int`, *optional*, defaults to 12):
            Number of dense hidden layers in the Transformer encoder layer.
        num_sparse_encoder_layers (`int`, *optional*, defaults to 6):
            Number of sparse (MoE) dense hidden layers in the Transformer encoder layer.
        num_decoder_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer decoder. Will use the same value as `num_layers` if not set.
        num_sparse_decoder_layers (`int`, *optional*, defaults to 12):
            Number of sparse (MoE) dense hidden layers in the Transformer decoder layer.
        num_heads (`int`, *optional*, defaults to 8):
            Number of attention heads for each attention layer in the Transformer encoder.
        num_experts (`int`, *optional*, defaults to 8):
            Number of experts for each SwitchTransformer layer.
        router_type (`str`, *optional*, defaults to `"tokens_masked"`):
            Router type - choose between `"tokens_masked", `"tokens_scatter"` and `"experts_masked"`.
        router_bias (`bool`, *optional*, defaults to `True`):
            Whether to add a bias to the router.
        router_jitter_noise (`float`, *optional*, defaults to 0.1):
            Amount of noise to add to the router.
        router_dtype (`str`, *optional*, default to `"float32"`):
            The `dtype` used for the routers. It is preferable to keep the `dtype` to `"float32"` as specified in the
            *selective precision* discussion in [the paper](https://arxiv.org/abs/2101.03961).
        router_ignore_padding_tokens (`bool`, *optional*, defaults to `False`):
            Whether to ignore padding tokens when routing.
        relative_attention_num_buckets (`int`, *optional*, defaults to 32):
            The number of buckets to use for each attention layer.
        relative_attention_max_distance (`int`, *optional*, defaults to 128):
            The maximum distance of the longer sequences for the bucket separation.
        dropout_rate (`float`, *optional*, defaults to 0.1):
            The ratio for all dropout layers.
        layer_norm_eps (`float`, *optional*, defaults to 1e-6):
            The epsilon used by the layer normalization layers.
        router_z_loss_coef (`float`, *optional*, defaults to 0.001):
            The z loss factor for the total loss.
        router_aux_loss_coef (`float`, *optional*, defaults to 0.001):
            The aux loss factor for the total loss.
        initializer_factor (`float`, *optional*, defaults to 1):
            A factor for initializing all weight matrices (should be kept to 1, used internally for initialization
            testing).
        feed_forward_proj (`string`, *optional*, defaults to `"relu"`):
            Type of feed forward layer to be used. Should be one of `"relu"` or `"gated-gelu"`. SwitchTransformersv1.1
            uses the `"gated-gelu"` feed forward projection. Original SwitchTransformers uses `"relu"`.
        add_router_probs (`bool`, *optional*, defaults to `False`):
            Whether to output router probabilities to compute router auxiliary loss.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models).
    '''
    model_type: str
    keys_to_ignore_at_inference: Incomplete
    attribute_map: Incomplete
    vocab_size: Incomplete
    d_model: Incomplete
    d_kv: Incomplete
    d_ff: Incomplete
    num_sparse_encoder_layers: Incomplete
    num_layers: Incomplete
    num_decoder_layers: Incomplete
    num_sparse_decoder_layers: Incomplete
    encoder_sparse_step: Incomplete
    decoder_sparse_step: Incomplete
    num_heads: Incomplete
    router_type: Incomplete
    num_experts: Incomplete
    expert_capacity: Incomplete
    router_bias: Incomplete
    router_jitter_noise: Incomplete
    router_dtype: Incomplete
    router_ignore_padding_tokens: Incomplete
    relative_attention_num_buckets: Incomplete
    relative_attention_max_distance: Incomplete
    dropout_rate: Incomplete
    layer_norm_epsilon: Incomplete
    initializer_factor: Incomplete
    feed_forward_proj: Incomplete
    use_cache: Incomplete
    add_router_probs: Incomplete
    router_z_loss_coef: Incomplete
    router_aux_loss_coef: Incomplete
    dense_act_fn: Incomplete
    is_gated_act: Incomplete
    def __init__(self, vocab_size: int = 32128, d_model: int = 768, d_kv: int = 64, d_ff: int = 2048, expert_capacity: int = 64, num_layers: int = 12, num_sparse_encoder_layers: int = 3, num_decoder_layers: int = 12, num_sparse_decoder_layers: int = 3, num_heads: int = 12, num_experts: int = 8, router_type: str = 'tokens_masked', router_bias: bool = False, router_jitter_noise: float = 0.01, router_dtype: str = 'float32', router_ignore_padding_tokens: bool = False, relative_attention_num_buckets: int = 32, relative_attention_max_distance: int = 128, dropout_rate: float = 0.1, layer_norm_epsilon: float = 1e-06, router_z_loss_coef: float = 0.001, router_aux_loss_coef: float = 0.001, initializer_factor: float = 1.0, feed_forward_proj: str = 'relu', is_encoder_decoder: bool = True, add_router_probs: bool = False, use_cache: bool = True, pad_token_id: int = 0, eos_token_id: int = 1, **kwargs) -> None: ...
