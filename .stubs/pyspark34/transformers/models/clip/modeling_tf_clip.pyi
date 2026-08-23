import numpy as np
import tensorflow as tf
from ...activations_tf import get_tf_activation as get_tf_activation
from ...modeling_tf_outputs import TFBaseModelOutput as TFBaseModelOutput, TFBaseModelOutputWithPooling as TFBaseModelOutputWithPooling
from ...modeling_tf_utils import DUMMY_INPUTS as DUMMY_INPUTS, TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, get_initializer as get_initializer, keras_serializable as keras_serializable, unpack_inputs as unpack_inputs
from ...tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_clip import CLIPConfig as CLIPConfig, CLIPTextConfig as CLIPTextConfig, CLIPVisionConfig as CLIPVisionConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple, Union

logger: Incomplete
TF_CLIP_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
LARGE_NEGATIVE: float

def contrastive_loss(logits: tf.Tensor) -> tf.Tensor: ...
def clip_loss(similarity: tf.Tensor) -> tf.Tensor: ...

@dataclass
class TFCLIPOutput(ModelOutput):
    """
    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `return_loss` is `True`):
            Contrastive loss for image-text similarity.
        logits_per_image:(`tf.Tensor` of shape `(image_batch_size, text_batch_size)`):
            The scaled dot product scores between `image_embeds` and `text_embeds`. This represents the image-text
            similarity scores.
        logits_per_text:(`tf.Tensor` of shape `(text_batch_size, image_batch_size)`):
            The scaled dot product scores between `text_embeds` and `image_embeds`. This represents the text-image
            similarity scores.
        text_embeds(`tf.Tensor` of shape `(batch_size, output_dim`):
            The text embeddings obtained by applying the projection layer to the pooled output of [`TFCLIPTextModel`].
        image_embeds(`tf.Tensor` of shape `(batch_size, output_dim`):
            The image embeddings obtained by applying the projection layer to the pooled output of
            [`TFCLIPVisionModel`].
        text_model_output([`~modeling_tf_utils.TFBaseModelOutputWithPooling`]):
            The output of the [`TFCLIPTextModel`].
        vision_model_output([`~modeling_tf_utils.TFBaseModelOutputWithPooling`]):
            The output of the [`TFCLIPVisionModel`].
    """
    loss: Optional[tf.Tensor] = ...
    logits_per_image: tf.Tensor = ...
    logits_per_text: tf.Tensor = ...
    text_embeds: tf.Tensor = ...
    image_embeds: tf.Tensor = ...
    text_model_output: TFBaseModelOutputWithPooling = ...
    vision_model_output: TFBaseModelOutputWithPooling = ...
    def to_tuple(self) -> Tuple[Any]: ...
    def __init__(self, loss, logits_per_image, logits_per_text, text_embeds, image_embeds, text_model_output, vision_model_output) -> None: ...

class TFCLIPVisionEmbeddings(tf.keras.layers.Layer):
    embed_dim: Incomplete
    image_size: Incomplete
    patch_size: Incomplete
    num_patches: Incomplete
    num_positions: Incomplete
    config: Incomplete
    patch_embedding: Incomplete
    def __init__(self, config: CLIPVisionConfig, **kwargs) -> None: ...
    class_embedding: Incomplete
    position_embedding: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def call(self, pixel_values: tf.Tensor) -> tf.Tensor:
        """`pixel_values` is expected to be of NCHW format."""

class TFCLIPTextEmbeddings(tf.keras.layers.Layer):
    embed_dim: Incomplete
    config: Incomplete
    def __init__(self, config: CLIPTextConfig, **kwargs) -> None: ...
    weight: Incomplete
    position_embedding: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def call(self, input_ids: tf.Tensor = None, position_ids: tf.Tensor = None, inputs_embeds: tf.Tensor = None) -> tf.Tensor:
        """
        Applies embedding based on inputs tensor.

        Returns:
            final_embeddings (`tf.Tensor`): output embedding tensor.
        """

