import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling, ImageClassifierOutput as ImageClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_efficientformer import EfficientFormerConfig as EfficientFormerConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
EFFICIENTFORMER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class EfficientFormerPatchEmbeddings(nn.Module):
    """
    This class performs downsampling between two stages. For the input tensor with the shape [batch_size, num_channels,
    height, width] it produces output tensor with the shape [batch_size, num_channels, height/stride, width/stride]
    """
    num_channels: Incomplete
    projection: Incomplete
    norm: Incomplete
    def __init__(self, config: EfficientFormerConfig, num_channels: int, embed_dim: int, apply_norm: bool = True) -> None: ...
    def forward(self, pixel_values: torch.Tensor) -> torch.Tensor: ...

class EfficientFormerSelfAttention(nn.Module):
    num_heads: Incomplete
    key_dim: Incomplete
    attention_ratio: Incomplete
    scale: Incomplete
    total_key_dim: Incomplete
    expanded_key_dim: Incomplete
    total_expanded_key_dim: Incomplete
    qkv: Incomplete
    projection: Incomplete
    attention_biases: Incomplete
    def __init__(self, dim: int, key_dim: int, num_heads: int, attention_ratio: int, resolution: int) -> None: ...
    ab: Incomplete
    def train(self, mode: bool = True) -> None: ...
    def forward(self, hidden_states: torch.Tensor, output_attentions: bool = False) -> Tuple[torch.Tensor]: ...

class EfficientFormerConvStem(nn.Module):
    convolution1: Incomplete
    batchnorm_before: Incomplete
    convolution2: Incomplete
    batchnorm_after: Incomplete
    activation: Incomplete
    def __init__(self, config: EfficientFormerConfig, out_channels: int) -> None: ...
    def forward(self, pixel_values: torch.Tensor) -> torch.Tensor: ...

class EfficientFormerPooling(nn.Module):
    pool: Incomplete
    def __init__(self, pool_size: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class EfficientFormerDenseMlp(nn.Module):
    linear_in: Incomplete
    activation: Incomplete
    dropout: Incomplete
    linear_out: Incomplete
    def __init__(self, config: EfficientFormerConfig, in_features: int, hidden_features: Optional[int] = None, out_features: Optional[int] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class EfficientFormerConvMlp(nn.Module):
    convolution1: Incomplete
    actvation: Incomplete
    convolution2: Incomplete
    dropout: Incomplete
    batchnorm_before: Incomplete
    batchnorm_after: Incomplete
    def __init__(self, config: EfficientFormerConfig, in_features: int, hidden_features: Optional[int] = None, out_features: Optional[int] = None, drop: float = 0.0) -> None: ...
    def forward(self, hidden_state: torch.Tensor) -> torch.Tensor: ...

def drop_path(input, drop_prob: float = 0.0, training: bool = False):
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).

    Comment by Ross Wightman: This is the same as the DropConnect impl I created for EfficientNet, etc networks,
    however, the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for changing the
    layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use 'survival rate' as the
    argument.
    """

class EfficientFormerDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    drop_prob: Incomplete
    def __init__(self, drop_prob: Optional[float] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def extra_repr(self) -> str: ...

class EfficientFormerFlat(nn.Module):
    def __init__(self) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> Tuple[torch.Tensor]: ...

class EfficientFormerMeta3D(nn.Module):
    token_mixer: Incomplete
    layernorm1: Incomplete
    layernorm2: Incomplete
    mlp: Incomplete
    drop_path: Incomplete
    use_layer_scale: Incomplete
    layer_scale_1: Incomplete
    layer_scale_2: Incomplete
    def __init__(self, config: EfficientFormerConfig, dim: int, drop_path: float = 0.0) -> None: ...
    def forward(self, hidden_states: torch.Tensor, output_attentions: bool = False) -> Tuple[torch.Tensor]: ...

class EfficientFormerMeta3DLayers(nn.Module):
    blocks: Incomplete
    def __init__(self, config: EfficientFormerConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, output_attentions: bool = False) -> Tuple[torch.Tensor]: ...

class EfficientFormerMeta4D(nn.Module):
    token_mixer: Incomplete
    mlp: Incomplete
    drop_path: Incomplete
    use_layer_scale: Incomplete
    layer_scale_1: Incomplete
    layer_scale_2: Incomplete
    def __init__(self, config: EfficientFormerConfig, dim: int, drop_path: float = 0.0) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> Tuple[torch.Tensor]: ...

class EfficientFormerMeta4DLayers(nn.Module):
    blocks: Incomplete
    def __init__(self, config: EfficientFormerConfig, stage_idx: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> Tuple[torch.Tensor]: ...

class EfficientFormerIntermediateStage(nn.Module):
    meta4D_layers: Incomplete
    def __init__(self, config: EfficientFormerConfig, index: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> Tuple[torch.Tensor]: ...

class EfficientFormerLastStage(nn.Module):
    meta4D_layers: Incomplete
    flat: Incomplete
    meta3D_layers: Incomplete
    def __init__(self, config: EfficientFormerConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, output_attentions: bool = False) -> Tuple[torch.Tensor]: ...

class EfficientFormerEncoder(nn.Module):
    config: Incomplete
    intermediate_stages: Incomplete
    last_stage: Incomplete
    def __init__(self, config: EfficientFormerConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, output_hidden_states: bool = False, output_attentions: bool = False, return_dict: bool = True) -> BaseModelOutput: ...

class EfficientFormerPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = EfficientFormerConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

EFFICIENTFORMER_START_DOCSTRING: str
EFFICIENTFORMER_INPUTS_DOCSTRING: str

class EfficientFormerModel(EfficientFormerPreTrainedModel):
    config: Incomplete
    patch_embed: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    def __init__(self, config: EfficientFormerConfig) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, BaseModelOutput]: ...

class EfficientFormerForImageClassification(EfficientFormerPreTrainedModel):
    num_labels: Incomplete
    efficientformer: Incomplete
    classifier: Incomplete
    def __init__(self, config: EfficientFormerConfig) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, ImageClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

@dataclass
class EfficientFormerForImageClassificationWithTeacherOutput(ModelOutput):
    """
    Output type of [`EfficientFormerForImageClassificationWithTeacher`].

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

class EfficientFormerForImageClassificationWithTeacher(EfficientFormerPreTrainedModel):
    num_labels: Incomplete
    efficientformer: Incomplete
    classifier: Incomplete
    distillation_classifier: Incomplete
    def __init__(self, config: EfficientFormerConfig) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, EfficientFormerForImageClassificationWithTeacherOutput]: ...
