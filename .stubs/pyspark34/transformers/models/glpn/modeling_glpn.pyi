import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, DepthEstimatorOutput as DepthEstimatorOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_glpn import GLPNConfig as GLPNConfig
from _typeshed import Incomplete
from torch import nn
from typing import List, Optional, Tuple, Union

logger: Incomplete
GLPN_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def drop_path(input, drop_prob: float = 0.0, training: bool = False):
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).

    Comment by Ross Wightman: This is the same as the DropConnect impl I created for EfficientNet, etc networks,
    however, the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for changing the
    layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use 'survival rate' as the
    argument.
    """

class GLPNDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    drop_prob: Incomplete
    def __init__(self, drop_prob: Optional[float] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def extra_repr(self) -> str: ...

class GLPNOverlapPatchEmbeddings(nn.Module):
    """Construct the overlapping patch embeddings."""
    proj: Incomplete
    layer_norm: Incomplete
    def __init__(self, patch_size, stride, num_channels, hidden_size) -> None: ...
    def forward(self, pixel_values): ...

class GLPNEfficientSelfAttention(nn.Module):
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

class GLPNSelfOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config, hidden_size) -> None: ...
    def forward(self, hidden_states, input_tensor): ...

class GLPNAttention(nn.Module):
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config, hidden_size, num_attention_heads, sequence_reduction_ratio) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states, height, width, output_attentions: bool = False): ...

class GLPNDWConv(nn.Module):
    dwconv: Incomplete
    def __init__(self, dim: int = 768) -> None: ...
    def forward(self, hidden_states, height, width): ...

class GLPNMixFFN(nn.Module):
    dense1: Incomplete
    dwconv: Incomplete
    intermediate_act_fn: Incomplete
    dense2: Incomplete
    dropout: Incomplete
    def __init__(self, config, in_features, hidden_features: Incomplete | None = None, out_features: Incomplete | None = None) -> None: ...
    def forward(self, hidden_states, height, width): ...

class GLPNLayer(nn.Module):
    """This corresponds to the Block class in the original implementation."""
    layer_norm_1: Incomplete
    attention: Incomplete
    drop_path: Incomplete
    layer_norm_2: Incomplete
    mlp: Incomplete
    def __init__(self, config, hidden_size, num_attention_heads, drop_path, sequence_reduction_ratio, mlp_ratio) -> None: ...
    def forward(self, hidden_states, height, width, output_attentions: bool = False): ...

class GLPNEncoder(nn.Module):
    config: Incomplete
    patch_embeddings: Incomplete
    block: Incomplete
    layer_norm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class GLPNPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = GLPNConfig
    base_model_prefix: str
    main_input_name: str

GLPN_START_DOCSTRING: str
GLPN_INPUTS_DOCSTRING: str

class GLPNModel(GLPNPreTrainedModel):
    config: Incomplete
    encoder: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]: ...

class GLPNSelectiveFeatureFusion(nn.Module):
    """
    Selective Feature Fusion module, as explained in the [paper](https://arxiv.org/abs/2201.07436) (section 3.4). This
    module adaptively selects and integrates local and global features by attaining an attention map for each feature.
    """
    convolutional_layer1: Incomplete
    convolutional_layer2: Incomplete
    convolutional_layer3: Incomplete
    sigmoid: Incomplete
    def __init__(self, in_channel: int = 64) -> None: ...
    def forward(self, local_features, global_features): ...

class GLPNDecoderStage(nn.Module):
    convolution: Incomplete
    fusion: Incomplete
    upsample: Incomplete
    def __init__(self, in_channels, out_channels) -> None: ...
    def forward(self, hidden_state, residual: Incomplete | None = None): ...

class GLPNDecoder(nn.Module):
    stages: Incomplete
    final_upsample: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: List[torch.Tensor]) -> List[torch.Tensor]: ...

class SiLogLoss(nn.Module):
    """
    Implements the Scale-invariant log scale loss [Eigen et al., 2014](https://arxiv.org/abs/1406.2283).

    $$L=\x0crac{1}{n} \\sum_{i} d_{i}^{2}-\x0crac{1}{2 n^{2}}\\left(\\sum_{i} d_{i}^{2}\right)$$ where $d_{i}=\\log y_{i}-\\log
    y_{i}^{*}$.

    """
    lambd: Incomplete
    def __init__(self, lambd: float = 0.5) -> None: ...
    def forward(self, pred, target): ...

class GLPNDepthEstimationHead(nn.Module):
    config: Incomplete
    head: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: List[torch.Tensor]) -> torch.Tensor: ...

class GLPNForDepthEstimation(GLPNPreTrainedModel):
    glpn: Incomplete
    decoder: Incomplete
    head: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor, labels: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], DepthEstimatorOutput]:
        '''
        labels (`torch.FloatTensor` of shape `(batch_size, height, width)`, *optional*):
            Ground truth depth estimation maps for computing the loss.

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, GLPNForDepthEstimation
        >>> import torch
        >>> import numpy as np
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("vinvino02/glpn-kitti")
        >>> model = GLPNForDepthEstimation.from_pretrained("vinvino02/glpn-kitti")

        >>> # prepare image for the model
        >>> inputs = image_processor(images=image, return_tensors="pt")

        >>> with torch.no_grad():
        ...     outputs = model(**inputs)
        ...     predicted_depth = outputs.predicted_depth

        >>> # interpolate to original size
        >>> prediction = torch.nn.functional.interpolate(
        ...     predicted_depth.unsqueeze(1),
        ...     size=image.size[::-1],
        ...     mode="bicubic",
        ...     align_corners=False,
        ... )

        >>> # visualize the prediction
        >>> output = prediction.squeeze().cpu().numpy()
        >>> formatted = (output * 255 / np.max(output)).astype("uint8")
        >>> depth = Image.fromarray(formatted)
        ```'''
