import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling, ImageClassifierOutput as ImageClassifierOutput, SemanticSegmenterOutput as SemanticSegmenterOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, meshgrid as meshgrid, prune_linear_layer as prune_linear_layer
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_data2vec_vision import Data2VecVisionConfig as Data2VecVisionConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import List, Optional, Tuple, Union

logger: Incomplete
DATA2VEC_VISION_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class Data2VecVisionModelOutputWithPooling(BaseModelOutputWithPooling):
    """
    Class for outputs of [`Data2VecVisionModel`].

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        pooler_output (`torch.FloatTensor` of shape `(batch_size, hidden_size)`):
            Average of the last layer hidden states of the patch tokens (excluding the *[CLS]* token) if
            *config.use_mean_pooling* is set to True. If set to False, then the final hidden state of the *[CLS]* token
            will be returned.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    def __init__(self, last_hidden_state, pooler_output, hidden_states, attentions) -> None: ...

def drop_path(input: torch.Tensor, drop_prob: float = 0.0, training: bool = False) -> torch.Tensor:
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).

    Comment by Ross Wightman: This is the same as the DropConnect impl I created for EfficientNet, etc networks,
    however, the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for changing the
    layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use 'survival rate' as the
    argument.
    """

class Data2VecVisionDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    drop_prob: Incomplete
    def __init__(self, drop_prob: Optional[float] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def extra_repr(self) -> str: ...

class Data2VecVisionEmbeddings(nn.Module):
    """
    Construct the CLS token, position and patch embeddings. Optionally, also the mask token.

    """
    cls_token: Incomplete
    mask_token: Incomplete
    patch_embeddings: Incomplete
    position_embeddings: Incomplete
    dropout: Incomplete
    def __init__(self, config: Data2VecVisionConfig) -> None: ...
    def forward(self, pixel_values: torch.Tensor, bool_masked_pos: Optional[torch.BoolTensor] = None) -> torch.Tensor: ...

class Data2VecVisionPatchEmbeddings(nn.Module):
    """
    This class turns `pixel_values` of shape `(batch_size, num_channels, height, width)` into the initial
    `hidden_states` (patch embeddings) of shape `(batch_size, seq_length, hidden_size)` to be consumed by a
    Transformer.
    """
    image_size: Incomplete
    patch_size: Incomplete
    num_channels: Incomplete
    num_patches: Incomplete
    patch_shape: Incomplete
    projection: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.Tensor) -> torch.Tensor: ...

class Data2VecVisionSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    relative_position_bias: Incomplete
    def __init__(self, config: Data2VecVisionConfig, window_size: Optional[tuple] = None) -> None: ...
    def transpose_for_scores(self, x): ...
    def forward(self, hidden_states: torch.Tensor, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False, relative_position_bias: Optional['Data2VecVisionRelativePositionBias'] = None) -> Union[Tuple[torch.Tensor], Tuple[torch.Tensor, torch.Tensor]]: ...

class Data2VecVisionSelfOutput(nn.Module):
    """
    The residual connection is defined in Data2VecVisionLayer instead of here (as is the case with other models), due
    to the layernorm applied before each block.
    """
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: Data2VecVisionConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor, gamma: Incomplete | None = None) -> torch.Tensor: ...

class Data2VecVisionAttention(nn.Module):
    attention: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config: Data2VecVisionConfig, window_size: Optional[tuple] = None) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states: torch.Tensor, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False, relative_position_bias: Optional['Data2VecVisionRelativePositionBias'] = None) -> Union[Tuple[torch.Tensor], Tuple[torch.Tensor, torch.Tensor]]: ...

class Data2VecVisionIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: Data2VecVisionConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class Data2VecVisionOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: Data2VecVisionConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class Data2VecVisionLayer(nn.Module):
    """This corresponds to the Block class in the timm implementation."""
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    layernorm_before: Incomplete
    drop_path: Incomplete
    layernorm_after: Incomplete
    lambda_1: Incomplete
    lambda_2: Incomplete
    def __init__(self, config: Data2VecVisionConfig, window_size: Optional[tuple] = None, drop_path_rate: float = 0.0) -> None: ...
    def forward(self, hidden_states: torch.Tensor, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False, relative_position_bias: Optional['Data2VecVisionRelativePositionBias'] = None) -> Union[Tuple[torch.Tensor], Tuple[torch.Tensor, torch.Tensor]]: ...

class Data2VecVisionRelativePositionBias(nn.Module):
    window_size: Incomplete
    num_relative_distance: Incomplete
    relative_position_bias_table: Incomplete
    def __init__(self, config: Data2VecVisionConfig, window_size: tuple) -> None: ...
    def forward(self) -> torch.Tensor: ...

class Data2VecVisionEncoder(nn.Module):
    config: Incomplete
    relative_position_bias: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: Data2VecVisionConfig, window_size: Optional[tuple] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor, head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True) -> Union[tuple, BaseModelOutput]: ...

class Data2VecVisionPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = Data2VecVisionConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

DATA2VEC_VISION_START_DOCSTRING: str
DATA2VEC_VISION_INPUTS_DOCSTRING: str

