import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BackboneOutput as BackboneOutput
from ...modeling_utils import BackboneMixin as BackboneMixin, PreTrainedModel as PreTrainedModel
from ...pytorch_utils import find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import ModelOutput as ModelOutput, OptionalDependencyNotAvailable as OptionalDependencyNotAvailable, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, is_natten_available as is_natten_available, logging as logging, replace_return_docstrings as replace_return_docstrings, requires_backends as requires_backends
from .configuration_nat import NatConfig as NatConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
NAT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class NatEncoderOutput(ModelOutput):
    """
    Nat encoder's outputs, with potential hidden states and attentions.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        reshaped_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, hidden_size, height, width)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
            include the spatial dimensions.
    """
    last_hidden_state: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    reshaped_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, last_hidden_state, hidden_states, attentions, reshaped_hidden_states) -> None: ...

@dataclass
class NatModelOutput(ModelOutput):
    """
    Nat model's outputs that also contains a pooling of the last hidden states.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        pooler_output (`torch.FloatTensor` of shape `(batch_size, hidden_size)`, *optional*, returned when `add_pooling_layer=True` is passed):
            Average pooling of the last layer hidden-state.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        reshaped_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, hidden_size, height, width)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
            include the spatial dimensions.
    """
    last_hidden_state: torch.FloatTensor = ...
    pooler_output: Optional[torch.FloatTensor] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    reshaped_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, last_hidden_state, pooler_output, hidden_states, attentions, reshaped_hidden_states) -> None: ...

@dataclass
class NatImageClassifierOutput(ModelOutput):
    """
    Nat outputs for image classification.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Classification (or regression if config.num_labels==1) loss.
        logits (`torch.FloatTensor` of shape `(batch_size, config.num_labels)`):
            Classification (or regression if config.num_labels==1) scores (before SoftMax).
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each stage) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        reshaped_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each stage) of
            shape `(batch_size, hidden_size, height, width)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs reshaped to
            include the spatial dimensions.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    reshaped_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, hidden_states, attentions, reshaped_hidden_states) -> None: ...

class NatEmbeddings(nn.Module):
    """
    Construct the patch and position embeddings.
    """
    patch_embeddings: Incomplete
    norm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor]) -> Tuple[torch.Tensor]: ...

class NatPatchEmbeddings(nn.Module):
    """
    This class turns `pixel_values` of shape `(batch_size, num_channels, height, width)` into the initial
    `hidden_states` (patch embeddings) of shape `(batch_size, height, width, hidden_size)` to be consumed by a
    Transformer.
    """
    num_channels: Incomplete
    projection: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor]) -> torch.Tensor: ...

class NatDownsampler(nn.Module):
    """
    Convolutional Downsampling Layer.

    Args:
        dim (`int`):
            Number of input channels.
        norm_layer (`nn.Module`, *optional*, defaults to `nn.LayerNorm`):
            Normalization layer class.
    """
    dim: Incomplete
    reduction: Incomplete
    norm: Incomplete
    def __init__(self, dim: int, norm_layer: nn.Module = ...) -> None: ...
    def forward(self, input_feature: torch.Tensor) -> torch.Tensor: ...

def drop_path(input, drop_prob: float = 0.0, training: bool = False, scale_by_keep: bool = True):
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).

    Comment by Ross Wightman: This is the same as the DropConnect impl I created for EfficientNet, etc networks,
    however, the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for changing the
    layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use 'survival rate' as the
    argument.
    """

class NatDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    drop_prob: Incomplete
    def __init__(self, drop_prob: Optional[float] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def extra_repr(self) -> str: ...

class NeighborhoodAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    kernel_size: Incomplete
    rpb: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config, dim, num_heads, kernel_size) -> None: ...
    def transpose_for_scores(self, x): ...
    def forward(self, hidden_states: torch.Tensor, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class NeighborhoodAttentionOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config, dim) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class NeighborhoodAttentionModule(nn.Module):
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config, dim, num_heads, kernel_size) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states: torch.Tensor, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class NatIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config, dim) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class NatOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config, dim) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class NatLayer(nn.Module):
    chunk_size_feed_forward: Incomplete
    kernel_size: Incomplete
    layernorm_before: Incomplete
    attention: Incomplete
    drop_path: Incomplete
    layernorm_after: Incomplete
    intermediate: Incomplete
    output: Incomplete
    layer_scale_parameters: Incomplete
    def __init__(self, config, dim, num_heads, drop_path_rate: float = 0.0) -> None: ...
    def maybe_pad(self, hidden_states, height, width): ...
    def forward(self, hidden_states: torch.Tensor, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor, torch.Tensor]: ...

class NatStage(nn.Module):
    config: Incomplete
    dim: Incomplete
    layers: Incomplete
    downsample: Incomplete
    pointing: bool
    def __init__(self, config, dim, depth, num_heads, drop_path_rate, downsample) -> None: ...
    def forward(self, hidden_states: torch.Tensor, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class NatEncoder(nn.Module):
    num_levels: Incomplete
    config: Incomplete
    levels: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, output_attentions: Optional[bool] = False, output_hidden_states: Optional[bool] = False, output_hidden_states_before_downsampling: Optional[bool] = False, return_dict: Optional[bool] = True) -> Union[Tuple, NatEncoderOutput]: ...

class NatPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = NatConfig
    base_model_prefix: str
    main_input_name: str

NAT_START_DOCSTRING: str
NAT_INPUTS_DOCSTRING: str

class NatModel(NatPreTrainedModel):
    config: Incomplete
    num_levels: Incomplete
    num_features: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    pooler: Incomplete
    def __init__(self, config, add_pooling_layer: bool = True) -> None: ...
    def get_input_embeddings(self): ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, NatModelOutput]: ...

class NatForImageClassification(NatPreTrainedModel):
    num_labels: Incomplete
    nat: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, NatImageClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class NatBackbone(NatPreTrainedModel, BackboneMixin):
    stage_names: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    out_features: Incomplete
    out_feature_channels: Incomplete
    hidden_states_norms: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    @property
    def channels(self): ...
    def forward(self, pixel_values: torch.Tensor, output_hidden_states: Optional[bool] = None, output_attentions: Optional[bool] = None, return_dict: Optional[bool] = None) -> BackboneOutput:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, AutoBackbone
        >>> import torch
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> processor = AutoImageProcessor.from_pretrained("shi-labs/nat-mini-in1k-224")
        >>> model = AutoBackbone.from_pretrained(
        ...     "shi-labs/nat-mini-in1k-224", out_features=["stage1", "stage2", "stage3", "stage4"]
        ... )

        >>> inputs = processor(image, return_tensors="pt")

        >>> outputs = model(**inputs)

        >>> feature_maps = outputs.feature_maps
        >>> list(feature_maps[-1].shape)
        [1, 512, 7, 7]
        ```'''
