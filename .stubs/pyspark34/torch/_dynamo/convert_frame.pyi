from . import config as config, exc as exc
from .allowed_functions import is_allowed as is_allowed
from .backends.registry import CompilerFn as CompilerFn
from .bytecode_analysis import remove_dead_code as remove_dead_code, remove_pointless_jumps as remove_pointless_jumps
from .bytecode_transformation import is_generator as is_generator, transform_code_object as transform_code_object
from .eval_frame import TorchPatcher as TorchPatcher, always_optimize_code_objects as always_optimize_code_objects, skip_code as skip_code
from .exc import BackendCompilerFailed as BackendCompilerFailed, InternalTorchDynamoError as InternalTorchDynamoError, TorchRuntimeError as TorchRuntimeError, Unsupported as Unsupported, augment_exc_message as augment_exc_message, format_error_msg as format_error_msg, unimplemented as unimplemented
from .guards import CheckFunctionManager as CheckFunctionManager, GuardedCode as GuardedCode
from .hooks import Hooks as Hooks
from .output_graph import OutputGraph as OutputGraph
from .replay_record import ExecutionRecord as ExecutionRecord
from .symbolic_convert import InstructionTranslator as InstructionTranslator
from .utils import CleanupManager as CleanupManager, counters as counters, dynamo_timed as dynamo_timed, format_bytecode as format_bytecode, gen_record_file_name as gen_record_file_name, guard_failures as guard_failures, increment_frame as increment_frame, init_logging as init_logging, is_namedtuple as is_namedtuple, istype as istype, orig_code_map as orig_code_map, troubleshooting_url as troubleshooting_url, write_record_to_file as write_record_to_file
from _typeshed import Incomplete

log: Incomplete

class Tracker:
    seen: Incomplete
    seen_ids: Incomplete
    def __init__(self) -> None: ...
    def add(self, strong_obj): ...
    def __contains__(self, item) -> bool: ...
    def clear(self) -> None: ...

input_codes: Incomplete
output_codes: Incomplete
initial_grad_state: Incomplete

def fx_forward_from_src_skip_result(*args, **kwargs): ...
def wrap_convert_context(fn):
    """
    Context manager to:
        1) Save/restore torch random state
        2) Save/restore torch.is_grad_enabled() state
        3) Monkey patch torch.fx.graph_module._forward_from_src
    """
def has_tensor_in_frame(frame):
    """Check if the frame has torch.* related bits"""
def exception_handler(e, code, frame: Incomplete | None = None) -> None: ...
def convert_frame_assert(compiler_fn: CompilerFn, one_graph: bool = True, export: bool = False):
    """Fully convert a frame into an FX graph"""
def convert_frame(compiler_fn: CompilerFn, hooks: Hooks):
    """Try to convert a frame into an FX graph, if error leave frame unmodified"""
def replay(filename) -> None: ...
