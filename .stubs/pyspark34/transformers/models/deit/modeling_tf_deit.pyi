import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFBaseModelOutputWithPooling as TFBaseModelOutputWithPooling, TFImageClassifierOutput as TFImageClassifierOutput, TFMaskedLMOutput as TFMaskedLMOutput
from ...modeling_tf_utils import TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_deit import DeiTConfig as DeiTConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Dict, Optional, Tuple, Union

logger: Incomplete
TF_DEIT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class TFDeiTForImageClassificationWithTeacherOutput(ModelOutput):
    """
    Output type of [`DeiTForImageClassificationWithTeacher`].

    Args:
        logits (`tf.Tensor` of shape `(batch_size, config.num_labels)`):
            Prediction scores as the average of the cls_logits and distillation logits.
        cls_logits (`tf.Tensor` of shape `(batch_size, config.num_labels)`):
            Prediction scores of the classification head (i.e. the linear layer on top of the final hidden state of the
            class token).
        distillation_logits (`tf.Tensor` of shape `(batch_size, config.num_labels)`):
            Prediction scores of the distillation head (i.e. the linear layer on top of the final hidden state of the
            distillation token).
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer plus
            the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    """
    logits: tf.Tensor = ...
    cls_logits: tf.Tensor = ...
    distillation_logits: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, logits, cls_logits, distillation_logits, hidden_states, attentions) -> None: ...

class TFDeiTEmbeddings(tf.keras.layers.Layer):
    """
    Construct the CLS token, distillation token, position and patch embeddings. Optionally, also the mask token.
    """
    config: Incomplete
    use_mask_token: Incomplete
    patch_embeddings: Incomplete
    dropout: Incomplete
    def __init__(self, config: DeiTConfig, use_mask_token: bool = False, **kwargs) -> None: ...
    cls_token: Incomplete
    distillation_token: Incomplete
    mask_token: Incomplete
    position_embeddings: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def call(self, pixel_values: tf.Tensor, bool_masked_pos: Optional[tf.Tensor] = None, training: bool = False) -> tf.Tensor: ...

class TFDeiTPatchEmbeddings(tf.keras.layers.Layer):
    """
    This class turns `pixel_values` of shape `(batch_size, num_channels, height, width)` into the initial
    `hidden_states` (patch embeddings) of shape `(batch_size, seq_length, hidden_size)` to be consumed by a
    Transformer.
    """
    image_size: Incomplete
    patch_size: Incomplete
    num_channels: Incomplete
    num_patches: Incomplete
    projection: Incomplete
    def __init__(self, config: DeiTConfig, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor) -> tf.Tensor: ...

class TFDeiTSelfAttention(tf.keras.layers.Layer):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    sqrt_att_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config: DeiTConfig, **kwargs) -> None: ...
    def transpose_for_scores(self, tensor: tf.Tensor, batch_size: int) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFDeiTSelfOutput(tf.keras.layers.Layer):
    """
    The residual connection is defined in TFDeiTLayer instead of here (as is the case with other models), due to the
    layernorm applied before each block.
    """
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: DeiTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFDeiTAttention(tf.keras.layers.Layer):
    self_attention: Incomplete
    dense_output: Incomplete
    def __init__(self, config: DeiTConfig, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, input_tensor: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFDeiTIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: DeiTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFDeiTOutput(tf.keras.layers.Layer):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: DeiTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFDeiTLayer(tf.keras.layers.Layer):
    """This corresponds to the Block class in the timm implementation."""
    attention: Incomplete
    intermediate: Incomplete
    deit_output: Incomplete
    layernorm_before: Incomplete
    layernorm_after: Incomplete
    def __init__(self, config: DeiTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFDeiTEncoder(tf.keras.layers.Layer):
    layer: Incomplete
    def __init__(self, config: DeiTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...

class TFDeiTMainLayer(tf.keras.layers.Layer):
    config_class = DeiTConfig
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    pooler: Incomplete
    def __init__(self, config: DeiTConfig, add_pooling_layer: bool = True, use_mask_token: bool = False, **kwargs) -> None: ...
    def get_input_embeddings(self) -> TFDeiTPatchEmbeddings: ...
    def get_head_mask(self, head_mask): ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, bool_masked_pos: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor, ...]]: ...

class TFDeiTPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DeiTConfig
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

DEIT_START_DOCSTRING: str
DEIT_INPUTS_DOCSTRING: str

class TFDeiTModel(TFDeiTPreTrainedModel):
    deit: Incomplete
    def __init__(self, config: DeiTConfig, add_pooling_layer: bool = True, use_mask_token: bool = False, **kwargs) -> None: ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, bool_masked_pos: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False): ...
    def serving_output(self, output: TFBaseModelOutputWithPooling) -> TFBaseModelOutputWithPooling: ...

