import tensorflow as tf
from ...modeling_tf_outputs import TFImageClassifierOutputWithNoAttention as TFImageClassifierOutputWithNoAttention
from ...modeling_tf_utils import TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_cvt import CvtConfig as CvtConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_CVT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class TFBaseModelOutputWithCLSToken(ModelOutput):
    """
    Base class for model's outputs.

    Args:
        last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        cls_token_value (`tf.Tensor` of shape `(batch_size, 1, hidden_size)`):
            Classification token at the output of the last layer of the model.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer plus
            the initial embedding outputs.
    """
    last_hidden_state: tf.Tensor = ...
    cls_token_value: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, last_hidden_state, cls_token_value, hidden_states) -> None: ...

class TFCvtDropPath(tf.keras.layers.Layer):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).
    References:
        (1) github.com:rwightman/pytorch-image-models
    """
    drop_prob: Incomplete
    def __init__(self, drop_prob: float, **kwargs) -> None: ...
    def call(self, x: tf.Tensor, training: Incomplete | None = None): ...

class TFCvtEmbeddings(tf.keras.layers.Layer):
    """Construct the Convolutional Token Embeddings."""
    convolution_embeddings: Incomplete
    dropout: Incomplete
    def __init__(self, config: CvtConfig, patch_size: int, embed_dim: int, stride: int, padding: int, dropout_rate: float, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFCvtConvEmbeddings(tf.keras.layers.Layer):
    """Image to Convolution Embeddings. This convolutional operation aims to model local spatial contexts."""
    padding: Incomplete
    patch_size: Incomplete
    projection: Incomplete
    normalization: Incomplete
    def __init__(self, config: CvtConfig, patch_size: int, embed_dim: int, stride: int, padding: int, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor) -> tf.Tensor: ...

class TFCvtSelfAttentionConvProjection(tf.keras.layers.Layer):
    """Convolutional projection layer."""
    padding: Incomplete
    convolution: Incomplete
    normalization: Incomplete
    def __init__(self, config: CvtConfig, embed_dim: int, kernel_size: int, stride: int, padding: int, **kwargs) -> None: ...
    def call(self, hidden_state: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFCvtSelfAttentionLinearProjection(tf.keras.layers.Layer):
    """Linear projection layer used to flatten tokens into 1D."""
    def call(self, hidden_state: tf.Tensor) -> tf.Tensor: ...

class TFCvtSelfAttentionProjection(tf.keras.layers.Layer):
    """Convolutional Projection for Attention."""
    convolution_projection: Incomplete
    linear_projection: Incomplete
    def __init__(self, config: CvtConfig, embed_dim: int, kernel_size: int, stride: int, padding: int, projection_method: str = 'dw_bn', **kwargs) -> None: ...
    def call(self, hidden_state: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFCvtSelfAttention(tf.keras.layers.Layer):
    """
    Self-attention layer. A depth-wise separable convolution operation (Convolutional Projection), is applied for
    query, key, and value embeddings.
    """
    scale: Incomplete
    with_cls_token: Incomplete
    embed_dim: Incomplete
    num_heads: Incomplete
    convolution_projection_query: Incomplete
    convolution_projection_key: Incomplete
    convolution_projection_value: Incomplete
    projection_query: Incomplete
    projection_key: Incomplete
    projection_value: Incomplete
    dropout: Incomplete
    def __init__(self, config: CvtConfig, num_heads: int, embed_dim: int, kernel_size: int, stride_q: int, stride_kv: int, padding_q: int, padding_kv: int, qkv_projection_method: str, qkv_bias: bool, attention_drop_rate: float, with_cls_token: bool = True, **kwargs) -> None: ...
    def rearrange_for_multi_head_attention(self, hidden_state: tf.Tensor) -> tf.Tensor: ...
    def call(self, hidden_state: tf.Tensor, height: int, width: int, training: bool = False) -> tf.Tensor: ...

class TFCvtSelfOutput(tf.keras.layers.Layer):
    """Output of the Attention layer ."""
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: CvtConfig, embed_dim: int, drop_rate: float, **kwargs) -> None: ...
    def call(self, hidden_state: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFCvtAttention(tf.keras.layers.Layer):
    """Attention layer. First chunk of the convolutional transformer block."""
    attention: Incomplete
    dense_output: Incomplete
    def __init__(self, config: CvtConfig, num_heads: int, embed_dim: int, kernel_size: int, stride_q: int, stride_kv: int, padding_q: int, padding_kv: int, qkv_projection_method: str, qkv_bias: bool, attention_drop_rate: float, drop_rate: float, with_cls_token: bool = True, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, hidden_state: tf.Tensor, height: int, width: int, training: bool = False): ...

class TFCvtIntermediate(tf.keras.layers.Layer):
    """Intermediate dense layer. Second chunk of the convolutional transformer block."""
    dense: Incomplete
    def __init__(self, config: CvtConfig, embed_dim: int, mlp_ratio: int, **kwargs) -> None: ...
    def call(self, hidden_state: tf.Tensor) -> tf.Tensor: ...

class TFCvtOutput(tf.keras.layers.Layer):
    """
    Output of the Convolutional Transformer Block (last chunk). It consists of a MLP and a residual connection.
    """
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: CvtConfig, embed_dim: int, drop_rate: int, **kwargs) -> None: ...
    def call(self, hidden_state: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFCvtLayer(tf.keras.layers.Layer):
    """
    Convolutional Transformer Block composed by attention layers, normalization and multi-layer perceptrons (mlps). It
    consists of 3 chunks : an attention layer, an intermediate dense layer and an output layer. This corresponds to the
    `Block` class in the original implementation.
    """
    attention: Incomplete
    intermediate: Incomplete
    dense_output: Incomplete
    drop_path: Incomplete
    layernorm_before: Incomplete
    layernorm_after: Incomplete
    def __init__(self, config: CvtConfig, num_heads: int, embed_dim: int, kernel_size: int, stride_q: int, stride_kv: int, padding_q: int, padding_kv: int, qkv_projection_method: str, qkv_bias: bool, attention_drop_rate: float, drop_rate: float, mlp_ratio: float, drop_path_rate: float, with_cls_token: bool = True, **kwargs) -> None: ...
    def call(self, hidden_state: tf.Tensor, height: int, width: int, training: bool = False) -> tf.Tensor: ...

class TFCvtStage(tf.keras.layers.Layer):
    """
    Cvt stage (encoder block). Each stage has 2 parts :
    - (1) A Convolutional Token Embedding layer
    - (2) A Convolutional Transformer Block (layer).
    The classification token is added only in the last stage.

    Args:
        config ([`CvtConfig`]): Model configuration class.
        stage (`int`): Stage number.
    """
    config: Incomplete
    stage: Incomplete
    cls_token: Incomplete
    embedding: Incomplete
    layers: Incomplete
    def __init__(self, config: CvtConfig, stage: int, **kwargs) -> None: ...
    def call(self, hidden_state: tf.Tensor, training: bool = False): ...

class TFCvtEncoder(tf.keras.layers.Layer):
    """
    Convolutional Vision Transformer encoder. CVT has 3 stages of encoder blocks with their respective number of layers
    (depth) being 1, 2 and 10.

    Args:
        config ([`CvtConfig`]): Model configuration class.
    """
    config_class = CvtConfig
    config: Incomplete
    stages: Incomplete
    def __init__(self, config: CvtConfig, **kwargs) -> None: ...
    def call(self, pixel_values: TFModelInputType, output_hidden_states: Optional[bool] = False, return_dict: Optional[bool] = True, training: Optional[bool] = False) -> Union[TFBaseModelOutputWithCLSToken, Tuple[tf.Tensor]]: ...

class TFCvtMainLayer(tf.keras.layers.Layer):
    """Construct the Cvt model."""
    config_class = CvtConfig
    config: Incomplete
    encoder: Incomplete
    def __init__(self, config: CvtConfig, **kwargs) -> None: ...
    def call(self, pixel_values: Optional[TFModelInputType] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutputWithCLSToken, Tuple[tf.Tensor]]: ...

class TFCvtPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = CvtConfig
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

TFCVT_START_DOCSTRING: str
TFCVT_INPUTS_DOCSTRING: str

class TFCvtModel(TFCvtPreTrainedModel):
    cvt: Incomplete
    def __init__(self, config: CvtConfig, *inputs, **kwargs) -> None: ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutputWithCLSToken, Tuple[tf.Tensor]]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, TFCvtModel
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("microsoft/cvt-13")
        >>> model = TFCvtModel.from_pretrained("microsoft/cvt-13")

        >>> inputs = image_processor(images=image, return_tensors="tf")
        >>> outputs = model(**inputs)
        >>> last_hidden_states = outputs.last_hidden_state
        ```'''
    def serving_output(self, output: TFBaseModelOutputWithCLSToken) -> TFBaseModelOutputWithCLSToken: ...

class TFCvtForImageClassification(TFCvtPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    cvt: Incomplete
    layernorm: Incomplete
    classifier: Incomplete
    def __init__(self, config: CvtConfig, *inputs, **kwargs) -> None: ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, labels: Optional[tf.Tensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFImageClassifierOutputWithNoAttention, Tuple[tf.Tensor]]:
        '''
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, TFCvtForImageClassification
        >>> import tensorflow as tf
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("microsoft/cvt-13")
        >>> model = TFCvtForImageClassification.from_pretrained("microsoft/cvt-13")

        >>> inputs = image_processor(images=image, return_tensors="tf")
        >>> outputs = model(**inputs)
        >>> logits = outputs.logits
        >>> # model predicts one of the 1000 ImageNet classes
        >>> predicted_class_idx = tf.math.argmax(logits, axis=-1)[0]
        >>> print("Predicted class:", model.config.id2label[int(predicted_class_idx)])
        ```'''
    def serving_output(self, output: TFImageClassifierOutputWithNoAttention) -> TFImageClassifierOutputWithNoAttention: ...
