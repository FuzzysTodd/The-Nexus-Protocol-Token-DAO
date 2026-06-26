import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling
from ...modeling_utils import PreTrainedModel as PreTrainedModel, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_flava import FlavaConfig as FlavaConfig, FlavaImageCodebookConfig as FlavaImageCodebookConfig, FlavaImageConfig as FlavaImageConfig, FlavaMultimodalConfig as FlavaMultimodalConfig, FlavaTextConfig as FlavaTextConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from transformers.utils.doc import add_code_sample_docstrings as add_code_sample_docstrings
from typing import Any, Optional, Set, Tuple, Union

logger: Incomplete
FLAVA_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
FLAVA_CODEBOOK_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete
LOGIT_SCALE_CLAMP_MIN: int
LOGIT_SCALE_CLAMP_MAX: float
FlavaPossibleConfigs = Union[FlavaTextConfig, FlavaImageConfig, FlavaMultimodalConfig]

@dataclass
class FlavaModelOutput(ModelOutput):
    """
    Output from FlavaModel containing embeddings and outputs from individual encoders.

    Note that `image_embeddings` and `text_embeddigns` returned are similar to pooled output returned from a
    transformer. If you want embeddings for contrastive loss or retrieval use a FLAVA model's `image_projection` and
    `text_projection` layers on `image_embeddings` and `text_embeddings` respectively.

    Args:
        image_embeddings (`torch.FloatTensor` of shape `(batch_size, output_dim)`, *optional*, returned when `pixel_values` are present):
            The image embeddings which are basically the pooled output of [`FlavaImageModel`].
        image_output (`BaseModelOutputWithPooling`, *optional*, returned when `pixel_values` are present):
            The output of the [`FlavaImageModel`].
        text_embeddings (`torch.FloatTensor` of shape `(batch_size, output_dim)`, *optional*, returned when `input_ids` are present):
            The text embeddings which are basically the pooled output of [`FlavaTextModel`].
        text_output (`BaseModelOutputWithPooling`, *optional*, returned when `input_ids` are present):
            The output of the [`FlavaTextModel`].
        multimodal_embeddings (`torch.FloatTensor` of shape `(batch_size, output_dim)`, *optional*, returned when `input_ids` and `pixel_values` are present and `skip_multimodal_encoder` is `None` or `False`):
            The multimodal embeddings which are basically the pooled output of [`FlavaTextModel`].
        multimodal_output (`BaseModelOutputWithPooling`, returned when `input_ids` and `pixel_values` are present and `skip_multimodal_encoder` is `None` or `False`):
            The output of the [`FlavaMultimodalModel`].
    """
    image_embeddings: Optional[torch.FloatTensor] = ...
    image_output: Optional[BaseModelOutputWithPooling] = ...
    text_embeddings: Optional[torch.FloatTensor] = ...
    text_output: Optional[BaseModelOutputWithPooling] = ...
    multimodal_embeddings: Optional[torch.FloatTensor] = ...
    multimodal_output: Optional[BaseModelOutputWithPooling] = ...
    def to_tuple(self) -> Tuple[Any]: ...
    def __init__(self, image_embeddings, image_output, text_embeddings, text_output, multimodal_embeddings, multimodal_output) -> None: ...

