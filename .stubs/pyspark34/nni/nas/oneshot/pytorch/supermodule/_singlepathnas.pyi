import torch.nn as nn
from _typeshed import Incomplete
from collections.abc import Generator
from nni.nas.nn.pytorch import ValueChoice as ValueChoice

class DifferentiableSuperConv2d(nn.Conv2d):
    """
    Only ``kernel_size`` ``in_channels`` and ``out_channels`` are supported. Kernel size candidates should be larger or smaller
    than each other in both candidates. See examples below:
    the following example is not allowed:
        >>> ValueChoice(candidates = [(5, 3), (3, 5)])
            □ ■ ■ ■ □   □ □ □ □ □
            □ ■ ■ ■ □   ■ ■ ■ ■ ■    # candidates are not bigger or smaller on both dimension
            □ ■ ■ ■ □   ■ ■ ■ ■ ■
            □ ■ ■ ■ □   ■ ■ ■ ■ ■
            □ ■ ■ ■ □   □ □ □ □ □
    the following 3 examples are valid:
        >>> ValueChoice(candidates = [5, 3, 1])
            ■ ■ ■ ■ ■   □ □ □ □ □   □ □ □ □ □
            ■ ■ ■ ■ ■   □ ■ ■ ■ □   □ □ □ □ □
            ■ ■ ■ ■ ■   □ ■ ■ ■ □   □ □ ■ □ □
            ■ ■ ■ ■ ■   □ ■ ■ ■ □   □ □ □ □ □
            ■ ■ ■ ■ ■   □ □ □ □ □   □ □ □ □ □
        >>> ValueChoice(candidates = [(5, 7), (3, 5), (1, 3)])
            ■ ■ ■ ■ ■ ■ ■  □ □ □ □ □ □ □   □ □ □ □ □ □ □
            ■ ■ ■ ■ ■ ■ ■  □ ■ ■ ■ ■ ■ □   □ □ □ □ □ □ □
            ■ ■ ■ ■ ■ ■ ■  □ ■ ■ ■ ■ ■ □   □ □ ■ ■ ■ □ □
            ■ ■ ■ ■ ■ ■ ■  □ ■ ■ ■ ■ ■ □   □ □ □ □ □ □ □
            ■ ■ ■ ■ ■ ■ ■  □ □ □ □ □ □ □   □ □ □ □ □ □ □
        >>> # when the difference between any two candidates is not even, the left upper will be picked:
        >>> ValueChoice(candidates = [(5, 5), (4, 4), (3, 3)])
            ■ ■ ■ ■ ■   ■ ■ ■ ■ □   □ □ □ □ □
            ■ ■ ■ ■ ■   ■ ■ ■ ■ □   □ ■ ■ ■ □
            ■ ■ ■ ■ ■   ■ ■ ■ ■ □   □ ■ ■ ■ □
            ■ ■ ■ ■ ■   ■ ■ ■ ■ □   □ ■ ■ ■ □
            ■ ■ ■ ■ ■   □ □ □ □ □   □ □ □ □ □
    """
    label: Incomplete
    out_channel_candidates: Incomplete
    kernel_size_candidates: Incomplete
    def __init__(self, module, name) -> None: ...
    def forward(self, input): ...
    def parameters(self) -> Generator[Incomplete, None, None]: ...
    def named_parameters(self) -> Generator[Incomplete, None, None]: ...
    def export(self):
        """
        result = {
            'kernel_size': i,
            'out_channels': j
        }
        which means the best candidate for an argument is the i-th one if candidates are sorted in descending order
        """
    @staticmethod
    def Lasso_sigmoid(matrix, t):
        """
        A trick that can make use of both the value of bool(lasso > t) and the gradient of sigmoid(lasso - t)

        Parameters
        ----------
        matrix : Tensor
            the matrix to calculate lasso norm
        t : float
            the threshold
        """
    alpha: Incomplete
    t_kernel: Incomplete
    kernel_masks: Incomplete
    t_expansion: Incomplete
    channel_masks: Incomplete
    def generate_architecture_params(self) -> None: ...

class DifferentiableBatchNorm2d(nn.BatchNorm2d):
    label: Incomplete
    alpha: Incomplete
    def __init__(self, module, name) -> None: ...
    def export(self):
        """
        No need to export ``BatchNorm2d``. Refer to the ``Conv2d`` layer that has the ``ValueChoice`` as ``out_channels``.
        """
