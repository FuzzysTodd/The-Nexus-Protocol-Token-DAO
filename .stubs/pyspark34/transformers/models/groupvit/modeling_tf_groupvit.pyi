import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFBaseModelOutputWithPooling as TFBaseModelOutputWithPooling
from ...modeling_tf_utils import DUMMY_INPUTS as DUMMY_INPUTS, TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, is_tensorflow_probability_available as is_tensorflow_probability_available, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_groupvit import GroupViTConfig as GroupViTConfig, GroupViTTextConfig as GroupViTTextConfig, GroupViTVisionConfig as GroupViTVisionConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple, Union

logger: Incomplete
_: Incomplete
TF_GROUPVIT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
LARGE_NEGATIVE: float

def contrastive_loss(logits: tf.Tensor) -> tf.Tensor: ...
def groupvit_loss(similarity: tf.Tensor) -> tf.Tensor: ...
def hard_softmax(logits: tf.Tensor, dim: int) -> tf.Tensor: ...
def gumbel_softmax(logits: tf.Tensor, tau: float = 1, hard: bool = False, dim: int = -1) -> tf.Tensor: ...
def resize_attention_map(attentions: tf.Tensor, height: int, width: int, align_corners: bool = False) -> tf.Tensor:
    """
    Args:
        attentions (`tf.Tensor`): attention map of shape [batch_size, groups, feat_height*feat_width]
        height (`int`): height of the output attention map
        width (`int`): width of the output attention map
        align_corners (`bool`, *optional*): the `align_corner` argument for `nn.functional.interpolate`.

    Returns:
        `tf.Tensor`: resized attention map of shape [batch_size, groups, height, width]
    """
def get_grouping_from_attentions(attentions: Tuple[tf.Tensor], hw_shape: Tuple[int]) -> tf.Tensor:
    """
    Args:
        attentions (`tuple(tf.Tensor)`: tuple of attention maps returned by `TFGroupViTVisionTransformer`
        hw_shape (`tuple(int)`): height and width of the output attention map
    Returns:
        `tf.Tensor`: the attention map of shape [batch_size, groups, height, width]
    """

@dataclass
class TFGroupViTModelOutput(ModelOutput):
    """
    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `return_loss` is `True`):
            Contrastive loss for image-text similarity.
        logits_per_image (`tf.Tensor` of shape `(image_batch_size, text_batch_size)`):
            The scaled dot product scores between `image_embeds` and `text_embeds`. This represents the image-text
            similarity scores.
        logits_per_text (`tf.Tensor` of shape `(text_batch_size, image_batch_size)`):
            The scaled dot product scores between `text_embeds` and `image_embeds`. This represents the text-image
            similarity scores.
        segmentation_logits (`tf.Tensor` of shape `(batch_size, config.num_labels, logits_height, logits_width)`):
            Classification scores for each pixel.

            <Tip warning={true}>

            The logits returned do not necessarily have the same size as the `pixel_values` passed as inputs. This is
            to avoid doing two interpolations and lose some quality when a user needs to resize the logits to the
            original image size as post-processing. You should always check your logits shape and resize as needed.

            </Tip>

        text_embeds (`tf.Tensor` of shape `(batch_size, output_dim`):
            The text embeddings obtained by applying the projection layer to the pooled output of
            [`TFGroupViTTextModel`].
        image_embeds (`tf.Tensor` of shape `(batch_size, output_dim`):
            The image embeddings obtained by applying the projection layer to the pooled output of
            [`TFGroupViTVisionModel`].
        text_model_output (`TFBaseModelOutputWithPooling`):
            The output of the [`TFGroupViTTextModel`].
        vision_model_output (`TFBaseModelOutputWithPooling`):
            The output of the [`TFGroupViTVisionModel`].
    """
    loss: Optional[tf.Tensor] = ...
    logits_per_image: tf.Tensor = ...
    logits_per_text: tf.Tensor = ...
    segmentation_logits: tf.Tensor = ...
    text_embeds: tf.Tensor = ...
    image_embeds: tf.Tensor = ...
    text_model_output: TFBaseModelOutputWithPooling = ...
    vision_model_output: TFBaseModelOutputWithPooling = ...
    def to_tuple(self) -> Tuple[Any]: ...
    def __init__(self, loss, logits_per_image, logits_per_text, segmentation_logits, text_embeds, image_embeds, text_model_output, vision_model_output) -> None: ...

