import tensorflow as tf
from ...activations_tf import ACT2FN as ACT2FN
from ...file_utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward
from ...modeling_tf_outputs import TFBaseModelOutputWithNoAttention as TFBaseModelOutputWithNoAttention, TFBaseModelOutputWithPoolingAndNoAttention as TFBaseModelOutputWithPoolingAndNoAttention, TFSequenceClassifierOutput as TFSequenceClassifierOutput
from ...modeling_tf_utils import TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list
from ...utils import logging as logging
from .configuration_regnet import RegNetConfig as RegNetConfig
from _typeshed import Incomplete
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_REGNET_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TFRegNetConvLayer(tf.keras.layers.Layer):
    padding: Incomplete
    convolution: Incomplete
    normalization: Incomplete
    activation: Incomplete
    def __init__(self, out_channels: int, kernel_size: int = 3, stride: int = 1, groups: int = 1, activation: Optional[str] = 'relu', **kwargs) -> None: ...
    def call(self, hidden_state): ...

class TFRegNetEmbeddings(tf.keras.layers.Layer):
    """
    RegNet Embeddings (stem) composed of a single aggressive convolution.
    """
    num_channels: Incomplete
    embedder: Incomplete
    def __init__(self, config: RegNetConfig, **kwargs) -> None: ...
    def call(self, pixel_values): ...

class TFRegNetShortCut(tf.keras.layers.Layer):
    """
    RegNet shortcut, used to project the residual features to the correct size. If needed, it is also used to
    downsample the input using `stride=2`.
    """
    convolution: Incomplete
    normalization: Incomplete
    def __init__(self, out_channels: int, stride: int = 2, **kwargs) -> None: ...
    def call(self, inputs: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFRegNetSELayer(tf.keras.layers.Layer):
    """
    Squeeze and Excitation layer (SE) proposed in [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507).
    """
    pooler: Incomplete
    attention: Incomplete
    def __init__(self, in_channels: int, reduced_channels: int, **kwargs) -> None: ...
    def call(self, hidden_state): ...

class TFRegNetXLayer(tf.keras.layers.Layer):
    """
    RegNet's layer composed by three `3x3` convolutions, same as a ResNet bottleneck layer with reduction = 1.
    """
    shortcut: Incomplete
    layers: Incomplete
    activation: Incomplete
    def __init__(self, config: RegNetConfig, in_channels: int, out_channels: int, stride: int = 1, **kwargs) -> None: ...
    def call(self, hidden_state): ...

class TFRegNetYLayer(tf.keras.layers.Layer):
    """
    RegNet's Y layer: an X layer with Squeeze and Excitation.
    """
    shortcut: Incomplete
    layers: Incomplete
    activation: Incomplete
    def __init__(self, config: RegNetConfig, in_channels: int, out_channels: int, stride: int = 1, **kwargs) -> None: ...
    def call(self, hidden_state): ...

class TFRegNetStage(tf.keras.layers.Layer):
    """
    A RegNet stage composed by stacked layers.
    """
    layers: Incomplete
    def __init__(self, config: RegNetConfig, in_channels: int, out_channels: int, stride: int = 2, depth: int = 2, **kwargs) -> None: ...
    def call(self, hidden_state): ...

class TFRegNetEncoder(tf.keras.layers.Layer):
    stages: Incomplete
    def __init__(self, config: RegNetConfig, **kwargs) -> None: ...
    def call(self, hidden_state: tf.Tensor, output_hidden_states: bool = False, return_dict: bool = True) -> TFBaseModelOutputWithNoAttention: ...

class TFRegNetMainLayer(tf.keras.layers.Layer):
    config_class = RegNetConfig
    config: Incomplete
    embedder: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> TFBaseModelOutputWithPoolingAndNoAttention: ...

class TFRegNetPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = RegNetConfig
    base_model_prefix: str
    main_input_name: str
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]:
        """
        Dummy inputs to build the network.

        Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """
    def serving(self, inputs):
        """
        Method used for serving the model.

        Args:
            inputs (`Dict[str, tf.Tensor]`):
                The input of the saved model as a dictionary of tensors.
        """

REGNET_START_DOCSTRING: str
REGNET_INPUTS_DOCSTRING: str

class TFRegNetModel(TFRegNetPreTrainedModel):
    regnet: Incomplete
    def __init__(self, config: RegNetConfig, *inputs, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPoolingAndNoAttention, Tuple[tf.Tensor]]: ...
    def serving_output(self, output: TFBaseModelOutputWithPoolingAndNoAttention) -> TFBaseModelOutputWithPoolingAndNoAttention: ...

class TFRegNetForImageClassification(TFRegNetPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    regnet: Incomplete
    classifier: Incomplete
    def __init__(self, config: RegNetConfig, *inputs, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor = None, labels: tf.Tensor = None, output_hidden_states: bool = None, return_dict: bool = None, training: bool = False) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...