@dataclass
class FlavaLosses(ModelOutput):
    """Class representing pretraining losses from FLAVA model

    Args:
        mim (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `mim_labels` and `pixel_values` are present, `input_ids_masked` is absent and `mim_weight` > 0.:
            Masked Image Modeling loss as used in BeIT calculated only for unimodal image data.
        mlm (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `mlm_labels` and `input_ids_masked` are present, `pixel_values` is absent and `mlm_weight` > 0.:
            Masked Language Modeling loss as used in BERT calculated only for unimodal text data.
        itm (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `itm_labels`, `input_ids_masked`, `pixel_values` are present and `itm_weight` > 0.:
            Image Text Matching (ITM) loss calculated for paired image-text data. Note that ITM loss is calculated on
            masked pairs in FLAVA.
        global_contrastive (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `input_ids` and `pixel_values` are present and `global_contrastive_weight` > 0.:
            Contrastive loss for image-text similarity similar to CLIP but calculated globally for paired image-text
            data. This is calculated on unmasked images and texts.
        mmm_image (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `mim_labels`, `pixel_values` and `input_ids_masked` are present and `mmm_image_weight` > 0.:
            Masked Multimodal Modeling loss's image component calculated on paired image-text data.
        mmm_text (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `mlm_labels`, `pixel_values` and `input_ids_masked` are present and `mmm_text_weight` > 0.:
            Masked Multimodal Modeling loss's text component calculated on paired image-text data.
    """
    mim: Optional[torch.FloatTensor] = ...
    mlm: Optional[torch.FloatTensor] = ...
    itm: Optional[torch.FloatTensor] = ...
    global_contrastive: Optional[torch.FloatTensor] = ...
    mmm_image: Optional[torch.FloatTensor] = ...
    mmm_text: Optional[torch.FloatTensor] = ...
    def all_none(self) -> bool: ...
    def __init__(self, mim, mlm, itm, global_contrastive, mmm_image, mmm_text) -> None: ...

