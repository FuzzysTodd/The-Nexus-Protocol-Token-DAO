import tensorflow as tf
from ...activations_tf import ACT2FN as ACT2FN
from ...modeling_tf_utils import TFPreTrainedModel as TFPreTrainedModel, TFSequenceClassificationLoss as TFSequenceClassificationLoss, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_swin import SwinConfig as SwinConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Union

logger: Incomplete
TF_SWIN_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class TFSwinEncoderOutput(ModelOutput):
    """
    Swin encoder's outputs, with potential hidden states and attentions.

    Args:
        last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each stage) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        reshaped_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each stage) of shape
            `(batch_size, hidden_size, height, width)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
            include the spatial dimensions.
    """
    last_hidden_state: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    reshaped_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, last_hidden_state, hidden_states, attentions, reshaped_hidden_states) -> None: ...

@dataclass
class TFSwinModelOutput(ModelOutput):
    """
    Swin model's outputs that also contains a pooling of the last hidden states.

    Args:
        last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        pooler_output (`tf.Tensor` of shape `(batch_size, hidden_size)`, *optional*, returned when `add_pooling_layer=True` is passed):
            Average pooling of the last layer hidden-state.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each stage) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        reshaped_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each stage) of shape
            `(batch_size, hidden_size, height, width)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
            include the spatial dimensions.
    """
    last_hidden_state: tf.Tensor = ...
    pooler_output: Optional[tf.Tensor] = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    reshaped_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, last_hidden_state, pooler_output, hidden_states, attentions, reshaped_hidden_states) -> None: ...

@dataclass
class TFSwinMaskedImageModelingOutput(ModelOutput):
    """
    Swin masked image model outputs.

    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `bool_masked_pos` is provided):
            Masked image modeling (MLM) loss.
        logits (`tf.Tensor` of shape `(batch_size, num_channels, height, width)`):
            Reconstructed pixel values.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each stage) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        reshaped_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each stage) of shape
            `(batch_size, hidden_size, height, width)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
            include the spatial dimensions.
    """
    loss: Optional[tf.Tensor] = ...
    logits: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    reshaped_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, logits, hidden_states, attentions, reshaped_hidden_states) -> None: ...

@dataclass
class TFSwinImageClassifierOutput(ModelOutput):
    """
    Swin outputs for image classification.

    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Classification (or regression if config.num_labels==1) loss.
        logits (`tf.Tensor` of shape `(batch_size, config.num_labels)`):
            Classification (or regression if config.num_labels==1) scores (before SoftMax).
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each stage) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        reshaped_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each stage) of shape
            `(batch_size, hidden_size, height, width)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
            include the spatial dimensions.
    """
    loss: Optional[tf.Tensor] = ...
    logits: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    reshaped_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, logits, hidden_states, attentions, reshaped_hidden_states) -> None: ...

def window_partition(input_feature: tf.Tensor, window_size: int) -> tf.Tensor:
    """
    Partitions the given input into windows.
    """
def window_reverse(windows: tf.Tensor, window_size: int, height: int, width: int) -> tf.Tensor:
    """
    Merges windows to produce higher resolution features.
    """
