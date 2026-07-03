import tensorflow as tf
from ...activations_tf import ACT2FN as ACT2FN
from ...modeling_tf_outputs import TFBaseModelOutputWithNoAttention as TFBaseModelOutputWithNoAttention, TFBaseModelOutputWithPoolingAndNoAttention as TFBaseModelOutputWithPoolingAndNoAttention, TFImageClassifierOutputWithNoAttention as TFImageClassifierOutputWithNoAttention
from ...modeling_tf_utils import TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_resnet import ResNetConfig as ResNetConfig
from _typeshed import Incomplete
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_RESNET_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFResNetConvLayer(tf.keras.layers.Layer):
    pad_value: Incomplete
    conv: Incomplete
    normalization: Incomplete
    activation: Incomplete
    def __init__(self, out_channels: int, kernel_size: int = 3, stride: int = 1, activation: str = 'relu', **kwargs) -> None: ...
    def convolution(self, hidden_state: tf.Tensor) -> tf.Tensor: ...
    def call(self, hidden_state: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFResNetEmbeddings(tf.keras.layers.Layer):
    """
    ResNet Embeddings (stem) composed of a single aggressive convolution.
    """
    embedder: Incomplete
    pooler: Incomplete
    num_channels: Incomplete
    def __init__(self, config: ResNetConfig, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFResNetShortCut(tf.keras.layers.Layer):
    """
    ResNet shortcut, used to project the residual features to the correct size. If needed, it is also used to
    downsample the input using `stride=2`.
    """
    convolution: Incomplete
    normalization: Incomplete
    def __init__(self, out_channels: int, stride: int = 2, **kwargs) -> None: ...
    def call(self, x: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFResNetBasicLayer(tf.keras.layers.Layer):
    """
    A classic ResNet's residual layer composed by two `3x3` convolutions.
    """
    conv1: Incomplete
    conv2: Incomplete
    shortcut: Incomplete
    activation: Incomplete
    def __init__(self, in_channels: int, out_channels: int, stride: int = 1, activation: str = 'relu', **kwargs) -> None: ...
    def call(self, hidden_state: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFResNetBottleNeckLayer(tf.keras.layers.Layer):
    """
    A classic ResNet's bottleneck layer composed by three `3x3` convolutions.

    The first `1x1` convolution reduces the input by a factor of `reduction` in order to make the second `3x3`
    convolution faster. The last `1x1` convolution remaps the reduced features to `out_channels`.
    """
    conv0: Incomplete
    conv1: Incomplete
    conv2: Incomplete
    shortcut: Incomplete
    activation: Incomplete
    def __init__(self, in_channels: int, out_channels: int, stride: int = 1, activation: str = 'relu', reduction: int = 4, **kwargs) -> None: ...
    def call(self, hidden_state: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFResNetStage(tf.keras.layers.Layer):
    """
    A ResNet stage composed of stacked layers.
    """
    stage_layers: Incomplete
    def __init__(self, config: ResNetConfig, in_channels: int, out_channels: int, stride: int = 2, depth: int = 2, **kwargs) -> None: ...
    def call(self, hidden_state: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFResNetEncoder(tf.keras.layers.Layer):
    stages: Incomplete
    def __init__(self, config: ResNetConfig, **kwargs) -> None: ...
    def call(self, hidden_state: tf.Tensor, output_hidden_states: bool = False, return_dict: bool = True, training: bool = False) -> TFBaseModelOutputWithNoAttention: ...

class TFResNetPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ResNetConfig
    base_model_prefix: str
    main_input_name: str
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]:
        """
        Dummy inputs to build the network. Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """
    def serving(self, inputs): ...

RESNET_START_DOCSTRING: str
RESNET_INPUTS_DOCSTRING: str

class TFResNetMainLayer(tf.keras.layers.Layer):
    config_class = ResNetConfig
    config: Incomplete
    embedder: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config: ResNetConfig, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[Tuple[tf.Tensor], TFBaseModelOutputWithPoolingAndNoAttention]: ...

class TFResNetModel(TFResNetPreTrainedModel):
    resnet: Incomplete
    def __init__(self, config: ResNetConfig, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[Tuple[tf.Tensor], TFBaseModelOutputWithPoolingAndNoAttention]: ...
    def serving_output(self, output: TFBaseModelOutputWithPoolingAndNoAttention) -> TFBaseModelOutputWithPoolingAndNoAttention: ...

class TFResNetForImageClassification(TFResNetPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    resnet: Incomplete
    classifier_layer: Incomplete
    def __init__(self, config: ResNetConfig, **kwargs) -> None: ...
    def classifier(self, x: tf.Tensor) -> tf.Tensor: ...
    def call(self, pixel_values: tf.Tensor = None, labels: tf.Tensor = None, output_hidden_states: bool = None, return_dict: bool = None, training: bool = False) -> Union[Tuple[tf.Tensor], TFImageClassifierOutputWithNoAttention]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFImageClassifierOutputWithNoAttention) -> TFImageClassifierOutputWithNoAttention: ...
