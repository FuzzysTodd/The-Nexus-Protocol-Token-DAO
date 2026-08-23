import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_blip import BlipConfig as BlipConfig, BlipTextConfig as BlipTextConfig, BlipVisionConfig as BlipVisionConfig
from .modeling_blip_text import BlipTextLMHeadModel as BlipTextLMHeadModel, BlipTextModel as BlipTextModel
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Any, Optional, Tuple, Union

logger: Incomplete
BLIP_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def contrastive_loss(logits: torch.Tensor) -> torch.Tensor: ...
def blip_loss(similarity: torch.Tensor) -> torch.Tensor: ...

@dataclass
class BlipForConditionalGenerationModelOutput(ModelOutput):
    """
    Adapted from the base class for vision model's outputs that also contains image embeddings of the pooling of the
    last hidden states. This class also adds the loss term from the text decoder.

    Args:
        loss (`torch.FloatTensor`, *optional*, returned when `labels` is provided, `torch.FloatTensor` of shape `(1,)`):
            Languge modeling loss from the text decoder.
        decoder_logits (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`, *optional*):
            Prediction scores of the language modeling head of the text decoder model.
        image_embeds (`torch.FloatTensor` of shape `(batch_size, output_dim)`, *optional*):
            The image embeddings obtained after applying the Vision Transformer model to the input image.
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the model.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[Tuple[torch.FloatTensor]] = ...
    decoder_logits: Optional[Tuple[torch.FloatTensor]] = ...
    image_embeds: Optional[torch.FloatTensor] = ...
    last_hidden_state: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, decoder_logits, image_embeds, last_hidden_state, hidden_states, attentions) -> None: ...

@dataclass
class BlipTextVisionModelOutput(ModelOutput):
    """
    Adapted from the base class for vision model's outputs that also contains image embeddings of the pooling of the
    last hidden states. This class also adds the loss term from the text decoder.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Languge modeling loss from the text decoder.
        image_embeds (`torch.FloatTensor` of shape `(batch_size, output_dim)` *optional* returned when model is initialized with `with_projection=True`):
            The image embeddings obtained by applying the projection layer to the pooler_output.
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    image_embeds: Optional[torch.FloatTensor] = ...
    last_hidden_state: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, image_embeds, last_hidden_state, hidden_states, attentions) -> None: ...

@dataclass
class BlipImageTextMatchingModelOutput(ModelOutput):
    """
    Adapted from the base class for vision model's outputs that also contains image embeddings of the pooling of the
    last hidden states. This class also adds the loss term from the text decoder as well as the image-text similarity
    scores.

    Args:
        itm_score (`torch.FloatTensor`):
            The image-text similarity scores.
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Languge modeling loss from the text decoder.
        image_embeds (`torch.FloatTensor` of shape `(batch_size, output_dim)` *optional* returned when model is initialized with `with_projection=True`):
            The image embeddings obtained by applying the projection layer to the pooler_output.
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
        vision_pooler_output (`torch.FloatTensor` of shape `(batch_size, hidden_size)`, *optional*):
            Last layer hidden-state of the vision of the vision-only branch of the model.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        question_embeds (`torch.FloatTensor`):
            The question embeddings obtained by the text projection layer.
    """
    itm_score: Optional[torch.FloatTensor] = ...
    loss: Optional[torch.FloatTensor] = ...
    image_embeds: Optional[torch.FloatTensor] = ...
    last_hidden_state: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    vision_pooler_output: Optional[torch.FloatTensor] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    question_embeds: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, itm_score, loss, image_embeds, last_hidden_state, hidden_states, vision_pooler_output, attentions, question_embeds) -> None: ...

@dataclass
class BlipOutput(ModelOutput):
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
            The text embeddings obtained by applying the projection layer to the pooled output of [`BlipTextModel`].
        image_embeds(`torch.FloatTensor` of shape `(batch_size, output_dim`):
            The image embeddings obtained by applying the projection layer to the pooled output of [`BlipVisionModel`].
        text_model_output(`BaseModelOutputWithPooling`):
            The output of the [`BlipTextModel`].
        vision_model_output(`BaseModelOutputWithPooling`):
            The output of the [`BlipVisionModel`].
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

class BlipVisionEmbeddings(nn.Module):
    config: Incomplete
    embed_dim: Incomplete
    image_size: Incomplete
    patch_size: Incomplete
    class_embedding: Incomplete
    patch_embedding: Incomplete
    num_patches: Incomplete
    num_positions: Incomplete
    position_embedding: Incomplete
    def __init__(self, config: BlipVisionConfig) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor) -> torch.Tensor: ...

