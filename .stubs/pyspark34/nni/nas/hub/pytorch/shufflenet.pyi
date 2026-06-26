import nni.nas.nn.pytorch as nn
from .utils.fixed import FixedFactory as FixedFactory
from .utils.pretrained import load_pretrained_weight as load_pretrained_weight
from _typeshed import Incomplete
from nni.nas import model_wrapper as model_wrapper

class ShuffleNetBlock(nn.Module):
    """
    Describe the basic building block of shuffle net, as described in
    `ShuffleNet: An Extremely Efficient Convolutional Neural Network for Mobile Devices <https://arxiv.org/pdf/1707.01083.pdf>`__.

    When stride = 1, the block expects an input with ``2 * input channels``. Otherwise input channels.
    """
    channels: Incomplete
    in_channels: Incomplete
    out_channels: Incomplete
    mid_channels: Incomplete
    kernel_size: Incomplete
    stride: Incomplete
    pad: Incomplete
    oup_main: Incomplete
    affine: Incomplete
    branch_main: Incomplete
    branch_proj: Incomplete
    def __init__(self, in_channels: int, out_channels: int, mid_channels: nn.MaybeChoice[int], *, kernel_size: int, stride: int, sequence: str = 'pdp', affine: bool = True) -> None: ...
    def forward(self, x): ...

class ShuffleXceptionBlock(ShuffleNetBlock):
    """
    The ``choice_x`` version of shuffle net block, described in
    `Single Path One-shot <https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123610528.pdf>`__.
    """
    def __init__(self, in_channels: int, out_channels: int, mid_channels: nn.MaybeChoice[int], *, stride: int, affine: bool = True) -> None: ...

class ShuffleNetSpace(nn.Module):
    '''
    The search space proposed in `Single Path One-shot <https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123610528.pdf>`__.

    The basic building block design is inspired by a state-of-the-art manually-designed network --
    `ShuffleNetV2 <https://openaccess.thecvf.com/content_ECCV_2018/html/Ningning_Light-weight_CNN_Architecture_ECCV_2018_paper.html>`__.
    There are 20 choice blocks in total. Each choice block has 4 candidates, namely ``choice 3``, ``choice 5``,
    ``choice_7`` and ``choice_x`` respectively. They differ in kernel sizes and the number of depthwise convolutions.
    The size of the search space is :math:`4^{20}`.

    Parameters
    ----------
    num_labels : int
        Number of classes for the classification head. Default: 1000.
    channel_search : bool
        If true, for each building block, the number of ``mid_channels``
        (output channels of the first 1x1 conv in each building block) varies from 0.2x to 1.6x (quantized to multiple of 0.2).
        Here, "k-x" means k times the number of default channels.
        Otherwise, 1.0x is used by default. Default: false.
    affine : bool
        Apply affine to all batch norm. Default: true.
    '''
    num_labels: Incomplete
    channel_search: Incomplete
    affine: Incomplete
    stage_repeats: Incomplete
    stage_out_channels: Incomplete
    first_conv: Incomplete
    features: Incomplete
    conv_last: Incomplete
    globalpool: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, num_labels: int = 1000, channel_search: bool = False, affine: bool = True) -> None: ...
    def forward(self, x): ...
    @classmethod
    def fixed_arch(cls, arch: dict) -> FixedFactory: ...
    @classmethod
    def load_searched_model(cls, name: str, pretrained: bool = False, download: bool = False, progress: bool = True) -> nn.Module: ...
