from ... import PreTrainedTokenizer as PreTrainedTokenizer
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...onnx import OnnxConfig as OnnxConfig, OnnxConfigWithPast as OnnxConfigWithPast, OnnxSeq2SeqConfigWithPast as OnnxSeq2SeqConfigWithPast
from ...onnx.utils import compute_effective_axis_dimension as compute_effective_axis_dimension
from ...utils import TensorType as TensorType, is_torch_available as is_torch_available, logging as logging
from _typeshed import Incomplete
from typing import Any, Mapping, Optional

logger: Incomplete
BIGBIRD_PEGASUS_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class BigBirdPegasusConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`BigBirdPegasusModel`]. It is used to instantiate
    an BigBirdPegasus model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the BigBirdPegasus
    [google/bigbird-pegasus-large-arxiv](https://huggingface.co/google/bigbird-pegasus-large-arxiv) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 96103):
            Vocabulary size of the BigBirdPegasus model. Defines the number of different tokens that can be represented
            by the `inputs_ids` passed when calling [`BigBirdPegasusModel`].
        d_model (`int`, *optional*, defaults to 1024):
            Dimension of the layers and the pooler layer.
        encoder_layers (`int`, *optional*, defaults to 16):
            Number of encoder layers.
        decoder_layers (`int`, *optional*, defaults to 16):
            Number of decoder layers.
        encoder_attention_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer encoder.
        decoder_attention_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer decoder.
        decoder_ffn_dim (`int`, *optional*, defaults to 4096):
            Dimension of the "intermediate" (often named feed-forward) layer in decoder.
        encoder_ffn_dim (`int`, *optional*, defaults to 4096):
            Dimension of the "intermediate" (often named feed-forward) layer in decoder.
        activation_function (`str` or `function`, *optional*, defaults to `"gelu_new"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        activation_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for activations inside the fully connected layer.
        classifier_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for classifier.
        max_position_embeddings (`int`, *optional*, defaults to 4096):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 1024 or 2048 or 4096).
        init_std (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        encoder_layerdrop (`float`, *optional*, defaults to 0.0):
            The LayerDrop probability for the encoder. See the [LayerDrop paper](see https://arxiv.org/abs/1909.11556)
            for more details.
        decoder_layerdrop (`float`, *optional*, defaults to 0.0):
            The LayerDrop probability for the decoder. See the [LayerDrop paper](see https://arxiv.org/abs/1909.11556)
            for more details.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models).
        attention_type (`str`, *optional*, defaults to `"block_sparse"`)
            Whether to use block sparse attention (with n complexity) as introduced in paper or original attention
            layer (with n^2 complexity) in encoder. Possible values are `"original_full"` and `"block_sparse"`.
        use_bias (`bool`, *optional*, defaults to `False`)
            Whether to use bias in query, key, value.
        block_size (`int`, *optional*, defaults to 64)
            Size of each block. Useful only when `attention_type == "block_sparse"`.
        num_random_blocks (`int`, *optional*, defaults to 3)
            Each query is going to attend these many number of random blocks. Useful only when `attention_type ==
            "block_sparse"`.
        scale_embeddings (`bool`, *optional*, defaults to `True`)
            Whether to rescale embeddings with (hidden_size ** 0.5).

    Example:

    ```python
    >>> from transformers import BigBirdPegasusConfig, BigBirdPegasusModel

    >>> # Initializing a BigBirdPegasus bigbird-pegasus-base style configuration
    >>> configuration = BigBirdPegasusConfig()

    >>> # Initializing a model (with random weights) from the bigbird-pegasus-base style configuration
    >>> model = BigBirdPegasusModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    keys_to_ignore_at_inference: Incomplete
    attribute_map: Incomplete
    vocab_size: Incomplete
    max_position_embeddings: Incomplete
    d_model: Incomplete
    encoder_ffn_dim: Incomplete
    encoder_layers: Incomplete
    encoder_attention_heads: Incomplete
    decoder_ffn_dim: Incomplete
    decoder_layers: Incomplete
    decoder_attention_heads: Incomplete
    dropout: Incomplete
    attention_dropout: Incomplete
    activation_dropout: Incomplete
    activation_function: Incomplete
    init_std: Incomplete
    encoder_layerdrop: Incomplete
    decoder_layerdrop: Incomplete
    classifier_dropout: Incomplete
    use_cache: Incomplete
    num_hidden_layers: Incomplete
    scale_embedding: Incomplete
    attention_type: Incomplete
    block_size: Incomplete
    num_random_blocks: Incomplete
    use_bias: Incomplete
    def __init__(self, vocab_size: int = 96103, max_position_embeddings: int = 4096, encoder_layers: int = 16, encoder_ffn_dim: int = 4096, encoder_attention_heads: int = 16, decoder_layers: int = 16, decoder_ffn_dim: int = 4096, decoder_attention_heads: int = 16, encoder_layerdrop: float = 0.0, decoder_layerdrop: float = 0.0, use_cache: bool = True, is_encoder_decoder: bool = True, activation_function: str = 'gelu_new', d_model: int = 1024, dropout: float = 0.1, attention_dropout: float = 0.0, activation_dropout: float = 0.0, init_std: float = 0.02, decoder_start_token_id: int = 2, classifier_dropout: float = 0.0, scale_embedding: bool = True, pad_token_id: int = 0, bos_token_id: int = 2, eos_token_id: int = 1, attention_type: str = 'block_sparse', block_size: int = 64, num_random_blocks: int = 3, use_bias: bool = False, **kwargs) -> None: ...

class BigBirdPegasusOnnxConfig(OnnxSeq2SeqConfigWithPast):
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def outputs(self) -> Mapping[str, Mapping[int, str]]: ...
    def generate_dummy_inputs(self, tokenizer: PreTrainedTokenizer, batch_size: int = -1, seq_length: int = -1, is_pair: bool = False, framework: Optional[TensorType] = None) -> Mapping[str, Any]: ...
