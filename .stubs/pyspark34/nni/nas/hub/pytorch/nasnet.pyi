import nni.nas.nn.pytorch as nn
import torch
from .utils.fixed import FixedFactory as FixedFactory
from .utils.pretrained import load_pretrained_weight as load_pretrained_weight
from _typeshed import Incomplete
from nni.nas import model_wrapper as model_wrapper
from nni.nas.oneshot.pytorch.supermodule.differentiable import DifferentiableMixedRepeat as DifferentiableMixedRepeat
from nni.nas.oneshot.pytorch.supermodule.sampling import PathSamplingRepeat as PathSamplingRepeat
from typing import List, Tuple
from typing_extensions import Literal

OPS: Incomplete

class ReLUConvBN(nn.Sequential):
    def __init__(self, C_in, C_out, kernel_size, stride, padding, affine: bool = True) -> None: ...

class DilConv(nn.Sequential):
    def __init__(self, C_in, C_out, kernel_size, stride, padding, dilation, affine: bool = True) -> None: ...

class SepConv(nn.Sequential):
    def __init__(self, C_in, C_out, kernel_size, stride, padding, affine: bool = True) -> None: ...

class DilSepConv(nn.Sequential):
    def __init__(self, C_in, C_out, kernel_size, stride, padding, dilation, affine: bool = True) -> None: ...

class Zero(nn.Module):
    stride: Incomplete
    def __init__(self, stride) -> None: ...
    def forward(self, x): ...

class FactorizedReduce(nn.Module):
    relu: Incomplete
    conv_1: Incomplete
    conv_2: Incomplete
    bn: Incomplete
    pad: Incomplete
    def __init__(self, C_in, C_out, affine: bool = True) -> None: ...
    def forward(self, x): ...

class DropPath_(nn.Module):
    drop_prob: Incomplete
    def __init__(self, drop_prob: float = 0.0) -> None: ...
    def forward(self, x): ...

class AuxiliaryHead(nn.Module):
    features: Incomplete
    classifier: Incomplete
    def __init__(self, C: int, num_labels: int, dataset: Literal['imagenet', 'cifar']) -> None: ...
    def forward(self, x): ...

class CellPreprocessor(nn.Module):
    """
    Aligning the shape of predecessors.

    If the last cell is a reduction cell, ``pre0`` should be ``FactorizedReduce`` instead of ``ReLUConvBN``.
    See :class:`CellBuilder` on how to calculate those channel numbers.
    """
    pre0: Incomplete
    pre1: Incomplete
    def __init__(self, C_pprev: nn.MaybeChoice[int], C_prev: nn.MaybeChoice[int], C: nn.MaybeChoice[int], last_cell_reduce: bool) -> None: ...
    def forward(self, cells): ...

class CellPostprocessor(nn.Module):
    """
    The cell outputs previous cell + this cell, so that cells can be directly chained.
    """
    def forward(self, this_cell, previous_cells): ...

class CellBuilder:
    '''The cell builder is used in Repeat.
    Builds an cell each time it\'s "called".
    Note that the builder is ephemeral, it can only be called once for every index.
    '''
    C_prev_in: Incomplete
    C_in: Incomplete
    C: Incomplete
    op_candidates: Incomplete
    num_nodes: Incomplete
    merge_op: Incomplete
    first_cell_reduce: Incomplete
    last_cell_reduce: Incomplete
    drop_path_prob: Incomplete
    num_predecessors: int
    num_ops_per_node: int
    def __init__(self, op_candidates: List[str], C_prev_in: nn.MaybeChoice[int], C_in: nn.MaybeChoice[int], C: nn.MaybeChoice[int], num_nodes: int, merge_op: Literal['all', 'loose_end'], first_cell_reduce: bool, last_cell_reduce: bool, drop_path_prob: float) -> None: ...
    def op_factory(self, node_index: int, op_index: int, input_index: int | None, *, op: str, channels: int, is_reduction_cell: bool): ...
    def __call__(self, repeat_idx: int): ...

class NDSStage(nn.Repeat):
    """This class defines NDSStage, a special type of Repeat, for isinstance check, and shape alignment.

    In NDS, we can't simply use Repeat to stack the blocks,
    because the output shape of each stacked block can be different.
    This is a problem for one-shot strategy because they assume every possible candidate
    should return values of the same shape.

    Therefore, we need :class:`NDSStagePathSampling` and :class:`NDSStageDifferentiable`
    to manually align the shapes -- specifically, to transform the first block in each stage.

    This is not required though, when depth is not changing, or the mutable depth causes no problem
    (e.g., when the minimum depth is large enough).

    .. attention::

       Assumption: Loose end is treated as all in ``merge_op`` (the case in one-shot),
       which enforces reduction cell and normal cells in the same stage to have the exact same output shape.
    """
    estimated_out_channels_prev: int
    estimated_out_channels: int
    downsampling: bool
    def first_cell_transformation_factory(self) -> nn.Module | None:
        '''To make the "previous cell" in first cell\'s output have the same shape as cells in this stage.'''