@dataclass
class FlavaForPreTrainingOutput(ModelOutput):
    """
    Output from FlavaForPreTraining containing embeddings, and outputs from individual encoders.

    Note that `image_embeddings` and `text_embeddings` returned are similar to pooled output returned from a
    transformer. If you want embeddings for contrastive loss or retrieval use a FLAVA model's `image_projection` and
    `text_projection` layers on `image_embeddings` and `text_embeddings` respectively.

    Args:
        loss (`torch.FloatTensor`, *optional*, returned when `return_loss` is True):
            Total loss calculated for this model.
        loss_info (`FlavaLosses`):
            Detailed info for FLAVA Pretraining losses. Check `FlavaLosses` class description for the information on
            the keys.
        image_embeddings (`torch.FloatTensor` of shape `(batch_size, output_dim)`, *optional*, returned when `pixel_values` are present):
            The image embeddings which are basically the pooled output of [`FlavaImageModel`].
        image_output (`BaseModelOutputWithPooling`, *optional*, returned when `pixel_values` are present):
            The output of the [`FlavaImageModel`].
        text_embeddings (`torch.FloatTensor` of shape `(batch_size, output_dim)`, *optional*, returned when `input_ids` are present):
            The text embeddings which are basically the pooled output of [`FlavaTextModel`].
        text_output (`BaseModelOutputWithPooling`, *optional*, returned when `input_ids` are present):
            The output of the [`FlavaTextModel`].
        multimodal_embeddings (`torch.FloatTensor` of shape `(batch_size, output_dim)`, *optional*, returned when `input_ids` and `pixel_values` are present and `skip_unmasked_multimodal_encoder` is `None` or `False`):
            The multimodal embeddings which are basically the pooled output of [`FlavaTextModel`].
        multimodal_output (`BaseModelOutputWithPooling`, returned when `input_ids` and `pixel_values` are present and `skip_unmasked_multimodal_encoder` is `None` or `False`):
            The output of the [`FlavaMultimodalModel`].

        image_masked_embeddings (`torch.FloatTensor` of shape `(batch_size, output_dim)`, *optional*, returned when `pixel_values` are present):
            The image embeddings which are basically the pooled output of [`FlavaImageModel`]. Uses `bool_masked_pos`
            to create masked images.
        image_masked_output (`BaseModelOutputWithPooling`, *optional*, returned when `pixel_values` are present):
            The output of the [`FlavaImageModel`]. Uses `bool_masked_pos` to create masked images.
        text_masked_embeddings (`torch.FloatTensor` of shape `(batch_size, output_dim)`, *optional*, returned when `input_ids_masked` are present):
            The text embeddings which are basically the pooled output of [`FlavaTextModel`].
        text_masked_output (`BaseModelOutputWithPooling`, *optional*, returned when `input_ids_masked` are present):
            The output of the [`FlavaTextModel`].
        multimodal_masked_embeddings (`torch.FloatTensor` of shape `(batch_size, output_dim)`, *optional*, returned when `input_ids` and `pixel_values` are present):
            The multimodal embeddings which are basically the pooled output of [`FlavaTextModel`].
        multimodal_masked_output (`BaseModelOutputWithPooling`, returned when `input_ids_masked` and `pixel_values` are present):
            The output of the [`FlavaMultimodalModel`].

        mim_logits (`torch.FloatTensor` of shape `(batch_size, num_image_patches, image_vocab_size)` or of shape `(total_masked_patches, image_vocab_size)` , *optional*, returned when `pixel_values` are present and `input_ids_masked` are not):
                The logits for MIM unimodal loss. Uses `book_masked_pos` to get masked patches. The flattened output is
                returned when `bool_masked_pos` has some of the patches masked.
        mlm_logits (`torch.FloatTensor` of shape `(batch_size, text_seq_length, text_vocab_size)` or of shape `(total_masked_seq_length, text_vocab_size)`, *optional*, returned when `input_ids_masked` are present and `pixel_values` are not):
                The logits for MLM unimodal loss. The flattened output is returned when `input_ids_masked` has some of
                the tokens masked.
        itm_logits (`torch.FloatTensor` of shape `(batch_size, 2)`, *optional*, returned when `input_ids_masked` and `pixel_values` are present):
                The logits for ITM loss. Note that ITM loss is calculated on masked pairs in FLAVA.
        mmm_image_logits (`torch.FloatTensor` of shape `(batch_size, num_image_patches, image_vocab_size)` or of shape`(total_masked_patches, image_vocab_size)`, *optional*, returned when `pixel_values` and `input_ids_masked` are present):
                The logits for MMM image multimodal loss. Uses `book_masked_pos` to get masked patches. The flattened
                output is returned when `bool_masked_pos` has some of the patches masked.
        mmm_text_logits (`torch.FloatTensor` of shape `(batch_size, text_seq_length, text_vocab_size)` or of shape `(`(total_masked_seq_length, text_vocab_size)`), *optional*, returned when `pixel_values` and `input_ids_masked` are present):
                The logits for MMM text multimodal loss. The flattened output is returned when `input_ids_masked` has
                some of the tokens masked.
        contrastive_logits_per_image (`torch.FloatTensor` of shape `(image_batch_size, text_batch_size)`):
            The scaled dot product scores between `image_embeddings` and `text_embeddings` but passed through FLAVA's
            `image_projection` and `text_projection` layers respectively. This represents the image-text similarity
            scores. This is calculated on unmasked images and texts.
        contrastive_logits_per_text (`torch.FloatTensor` of shape `(text_batch_size, image_batch_size)`):
            The scaled dot product scores between `text_embeddings` and `image_embeddings` but passed through FLAVA's
            `text_projection` and `image_projection` layers respectively. This is calculated on unmasked images and
            texts.
    """
    loss: Optional[torch.FloatTensor] = ...
    loss_info: FlavaLosses = ...
    image_embeddings: Optional[torch.FloatTensor] = ...
    image_output: Optional[BaseModelOutputWithPooling] = ...
    text_embeddings: Optional[torch.FloatTensor] = ...
    text_output: Optional[BaseModelOutputWithPooling] = ...
    multimodal_embeddings: Optional[torch.FloatTensor] = ...
    multimodal_output: Optional[BaseModelOutputWithPooling] = ...
    image_masked_embeddings: Optional[torch.FloatTensor] = ...
    image_masked_output: Optional[BaseModelOutputWithPooling] = ...
    text_masked_embeddings: Optional[torch.FloatTensor] = ...
    text_masked_output: Optional[BaseModelOutputWithPooling] = ...
    multimodal_masked_embeddings: Optional[torch.FloatTensor] = ...
    multimodal_masked_output: Optional[BaseModelOutputWithPooling] = ...
    mim_logits: Optional[torch.FloatTensor] = ...
    mlm_logits: Optional[torch.FloatTensor] = ...
    itm_logits: Optional[torch.FloatTensor] = ...
    contrastive_logits_per_image: Optional[torch.FloatTensor] = ...
    contrastive_logits_per_text: Optional[torch.FloatTensor] = ...
    mmm_image_logits: Optional[torch.FloatTensor] = ...
    mmm_text_logits: Optional[torch.FloatTensor] = ...
    def to_tuple(self) -> Tuple[Any]: ...
    def __init__(self, loss, loss_info, image_embeddings, image_output, text_embeddings, text_output, multimodal_embeddings, multimodal_output, image_masked_embeddings, image_masked_output, text_masked_embeddings, text_masked_output, multimodal_masked_embeddings, multimodal_masked_output, mim_logits, mlm_logits, itm_logits, contrastive_logits_per_image, contrastive_logits_per_text, mmm_image_logits, mmm_text_logits) -> None: ...

