import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling, MaskedLMOutput as MaskedLMOutput, ModelOutput as ModelOutput, SequenceClassifierOutput as SequenceClassifierOutput, TokenClassifierOutput as TokenClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, is_torch_greater_or_equal_than_1_10 as is_torch_greater_or_equal_than_1_10, meshgrid as meshgrid, prune_linear_layer as prune_linear_layer
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_vilt import ViltConfig as ViltConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import List, Optional, Tuple, Union

logger: Incomplete
VILT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class ViltForImagesAndTextClassificationOutput(ModelOutput):
    """
    Class for outputs of [`ViltForImagesAndTextClassification`].

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Classification (or regression if config.num_labels==1) loss.
        logits (`torch.FloatTensor` of shape `(batch_size, config.num_labels)`):
            Classification (or regression if config.num_labels==1) scores (before SoftMax).
        hidden_states (`List[tuple(torch.FloatTensor)]`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            List of tuples of `torch.FloatTensor` (one for each image-text pair, each tuple containing the output of
            the embeddings + one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.
            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`List[tuple(torch.FloatTensor)]`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            List of tuples of `torch.FloatTensor` (one for each image-text pair, each tuple containing the attention
            weights of shape `(batch_size, num_heads, sequence_length, sequence_length)`. Attentions weights after the
            attention softmax, used to compute the weighted average in the self-attention heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    hidden_states: Optional[List[Tuple[torch.FloatTensor]]] = ...
    attentions: Optional[List[Tuple[torch.FloatTensor]]] = ...
    def __init__(self, loss, logits, hidden_states, attentions) -> None: ...

class ViltEmbeddings(nn.Module):
    """
    Construct the text and patch embeddings.

    Text embeddings are equivalent to BERT embeddings.

    Patch embeddings are equivalent to ViT embeddings.
    """
    text_embeddings: Incomplete
    cls_token: Incomplete
    patch_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    dropout: Incomplete
    config: Incomplete
    def __init__(self, config) -> None: ...
    def visual_embed(self, pixel_values, pixel_mask, max_image_length: int = 200): ...
    def forward(self, input_ids, attention_mask, token_type_ids, pixel_values, pixel_mask, inputs_embeds, image_embeds, image_token_type_idx: int = 1): ...

class TextEmbeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None): ...

class ViltPatchEmbeddings(nn.Module):
    """
    Image to Patch Embedding.
    """
    image_size: Incomplete
    patch_size: Incomplete
    num_channels: Incomplete
    num_patches: Incomplete
    projection: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values): ...

class ViltSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def transpose_for_scores(self, x): ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class ViltSelfOutput(nn.Module):
    """
    The residual connection is defined in ViltLayer instead of here (as is the case with other models), due to the
    layernorm applied before each block.
    """
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: ViltConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class ViltAttention(nn.Module):
    attention: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class ViltIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: ViltConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class ViltOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: ViltConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class ViltLayer(nn.Module):
    """This corresponds to the Block class in the timm implementation."""
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    layernorm_before: Incomplete
    layernorm_after: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class ViltEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class ViltPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ViltConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool

VILT_START_DOCSTRING: str
VILT_INPUTS_DOCSTRING: str
VILT_IMAGES_AND_TEXT_CLASSIFICATION_INPUTS_DOCSTRING: str

class ViltModel(ViltPreTrainedModel):
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    pooler: Incomplete
    def __init__(self, config, add_pooling_layer: bool = True) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, pixel_values: Optional[torch.FloatTensor] = None, pixel_mask: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, image_embeds: Optional[torch.FloatTensor] = None, image_token_type_idx: Optional[int] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[BaseModelOutputWithPooling, Tuple[torch.FloatTensor]]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import ViltProcessor, ViltModel
        >>> from PIL import Image
        >>> import requests

        >>> # prepare image and text
        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)
        >>> text = "hello world"

        >>> processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-mlm")
        >>> model = ViltModel.from_pretrained("dandelin/vilt-b32-mlm")

        >>> inputs = processor(image, text, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> last_hidden_states = outputs.last_hidden_state
        ```'''

class ViltPooler(nn.Module):
    dense: Incomplete
    activation: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class ViltForMaskedLM(ViltPreTrainedModel):
    vilt: Incomplete
    mlm_score: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, pixel_values: Optional[torch.FloatTensor] = None, pixel_mask: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, image_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[MaskedLMOutput, Tuple[torch.FloatTensor]]:
        '''
        labels (*torch.LongTensor* of shape *(batch_size, sequence_length)*, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in *[-100, 0, ...,
            config.vocab_size]* (see *input_ids* docstring) Tokens with indices set to *-100* are ignored (masked), the
            loss is only computed for the tokens with labels in *[0, ..., config.vocab_size]*

        Returns:

        Examples:

        ```python
        >>> from transformers import ViltProcessor, ViltForMaskedLM
        >>> import requests
        >>> from PIL import Image
        >>> import re
        >>> import torch

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)
        >>> text = "a bunch of [MASK] laying on a [MASK]."

        >>> processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-mlm")
        >>> model = ViltForMaskedLM.from_pretrained("dandelin/vilt-b32-mlm")

        >>> # prepare inputs
        >>> encoding = processor(image, text, return_tensors="pt")

        >>> # forward pass
        >>> outputs = model(**encoding)

        >>> tl = len(re.findall("\\[MASK\\]", text))
        >>> inferred_token = [text]

        >>> # gradually fill in the MASK tokens, one by one
        >>> with torch.no_grad():
        ...     for i in range(tl):
        ...         encoded = processor.tokenizer(inferred_token)
        ...         input_ids = torch.tensor(encoded.input_ids)
        ...         encoded = encoded["input_ids"][0][1:-1]
        ...         outputs = model(input_ids=input_ids, pixel_values=encoding.pixel_values)
        ...         mlm_logits = outputs.logits[0]  # shape (seq_len, vocab_size)
        ...         # only take into account text features (minus CLS and SEP token)
        ...         mlm_logits = mlm_logits[1 : input_ids.shape[1] - 1, :]
        ...         mlm_values, mlm_ids = mlm_logits.softmax(dim=-1).max(dim=-1)
        ...         # only take into account text
        ...         mlm_values[torch.tensor(encoded) != 103] = 0
        ...         select = mlm_values.argmax().item()
        ...         encoded[select] = mlm_ids[select].item()
        ...         inferred_token = [processor.decode(encoded)]

        >>> selected_token = ""
        >>> encoded = processor.tokenizer(inferred_token)
        >>> output = processor.decode(encoded.input_ids[0], skip_special_tokens=True)
        >>> print(output)
        a bunch of cats laying on a couch.
        ```'''

class ViltPredictionHeadTransform(nn.Module):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class ViltMLMHead(nn.Module):
    config: Incomplete
    transform: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def __init__(self, config, weight: Incomplete | None = None) -> None: ...
    def forward(self, x): ...

class ViltForQuestionAnswering(ViltPreTrainedModel):
    num_labels: Incomplete
    vilt: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, pixel_values: Optional[torch.FloatTensor] = None, pixel_mask: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, image_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[SequenceClassifierOutput, Tuple[torch.FloatTensor]]:
        '''
        labels (`torch.FloatTensor` of shape `(batch_size, num_labels)`, *optional*):
            Labels for computing the visual question answering loss. This tensor must be either a one-hot encoding of
            all answers that are applicable for a given example in the batch, or a soft encoding indicating which
            answers are applicable, where 1.0 is the highest score.

        Returns:

        Examples:

        ```python
        >>> from transformers import ViltProcessor, ViltForQuestionAnswering
        >>> import requests
        >>> from PIL import Image

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)
        >>> text = "How many cats are there?"

        >>> processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
        >>> model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

        >>> # prepare inputs
        >>> encoding = processor(image, text, return_tensors="pt")

        >>> # forward pass
        >>> outputs = model(**encoding)
        >>> logits = outputs.logits
        >>> idx = logits.argmax(-1).item()
        >>> print("Predicted answer:", model.config.id2label[idx])
        Predicted answer: 2
        ```'''

class ViltForImageAndTextRetrieval(ViltPreTrainedModel):
    vilt: Incomplete
    rank_output: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, pixel_values: Optional[torch.FloatTensor] = None, pixel_mask: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, image_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[SequenceClassifierOutput, Tuple[torch.FloatTensor]]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels are currently not supported.

        Returns:

        Examples:

        ```python
        >>> from transformers import ViltProcessor, ViltForImageAndTextRetrieval
        >>> import requests
        >>> from PIL import Image

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)
        >>> texts = ["An image of two cats chilling on a couch", "A football player scoring a goal"]

        >>> processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-coco")
        >>> model = ViltForImageAndTextRetrieval.from_pretrained("dandelin/vilt-b32-finetuned-coco")

        >>> # forward pass
        >>> scores = dict()
        >>> for text in texts:
        ...     # prepare inputs
        ...     encoding = processor(image, text, return_tensors="pt")
        ...     outputs = model(**encoding)
        ...     scores[text] = outputs.logits[0, :].item()
        ```'''

class ViltForImagesAndTextClassification(ViltPreTrainedModel):
    num_labels: Incomplete
    vilt: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, pixel_values: Optional[torch.FloatTensor] = None, pixel_mask: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, image_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[ViltForImagesAndTextClassificationOutput, Tuple[torch.FloatTensor]]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Binary classification labels.

        Returns:

        Examples:

        ```python
        >>> from transformers import ViltProcessor, ViltForImagesAndTextClassification
        >>> import requests
        >>> from PIL import Image

        >>> image1 = Image.open(requests.get("https://lil.nlp.cornell.edu/nlvr/exs/ex0_0.jpg", stream=True).raw)
        >>> image2 = Image.open(requests.get("https://lil.nlp.cornell.edu/nlvr/exs/ex0_1.jpg", stream=True).raw)
        >>> text = "The left image contains twice the number of dogs as the right image."

        >>> processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-nlvr2")
        >>> model = ViltForImagesAndTextClassification.from_pretrained("dandelin/vilt-b32-finetuned-nlvr2")

        >>> # prepare inputs
        >>> encoding = processor([image1, image2], text, return_tensors="pt")

        >>> # forward pass
        >>> outputs = model(input_ids=encoding.input_ids, pixel_values=encoding.pixel_values.unsqueeze(0))
        >>> logits = outputs.logits
        >>> idx = logits.argmax(-1).item()
        >>> print("Predicted answer:", model.config.id2label[idx])
        Predicted answer: True
        ```'''

class ViltForTokenClassification(ViltPreTrainedModel):
    num_labels: Incomplete
    vilt: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, pixel_values: Optional[torch.FloatTensor] = None, pixel_mask: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, image_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[TokenClassifierOutput, Tuple[torch.FloatTensor]]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, text_sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.

        Returns:
        """
