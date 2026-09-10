import nni.nas.nn.pytorch as nn
from .proxylessnas import ConvBNReLU as ConvBNReLU, DepthwiseSeparableConv as DepthwiseSeparableConv, InvertedResidual as InvertedResidual, make_divisible as make_divisible, reset_parameters as reset_parameters
from .utils.fixed import FixedFactory as FixedFactory
from .utils.pretrained import load_pretrained_weight as load_pretrained_weight
from _typeshed import Incomplete
from nni.nas import model_wrapper as model_wrapper
from nni.typehint import Literal as Literal
from typing import Callable, List, Tuple

class SqueezeExcite(nn.Module):
    """Squeeze-and-excite layer.

    We can't use the op from ``torchvision.ops`` because it's not (yet) properly wrapped,
    and ValueChoice couldn't be processed.

    Reference:

    - https://github.com/rwightman/pytorch-image-models/blob/b7cb8d03/timm/models/efficientnet_blocks.py#L26
    - https://github.com/d-li14/mobilenetv3.pytorch/blob/3e6938cedcbbc5ee5bc50780ea18e644702d85fc/mobilenetv3.py#L53
    """
    conv_reduce: Incomplete
    act1: Incomplete
    conv_expand: Incomplete
    gate: Incomplete
    def __init__(self, channels: int, reduction_ratio: float = 0.25, gate_layer: Callable[..., nn.Module] | None = None, activation_layer: Callable[..., nn.Module] | None = None) -> None: ...
    def forward(self, x): ...

class MobileNetV3Space(nn.Module):
    """
    MobileNetV3Space implements the largest search space in `TuNAS <https://arxiv.org/abs/2008.06120>`__.

    The search dimensions include widths, expand ratios, kernel sizes, SE ratio.
    Some of them can be turned off via arguments to narrow down the search space.

    Different from ProxylessNAS search space, this space is implemented with :class:`~nni.retiarii.nn.pytorch.ValueChoice`.

    We use the following snipppet as reference.
    https://github.com/google-research/google-research/blob/20736344591f774f4b1570af64624ed1e18d2867/tunas/mobile_search_space_v3.py#L728

    We have ``num_blocks`` which equals to the length of ``self.blocks`` (the main body of the network).
    For simplicity, the following parameter specification assumes ``num_blocks`` equals 8 (body + head).
    If a shallower body is intended, arrays including ``base_widths``, ``squeeze_excite``, ``depth_range``,
    ``stride``, ``activation`` should also be shortened accordingly.

    Parameters
    ----------
    num_labels
        Dimensions for classification head.
    base_widths
        Widths of each stage, from stem, to body, to head.
        Length should be 9, i.e., ``num_blocks + 1`` (because there is a stem width in front).
    width_multipliers
        A range of widths multiplier to choose from. The choice is independent for each stage.
        Or it can be a fixed float. This will be applied on ``base_widths``,
        and we would also make sure that widths can be divided by 8.
    expand_ratios
        A list of expand ratios to choose from. Independent for every **block**.
    squeeze_excite
        Indicating whether the current stage can have an optional SE layer.
        Expect array of length 6 for stage 0 to 5. Each element can be one of ``force``, ``optional``, ``none``.
    depth_range
        A range (e.g., ``(1, 4)``),
        or a list of range (e.g., ``[(1, 3), (1, 4), (1, 4), (1, 3), (0, 2)]``).
        If a list, the length should be 5. The depth are specified for stage 1 to 5.
    stride
        Stride for all stages (including stem and head). Length should be same as ``base_widths``.
    activation
        Activation (class) for all stages. Length is same as ``base_widths``.
    se_from_exp
        Calculate SE channel reduction from expanded (mid) channels.
    dropout_rate
        Dropout rate at classification head.
    bn_eps
        Epsilon of batch normalization.
    bn_momentum
        Momentum of batch normalization.
    """
    widths: List[nn.ChoiceOf[int] | int]
    depth_range: List[Tuple[int, int]]
    num_blocks: Incomplete
    expand_ratios: Incomplete
    se_from_exp: Incomplete
    stem: Incomplete
    blocks: Incomplete
    classifier: Incomplete
    def __init__(self, num_labels: int = 1000, base_widths: Tuple[int, ...] = (16, 16, 16, 32, 64, 128, 256, 512, 1024), width_multipliers: Tuple[float, ...] | float = (0.5, 0.625, 0.75, 1.0, 1.25, 1.5, 2.0), expand_ratios: Tuple[float, ...] = (1.0, 2.0, 3.0, 4.0, 5.0, 6.0), squeeze_excite: Tuple[Literal['force', 'optional', 'none'], ...] = ('none', 'none', 'optional', 'none', 'optional', 'optional'), depth_range: List[Tuple[int, int]] | Tuple[int, int] = (1, 4), stride: Tuple[int, ...] = (2, 1, 2, 2, 2, 1, 2, 1, 1), activation: Tuple[Literal['hswish', 'swish', 'relu'], ...] = ('hswish', 'relu', 'relu', 'relu', 'hswish', 'hswish', 'hswish', 'hswish', 'hswish'), se_from_exp: bool = True, dropout_rate: float = 0.2, bn_eps: float = 0.001, bn_momentum: float = 0.1) -> None: ...
    def forward(self, x): ...
    @classmethod
    def fixed_arch(cls, arch: dict) -> FixedFactory: ...
    @classmethod
    def load_searched_model(cls, name: str, pretrained: bool = False, download: bool = False, progress: bool = True) -> nn.Module: ...
