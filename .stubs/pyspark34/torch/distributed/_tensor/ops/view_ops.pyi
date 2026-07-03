import torch
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import Tensor as Tensor
from torch.distributed._tensor.api import Shard as Shard
from torch.distributed._tensor.op_schema import OpSchema as OpSchema, OutputSharding as OutputSharding
from torch.distributed._tensor.ops.utils import normalize_dim as normalize_dim, normalize_dims as normalize_dims, prod as prod, register_prop_rule as register_prop_rule
from torch.distributed._tensor.placement_types import DTensorSpec as DTensorSpec, Placement as Placement, Replicate as Replicate
from typing import Callable, Dict, Iterable, Sequence, Tuple

aten: Incomplete
Shape = Tuple[int, ...]

@dataclass
class DimSpec:
    """Specifies how an output dimension maps to an input dimension."""
    def inputs(self) -> Iterable['DimSpec']: ...
DimMap = Tuple[DimSpec, ...]

@dataclass
class Singleton(DimSpec):
    """Output dimension is a singleton"""

@dataclass
class InputDim(DimSpec):
    """Output dimension maps directly to an input dimension."""
    input_dim: int
    def __init__(self, input_dim) -> None: ...

@dataclass
class Broadcast(DimSpec):
    """Output is the broadcast of a singleton input dimension."""
    dim: DimSpec
    dim_size: int
    @classmethod
    def new(cls, dim: DimSpec, dim_size: int) -> DimSpec: ...
    def inputs(self) -> Iterable[DimSpec]: ...
    def __init__(self, dim, dim_size) -> None: ...

@dataclass
class NewDim(DimSpec):
    """This is a new dimension created by the op."""
    size: int
    @classmethod
    def new(cls, size: int) -> DimSpec: ...
    def __init__(self, size) -> None: ...

@dataclass
class Repeat(DimSpec):
    """Output dimension is the input dimension repeated n-times."""
    input_dim: DimSpec
    times: int
    @classmethod
    def new(cls, dim: DimSpec, times: int) -> DimSpec: ...
    def inputs(self) -> Iterable[DimSpec]: ...
    def __init__(self, input_dim, times) -> None: ...

@dataclass
class Flatten(DimSpec):
    """
    Output dimension is a set of input dimensions flattened, keeping
    right-most adjacent elements adjacent in the output.
    """
    input_dims: Sequence[DimSpec]
    @classmethod
    def new(cls, dims: Sequence[DimSpec]) -> DimSpec: ...
    def inputs(self) -> Iterable[DimSpec]: ...
    def __init__(self, input_dims) -> None: ...

@dataclass
class Split(DimSpec):
    """
    This dimension is a member of a decomposition of the input dim.
    Note that input_dim itself could be a Flattened set of input dims.
    """
    input_dim: DimSpec
    group_shape: Shape
    split_id: int
    @classmethod
    def new(cls, dim: DimSpec, group_shape: Tuple[int, ...], idx: int) -> DimSpec: ...
    def inputs(self) -> Iterable[DimSpec]: ...
    def __init__(self, input_dim, group_shape, split_id) -> None: ...

def dim_pad_left(ndim: int, min_dims: int) -> DimMap: ...
def dim_atleast_3d(ndim: int) -> DimMap: ...
def expand(input_shape: Shape, shape: Shape) -> DimMap:
    """Implements broadcast on multiple dimensions"""
def normalize_sizes(sizes: Shape | Tuple[Shape]) -> Shape: ...
def dim_flatten(ndim: int) -> DimMap: ...
def dim_movedim(ndim: int, input: int | Sequence[int], destination: int | Sequence[int]) -> DimMap: ...
def dim_repeat(ndim: int, sizes: Shape) -> DimMap: ...
def infer_size(total_size: int, sizes: Shape) -> Shape:
    '''
    One dimension input to view may be "-1".
    Infer the size of this dimension given the total_size.
    '''
def view_groups(from_size: Shape, to_size: Shape) -> DimMap:
    """
    A view or reshape operation can be decomposed into a set of 3 types of smaller operations:
    1) Forward a dimension from input to output
    2) Flatten a set of dimensions into a single dimension
    3) Split one dimension into multiple dimensions

    view_groups identifies these operations and returns, for each output dimension, what
    is operation was performed in the input dimension. For example:

        view_groups([2, 3, 4], [2, 12]) -> (
            InputDim(0),
            Flatten((InputDim(1), InputDim(2)))
        )

    - ouptut dimension 0 maps to input dimension 0
    - output dimension 1 maps to a flattened input dimensions 1 and 2


        view_groups([2, 3], [3, 2]) -> (
            Split(Flatten((InputDim(0), InputDim(1))), (3, 2), 0),
            Split(Flatten((InputDim(0), InputDim(1))), (3, 2), 1),
        )

    - in the above, input is flattened into a single dimension and then split
      into two separate dimensions with different sizes from the input.
    """
def dim_tile(ndim: int, dims: Tuple[int, ...]) -> DimMap: ...
def dim_transpose(ndim: int, dim1: int, dim2: int) -> DimMap: ...
def dim_squeeze(shape: Shape, dim: int | None = None) -> DimMap: ...
def dim_unsqueeze(ndim: int, dim: int) -> DimMap: ...
def dim_reduction(ndim: int, dim_or_dims: int | Sequence[int] | None, keepdim: bool) -> DimMap:
    """
    General fallback for reduction ops where _Partial() does not apply.
    This will cause incoming tensor to be replicated on the reducing dimensions.
    """

@dataclass
class Op:
    dim_map: Callable[..., DimMap]
    shape_argnum: int | None = ...
    def __init__(self, dim_map, shape_argnum) -> None: ...

ops: Dict[Callable[..., torch.Tensor], Op]

def propagate_shape_and_sharding(in_shard: Sequence[Placement], local_in_shape: Shape, rule: DimMap, mesh_sizes: Shape) -> Tuple[Shape, Sequence[Placement] | None, torch.Tensor]:
    """
    Takes as input the global shape of the tensor, and the input sharding,
    and produce corresponding output sharding and shape of the output tensor.

    Sharding propagation follows mapped dimensions:
    - An output dimension that maps directly to an input dimension is sharded equally
    - An output dimension that is a flattened set of input dimensions can only be
      sharded if only the leftmost flattened dimension is sharded.
    - An output dimension that is a split of the input dimension can only be sharded
      if the leftmost split size is divisible by the mesh dimension
    """
def register_prop_rule_map(aten_op_overload: torch._ops.OpOverload, local_op_name: Callable[..., torch.Tensor]) -> None: ...