class TFGroupViTCrossAttentionLayer(tf.keras.layers.Layer):
    attn: Incomplete
    norm2: Incomplete
    mlp: Incomplete
    norm_post: Incomplete
    def __init__(self, config: GroupViTVisionConfig, **kwargs) -> None: ...
    def call(self, query: tf.Tensor, key: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFGroupViTAssignAttention(tf.keras.layers.Layer):
    scale: Incomplete
    q_proj: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    proj: Incomplete
    assign_eps: Incomplete
    def __init__(self, config: GroupViTVisionConfig, **kwargs) -> None: ...
    def get_attn(self, attn: tf.Tensor, gumbel: bool = True, hard: bool = True, training: bool = False) -> tf.Tensor: ...
    def call(self, query: tf.Tensor, key: tf.Tensor, training: bool = False): ...

class TFGroupViTTokenAssign(tf.keras.layers.Layer):
    num_output_group: Incomplete
    norm_tokens: Incomplete
    mlp_inter: Incomplete
    norm_post_tokens: Incomplete
    norm_x: Incomplete
    pre_assign_attn: Incomplete
    assign: Incomplete
    norm_new_x: Incomplete
    mlp_channels: Incomplete
    def __init__(self, config: GroupViTVisionConfig, num_group_token: int, num_output_group: int, **kwargs) -> None: ...
    def project_group_token(self, group_tokens: tf.Tensor) -> tf.Tensor:
        """
        Args:
            group_tokens (tf.Tensor): group tokens, [batch_size, num_group_tokens, channels]

        Returns:
            projected_group_tokens (tf.Tensor): [batch_size, num_output_groups, channels]
        """
    def call(self, image_tokens: tf.Tensor, group_tokens: tf.Tensor, training: bool = False):
        """
        Args:
            image_tokens (`tf.Tensor`): image tokens, of shape [batch_size, input_length, channels]
            group_tokens (`tf.Tensor`): group tokens, [batch_size, num_group_tokens, channels]
        """

class TFGroupViTPatchEmbeddings(tf.keras.layers.Layer):
    """
    This class turns `pixel_values` of shape `(batch_size, num_channels, height, width)` into the initial
    `hidden_states` (patch embeddings) of shape `(batch_size, seq_length, hidden_size)` to be consumed by a
    Transformer.
    """
    hidden_size: Incomplete
    image_size: Incomplete
    patch_size: Incomplete
    num_patches: Incomplete
    num_channels: Incomplete
    config: Incomplete
    projection: Incomplete
    def __init__(self, config: GroupViTConfig, **kwargs) -> None: ...
    def call(self, pixel_values: tf.Tensor, interpolate_pos_encoding: bool = False, training: bool = False) -> tf.Tensor: ...

class TFGroupViTVisionEmbeddings(tf.keras.layers.Layer):
    """
    Construct the position and patch embeddings.

    """
    patch_embeddings: Incomplete
    dropout: Incomplete
    layernorm: Incomplete
    config: Incomplete
    def __init__(self, config: GroupViTVisionConfig, **kwargs) -> None: ...
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

class TFGroupViTTextEmbeddings(tf.keras.layers.Layer):
    embed_dim: Incomplete
    config: Incomplete
    def __init__(self, config: GroupViTTextConfig, **kwargs) -> None: ...
    weight: Incomplete
    position_embedding: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def call(self, input_ids: tf.Tensor = None, position_ids: tf.Tensor = None, inputs_embeds: tf.Tensor = None) -> tf.Tensor:
        """
        Applies embedding based on inputs tensor.

        Returns:
            final_embeddings (`tf.Tensor`): output embedding tensor.
        """

class TFGroupViTStage(tf.keras.layers.Layer):
    """This corresponds to the `GroupingLayer` class in the GroupViT implementation."""
    config: Incomplete
    depth: Incomplete
    num_group_token: Incomplete
    layers: Incomplete
    downsample: Incomplete
    group_projector: Incomplete
    def __init__(self, config: GroupViTVisionConfig, depth: int, num_prev_group_token: int, num_group_token: int, num_output_group: int, **kwargs) -> None: ...
    group_token: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    @property
    def with_group_token(self): ...
    def split_x(self, x: tf.Tensor) -> tf.Tensor: ...
    def concat_x(self, x: tf.Tensor, group_token: Optional[tf.Tensor] = None) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, prev_group_token: Optional[tf.Tensor] = None, output_attentions: bool = False, training: bool = False) -> Tuple[tf.Tensor]:
        """
        Args:
            hidden_states (`tf.Tensor`): input to the layer of shape `(batch, seq_len, embed_dim)`
            attention_mask (`tf.Tensor`): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
                `(config.encoder_attention_heads,)`.
            output_attentions (`bool`, *optional*):
                Whether or not to return the grouping tensors of Grouping block.
        """