class Data2VecVisionModel(Data2VecVisionPreTrainedModel):
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    pooler: Incomplete
    def __init__(self, config: Data2VecVisionConfig, add_pooling_layer: bool = False) -> None: ...
    def get_input_embeddings(self): ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, bool_masked_pos: Optional[torch.BoolTensor] = None, head_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, Data2VecVisionModelOutputWithPooling]: ...

class Data2VecVisionPooler(nn.Module):
    layernorm: Incomplete
    def __init__(self, config: Data2VecVisionConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class Data2VecVisionForImageClassification(Data2VecVisionPreTrainedModel):
    num_labels: Incomplete
    data2vec_vision: Incomplete
    classifier: Incomplete
    def __init__(self, config: Data2VecVisionConfig) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, ImageClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class Data2VecVisionConvModule(nn.Module):
    """
    A convolutional block that bundles conv/norm/activation layers. This block simplifies the usage of convolution
    layers, which are commonly used with a norm layer (e.g., BatchNorm) and activation layer (e.g., ReLU).

    Based on OpenMMLab's implementation, found in https://github.com/open-mmlab/mmsegmentation.
    """
    conv: Incomplete
    bn: Incomplete
    activation: Incomplete
    def __init__(self, in_channels: int, out_channels: int, kernel_size: Union[int, Tuple[int, int]], padding: Union[int, Tuple[int, int], str] = 0, bias: bool = False, dilation: Union[int, Tuple[int, int]] = 1) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...

class Data2VecVisionPyramidPoolingBlock(nn.Module):
    layers: Incomplete
    def __init__(self, pool_scale: int, in_channels: int, channels: int) -> None: ...
    def forward(self, input: torch.Tensor) -> torch.Tensor: ...

class Data2VecVisionPyramidPoolingModule(nn.Module):
    """
    Pyramid Pooling Module (PPM) used in PSPNet.

    Args:
        pool_scales (tuple[int]): Pooling scales used in Pooling Pyramid
            Module.
        in_channels (int): Input channels.
        channels (int): Channels after modules, before conv_seg.
        align_corners (bool): align_corners argument of F.interpolate.

    Based on OpenMMLab's implementation, found in https://github.com/open-mmlab/mmsegmentation.
    """
    pool_scales: Incomplete
    align_corners: Incomplete
    in_channels: Incomplete
    channels: Incomplete
    blocks: Incomplete
    def __init__(self, pool_scales: Tuple[int, ...], in_channels: int, channels: int, align_corners: bool) -> None: ...
    def forward(self, x: torch.Tensor) -> List[torch.Tensor]: ...

class Data2VecVisionUperHead(nn.Module):
    """
    Unified Perceptual Parsing for Scene Understanding. This head is the implementation of
    [UPerNet](https://arxiv.org/abs/1807.10221).

    Based on OpenMMLab's implementation, found in https://github.com/open-mmlab/mmsegmentation.
    """
    pool_scales: Incomplete
    in_channels: Incomplete
    channels: Incomplete
    align_corners: bool
    classifier: Incomplete
    psp_modules: Incomplete
    bottleneck: Incomplete
    lateral_convs: Incomplete
    fpn_convs: Incomplete
    fpn_bottleneck: Incomplete
    def __init__(self, config: Data2VecVisionConfig) -> None: ...
    def psp_forward(self, inputs): ...
    def forward(self, encoder_hidden_states: torch.Tensor) -> torch.Tensor: ...

class Data2VecVisionFCNHead(nn.Module):
    """
    Fully Convolution Networks for Semantic Segmentation. This head is implemented of
    [FCNNet](https://arxiv.org/abs/1411.4038>).

    Args:
        config (Data2VecVisionConfig): Configuration.
        in_channels
        kernel_size (int): The kernel size for convs in the head. Default: 3.
        dilation (int): The dilation rate for convs in the head. Default: 1.


    Based on OpenMMLab's implementation, found in https://github.com/open-mmlab/mmsegmentation.
    """
    in_channels: Incomplete
    channels: Incomplete
    num_convs: Incomplete
    concat_input: Incomplete
    in_index: Incomplete
    convs: Incomplete
    conv_cat: Incomplete
    classifier: Incomplete
    def __init__(self, config: Data2VecVisionConfig, in_index: int = 2, kernel_size: int = 3, dilation: Union[int, Tuple[int, int]] = 1) -> None: ...
    def forward(self, encoder_hidden_states: torch.Tensor) -> torch.Tensor: ...

class Data2VecVisionForSemanticSegmentation(Data2VecVisionPreTrainedModel):
    num_labels: Incomplete
    data2vec_vision: Incomplete
    fpn1: Incomplete
    fpn2: Incomplete
    fpn3: Incomplete
    fpn4: Incomplete
    decode_head: Incomplete
    auxiliary_head: Incomplete
    def __init__(self, config: Data2VecVisionConfig) -> None: ...
    def compute_loss(self, logits, auxiliary_logits, labels): ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, SemanticSegmenterOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, height, width)`, *optional*):
            Ground truth semantic segmentation maps for computing the loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1`, a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, Data2VecVisionForSemanticSegmentation
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("facebook/data2vec-vision-base")
        >>> model = Data2VecVisionForSemanticSegmentation.from_pretrained("facebook/data2vec-vision-base")

        >>> inputs = image_processor(images=image, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> # logits are of shape (batch_size, num_labels, height, width)
        >>> logits = outputs.logits
        ```'''
