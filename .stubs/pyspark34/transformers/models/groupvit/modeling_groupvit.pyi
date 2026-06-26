import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_groupvit import GroupViTConfig as GroupViTConfig, GroupViTTextConfig as GroupViTTextConfig, GroupViTVisionConfig as GroupViTVisionConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Any, Optional, Tuple, Union

logger: Incomplete
GROUPVIT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def contrastive_loss(logits: torch.Tensor) -> torch.Tensor: ...
def groupvit_loss(similarity: torch.Tensor) -> torch.Tensor: ...
def hard_softmax(logits: torch.Tensor, dim: int): ...
def gumbel_softmax(logits: torch.Tensor, tau: float = 1, hard: bool = False, dim: int = -1) -> torch.Tensor: ...
def resize_attention_map(attentions, height, width, align_corners: bool = False):
    """
    Args:
        attentions (`torch.Tensor`): attention map of shape [batch_size, groups, feat_height*feat_width]
        height (`int`): height of the output attention map
        width (`int`): width of the output attention map
        align_corners (`bool`, *optional*): the `align_corner` argument for `nn.functional.interpolate`.

    Returns:
        `torch.Tensor`: resized attention map of shape [batch_size, groups, height, width]
    """
def get_grouping_from_attentions(attentions, hw_shape):
    """
    Args:
        attentions (`tuple(torch.FloatTensor)`: tuple of attention maps returned by `GroupViTVisionTransformer`
        hw_shape (`tuple(int)`): height and width of the output attention map
    Returns:
        `torch.Tensor`: the attention map of shape [batch_size, groups, height, width]
    """

class GroupViTCrossAttentionLayer(nn.Module):
    attn: Incomplete
    norm2: Incomplete
    mlp: Incomplete
    norm_post: Incomplete
    def __init__(self, config: GroupViTVisionConfig) -> None: ...
    def forward(self, query, key): ...

class GroupViTAssignAttention(nn.Module):
    scale: Incomplete
    q_proj: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    proj: Incomplete
    assign_eps: Incomplete
    def __init__(self, config: GroupViTVisionConfig) -> None: ...
    def get_attn(self, attn, gumbel: bool = True, hard: bool = True): ...
    def forward(self, query, key): ...

class GroupViTTokenAssign(nn.Module):
    num_output_group: Incomplete
    norm_tokens: Incomplete
    mlp_inter: Incomplete
    norm_post_tokens: Incomplete
    norm_x: Incomplete
    pre_assign_attn: Incomplete
    assign: Incomplete
    norm_new_x: Incomplete
    mlp_channels: Incomplete
    def __init__(self, config: GroupViTVisionConfig, num_group_token, num_output_group) -> None: ...
    def project_group_token(self, group_tokens):
        """
        Args:
            group_tokens (torch.Tensor): group tokens, [batch_size, num_group_tokens, channels]

        Returns:
            projected_group_tokens (torch.Tensor): [batch_size, num_output_groups, channels]
        """
    def forward(self, image_tokens, group_tokens):
        """
        Args:
            image_tokens (`torch.Tensor`): image tokens, of shape [batch_size, input_length, channels]
            group_tokens (`torch.Tensor`): group tokens, [batch_size, num_group_tokens, channels]
        """

@dataclass
class GroupViTModelOutput(ModelOutput):
    """
    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `return_loss` is `True`):
            Contrastive loss for image-text similarity.
        logits_per_image (`torch.FloatTensor` of shape `(image_batch_size, text_batch_size)`):
            The scaled dot product scores between `image_embeds` and `text_embeds`. This represents the image-text
            similarity scores.
        logits_per_text (`torch.FloatTensor` of shape `(text_batch_size, image_batch_size)`):
            The scaled dot product scores between `text_embeds` and `image_embeds`. This represents the text-image
            similarity scores.
        segmentation_logits (`torch.FloatTensor` of shape `(batch_size, config.num_labels, logits_height, logits_width)`):
            Classification scores for each pixel.

            <Tip warning={true}>

            The logits returned do not necessarily have the same size as the `pixel_values` passed as inputs. This is
            to avoid doing two interpolations and lose some quality when a user needs to resize the logits to the
            original image size as post-processing. You should always check your logits shape and resize as needed.

            </Tip>

        text_embeds (`torch.FloatTensor` of shape `(batch_size, output_dim`):
            The text embeddings obtained by applying the projection layer to the pooled output of
            [`GroupViTTextModel`].
        image_embeds (`torch.FloatTensor` of shape `(batch_size, output_dim`):
            The image embeddings obtained by applying the projection layer to the pooled output of
            [`GroupViTVisionModel`].
        text_model_output (`BaseModelOutputWithPooling`):
            The output of the [`GroupViTTextModel`].
        vision_model_output (`BaseModelOutputWithPooling`):
            The output of the [`GroupViTVisionModel`].
    """
    loss: Optional[torch.FloatTensor] = ...
    logits_per_image: torch.FloatTensor = ...
    logits_per_text: torch.FloatTensor = ...
    segmentation_logits: torch.FloatTensor = ...
    text_embeds: torch.FloatTensor = ...
    image_embeds: torch.FloatTensor = ...
    text_model_output: BaseModelOutputWithPooling = ...
    vision_model_output: BaseModelOutputWithPooling = ...
    def to_tuple(self) -> Tuple[Any]: ...
    def __init__(self, loss, logits_per_image, logits_per_text, segmentation_logits, text_embeds, image_embeds, text_model_output, vision_model_output) -> None: ...