class TFGroupViTMLP(tf.keras.layers.Layer):
    config: Incomplete
    activation_fn: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    def __init__(self, config: GroupViTVisionConfig, hidden_size: Optional[int] = None, intermediate_size: Optional[int] = None, output_size: Optional[int] = None, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, training: bool = False) -> tf.Tensor: ...

class TFGroupViTMixerMLP(TFGroupViTMLP):
    def call(self, x, training: bool = False): ...

class TFGroupViTAttention(tf.keras.layers.Layer):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    embed_dim: Incomplete
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    sqrt_att_head_size: Incomplete
    q_proj: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def __init__(self, config: GroupViTConfig, **kwargs) -> None: ...
    def transpose_for_scores(self, tensor: tf.Tensor, batch_size: int) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor = None, causal_attention_mask: tf.Tensor = None, output_attentions: bool = None, encoder_hidden_states: tf.Tensor = None, training: bool = False) -> Tuple[tf.Tensor]:
        """Input shape: Batch x Time x Channel"""

class TFGroupViTEncoderLayer(tf.keras.layers.Layer):
    embed_dim: Incomplete
    self_attn: Incomplete
    layer_norm1: Incomplete
    mlp: Incomplete
    layer_norm2: Incomplete
    def __init__(self, config: GroupViTConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, causal_attention_mask: tf.Tensor, output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]:
        """
        Args:
            hidden_states (`tf.Tensor`): input to the layer of shape `(batch, seq_len, embed_dim)`
            attention_mask (`tf.Tensor`): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            causal_attention_mask (`tf.Tensor`): causal attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            output_attentions (`bool`):
                Whether or not to return the attentions tensors of all attention layers. See `outputs` under returned
                tensors for more detail.
        """

class TFGroupViTTextEncoder(tf.keras.layers.Layer):
    layers: Incomplete
    def __init__(self, config: GroupViTTextConfig, **kwargs) -> None: ...
    def call(self, hidden_states, attention_mask: tf.Tensor, causal_attention_mask: tf.Tensor, output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = False) -> Union[Tuple, TFBaseModelOutput]: ...

class TFGroupViTVisionEncoder(tf.keras.layers.Layer):
    stages: Incomplete
    def __init__(self, config: GroupViTVisionConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, output_hidden_states: bool, output_attentions: bool, return_dict: bool, training: bool = False) -> Union[tuple, TFBaseModelOutput]: ...

