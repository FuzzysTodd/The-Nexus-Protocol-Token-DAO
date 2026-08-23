from . import external_utils as external_utils
from .config_utils import install_config_module as install_config_module
from .logging import get_loggers_level as get_loggers_level, set_loggers_level as set_loggers_level
from _typeshed import Incomplete

log_level: Incomplete
output_code: bool
log_file_name: Incomplete
verbose: bool
output_graph_code: bool
verify_correctness: bool
minimum_call_count: int
dead_code_elimination: bool
cache_size_limit: int
specialize_int_float: bool
constant_functions: Incomplete
dynamic_shapes: Incomplete
guard_nn_modules: bool
traceable_tensor_subclasses: Incomplete
suppress_errors: Incomplete
replay_record_enabled: Incomplete
rewrite_assert_with_torch_assert: bool
print_graph_breaks: bool
disable: Incomplete
skipfiles_inline_module_allowlist: Incomplete
allowed_functions_module_string_ignorelist: Incomplete
repro_after: Incomplete
repro_level: Incomplete
repro_forward_only: Incomplete
repro_tolerance: float
capture_scalar_outputs: bool
enforce_cond_guards_match: bool
optimize_ddp: bool
raise_on_ctx_manager_usage: bool
raise_on_unsafe_aot_autograd: bool
raise_on_backend_change: bool
error_on_nested_fx_trace: bool
allow_rnn: bool
base_dir: Incomplete

def is_fbcode(): ...

debug_dir_root: Incomplete
DO_NOT_USE_legacy_non_fake_example_inputs: bool
