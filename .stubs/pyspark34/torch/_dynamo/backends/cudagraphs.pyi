from .common import aot_autograd as aot_autograd
from .registry import register_backend as register_backend
from _typeshed import Incomplete
from torch.fx import GraphModule as GraphModule
from torch.fx.passes.backends.cudagraphs import partition_cudagraphs as partition_cudagraphs
from torch.multiprocessing.reductions import StorageWeakRef as StorageWeakRef
from torch.nn import Module as Module
from torch.utils._pytree import tree_map as tree_map
from typing import Set

log: Incomplete

def cloner(t): ...

class CudaGraphModule(Module):
    gm: GraphModule
    mutated_inputs: Set[int]
    def __init__(self, gm, mutated_inputs) -> None: ...
    warmed_up: bool
    graph: Incomplete
    static_inputs: Incomplete
    static_outputs: Incomplete
    def __call__(self, *args): ...

def find_input_mutations(g): ...
def apply_cuda_graphs(gm) -> None: ...
def cudagraphs(model, inputs): ...

aot_cudagraphs: Incomplete

def cudagraphs_inner(model, inputs, copy_outputs: bool = True):
    """This isn't registered as a backend, but is used in some benchmarks"""
