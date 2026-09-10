from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...onnx import OnnxConfig as OnnxConfig
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import Mapping

logger: Incomplete
CONVNEXT_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class ConvNextConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`ConvNextModel`]. It is used to instantiate an
    ConvNeXT model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the ConvNeXT
    [facebook/convnext-tiny-224](https://huggingface.co/facebook/convnext-tiny-224) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        patch_size (`int`, optional, defaults to 4):
            Patch size to use in the patch embedding layer.
        num_stages (`int`, optional, defaults to 4):
            The number of stages in the model.
        hidden_sizes (`List[int]`, *optional*, defaults to [96, 192, 384, 768]):
            Dimensionality (hidden size) at each stage.
        depths (`List[int]`, *optional*, defaults to [3, 3, 9, 3]):
            Depth (number of blocks) for each stage.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in each block. If string, `"gelu"`, `"relu"`,
            `"selu"` and `"gelu_new"` are supported.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        layer_scale_init_value (`float`, *optional*, defaults to 1e-6):
            The initial value for the layer scale.
        drop_path_rate (`float`, *optional*, defaults to 0.0):
            The drop rate for stochastic depth.
        out_features (`List[str]`, *optional*):
            If used as backbone, list of features to output. Can be any of `"stem"`, `"stage1"`, `"stage2"`, etc.
            (depending on how many stages the model has). Will default to the last stage if unset.

    Example:
    ```python
    >>> from transformers import ConvNextConfig, ConvNextModel

    >>> # Initializing a ConvNext convnext-tiny-224 style configuration
    >>> configuration = ConvNextConfig()

    >>> # Initializing a model (with random weights) from the convnext-tiny-224 style configuration
    >>> model = ConvNextModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    num_channels: Incomplete
    patch_size: Incomplete
    num_stages: Incomplete
    hidden_sizes: Incomplete
    depths: Incomplete
    hidden_act: Incomplete
    initializer_range: Incomplete
    layer_norm_eps: Incomplete
    layer_scale_init_value: Incomplete
    drop_path_rate: Incomplete
    image_size: Incomplete
    stage_names: Incomplete
    out_features: Incomplete
    def __init__(self, num_channels: int = 3, patch_size: int = 4, num_stages: int = 4, hidden_sizes: Incomplete | None = None, depths: Incomplete | None = None, hidden_act: str = 'gelu', initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, layer_scale_init_value: float = 1e-06, drop_path_rate: float = 0.0, image_size: int = 224, out_features: Incomplete | None = None, **kwargs) -> None: ...

class ConvNextOnnxConfig(OnnxConfig):
    torch_onnx_minimum_version: Incomplete
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]: ...
    @property
    def atol_for_validation(self) -> float: ...