class BlipTextEmbeddings(nn.Module):
    token_embedding: Incomplete
    position_embedding: Incomplete
    def __init__(self, config: BlipTextConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None) -> torch.Tensor: ...

class BlipAttention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    config: Incomplete
    embed_dim: Incomplete
    num_heads: Incomplete
    head_dim: Incomplete
    scale: Incomplete
    dropout: Incomplete
    qkv: Incomplete
    projection: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        """Input shape: Batch x Time x Channel"""

class BlipMLP(nn.Module):
    config: Incomplete
    activation_fn: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class BlipEncoderLayer(nn.Module):
    embed_dim: Incomplete
    self_attn: Incomplete
    layer_norm1: Incomplete
    mlp: Incomplete
    layer_norm2: Incomplete
    def __init__(self, config: BlipConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: torch.Tensor, output_attentions: Optional[bool] = False) -> Tuple[torch.FloatTensor]:
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

class BlipPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = BlipConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool

BLIP_START_DOCSTRING: str
BLIP_TEXT_INPUTS_DOCSTRING: str
BLIP_VISION_INPUTS_DOCSTRING: str
BLIP_INPUTS_DOCSTRING: str

class BlipEncoder(nn.Module):
    """
    Transformer encoder consisting of `config.num_hidden_layers` self attention layers. Each layer is a
    [`BlipEncoderLayer`].

    Args:
        config (`BlipConfig`):
            The corresponding vision configuration for the `BlipEncoder`.
    """
    config: Incomplete
    layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: BlipConfig) -> None: ...
    def forward(self, inputs_embeds, attention_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]:
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
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """

class BlipVisionModel(BlipPreTrainedModel):
    main_input_name: str
    config_class = BlipVisionConfig
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    post_layernorm: Incomplete
    def __init__(self, config: BlipVisionConfig) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]:
        """
        Returns:

        """
    def get_input_embeddings(self): ...

class BlipModel(BlipPreTrainedModel):
    config_class = BlipConfig
    projection_dim: Incomplete
    text_embed_dim: Incomplete
    vision_embed_dim: Incomplete
    text_model: Incomplete
    vision_model: Incomplete
    visual_projection: Incomplete
    text_projection: Incomplete
    logit_scale: Incomplete
    def __init__(self, config: BlipConfig) -> None: ...
    def get_text_features(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, return_dict: Optional[bool] = None) -> torch.FloatTensor:
        '''
        Returns:
            text_features (`torch.FloatTensor` of shape `(batch_size, output_dim`): The text embeddings obtained by
            applying the projection layer to the pooled output of [`BlipTextModel`].

        Examples:

        ```python
        >>> from transformers import AutoProcessor, BlipModel

        >>> model = BlipModel.from_pretrained("Salesforce/blip-image-captioning-base")
        >>> processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

        >>> inputs = processor(text=["a photo of a cat", "a photo of a dog"], padding=True, return_tensors="pt")
        >>> text_features = model.get_text_features(**inputs)
        ```'''
    def get_image_features(self, pixel_values: Optional[torch.FloatTensor] = None, return_dict: Optional[bool] = None) -> torch.FloatTensor:
        '''
        Returns:
            image_features (`torch.FloatTensor` of shape `(batch_size, output_dim`): The image embeddings obtained by
            applying the projection layer to the pooled output of [`BlipVisionModel`].

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, BlipModel

        >>> model = BlipModel.from_pretrained("Salesforce/blip-image-captioning-base")
        >>> processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="pt")

        >>> image_features = model.get_image_features(**inputs)
        ```'''
    def forward(self, input_ids: Optional[torch.LongTensor] = None, pixel_values: Optional[torch.FloatTensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.LongTensor] = None, return_loss: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BlipOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, BlipModel

        >>> model = BlipModel.from_pretrained("Salesforce/blip-image-captioning-base")
        >>> processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(
        ...     text=["a photo of a cat", "a photo of a dog"], images=image, return_tensors="pt", padding=True
        ... )

        >>> outputs = model(**inputs)
        >>> logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
        >>> probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities
        ```'''

class BlipForConditionalGeneration(BlipPreTrainedModel):
    config_class = BlipConfig
    main_input_name: str
    vision_model: Incomplete
    text_decoder: Incomplete
    decoder_input_ids: Incomplete
    decoder_pad_token_id: Incomplete
    def __init__(self, config: BlipConfig) -> None: ...
    def get_input_embeddings(self) -> nn.Module: ...
    def forward(self, pixel_values: torch.FloatTensor, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, labels: Optional[torch.LongTensor] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BlipForConditionalGenerationModelOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, BlipForConditionalGeneration

        >>> processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        >>> model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="pt")

        >>> outputs = model(**inputs)
        ```'''
    def generate(self, pixel_values: torch.FloatTensor, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.LongTensor] = None, **generate_kwargs) -> torch.LongTensor:
        '''
        Overrides *generate* function to be able to use the model as a conditional generator

        Parameters:
            pixel_values (*torch.FloatTensor* of shape *(batch_size, image_width, image_height)*:
                Input image to be processed
            input_ids (*torch.LongTensor* of shape *(batch_size, sequence_length)*, *optional*):
                The sequence used as a prompt for the generation.
            attention_mask (*torch.LongTensor* of shape *(batch_size, sequence_length)*, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:


        Examples:
        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, BlipForConditionalGeneration

        >>> model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        >>> processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="pt")

        >>> outputs = model.generate(**inputs)
        >>> print(processor.decode(outputs[0], skip_special_tokens=True))
        two cats are laying on a couch
        ```
        '''

class BlipForQuestionAnswering(BlipPreTrainedModel):
    config_class = BlipConfig
    vision_model: Incomplete
    text_encoder: Incomplete
    text_decoder: Incomplete
    decoder_pad_token_id: Incomplete
    decoder_start_token_id: Incomplete
    def __init__(self, config: BlipConfig) -> None: ...
    def get_input_embeddings(self) -> nn.Module: ...
    def forward(self, input_ids: torch.LongTensor, pixel_values: torch.FloatTensor, decoder_input_ids: Optional[torch.LongTensor] = None, decoder_attention_mask: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, labels: Optional[torch.LongTensor] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BlipTextVisionModelOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, BlipForQuestionAnswering

        >>> model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")
        >>> processor = AutoProcessor.from_pretrained("Salesforce/blip-vqa-base")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> # training
        >>> text = "How many cats are in the picture?"
        >>> label = "2"
        >>> inputs = processor(images=image, text=text, return_tensors="pt")
        >>> labels = processor(text=label, return_tensors="pt").input_ids

        >>> inputs["labels"] = labels
        >>> outputs = model(**inputs)
        >>> loss = outputs.loss
        >>> loss.backward()

        >>> # inference
        >>> text = "How many cats are in the picture?"
        >>> inputs = processor(images=image, text=text, return_tensors="pt")
        >>> outputs = model.generate(**inputs)
        >>> print(processor.decode(outputs[0], skip_special_tokens=True))
        2
        ```'''
    def generate(self, input_ids: torch.LongTensor, pixel_values: torch.FloatTensor, attention_mask: Optional[torch.LongTensor] = None, **generate_kwargs) -> torch.LongTensor:
        '''
        Overrides *generate* function to be able to use the model as a conditional generator

        Parameters:
            input_ids (*torch.LongTensor* of shape *(batch_size, sequence_length)*):
                The sequence used as a prompt for the generation.
            pixel_values (*torch.FloatTensor* of shape *(batch_size, image_width, image_height)*:
                Input image to be processed
            attention_mask (*torch.LongTensor* of shape *(batch_size, sequence_length)*, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`. `1` for
                tokens that are NOT MASKED, `0` for MASKED tokens.
            **generate_kwargs:
                Additional arguments passed to the *generate* function of the decoder


        Examples:
        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, BlipForQuestionAnswering

        >>> model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")
        >>> processor = AutoProcessor.from_pretrained("Salesforce/blip-vqa-base")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)
        >>> text = "How many cats are in the picture?"

        >>> inputs = processor(images=image, text=text, return_tensors="pt")

        >>> outputs = model.generate(**inputs)
        >>> print(processor.decode(outputs[0], skip_special_tokens=True))
        2
        ```
        '''

class BlipForImageTextRetrieval(BlipPreTrainedModel):
    config_class = BlipConfig
    vision_model: Incomplete
    text_encoder: Incomplete
    vision_proj: Incomplete
    text_proj: Incomplete
    itm_head: Incomplete
    decoder_pad_token_id: Incomplete
    decoder_start_token_id: Incomplete
    def __init__(self, config: BlipConfig) -> None: ...
    def get_input_embeddings(self) -> nn.Module: ...
    def forward(self, input_ids: torch.LongTensor, pixel_values: torch.FloatTensor, use_itm_head: Optional[bool] = True, attention_mask: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BlipTextVisionModelOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, BlipForImageTextRetrieval

        >>> model = BlipForImageTextRetrieval.from_pretrained("Salesforce/blip-itm-base-coco")
        >>> processor = AutoProcessor.from_pretrained("Salesforce/blip-itm-base-coco")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)
        >>> text = "an image of a cat"

        >>> inputs = processor(images=image, text=text, return_tensors="pt")
        >>> outputs = model(**inputs)
        ```
        '''
