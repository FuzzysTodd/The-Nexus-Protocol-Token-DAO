import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...file_utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, replace_return_docstrings as replace_return_docstrings
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput
from ...modeling_tf_utils import TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import logging as logging
from .configuration_vit_mae import ViTMAEConfig as ViTMAEConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Dict, Optional, Tuple, Union

logger: Incomplete

@dataclass
class TFViTMAEModelOutput(ModelOutput):
    """
    Class for TFViTMAEModel's outputs, with potential hidden states and attentions.

    Args:
        last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        mask (`tf.Tensor` of shape `(batch_size, sequence_length)`):
            Tensor indicating which patches are masked (1) and which are not (0).
        ids_restore (`tf.Tensor` of shape `(batch_size, sequence_length)`):
            Tensor containing the original index of the (shuffled) masked patches.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer plus
            the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    """
    last_hidden_state: tf.Tensor = ...
    mask: tf.Tensor = ...
    ids_restore: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, last_hidden_state, mask, ids_restore, hidden_states, attentions) -> None: ...

@dataclass
class TFViTMAEDecoderOutput(ModelOutput):
    """
    Class for TFViTMAEDecoder's outputs, with potential hidden states and attentions.

    Args:
        logits (`tf.Tensor` of shape `(batch_size, sequence_length, patch_size ** 2 * num_channels)`):
            Pixel reconstruction logits.
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
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, logits, hidden_states, attentions) -> None: ...

@dataclass
class TFViTMAEForPreTrainingOutput(ModelOutput):
    """
    Class for TFViTMAEForPreTraining's outputs, with potential hidden states and attentions.

    Args:
        loss (`tf.Tensor` of shape `(1,)`):
            Pixel reconstruction loss.
        logits (`tf.Tensor` of shape `(batch_size, sequence_length, patch_size ** 2 * num_channels)`):
            Pixel reconstruction logits.
        mask (`tf.Tensor` of shape `(batch_size, sequence_length)`):
            Tensor indicating which patches are masked (1) and which are not (0).
        ids_restore (`tf.Tensor` of shape `(batch_size, sequence_length)`):
            Tensor containing the original index of the (shuffled) masked patches.
        hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer plus
            the initial embedding outputs.
        attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    """
    loss: Optional[tf.Tensor] = ...
    logits: tf.Tensor = ...
    mask: tf.Tensor = ...
    ids_restore: tf.Tensor = ...
    hidden_states: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, logits, mask, ids_restore, hidden_states, attentions) -> None: ...

def get_2d_sincos_pos_embed(embed_dim, grid_size, add_cls_token: bool = False):
    """
    Create 2D sin/cos positional embeddings.

    Args:
        embed_dim (`int`):
            Embedding dimension.
        grid_size (`int`):
            The grid height and width.
        add_cls_token (`bool`, *optional*, defaults to `False`):
            Whether or not to add a classification (CLS) token.

    Returns:
        (`tf.Tensor` of shape (grid_size*grid_size, embed_dim) or (1+grid_size*grid_size, embed_dim): the position
        embeddings (with or without classification token)
    """
def get_2d_sincos_pos_embed_from_grid(embed_dim, grid): ...
def get_1d_sincos_pos_embed_from_grid(embed_dim, pos):
    """
    embed_dim: output dimension for each position pos: a list of positions to be encoded: size (M,) out: (M, D)
    """

class TFViTMAEEmbeddings(tf.keras.layers.Layer):
    """
    Construct the CLS token, position and patch embeddings.

    """
    patch_embeddings: Incomplete
    num_patches: Incomplete
    config: Incomplete
    def __init__(self, config: ViTMAEConfig, **kwargs) -> None: ...
    cls_token: Incomplete
    position_embeddings: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def random_masking(self, sequence: tf.Tensor, noise: Optional[tf.Tensor] = None):
        """
        Perform per-sample random masking by per-sample shuffling. Per-sample shuffling is done by argsort random
        noise.

        Args:
            sequence (`tf.Tensor` of shape `(batch_size, sequence_length, dim)`)
            noise (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*) which is
                mainly used for testing purposes to control randomness and maintain the reproducibility
        """
    def call(self, pixel_values: tf.Tensor, noise: tf.Tensor = None) -> tf.Tensor: ...

class TFViTMAEPatchEmbeddings(tf.keras.layers.Layer):
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
    def __init__(self, config: ViTMAEConfig, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFViTMAESelfAttention(tf.keras.layers.Layer):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    sqrt_att_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config: ViTMAEConfig, **kwargs) -> None: ...
    def transpose_for_scores(self, tensor: tf.Tensor, batch_size: int) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFViTMAESelfOutput(tf.keras.layers.Layer):
    """
    The residual connection is defined in TFViTMAELayer instead of here (as is the case with other models), due to the
    layernorm applied before each block.
    """
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: ViTMAEConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFViTMAEAttention(tf.keras.layers.Layer):
    self_attention: Incomplete
    dense_output: Incomplete
    def __init__(self, config: ViTMAEConfig, **kwargs) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def call(self, input_tensor: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFViTMAEIntermediate(tf.keras.layers.Layer):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: ViTMAEConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFViTMAEOutput(tf.keras.layers.Layer):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: ViTMAEConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, input_tensor: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFViTMAELayer(tf.keras.layers.Layer):
    """This corresponds to the Block class in the timm implementation."""
    attention: Incomplete
    intermediate: Incomplete
    vit_output: Incomplete
    layernorm_before: Incomplete
    layernorm_after: Incomplete
    def __init__(self, config: ViTMAEConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]: ...

class TFViTMAEEncoder(tf.keras.layers.Layer):
    layer: Incomplete
    def __init__(self, config: ViTMAEConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, head_mask: tf.Tensor, output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...

class TFViTMAEMainLayer(tf.keras.layers.Layer):
    config_class = ViTMAEConfig
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    def __init__(self, config: ViTMAEConfig, **kwargs) -> None: ...
    def get_input_embeddings(self) -> tf.keras.layers.Layer: ...
    def call(self, pixel_values: Optional[TFModelInputType] = None, noise: tf.Tensor = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFViTMAEModelOutput, Tuple[tf.Tensor]]: ...

class TFViTMAEPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ViTMAEConfig
    base_model_prefix: str
    main_input_name: str
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]:
        """
        Dummy inputs to build the network. Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """
    def serving(self, inputs):
        """
        Method used for serving the model.

        Args:
            inputs (`Dict[str, tf.Tensor]`):
                The input of the saved model as a dictionary of tensors.
        """

VIT_MAE_START_DOCSTRING: str
VIT_MAE_INPUTS_DOCSTRING: str

class TFViTMAEModel(TFViTMAEPreTrainedModel):
    vit: Incomplete
    def __init__(self, config: ViTMAEConfig, *inputs, **kwargs) -> None: ...
    def get_input_embeddings(self): ...
    def call(self, pixel_values: Optional[TFModelInputType] = None, noise: tf.Tensor = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFViTMAEModelOutput, Tuple[tf.Tensor]]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, TFViTMAEModel
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("facebook/vit-mae-base")
        >>> model = TFViTMAEModel.from_pretrained("facebook/vit-mae-base")

        >>> inputs = image_processor(images=image, return_tensors="tf")
        >>> outputs = model(**inputs)
        >>> last_hidden_states = outputs.last_hidden_state
        ```'''
    def serving_output(self, output: TFViTMAEModelOutput) -> TFViTMAEModelOutput: ...

class TFViTMAEDecoder(tf.keras.layers.Layer):
    decoder_embed: Incomplete
    decoder_layers: Incomplete
    decoder_norm: Incomplete
    decoder_pred: Incomplete
    config: Incomplete
    num_patches: Incomplete
    def __init__(self, config, num_patches, **kwargs) -> None: ...
    mask_token: Incomplete
    decoder_pos_embed: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def call(self, hidden_states, ids_restore, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class TFViTMAEForPreTraining(TFViTMAEPreTrainedModel):
    config: Incomplete
    vit: Incomplete
    decoder: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def patchify(self, pixel_values):
        """
        Args:
            pixel_values (`tf.Tensor` of shape `(batch_size, height, width, num_channels)` or `(batch_size, num_channels, height, width)`):
                Pixel values.

        Returns:
            `tf.Tensor` of shape `(batch_size, num_patches, patch_size**2 * num_channels)`:
                Patchified pixel values.
        """
    def unpatchify(self, patchified_pixel_values):
        """
        Args:
            patchified_pixel_values (`tf.Tensor` of shape `(batch_size, num_patches, patch_size**2 * num_channels)`:
                Patchified pixel values.

        Returns:
            `tf.Tensor` of shape `(batch_size, height, width, num_channels)`:
                Pixel values.
        """
    def forward_loss(self, pixel_values, pred, mask):
        """
        Args:
            pixel_values (`tf.Tensor` of shape `(batch_size, height, width, num_channels)`):
                Pixel values.
            pred (`tf.Tensor` of shape `(batch_size, num_patches, patch_size**2 * num_channels)`:
                Predicted pixel values.
            mask (`tf.Tensor` of shape `(batch_size, sequence_length)`):
                Tensor indicating which patches are masked (1) and which are not (0).

        Returns:
            `tf.Tensor`: Pixel reconstruction loss.
        """
    def call(self, pixel_values: Optional[TFModelInputType] = None, noise: tf.Tensor = None, head_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFViTMAEForPreTrainingOutput, Tuple[tf.Tensor]]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, TFViTMAEForPreTraining
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("facebook/vit-mae-base")
        >>> model = TFViTMAEForPreTraining.from_pretrained("facebook/vit-mae-base")

        >>> inputs = image_processor(images=image, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> loss = outputs.loss
        >>> mask = outputs.mask
        >>> ids_restore = outputs.ids_restore
        ```'''
    def serving_output(self, output: TFViTMAEForPreTrainingOutput) -> TFViTMAEForPreTrainingOutput: ...
