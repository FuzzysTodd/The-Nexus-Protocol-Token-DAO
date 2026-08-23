import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutputWithNoAttention as BaseModelOutputWithNoAttention, ImageClassifierOutputWithNoAttention as ImageClassifierOutputWithNoAttention
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_poolformer import PoolFormerConfig as PoolFormerConfig
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
POOLFORMER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def drop_path(input, drop_prob: float = 0.0, training: bool = False):
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).

    Comment by Ross Wightman: This is the same as the DropConnect impl I created for EfficientNet, etc networks,
    however, the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for changing the
    layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use 'survival rate' as the
    argument.
    """

class PoolFormerDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    drop_prob: Incomplete
    def __init__(self, drop_prob: Optional[float] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def extra_repr(self) -> str: ...

class PoolFormerEmbeddings(nn.Module):
    """
    Construct Patch Embeddings.
    """
    projection: Incomplete
    norm: Incomplete
    def __init__(self, hidden_size, num_channels, patch_size, stride, padding, norm_layer: Incomplete | None = None) -> None: ...
    def forward(self, pixel_values): ...

class PoolFormerGroupNorm(nn.GroupNorm):
    """
    Group Normalization with 1 group. Input: tensor in shape [B, C, H, W]
    """
    def __init__(self, num_channels, **kwargs) -> None: ...

class PoolFormerPooling(nn.Module):
    pool: Incomplete
    def __init__(self, pool_size) -> None: ...
    def forward(self, hidden_states): ...

class PoolFormerOutput(nn.Module):
    conv1: Incomplete
    conv2: Incomplete
    drop: Incomplete
    act_fn: Incomplete
    def __init__(self, config, dropout_prob, hidden_size, intermediate_size) -> None: ...
    def forward(self, hidden_states): ...

class PoolFormerLayer(nn.Module):
    """This corresponds to the 'PoolFormerBlock' class in the original implementation."""
    pooling: Incomplete
    output: Incomplete
    before_norm: Incomplete
    after_norm: Incomplete
    drop_path: Incomplete
    use_layer_scale: Incomplete
    layer_scale_1: Incomplete
    layer_scale_2: Incomplete
    def __init__(self, config, num_channels, pool_size, hidden_size, intermediate_size, drop_path) -> None: ...
    def forward(self, hidden_states): ...

class PoolFormerEncoder(nn.Module):
    config: Incomplete
    patch_embeddings: Incomplete
    block: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values, output_hidden_states: bool = False, return_dict: bool = True): ...

class PoolFormerPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = PoolFormerConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

POOLFORMER_START_DOCSTRING: str
POOLFORMER_INPUTS_DOCSTRING: str

class PoolFormerModel(PoolFormerPreTrainedModel):
    config: Incomplete
    encoder: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithNoAttention]: ...

class PoolFormerFinalPooler(nn.Module):
    dense: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class PoolFormerForImageClassification(PoolFormerPreTrainedModel):
    num_labels: Incomplete
    poolformer: Incomplete
    norm: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, ImageClassifierOutputWithNoAttention]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
