from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...onnx import OnnxConfig as OnnxConfig
from ...utils import logging as logging
from ..auto import CONFIG_MAPPING as CONFIG_MAPPING
from _typeshed import Incomplete
from typing import Mapping

logger: Incomplete
CONDITIONAL_DETR_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class ConditionalDetrConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`ConditionalDetrModel`]. It is used to instantiate
    a Conditional DETR model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the Conditional DETR
    [microsoft/conditional-detr-resnet-50](https://huggingface.co/microsoft/conditional-detr-resnet-50) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        use_timm_backbone (`bool`, *optional*, defaults to `True`):
            Whether or not to use the `timm` library for the backbone. If set to `False`, will use the [`AutoBackbone`]
            API.
        backbone_config (`PretrainedConfig` or `dict`, *optional*):
            The configuration of the backbone model. Only used in case `use_timm_backbone` is set to `False` in which
            case it will default to `ResNetConfig()`.
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        num_queries (`int`, *optional*, defaults to 100):
            Number of object queries, i.e. detection slots. This is the maximal number of objects
            [`ConditionalDetrModel`] can detect in a single image. For COCO, we recommend 100 queries.
        d_model (`int`, *optional*, defaults to 256):
            Dimension of the layers.
        encoder_layers (`int`, *optional*, defaults to 6):
            Number of encoder layers.
        decoder_layers (`int`, *optional*, defaults to 6):
            Number of decoder layers.
        encoder_attention_heads (`int`, *optional*, defaults to 8):
            Number of attention heads for each attention layer in the Transformer encoder.
        decoder_attention_heads (`int`, *optional*, defaults to 8):
            Number of attention heads for each attention layer in the Transformer decoder.
        decoder_ffn_dim (`int`, *optional*, defaults to 2048):
            Dimension of the "intermediate" (often named feed-forward) layer in decoder.
        encoder_ffn_dim (`int`, *optional*, defaults to 2048):
            Dimension of the "intermediate" (often named feed-forward) layer in decoder.
        activation_function (`str` or `function`, *optional*, defaults to `"relu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        activation_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for activations inside the fully connected layer.
        init_std (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        init_xavier_std (`float`, *optional*, defaults to 1):
            The scaling factor used for the Xavier initialization gain in the HM Attention map module.
        encoder_layerdrop (`float`, *optional*, defaults to 0.0):
            The LayerDrop probability for the encoder. See the [LayerDrop paper](see https://arxiv.org/abs/1909.11556)
            for more details.
        decoder_layerdrop (`float`, *optional*, defaults to 0.0):
            The LayerDrop probability for the decoder. See the [LayerDrop paper](see https://arxiv.org/abs/1909.11556)
            for more details.
        auxiliary_loss (`bool`, *optional*, defaults to `False`):
            Whether auxiliary decoding losses (loss at each decoder layer) are to be used.
        position_embedding_type (`str`, *optional*, defaults to `"sine"`):
            Type of position embeddings to be used on top of the image features. One of `"sine"` or `"learned"`.
        backbone (`str`, *optional*, defaults to `"resnet50"`):
            Name of convolutional backbone to use in case `use_timm_backbone` = `True`. Supports any convolutional
            backbone from the timm package. For a list of all available models, see [this
            page](https://rwightman.github.io/pytorch-image-models/#load-a-pretrained-model).
        use_pretrained_backbone (`bool`, *optional*, defaults to `True`):
            Whether to use pretrained weights for the backbone. Only supported when `use_timm_backbone` = `True`.
        dilation (`bool`, *optional*, defaults to `False`):
            Whether to replace stride with dilation in the last convolutional block (DC5). Only supported when
            `use_timm_backbone` = `True`.
        class_cost (`float`, *optional*, defaults to 1):
            Relative weight of the classification error in the Hungarian matching cost.
        bbox_cost (`float`, *optional*, defaults to 5):
            Relative weight of the L1 error of the bounding box coordinates in the Hungarian matching cost.
        giou_cost (`float`, *optional*, defaults to 2):
            Relative weight of the generalized IoU loss of the bounding box in the Hungarian matching cost.
        mask_loss_coefficient (`float`, *optional*, defaults to 1):
            Relative weight of the Focal loss in the panoptic segmentation loss.
        dice_loss_coefficient (`float`, *optional*, defaults to 1):
            Relative weight of the DICE/F-1 loss in the panoptic segmentation loss.
        bbox_loss_coefficient (`float`, *optional*, defaults to 5):
            Relative weight of the L1 bounding box loss in the object detection loss.
        giou_loss_coefficient (`float`, *optional*, defaults to 2):
            Relative weight of the generalized IoU loss in the object detection loss.
        eos_coefficient (`float`, *optional*, defaults to 0.1):
            Relative classification weight of the \'no-object\' class in the object detection loss.
        focal_alpha (`float`, *optional*, defaults to 0.25):
            Alpha parameter in the focal loss.

    Examples:

    ```python
    >>> from transformers import ConditionalDetrConfig, ConditionalDetrModel

    >>> # Initializing a Conditional DETR microsoft/conditional-detr-resnet-50 style configuration
    >>> configuration = ConditionalDetrConfig()

    >>> # Initializing a model (with random weights) from the microsoft/conditional-detr-resnet-50 style configuration
    >>> model = ConditionalDetrModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    keys_to_ignore_at_inference: Incomplete
    attribute_map: Incomplete
    use_timm_backbone: Incomplete
    backbone_config: Incomplete
    num_channels: Incomplete
    num_queries: Incomplete
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
    init_xavier_std: Incomplete
    encoder_layerdrop: Incomplete
    decoder_layerdrop: Incomplete
    num_hidden_layers: Incomplete
    scale_embedding: Incomplete
    auxiliary_loss: Incomplete
    position_embedding_type: Incomplete
    backbone: Incomplete
    use_pretrained_backbone: Incomplete
    dilation: Incomplete
    class_cost: Incomplete
    bbox_cost: Incomplete
    giou_cost: Incomplete
    mask_loss_coefficient: Incomplete
    dice_loss_coefficient: Incomplete
    cls_loss_coefficient: Incomplete
    bbox_loss_coefficient: Incomplete
    giou_loss_coefficient: Incomplete
    focal_alpha: Incomplete
    def __init__(self, use_timm_backbone: bool = True, backbone_config: Incomplete | None = None, num_channels: int = 3, num_queries: int = 300, encoder_layers: int = 6, encoder_ffn_dim: int = 2048, encoder_attention_heads: int = 8, decoder_layers: int = 6, decoder_ffn_dim: int = 2048, decoder_attention_heads: int = 8, encoder_layerdrop: float = 0.0, decoder_layerdrop: float = 0.0, is_encoder_decoder: bool = True, activation_function: str = 'relu', d_model: int = 256, dropout: float = 0.1, attention_dropout: float = 0.0, activation_dropout: float = 0.0, init_std: float = 0.02, init_xavier_std: float = 1.0, classifier_dropout: float = 0.0, scale_embedding: bool = False, auxiliary_loss: bool = False, position_embedding_type: str = 'sine', backbone: str = 'resnet50', use_pretrained_backbone: bool = True, dilation: bool = False, class_cost: int = 2, bbox_cost: int = 5, giou_cost: int = 2, mask_loss_coefficient: int = 1, dice_loss_coefficient: int = 1, cls_loss_coefficient: int = 2, bbox_loss_coefficient: int = 5, giou_loss_coefficient: int = 2, focal_alpha: float = 0.25, **kwargs) -> None: ...
    @property
    def num_attention_heads(self) -> int: ...
    @property
    def hidden_size(self) -> int: ...

class ConditionalDetrOnnxConfig(OnnxConfig):
    torch_onnx_minimum_version: Incomplete
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def atol_for_validation(self) -> float: ...
    @property
    def default_onnx_opset(self) -> int: ...
