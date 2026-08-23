import flax.linen as nn
import jax
import jax.numpy as jnp
from ...modeling_flax_outputs import FlaxBaseModelOutput as FlaxBaseModelOutput, FlaxBaseModelOutputWithPooling as FlaxBaseModelOutputWithPooling
from ...modeling_flax_utils import ACT2FN as ACT2FN, FlaxPreTrainedModel as FlaxPreTrainedModel, append_replace_return_docstrings as append_replace_return_docstrings, overwrite_call_docstring as overwrite_call_docstring
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, logging as logging
from .configuration_clip import CLIPConfig as CLIPConfig, CLIPTextConfig as CLIPTextConfig, CLIPVisionConfig as CLIPVisionConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from typing import Any, Optional, Tuple, Union

logger: Incomplete
CLIP_START_DOCSTRING: str
CLIP_TEXT_INPUTS_DOCSTRING: str
CLIP_VISION_INPUTS_DOCSTRING: str
CLIP_INPUTS_DOCSTRING: str

class FlaxCLIPOutput(ModelOutput):
    """
    Args:
        logits_per_image:(`jnp.ndarray` of shape `(image_batch_size, text_batch_size)`):
            The scaled dot product scores between `image_embeds` and `text_embeds`. This represents the image-text
            similarity scores.
        logits_per_text:(`jnp.ndarray` of shape `(text_batch_size, image_batch_size)`):
            The scaled dot product scores between `text_embeds` and `image_embeds`. This represents the text-image
            similarity scores.
        text_embeds(`jnp.ndarray` of shape `(batch_size, output_dim`):
            The text embeddings obtained by applying the projection layer to the pooled output of
            [`FlaxCLIPTextModel`].
        image_embeds(`jnp.ndarray` of shape `(batch_size, output_dim`):
            The image embeddings obtained by applying the projection layer to the pooled output of
            [`FlaxCLIPVisionModel`].
        text_model_output(`FlaxBaseModelOutputWithPooling`):
            The output of the [`FlaxCLIPTextModel`].
        vision_model_output(`FlaxBaseModelOutputWithPooling`):
            The output of the [`FlaxCLIPVisionModel`].
    """
    logits_per_image: jnp.ndarray
    logits_per_text: jnp.ndarray
    text_embeds: jnp.ndarray
    image_embeds: jnp.ndarray
    text_model_output: FlaxBaseModelOutputWithPooling
    vision_model_output: FlaxBaseModelOutputWithPooling
    def to_tuple(self) -> Tuple[Any]: ...

class FlaxCLIPVisionEmbeddings(nn.Module):
    config: CLIPVisionConfig
    dtype: jnp.dtype
    class_embedding: Incomplete
    patch_embedding: Incomplete
    num_patches: Incomplete
    position_embedding: Incomplete
    position_ids: Incomplete
    def setup(self) -> None: ...
    def __call__(self, pixel_values): ...

class FlaxCLIPTextEmbeddings(nn.Module):
    config: CLIPTextConfig
    dtype: jnp.dtype
    token_embedding: Incomplete
    position_embedding: Incomplete
    position_ids: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, position_ids): ...

class FlaxCLIPAttention(nn.Module):
    config: Union[CLIPTextConfig, CLIPVisionConfig]
    dtype: jnp.dtype
    embed_dim: Incomplete
    num_heads: Incomplete
    head_dim: Incomplete
    scale: Incomplete
    dropout: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    q_proj: Incomplete
    out_proj: Incomplete
    causal: Incomplete
    causal_mask: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxCLIPMLP(nn.Module):
    config: Union[CLIPTextConfig, CLIPVisionConfig]
    dtype: jnp.dtype
    activation_fn: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states): ...

class FlaxCLIPEncoderLayer(nn.Module):
    config: Union[CLIPTextConfig, CLIPVisionConfig]
    dtype: jnp.dtype
    self_attn: Incomplete
    layer_norm1: Incomplete
    mlp: Incomplete
    layer_norm2: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask, deterministic: bool = True, output_attentions: bool = False): ...

