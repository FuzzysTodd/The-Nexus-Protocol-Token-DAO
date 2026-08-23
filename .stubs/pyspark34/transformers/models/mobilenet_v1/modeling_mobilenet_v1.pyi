import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutputWithPoolingAndNoAttention as BaseModelOutputWithPoolingAndNoAttention, ImageClassifierOutputWithNoAttention as ImageClassifierOutputWithNoAttention
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_mobilenet_v1 import MobileNetV1Config as MobileNetV1Config
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Union

logger: Incomplete
MOBILENET_V1_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def load_tf_weights_in_mobilenet_v1(model, config, tf_checkpoint_path):
    """Load TensorFlow checkpoints in a PyTorch model."""
def apply_tf_padding(features: torch.Tensor, conv_layer: nn.Conv2d) -> torch.Tensor:
    '''
    Apply TensorFlow-style "SAME" padding to a convolution layer. See the notes at:
    https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2
    '''

class MobileNetV1ConvLayer(nn.Module):
    config: Incomplete
    convolution: Incomplete
    normalization: Incomplete
    activation: Incomplete
    def __init__(self, config: MobileNetV1Config, in_channels: int, out_channels: int, kernel_size: int, stride: Optional[int] = 1, groups: Optional[int] = 1, bias: bool = False, use_normalization: Optional[bool] = True, use_activation: Optional[None] = True) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MobileNetV1PreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = MobileNetV1Config
    load_tf_weights = load_tf_weights_in_mobilenet_v1
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

MOBILENET_V1_START_DOCSTRING: str
MOBILENET_V1_INPUTS_DOCSTRING: str

class MobileNetV1Model(MobileNetV1PreTrainedModel):
    config: Incomplete
    conv_stem: Incomplete
    layer: Incomplete
    pooler: Incomplete
    def __init__(self, config: MobileNetV1Config, add_pooling_layer: bool = True) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[tuple, BaseModelOutputWithPoolingAndNoAttention]: ...

class MobileNetV1ForImageClassification(MobileNetV1PreTrainedModel):
    num_labels: Incomplete
    mobilenet_v1: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config: MobileNetV1Config) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, output_hidden_states: Optional[bool] = None, labels: Optional[torch.Tensor] = None, return_dict: Optional[bool] = None) -> Union[tuple, ImageClassifierOutputWithNoAttention]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss). If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
