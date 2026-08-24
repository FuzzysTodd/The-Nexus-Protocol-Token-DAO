import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling, ImageClassifierOutput as ImageClassifierOutput, MaskedLMOutput as MaskedLMOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_deit import DeiTConfig as DeiTConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Optional, Set, Tuple, Union

logger: Incomplete
DEIT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class DeiTEmbeddings(nn.Module):
    """
    Construct the CLS token, distillation token, position and patch embeddings. Optionally, also the mask token.
    """
    cls_token: Incomplete
    distillation_token: Incomplete
    mask_token: Incomplete
    patch_embeddings: Incomplete
    position_embeddings: Incomplete
    dropout: Incomplete
    def __init__(self, config: DeiTConfig, use_mask_token: bool = False) -> None: ...
    def forward(self, pixel_values: torch.Tensor, bool_masked_pos: Optional[torch.BoolTensor] = None) -> torch.Tensor: ...

class DeiTPatchEmbeddings(nn.Module):
    """
    This class turns `pixel_values` of shape `(batch_size, num_channels, height, width)` into the initial
    `hidden_states` (patch embeddings) of shape `(batch_size, seq_length, hidden_size)` to be consumed by a
    Transformer.
    """
    image_size: Incomplete
    patch_size: Incomplete
    num_channels: Incomplete
    num_patches: Incomplete
    projection: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.Tensor) -> torch.Tensor: ...

class DeiTSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config: DeiTConfig) -> None: ...
    def transpose_for_scores(self, x: torch.Tensor) -> torch.Tensor: ...
    def forward(self, hidden_states, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Union[Tuple[torch.Tensor, torch.Tensor], Tuple[torch.Tensor]]: ...

class DeiTSelfOutput(nn.Module):
    """
    The residual connection is defined in DeiTLayer instead of here (as is the case with other models), due to the
    layernorm applied before each block.
    """
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: DeiTConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class DeiTAttention(nn.Module):
    attention: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config: DeiTConfig) -> None: ...
    def prune_heads(self, heads: Set[int]) -> None: ...
    def forward(self, hidden_states: torch.Tensor, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Union[Tuple[torch.Tensor, torch.Tensor], Tuple[torch.Tensor]]: ...

class DeiTIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: DeiTConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class DeiTOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: DeiTConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class DeiTLayer(nn.Module):
    """This corresponds to the Block class in the timm implementation."""
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    layernorm_before: Incomplete
    layernorm_after: Incomplete
    def __init__(self, config: DeiTConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Union[Tuple[torch.Tensor, torch.Tensor], Tuple[torch.Tensor]]: ...

class DeiTEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: DeiTConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True) -> Union[tuple, BaseModelOutput]: ...

class DeiTPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DeiTConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

DEIT_START_DOCSTRING: str
DEIT_INPUTS_DOCSTRING: str

class DeiTModel(DeiTPreTrainedModel):
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    pooler: Incomplete
    def __init__(self, config: DeiTConfig, add_pooling_layer: bool = True, use_mask_token: bool = False) -> None: ...
    def get_input_embeddings(self) -> DeiTPatchEmbeddings: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, bool_masked_pos: Optional[torch.BoolTensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPooling]: ...

class DeiTPooler(nn.Module):
    dense: Incomplete
    activation: Incomplete
    def __init__(self, config: DeiTConfig) -> None: ...
    def forward(self, hidden_states): ...

class DeiTForMaskedImageModeling(DeiTPreTrainedModel):
    deit: Incomplete
    decoder: Incomplete
    def __init__(self, config: DeiTConfig) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, bool_masked_pos: Optional[torch.BoolTensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, MaskedLMOutput]:
        '''
        bool_masked_pos (`torch.BoolTensor` of shape `(batch_size, num_patches)`):
            Boolean masked positions. Indicates which patches are masked (1) and which aren\'t (0).

        Returns:

        Examples:
        ```python
        >>> from transformers import AutoImageProcessor, DeiTForMaskedImageModeling
        >>> import torch
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("facebook/deit-base-distilled-patch16-224")
        >>> model = DeiTForMaskedImageModeling.from_pretrained("facebook/deit-base-distilled-patch16-224")

        >>> num_patches = (model.config.image_size // model.config.patch_size) ** 2
        >>> pixel_values = image_processor(images=image, return_tensors="pt").pixel_values
        >>> # create random boolean mask of shape (batch_size, num_patches)
        >>> bool_masked_pos = torch.randint(low=0, high=2, size=(1, num_patches)).bool()

        >>> outputs = model(pixel_values, bool_masked_pos=bool_masked_pos)
        >>> loss, reconstructed_pixel_values = outputs.loss, outputs.logits
        >>> list(reconstructed_pixel_values.shape)
        [1, 3, 224, 224]
        ```'''

class DeiTForImageClassification(DeiTPreTrainedModel):
    num_labels: Incomplete
    deit: Incomplete
    classifier: Incomplete
    def __init__(self, config: DeiTConfig) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, ImageClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, DeiTForImageClassification
        >>> import torch
        >>> from PIL import Image
        >>> import requests

        >>> torch.manual_seed(3)  # doctest: +IGNORE_RESULT
        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> # note: we are loading a DeiTForImageClassificationWithTeacher from the hub here,
        >>> # so the head will be randomly initialized, hence the predictions will be random
        >>> image_processor = AutoImageProcessor.from_pretrained("facebook/deit-base-distilled-patch16-224")
        >>> model = DeiTForImageClassification.from_pretrained("facebook/deit-base-distilled-patch16-224")

        >>> inputs = image_processor(images=image, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> logits = outputs.logits
        >>> # model predicts one of the 1000 ImageNet classes
        >>> predicted_class_idx = logits.argmax(-1).item()
        >>> print("Predicted class:", model.config.id2label[predicted_class_idx])
        Predicted class: magpie
        ```'''

@dataclass
class DeiTForImageClassificationWithTeacherOutput(ModelOutput):
    """
    Output type of [`DeiTForImageClassificationWithTeacher`].

    Args:
        logits (`torch.FloatTensor` of shape `(batch_size, config.num_labels)`):
            Prediction scores as the average of the cls_logits and distillation logits.
        cls_logits (`torch.FloatTensor` of shape `(batch_size, config.num_labels)`):
            Prediction scores of the classification head (i.e. the linear layer on top of the final hidden state of the
            class token).
        distillation_logits (`torch.FloatTensor` of shape `(batch_size, config.num_labels)`):
            Prediction scores of the distillation head (i.e. the linear layer on top of the final hidden state of the
            distillation token).
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`. Attentions weights after the attention softmax, used to compute the weighted average in
            the self-attention heads.
    """
    logits: torch.FloatTensor = ...
    cls_logits: torch.FloatTensor = ...
    distillation_logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, logits, cls_logits, distillation_logits, hidden_states, attentions) -> None: ...

class DeiTForImageClassificationWithTeacher(DeiTPreTrainedModel):
    num_labels: Incomplete
    deit: Incomplete
    cls_classifier: Incomplete
    distillation_classifier: Incomplete
    def __init__(self, config: DeiTConfig) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, DeiTForImageClassificationWithTeacherOutput]: ...
