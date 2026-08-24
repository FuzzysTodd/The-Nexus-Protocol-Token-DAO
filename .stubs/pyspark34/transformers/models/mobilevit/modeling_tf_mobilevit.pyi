import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...file_utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, replace_return_docstrings as replace_return_docstrings
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFBaseModelOutputWithPooling as TFBaseModelOutputWithPooling, TFImageClassifierOutputWithNoAttention as TFImageClassifierOutputWithNoAttention, TFSemanticSegmenterOutputWithNoAttention as TFSemanticSegmenterOutputWithNoAttention
from ...modeling_tf_utils import TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import logging as logging
from .configuration_mobilevit import MobileViTConfig as MobileViTConfig
from _typeshed import Incomplete
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_MOBILEVIT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def make_divisible(value: int, divisor: int = 8, min_value: Optional[int] = None) -> int:
    """
    Ensure that all layers have a channel count that is divisible by `divisor`. This function is taken from the
    original TensorFlow repo. It can be seen here:
    https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/mobilenet.py
    """

class TFMobileViTConvLayer(tf.keras.layers.Layer):
    padding: Incomplete
    convolution: Incomplete
    normalization: Incomplete
    activation: Incomplete
    def __init__(self, config: MobileViTConfig, out_channels: int, kernel_size: int, stride: int = 1, groups: int = 1, bias: bool = False, dilation: int = 1, use_normalization: bool = True, use_activation: Union[bool, str] = True, **kwargs) -> None: ...
    def call(self, features: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFMobileViTInvertedResidual(tf.keras.layers.Layer):
    """
    Inverted residual block (MobileNetv2): https://arxiv.org/abs/1801.04381
    """
    use_residual: Incomplete
    expand_1x1: Incomplete
    conv_3x3: Incomplete
    reduce_1x1: Incomplete
    def __init__(self, config: MobileViTConfig, in_channels: int, out_channels: int, stride: int, dilation: int = 1, **kwargs) -> None: ...
    def call(self, features: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFMobileViTMobileNetLayer(tf.keras.layers.Layer):
    layers: Incomplete
    def __init__(self, config: MobileViTConfig, in_channels: int, out_channels: int, stride: int = 1, num_stages: int = 1, **kwargs) -> None: ...
    def call(self, features: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFMobileViTSelfAttention(tf.keras.layers.Layer):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    scale: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config: MobileViTConfig, hidden_size: int, **kwargs) -> None: ...
    def transpose_for_scores(self, x: tf.Tensor) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFMobileViTSelfOutput(tf.keras.layers.Layer):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: MobileViTConfig, hidden_size: int, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFMobileViTAttention(tf.keras.layers.Layer):
    attention: Incomplete
    dense_output: Incomplete
    def __init__(self, config: MobileViTConfig, hidden_size: int, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, hidden_states: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFMobileViTIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: MobileViTConfig, hidden_size: int, intermediate_size: int, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFMobileViTOutput(tf.keras.layers.Layer):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: MobileViTConfig, hidden_size: int, intermediate_size: int, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFMobileViTTransformerLayer(tf.keras.layers.Layer):
    attention: Incomplete
    intermediate: Incomplete
    mobilevit_output: Incomplete
    layernorm_before: Incomplete
    layernorm_after: Incomplete
    def __init__(self, config: MobileViTConfig, hidden_size: int, intermediate_size: int, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFMobileViTTransformer(tf.keras.layers.Layer):
    layers: Incomplete
    def __init__(self, config: MobileViTConfig, hidden_size: int, num_stages: int, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFMobileViTLayer(tf.keras.layers.Layer):
    """
    MobileViT block: https://arxiv.org/abs/2110.02178
    """
    patch_width: Incomplete
    patch_height: Incomplete
    downsampling_layer: Incomplete
    conv_kxk: Incomplete
    conv_1x1: Incomplete
    transformer: Incomplete
    layernorm: Incomplete
    conv_projection: Incomplete
    fusion: Incomplete
    def __init__(self, config: MobileViTConfig, in_channels: int, out_channels: int, stride: int, hidden_size: int, num_stages: int, dilation: int = 1, **kwargs) -> None: ...
    def unfolding(self, features: tf.Tensor) -> Tuple[tf.Tensor, Dict]: ...
    def folding(self, patches: tf.Tensor, info_dict: Dict) -> tf.Tensor: ...
    def call(self, features: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFMobileViTEncoder(tf.keras.layers.Layer):
    config: Incomplete
    layers: Incomplete
    def __init__(self, config: MobileViTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, output_hidden_states: bool = False, return_dict: bool = True, training: bool = False) -> Union[tuple, TFBaseModelOutput]: ...

class TFMobileViTMainLayer(tf.keras.layers.Layer):
    config_class = MobileViTConfig
    config: Incomplete
    expand_output: Incomplete
    conv_stem: Incomplete
    encoder: Incomplete
    conv_1x1_exp: Incomplete
    pooler: Incomplete
    def __init__(self, config: MobileViTConfig, expand_output: bool = True, **kwargs) -> None: ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[Tuple[tf.Tensor], TFBaseModelOutputWithPooling]: ...

class TFMobileViTPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = MobileViTConfig
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

MOBILEVIT_START_DOCSTRING: str
MOBILEVIT_INPUTS_DOCSTRING: str

class TFMobileViTModel(TFMobileViTPreTrainedModel):
    config: Incomplete
    expand_output: Incomplete
    mobilevit: Incomplete
    def __init__(self, config: MobileViTConfig, expand_output: bool = True, *inputs, **kwargs) -> None: ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[Tuple[tf.Tensor], TFBaseModelOutputWithPooling]: ...
    def serving_output(self, output: TFBaseModelOutputWithPooling) -> TFBaseModelOutputWithPooling: ...

class TFMobileViTForImageClassification(TFMobileViTPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    mobilevit: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: MobileViTConfig, *inputs, **kwargs) -> None: ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, output_hidden_states: Optional[bool] = None, labels: Optional[tf.Tensor] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[tuple, TFImageClassifierOutputWithNoAttention]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss). If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFImageClassifierOutputWithNoAttention) -> TFImageClassifierOutputWithNoAttention: ...

class TFMobileViTASPPPooling(tf.keras.layers.Layer):
    global_pool: Incomplete
    conv_1x1: Incomplete
    def __init__(self, config: MobileViTConfig, out_channels: int, **kwargs) -> None: ...
    def call(self, features: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFMobileViTASPP(tf.keras.layers.Layer):
    """
    ASPP module defined in DeepLab papers: https://arxiv.org/abs/1606.00915, https://arxiv.org/abs/1706.05587
    """
    convs: Incomplete
    project: Incomplete
    dropout: Incomplete
    def __init__(self, config: MobileViTConfig, **kwargs) -> None: ...
    def call(self, features: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFMobileViTDeepLabV3(tf.keras.layers.Layer):
    """
    DeepLabv3 architecture: https://arxiv.org/abs/1706.05587
    """
    aspp: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: MobileViTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFMobileViTForSemanticSegmentation(TFMobileViTPreTrainedModel):
    num_labels: Incomplete
    mobilevit: Incomplete
    segmentation_head: Incomplete
    def __init__(self, config: MobileViTConfig, **kwargs) -> None: ...
    def hf_compute_loss(self, logits, labels): ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, labels: Optional[tf.Tensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[tuple, TFSemanticSegmenterOutputWithNoAttention]:
        '''
        labels (`tf.Tensor` of shape `(batch_size, height, width)`, *optional*):
            Ground truth semantic segmentation maps for computing the loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1`, a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, TFMobileViTForSemanticSegmentation
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("apple/deeplabv3-mobilevit-small")
        >>> model = TFMobileViTForSemanticSegmentation.from_pretrained("apple/deeplabv3-mobilevit-small")

        >>> inputs = image_processor(images=image, return_tensors="tf")

        >>> outputs = model(**inputs)

        >>> # logits are of shape (batch_size, num_labels, height, width)
        >>> logits = outputs.logits
        ```'''
    def serving_output(self, output: TFSemanticSegmenterOutputWithNoAttention) -> TFSemanticSegmenterOutputWithNoAttention: ...
