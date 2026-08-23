import torch
from ...modeling_outputs import BaseModelOutputWithNoAttention as BaseModelOutputWithNoAttention, BaseModelOutputWithPoolingAndNoAttention as BaseModelOutputWithPoolingAndNoAttention, ImageClassifierOutputWithNoAttention as ImageClassifierOutputWithNoAttention, ModelOutput as ModelOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_levit import LevitConfig as LevitConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
LEVIT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class LevitForImageClassificationWithTeacherOutput(ModelOutput):
    """
    Output type of [`LevitForImageClassificationWithTeacher`].

    Args:
        logits (`torch.FloatTensor` of shape `(batch_size, config.num_labels)`):
            Prediction scores as the average of the `cls_logits` and `distillation_logits`.
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
    """
    logits: torch.FloatTensor = ...
    cls_logits: torch.FloatTensor = ...
    distillation_logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, logits, cls_logits, distillation_logits, hidden_states) -> None: ...

class LevitConvEmbeddings(nn.Module):
    """
    LeViT Conv Embeddings with Batch Norm, used in the initial patch embedding layer.
    """
    convolution: Incomplete
    batch_norm: Incomplete
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding, dilation: int = 1, groups: int = 1, bn_weight_init: int = 1) -> None: ...
    def forward(self, embeddings): ...

class LevitPatchEmbeddings(nn.Module):
    """
    LeViT patch embeddings, for final embeddings to be passed to transformer blocks. It consists of multiple
    `LevitConvEmbeddings`.
    """
    embedding_layer_1: Incomplete
    activation_layer_1: Incomplete
    embedding_layer_2: Incomplete
    activation_layer_2: Incomplete
    embedding_layer_3: Incomplete
    activation_layer_3: Incomplete
    embedding_layer_4: Incomplete
    num_channels: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values): ...

class MLPLayerWithBN(nn.Module):
    linear: Incomplete
    batch_norm: Incomplete
    def __init__(self, input_dim, output_dim, bn_weight_init: int = 1) -> None: ...
    def forward(self, hidden_state): ...

class LevitSubsample(nn.Module):
    stride: Incomplete
    resolution: Incomplete
    def __init__(self, stride, resolution) -> None: ...
    def forward(self, hidden_state): ...

class LevitAttention(nn.Module):
    num_attention_heads: Incomplete
    scale: Incomplete
    key_dim: Incomplete
    attention_ratio: Incomplete
    out_dim_keys_values: Incomplete
    out_dim_projection: Incomplete
    queries_keys_values: Incomplete
    activation: Incomplete
    projection: Incomplete
    attention_bias_cache: Incomplete
    attention_biases: Incomplete
    def __init__(self, hidden_sizes, key_dim, num_attention_heads, attention_ratio, resolution) -> None: ...
    def train(self, mode: bool = True) -> None: ...
    def get_attention_biases(self, device): ...
    def forward(self, hidden_state): ...

class LevitAttentionSubsample(nn.Module):
    num_attention_heads: Incomplete
    scale: Incomplete
    key_dim: Incomplete
    attention_ratio: Incomplete
    out_dim_keys_values: Incomplete
    out_dim_projection: Incomplete
    resolution_out: Incomplete
    keys_values: Incomplete
    queries_subsample: Incomplete
    queries: Incomplete
    activation: Incomplete
    projection: Incomplete
    attention_bias_cache: Incomplete
    attention_biases: Incomplete
    def __init__(self, input_dim, output_dim, key_dim, num_attention_heads, attention_ratio, stride, resolution_in, resolution_out) -> None: ...
    def train(self, mode: bool = True) -> None: ...
    def get_attention_biases(self, device): ...
    def forward(self, hidden_state): ...

class LevitMLPLayer(nn.Module):
    """
    MLP Layer with `2X` expansion in contrast to ViT with `4X`.
    """
    linear_up: Incomplete
    activation: Incomplete
    linear_down: Incomplete
    def __init__(self, input_dim, hidden_dim) -> None: ...
    def forward(self, hidden_state): ...

class LevitResidualLayer(nn.Module):
    """
    Residual Block for LeViT
    """
    module: Incomplete
    drop_rate: Incomplete
    def __init__(self, module, drop_rate) -> None: ...
    def forward(self, hidden_state): ...

class LevitStage(nn.Module):
    """
    LeViT Stage consisting of `LevitMLPLayer` and `LevitAttention` layers.
    """
    layers: Incomplete
    config: Incomplete
    resolution_in: Incomplete
    resolution_out: Incomplete
    def __init__(self, config, idx, hidden_sizes, key_dim, depths, num_attention_heads, attention_ratio, mlp_ratio, down_ops, resolution_in) -> None: ...
    def get_resolution(self): ...
    def forward(self, hidden_state): ...

class LevitEncoder(nn.Module):
    """
    LeViT Encoder consisting of multiple `LevitStage` stages.
    """
    config: Incomplete
    stages: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_state, output_hidden_states: bool = False, return_dict: bool = True): ...

class LevitClassificationLayer(nn.Module):
    """
    LeViT Classification Layer
    """
    batch_norm: Incomplete
    linear: Incomplete
    def __init__(self, input_dim, output_dim) -> None: ...
    def forward(self, hidden_state): ...

class LevitPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = LevitConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

LEVIT_START_DOCSTRING: str
LEVIT_INPUTS_DOCSTRING: str

class LevitModel(LevitPreTrainedModel):
    config: Incomplete
    patch_embeddings: Incomplete
    encoder: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPoolingAndNoAttention]: ...

class LevitForImageClassification(LevitPreTrainedModel):
    config: Incomplete
    num_labels: Incomplete
    levit: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor = None, labels: Optional[torch.LongTensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, ImageClassifierOutputWithNoAttention]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class LevitForImageClassificationWithTeacher(LevitPreTrainedModel):
    config: Incomplete
    num_labels: Incomplete
    levit: Incomplete
    classifier: Incomplete
    classifier_distill: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, LevitForImageClassificationWithTeacherOutput]: ...
