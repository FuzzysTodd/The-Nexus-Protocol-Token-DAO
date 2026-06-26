import torch
import torch.nn
import traceback
from . import config as config, variables as variables
from .backends.registry import CompiledFn as CompiledFn, CompilerFn as CompilerFn
from .bytecode_transformation import Instruction as Instruction, create_instruction as create_instruction, unique_id as unique_id
from .codegen import PyCodegen as PyCodegen
from .exc import BackendCompilerFailed as BackendCompilerFailed, unimplemented as unimplemented
from .guards import GuardBuilder as GuardBuilder
from .mutation_guard import is_dynamic_nn_module as is_dynamic_nn_module
from .side_effects import SideEffects as SideEffects
from .source import ConstantSource as ConstantSource, LocalInputSource as LocalInputSource, LocalSource as LocalSource, ShapeEnvSource as ShapeEnvSource, is_constant_source as is_constant_source
from .utils import CleanupHook as CleanupHook, assert_no_fake_params_or_buffers as assert_no_fake_params_or_buffers, checkpoint_params as checkpoint_params, clone_inputs as clone_inputs, count_calls as count_calls, counters as counters, dynamo_timed as dynamo_timed, format_graph_tabular as format_graph_tabular, same as same
from .variables.base import VariableTracker as VariableTracker
from .variables.builder import GraphArg as GraphArg, TrackedFake as TrackedFake, VariableBuilder as VariableBuilder, wrap_fx_proxy as wrap_fx_proxy
from .variables.nn_module import NNModuleVariable as NNModuleVariable
from .variables.tensor import SymNodeVariable as SymNodeVariable, TensorVariable as TensorVariable, UnspecializedPythonVariable as UnspecializedPythonVariable
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import fx as fx
from torch._guards import Checkpointable as Checkpointable, Guard as Guard, GuardsCheckpointState as GuardsCheckpointState, TracingContext as TracingContext, tracing as tracing
from torch.fx.experimental.symbolic_shapes import ShapeEnv as ShapeEnv
from typing import Any, Dict, List, NamedTuple, Set

log: Incomplete

class OutputGraphState(NamedTuple):
    graphargs: List[GraphArg]
    tracked_fakes: List[TrackedFake]
    guard_state: GuardsCheckpointState
    nn_modules: Dict[str, torch.nn.Module] | None
    side_effects: SideEffects
    timestamp: int
    def diff(self, other: OutputGraphState, *, prefix: str = '') -> str | None: ...
    @property
    def guards(self): ...

@dataclass
class GraphCompileReason:
    """Stores why a given output graph was compiled; i.e. what caused the graph break."""
    reason: str
    user_stack: List[traceback.FrameSummary]
    def __init__(self, reason, user_stack) -> None: ...

class FakeRootModule(torch.nn.Module):
    """Trick the constructor of fx.GraphModule"""
    def __init__(self, nn_modules: Dict[str, torch.nn.Module]) -> None: ...

class WrapperBackend:
    backend: Incomplete
    original_example_inputs: Incomplete
    def __init__(self, backend: CompilerFn, original_example_inputs) -> None: ...
    @property
    def example_inputs(self): ...
    restore: Incomplete
    gm: Incomplete
    candidate: Incomplete
    def __call__(self, gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]): ...

class OutputGraph(fx.Tracer, Checkpointable[OutputGraphState]):
    """
    Wrapper class to hold outputs of InstructionTranslator.  Mainly the
    generated fx.Graph.
    """
    graph: Incomplete
    graphargs: Incomplete
    tracing_context: Incomplete
    tracked_fakes: Incomplete
    orig_graphargs: Incomplete
    nn_modules: Incomplete
    side_effects: Incomplete
    code_options: Incomplete
    output_instructions: Incomplete
    timestamp: int
    real_value_cache: Incomplete
    compiler_fn: Incomplete
    root_globals: Incomplete
    root_tx: Incomplete
    cleanups: Incomplete
    should_exit: bool
    random_values_var: Incomplete
    initial_random_state: Incomplete
    unspec_variable_map: Incomplete
    pos_to_arg: Incomplete
    name_to_input: Incomplete
    def __init__(self, f_globals: Dict[str, Any], code_options: Dict[str, Any], compiler_fn: CompilerFn, root_tx) -> None: ...
    @property
    def output(self): ...
    @property
    def fake_mode(self): ...
    @property
    def shape_env(self): ...
    @property
    def guards(self) -> Set[Guard]: ...
    def push_tx(self, tx) -> None: ...
    def pop_tx(self): ...
    @property
    def current_tx(self): ...
    def copy_graphstate(self) -> OutputGraphState:
        """Create a checkpoint of the current state by copying everything"""
    def restore_graphstate(self, state: OutputGraphState):
        """Restore a checkpoint created by self.copy_graphstate()"""
    def add_grapharg(self, arg: GraphArg): ...
    def count_calls(self): ...
    def get_submodule(self, keys): ...
    def create_graph_input(self, name, type_expr: Incomplete | None = None): ...
    def new_var(self, name: str = 'tmp'): ...
    def update_co_names(self, name) -> None:
        """Ensure self.code_options.co_names contains name"""
    def register_attr_or_module(self, target: torch.nn.Module | torch.Tensor | Any, *names, **options): ...
    partial_convert: Incomplete
    compile_subgraph_reason: Incomplete
    def compile_subgraph(self, tx, partial_convert: bool = False, reason: GraphCompileReason | None = None):
        """
        Generate a subgraph to continue execution on user code.
        Automatically restore live variables.
        """
    def compile_and_call_fx_graph(self, tx, rv, root):
        """
        Generate code from self.graph and return the Instruction()s to
        call that generated code.
        """
    def call_user_compiler(self, gm: fx.GraphModule) -> CompiledFn: ...
    def fake_example_inputs(self) -> List[torch.Tensor]: ...
    def example_inputs(self) -> List[torch.Tensor]: ...
    def remove_unused_graphargs(self) -> None: ...
    def add_output_instructions(self, prefix: List[Instruction]) -> None:
        """
        We call this on the creation of a new compiled subgraph that is inserted
        before user code.
        """
    def install_global(self, name, value) -> None: ...
    def cleanup(self) -> None: ...
    def create_proxy(self, kind, target, args, kwargs, name: Incomplete | None = None, type_expr: Incomplete | None = None, proxy_factory_fn: Incomplete | None = None): ...
    def create_node(self, *args, **kwargs): ...
    def remove_node(self, node) -> None: ...