class TFCLIPAttention(tf.keras.layers.Layer):
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
    def __init__(self, config: CLIPConfig, **kwargs) -> None: ...
    def transpose_for_scores(self, tensor: tf.Tensor, batch_size: int) -> tf.Tensor: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, causal_attention_mask: tf.Tensor, output_attentions: bool, training: bool = False) -> Tuple[tf.Tensor]:
        """Input shape: Batch x Time x Channel"""

class TFCLIPMLP(tf.keras.layers.Layer):
    activation_fn: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    def __init__(self, config: CLIPConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor) -> tf.Tensor: ...

class TFCLIPEncoderLayer(tf.keras.layers.Layer):
    embed_dim: Incomplete
    self_attn: Incomplete
    layer_norm1: Incomplete
    mlp: Incomplete
    layer_norm2: Incomplete
    def __init__(self, config: CLIPConfig, **kwargs) -> None: ...
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

class TFCLIPEncoder(tf.keras.layers.Layer):
    """
    Transformer encoder consisting of `config.num_hidden_layers` self attention layers. Each layer is a
    [`TFCLIPEncoderLayer`].

    Args:
        config: CLIPConfig
    """
    layers: Incomplete
    def __init__(self, config: CLIPConfig, **kwargs) -> None: ...
    def call(self, hidden_states: tf.Tensor, attention_mask: tf.Tensor, causal_attention_mask: tf.Tensor, output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = False) -> Union[TFBaseModelOutput, Tuple[tf.Tensor]]: ...

class TFCLIPTextTransformer(tf.keras.layers.Layer):
    embeddings: Incomplete
    encoder: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: CLIPTextConfig, **kwargs) -> None: ...
    def call(self, input_ids: TFModelInputType, attention_mask: tf.Tensor, position_ids: tf.Tensor, output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]: ...

class TFCLIPTextMainLayer(tf.keras.layers.Layer):
    config_class = CLIPTextConfig
    config: Incomplete
    text_model: Incomplete
    def __init__(self, config: CLIPTextConfig, **kwargs) -> None: ...
    def get_input_embeddings(self) -> tf.keras.layers.Layer: ...
    def set_input_embeddings(self, value: tf.Variable): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]: ...

class TFCLIPVisionTransformer(tf.keras.layers.Layer):
    embeddings: Incomplete
    pre_layernorm: Incomplete
    encoder: Incomplete
    post_layernorm: Incomplete
    def __init__(self, config: CLIPVisionConfig, **kwargs) -> None: ...
    def call(self, pixel_values: TFModelInputType, output_attentions: bool, output_hidden_states: bool, return_dict: bool, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]: ...

class TFCLIPVisionMainLayer(tf.keras.layers.Layer):
    config_class = CLIPVisionConfig
    config: Incomplete
    vision_model: Incomplete
    def __init__(self, config: CLIPVisionConfig, **kwargs) -> None: ...
    def get_input_embeddings(self) -> tf.keras.layers.Layer: ...
    def call(self, pixel_values: Optional[TFModelInputType] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]: ...