class FlavaImageEmbeddings(nn.Module):
    """
    Construct the CLS token, position and patch embeddings. Optionally, also the mask token.
    """
    cls_token: Incomplete
    mask_token: Incomplete
    patch_embeddings: Incomplete
    position_embeddings: Incomplete
    dropout: Incomplete
    config: Incomplete
    def __init__(self, config: FlavaImageConfig, use_mask_token: bool = False) -> None: ...
    def interpolate_pos_encoding(self, embeddings: torch.Tensor, height: int, width: int) -> torch.Tensor:
        """
        This method allows to interpolate the pre-trained position encodings, to be able to use the model on higher
        resolution images.

        Source:
        https://github.com/facebookresearch/dino/blob/de9ee3df6cf39fac952ab558447af1fa1365362a/image_transformer.py#L174
        """
    def forward(self, pixel_values: torch.Tensor, bool_masked_pos: Optional[torch.BoolTensor] = None, interpolate_pos_encoding: bool = False) -> torch.Tensor: ...

class PatchEmbeddings(nn.Module):
    """
    Image to Patch Embedding.
    """
    image_size: Incomplete
    patch_size: Incomplete
    num_patches: Incomplete
    projection: Incomplete
    def __init__(self, image_size: int = 224, patch_size: Union[int, Tuple[int, int]] = 16, num_channels: int = 3, embed_dim: int = 768) -> None: ...
    def forward(self, pixel_values: torch.Tensor, interpolate_pos_encoding: bool = False) -> torch.Tensor: ...

class FlavaTextEmbeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None): ...

class FlavaSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config: FlavaPossibleConfigs) -> None: ...
    def transpose_for_scores(self, x: torch.Tensor) -> torch.Tensor: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Union[Tuple[torch.Tensor, torch.Tensor], Tuple[torch.Tensor]]: ...

class FlavaSelfOutput(nn.Module):
    """
    The residual connection is defined in FlavaLayer (same as ViTLayer) instead of here (as is the case with other
    models), due to the layernorm applied before each block.
    """
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: FlavaPossibleConfigs) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class FlavaAttention(nn.Module):
    attention: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config: FlavaPossibleConfigs) -> None: ...
    def prune_heads(self, heads: Set[int]) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Union[Tuple[torch.Tensor, torch.Tensor], Tuple[torch.Tensor]]: ...

class FlavaIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: FlavaPossibleConfigs) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class FlavaOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: FlavaPossibleConfigs) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class FlavaLayer(nn.Module):
    """This corresponds to the Block class in the timm implementation."""
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    layernorm_before: Incomplete
    layernorm_after: Incomplete
    def __init__(self, config: FlavaPossibleConfigs) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Union[Tuple[torch.Tensor, torch.Tensor], Tuple[torch.Tensor]]: ...

class FlavaEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: FlavaConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True) -> Union[tuple, BaseModelOutput]: ...

class FlavaPooler(nn.Module):
    dense: Incomplete
    activation: Incomplete
    def __init__(self, config: FlavaPossibleConfigs) -> None: ...
    def forward(self, hidden_states: torch.Tensor): ...

