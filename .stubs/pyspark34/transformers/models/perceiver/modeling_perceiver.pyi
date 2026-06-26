import abc
import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutputWithCrossAttentions as BaseModelOutputWithCrossAttentions
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import apply_chunking_to_forward as apply_chunking_to_forward, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, meshgrid as meshgrid, prune_linear_layer as prune_linear_layer
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_perceiver import PerceiverConfig as PerceiverConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Any, Callable, Dict, List, Mapping, Optional, Tuple, Union

ModalitySizeType = Mapping[str, int]
PreprocessorOutputType: Incomplete
PreprocessorType = Callable[..., PreprocessorOutputType]
PostprocessorType = Callable[..., Any]
logger: Incomplete
PERCEIVER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class PerceiverModelOutput(ModelOutput):
    """
    Base class for Perceiver base model's outputs, with potential hidden states, attentions and cross-attentions.

    Args:
        logits (`torch.FloatTensor` of shape `(batch_size, num_labels)`):
            Classification (or regression if config.num_labels==1) scores (before SoftMax).
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
        cross_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights of the decoder's cross-attention layer, after the attention softmax,
            used to compute the weighted average in the cross-attention heads.
    """
    logits: torch.FloatTensor = ...
    last_hidden_state: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    cross_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, logits, last_hidden_state, hidden_states, attentions, cross_attentions) -> None: ...

@dataclass
class PerceiverDecoderOutput(ModelOutput):
    """
    Base class for Perceiver decoder outputs, with potential cross-attentions.

    Args:
        logits (`torch.FloatTensor` of shape `(batch_size, num_labels)`):
            Output of the basic decoder.
        cross_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights of the decoder's cross-attention layer, after the attention softmax,
            used to compute the weighted average in the cross-attention heads.
    """
    logits: torch.FloatTensor = ...
    cross_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, logits, cross_attentions) -> None: ...

@dataclass
class PerceiverMaskedLMOutput(ModelOutput):
    """
    Base class for Perceiver's masked language model outputs.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Masked language modeling (MLM) loss.
        logits (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, num_latents,
            num_latents)`. Attentions weights after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        cross_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights of the decoder's cross-attention layer, after the attention softmax,
            used to compute the weighted average in the cross-attention heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    cross_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, hidden_states, attentions, cross_attentions) -> None: ...

@dataclass
class PerceiverClassifierOutput(ModelOutput):
    """
    Base class for Perceiver's outputs of sequence/image classification models, optical flow and multimodal
    autoencoding.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Classification (or regression if config.num_labels==1) loss.
        logits (`torch.FloatTensor` of shape `(batch_size, config.num_labels)`):
            Classification (or regression if config.num_labels==1) scores (before SoftMax).
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
        cross_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights of the decoder's cross-attention layer, after the attention softmax,
            used to compute the weighted average in the cross-attention heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    cross_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, hidden_states, attentions, cross_attentions) -> None: ...

class PerceiverEmbeddings(nn.Module):
    """Construct the latent embeddings."""
    latents: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, batch_size: int): ...

class PerceiverSelfAttention(nn.Module):
    """Multi-headed {cross, self}-attention. Can be used both in the encoder as well as in the decoder."""
    num_heads: Incomplete
    qk_channels: Incomplete
    v_channels: Incomplete
    qk_channels_per_head: Incomplete
    v_channels_per_head: Incomplete
    layernorm1: Incomplete
    layernorm2: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config, is_cross_attention: bool = False, qk_channels: Incomplete | None = None, v_channels: Incomplete | None = None, num_heads: int = 1, q_dim: Incomplete | None = None, kv_dim: Incomplete | None = None) -> None: ...
    def transpose_for_scores(self, x, channels_per_head): ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs: Optional[torch.FloatTensor] = None, inputs_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class PerceiverSelfOutput(nn.Module):
    dense: Incomplete
    def __init__(self, config, input_channels, output_channels) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class PerceiverAttention(nn.Module):
    """Attention module, including a dense block."""
    self: Incomplete
    output: Incomplete
    use_query_residual: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config, is_cross_attention: bool = False, qk_channels: Incomplete | None = None, v_channels: Incomplete | None = None, num_heads: int = 1, q_dim: Incomplete | None = None, kv_dim: Incomplete | None = None, use_query_residual: bool = True) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs: Optional[torch.FloatTensor] = None, inputs_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class PerceiverMLP(nn.Module):
    """A Transformer-style dense module to follow attention."""
    dense1: Incomplete
    intermediate_act_fn: Incomplete
    dense2: Incomplete
    def __init__(self, config, input_size, widening_factor) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class PerceiverLayer(nn.Module):
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    layernorm: Incomplete
    mlp: Incomplete
    def __init__(self, config, is_cross_attention: bool = False, qk_channels: Incomplete | None = None, v_channels: Incomplete | None = None, num_heads: int = 1, q_dim: Incomplete | None = None, kv_dim: Incomplete | None = None, widening_factor: int = 4, use_query_residual: bool = True) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs: Optional[torch.FloatTensor] = None, inputs_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...
    def feed_forward_chunk(self, attention_output): ...

class PerceiverEncoder(nn.Module):
    """The Perceiver Encoder: a scalable, fully attentional encoder."""
    config: Incomplete
    cross_attention: Incomplete
    self_attends: Incomplete
    def __init__(self, config, kv_dim: Incomplete | None = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs: Optional[torch.FloatTensor] = None, inputs_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False, output_hidden_states: Optional[bool] = False, return_dict: Optional[bool] = True) -> Union[Tuple, BaseModelOutputWithCrossAttentions]: ...

class PerceiverPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = PerceiverConfig
    base_model_prefix: str
    main_input_name: str

PERCEIVER_START_DOCSTRING: str
PERCEIVER_MODEL_START_DOCSTRING: str
PERCEIVER_INPUTS_DOCSTRING: str

class PerceiverModel(PerceiverPreTrainedModel):
    config: Incomplete
    input_preprocessor: Incomplete
    output_postprocessor: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, config, decoder: Incomplete | None = None, input_preprocessor: PreprocessorType = None, output_postprocessor: PostprocessorType = None) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, inputs: torch.FloatTensor, attention_mask: Optional[torch.FloatTensor] = None, subsampled_output_points: Optional[Dict[str, torch.Tensor]] = None, head_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, PerceiverModelOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import PerceiverConfig, AutoTokenizer, PerceiverImageProcessor, PerceiverModel
        >>> from transformers.models.perceiver.modeling_perceiver import (
        ...     PerceiverTextPreprocessor,
        ...     PerceiverImagePreprocessor,
        ...     PerceiverClassificationDecoder,
        ... )
        >>> import torch
        >>> import requests
        >>> from PIL import Image

        >>> # EXAMPLE 1: using the Perceiver to classify texts
        >>> # - we define a TextPreprocessor, which can be used to embed tokens
        >>> # - we define a ClassificationDecoder, which can be used to decode the
        >>> # final hidden states of the latents to classification logits
        >>> # using trainable position embeddings
        >>> config = PerceiverConfig()
        >>> preprocessor = PerceiverTextPreprocessor(config)
        >>> decoder = PerceiverClassificationDecoder(
        ...     config,
        ...     num_channels=config.d_latents,
        ...     trainable_position_encoding_kwargs=dict(num_channels=config.d_latents, index_dims=1),
        ...     use_query_residual=True,
        ... )
        >>> model = PerceiverModel(config, input_preprocessor=preprocessor, decoder=decoder)

        >>> # you can then do a forward pass as follows:
        >>> tokenizer = AutoTokenizer()
        >>> text = "hello world"
        >>> inputs = tokenizer(text, return_tensors="pt").input_ids

        >>> with torch.no_grad():
        ...     outputs = model(inputs=inputs)
        >>> logits = outputs.logits
        >>> list(logits.shape)
        [1, 2]

        >>> # to train, one can train the model using standard cross-entropy:
        >>> criterion = torch.nn.CrossEntropyLoss()

        >>> labels = torch.tensor([1])
        >>> loss = criterion(logits, labels)

        >>> # EXAMPLE 2: using the Perceiver to classify images
        >>> # - we define an ImagePreprocessor, which can be used to embed images
        >>> config = PerceiverConfig(image_size=224)
        >>> preprocessor = PerceiverImagePreprocessor(
        ...     config,
        ...     prep_type="conv1x1",
        ...     spatial_downsample=1,
        ...     out_channels=256,
        ...     position_encoding_type="trainable",
        ...     concat_or_add_pos="concat",
        ...     project_pos_dim=256,
        ...     trainable_position_encoding_kwargs=dict(
        ...         num_channels=256,
        ...         index_dims=config.image_size**2,
        ...     ),
        ... )

        >>> model = PerceiverModel(
        ...     config,
        ...     input_preprocessor=preprocessor,
        ...     decoder=PerceiverClassificationDecoder(
        ...         config,
        ...         num_channels=config.d_latents,
        ...         trainable_position_encoding_kwargs=dict(num_channels=config.d_latents, index_dims=1),
        ...         use_query_residual=True,
        ...     ),
        ... )

        >>> # you can then do a forward pass as follows:
        >>> image_processor = PerceiverImageProcessor()
        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)
        >>> inputs = image_processor(image, return_tensors="pt").pixel_values

        >>> with torch.no_grad():
        ...     outputs = model(inputs=inputs)
        >>> logits = outputs.logits
        >>> list(logits.shape)
        [1, 2]

        >>> # to train, one can train the model using standard cross-entropy:
        >>> criterion = torch.nn.CrossEntropyLoss()

        >>> labels = torch.tensor([1])
        >>> loss = criterion(logits, labels)
        ```'''

class PerceiverForMaskedLM(PerceiverPreTrainedModel):
    perceiver: Incomplete
    embedding_decoder: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, inputs: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, labels: Optional[torch.Tensor] = None, return_dict: Optional[bool] = None, input_ids: Optional[torch.Tensor] = None) -> Union[Tuple, PerceiverMaskedLMOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, PerceiverForMaskedLM
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("deepmind/language-perceiver")
        >>> model = PerceiverForMaskedLM.from_pretrained("deepmind/language-perceiver")

        >>> # training
        >>> text = "This is an incomplete sentence where some words are missing."
        >>> inputs = tokenizer(text, padding="max_length", return_tensors="pt")
        >>> # mask " missing."
        >>> inputs["input_ids"][0, 52:61] = tokenizer.mask_token_id
        >>> labels = tokenizer(text, padding="max_length", return_tensors="pt").input_ids

        >>> outputs = model(**inputs, labels=labels)
        >>> loss = outputs.loss
        >>> round(loss.item(), 2)
        19.87

        >>> logits = outputs.logits
        >>> list(logits.shape)
        [1, 2048, 262]

        >>> # inference
        >>> text = "This is an incomplete sentence where some words are missing."
        >>> encoding = tokenizer(text, padding="max_length", return_tensors="pt")

        >>> # mask bytes corresponding to " missing.". Note that the model performs much better if the masked span starts with a space.
        >>> encoding["input_ids"][0, 52:61] = tokenizer.mask_token_id

        >>> # forward pass
        >>> with torch.no_grad():
        ...     outputs = model(**encoding)
        >>> logits = outputs.logits
        >>> list(logits.shape)
        [1, 2048, 262]

        >>> masked_tokens_predictions = logits[0, 52:61].argmax(dim=-1).tolist()
        >>> tokenizer.decode(masked_tokens_predictions)
        \' missing.\'
        ```'''

class PerceiverForSequenceClassification(PerceiverPreTrainedModel):
    num_labels: Incomplete
    perceiver: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, inputs: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, labels: Optional[torch.Tensor] = None, return_dict: Optional[bool] = None, input_ids: Optional[torch.Tensor] = None) -> Union[Tuple, PerceiverClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the classification/regression loss. Indices should be in `[0, ..., config.num_labels -
            1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If `config.num_labels >
            1` a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, PerceiverForSequenceClassification

        >>> tokenizer = AutoTokenizer.from_pretrained("deepmind/language-perceiver")
        >>> model = PerceiverForSequenceClassification.from_pretrained("deepmind/language-perceiver")

        >>> text = "hello world"
        >>> inputs = tokenizer(text, return_tensors="pt").input_ids
        >>> outputs = model(inputs=inputs)
        >>> logits = outputs.logits
        >>> list(logits.shape)
        [1, 2]
        ```'''

