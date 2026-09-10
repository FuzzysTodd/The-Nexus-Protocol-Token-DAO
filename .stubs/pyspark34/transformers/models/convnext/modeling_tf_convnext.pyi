import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFBaseModelOutputWithPooling as TFBaseModelOutputWithPooling, TFSequenceClassifierOutput as TFSequenceClassifierOutput
from ...modeling_tf_utils import TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_convnext import ConvNextConfig as ConvNextConfig
from _typeshed import Incomplete
from transformers import shape_list as shape_list
from typing import Dict, Optional, Tuple, Union

logger: Incomplete

class TFConvNextDropPath(tf.keras.layers.Layer):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).
    References:
        (1) github.com:rwightman/pytorch-image-models
    """
    drop_path: Incomplete
    def __init__(self, drop_path, **kwargs) -> None: ...
    def call(self, x, training: Incomplete | None = None): ...

class TFConvNextEmbeddings(tf.keras.layers.Layer):
    """This class is comparable to (and inspired by) the SwinEmbeddings class
    found in src/transformers/models/swin/modeling_swin.py.
    """
    patch_embeddings: Incomplete
    layernorm: Incomplete
    num_channels: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, pixel_values): ...

class TFConvNextLayer(tf.keras.layers.Layer):
    """This corresponds to the `Block` class in the original implementation.

    There are two equivalent implementations: [DwConv, LayerNorm (channels_first), Conv, GELU,1x1 Conv]; all in (N, C,
    H, W) (2) [DwConv, Permute to (N, H, W, C), LayerNorm (channels_last), Linear, GELU, Linear]; Permute back

    The authors used (2) as they find it slightly faster in PyTorch. Since we already permuted the inputs to follow
    NHWC ordering, we can just apply the operations straight-away without the permutation.

    Args:
        config ([`ConvNextConfig`]): Model configuration class.
        dim (`int`): Number of input channels.
        drop_path (`float`): Stochastic depth rate. Default: 0.0.
    """
    dim: Incomplete
    config: Incomplete
    dwconv: Incomplete
    layernorm: Incomplete
    pwconv1: Incomplete
    act: Incomplete
    pwconv2: Incomplete
    drop_path: Incomplete
    def __init__(self, config, dim, drop_path: float = 0.0, **kwargs) -> None: ...
    layer_scale_parameter: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def call(self, hidden_states, training: bool = False): ...

class TFConvNextStage(tf.keras.layers.Layer):
    """ConvNext stage, consisting of an optional downsampling layer + multiple residual blocks.

    Args:
        config ([`ConvNextConfig`]): Model configuration class.
        in_channels (`int`): Number of input channels.
        out_channels (`int`): Number of output channels.
        depth (`int`): Number of residual blocks.
        drop_path_rates(`List[float]`): Stochastic depth rates for each layer.
    """
    downsampling_layer: Incomplete
    layers: Incomplete
    def __init__(self, config, in_channels, out_channels, kernel_size: int = 2, stride: int = 2, depth: int = 2, drop_path_rates: Incomplete | None = None, **kwargs) -> None: ...
    def call(self, hidden_states): ...

class TFConvNextEncoder(tf.keras.layers.Layer):
    stages: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def call(self, hidden_states, output_hidden_states: bool = False, return_dict: bool = True): ...

class TFConvNextMainLayer(tf.keras.layers.Layer):
    config_class = ConvNextConfig
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    pooler: Incomplete
    def __init__(self, config: ConvNextConfig, add_pooling_layer: bool = True, **kwargs) -> None: ...
    def call(self, pixel_values: Optional[TFModelInputType] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]: ...

class TFConvNextPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ConvNextConfig
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

CONVNEXT_START_DOCSTRING: str
CONVNEXT_INPUTS_DOCSTRING: str

class TFConvNextModel(TFConvNextPreTrainedModel):
    convnext: Incomplete
    def __init__(self, config, *inputs, add_pooling_layer: bool = True, **kwargs) -> None: ...
    def call(self, pixel_values: Optional[TFModelInputType] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, TFConvNextModel
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("facebook/convnext-tiny-224")
        >>> model = TFConvNextModel.from_pretrained("facebook/convnext-tiny-224")

        >>> inputs = image_processor(images=image, return_tensors="tf")
        >>> outputs = model(**inputs)
        >>> last_hidden_states = outputs.last_hidden_state
        ```'''
    def serving_output(self, output: TFBaseModelOutputWithPooling) -> TFBaseModelOutputWithPooling: ...

class TFConvNextForImageClassification(TFConvNextPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    convnext: Incomplete
    classifier: Incomplete
    def __init__(self, config: ConvNextConfig, *inputs, **kwargs) -> None: ...
    def call(self, pixel_values: Optional[TFModelInputType] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor]]:
        '''
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, TFConvNextForImageClassification
        >>> import tensorflow as tf
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("facebook/convnext-tiny-224")
        >>> model = TFConvNextForImageClassification.from_pretrained("facebook/convnext-tiny-224")

        >>> inputs = image_processor(images=image, return_tensors="tf")
        >>> outputs = model(**inputs)
        >>> logits = outputs.logits
        >>> # model predicts one of the 1000 ImageNet classes
        >>> predicted_class_idx = tf.math.argmax(logits, axis=-1)[0]
        >>> print("Predicted class:", model.config.id2label[int(predicted_class_idx)])
        ```'''
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...
