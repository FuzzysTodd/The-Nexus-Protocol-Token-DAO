import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, ImageClassifierOutput as ImageClassifierOutput, SemanticSegmenterOutput as SemanticSegmenterOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_segformer import SegformerConfig as SegformerConfig
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
SEGFORMER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class SegFormerImageClassifierOutput(ImageClassifierOutput):
    """
    Base class for outputs of image classification models.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Classification (or regression if config.num_labels==1) loss.
        logits (`torch.FloatTensor` of shape `(batch_size, config.num_labels)`):
            Classification (or regression if config.num_labels==1) scores (before SoftMax).
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each stage) of shape `(batch_size, num_channels, height, width)`. Hidden-states (also
            called feature maps) of the model at the output of each stage.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, patch_size,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor]
    logits: torch.FloatTensor
    hidden_states: Optional[Tuple[torch.FloatTensor]]
    attentions: Optional[Tuple[torch.FloatTensor]]

def drop_path(input, drop_prob: float = 0.0, training: bool = False, scale_by_keep: bool = True):
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).

    Comment by Ross Wightman: This is the same as the DropConnect impl I created for EfficientNet, etc networks,
    however, the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for changing the
    layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use 'survival rate' as the
    argument.
    """

class SegformerDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    drop_prob: Incomplete
    def __init__(self, drop_prob: Optional[float] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def extra_repr(self) -> str: ...

class SegformerOverlapPatchEmbeddings(nn.Module):
    """Construct the overlapping patch embeddings."""
    proj: Incomplete
    layer_norm: Incomplete
    def __init__(self, patch_size, stride, num_channels, hidden_size) -> None: ...
    def forward(self, pixel_values): ...

class SegformerEfficientSelfAttention(nn.Module):
    """SegFormer's efficient self-attention mechanism. Employs the sequence reduction process introduced in the [PvT
    paper](https://arxiv.org/abs/2102.12122)."""
    hidden_size: Incomplete
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    sr_ratio: Incomplete
    sr: Incomplete
    layer_norm: Incomplete
    def __init__(self, config, hidden_size, num_attention_heads, sequence_reduction_ratio) -> None: ...
    def transpose_for_scores(self, hidden_states): ...
    def forward(self, hidden_states, height, width, output_attentions: bool = False): ...

class SegformerSelfOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config, hidden_size) -> None: ...
    def forward(self, hidden_states, input_tensor): ...

class SegformerAttention(nn.Module):
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config, hidden_size, num_attention_heads, sequence_reduction_ratio) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states, height, width, output_attentions: bool = False): ...

class SegformerDWConv(nn.Module):
    dwconv: Incomplete
    def __init__(self, dim: int = 768) -> None: ...
    def forward(self, hidden_states, height, width): ...

class SegformerMixFFN(nn.Module):
    dense1: Incomplete
    dwconv: Incomplete
    intermediate_act_fn: Incomplete
    dense2: Incomplete
    dropout: Incomplete
    def __init__(self, config, in_features, hidden_features: Incomplete | None = None, out_features: Incomplete | None = None) -> None: ...
    def forward(self, hidden_states, height, width): ...

class SegformerLayer(nn.Module):
    """This corresponds to the Block class in the original implementation."""
    layer_norm_1: Incomplete
    attention: Incomplete
    drop_path: Incomplete
    layer_norm_2: Incomplete
    mlp: Incomplete
    def __init__(self, config, hidden_size, num_attention_heads, drop_path, sequence_reduction_ratio, mlp_ratio) -> None: ...
    def forward(self, hidden_states, height, width, output_attentions: bool = False): ...

class SegformerEncoder(nn.Module):
    config: Incomplete
    patch_embeddings: Incomplete
    block: Incomplete
    layer_norm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor, output_attentions: Optional[bool] = False, output_hidden_states: Optional[bool] = False, return_dict: Optional[bool] = True) -> Union[Tuple, BaseModelOutput]: ...

class SegformerPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = SegformerConfig
    base_model_prefix: str
    main_input_name: str

SEGFORMER_START_DOCSTRING: str
SEGFORMER_INPUTS_DOCSTRING: str

class SegformerModel(SegformerPreTrainedModel):
    config: Incomplete
    encoder: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]: ...

class SegformerForImageClassification(SegformerPreTrainedModel):
    num_labels: Incomplete
    segformer: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, SegFormerImageClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class SegformerMLP(nn.Module):
    """
    Linear Embedding.
    """
    proj: Incomplete
    def __init__(self, config: SegformerConfig, input_dim) -> None: ...
    def forward(self, hidden_states: torch.Tensor): ...

class SegformerDecodeHead(SegformerPreTrainedModel):
    linear_c: Incomplete
    linear_fuse: Incomplete
    batch_norm: Incomplete
    activation: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    config: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, encoder_hidden_states: torch.FloatTensor) -> torch.Tensor: ...

class SegformerForSemanticSegmentation(SegformerPreTrainedModel):
    segformer: Incomplete
    decode_head: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, SemanticSegmenterOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, height, width)`, *optional*):
            Ground truth semantic segmentation maps for computing the loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels > 1`, a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, SegformerForSemanticSegmentation
        >>> from PIL import Image
        >>> import requests

        >>> image_processor = AutoImageProcessor.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")
        >>> model = SegformerForSemanticSegmentation.from_pretrained("nvidia/segformer-b0-finetuned-ade-512-512")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = image_processor(images=image, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> logits = outputs.logits  # shape (batch_size, num_labels, height/4, width/4)
        >>> list(logits.shape)
        [1, 150, 128, 128]
        ```'''