class TFDeiTPooler(tf.keras.layers.Layer):
    dense: Incomplete
    def __init__(self, config: DeiTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFDeitPixelShuffle(tf.keras.layers.Layer):
    """TF layer implementation of torch.nn.PixelShuffle"""
    upscale_factor: Incomplete
    def __init__(self, upscale_factor: int, **kwargs) -> None: ...
    def call(self, x: tf.Tensor) -> tf.Tensor: ...

class TFDeitDecoder(tf.keras.layers.Layer):
    conv2d: Incomplete
    pixel_shuffle: Incomplete
    def __init__(self, config: DeiTConfig, **kwargs) -> None: ...
    def call(self, inputs: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFDeiTForMaskedImageModeling(TFDeiTPreTrainedModel):
    deit: Incomplete
    decoder: Incomplete
    def __init__(self, config: DeiTConfig) -> None: ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, bool_masked_pos: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[tuple, TFMaskedLMOutput]:
        '''
        bool_masked_pos (`tf.Tensor` of type bool and shape `(batch_size, num_patches)`):
            Boolean masked positions. Indicates which patches are masked (1) and which aren\'t (0).

        Returns:

        Examples:
        ```python
        >>> from transformers import AutoImageProcessor, TFDeiTForMaskedImageModeling
        >>> import tensorflow as tf
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("facebook/deit-base-distilled-patch16-224")
        >>> model = TFDeiTForMaskedImageModeling.from_pretrained("facebook/deit-base-distilled-patch16-224")

        >>> num_patches = (model.config.image_size // model.config.patch_size) ** 2
        >>> pixel_values = image_processor(images=image, return_tensors="tf").pixel_values
        >>> # create random boolean mask of shape (batch_size, num_patches)
        >>> bool_masked_pos = tf.cast(tf.random.uniform((1, num_patches), minval=0, maxval=2, dtype=tf.int32), tf.bool)

        >>> outputs = model(pixel_values, bool_masked_pos=bool_masked_pos)
        >>> loss, reconstructed_pixel_values = outputs.loss, outputs.logits
        >>> list(reconstructed_pixel_values.shape)
        [1, 3, 224, 224]
        ```'''
    def serving_output(self, output: TFMaskedLMOutput) -> TFMaskedLMOutput: ...

class TFDeiTForImageClassification(TFDeiTPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    deit: Incomplete
    classifier: Incomplete
    def __init__(self, config: DeiTConfig) -> None: ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, labels: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[tf.Tensor, TFImageClassifierOutput]:
        '''
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, TFDeiTForImageClassification
        >>> import tensorflow as tf
        >>> from PIL import Image
        >>> import requests

        >>> tf.keras.utils.set_random_seed(3)  # doctest: +IGNORE_RESULT
        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> # note: we are loading a TFDeiTForImageClassificationWithTeacher from the hub here,
        >>> # so the head will be randomly initialized, hence the predictions will be random
        >>> image_processor = AutoImageProcessor.from_pretrained("facebook/deit-base-distilled-patch16-224")
        >>> model = TFDeiTForImageClassification.from_pretrained("facebook/deit-base-distilled-patch16-224")

        >>> inputs = image_processor(images=image, return_tensors="tf")
        >>> outputs = model(**inputs)
        >>> logits = outputs.logits
        >>> # model predicts one of the 1000 ImageNet classes
        >>> predicted_class_idx = tf.math.argmax(logits, axis=-1)[0]
        >>> print("Predicted class:", model.config.id2label[int(predicted_class_idx)])
        Predicted class: little blue heron, Egretta caerulea
        ```'''
    def serving_output(self, output: TFImageClassifierOutput) -> TFImageClassifierOutput: ...

class TFDeiTForImageClassificationWithTeacher(TFDeiTPreTrainedModel):
    num_labels: Incomplete
    deit: Incomplete
    cls_classifier: Incomplete
    distillation_classifier: Incomplete
    def __init__(self, config: DeiTConfig) -> None: ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[tuple, TFDeiTForImageClassificationWithTeacherOutput]: ...
    def serving_output(self, output: TFDeiTForImageClassificationWithTeacherOutput) -> TFDeiTForImageClassificationWithTeacherOutput: ...
