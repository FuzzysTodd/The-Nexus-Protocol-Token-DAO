import nni.nas.nn.pytorch as nn
import torch
from .utils.fixed import FixedFactory as FixedFactory
from .utils.pretrained import load_pretrained_weight as load_pretrained_weight
from _typeshed import Incomplete
from nni.nas import model_wrapper as model_wrapper
from typing import Callable, Iterator, List, Tuple, overload

@overload
def make_divisible(v: int | float, divisor, min_val: Incomplete | None = None) -> int: ...
@overload
def make_divisible(v: nn.ChoiceOf[int] | nn.ChoiceOf[float], divisor, min_val: Incomplete | None = None) -> nn.ChoiceOf[int]: ...
def simplify_sequential(sequentials: List[nn.Module]) -> Iterator[nn.Module]:
    """
    Flatten the sequential blocks so that the hierarchy looks better.
    Eliminate identity modules automatically.
    """

class ConvBNReLU(nn.Sequential):
    """
    The template for a conv-bn-relu block.
    """
    def __init__(self, in_channels: nn.MaybeChoice[int], out_channels: nn.MaybeChoice[int], kernel_size: nn.MaybeChoice[int] = 3, stride: int = 1, groups: nn.MaybeChoice[int] = 1, norm_layer: Callable[[int], nn.Module] | None = None, activation_layer: Callable[..., nn.Module] | None = None, dilation: int = 1) -> None: ...

class DepthwiseSeparableConv(nn.Sequential):
    """
    In the original MobileNetV2 implementation, this is InvertedResidual when expand ratio = 1.
    Residual connection is added if input and output shape are the same.

    References:

    - https://github.com/rwightman/pytorch-image-models/blob/b7cb8d03/timm/models/efficientnet_blocks.py#L90
    - https://github.com/google-research/google-research/blob/20736344/tunas/rematlib/mobile_model_v3.py#L433
    - https://github.com/ultmaster/AceNAS/blob/46c8895f/searchspace/proxylessnas/utils.py#L100
    """
    has_skip: Incomplete
    def __init__(self, in_channels: nn.MaybeChoice[int], out_channels: nn.MaybeChoice[int], kernel_size: nn.MaybeChoice[int] = 3, stride: int = 1, squeeze_excite: Callable[[nn.MaybeChoice[int], nn.MaybeChoice[int]], nn.Module] | None = None, norm_layer: Callable[[int], nn.Module] | None = None, activation_layer: Callable[..., nn.Module] | None = None) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class InvertedResidual(nn.Sequential):
    """
    An Inverted Residual Block, sometimes called an MBConv Block, is a type of residual block used for image models
    that uses an inverted structure for efficiency reasons.

    It was originally proposed for the `MobileNetV2 <https://arxiv.org/abs/1801.04381>`__ CNN architecture.
    It has since been reused for several mobile-optimized CNNs.
    It follows a narrow -> wide -> narrow approach, hence the inversion.
    It first widens with a 1x1 convolution, then uses a 3x3 depthwise convolution (which greatly reduces the number of parameters),
    then a 1x1 convolution is used to reduce the number of channels so input and output can be added.

    This implementation is sort of a mixture between:

    - https://github.com/google-research/google-research/blob/20736344/tunas/rematlib/mobile_model_v3.py#L453
    - https://github.com/rwightman/pytorch-image-models/blob/b7cb8d03/timm/models/efficientnet_blocks.py#L134

    Parameters
    ----------
    in_channels
        The number of input channels. Can be a value choice.
    out_channels
        The number of output channels. Can be a value choice.
    expand_ratio
        The ratio of intermediate channels with respect to input channels. Can be a value choice.
    kernel_size
        The kernel size of the depthwise convolution. Can be a value choice.
    stride
        The stride of the depthwise convolution.
    squeeze_excite
        Callable to create squeeze and excitation layer. Take hidden channels and input channels as arguments.
    norm_layer
        Callable to create normalization layer. Take input channels as argument.
    activation_layer
        Callable to create activation layer. No input arguments.
    """
    stride: Incomplete
    out_channels: Incomplete
    has_skip: Incomplete
    def __init__(self, in_channels: nn.MaybeChoice[int], out_channels: nn.MaybeChoice[int], expand_ratio: nn.MaybeChoice[float], kernel_size: nn.MaybeChoice[int] = 3, stride: int = 1, squeeze_excite: Callable[[nn.MaybeChoice[int], nn.MaybeChoice[int]], nn.Module] | None = None, norm_layer: Callable[[int], nn.Module] | None = None, activation_layer: Callable[..., nn.Module] | None = None) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

def inverted_residual_choice_builder(expand_ratios: List[int], kernel_sizes: List[int], downsample: bool, stage_input_width: int, stage_output_width: int, label: str): ...

class ProxylessNAS(nn.Module):
    """
    The search space proposed by `ProxylessNAS <https://arxiv.org/abs/1812.00332>`__.

    Following the official implementation, the inverted residual with kernel size / expand ratio variations in each layer
    is implemented with a :class:`~nni.retiarii.nn.pytorch.LayerChoice` with all-combination candidates. That means,
    when used in weight sharing, these candidates will be treated as separate layers, and won't be fine-grained shared.
    We note that :class:`MobileNetV3Space` is different in this perspective.

    This space can be implemented as part of :class:`MobileNetV3Space`, but we separate those following conventions.

    Parameters
    ----------
    num_labels
        The number of labels for classification.
    base_widths
        Widths of each stage, from stem, to body, to head. Length should be 9.
    dropout_rate
        Dropout rate for the final classification layer.
    width_mult
        Width multiplier for the model.
    bn_eps
        Epsilon for batch normalization.
    bn_momentum
        Momentum for batch normalization.
    """
    num_labels: Incomplete
    dropout_rate: Incomplete
    bn_eps: Incomplete
    bn_momentum: Incomplete
    stem: Incomplete
    blocks: Incomplete
    feature_mix_layer: Incomplete
    global_avg_pooling: Incomplete
    dropout_layer: Incomplete
    classifier: Incomplete
    def __init__(self, num_labels: int = 1000, base_widths: Tuple[int, ...] = (32, 16, 32, 40, 80, 96, 192, 320, 1280), dropout_rate: float = 0.0, width_mult: float = 1.0, bn_eps: float = 0.001, bn_momentum: float = 0.1) -> None: ...
    def forward(self, x): ...
    def no_weight_decay(self): ...
    @classmethod
    def fixed_arch(cls, arch: dict) -> FixedFactory: ...
    @classmethod
    def load_searched_model(cls, name: str, pretrained: bool = False, download: bool = False, progress: bool = True) -> nn.Module: ...

def reset_parameters(model, model_init: str = 'he_fout', init_div_groups: bool = False, bn_momentum: float = 0.1, bn_eps: float = 1e-05) -> None: ...