class NDSStagePathSampling(PathSamplingRepeat):
    """The path-sampling implementation (for one-shot) of each NDS stage if depth is mutating."""
    @classmethod
    def mutate(cls, module, name, memo, mutate_kwargs): ...
    first_cell_transformation: Incomplete
    def __init__(self, first_cell_transformation: nn.Module | None, *args, **kwargs) -> None: ...
    def reduction(self, items: List[Tuple[torch.Tensor, torch.Tensor]], sampled: List[int]) -> Tuple[torch.Tensor, torch.Tensor]: ...

class NDSStageDifferentiable(DifferentiableMixedRepeat):
    """The differentiable implementation (for one-shot) of each NDS stage if depth is mutating."""
    @classmethod
    def mutate(cls, module, name, memo, mutate_kwargs): ...
    first_cell_transformation: Incomplete
    def __init__(self, first_cell_transformation: nn.Module | None, *args, **kwargs) -> None: ...
    def reduction(self, items: List[Tuple[torch.Tensor, torch.Tensor]], weights: List[float], depths: List[int]) -> Tuple[torch.Tensor, torch.Tensor]: ...

class NDS(nn.Module):
    __doc__: Incomplete
    dataset: Incomplete
    num_labels: Incomplete
    auxiliary_loss: Incomplete
    drop_path_prob: Incomplete
    num_cells: Incomplete
    stem0: Incomplete
    stem1: Incomplete
    stem: Incomplete
    stages: Incomplete
    auxiliary_head: Incomplete
    global_pooling: Incomplete
    classifier: Incomplete
    def __init__(self, op_candidates: List[str], merge_op: Literal['all', 'loose_end'] = 'all', num_nodes_per_cell: int = 4, width: Tuple[int, ...] | int = 16, num_cells: Tuple[int, ...] | int = 20, dataset: Literal['cifar', 'imagenet'] = 'imagenet', auxiliary_loss: bool = False, drop_path_prob: float = 0.0) -> None: ...
    def forward(self, inputs): ...
    def set_drop_path_prob(self, drop_prob) -> None:
        """
        Set the drop probability of Drop-path in the network.
        Reference: `FractalNet: Ultra-Deep Neural Networks without Residuals <https://arxiv.org/pdf/1605.07648v4.pdf>`__.
        """
    @classmethod
    def fixed_arch(cls, arch: dict) -> FixedFactory: ...

class NASNet(NDS):
    __doc__: Incomplete
    NASNET_OPS: Incomplete
    def __init__(self, width: Tuple[int, ...] | int = (16, 24, 32), num_cells: Tuple[int, ...] | int = (4, 8, 12, 16, 20), dataset: Literal['cifar', 'imagenet'] = 'cifar', auxiliary_loss: bool = False, drop_path_prob: float = 0.0) -> None: ...

class ENAS(NDS):
    __doc__: Incomplete
    ENAS_OPS: Incomplete
    def __init__(self, width: Tuple[int, ...] | int = (16, 24, 32), num_cells: Tuple[int, ...] | int = (4, 8, 12, 16, 20), dataset: Literal['cifar', 'imagenet'] = 'cifar', auxiliary_loss: bool = False, drop_path_prob: float = 0.0) -> None: ...

class AmoebaNet(NDS):
    __doc__: Incomplete
    AMOEBA_OPS: Incomplete
    def __init__(self, width: Tuple[int, ...] | int = (16, 24, 32), num_cells: Tuple[int, ...] | int = (4, 8, 12, 16, 20), dataset: Literal['cifar', 'imagenet'] = 'cifar', auxiliary_loss: bool = False, drop_path_prob: float = 0.0) -> None: ...

class PNAS(NDS):
    __doc__: Incomplete
    PNAS_OPS: Incomplete
    def __init__(self, width: Tuple[int, ...] | int = (16, 24, 32), num_cells: Tuple[int, ...] | int = (4, 8, 12, 16, 20), dataset: Literal['cifar', 'imagenet'] = 'cifar', auxiliary_loss: bool = False, drop_path_prob: float = 0.0) -> None: ...

class DARTS(NDS):
    __doc__: Incomplete
    DARTS_OPS: Incomplete
    def __init__(self, width: Tuple[int, ...] | int = (16, 24, 32), num_cells: Tuple[int, ...] | int = (4, 8, 12, 16, 20), dataset: Literal['cifar', 'imagenet'] = 'cifar', auxiliary_loss: bool = False, drop_path_prob: float = 0.0) -> None: ...
    @classmethod
    def load_searched_model(cls, name: str, pretrained: bool = False, download: bool = False, progress: bool = True) -> nn.Module: ...