class FlaxCLIPLayerCollection(nn.Module):
    config: Union[CLIPTextConfig, CLIPVisionConfig]
    dtype: jnp.dtype
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, hidden_states, attention_mask: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxCLIPEncoder(nn.Module):
    config: Union[CLIPTextConfig, CLIPVisionConfig]
    dtype: jnp.dtype
    layers: Incomplete
    def setup(self) -> None: ...
    def __call__(self, inputs_embeds, attention_mask: Incomplete | None = None, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxCLIPTextTransformer(nn.Module):
    config: CLIPTextConfig
    dtype: jnp.dtype
    embeddings: Incomplete
    encoder: Incomplete
    final_layer_norm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxCLIPVisionTransformer(nn.Module):
    config: CLIPVisionConfig
    dtype: jnp.dtype
    embeddings: Incomplete
    pre_layrnorm: Incomplete
    encoder: Incomplete
    post_layernorm: Incomplete
    def setup(self) -> None: ...
    def __call__(self, pixel_values: Incomplete | None = None, deterministic: bool = True, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: bool = True): ...

class FlaxCLIPTextPreTrainedModel(FlaxPreTrainedModel):
    config_class = CLIPTextConfig
    module_class: nn.Module
    def __init__(self, config: CLIPTextConfig, input_shape=(1, 1), seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict: ...
    def __call__(self, input_ids, attention_mask: Incomplete | None = None, position_ids: Incomplete | None = None, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None): ...

class FlaxCLIPVisionPreTrainedModel(FlaxPreTrainedModel):
    config_class = CLIPVisionConfig
    main_input_name: str
    module_class: nn.Module
    def __init__(self, config: CLIPVisionConfig, input_shape: Optional[Tuple] = None, seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict: ...
    def __call__(self, pixel_values, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None): ...

class FlaxCLIPPreTrainedModel(FlaxPreTrainedModel):
    config_class = CLIPConfig
    module_class: nn.Module
    def __init__(self, config: CLIPConfig, input_shape: Optional[Tuple] = None, seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict: ...
    def __call__(self, input_ids, pixel_values, attention_mask: Incomplete | None = None, position_ids: Incomplete | None = None, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None): ...
    def get_text_features(self, input_ids, attention_mask: Incomplete | None = None, position_ids: Incomplete | None = None, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False):
        '''
        Args:
            input_ids (`numpy.ndarray` of shape `(batch_size, sequence_length)`):
                Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you
                provide it.

                Indices can be obtained using [`AutoTokenizer`]. See [`PreTrainedTokenizer.encode`] and
                [`PreTrainedTokenizer.__call__`] for details.

                [What are input IDs?](../glossary#input-ids)

        Returns:
            text_features (`jnp.ndarray` of shape `(batch_size, output_dim`): The text embeddings obtained by applying
            the projection layer to the pooled output of [`FlaxCLIPTextModel`].

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, FlaxCLIPModel

        >>> model = FlaxCLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        >>> tokenizer = AutoTokenizer.from_pretrained("openai/clip-vit-base-patch32")

        >>> inputs = tokenizer(["a photo of a cat", "a photo of a dog"], padding=True, return_tensors="np")
        >>> text_features = model.get_text_features(**inputs)
        ```'''
    def get_image_features(self, pixel_values, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False):
        '''
        Args:
            pixel_values (`numpy.ndarray` of shape `(batch_size, num_channels, height, width)`):
                Pixel values. Padding will be ignored by default should you provide it. Pixel values can be obtained
                using [`AutoImageProcessor`]. See [`CLIPImageProcessor.__call__`] for details.

        Returns:
            image_features (`jnp.ndarray` of shape `(batch_size, output_dim`): The image embeddings obtained by
            applying the projection layer to the pooled output of [`FlaxCLIPVisionModel`]

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, FlaxCLIPModel

        >>> model = FlaxCLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        >>> processor = AutoProcessor.from_pretrained("openai/clip-vit-base-patch32")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="np")

        >>> image_features = model.get_image_features(**inputs)
        ```'''

class FlaxCLIPTextModule(nn.Module):
    config: CLIPTextConfig
    dtype: jnp.dtype
    text_model: Incomplete
    def setup(self) -> None: ...
    def __call__(self, input_ids, attention_mask, position_ids, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxCLIPTextModel(FlaxCLIPTextPreTrainedModel):
    module_class = FlaxCLIPTextModule

FLAX_CLIP_TEXT_MODEL_DOCSTRING: str

class FlaxCLIPVisionModule(nn.Module):
    config: CLIPVisionConfig
    dtype: jnp.dtype
    vision_model: Incomplete
    def setup(self) -> None: ...
    def __call__(self, pixel_values, deterministic: bool = True, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class FlaxCLIPVisionModel(FlaxCLIPVisionPreTrainedModel):
    module_class = FlaxCLIPVisionModule

FLAX_CLIP_VISION_MODEL_DOCSTRING: str

class FlaxCLIPModule(nn.Module):
    config: CLIPConfig
    dtype: jnp.dtype
    projection_dim: Incomplete
    text_embed_dim: Incomplete
    vision_embed_dim: Incomplete
    text_model: Incomplete
    vision_model: Incomplete
    visual_projection: Incomplete
    text_projection: Incomplete
    logit_scale: Incomplete
    def setup(self): ...
    def __call__(self, input_ids: Incomplete | None = None, pixel_values: Incomplete | None = None, attention_mask: Incomplete | None = None, position_ids: Incomplete | None = None, deterministic: bool = True, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None): ...

class FlaxCLIPModel(FlaxCLIPPreTrainedModel):
    module_class = FlaxCLIPModule

FLAX_CLIP_MODEL_DOCSTRING: str
