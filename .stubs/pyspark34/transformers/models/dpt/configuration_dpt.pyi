from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from ..bit import BitConfig as BitConfig
from _typeshed import Incomplete

logger: Incomplete
DPT_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class DPTConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`DPTModel`]. It is used to instantiate an DPT
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the DPT
    [Intel/dpt-large](https://huggingface.co/Intel/dpt-large) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probabilitiy for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        image_size (`int`, *optional*, defaults to 384):
            The size (resolution) of each image.
        patch_size (`int`, *optional*, defaults to 16):
            The size (resolution) of each patch.
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        qkv_bias (`bool`, *optional*, defaults to `True`):
            Whether to add a bias to the queries, keys and values.
        backbone_out_indices (`List[int]`, *optional*, defaults to `[2, 5, 8, 11]`):
            Indices of the intermediate hidden states to use from backbone.
        readout_type (`str`, *optional*, defaults to `"project"`):
            The readout type to use when processing the readout token (CLS token) of the intermediate hidden states of
            the ViT backbone. Can be one of [`"ignore"`, `"add"`, `"project"`].

            - "ignore" simply ignores the CLS token.
            - "add" passes the information from the CLS token to all other tokens by adding the representations.
            - "project" passes information to the other tokens by concatenating the readout to all other tokens before
              projecting the
            representation to the original feature dimension D using a linear layer followed by a GELU non-linearity.
        is_hybrid (`bool`, *optional*, defaults to `False`):
            Whether to use a hybrid backbone. Useful in the context of loading DPT-Hybrid models.
        reassemble_factors (`List[int]`, *optional*, defaults to `[4, 2, 1, 0.5]`):
            The up/downsampling factors of the reassemble layers.
        neck_hidden_sizes (`List[str]`, *optional*, defaults to [96, 192, 384, 768]):
            The hidden sizes to project to for the feature maps of the backbone.
        fusion_hidden_size (`int`, *optional*, defaults to 256):
            The number of channels before fusion.
        head_in_index (`int`, *optional*, defaults to -1):
            The index of the features to use in the heads.
        use_batch_norm_in_fusion_residual (`bool`, *optional*, defaults to `False`):
            Whether to use batch normalization in the pre-activate residual units of the fusion blocks.
        use_auxiliary_head (`bool`, *optional*, defaults to `True`):
            Whether to use an auxiliary head during training.
        auxiliary_loss_weight (`float`, *optional*, defaults to 0.4):
            Weight of the cross-entropy loss of the auxiliary head.
        semantic_loss_ignore_index (`int`, *optional*, defaults to 255):
            The index that is ignored by the loss function of the semantic segmentation model.
        semantic_classifier_dropout (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the semantic classification head.
        backbone_featmap_shape (`List[int]`, *optional*, defaults to `[1, 1024, 24, 24]`):
            Used only for the `hybrid` embedding type. The shape of the feature maps of the backbone.
        neck_ignore_stages (`List[int]`, *optional*, defaults to `[0, 1]`):
            Used only for the `hybrid` embedding type. The stages of the readout layers to ignore.
        backbone_config (`Union[Dict[str, Any], PretrainedConfig]`, *optional*):
            Used only for the `hybrid` embedding type. The configuration of the backbone in a dictionary.

    Example:

    ```python
    >>> from transformers import DPTModel, DPTConfig

    >>> # Initializing a DPT dpt-large style configuration
    >>> configuration = DPTConfig()

    >>> # Initializing a model from the dpt-large style configuration
    >>> model = DPTModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    hidden_size: Incomplete
    is_hybrid: Incomplete
    backbone_config: Incomplete
    backbone_featmap_shape: Incomplete
    neck_ignore_stages: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    intermediate_size: Incomplete
    hidden_act: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    initializer_range: Incomplete
    layer_norm_eps: Incomplete
    image_size: Incomplete
    patch_size: Incomplete
    num_channels: Incomplete
    qkv_bias: Incomplete
    backbone_out_indices: Incomplete
    readout_type: Incomplete
    reassemble_factors: Incomplete
    neck_hidden_sizes: Incomplete
    fusion_hidden_size: Incomplete
    head_in_index: Incomplete
    use_batch_norm_in_fusion_residual: Incomplete
    use_auxiliary_head: Incomplete
    auxiliary_loss_weight: Incomplete
    semantic_loss_ignore_index: Incomplete
    semantic_classifier_dropout: Incomplete
    def __init__(self, hidden_size: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 12, intermediate_size: int = 3072, hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.0, attention_probs_dropout_prob: float = 0.0, initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, image_size: int = 384, patch_size: int = 16, num_channels: int = 3, is_hybrid: bool = False, qkv_bias: bool = True, backbone_out_indices=[2, 5, 8, 11], readout_type: str = 'project', reassemble_factors=[4, 2, 1, 0.5], neck_hidden_sizes=[96, 192, 384, 768], fusion_hidden_size: int = 256, head_in_index: int = -1, use_batch_norm_in_fusion_residual: bool = False, use_auxiliary_head: bool = True, auxiliary_loss_weight: float = 0.4, semantic_loss_ignore_index: int = 255, semantic_classifier_dropout: float = 0.1, backbone_featmap_shape=[1, 1024, 24, 24], neck_ignore_stages=[0, 1], backbone_config: Incomplete | None = None, **kwargs) -> None: ...
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`]. Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