class TFGroupViTTextTransformer(tf.keras.layers.Layer):
    embeddings: Incomplete
    encoder: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: GroupViTTextConfig, **kwargs) -> None: ...
    def call(self, input_ids: TFModelInputType, attention_mask: tf.Tensor, position_ids: tf.Tensor, output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]: ...

class TFGroupViTVisionTransformer(tf.keras.layers.Layer):
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    def __init__(self, config: GroupViTVisionConfig, **kwargs) -> None: ...
    def call(self, pixel_values: TFModelInputType, output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = False) -> Union[Tuple, TFBaseModelOutputWithPooling]: ...

class TFGroupViTTextMainLayer(tf.keras.layers.Layer):
    config_class = GroupViTTextConfig
    config: Incomplete
    text_model: Incomplete
    def __init__(self, config: GroupViTTextConfig, **kwargs) -> None: ...
    def get_input_embeddings(self) -> tf.keras.layers.Layer: ...
    def set_input_embeddings(self, value: tf.Variable): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]: ...

class TFGroupViTVisionMainLayer(tf.keras.layers.Layer):
    config_class = GroupViTVisionConfig
    config: Incomplete
    vision_model: Incomplete
    def __init__(self, config: GroupViTVisionConfig, **kwargs) -> None: ...
    def get_input_embeddings(self) -> tf.keras.layers.Layer: ...
    def call(self, pixel_values: Optional[TFModelInputType] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]: ...

