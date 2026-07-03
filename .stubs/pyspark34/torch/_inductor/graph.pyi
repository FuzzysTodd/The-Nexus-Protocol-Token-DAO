import torch
import torch.fx
from . import config as config, ir as ir
from .codegen.wrapper import CppWrapperCodeGen as CppWrapperCodeGen, WrapperCodeGen as WrapperCodeGen
from .exc import LoweringException as LoweringException, MissingOperatorWithDecomp as MissingOperatorWithDecomp, MissingOperatorWithoutDecomp as MissingOperatorWithoutDecomp
from .ir import Constant as Constant, FixedLayout as FixedLayout, InputBuffer as InputBuffer, Pointwise as Pointwise, Reduction as Reduction, TensorBox as TensorBox
from .lowering import FALLBACK_ALLOW_LIST as FALLBACK_ALLOW_LIST, layout_constraints as layout_constraints, lowerings as lowerings, make_fallback as make_fallback, needs_realized_inputs as needs_realized_inputs
from .sizevars import CppSizeVarAllocator as CppSizeVarAllocator, SizeVarAllocator as SizeVarAllocator
from .utils import convert_shape_to_inductor as convert_shape_to_inductor, gather_origins as gather_origins, get_dtype_size as get_dtype_size, sympy_product as sympy_product
from .virtualized import V as V
from _typeshed import Incomplete
from torch._decomp import get_decompositions as get_decompositions
from torch._dynamo.utils import dynamo_timed as dynamo_timed
from torch.fx.experimental.symbolic_shapes import ShapeEnv as ShapeEnv
from torch.utils._mode_utils import no_dispatch as no_dispatch

log: Incomplete

def supported_dtype_of_cpp_wrapper(dtype): ...

class GraphLowering(torch.fx.Interpreter):
    def symbolic_sizes_strides(self, ex: torch.Tensor):
        """
        Support dynamic shapes and dynamic strides by assigning variables
        to each dimension.  We duck-shape tensors, so if two tensors
        have the same size they get assigned the same symbolic variable.
        """
    def static_sizes_strides(self, ex: torch.Tensor):
        """
        Primarily used to weights
        """
    reuse_shape_env: bool
    sizevars: Incomplete
    graph_inputs: Incomplete
    graph_inputs_original: Incomplete
    graph_outputs: Incomplete
    device_types: Incomplete
    buffers: Incomplete
    constants: Incomplete
    removed_buffers: Incomplete
    inplaced_to_remove: Incomplete
    wrapper_code: Incomplete
    num_static_inputs: Incomplete
    mutated_inputs: Incomplete
    unaligned_buffers: Incomplete
    randomness_offset: Incomplete
    randomness_seeds: Incomplete
    name_to_buffer: Incomplete
    creation_time: Incomplete
    name: str
    graph_id: Incomplete
    scheduler: Incomplete
    def __init__(self, gm: torch.fx.GraphModule, shape_env: Incomplete | None = None, num_static_inputs: Incomplete | None = None, graph_id: Incomplete | None = None) -> None: ...
    def warn_fallback(self, name) -> None: ...
    @property
    def fake_mode(self): ...
    def get_dtype(self, buffer_name: str): ...
    def random_seed_buffer(self, device: torch.device):
        """
        Return a device-unique 1-element tensor storing our RNG seed.
        This will get initialized at the start of each graph in
        `wrapper.py`.

        Note this is only used by cuda backends.  The CPU backend handles
        RNG seeds as a sizevar.
        """
    def increment_randomness_offset(self, numel):
        """
        A global counter of how many random numbers we have handed out so far.
        """
    def run(self, *args): ...
    def disable_cpp_wrapper(self, cond) -> None: ...
    def check_buffer_for_cpp_wrapper(self, buffer: ir.ComputedBuffer): ...
    def register_buffer(self, buffer: ir.ComputedBuffer): ...
    def realize_users_of(self, name: str):
        """
        When a buffer is mutated we need to make sure all the reads to
        the old version are realized before the mutation happens.
        """
    def add_tensor_constant(self, data): ...
    def constant_name(self, name: str, device_override: torch.device):
        """
        We AOT copy constants to the devices they are needed on.
        If device_override doesn't match the constant's device, then
        copy it and return a different name.
        """
    def placeholder(self, target: str, args, kwargs): ...
    def call_function(self, target, args, kwargs): ...
    def get_attr(self, target, args, kwargs): ...
    def call_module(self, target, args, kwargs) -> None: ...
    def call_method(self, target, args, kwargs) -> None: ...
    def output(self, target, args, kwargs) -> None: ...
    def finalize(self) -> None: ...
    def run_node(self, n: torch.fx.Node): ...
    def check_platform(self) -> None: ...
    def check_profiler_mark_wrapper_call(self) -> None: ...
    def check_device_for_cpp_buffer(self) -> None: ...
    def check_input_for_cpp_buffer(self) -> None: ...
    def check_constant_for_cpp_buffer(self) -> None: ...
    def check_cpp_wrapper(self) -> None: ...
    def init_wrapper_code(self) -> None: ...
    def codegen(self): ...
    def count_bytes(self): ...
    def compile_to_module(self): ...
    def compile_to_fn(self): ...
    def get_output_names(self): ...
    def is_unspec_arg(self, name: str): ...
