import flax.linen as nn
import jax
import jax.numpy as jnp
from ...modeling_flax_utils import FlaxPreTrainedModel as FlaxPreTrainedModel, append_replace_return_docstrings as append_replace_return_docstrings, overwrite_call_docstring as overwrite_call_docstring
from ...utils import add_start_docstrings as add_start_docstrings, logging as logging
from ..auto.configuration_auto import AutoConfig as AutoConfig
from ..auto.modeling_flax_auto import FLAX_MODEL_MAPPING as FLAX_MODEL_MAPPING, FlaxAutoModel as FlaxAutoModel
from ..clip.modeling_flax_clip import FlaxCLIPOutput as FlaxCLIPOutput, FlaxCLIPVisionModel as FlaxCLIPVisionModel
from .configuration_vision_text_dual_encoder import VisionTextDualEncoderConfig as VisionTextDualEncoderConfig
from _typeshed import Incomplete
from flax.core.frozen_dict import FrozenDict as FrozenDict
from typing import Optional, Tuple

logger: Incomplete
VISION_TEXT_DUAL_ENCODER_START_DOCSTRING: str
VISION_TEXT_DUAL_ENCODER_INPUTS_DOCSTRING: str

class FlaxVisionTextDualEncoderModule(nn.Module):
    config: VisionTextDualEncoderConfig
    dtype: jnp.dtype
    vision_embed_dim: Incomplete
    text_embed_dim: Incomplete
    projection_dim: Incomplete
    vision_model: Incomplete
    text_model: Incomplete
    visual_projection: Incomplete
    text_projection: Incomplete
    logit_scale: Incomplete
    def setup(self): ...
    def __call__(self, input_ids: Incomplete | None = None, pixel_values: Incomplete | None = None, attention_mask: Incomplete | None = None, position_ids: Incomplete | None = None, token_type_ids: Incomplete | None = None, deterministic: bool = True, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None): ...

class FlaxVisionTextDualEncoderModel(FlaxPreTrainedModel):
    config_class = VisionTextDualEncoderConfig
    module_class = FlaxVisionTextDualEncoderModule
    def __init__(self, config: VisionTextDualEncoderConfig, input_shape: Optional[Tuple] = None, seed: int = 0, dtype: jnp.dtype = ..., _do_init: bool = True, **kwargs) -> None: ...
    def init_weights(self, rng: jax.random.PRNGKey, input_shape: Tuple, params: FrozenDict = None) -> FrozenDict: ...
    def __call__(self, input_ids, pixel_values, attention_mask: Incomplete | None = None, position_ids: Incomplete | None = None, token_type_ids: Incomplete | None = None, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None): ...
    def get_text_features(self, input_ids, attention_mask: Incomplete | None = None, position_ids: Incomplete | None = None, token_type_ids: Incomplete | None = None, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False):
        """
        Args:
            input_ids (`numpy.ndarray` of shape `(batch_size, sequence_length)`):
                Indices of input sequence tokens in the vocabulary. Padding will be ignored by default should you
                provide it.

                Indices can be obtained using [`PreTrainedTokenizer`]. See [`PreTrainedTokenizer.encode`] and
                [`PreTrainedTokenizer.__call__`] for details.

                [What are input IDs?](../glossary#input-ids)

        Returns:
            text_features (`jnp.ndarray` of shape `(batch_size, output_dim`): The text embeddings obtained by applying
            the projection layer to the pooled output of text model.
        """
    def get_image_features(self, pixel_values, params: dict = None, dropout_rng: jax.random.PRNGKey = None, train: bool = False):
        """
        Args:
            pixel_values (`numpy.ndarray` of shape `(batch_size, num_channels, height, width)`):
                Pixel values. Padding will be ignored by default should you provide it. Pixel values can be obtained
                using [`ImageFeatureExtractionMixin`]. See [`ImageFeatureExtractionMixin.__call__`] for details.

        Returns:
            image_features (`jnp.ndarray` of shape `(batch_size, output_dim`): The image embeddings obtained by
            applying the projection layer to the pooled output of vision model.
        """
    @classmethod
    def from_vision_text_pretrained(cls, vision_model_name_or_path: str = None, text_model_name_or_path: str = None, *model_args, **kwargs) -> FlaxPreTrainedModel:
        '''
        Params:
            vision_model_name_or_path (`str`, *optional*, defaults to `None`):
                Information necessary to initiate the vision model. Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co.
                      Valid model ids can be located at the root-level, like `bert-base-uncased`, or namespaced under a
                      user or organization name, like `dbmdz/bert-base-german-cased`.
                    - A path to a *directory* containing model weights saved using
                      [`~FlaxPreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.
                    - A path or url to a *PyTorch checkpoint folder* (e.g, `./pt_model`). In this case, `from_pt`
                      should be set to `True` and a configuration object should be provided as `config` argument. This
                      loading path is slower than converting the PyTorch checkpoint in a Flax model using the provided
                      conversion scripts and loading the Flax model afterwards.

            text_model_name_or_path (`str`, *optional*):
                Information necessary to initiate the text model. Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co.
                      Valid model ids can be located at the root-level, like `bert-base-uncased`, or namespaced under a
                      user or organization name, like `dbmdz/bert-base-german-cased`.
                    - A path to a *directory* containing model weights saved using
                      [`~FlaxPreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.
                    - A path or url to a *PyTorch checkpoint folder* (e.g, `./pt_model`). In this case, `from_pt`
                      should be set to `True` and a configuration object should be provided as `config` argument. This
                      loading path is slower than converting the PyTorch checkpoint in a Flax model using the provided
                      conversion scripts and loading the Flax model afterwards.

            model_args (remaining positional arguments, *optional*):
                All remaning positional arguments will be passed to the underlying model\'s `__init__` method.

            kwargs (remaining dictionary of keyword arguments, *optional*):
                Can be used to update the configuration object (after it being loaded) and initiate the model (e.g.,
                `output_attentions=True`).

                - To update the text configuration, use the prefix *text_* for each configuration parameter.
                - To update the vision configuration, use the prefix *vision_* for each configuration parameter.
                - To update the parent model configuration, do not use a prefix for each configuration parameter.

                Behaves differently depending on whether a `config` is provided or automatically loaded.

        Example:

        ```python
        >>> from transformers import FlaxVisionTextDualEncoderModel

        >>> # initialize a model from pretrained ViT and BERT models. Note that the projection layers will be randomly initialized.
        >>> model = FlaxVisionTextDualEncoderModel.from_vision_text_pretrained(
        ...     "google/vit-base-patch16-224", "bert-base-uncased"
        ... )
        >>> # saving model after fine-tuning
        >>> model.save_pretrained("./vit-bert")
        >>> # load fine-tuned model
        >>> model = FlaxVisionTextDualEncoderModel.from_pretrained("./vit-bert")
        ```'''

VISION_TEXT_DUAL_ENCODER_MODEL_DOCSTRING: str