class TFGroupViTMainLayer(tf.keras.layers.Layer):
    config_class = GroupViTConfig
    config: Incomplete
    projection_dim: Incomplete
    projection_intermediate_dim: Incomplete
    text_embed_dim: Incomplete
    vision_embed_dim: Incomplete
    text_model: Incomplete
    vision_model: Incomplete
    visual_projection: Incomplete
    text_projection: Incomplete
    def __init__(self, config: GroupViTConfig, **kwargs) -> None: ...
    logit_scale: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def get_text_features(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> tf.Tensor: ...
    def get_image_features(self, pixel_values: Optional[TFModelInputType] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> tf.Tensor: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, pixel_values: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, return_loss: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_segmentation: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFGroupViTModelOutput, Tuple[tf.Tensor]]: ...

class TFGroupViTPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = GroupViTConfig
    base_model_prefix: str

GROUPVIT_START_DOCSTRING: str
GROUPVIT_TEXT_INPUTS_DOCSTRING: str
GROUPVIT_VISION_INPUTS_DOCSTRING: str
GROUPVIT_INPUTS_DOCSTRING: str

class TFGroupViTTextModel(TFGroupViTPreTrainedModel):
    config_class = GroupViTTextConfig
    main_input_name: str
    groupvit: Incomplete
    def __init__(self, config: GroupViTTextConfig, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]:
        """
        Dummy inputs to build the network.

        Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """
    def serving(self, inputs: Dict[str, tf.Tensor]) -> TFBaseModelOutputWithPooling: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import CLIPTokenizer, TFGroupViTTextModel

        >>> tokenizer = CLIPTokenizer.from_pretrained("nvidia/groupvit-gcc-yfcc")
        >>> model = TFGroupViTTextModel.from_pretrained("nvidia/groupvit-gcc-yfcc")

        >>> inputs = tokenizer(["a photo of a cat", "a photo of a dog"], padding=True, return_tensors="tf")

        >>> outputs = model(**inputs)
        >>> last_hidden_state = outputs.last_hidden_state
        >>> pooled_output = outputs.pooler_output  # pooled (EOS token) states
        ```'''
    def serving_output(self, output: TFBaseModelOutputWithPooling) -> TFBaseModelOutputWithPooling: ...

class TFGroupViTVisionModel(TFGroupViTPreTrainedModel):
    config_class = GroupViTVisionConfig
    main_input_name: str
    groupvit: Incomplete
    def __init__(self, config: GroupViTVisionConfig, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]:
        """
        Dummy inputs to build the network.

        Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """
    def serving(self, inputs: Dict[str, tf.Tensor]) -> TFBaseModelOutputWithPooling:
        """
        Method used for serving the model.

        Args:
            inputs (`Dict[str, tf.Tensor]`):
                The input of the saved model as a dictionary of tensors.
        """
    def call(self, pixel_values: Optional[TFModelInputType] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]:
        '''
        Returns:

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, TFGroupViTVisionModel

        >>> processor = AutoProcessor.from_pretrained("nvidia/groupvit-gcc-yfcc")
        >>> model = TFGroupViTVisionModel.from_pretrained("nvidia/groupvit-gcc-yfcc")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="tf")

        >>> outputs = model(**inputs)
        >>> last_hidden_state = outputs.last_hidden_state
        >>> pooled_output = outputs.pooler_output  # pooled CLS states
        ```'''
    def serving_output(self, output: TFBaseModelOutputWithPooling) -> TFBaseModelOutputWithPooling: ...

class TFGroupViTModel(TFGroupViTPreTrainedModel):
    config_class = GroupViTConfig
    groupvit: Incomplete
    def __init__(self, config: GroupViTConfig, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]:
        """
        Dummy inputs to build the network.

        Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """
    def serving(self, inputs: Dict[str, tf.Tensor]) -> TFGroupViTModelOutput:
        """
        Method used for serving the model.

        Args:
            inputs (`Dict[str, tf.Tensor]`):
                The input of the saved model as a dictionary of tensors.
        """
    def get_text_features(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> tf.Tensor:
        '''
        Returns:
            text_features (`tf.Tensor` of shape `(batch_size, output_dim`): The text embeddings obtained by applying
            the projection layer to the pooled output of [`TFGroupViTTextModel`].

        Examples:

        ```python
        >>> from transformers import CLIPTokenizer, TFGroupViTModel

        >>> model = TFGroupViTModel.from_pretrained("nvidia/groupvit-gcc-yfcc")
        >>> tokenizer = CLIPTokenizer.from_pretrained("nvidia/groupvit-gcc-yfcc")

        >>> inputs = tokenizer(["a photo of a cat", "a photo of a dog"], padding=True, return_tensors="tf")
        >>> text_features = model.get_text_features(**inputs)
        ```'''
    def get_image_features(self, pixel_values: Optional[TFModelInputType] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> tf.Tensor:
        '''
        Returns:
            image_features (`tf.Tensor` of shape `(batch_size, output_dim`): The image embeddings obtained by applying
            the projection layer to the pooled output of [`TFGroupViTVisionModel`].

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, TFGroupViTModel

        >>> model = TFGroupViTModel.from_pretrained("nvidia/groupvit-gcc-yfcc")
        >>> processor = AutoProcessor.from_pretrained("nvidia/groupvit-gcc-yfcc")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="tf")

        >>> image_features = model.get_image_features(**inputs)
        ```'''
    def call(self, input_ids: Optional[TFModelInputType] = None, pixel_values: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, return_loss: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_segmentation: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFGroupViTModelOutput, Tuple[tf.Tensor]]:
        '''
        Returns:

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, TFGroupViTModel
        >>> import tensorflow as tf

        >>> model = TFGroupViTModel.from_pretrained("nvidia/groupvit-gcc-yfcc")
        >>> processor = AutoProcessor.from_pretrained("nvidia/groupvit-gcc-yfcc")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(
        ...     text=["a photo of a cat", "a photo of a dog"], images=image, return_tensors="tf", padding=True
        ... )

        >>> outputs = model(**inputs)
        >>> logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
        >>> probs = tf.math.softmax(logits_per_image, axis=1)  # we can take the softmax to get the label probabilities
        ```'''
    def serving_output(self, output: TFGroupViTModelOutput) -> TFGroupViTModelOutput: ...
