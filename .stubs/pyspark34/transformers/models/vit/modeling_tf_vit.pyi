import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFBaseModelOutputWithPooling as TFBaseModelOutputWithPooling, TFSequenceClassifierOutput as TFSequenceClassifierOutput
from ...modeling_tf_utils import TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_vit import ViTConfig as ViTConfig
from _typeshed import Incomplete
from typing import Dict, Optional, Tuple, Union

logger: Incomplete

class TFViTEmbeddings(tf.keras.layers.Layer):
    """
    Construct the CLS token, position and patch embeddings.

    """
    patch_embeddings: Incomplete
    dropout: Incomplete
    config: Incomplete
    def __init__(self, config: ViTConfig, **kwargs) -> None: ...
    cls_token: Incomplete
    position_embeddings: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def interpolate_pos_encoding(self, embeddings, height, width) -> tf.Tensor:
        """
        This method allows to interpolate the pre-trained position encodings, to be able to use the model on higher
        resolution images.

        Source:
        https://github.com/facebookresearch/dino/blob/de9ee3df6cf39fac952ab558447af1fa1365362a/vision_transformer.py#L174
        """
    def call(self, pixel_values: tf.Tensor, interpolate_pos_encoding: bool = False, training: bool = False) -> tf.Tensor: ...

class TFViTPatchEmbeddings(tf.keras.layers.Layer):
    """
    This class turns `pixel_values` of shape `(batch_size, num_channels, height, width)` into the initial
    `hidden_states` (patch embeddings) of shape `(batch_size, seq_length, hidden_size)` to be consumed by a
    Transformer.
    """
    image_size: Incomplete
    patch_size: Incomplete
    num_patches: Incomplete
    num_channels: Incomplete
    config: Incomplete
    projection: Incomplete
    def __init__(self, config: ViTConfig, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor, interpolate_pos_encoding: bool = False, training: bool = False) -> tf.Tensor: ...

class TFViTSelfAttention(tf.keras.layers.Layer):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    sqrt_att_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config: ViTConfig, **kwargs) -> None: ...
    def transpose_for_scores(self, tensor: tf.Tensor, batch_size: int) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFViTSelfOutput(tf.keras.layers.Layer):
    """
    The residual connection is defined in TFViTLayer instead of here (as is the case with other models), due to the
    layernorm applied before each block.
    """
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: ViTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFViTAttention(tf.keras.layers.Layer):
    self_attention: Incomplete
    dense_output: Incomplete
    def __init__(self, config: ViTConfig, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, input_tensor: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFViTIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: ViTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFViTOutput(tf.keras.layers.Layer):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: ViTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFViTLayer(tf.keras.layers.Layer):
    """This corresponds to the Block class in the timm implementation."""
    attention: Incomplete
    intermediate: Incomplete
    vit_output: Incomplete
    layernorm_before: Incomplete
    layernorm_after: Incomplete
    def __init__(self, config: ViTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFViTEncoder(tf.keras.layers.Layer):
    layer: Incomplete
    def __init__(self, config: ViTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...

class TFViTMainLayer(tf.keras.layers.Layer):
    config_class = ViTConfig
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    pooler: Incomplete
    def __init__(self, config: ViTConfig, add_pooling_layer: bool = True, **kwargs) -> None: ...
    def get_input_embeddings(self) -> tf.keras.layers.Layer: ...
    def call(self, pixel_values: Optional[TFModelInputType] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, interpolate_pos_encoding: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]: ...

class TFViTPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ViTConfig
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

VIT_START_DOCSTRING: str
VIT_INPUTS_DOCSTRING: str

class TFViTModel(TFViTPreTrainedModel):
    vit: Incomplete
    def __init__(self, config: ViTConfig, *inputs, add_pooling_layer: bool = True, **kwargs) -> None: ...
    def call(self, pixel_values: Optional[TFModelInputType] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, interpolate_pos_encoding: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]: ...
    def serving_output(self, output: TFBaseModelOutputWithPooling) -> TFBaseModelOutputWithPooling: ...

class TFViTPooler(tf.keras.layers.Layer):
    dense: Incomplete
    def __init__(self, config: ViTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFViTForImageClassification(TFViTPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    vit: Incomplete
    classifier: Incomplete
    def __init__(self, config: ViTConfig, *inputs, **kwargs) -> None: ...
    def call(self, pixel_values: Optional[TFModelInputType] = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, interpolate_pos_encoding: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, training: Optional[bool] = False) -> Union[TFSequenceClassifierOutput, Tuple[tf.Tensor]]:
        """
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFSequenceClassifierOutput) -> TFSequenceClassifierOutput: ...