class PerceiverForImageClassificationLearned(PerceiverPreTrainedModel):
    num_labels: Incomplete
    perceiver: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, inputs: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, labels: Optional[torch.Tensor] = None, return_dict: Optional[bool] = None, pixel_values: Optional[torch.Tensor] = None) -> Union[Tuple, PerceiverClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, PerceiverForImageClassificationLearned
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("deepmind/vision-perceiver-learned")
        >>> model = PerceiverForImageClassificationLearned.from_pretrained("deepmind/vision-perceiver-learned")

        >>> inputs = image_processor(images=image, return_tensors="pt").pixel_values
        >>> outputs = model(inputs=inputs)
        >>> logits = outputs.logits
        >>> list(logits.shape)
        [1, 1000]

        >>> # model predicts one of the 1000 ImageNet classes
        >>> predicted_class_idx = logits.argmax(-1).item()
        >>> print("Predicted class:", model.config.id2label[predicted_class_idx])
        Predicted class: tabby, tabby cat
        ```'''

class PerceiverForImageClassificationFourier(PerceiverPreTrainedModel):
    num_labels: Incomplete
    perceiver: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, inputs: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, labels: Optional[torch.Tensor] = None, return_dict: Optional[bool] = None, pixel_values: Optional[torch.Tensor] = None) -> Union[Tuple, PerceiverClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, PerceiverForImageClassificationFourier
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("deepmind/vision-perceiver-fourier")
        >>> model = PerceiverForImageClassificationFourier.from_pretrained("deepmind/vision-perceiver-fourier")

        >>> inputs = image_processor(images=image, return_tensors="pt").pixel_values
        >>> outputs = model(inputs=inputs)
        >>> logits = outputs.logits
        >>> list(logits.shape)
        [1, 1000]

        >>> # model predicts one of the 1000 ImageNet classes
        >>> predicted_class_idx = logits.argmax(-1).item()
        >>> print("Predicted class:", model.config.id2label[predicted_class_idx])
        Predicted class: tabby, tabby cat
        ```'''

class PerceiverForImageClassificationConvProcessing(PerceiverPreTrainedModel):
    num_labels: Incomplete
    perceiver: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, inputs: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, labels: Optional[torch.Tensor] = None, return_dict: Optional[bool] = None, pixel_values: Optional[torch.Tensor] = None) -> Union[Tuple, PerceiverClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, PerceiverForImageClassificationConvProcessing
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("deepmind/vision-perceiver-conv")
        >>> model = PerceiverForImageClassificationConvProcessing.from_pretrained("deepmind/vision-perceiver-conv")

        >>> inputs = image_processor(images=image, return_tensors="pt").pixel_values
        >>> outputs = model(inputs=inputs)
        >>> logits = outputs.logits
        >>> list(logits.shape)
        [1, 1000]

        >>> # model predicts one of the 1000 ImageNet classes
        >>> predicted_class_idx = logits.argmax(-1).item()
        >>> print("Predicted class:", model.config.id2label[predicted_class_idx])
        Predicted class: tabby, tabby cat
        ```'''

class PerceiverForOpticalFlow(PerceiverPreTrainedModel):
    perceiver: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, inputs: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, labels: Optional[torch.Tensor] = None, return_dict: Optional[bool] = None) -> Union[Tuple, PerceiverClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the optical flow loss. Indices should be in `[0, ..., config.num_labels - 1]`.

        Returns:

        Examples:

        ```python
        >>> from transformers import PerceiverForOpticalFlow
        >>> import torch

        >>> model = PerceiverForOpticalFlow.from_pretrained("deepmind/optical-flow-perceiver")

        >>> # in the Perceiver IO paper, the authors extract a 3 x 3 patch around each pixel,
        >>> # leading to 3 x 3 x 3 = 27 values for each pixel (as each pixel also has 3 color channels)
        >>> # patches have shape (batch_size, num_frames, num_channels, height, width)
        >>> # the authors train on resolutions of 368 x 496
        >>> patches = torch.randn(1, 2, 27, 368, 496)
        >>> outputs = model(inputs=patches)
        >>> logits = outputs.logits
        >>> list(logits.shape)
        [1, 368, 496, 2]
        ```'''

class PerceiverForMultimodalAutoencoding(PerceiverPreTrainedModel):
    perceiver: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, inputs: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, subsampled_output_points: Optional[Dict[str, torch.Tensor]] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, labels: Optional[torch.Tensor] = None, return_dict: Optional[bool] = None) -> Union[Tuple, PerceiverClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import PerceiverForMultimodalAutoencoding
        >>> import torch
        >>> import numpy as np

        >>> # create multimodal inputs
        >>> images = torch.randn((1, 16, 3, 224, 224))
        >>> audio = torch.randn((1, 30720, 1))
        >>> inputs = dict(image=images, audio=audio, label=torch.zeros((images.shape[0], 700)))

        >>> model = PerceiverForMultimodalAutoencoding.from_pretrained("deepmind/multimodal-perceiver")

        >>> # in the Perceiver IO paper, videos are auto-encoded in chunks
        >>> # each chunk subsamples different index dimensions of the image and audio modality decoder queries
        >>> nchunks = 128
        >>> image_chunk_size = np.prod((16, 224, 224)) // nchunks
        >>> audio_chunk_size = audio.shape[1] // model.config.samples_per_patch // nchunks
        >>> # process the first chunk
        >>> chunk_idx = 0
        >>> subsampling = {
        ...     "image": torch.arange(image_chunk_size * chunk_idx, image_chunk_size * (chunk_idx + 1)),
        ...     "audio": torch.arange(audio_chunk_size * chunk_idx, audio_chunk_size * (chunk_idx + 1)),
        ...     "label": None,
        ... }

        >>> outputs = model(inputs=inputs, subsampled_output_points=subsampling)
        >>> logits = outputs.logits
        >>> list(logits["audio"].shape)
        [1, 240]

        >>> list(logits["image"].shape)
        [1, 6272, 3]

        >>> list(logits["label"].shape)
        [1, 700]
        ```'''

def build_position_encoding(position_encoding_type, out_channels: Incomplete | None = None, project_pos_dim: int = -1, trainable_position_encoding_kwargs: Incomplete | None = None, fourier_position_encoding_kwargs: Incomplete | None = None):
    """
    Builds the position encoding.

    Args:
    - out_channels: refers to the number of channels of the position encodings.
    - project_pos_dim: if specified, will project the position encodings to this dimension.

    """

class PerceiverAbstractDecoder(nn.Module, metaclass=abc.ABCMeta):
    """Perceiver abstract decoder."""
    @abc.abstractmethod
    def decoder_query(self, inputs, modality_sizes: Incomplete | None = None, inputs_without_pos: Incomplete | None = None, subsampled_points: Incomplete | None = None): ...
    @property
    @abc.abstractmethod
    def num_query_channels(self): ...
    @abc.abstractmethod
    def forward(self, query, z, query_mask: Incomplete | None = None): ...

class PerceiverProjectionDecoder(PerceiverAbstractDecoder, metaclass=abc.ABCMeta):
    """
    Baseline projection decoder (no cross-attention).

    Args:
        config ([`PerceiverConfig`]):
            Model configuration.
    """
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def decoder_query(self, inputs, modality_sizes: Incomplete | None = None, inputs_without_pos: Incomplete | None = None, subsampled_points: Incomplete | None = None) -> None: ...
    def forward(self, query: torch.Tensor, z: torch.FloatTensor, query_mask: Optional[torch.FloatTensor] = None) -> torch.FloatTensor: ...

class PerceiverBasicDecoder(PerceiverAbstractDecoder):
    '''
    Cross-attention-based decoder. This class can be used to decode the final hidden states of the latents using a
    cross-attention operation, in which the latents produce keys and values.

    The shape of the output of this class depends on how one defines the output queries (also called decoder queries).

    Args:
        config ([*PerceiverConfig*]):
            Model configuration.
        output_num_channels (`int`, *optional*):
            The number of channels in the output. Will only be used in case *final_project* is set to `True`.
        position_encoding_type (`str`, *optional*, defaults to "trainable"):
            The type of position encoding to use. Can be either "trainable", "fourier", or "none".
        output_index_dims (`int`, *optional*):
            The number of dimensions of the output queries. Ignored if \'position_encoding_type\' == \'none\'.
        num_channels (`int`, *optional*, defaults to 128):
            The number of channels of the decoder queries. Ignored if \'position_encoding_type\' == \'none\'.
        qk_channels (`int`, *optional*):
            The number of channels of the queries and keys in the cross-attention layer.
        v_channels (`int`, *optional*):
            The number of channels of the values in the cross-attention layer.
        num_heads (`int`, *optional*, defaults to 1):
            The number of attention heads in the cross-attention layer.
        widening_factor (`int`, *optional*, defaults to 1):
            The widening factor of the cross-attention layer.
        use_query_residual (`bool`, *optional*, defaults to `False`):
            Whether to use a residual connection between the query and the output of the cross-attention layer.
        concat_preprocessed_input (`bool`, *optional*, defaults to `False`):
            Whether to concatenate the preprocessed input to the query.
        final_project (`bool`, *optional*, defaults to `True`):
            Whether to project the output of the cross-attention layer to a target dimension.
        position_encoding_only (`bool`, *optional*, defaults to `False`):
            Whether to only use this class to define output queries.
    '''
    output_num_channels: Incomplete
    output_position_encodings: Incomplete
    position_encoding_type: Incomplete
    position_encoding_kwargs: Incomplete
    output_index_dims: Incomplete
    num_channels: Incomplete
    subsampled_index_dims: Incomplete
    concat_preprocessed_input: Incomplete
    final_project: Incomplete
    position_encoding_only: Incomplete
    decoding_cross_attention: Incomplete
    final_layer: Incomplete
    def __init__(self, config: PerceiverConfig, output_num_channels: int, position_encoding_type: Optional[str] = 'trainable', output_index_dims: Optional[int] = None, num_channels: Optional[int] = 128, subsampled_index_dims: Optional[int] = None, qk_channels: Optional[int] = None, v_channels: Optional[int] = None, num_heads: Optional[int] = 1, widening_factor: Optional[int] = 1, use_query_residual: Optional[bool] = False, concat_preprocessed_input: Optional[bool] = False, final_project: Optional[bool] = True, position_encoding_only: Optional[bool] = False, **position_encoding_kwargs) -> None: ...
    @property
    def num_query_channels(self) -> int: ...
    def decoder_query(self, inputs, modality_sizes: Incomplete | None = None, inputs_without_pos: Incomplete | None = None, subsampled_points: Incomplete | None = None): ...
    def forward(self, query: torch.Tensor, z: torch.FloatTensor, query_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> PerceiverDecoderOutput: ...

class PerceiverClassificationDecoder(PerceiverAbstractDecoder):
    """
    Cross-attention based classification decoder. Light-weight wrapper of [`PerceiverBasicDecoder`] for logit output.
    Will turn the output of the Perceiver encoder which is of shape (batch_size, num_latents, d_latents) to a tensor of
    shape (batch_size, num_labels). The queries are of shape (batch_size, 1, num_labels).

    Args:
        config ([`PerceiverConfig`]):
            Model configuration.
    """
    num_labels: Incomplete
    decoder: Incomplete
    def __init__(self, config, **decoder_kwargs) -> None: ...
    @property
    def num_query_channels(self) -> int: ...
    def decoder_query(self, inputs, modality_sizes: Incomplete | None = None, inputs_without_pos: Incomplete | None = None, subsampled_points: Incomplete | None = None): ...
    def forward(self, query: torch.Tensor, z: torch.FloatTensor, query_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> PerceiverDecoderOutput: ...

class PerceiverOpticalFlowDecoder(PerceiverAbstractDecoder):
    """Cross-attention based optical flow decoder."""
    output_image_shape: Incomplete
    output_num_channels: Incomplete
    rescale_factor: Incomplete
    decoder: Incomplete
    def __init__(self, config, output_image_shape, output_num_channels: int = 2, rescale_factor: float = 100.0, **decoder_kwargs) -> None: ...
    @property
    def num_query_channels(self) -> int: ...
    def decoder_query(self, inputs, modality_sizes: Incomplete | None = None, inputs_without_pos: Incomplete | None = None, subsampled_points: Incomplete | None = None): ...
    def forward(self, query: torch.Tensor, z: torch.FloatTensor, query_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> PerceiverDecoderOutput: ...

class PerceiverBasicVideoAutoencodingDecoder(PerceiverAbstractDecoder):
    '''
    Cross-attention based video-autoencoding decoder. Light-weight wrapper of [*PerceiverBasicDecoder*] with video
    reshaping logic.

    Args:
        config ([*PerceiverConfig*]):
            Model configuration.
        output_shape (`List[int]`):
            Shape of the output as (batch_size, num_frames, height, width), excluding the channel dimension.
        position_encoding_type (`str`):
            The type of position encoding to use. Can be either "trainable", "fourier", or "none".
    '''
    output_shape: Incomplete
    output_num_channels: Incomplete
    decoder: Incomplete
    def __init__(self, config: PerceiverConfig, output_shape: List[int], position_encoding_type: str, **decoder_kwargs) -> None: ...
    @property
    def num_query_channels(self) -> int: ...
    def decoder_query(self, inputs, modality_sizes: Incomplete | None = None, inputs_without_pos: Incomplete | None = None, subsampled_points: Incomplete | None = None): ...
    def forward(self, query: torch.Tensor, z: torch.FloatTensor, query_mask: Optional[torch.FloatTensor] = None) -> PerceiverDecoderOutput: ...

def restructure(modality_sizes: ModalitySizeType, inputs: torch.Tensor) -> Mapping[str, torch.Tensor]:
    """
    Partitions a [B, N, C] tensor into tensors for each modality.

    Args:
        modality_sizes
            dict specifying the size of the modality
        inputs:
            input tensor

    Returns:
        dict mapping name of modality to its associated tensor.
    """

class PerceiverMultimodalDecoder(PerceiverAbstractDecoder):
    """
    Multimodal decoding by composing uni-modal decoders. The *modalities* argument of the constructor is a dictionary
    mapping modality name to the decoder of that modality. That decoder will be used to construct queries for that
    modality. Modality-specific queries are padded with trainable modality-specific parameters, after which they are
    concatenated along the time dimension.

    Next, there is a shared cross attention operation across all modalities.

    Args:
        config ([*PerceiverConfig*]):
            Model configuration.
        modalities (`Dict[str, PerceiverAbstractDecoder]`):
            Dictionary mapping modality name to the decoder of that modality.
        num_outputs (`int`):
            The number of outputs of the decoder.
        output_num_channels (`int`):
            The number of channels in the output.
        min_padding_size (`int`, *optional*, defaults to 2):
            The minimum padding size for all modalities. The final output will have num_channels equal to the maximum
            channels across all modalities plus min_padding_size.
        subsampled_index_dims (`Dict[str, PerceiverAbstractDecoder]`, *optional*):
            Dictionary mapping modality name to the subsampled index dimensions to use for the decoder query of that
            modality.
    """
    modalities: Incomplete
    subsampled_index_dims: Incomplete
    min_padding_size: Incomplete
    output_num_channels: Incomplete
    num_outputs: Incomplete
    decoder: Incomplete
    padding: Incomplete
    def __init__(self, config: PerceiverConfig, modalities: Dict[str, PerceiverAbstractDecoder], num_outputs: int, output_num_channels: int, min_padding_size: Optional[int] = 2, subsampled_index_dims: Optional[Dict[str, PerceiverAbstractDecoder]] = None, **decoder_kwargs) -> None: ...
    @property
    def num_query_channels(self) -> int: ...
    def decoder_query(self, inputs, modality_sizes, inputs_without_pos: Incomplete | None = None, subsampled_points: Incomplete | None = None): ...
    def forward(self, query: torch.Tensor, z: torch.FloatTensor, query_mask: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = False) -> torch.Tensor: ...

def space_to_depth(frames: torch.Tensor, temporal_block_size: int = 1, spatial_block_size: int = 1) -> torch.Tensor:
    """
    Space to depth transform. Rearranges blocks of spatial data, into depth.

    This function assumes the channels to be first, but will place the channels last after transformation.

    Based on https://discuss.pytorch.org/t/is-there-any-layer-like-tensorflows-space-to-depth-function/3487/15.
    """

class Conv2dSamePadding(nn.Conv2d):
    '''
    Conv2d layer with padding="same" support. Source:
    https://gist.github.com/sumanmichael/4de9dee93f972d47c80c4ade8e149ea6
    '''
    zero_pad_2d: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def forward(self, input): ...

class Conv2DDownsample(nn.Module):
    """Downsamples 4x by applying a 2D convolution and doing max pooling."""
    conv: Incomplete
    batchnorm: Incomplete
    relu: Incomplete
    max_pool: Incomplete
    def __init__(self, num_layers: int = 1, in_channels: int = 3, out_channels: int = 64, use_batchnorm: bool = True) -> None:
        """
        Constructs a Conv2DDownsample model.

        Args:
          in_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
          out_channels (`int`, *optional*, defaults to 64):
            The number of conv output channels.
          use_batchnorm (`bool`, *optional*, defaults to `True`):
            Whether to use batchnorm.
        """
    def forward(self, inputs: torch.Tensor) -> torch.Tensor: ...

def generate_fourier_features(pos, num_bands, max_resolution=(224, 224), concat_pos: bool = True, sine_only: bool = False):
    """
    Generate a Fourier frequency position encoding with linear spacing.

    Args:
      pos (`torch.LongTensor` of shape `(batch_size, sequence_length, dim)`):
        The Tensor containing the position of n points in d dimensional space.
      num_bands (`int`):
        The number of frequency bands (K) to use.
      max_resolution (`Tuple[int]`, *optional*, defaults to (224, 224)):
        The maximum resolution (i.e. the number of pixels per dim). A tuple representing resolution for each dimension.
      concat_pos (`bool`, *optional*, defaults to `True`):
        Whether to concatenate the input position encoding to the Fourier features.
      sine_only (`bool`, *optional*, defaults to `False`):
        Whether to use a single phase (sin) or two (sin/cos) for each frequency band.

    Returns:
      `torch.FloatTensor` of shape `(batch_size, sequence_length, n_channels)`: The Fourier position embeddings. If
      `concat_pos` is `True` and `sine_only` is `False`, output dimensions are ordered as: [dim_1, dim_2, ..., dim_d,
      sin(pi*f_1*dim_1), ..., sin(pi*f_K*dim_1), ..., sin(pi*f_1*dim_d), ..., sin(pi*f_K*dim_d), cos(pi*f_1*dim_1),
      ..., cos(pi*f_K*dim_1), ..., cos(pi*f_1*dim_d), ..., cos(pi*f_K*dim_d)], where dim_i is pos[:, i] and f_k is the
      kth frequency band.
    """
def build_linear_positions(index_dims, output_range=(-1.0, 1.0)):
    """
    Generate an array of position indices for an N-D input array.

    Args:
      index_dims (`List[int]`):
        The shape of the index dimensions of the input array.
      output_range (`Tuple[float]`, *optional*, defaults to `(-1.0, 1.0)`):
        The min and max values taken by each input index dimension.

    Returns:
      `torch.FloatTensor` of shape `(index_dims[0], index_dims[1], .., index_dims[-1], N)`.
    """

class PerceiverAbstractPositionEncoding(nn.Module, metaclass=abc.ABCMeta):
    """Perceiver abstract position encoding."""
    @property
    @abc.abstractmethod
    def num_dimensions(self) -> int: ...
    @abc.abstractmethod
    def output_size(self, *args, **kwargs) -> int: ...
    @abc.abstractmethod
    def forward(self, batch_size, pos): ...

class PerceiverTrainablePositionEncoding(PerceiverAbstractPositionEncoding):
    """Trainable position encoding."""
    position_embeddings: Incomplete
    def __init__(self, index_dims, num_channels: int = 128) -> None: ...
    @property
    def num_dimensions(self) -> int: ...
    def output_size(self, *args, **kwargs) -> int: ...
    def forward(self, batch_size: int) -> torch.Tensor: ...

class PerceiverFourierPositionEncoding(PerceiverAbstractPositionEncoding):
    """Fourier (Sinusoidal) position encoding."""
    num_bands: Incomplete
    max_resolution: Incomplete
    concat_pos: Incomplete
    sine_only: Incomplete
    def __init__(self, num_bands, max_resolution, concat_pos: bool = True, sine_only: bool = False) -> None: ...
    @property
    def num_dimensions(self) -> int: ...
    def output_size(self):
        """Returns size of positional encodings last dimension."""
    def forward(self, index_dims: List[int], batch_size: int, device, pos: torch.FloatTensor = None) -> torch.FloatTensor: ...

class AbstractPreprocessor(nn.Module):
    @property
    def num_channels(self) -> int:
        """Returns size of preprocessor output."""

class PerceiverTextPreprocessor(AbstractPreprocessor):
    """
    Text preprocessing for Perceiver Encoder. Can be used to embed `inputs` and add positional encodings.

    The dimensionality of the embeddings is determined by the `d_model` attribute of the configuration.

    Args:
        config ([`PerceiverConfig`]):
            Model configuration.
    """
    config: Incomplete
    embeddings: Incomplete
    position_embeddings: Incomplete
    def __init__(self, config: PerceiverConfig) -> None: ...
    @property
    def num_channels(self) -> int: ...
    def forward(self, inputs: torch.LongTensor) -> torch.FloatTensor: ...

class PerceiverEmbeddingDecoder(nn.Module):
    """
    Module to decode embeddings (for masked language modeling).

    Args:
        config ([`PerceiverConfig`]):
            Model configuration.
    """
    config: Incomplete
    vocab_size: Incomplete
    bias: Incomplete
    def __init__(self, config: PerceiverConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, embedding_layer: torch.Tensor) -> torch.Tensor: ...

class PerceiverMultimodalPostprocessor(nn.Module):
    """
    Multimodal postprocessing for Perceiver. Can be used to combine modality-specific postprocessors into a single
    postprocessor.

    Args:
          modalities (`Dict[str, PostprocessorType]`):
            Dictionary mapping modality name to postprocessor class for that modality.
          input_is_dict (`bool`, *optional*, defaults to `False`):
            If True, input is assumed to be dictionary structured, and outputs keep the same dictionary shape. If
            False, input is a tensor which is sliced up during postprocessing by *modality_sizes*.
    """
    modalities: Incomplete
    input_is_dict: Incomplete
    def __init__(self, modalities: Mapping[str, PostprocessorType], input_is_dict: bool = False) -> None: ...
    def forward(self, inputs: torch.Tensor, pos: Optional[torch.Tensor] = None, modality_sizes: Incomplete | None = None) -> Mapping[str, torch.Tensor]: ...

class PerceiverClassificationPostprocessor(nn.Module):
    """
    Classification postprocessing for Perceiver. Can be used to convert the decoder output to classification logits.

    Args:
        config ([*PerceiverConfig*]):
            Model configuration.
        in_channels (`int`):
            Number of channels in the input.
    """
    classifier: Incomplete
    def __init__(self, config: PerceiverConfig, in_channels: int) -> None: ...
    def forward(self, inputs, pos: Optional[torch.Tensor] = None, modality_sizes: Incomplete | None = None) -> torch.Tensor: ...

class PerceiverAudioPostprocessor(nn.Module):
    '''
    Audio postprocessing for Perceiver. Can be used to convert the decoder output to audio features.

    Args:
        config ([*PerceiverConfig*]):
            Model configuration.
        in_channels (`int`):
            Number of channels in the input.
        postproc_type (`str`, *optional*, defaults to `"patches"`):
            Postprocessor type to use. Currently, only "patches" is supported.
    '''
    classifier: Incomplete
    def __init__(self, config: PerceiverConfig, in_channels: int, postproc_type: str = 'patches') -> None: ...
    def forward(self, inputs: torch.Tensor, pos: Optional[torch.Tensor] = None, modality_sizes: Incomplete | None = None) -> torch.Tensor: ...

class PerceiverProjectionPostprocessor(nn.Module):
    """
    Projection postprocessing for Perceiver. Can be used to project the channels of the decoder output to a lower
    dimension.

    Args:
        in_channels (`int`):
            Number of channels in the input.
        out_channels (`int`):
            Number of channels in the output.
    """
    classifier: Incomplete
    def __init__(self, in_channels: int, out_channels: int) -> None: ...
    def forward(self, inputs: torch.Tensor, pos: Optional[torch.Tensor] = None, modality_sizes: Incomplete | None = None) -> torch.Tensor: ...

class PerceiverImagePreprocessor(AbstractPreprocessor):
    '''
    Image preprocessing for Perceiver Encoder.

    Note: the *out_channels* argument refers to the output channels of a convolutional layer, if *prep_type* is set to
    "conv1x1" or "conv". If one adds absolute position embeddings, one must make sure the *num_channels* of the
    position encoding kwargs are set equal to the *out_channels*.

    Args:
        config ([*PerceiverConfig*]):
            Model configuration.
        prep_type (`str`, *optional*, defaults to `"conv"`):
            Preprocessing type. Can be "conv1x1", "conv", "patches", "pixels".
        spatial_downsample (`int`, *optional*, defaults to 4):
            Spatial downsampling factor.
        temporal_downsample (`int`, *optional*, defaults to 1):
            Temporal downsampling factor (only relevant in case a time dimension is present).
        position_encoding_type (`str`, *optional*, defaults to `"fourier"`):
            Position encoding type. Can be "fourier" or "trainable".
        in_channels (`int`, *optional*, defaults to 3):
            Number of channels in the input.
        out_channels (`int`, *optional*, defaults to 64):
            Number of channels in the output.
        conv_after_patching (`bool`, *optional*, defaults to `False`):
            Whether to apply a convolutional layer after patching.
        conv_after_patching_in_channels (`int`, *optional*, defaults to 54):
            Number of channels in the input of the convolutional layer after patching.
        conv2d_use_batchnorm (`bool`, *optional*, defaults to `True`):
            Whether to use batch normalization in the convolutional layer.
        concat_or_add_pos (`str`, *optional*, defaults to `"concat"`):
            How to concatenate the position encoding to the input. Can be "concat" or "add".
        project_pos_dim (`int`, *optional*, defaults to -1):
            Dimension of the position encoding to project to. If -1, no projection is applied.
        **position_encoding_kwargs (`Dict`, *optional*):
            Keyword arguments for the position encoding.
    '''
    config: Incomplete
    in_channels: Incomplete
    prep_type: Incomplete
    spatial_downsample: Incomplete
    temporal_downsample: Incomplete
    position_encoding_type: Incomplete
    concat_or_add_pos: Incomplete
    conv_after_patching: Incomplete
    out_channels: Incomplete
    convnet: Incomplete
    convnet_1x1: Incomplete
    project_pos_dim: Incomplete
    conv_after_patches: Incomplete
    def __init__(self, config, prep_type: str = 'conv', spatial_downsample: int = 4, temporal_downsample: int = 1, position_encoding_type: str = 'fourier', in_channels: int = 3, out_channels: int = 64, conv_after_patching: bool = False, conv_after_patching_in_channels: int = 54, conv2d_use_batchnorm: bool = True, concat_or_add_pos: str = 'concat', project_pos_dim: int = -1, **position_encoding_kwargs) -> None: ...
    @property
    def num_channels(self) -> int: ...
    def forward(self, inputs: torch.Tensor, pos: Optional[torch.Tensor] = None, network_input_is_1d: bool = True): ...

class PerceiverOneHotPreprocessor(AbstractPreprocessor):
    """
    One-hot preprocessor for Perceiver Encoder. Can be used to add a dummy index dimension to the input.

    Args:
        config ([`PerceiverConfig`]):
            Model configuration.
    """
    config: Incomplete
    def __init__(self, config: PerceiverConfig) -> None: ...
    @property
    def num_channels(self) -> int: ...
    def forward(self, inputs: torch.Tensor, pos: Optional[torch.Tensor] = None, network_input_is_1d: bool = True): ...

class PerceiverAudioPreprocessor(AbstractPreprocessor):
    '''
    Audio preprocessing for Perceiver Encoder.

    Args:
        config ([*PerceiverConfig*]):
            Model configuration.
        prep_type (`str`, *optional*, defaults to `"patches"`):
            Preprocessor type to use. Only "patches" is supported.
        samples_per_patch (`int`, *optional*, defaults to 96):
            Number of samples per patch.
        position_encoding_type (`str`, *optional*, defaults to `"fourier"`):
            Type of position encoding to use. Can be "trainable" or "fourier".
        concat_or_add_pos (`str`, *optional*, defaults to `"concat"`):
            How to concatenate the position encoding to the input. Can be "concat" or "add".
        out_channels (`int`, *optional*, defaults to 64):
            Number of channels in the output.
        project_pos_dim (`int`, *optional*, defaults to -1):
            Dimension of the position encoding to project to. If -1, no projection is applied.
        **position_encoding_kwargs (`Dict`, *optional*):
            Keyword arguments for the position encoding.
    '''
    config: Incomplete
    samples_per_patch: Incomplete
    position_encoding_type: Incomplete
    concat_or_add_pos: Incomplete
    project_pos_dim: Incomplete
    def __init__(self, config, prep_type: str = 'patches', samples_per_patch: int = 96, position_encoding_type: str = 'fourier', concat_or_add_pos: str = 'concat', out_channels: int = 64, project_pos_dim: int = -1, **position_encoding_kwargs) -> None: ...
    @property
    def num_channels(self) -> int: ...
    def forward(self, inputs: torch.Tensor, pos: Optional[torch.Tensor] = None, network_input_is_1d: bool = True): ...

class PerceiverMultimodalPreprocessor(AbstractPreprocessor):
    """
    Multimodal preprocessing for Perceiver Encoder.

    Inputs for each modality are preprocessed, then padded with trainable position embeddings to have the same number
    of channels.

    Args:
        modalities (`Dict[str, PreprocessorType]`):
            Dict mapping modality name to preprocessor.
        mask_probs (`Dict[str, float]`):
            Dict mapping modality name to masking probability of that modality.
        min_padding_size (`int`, *optional*, defaults to 2):
            The minimum padding size for all modalities. The final output will have num_channels equal to the maximum
            channels across all modalities plus min_padding_size.
    """
    modalities: Incomplete
    min_padding_size: Incomplete
    mask_probs: Incomplete
    padding: Incomplete
    mask: Incomplete
    def __init__(self, modalities: Mapping[str, PreprocessorType], mask_probs: Optional[Mapping[str, float]] = None, min_padding_size: int = 2) -> None: ...
    @property
    def num_channels(self) -> int: ...
    def forward(self, inputs: Mapping[str, torch.Tensor], pos: Optional[torch.Tensor] = None, network_input_is_1d: bool = True) -> PreprocessorOutputType: ...
