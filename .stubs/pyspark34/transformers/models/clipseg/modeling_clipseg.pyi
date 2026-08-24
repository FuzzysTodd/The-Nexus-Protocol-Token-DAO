import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_clipseg import CLIPSegConfig as CLIPSegConfig, CLIPSegTextConfig as CLIPSegTextConfig, CLIPSegVisionConfig as CLIPSegVisionConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Any, Optional, Tuple, Union

logger: Incomplete
CLIPSEG_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def contrastive_loss(logits: torch.Tensor) -> torch.Tensor: ...
def clipseg_loss(similarity: torch.Tensor) -> torch.Tensor: ...

@dataclass
class CLIPSegOutput(ModelOutput):
    """
    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `return_loss` is `True`):
            Contrastive loss for image-text similarity.
        logits_per_image:(`torch.FloatTensor` of shape `(image_batch_size, text_batch_size)`):
            The scaled dot product scores between `image_embeds` and `text_embeds`. This represents the image-text
            similarity scores.
        logits_per_text:(`torch.FloatTensor` of shape `(text_batch_size, image_batch_size)`):
            The scaled dot product scores between `text_embeds` and `image_embeds`. This represents the text-image
            similarity scores.
        text_embeds(`torch.FloatTensor` of shape `(batch_size, output_dim`):
            The text embeddings obtained by applying the projection layer to the pooled output of [`CLIPSegTextModel`].
        image_embeds(`torch.FloatTensor` of shape `(batch_size, output_dim`):
            The image embeddings obtained by applying the projection layer to the pooled output of
            [`CLIPSegVisionModel`].
        text_model_output(`BaseModelOutputWithPooling`):
            The output of the [`CLIPSegTextModel`].
        vision_model_output(`BaseModelOutputWithPooling`):
            The output of the [`CLIPSegVisionModel`].
    """
    loss: Optional[torch.FloatTensor] = ...
    logits_per_image: torch.FloatTensor = ...
    logits_per_text: torch.FloatTensor = ...
    text_embeds: torch.FloatTensor = ...
    image_embeds: torch.FloatTensor = ...
    text_model_output: BaseModelOutputWithPooling = ...
    vision_model_output: BaseModelOutputWithPooling = ...
    def to_tuple(self) -> Tuple[Any]: ...
    def __init__(self, loss, logits_per_image, logits_per_text, text_embeds, image_embeds, text_model_output, vision_model_output) -> None: ...

@dataclass
class CLIPSegDecoderOutput(ModelOutput):
    """
    Args:
        logits (`torch.FloatTensor` of shape `(batch_size, height, width)`):
            Classification scores for each pixel.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    """
    logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, logits, hidden_states, attentions) -> None: ...