FLAVA_START_DOCSTRING: str
FLAVA_INPUTS_DOCSTRING_COMMON: str
FLAVA_IMAGE_INPUTS_DOCSTRING_BASE: str
FLAVA_IMAGE_INPUTS_DOCSTRING: Incomplete
FLAVA_TEXT_INPUTS_DOCSTRING_BASE: str
FLAVA_TEXT_INPUTS_DOCSTRING: Incomplete
FLAVA_MULTIMODAL_INPUTS_DOCSTRING: Incomplete
FLAVA_MODEL_INPUTS_DOCSTRING_BASE: str
FLAVA_MODEL_INPUTS_DOCSTRING: Incomplete
FLAVA_PRETRAINING_INPUTS_DOCSTRING: Incomplete
FLAVA_PRETRAINING_START_DOCSTRING_EXTRA: str

class FlavaPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = FlavaConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool

class FlavaImageModel(FlavaPreTrainedModel):
    config_class = FlavaImageConfig
    base_model_prefix: str
    main_input_name: str
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    pooler: Incomplete
    def __init__(self, config: FlavaImageConfig, add_pooling_layer: bool = True) -> None: ...
    def get_input_embeddings(self) -> nn.Module: ...
    def set_input_embeddings(self, value: nn.Module): ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, bool_masked_pos: Optional[torch.BoolTensor] = None, interpolate_pos_encoding: Optional[bool] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, BaseModelOutputWithPooling]: ...

class FlavaTextModel(FlavaPreTrainedModel):
    config_class = FlavaTextConfig
    base_model_prefix: str
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    pooler: Incomplete
    def __init__(self, config: FlavaTextConfig, add_pooling_layer: bool = True) -> None: ...
    def get_input_embeddings(self) -> PatchEmbeddings: ...
    def set_input_embeddings(self, value: nn.Module): ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, BaseModelOutputWithPooling]: ...

class FlavaMultimodalModel(FlavaPreTrainedModel):
    config_class = FlavaMultimodalConfig
    base_model_prefix: str
    main_input_name: str
    config: Incomplete
    use_cls_token: Incomplete
    cls_token: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    pooler: Incomplete
    def __init__(self, config: FlavaMultimodalConfig, add_pooling_layer: bool = True) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, BaseModelOutputWithPooling]: ...

