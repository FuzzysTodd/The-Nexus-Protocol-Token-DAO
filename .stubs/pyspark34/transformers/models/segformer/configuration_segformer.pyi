from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...onnx import OnnxConfig as OnnxConfig
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Mapping

logger: Incomplete
SEGFORMER_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class SegformerConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`SegformerModel`]. It is used to instantiate an
    SegFormer model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the SegFormer
    [nvidia/segformer-b0-finetuned-ade-512-512](https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512)
    architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        num_encoder_blocks (`int`, *optional*, defaults to 4):
            The number of encoder blocks (i.e. stages in the Mix Transformer encoder).
        depths (`List[int]`, *optional*, defaults to [2, 2, 2, 2]):
            The number of layers in each encoder block.
        sr_ratios (`List[int]`, *optional*, defaults to [8, 4, 2, 1]):
            Sequence reduction ratios in each encoder block.
        hidden_sizes (`List[int]`, *optional*, defaults to [32, 64, 160, 256]):
            Dimension of each of the encoder blocks.
        patch_sizes (`List[int]`, *optional*, defaults to [7, 3, 3, 3]):
            Patch size before each encoder block.
        strides (`List[int]`, *optional*, defaults to [4, 2, 2, 2]):
            Stride before each encoder block.
        num_attention_heads (`List[int]`, *optional*, defaults to [1, 2, 5, 8]):
            Number of attention heads for each attention layer in each block of the Transformer encoder.
        mlp_ratios (`List[int]`, *optional*, defaults to [4, 4, 4, 4]):
            Ratio of the size of the hidden layer compared to the size of the input layer of the Mix FFNs in the
            encoder blocks.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        classifier_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability before the classification head.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        drop_path_rate (`float`, *optional*, defaults to 0.1):
            The dropout probability for stochastic depth, used in the blocks of the Transformer encoder.
        layer_norm_eps (`float`, *optional*, defaults to 1e-6):
            The epsilon used by the layer normalization layers.
        decoder_hidden_size (`int`, *optional*, defaults to 256):
            The dimension of the all-MLP decode head.
        semantic_loss_ignore_index (`int`, *optional*, defaults to 255):
            The index that is ignored by the loss function of the semantic segmentation model.

    Example:

    ```python
    >>> from transformers import SegformerModel, SegformerConfig

    >>> # Initializing a SegFormer nvidia/segformer-b0-finetuned-ade-512-512 style configuration
    >>> configuration = SegformerConfig()

    >>> # Initializing a model from the nvidia/segformer-b0-finetuned-ade-512-512 style configuration
    >>> model = SegformerModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    num_channels: Incomplete
    num_encoder_blocks: Incomplete
    depths: Incomplete
    sr_ratios: Incomplete
    hidden_sizes: Incomplete
    patch_sizes: Incomplete
    strides: Incomplete
    mlp_ratios: Incomplete
    num_attention_heads: Incomplete
    hidden_act: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    classifier_dropout_prob: Incomplete
    initializer_range: Incomplete
    drop_path_rate: Incomplete
    layer_norm_eps: Incomplete
    decoder_hidden_size: Incomplete
    reshape_last_stage: Incomplete
    semantic_loss_ignore_index: Incomplete
    def __init__(self, num_channels: int = 3, num_encoder_blocks: int = 4, depths=[2, 2, 2, 2], sr_ratios=[8, 4, 2, 1], hidden_sizes=[32, 64, 160, 256], patch_sizes=[7, 3, 3, 3], strides=[4, 2, 2, 2], num_attention_heads=[1, 2, 5, 8], mlp_ratios=[4, 4, 4, 4], hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.0, attention_probs_dropout_prob: float = 0.0, classifier_dropout_prob: float = 0.1, initializer_range: float = 0.02, drop_path_rate: float = 0.1, layer_norm_eps: float = 1e-06, decoder_hidden_size: int = 256, semantic_loss_ignore_index: int = 255, **kwargs) -> None: ...

class SegformerOnnxConfig(OnnxConfig):
    torch_onnx_minimum_version: Incomplete
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def atol_for_validation(self) -> float: ...
    @property
    def default_onnx_opset(self) -> int: ...
