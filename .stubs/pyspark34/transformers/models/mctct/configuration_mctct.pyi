from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
MCTCT_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class MCTCTConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`MCTCTModel`]. It is used to instantiate an
    M-CTC-T model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the M-CTC-T
    [speechbrain/m-ctc-t-large](https://huggingface.co/speechbrain/m-ctc-t-large) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 8065):
            Vocabulary size of the M-CTC-T model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`MCTCTModel`].
        hidden_size (`int`, *optional*, defaults to 1536):
            Dimension of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 36):
            Number of hidden layers in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 6144):
            Dimension of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 4):
            Number of attention heads for each attention layer in the Transformer encoder.
        attention_head_dim (`int`, *optional*, defaults to 384):
            Dimensions of each attention head for each attention layer in the Transformer encoder.
        max_position_embeddings (`int`, *optional*, defaults to 920):
            The maximum sequence length that this model might ever be used with (after log-mel spectrogram extraction).
        layer_norm_eps (`float`, *optional*, defaults to 1e-5):
            The epsilon used by the layer normalization layers.
        layerdrop (`float`, *optional*, defaults to 0.3):
            The probability of dropping an encoder layer during training. The default 0.3 value is used in the original
            implementation.
        hidden_act (`str` or `function`, *optional*, defaults to `"relu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probabilitiy for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        pad_token_id (`int`, *optional*, defaults to 1):
            The tokenizer index of the pad token.
        bos_token_id (`int`, *optional*, defaults to 0):
            The tokenizer index of the bos token.
        eos_token_id (`int`, *optional*, defaults to 2):
            The tokenizer index of the eos token.
        conv_glu_dim (`int`, *optional*, defaults to 1):
            The dimension of the output of the `Conv1dSubsampler` layer in which GLU is applied on. Though the original
            Flashlight code uses the value of 2, here it\'s adapted to 1 due to transposition differences.
        conv_dropout (`int`, *optional*, defaults to 0.3):
            The probability of randomly dropping the `Conv1dSubsampler` layer during training.
        num_conv_layers (`int`, *optional*, defaults to 1):
            Number of convolution layers before applying transformer encoder layers.
        conv_kernel (`List[int]`, *optional*, defaults to `[7]`):
            The kernel size of the 1D convolution applied before transformer layers. `len(conv_kernel)` must be equal
            to `num_conv_layers`.
        conv_stride (`List[int]`, *optional*, defaults to `[3]`):
            The stride length of the 1D convolution applied before transformer layers. `len(conv_stride)` must be equal
            to `num_conv_layers`.
        input_feat_per_channel (`int`, *optional*, defaults to 80):
            Feature dimensions of the channels of the input to the Conv1D layer.
        input_channels (`int`, *optional*, defaults to 1):
            Number of input channels of the input to the Conv1D layer.
        conv_channels (`List[int]`, *optional*, defaults to None):
            Channel sizes of intermediate Conv1D layers.
        ctc_loss_reduction (`str`, *optional*, defaults to `"sum"`):
            Specifies the reduction to apply to the output of `torch.nn.CTCLoss`. Only relevant when training an
            instance of [`MCTCTForCTC`].
        ctc_zero_infinity (`bool`, *optional*, defaults to `False`):
            Whether to zero infinite losses and the associated gradients of `torch.nn.CTCLoss`. Infinite losses mainly
            occur when the inputs are too short to be aligned to the targets. Only relevant when training an instance
            of [`MCTCTForCTC`].

    Example:

    ```python
    >>> from transformers import MCTCTConfig, MCTCTModel

    >>> # Initializing a M-CTC-T mctct-large style configuration
    >>> configuration = MCTCTConfig()

    >>> # Initializing a model (with random weights) from the mctct-large style configuration
    >>> model = MCTCTModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    vocab_size: Incomplete
    hidden_size: Incomplete
    num_hidden_layers: Incomplete
    intermediate_size: Incomplete
    num_attention_heads: Incomplete
    attention_head_dim: Incomplete
    max_position_embeddings: Incomplete
    layer_norm_eps: Incomplete
    layerdrop: Incomplete
    hidden_act: Incomplete
    initializer_range: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    pad_token_id: Incomplete
    bos_token_id: Incomplete
    eos_token_id: Incomplete
    conv_glu_dim: Incomplete
    conv_dropout: Incomplete
    num_conv_layers: Incomplete
    input_feat_per_channel: Incomplete
    input_channels: Incomplete
    conv_channels: Incomplete
    ctc_loss_reduction: Incomplete
    ctc_zero_infinity: Incomplete
    conv_kernel: Incomplete
    conv_stride: Incomplete
    def __init__(self, vocab_size: int = 8065, hidden_size: int = 1536, num_hidden_layers: int = 36, intermediate_size: int = 6144, num_attention_heads: int = 4, attention_head_dim: int = 384, max_position_embeddings: int = 920, layer_norm_eps: float = 1e-05, layerdrop: float = 0.3, hidden_act: str = 'relu', initializer_range: float = 0.02, hidden_dropout_prob: float = 0.3, attention_probs_dropout_prob: float = 0.3, pad_token_id: int = 1, bos_token_id: int = 0, eos_token_id: int = 2, conv_glu_dim: int = 1, conv_dropout: float = 0.3, num_conv_layers: int = 1, conv_kernel=(7,), conv_stride=(3,), input_feat_per_channel: int = 80, input_channels: int = 1, conv_channels: Incomplete | None = None, ctc_loss_reduction: str = 'sum', ctc_zero_infinity: bool = False, **kwargs) -> None: ...