class FlavaModel(FlavaPreTrainedModel):
    config_class = FlavaConfig
    projection_dim: Incomplete
    text_hidden_size: Incomplete
    image_hidden_size: Incomplete
    mm_hidden_size: Incomplete
    text_model: Incomplete
    image_model: Incomplete
    multimodal_model: Incomplete
    image_projection: Incomplete
    text_projection: Incomplete
    logit_scale: Incomplete
    image_to_mm_projection: Incomplete
    text_to_mm_projection: Incomplete
    def __init__(self, config: FlavaConfig) -> None: ...
    def get_text_features(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> torch.FloatTensor: ...
    def get_image_features(self, pixel_values: Optional[torch.Tensor] = None, bool_masked_pos: Optional[torch.BoolTensor] = None, interpolate_pos_encoding: Optional[bool] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> torch.FloatTensor: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, pixel_values: Optional[torch.FloatTensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, bool_masked_pos: Optional[torch.Tensor] = None, position_ids: Optional[torch.LongTensor] = None, image_attention_mask: Optional[torch.Tensor] = None, skip_multimodal_encoder: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: bool = True, return_dict: Optional[bool] = None) -> Union[Tuple, FlavaOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, FlavaModel

        >>> model = FlavaModel.from_pretrained("facebook/flava-full")
        >>> processor = AutoProcessor.from_pretrained("facebook/flava-full")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(text=["a photo of a cat"], images=image, return_tensors="pt", padding=True)

        >>> outputs = model(**inputs)
        >>> logits_per_image = outputs.contrastive_logits_per_image  # this is the image-text similarity score
        >>> probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities
        ```
        '''

class FlavaImageCodebookResPath(nn.Module):
    path: Incomplete
    def __init__(self, in_size: int, out_size: int, **kwargs) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class FlavaImageCodebookBlock(nn.Module):
    post_gain: Incomplete
    id_path: Incomplete
    res_path: Incomplete
    def __init__(self, in_size: int, out_size: int, num_layers: int, **kwargs) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class FlavaImageCodebookLayerGroup(nn.Module):
    group: Incomplete
    def __init__(self, num_blocks: int, num_layers: int, in_size: int, out_size: int, use_pool: bool = True) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class FlavaImageCodebook(FlavaPreTrainedModel):
    base_model_prefix: str
    config_class = FlavaImageCodebookConfig
    main_input_name: str
    supports_gradient_checkpointing: bool
    config: Incomplete
    num_groups: Incomplete
    input_channels: Incomplete
    num_blocks_per_group: Incomplete
    hidden_size: Incomplete
    vocab_size: Incomplete
    blocks: Incomplete
    def __init__(self, config: FlavaImageCodebookConfig, **kwargs: Any) -> None: ...
    def get_codebook_indices(self, pixel_values: torch.Tensor) -> torch.Tensor: ...
    def get_codebook_probs(self, pixel_values: torch.Tensor) -> torch.Tensor: ...
    def forward(self, pixel_values: torch.FloatTensor) -> torch.Tensor: ...

class FlavaPredictionHeadTransform(nn.Module):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class FlavaMaskedPredictionHead(nn.Module):
    config: Incomplete
    transform: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def __init__(self, config, weight: Incomplete | None = None) -> None: ...
    def forward(self, x): ...

class FlavaITMHead(nn.Module):
    config: Incomplete
    pooler: Incomplete
    seq_relationship: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, x): ...

class FlavaGlobalContrastiveHead(nn.Module):
    config: Incomplete
    global_backprop_contrastive: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, image_embeddings, text_embeddings, logit_scale): ...

class FlavaForPreTraining(FlavaPreTrainedModel):
    flava: Incomplete
    image_codebook: Incomplete
    mim_head: Incomplete
    mlm_head: Incomplete
    itm_head: Incomplete
    mmm_image_head: Incomplete
    mmm_text_head: Incomplete
    global_contrastive_head: Incomplete
    image_vocab_size: Incomplete
    text_vocab_size: Incomplete
    mlm_weight: Incomplete
    mim_weight: Incomplete
    global_contrastive_weight: Incomplete
    ce_ignore_index: Incomplete
    itm_weight: Incomplete
    mmm_image_weight: Incomplete
    mmm_text_weight: Incomplete
    skip_unmasked_multimodal_encoder: Incomplete
    def __init__(self, config: FlavaConfig, image_codebook: Optional[nn.Module] = None) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, input_ids_masked: Optional[torch.LongTensor] = None, pixel_values: Optional[torch.FloatTensor] = None, codebook_pixel_values: Optional[torch.FloatTensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, bool_masked_pos: Optional[torch.Tensor] = None, position_ids: Optional[torch.LongTensor] = None, image_attention_mask: Optional[torch.Tensor] = None, skip_unmasked_multimodal_encoder: bool = None, mlm_labels: Optional[torch.Tensor] = None, mim_labels: Optional[torch.Tensor] = None, itm_labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: bool = True, return_dict: Optional[bool] = None, return_loss: Optional[bool] = None) -> Union[Tuple[torch.Tensor], FlavaForPreTrainingOutput]:
        '''
        Examples:
        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import FlavaForPreTraining, AutoProcessor

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> model = FlavaForPreTraining.from_pretrained("facebook/flava-full")
        >>> processor = AutoProcessor.from_pretrained("facebook/flava-full")

        >>> text = ["a photo of a cat"]

        >>> inputs = processor(
        ...     images=[image],
        ...     text=text,
        ...     return_masks=True,
        ...     return_codebook_pixels=True,
        ...     padding=True,
        ...     max_length=77,
        ...     return_tensors="pt",
        ... )


        >>> output = model(**inputs)
        ```

        Return:

        '''