class GroupViTPatchEmbeddings(nn.Module):
    """
    Image to Patch Embedding.
    """
    image_size: Incomplete
    patch_size: Incomplete
    num_patches: Incomplete
    projection: Incomplete
    def __init__(self, image_size: int = 224, patch_size: Union[int, Tuple[int, int]] = 16, num_channels: int = 3, embed_dim: int = 768) -> None: ...
    def forward(self, pixel_values: torch.Tensor, interpolate_pos_encoding: bool = False) -> torch.Tensor: ...

class GroupViTVisionEmbeddings(nn.Module):
    patch_embeddings: Incomplete
    position_embeddings: Incomplete
    dropout: Incomplete
    layernorm: Incomplete
    config: Incomplete
    def __init__(self, config: GroupViTVisionConfig) -> None: ...
    def interpolate_pos_encoding(self, embeddings: torch.Tensor, height: int, width: int) -> torch.Tensor:
        """
        This method allows to interpolate the pre-trained position encodings, to be able to use the model on higher
        resolution images.

        Source:
        https://github.com/facebookresearch/dino/blob/de9ee3df6cf39fac952ab558447af1fa1365362a/vision_transformer.py#L174
        """
    def forward(self, pixel_values: torch.Tensor, interpolate_pos_encoding: bool = False) -> torch.Tensor: ...

class GroupViTTextEmbeddings(nn.Module):
    token_embedding: Incomplete
    position_embedding: Incomplete
    def __init__(self, config: GroupViTTextConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None) -> torch.Tensor: ...

class GroupViTStage(nn.Module):
    """This corresponds to the `GroupingLayer` class in the GroupViT implementation."""
    depth: Incomplete
    num_group_token: Incomplete
    group_token: Incomplete
    gradient_checkpointing: bool
    layers: Incomplete
    downsample: Incomplete
    group_projector: Incomplete
    def __init__(self, config: GroupViTVisionConfig, depth: int, num_prev_group_token: int, num_group_token: int, num_output_group: int) -> None: ...
    @property
    def with_group_token(self): ...
    def split_x(self, x): ...
    def concat_x(self, x: torch.Tensor, group_token: Optional[torch.Tensor] = None) -> torch.Tensor: ...
    def forward(self, hidden_states: torch.Tensor, prev_group_token: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.FloatTensor]:
        """
        Args:
            hidden_states (`torch.FloatTensor`): input to the layer of shape `(batch, seq_len, embed_dim)`
            attention_mask (`torch.FloatTensor`): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
                `(config.encoder_attention_heads,)`.
            output_attentions (`bool`, *optional*):
                Whether or not to return the grouping tensors of Grouping block.
        """

class GroupViTMLP(nn.Module):
    config: Incomplete
    activation_fn: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    def __init__(self, config: GroupViTVisionConfig, hidden_size: Optional[int] = None, intermediate_size: Optional[int] = None, output_size: Optional[int] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class GroupViTMixerMLP(GroupViTMLP):
    def forward(self, x): ...

class GroupViTAttention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    config: Incomplete
    embed_dim: Incomplete
    num_heads: Incomplete
    head_dim: Incomplete
    scale: Incomplete
    dropout: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    q_proj: Incomplete
    out_proj: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, causal_attention_mask: Optional[torch.Tensor] = None, encoder_hidden_states: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        """Input shape: Batch x Time x Channel"""

class GroupViTEncoderLayer(nn.Module):
    embed_dim: Incomplete
    self_attn: Incomplete
    layer_norm1: Incomplete
    mlp: Incomplete
    layer_norm2: Incomplete
    def __init__(self, config: GroupViTConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: torch.Tensor, causal_attention_mask: torch.Tensor, output_attentions: Optional[bool] = False) -> Tuple[torch.FloatTensor]:
        """
        Args:
            hidden_states (`torch.FloatTensor`): input to the layer of shape `(batch, seq_len, embed_dim)`
            attention_mask (`torch.FloatTensor`): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
                `(config.encoder_attention_heads,)`.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
        """

class GroupViTPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = GroupViTConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool

GROUPVIT_START_DOCSTRING: str
GROUPVIT_TEXT_INPUTS_DOCSTRING: str
GROUPVIT_VISION_INPUTS_DOCSTRING: str
GROUPVIT_INPUTS_DOCSTRING: str

class GroupViTVisionEncoder(nn.Module):
    config: Incomplete
    stages: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: GroupViTVisionConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, output_hidden_states: Optional[bool] = None, output_attentions: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, BaseModelOutput]: ...

