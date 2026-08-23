import torch
from ...file_utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward
from ...modeling_outputs import ImageClassifierOutputWithNoAttention as ImageClassifierOutputWithNoAttention, ModelOutput as ModelOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import logging as logging
from .configuration_cvt import CvtConfig as CvtConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
CVT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class BaseModelOutputWithCLSToken(ModelOutput):
    """
    Base class for model's outputs, with potential hidden states and attentions.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        cls_token_value (`torch.FloatTensor` of shape `(batch_size, 1, hidden_size)`):
            Classification token at the output of the last layer of the model.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`. Hidden-states of the model at the output of each layer
            plus the initial embedding outputs.
    """
    last_hidden_state: torch.FloatTensor = ...
    cls_token_value: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, last_hidden_state, cls_token_value, hidden_states) -> None: ...

def drop_path(input, drop_prob: float = 0.0, training: bool = False):
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).

    Comment by Ross Wightman: This is the same as the DropConnect impl I created for EfficientNet, etc networks,
    however, the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for changing the
    layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use 'survival rate' as the
    argument.
    """

class CvtDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    drop_prob: Incomplete
    def __init__(self, drop_prob: Optional[float] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def extra_repr(self) -> str: ...

class CvtEmbeddings(nn.Module):
    """
    Construct the CvT embeddings.
    """
    convolution_embeddings: Incomplete
    dropout: Incomplete
    def __init__(self, patch_size, num_channels, embed_dim, stride, padding, dropout_rate) -> None: ...
    def forward(self, pixel_values): ...

class CvtConvEmbeddings(nn.Module):
    """
    Image to Conv Embedding.
    """
    patch_size: Incomplete
    projection: Incomplete
    normalization: Incomplete
    def __init__(self, patch_size, num_channels, embed_dim, stride, padding) -> None: ...
    def forward(self, pixel_values): ...

class CvtSelfAttentionConvProjection(nn.Module):
    convolution: Incomplete
    normalization: Incomplete
    def __init__(self, embed_dim, kernel_size, padding, stride) -> None: ...
    def forward(self, hidden_state): ...

class CvtSelfAttentionLinearProjection(nn.Module):
    def forward(self, hidden_state): ...

class CvtSelfAttentionProjection(nn.Module):
    convolution_projection: Incomplete
    linear_projection: Incomplete
    def __init__(self, embed_dim, kernel_size, padding, stride, projection_method: str = 'dw_bn') -> None: ...
    def forward(self, hidden_state): ...

class CvtSelfAttention(nn.Module):
    scale: Incomplete
    with_cls_token: Incomplete
    embed_dim: Incomplete
    num_heads: Incomplete
    convolution_projection_query: Incomplete
    convolution_projection_key: Incomplete
    convolution_projection_value: Incomplete
    projection_query: Incomplete
    projection_key: Incomplete
    projection_value: Incomplete
    dropout: Incomplete
    def __init__(self, num_heads, embed_dim, kernel_size, padding_q, padding_kv, stride_q, stride_kv, qkv_projection_method, qkv_bias, attention_drop_rate, with_cls_token: bool = True, **kwargs) -> None: ...
    def rearrange_for_multi_head_attention(self, hidden_state): ...
    def forward(self, hidden_state, height, width): ...

class CvtSelfOutput(nn.Module):
    """
    The residual connection is defined in CvtLayer instead of here (as is the case with other models), due to the
    layernorm applied before each block.
    """
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, embed_dim, drop_rate) -> None: ...
    def forward(self, hidden_state, input_tensor): ...

class CvtAttention(nn.Module):
    attention: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, num_heads, embed_dim, kernel_size, padding_q, padding_kv, stride_q, stride_kv, qkv_projection_method, qkv_bias, attention_drop_rate, drop_rate, with_cls_token: bool = True) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_state, height, width): ...

class CvtIntermediate(nn.Module):
    dense: Incomplete
    activation: Incomplete
    def __init__(self, embed_dim, mlp_ratio) -> None: ...
    def forward(self, hidden_state): ...

class CvtOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, embed_dim, mlp_ratio, drop_rate) -> None: ...
    def forward(self, hidden_state, input_tensor): ...

class CvtLayer(nn.Module):
    """
    CvtLayer composed by attention layers, normalization and multi-layer perceptrons (mlps).
    """
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    drop_path: Incomplete
    layernorm_before: Incomplete
    layernorm_after: Incomplete
    def __init__(self, num_heads, embed_dim, kernel_size, padding_q, padding_kv, stride_q, stride_kv, qkv_projection_method, qkv_bias, attention_drop_rate, drop_rate, mlp_ratio, drop_path_rate, with_cls_token: bool = True) -> None: ...
    def forward(self, hidden_state, height, width): ...

class CvtStage(nn.Module):
    config: Incomplete
    stage: Incomplete
    cls_token: Incomplete
    embedding: Incomplete
    layers: Incomplete
    def __init__(self, config, stage) -> None: ...
    def forward(self, hidden_state): ...

class CvtEncoder(nn.Module):
    config: Incomplete
    stages: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values, output_hidden_states: bool = False, return_dict: bool = True): ...

class CvtPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = CvtConfig
    base_model_prefix: str
    main_input_name: str

CVT_START_DOCSTRING: str
CVT_INPUTS_DOCSTRING: str

class CvtModel(CvtPreTrainedModel):
    config: Incomplete
    encoder: Incomplete
    def __init__(self, config, add_pooling_layer: bool = True) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithCLSToken]: ...

class CvtForImageClassification(CvtPreTrainedModel):
    num_labels: Incomplete
    cvt: Incomplete
    layernorm: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, ImageClassifierOutputWithNoAttention]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