@dataclass
class CLIPSegImageSegmentationOutput(ModelOutput):
    """
    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `return_loss` is `True`):
            Contrastive loss for image-text similarity.
        ...
        vision_model_output (`BaseModelOutputWithPooling`):
            The output of the [`CLIPSegVisionModel`].
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    conditional_embeddings: torch.FloatTensor = ...
    pooled_output: torch.FloatTensor = ...
    vision_model_output: BaseModelOutputWithPooling = ...
    decoder_output: CLIPSegDecoderOutput = ...
    def to_tuple(self) -> Tuple[Any]: ...
    def __init__(self, loss, logits, conditional_embeddings, pooled_output, vision_model_output, decoder_output) -> None: ...

class CLIPSegVisionEmbeddings(nn.Module):
    config: Incomplete
    embed_dim: Incomplete
    image_size: Incomplete
    patch_size: Incomplete
    class_embedding: Incomplete
    patch_embedding: Incomplete
    num_patches: Incomplete
    num_positions: Incomplete
    position_embedding: Incomplete
    def __init__(self, config: CLIPSegVisionConfig) -> None: ...
    def interpolate_position_embeddings(self, new_size): ...
    def forward(self, pixel_values: torch.FloatTensor) -> torch.Tensor: ...

class CLIPSegTextEmbeddings(nn.Module):
    token_embedding: Incomplete
    position_embedding: Incomplete
    def __init__(self, config: CLIPSegTextConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None) -> torch.Tensor: ...

class CLIPSegAttention(nn.Module):
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
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, causal_attention_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        """Input shape: Batch x Time x Channel"""

class CLIPSegMLP(nn.Module):
    config: Incomplete
    activation_fn: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class CLIPSegEncoderLayer(nn.Module):
    embed_dim: Incomplete
    self_attn: Incomplete
    layer_norm1: Incomplete
    mlp: Incomplete
    layer_norm2: Incomplete
    def __init__(self, config: CLIPSegConfig) -> None: ...
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

class CLIPSegPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = CLIPSegConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool

CLIPSEG_START_DOCSTRING: str
CLIPSEG_TEXT_INPUTS_DOCSTRING: str
CLIPSEG_VISION_INPUTS_DOCSTRING: str
CLIPSEG_INPUTS_DOCSTRING: str

class CLIPSegEncoder(nn.Module):
    """
    Transformer encoder consisting of `config.num_hidden_layers` self attention layers. Each layer is a
    [`CLIPSegEncoderLayer`].

    Args:
        config: CLIPSegConfig
    """
    config: Incomplete
    layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: CLIPSegConfig) -> None: ...
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

class CLIPSegTextTransformer(nn.Module):
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: CLIPSegTextConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]:
        """
        Returns:

        """

class CLIPSegTextModel(CLIPSegPreTrainedModel):
    config_class = CLIPSegTextConfig
    text_model: Incomplete
    def __init__(self, config: CLIPSegTextConfig) -> None: ...
    def get_input_embeddings(self) -> nn.Module: ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, CLIPSegTextModel

        >>> tokenizer = AutoTokenizer.from_pretrained("CIDAS/clipseg-rd64-refined")
        >>> model = CLIPSegTextModel.from_pretrained("CIDAS/clipseg-rd64-refined")

        >>> inputs = tokenizer(["a photo of a cat", "a photo of a dog"], padding=True, return_tensors="pt")

        >>> outputs = model(**inputs)
        >>> last_hidden_state = outputs.last_hidden_state
        >>> pooled_output = outputs.pooler_output  # pooled (EOS token) states
        ```'''

class CLIPSegVisionTransformer(nn.Module):
    config: Incomplete
    embeddings: Incomplete
    pre_layrnorm: Incomplete
    encoder: Incomplete
    post_layernorm: Incomplete
    def __init__(self, config: CLIPSegVisionConfig) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]:
        """
        Returns:

        """

class CLIPSegVisionModel(CLIPSegPreTrainedModel):
    config_class = CLIPSegVisionConfig
    main_input_name: str
    vision_model: Incomplete
    def __init__(self, config: CLIPSegVisionConfig) -> None: ...
    def get_input_embeddings(self) -> nn.Module: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]:
        '''
        Returns:

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, CLIPSegVisionModel

        >>> processor = AutoProcessor.from_pretrained("CIDAS/clipseg-rd64-refined")
        >>> model = CLIPSegVisionModel.from_pretrained("CIDAS/clipseg-rd64-refined")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="pt")

        >>> outputs = model(**inputs)
        >>> last_hidden_state = outputs.last_hidden_state
        >>> pooled_output = outputs.pooler_output  # pooled CLS states
        ```'''

class CLIPSegModel(CLIPSegPreTrainedModel):
    config_class = CLIPSegConfig
    projection_dim: Incomplete
    text_embed_dim: Incomplete
    vision_embed_dim: Incomplete
    text_model: Incomplete
    vision_model: Incomplete
    visual_projection: Incomplete
    text_projection: Incomplete
    logit_scale: Incomplete
    def __init__(self, config: CLIPSegConfig) -> None: ...
    def get_text_features(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> torch.FloatTensor:
        '''
        Returns:
            text_features (`torch.FloatTensor` of shape `(batch_size, output_dim`): The text embeddings obtained by
            applying the projection layer to the pooled output of [`CLIPSegTextModel`].

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, CLIPSegModel

        >>> tokenizer = AutoTokenizer.from_pretrained("CIDAS/clipseg-rd64-refined")
        >>> model = CLIPSegModel.from_pretrained("CIDAS/clipseg-rd64-refined")

        >>> inputs = tokenizer(["a photo of a cat", "a photo of a dog"], padding=True, return_tensors="pt")
        >>> text_features = model.get_text_features(**inputs)
        ```'''
    def get_image_features(self, pixel_values: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> torch.FloatTensor:
        '''
        Returns:
            image_features (`torch.FloatTensor` of shape `(batch_size, output_dim`): The image embeddings obtained by
            applying the projection layer to the pooled output of [`CLIPSegVisionModel`].

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, CLIPSegModel

        >>> processor = AutoProcessor.from_pretrained("CIDAS/clipseg-rd64-refined")
        >>> model = CLIPSegModel.from_pretrained("CIDAS/clipseg-rd64-refined")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="pt")

        >>> image_features = model.get_image_features(**inputs)
        ```'''
    def forward(self, input_ids: Optional[torch.LongTensor] = None, pixel_values: Optional[torch.FloatTensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.LongTensor] = None, return_loss: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, CLIPSegOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, CLIPSegModel

        >>> processor = AutoProcessor.from_pretrained("CIDAS/clipseg-rd64-refined")
        >>> model = CLIPSegModel.from_pretrained("CIDAS/clipseg-rd64-refined")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(
        ...     text=["a photo of a cat", "a photo of a dog"], images=image, return_tensors="pt", padding=True
        ... )

        >>> outputs = model(**inputs)
        >>> logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
        >>> probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities
        ```'''

class CLIPSegDecoderLayer(nn.Module):
    """
    CLIPSeg decoder layer, which is identical to `CLIPSegEncoderLayer`, except that normalization is applied after
    self-attention/MLP, rather than before.
    """
    embed_dim: Incomplete
    self_attn: Incomplete
    layer_norm1: Incomplete
    mlp: Incomplete
    layer_norm2: Incomplete
    def __init__(self, config: CLIPSegConfig) -> None: ...
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

class CLIPSegDecoder(CLIPSegPreTrainedModel):
    conditional_layer: Incomplete
    film_mul: Incomplete
    film_add: Incomplete
    transposed_convolution: Incomplete
    reduces: Incomplete
    layers: Incomplete
    def __init__(self, config: CLIPSegConfig) -> None: ...
    def forward(self, hidden_states: Tuple[torch.Tensor], conditional_embeddings: torch.Tensor, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = True): ...

class CLIPSegForImageSegmentation(CLIPSegPreTrainedModel):
    config_class = CLIPSegConfig
    config: Incomplete
    clip: Incomplete
    extract_layers: Incomplete
    decoder: Incomplete
    def __init__(self, config: CLIPSegConfig) -> None: ...
    def get_conditional_embeddings(self, batch_size: int = None, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, conditional_pixel_values: Optional[torch.Tensor] = None): ...
    def forward(self, input_ids: Optional[torch.FloatTensor] = None, pixel_values: Optional[torch.FloatTensor] = None, conditional_pixel_values: Optional[torch.FloatTensor] = None, conditional_embeddings: Optional[torch.FloatTensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.LongTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, CLIPSegOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, CLIPSegForImageSegmentation
        >>> from PIL import Image
        >>> import requests

        >>> processor = AutoProcessor.from_pretrained("CIDAS/clipseg-rd64-refined")
        >>> model = CLIPSegForImageSegmentation.from_pretrained("CIDAS/clipseg-rd64-refined")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)
        >>> texts = ["a cat", "a remote", "a blanket"]
        >>> inputs = processor(text=texts, images=[image] * len(texts), padding=True, return_tensors="pt")

        >>> outputs = model(**inputs)

        >>> logits = outputs.logits
        >>> print(logits.shape)
        torch.Size([3, 352, 352])
        ```'''