class TFCLIPMainLayer(tf.keras.layers.Layer):
    config_class = CLIPConfig
    config: Incomplete
    projection_dim: Incomplete
    text_model: Incomplete
    vision_model: Incomplete
    visual_projection: Incomplete
    text_projection: Incomplete
    def __init__(self, config: CLIPConfig, **kwargs) -> None: ...
    logit_scale: Incomplete
    def build(self, input_shape: tf.TensorShape): ...
    def get_text_features(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> tf.Tensor: ...
    def get_image_features(self, pixel_values: Optional[TFModelInputType] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> tf.Tensor: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, pixel_values: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, return_loss: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFCLIPOutput, Tuple[tf.Tensor]]: ...

class TFCLIPPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = CLIPConfig
    base_model_prefix: str

CLIP_START_DOCSTRING: str
CLIP_TEXT_INPUTS_DOCSTRING: str
CLIP_VISION_INPUTS_DOCSTRING: str
CLIP_INPUTS_DOCSTRING: str

class TFCLIPTextModel(TFCLIPPreTrainedModel):
    config_class = CLIPTextConfig
    clip: Incomplete
    def __init__(self, config: CLIPTextConfig, *inputs, **kwargs) -> None: ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, TFCLIPTextModel

        >>> model = TFCLIPTextModel.from_pretrained("openai/clip-vit-base-patch32")
        >>> tokenizer = AutoTokenizer.from_pretrained("openai/clip-vit-base-patch32")

        >>> inputs = tokenizer(["a photo of a cat", "a photo of a dog"], padding=True, return_tensors="tf")

        >>> outputs = model(**inputs)
        >>> last_hidden_state = outputs.last_hidden_state
        >>> pooled_output = outputs.pooler_output  # pooled (EOS token) states
        ```'''
    def serving(self, inputs: Dict[str, tf.Tensor]) -> TFBaseModelOutputWithPooling: ...
    def serving_output(self, output: TFBaseModelOutputWithPooling) -> TFBaseModelOutputWithPooling: ...

class TFCLIPVisionModel(TFCLIPPreTrainedModel):
    config_class = CLIPVisionConfig
    main_input_name: str
    clip: Incomplete
    def __init__(self, config: CLIPVisionConfig, *inputs, **kwargs) -> None: ...
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
    def call(self, pixel_values: Optional[TFModelInputType] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: Optional[bool] = False) -> Union[TFBaseModelOutputWithPooling, Tuple[tf.Tensor]]:
        '''
        Returns:

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, TFCLIPVisionModel

        >>> model = TFCLIPVisionModel.from_pretrained("openai/clip-vit-base-patch32")
        >>> processor = AutoProcessor.from_pretrained("openai/clip-vit-base-patch32")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="tf")

        >>> outputs = model(**inputs)
        >>> last_hidden_state = outputs.last_hidden_state
        >>> pooled_output = outputs.pooler_output  # pooled CLS states
        ```'''
    def serving_output(self, output: TFBaseModelOutputWithPooling) -> TFBaseModelOutputWithPooling: ...

class TFCLIPModel(TFCLIPPreTrainedModel):
    config_class = CLIPConfig
    clip: Incomplete
    def __init__(self, config: CLIPConfig, *inputs, **kwargs) -> None: ...
    @property
    def dummy_inputs(self) -> Dict[str, tf.Tensor]:
        """
        Dummy inputs to build the network.

        Returns:
            `Dict[str, tf.Tensor]`: The dummy inputs.
        """
    def serving(self, inputs: Dict[str, tf.Tensor]) -> TFCLIPOutput:
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
            the projection layer to the pooled output of [`TFCLIPTextModel`].

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, TFCLIPModel

        >>> model = TFCLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        >>> tokenizer = AutoTokenizer.from_pretrained("openai/clip-vit-base-patch32")

        >>> inputs = tokenizer(["a photo of a cat", "a photo of a dog"], padding=True, return_tensors="tf")
        >>> text_features = model.get_text_features(**inputs)
        ```'''
    def get_image_features(self, pixel_values: Optional[TFModelInputType] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> tf.Tensor:
        '''
        Returns:
            image_features (`tf.Tensor` of shape `(batch_size, output_dim`): The image embeddings obtained by applying
            the projection layer to the pooled output of [`TFCLIPVisionModel`].

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, TFCLIPModel

        >>> model = TFCLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        >>> processor = AutoProcessor.from_pretrained("openai/clip-vit-base-patch32")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="tf")

        >>> image_features = model.get_image_features(**inputs)
        ```'''
    def call(self, input_ids: Optional[TFModelInputType] = None, pixel_values: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, position_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, return_loss: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False) -> Union[TFCLIPOutput, Tuple[tf.Tensor]]:
        '''
        Returns:

        Examples:

        ```python
        >>> import tensorflow as tf
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, TFCLIPModel

        >>> model = TFCLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        >>> processor = AutoProcessor.from_pretrained("openai/clip-vit-base-patch32")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(
        ...     text=["a photo of a cat", "a photo of a dog"], images=image, return_tensors="tf", padding=True
        ... )

        >>> outputs = model(**inputs)
        >>> logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
        >>> probs = tf.nn.softmax(logits_per_image, axis=1)  # we can take the softmax to get the label probabilities
        ```'''
    def serving_output(self, output: TFCLIPOutput) -> TFCLIPOutput: ...
