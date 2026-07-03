import torch
from _typeshed import Incomplete
from dataclasses import dataclass
from nvfuser._C import DataType
from torch._prims_common import Number as Number, getnvFuserDtype as getnvFuserDtype, number_type as number_type
from torch.fx import GraphModule as GraphModule
from torch.fx.passes.infra.partitioner import CapabilityBasedPartitioner as CapabilityBasedPartitioner
from torch.utils._pytree import tree_flatten as tree_flatten, tree_map as tree_map, tree_unflatten as tree_unflatten

def get_nvprim_dump_nvtx(): ...

DEFAULT_NVFUSER_PYTHON_CONFIG: Incomplete

@dataclass(frozen=True)
class nvFuserTensorTemplate:
    symbolic_shape: tuple
    contiguity: tuple
    dtype: DataType
    is_cpu: bool
    def __init__(self, symbolic_shape, contiguity, dtype, is_cpu) -> None: ...

@dataclass(frozen=True)
class nvFuserScalarTemplate:
    dtype: DataType
    def __init__(self, dtype) -> None: ...

def compute_symbolic_shape(shape):
    """Computes the symbolic shape of a tensor.
    nvFuser specializes on size-1 dimensions as broadcasted dimensions.
    -1 is used to represent any size."""
def compute_contiguity(shape, strides):
    """Computes the contiguity information to simplify internal indexing.
    Contiguous dimensions are represented by True, strided dimensions
    are represented by False.
    """
def to_nvfuser_template_args(args): ...
def make_nvfuser_fusion(gm: GraphModule, *nv_args_templates): ...
def nvfuser_execute(gm: GraphModule, *args, executor_parameters: Incomplete | None = None): ...

class NvfuserPrimOperatorSupport(torch.fx.passes.operator_support.OperatorSupport):
    def is_node_supported(self, submodules, node: torch.fx.Node) -> bool: ...

class PartitionedInterpreter(torch.fx.Interpreter):
    def call_module(self, target, args, kwargs): ...

class NvfuserGraphModule(torch.nn.Module):
    gm: Incomplete
    executor_parameters: Incomplete
    def __init__(self, gm, use_python_fusion_cache) -> None: ...
    def __call__(self, *args): ...

def maybe_partition_graph(gm: GraphModule, allow_single_op_fusion: bool, use_python_fusion_cache: bool): ...

class NVTXInterpreter(torch.fx.Interpreter):
    def run_node(self, n): ...

def nvfuser_execute_partitioned(gm: GraphModule, *args, executor_parameters: Incomplete | None = None): ...