class GroupViTTextEncoder(nn.Module):
    """
    Transformer encoder consisting of `config.num_hidden_layers` self-attention layers. Each layer is a
    [`GroupViTEncoderLayer`].

    Args:
        config: GroupViTTextConfig
    """
    config: Incomplete
    layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: GroupViTTextConfig) -> None: ...
    def forward(self, inputs_embeds, attention_mask: Optional[torch.Tensor] = None, causal_attention_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]:
        """
        Args:
            inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
                Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation.
                This is useful if you want more control over how to convert `input_ids` indices into associated vectors
                than the model's internal embedding lookup matrix.
            attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            causal_attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Causal mask for the text model. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """

class GroupViTTextTransformer(nn.Module):
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: GroupViTTextConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]:
        """
        Returns:

        """

class GroupViTTextModel(GroupViTPreTrainedModel):
    config_class = GroupViTTextConfig
    text_model: Incomplete
    def __init__(self, config: GroupViTTextConfig) -> None: ...
    def get_input_embeddings(self) -> nn.Module: ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import CLIPTokenizer, GroupViTTextModel

        >>> tokenizer = CLIPTokenizer.from_pretrained("nvidia/groupvit-gcc-yfcc")
        >>> model = GroupViTTextModel.from_pretrained("nvidia/groupvit-gcc-yfcc")

        >>> inputs = tokenizer(["a photo of a cat", "a photo of a dog"], padding=True, return_tensors="pt")

        >>> outputs = model(**inputs)
        >>> last_hidden_state = outputs.last_hidden_state
        >>> pooled_output = outputs.pooler_output  # pooled (EOS token) states
        ```'''

class GroupViTVisionTransformer(nn.Module):
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    def __init__(self, config: GroupViTVisionConfig) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, output_hidden_states: Optional[bool] = None, output_attentions: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]:
        """
        Returns:

        """

class GroupViTVisionModel(GroupViTPreTrainedModel):
    config_class = GroupViTVisionConfig
    main_input_name: str
    vision_model: Incomplete
    def __init__(self, config: GroupViTVisionConfig) -> None: ...
    def get_input_embeddings(self) -> GroupViTPatchEmbeddings: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]:
        '''
        Returns:

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, GroupViTVisionModel

        >>> processor = AutoProcessor.from_pretrained("nvidia/groupvit-gcc-yfcc")
        >>> model = GroupViTVisionModel.from_pretrained("nvidia/groupvit-gcc-yfcc")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="pt")

        >>> outputs = model(**inputs)
        >>> last_hidden_state = outputs.last_hidden_state
        >>> pooled_output = outputs.pooler_output  # pooled CLS states
        ```'''

class GroupViTModel(GroupViTPreTrainedModel):
    config_class = GroupViTConfig
    projection_dim: Incomplete
    projection_intermediate_dim: Incomplete
    text_embed_dim: Incomplete
    vision_embed_dim: Incomplete
    text_model: Incomplete
    vision_model: Incomplete
    visual_projection: Incomplete
    text_projection: Incomplete
    logit_scale: Incomplete
    def __init__(self, config: GroupViTConfig) -> None: ...
    def get_text_features(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> torch.FloatTensor:
        '''
        Returns:
            text_features (`torch.FloatTensor` of shape `(batch_size, output_dim`): The text embeddings obtained by
            applying the projection layer to the pooled output of [`GroupViTTextModel`].

        Examples:

        ```python
        >>> from transformers import CLIPTokenizer, GroupViTModel

        >>> model = GroupViTModel.from_pretrained("nvidia/groupvit-gcc-yfcc")
        >>> tokenizer = CLIPTokenizer.from_pretrained("nvidia/groupvit-gcc-yfcc")

        >>> inputs = tokenizer(["a photo of a cat", "a photo of a dog"], padding=True, return_tensors="pt")
        >>> text_features = model.get_text_features(**inputs)
        ```'''
    def get_image_features(self, pixel_values: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> torch.FloatTensor:
        '''
        Returns:
            image_features (`torch.FloatTensor` of shape `(batch_size, output_dim`): The image embeddings obtained by
            applying the projection layer to the pooled output of [`GroupViTVisionModel`].

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, GroupViTModel

        >>> model = GroupViTModel.from_pretrained("nvidia/groupvit-gcc-yfcc")
        >>> processor = AutoProcessor.from_pretrained("nvidia/groupvit-gcc-yfcc")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="pt")

        >>> image_features = model.get_image_features(**inputs)
        ```'''
    def forward(self, input_ids: Optional[torch.LongTensor] = None, pixel_values: Optional[torch.FloatTensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.LongTensor] = None, return_loss: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_segmentation: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, GroupViTModelOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, GroupViTModel

        >>> model = GroupViTModel.from_pretrained("nvidia/groupvit-gcc-yfcc")
        >>> processor = AutoProcessor.from_pretrained("nvidia/groupvit-gcc-yfcc")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(
        ...     text=["a photo of a cat", "a photo of a dog"], images=image, return_tensors="pt", padding=True
        ... )

        >>> outputs = model(**inputs)
        >>> logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
        >>> probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities
        ```'''
