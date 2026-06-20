import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling, SequenceClassifierOutput as SequenceClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_audio_spectrogram_transformer import ASTConfig as ASTConfig
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Set, Tuple, Union

logger: Incomplete
AUDIO_SPECTROGRAM_TRANSFORMER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class ASTEmbeddings(nn.Module):
    """
    Construct the CLS token, position and patch embeddings.
    """
    cls_token: Incomplete
    distillation_token: Incomplete
    patch_embeddings: Incomplete
    position_embeddings: Incomplete
    dropout: Incomplete
    config: Incomplete
    def __init__(self, config: ASTConfig) -> None: ...
    def get_shape(self, config): ...
    def forward(self, input_values: torch.Tensor) -> torch.Tensor: ...

class ASTPatchEmbeddings(nn.Module):
    """
    This class turns `input_values` into the initial `hidden_states` (patch embeddings) of shape `(batch_size,
    seq_length, hidden_size)` to be consumed by a Transformer.
    """
    projection: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_values: torch.Tensor) -> torch.Tensor: ...

class ASTSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config: ASTConfig) -> None: ...
    def transpose_for_scores(self, x: torch.Tensor) -> torch.Tensor: ...
    def forward(self, hidden_states, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Union[Tuple[torch.Tensor, torch.Tensor], Tuple[torch.Tensor]]: ...

class ASTSelfOutput(nn.Module):
    """
    The residual connection is defined in ASTLayer instead of here (as is the case with other models), due to the
    layernorm applied before each block.
    """
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: ASTConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class ASTAttention(nn.Module):
    attention: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config: ASTConfig) -> None: ...
    def prune_heads(self, heads: Set[int]) -> None: ...
    def forward(self, hidden_states: torch.Tensor, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Union[Tuple[torch.Tensor, torch.Tensor], Tuple[torch.Tensor]]: ...

class ASTIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: ASTConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class ASTOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: ASTConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class ASTLayer(nn.Module):
    """This corresponds to the Block class in the timm implementation."""
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    layernorm_before: Incomplete
    layernorm_after: Incomplete
    def __init__(self, config: ASTConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Union[Tuple[torch.Tensor, torch.Tensor], Tuple[torch.Tensor]]: ...

class ASTEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: ASTConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True) -> Union[tuple, BaseModelOutput]: ...

class ASTPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ASTConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

AUDIO_SPECTROGRAM_TRANSFORMER_START_DOCSTRING: str
AUDIO_SPECTROGRAM_TRANSFORMER_INPUTS_DOCSTRING: str

class ASTModel(ASTPreTrainedModel):
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    def __init__(self, config: ASTConfig) -> None: ...
    def get_input_embeddings(self) -> ASTPatchEmbeddings: ...
    def forward(self, input_values: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None): ...

class ASTMLPHead(nn.Module):
    layernorm: Incomplete
    dense: Incomplete
    def __init__(self, config: ASTConfig) -> None: ...
    def forward(self, hidden_state): ...

class ASTForAudioClassification(ASTPreTrainedModel):
    num_labels: Incomplete
    audio_spectrogram_transformer: Incomplete
    classifier: Incomplete
    def __init__(self, config: ASTConfig) -> None: ...
    def forward(self, input_values: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, SequenceClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the audio classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
