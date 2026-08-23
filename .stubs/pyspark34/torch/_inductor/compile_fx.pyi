import dataclasses
import torch
import torch.fx
from . import config as config, metrics as metrics, overrides as overrides, pattern_matcher as pattern_matcher
from .._dynamo.backends.common import aot_autograd as aot_autograd
from .debug import DebugContext as DebugContext
from .decomposition import select_decomp_table as select_decomp_table
from .graph import GraphLowering as GraphLowering
from .mkldnn import convert_outplace_to_inplace as convert_outplace_to_inplace
from .utils import developer_warning as developer_warning, get_dtype_size as get_dtype_size, has_incompatible_cudagraph_ops as has_incompatible_cudagraph_ops
from .virtualized import V as V
from _typeshed import Incomplete
from torch._dynamo.utils import fake_mode_from_tensors as fake_mode_from_tensors
from torch._functorch.aot_autograd import make_boxed_func as make_boxed_func
from torch._subclasses.fake_tensor import FakeTensor as FakeTensor
from typing import Any, Dict, List

log: Incomplete
ALIGNMENT: int

@dataclasses.dataclass
class BoxedBool:
    value: bool
    def __bool__(self) -> bool: ...
    @staticmethod
    def disable(obj): ...
    def __init__(self, value) -> None: ...

def get_expanded_dims(t): ...
def index_expanded_dims(t, expanded_dims): ...
def complex_memory_overlap(t): ...
def is_tf32_warning_applicable(gm: torch.fx.GraphModule): ...
def count_bytes_inner(gm, example_inputs, num_fixed: int = 0, **kwargs): ...
def compile_fx_inner(gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor], cudagraphs: Incomplete | None = None, num_fixed: int = 0, is_backward: bool = False, graph_id: Incomplete | None = None): ...
def clone_preserve_strides(x): ...
def align_inputs(model, inputs, static_input_idxs=()): ...
def cudagraphify(model, inputs, static_input_idxs=()): ...
def remove_unaligned_input_idxs(inputs, static_input_idxs):
    """
    We require all inputs to be aligned, so introduce a copy for any
    that aren't.
    """
def cudagraphify_impl(model, inputs, static_input_idxs=()):
    """
    Assumes inputs[static_input_idxs[i]] are always the same memory address
    """
def count_tangents(fx_g: torch.fx.GraphModule):
    """
    Infers which inputs are static for a backwards graph
    """
def compile_fx(model_: torch.fx.GraphModule, example_inputs_: List[torch.Tensor], inner_compile=..., config_patches: Dict[str, Any] | None = None):
    """Main entrypoint to a compile given FX graph"""
