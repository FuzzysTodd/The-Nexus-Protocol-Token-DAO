from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
SPEECH_TO_TEXT_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class Speech2TextConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`Speech2TextModel`]. It is used to instantiate an
    Speech2Text model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the Speech2Text
    [facebook/s2t-small-librispeech-asr](https://huggingface.co/facebook/s2t-small-librispeech-asr) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 50265):
            Vocabulary size of the Speech2Text model. Defines the number of different tokens that can be represented by
            the `inputs_ids` passed when calling [`Speech2TextModel`]
        d_model (`int`, *optional*, defaults to 1024):
            Dimensionality of the layers and the pooler layer.
        encoder_layers (`int`, *optional*, defaults to 12):
            Number of encoder layers.
        decoder_layers (`int`, *optional*, defaults to 12):
            Number of decoder layers.
        encoder_attention_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer encoder.
        decoder_attention_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer decoder.
        decoder_ffn_dim (`int`, *optional*, defaults to 4096):
            Dimensionality of the "intermediate" (often named feed-forward) layer in decoder.
        encoder_ffn_dim (`int`, *optional*, defaults to 4096):
            Dimensionality of the "intermediate" (often named feed-forward) layer in decoder.
        activation_function (`str` or `function`, *optional*, defaults to `"gelu"`):
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
        max_source_positions (`int`, *optional*, defaults to 6000):
            The maximum sequence length of log-mel filter-bank features that this model might ever be used with.
        max_target_positions (`int`, *optional*, defaults to 1024):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        num_conv_layers (`int`, *optional*, defaults to 2):
            Number of 1D convolutional layers in the conv module.
        conv_kernel_sizes (`Tuple[int]`, *optional*, defaults to `(5, 5)`):
            A tuple of integers defining the kernel size of each 1D convolutional layer in the conv module. The length
            of `conv_kernel_sizes` has to match `num_conv_layers`.
        conv_channels (`int`, *optional*, defaults to 1024):
            An integer defining the number of output channels of each convolution layers except the final one in the
            conv module.
        input_feat_per_channel (`int`, *optional*, defaults to 80):
            An integer specifying the size of feature vector. This is also the dimensions of log-mel filter-bank
            features.
        input_channels (`int`, *optional*, defaults to 1):
            An integer specifying number of input channels of the input feature vector.

    Example:

    ```python
    >>> from transformers import Speech2TextConfig, Speech2TextModel

    >>> # Initializing a Speech2Text s2t_transformer_s style configuration
    >>> configuration = Speech2TextConfig()

    >>> # Initializing a model (with random weights) from the s2t_transformer_s style configuration
    >>> model = Speech2TextModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    keys_to_ignore_at_inference: Incomplete
    attribute_map: Incomplete
    vocab_size: Incomplete
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
    max_source_positions: Incomplete
    max_target_positions: Incomplete
    num_conv_layers: Incomplete
    conv_kernel_sizes: Incomplete
    conv_channels: Incomplete
    input_feat_per_channel: Incomplete
    input_channels: Incomplete
    def __init__(self, vocab_size: int = 10000, encoder_layers: int = 12, encoder_ffn_dim: int = 2048, encoder_attention_heads: int = 4, decoder_layers: int = 6, decoder_ffn_dim: int = 2048, decoder_attention_heads: int = 4, encoder_layerdrop: float = 0.0, decoder_layerdrop: float = 0.0, use_cache: bool = True, is_encoder_decoder: bool = True, activation_function: str = 'relu', d_model: int = 256, dropout: float = 0.1, attention_dropout: float = 0.0, activation_dropout: float = 0.0, init_std: float = 0.02, decoder_start_token_id: int = 2, classifier_dropout: float = 0.0, scale_embedding: bool = True, pad_token_id: int = 1, bos_token_id: int = 0, eos_token_id: int = 2, max_source_positions: int = 6000, max_target_positions: int = 1024, num_conv_layers: int = 2, conv_kernel_sizes=(5, 5), conv_channels: int = 1024, input_feat_per_channel: int = 80, input_channels: int = 1, **kwargs) -> None: ...