def drop_path(input: tf.Tensor, drop_prob: float = 0.0, training: bool = False, scale_by_keep: bool = True) -> tf.Tensor:
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).
    """

class TFSwinEmbeddings(tf.keras.layers.Layer):
    """
    Construct the patch and position embeddings. Optionally, also the mask token.
    """
    patch_embeddings: Incomplete
    num_patches: Incomplete
    patch_grid: Incomplete
    embed_dim: Incomplete
    use_mask_token: Incomplete
    use_absolute_embeddings: Incomplete
    norm: Incomplete
    dropout: Incomplete
    def __init__(self, config: SwinConfig, use_mask_token: bool = False, **kwargs) -> None: ...
    mask_token: Incomplete
    position_embeddings: Incomplete
    def build(self, input_shape: tf.TensorShape) -> None: ...
    def call(self, pixel_values: tf.Tensor, bool_masked_pos: bool = None, training: bool = False) -> Tuple[tf.Tensor, Tuple[int, int]]: ...

class TFSwinPatchEmbeddings(tf.keras.layers.Layer):
    """
    Image to Patch Embedding.
    """
    image_size: Incomplete
    patch_size: Incomplete
    num_channels: Incomplete
    num_patches: Incomplete
    grid_size: Incomplete
    projection: Incomplete
    def __init__(self, config, **kwargs) -> None: ...
    def maybe_pad(self, pixel_values: tf.Tensor, height: int, width: int) -> tf.Tensor: ...
    def call(self, pixel_values: tf.Tensor, training: bool = False) -> Tuple[tf.Tensor, Tuple[int, int]]: ...

class TFSwinPatchMerging(tf.keras.layers.Layer):
    """
    Patch Merging Layer.

    Args:
        input_resolution (`Tuple[int]`):
            Resolution of input feature.
        dim (`int`):
            Number of input channels.
        norm_layer (`tf.keras.layer.Layer`, *optional*, defaults to `tf.keras.layers.LayerNormalization`):
            Normalization layer class.
    """
    input_resolution: Incomplete
    dim: Incomplete
    reduction: Incomplete
    norm: Incomplete
    def __init__(self, input_resolution: Tuple[int, int], dim: int, norm_layer: Optional[Callable] = None, **kwargs) -> None: ...
    def maybe_pad(self, input_feature: tf.Tensor, height: int, width: int) -> tf.Tensor: ...
    def call(self, input_feature: tf.Tensor, input_dimensions: Tuple[int, int], training: bool = False) -> tf.Tensor: ...

class TFSwinDropPath(tf.keras.layers.Layer):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    drop_prob: Incomplete
    scale_by_keep: Incomplete
    def __init__(self, drop_prob: float = None, scale_by_keep: bool = True, **kwargs) -> None: ...
    def call(self, input: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFSwinSelfAttention(tf.keras.layers.Layer):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    window_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config: SwinConfig, dim: int, num_heads: int, **kwargs) -> None: ...
    relative_position_bias_table: Incomplete
    relative_position_index: Incomplete
    def build(self, input_shape: tf.TensorShape) -> None: ...
    def transpose_for_scores(self, x: tf.Tensor) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, output_attentions: bool = False, training: bool = False) -> Tuple[tf.Tensor, ...]: ...

class TFSwinSelfOutput(tf.keras.layers.Layer):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: SwinConfig, dim: int, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFSwinAttention(tf.keras.layers.Layer):
    self: Incomplete
    self_output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config: SwinConfig, dim: int, num_heads: int, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None:
        """
        Prunes heads of the model. See base class PreTrainedModel heads: dict of {layer_num: list of heads to prune in
        this layer}
        """
    def call(self, hidden_states: tf.Tensor, attention_mask: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, output_attentions: bool = False, training: bool = False) -> tf.Tensor: ...

class TFSwinIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: SwinConfig, dim: int, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFSwinOutput(tf.keras.layers.Layer):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: SwinConfig, dim: int, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFSwinLayer(tf.keras.layers.Layer):
    chunk_size_feed_forward: Incomplete
    window_size: Incomplete
    shift_size: Incomplete
    input_resolution: Incomplete
    layernorm_before: Incomplete
    attention: Incomplete
    drop_path: Incomplete
    layernorm_after: Incomplete
    intermediate: Incomplete
    swin_output: Incomplete
    def __init__(self, config, dim, input_resolution: Tuple[int, int], num_heads: int, shift_size: int = 0, **kwargs) -> None: ...
    def get_attn_mask(self, height: int, width: int, window_size: int, shift_size: int) -> Optional[tf.Tensor]: ...
    def maybe_pad(self, hidden_states: tf.Tensor, window_size: int, height: int, width: int) -> Tuple[tf.Tensor, tf.Tensor]: ...
    def call(self, hidden_states: tf.Tensor, input_dimensions: Tuple[int, int], head_mask: Optional[tf.Tensor] = None, output_attentions: bool = False, training: bool = False) -> tf.Tensor: ...

class TFSwinStage(tf.keras.layers.Layer):
    config: Incomplete
    dim: Incomplete
    blocks: Incomplete
    downsample: Incomplete
    pointing: bool
    def __init__(self, config: SwinConfig, dim: int, input_resolution: Tuple[int, int], depth: int, num_heads: int, drop_path: List[float], downsample: Optional[Callable], **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_dimensions: Tuple[int, int], head_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = False, training: bool = False) -> Tuple[tf.Tensor, ...]: ...

class TFSwinEncoder(tf.keras.layers.Layer):
    num_layers: Incomplete
    config: Incomplete
    layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: SwinConfig, grid_size: Tuple[int, int], **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_dimensions: Tuple[int, int], head_mask: Optional[tf.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True, training: bool = False) -> Union[Tuple[tf.Tensor, ...], TFSwinEncoderOutput]: ...

class TFSwinPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = SwinConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]:
        """
        Dummy inputs to build the network. Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """
    def serving(self, inputs): ...

SWIN_START_DOCSTRING: str
SWIN_INPUTS_DOCSTRING: str

def normalize_data_format(value: str) -> str:
    """
    From tensorflow addons
    https://github.com/tensorflow/addons/blob/8cec33fcaaf1cf90aec7bdd55a0fcdbb251ce5c2/tensorflow_addons/utils/keras_utils.py#L71
    """

class AdaptiveAveragePooling1D(tf.keras.layers.Layer):
    """
    Args:
    Average 1D Pooling with adaptive kernel size.
      output_size: An integer or tuple/list of a single integer, specifying pooled_features.
        The new size of output channels.
      data_format: A string,
        one of `channels_last` (default) or `channels_first`. The ordering of the dimensions in the inputs.
        `channels_last` corresponds to inputs with shape `(batch, steps, channels)` while `channels_first` corresponds
        to inputs with shape `(batch, channels, steps)`.
    Input shape:
      - If `data_format='channels_last'`: 3D tensor with shape `(batch, steps, channels)`.
      - If `data_format='channels_first'`: 3D tensor with shape `(batch, channels, steps)`.
    Output shape:
      - If `data_format='channels_last'`: 3D tensor with shape `(batch_size, pooled_steps, channels)`.
      - If `data_format='channels_first'`: 3D tensor with shape `(batch_size, channels, pooled_steps)`.

    Adapted from [tensorflow-addon's adaptive pooling.py](
        https://github.com/tensorflow/addons/blob/8cec33fcaaf1cf90aec7bdd55a0fcdbb251ce5c2/tensorflow_addons/layers/adaptive_pooling.py#L90-L120
    )
    """
    data_format: Incomplete
    reduce_function: Incomplete
    output_size: Incomplete
    def __init__(self, output_size: Union[int, Iterable[int]], reduce_function: Callable = ..., data_format: Optional[str] = None, **kwargs) -> None: ...
    def call(self, inputs: tf.Tensor, *args) -> None: ...
    def compute_output_shape(self, input_shape: Iterable[int]) -> tf.TensorShape: ...
    def get_config(self) -> Dict[str, Any]: ...

class TFSwinMainLayer(tf.keras.layers.Layer):
    config_class = SwinConfig
    config: Incomplete
    num_layers: Incomplete
    num_features: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    pooler: Incomplete
    def __init__(self, config: SwinConfig, add_pooling_layer: bool = True, use_mask_token: bool = False, **kwargs) -> None: ...
    def get_input_embeddings(self) -> TFSwinPatchEmbeddings: ...
    def get_head_mask(self, head_mask: Optional[Any]) -> List: ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, bool_masked_pos: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFSwinModelOutput, Tuple[tf.Tensor, ...]]: ...

class TFSwinModel(TFSwinPreTrainedModel):
    config: Incomplete
    swin: Incomplete
    def __init__(self, config: SwinConfig, add_pooling_layer: bool = True, use_mask_token: bool = False, **kwargs) -> None: ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, bool_masked_pos: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFSwinModelOutput, Tuple[tf.Tensor, ...]]: ...
    def serving_output(self, output: TFSwinModelOutput) -> TFSwinModelOutput: ...

class TFSwinPixelShuffle(tf.keras.layers.Layer):
    """TF layer implementation of torch.nn.PixelShuffle"""
    upscale_factor: Incomplete
    def __init__(self, upscale_factor: int, **kwargs) -> None: ...
    def call(self, x: tf.Tensor) -> tf.Tensor: ...

class TFSwinDecoder(tf.keras.layers.Layer):
    conv2d: Incomplete
    pixel_shuffle: Incomplete
    def __init__(self, config: SwinConfig, **kwargs) -> None: ...
    def call(self, x: tf.Tensor) -> tf.Tensor: ...

class TFSwinForMaskedImageModeling(TFSwinPreTrainedModel):
    swin: Incomplete
    decoder: Incomplete
    def __init__(self, config: SwinConfig) -> None: ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, bool_masked_pos: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[Tuple, TFSwinMaskedImageModelingOutput]:
        '''
        bool_masked_pos (`tf.Tensor` of shape `(batch_size, num_patches)`):
            Boolean masked positions. Indicates which patches are masked (1) and which aren\'t (0).

        Returns:

        Examples:
        ```python
        >>> from transformers import AutoImageProcessor, TFSwinForMaskedImageModeling
        >>> import tensorflow as tf
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("microsoft/swin-tiny-patch4-window7-224")
        >>> model = TFSwinForMaskedImageModeling.from_pretrained("microsoft/swin-tiny-patch4-window7-224")

        >>> num_patches = (model.config.image_size // model.config.patch_size) ** 2
        >>> pixel_values = image_processor(images=image, return_tensors="tf").pixel_values
        >>> # create random boolean mask of shape (batch_size, num_patches)
        >>> bool_masked_pos = tf.random.uniform((1, num_patches)) >= 0.5

        >>> outputs = model(pixel_values, bool_masked_pos=bool_masked_pos)
        >>> loss, reconstructed_pixel_values = outputs.loss, outputs.logits
        >>> list(reconstructed_pixel_values.shape)
        [1, 3, 224, 224]
        ```'''
    def serving_output(self, output: TFSwinMaskedImageModelingOutput) -> TFSwinMaskedImageModelingOutput: ...

class TFSwinForImageClassification(TFSwinPreTrainedModel, TFSequenceClassificationLoss):
    num_labels: Incomplete
    swin: Incomplete
    classifier: Incomplete
    def __init__(self, config: SwinConfig) -> None: ...
    def call(self, pixel_values: Optional[tf.Tensor] = None, head_mask: Optional[tf.Tensor] = None, labels: Optional[tf.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[Tuple[tf.Tensor, ...], TFSwinImageClassifierOutput]:
        """
        labels (`tf.Tensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
    def serving_output(self, output: TFSwinImageClassifierOutput) -> TFSwinImageClassifierOutput: ...
