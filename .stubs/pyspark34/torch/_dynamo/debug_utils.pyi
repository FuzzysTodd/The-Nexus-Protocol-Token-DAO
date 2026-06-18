from . import config as config
from .backends.registry import lookup_backend as lookup_backend, register_debug_backend as register_debug_backend
from .utils import clone_inputs as clone_inputs, get_debug_dir as get_debug_dir
from _typeshed import Incomplete
from torch._prims_common import is_float_dtype as is_float_dtype

log: Incomplete
inductor_config: Incomplete
use_buck: Incomplete
extra_deps: Incomplete
extra_imports: str

class BuckTargetWriter:
    target: Incomplete
    path: Incomplete
    cmd_line_path: Incomplete
    def __init__(self, filename) -> None: ...
    def build(self): ...
    def write(self, print_msg: bool = True): ...

def minifier_dir(): ...

class NNModuleToString:
    safe_reprs: Incomplete
    @staticmethod
    def can_convert_to_string(gm): ...
    @staticmethod
    def convert(gm): ...

def generate_config_string(): ...

TEST_REPLACEABLE_COMMENT: str

def generate_compiler_repro_string(gm, args): ...

INDUCTOR_IMPORT: str
COMPILER_REPRO_OPTIONS: Incomplete

def dump_compiler_graph_state(gm, args, compiler_name) -> None: ...
def save_graph_repro(fd, gm, args, compiler_name) -> None: ...
def isolate_fails(fx_g, args, compiler_name: str, env: Incomplete | None = None, patch_code: Incomplete | None = None): ...
def inductor_fails(fx_g, args, check_str: Incomplete | None = None): ...
def inductor_accuracy_fails(fx_g, args, check_str: Incomplete | None = None): ...
def get_minifier_repro_path(): ...
def helper_for_dump_minify(contents) -> None: ...
def dump_to_minify(gm, args, compiler_name: str): ...

class AccuracyError(Exception): ...

def wrap_compiler_debug(unconfigured_compiler_fn, compiler_name: str):
    """
    Minifier for Fx Graph modules after Aot Autograd has finished. We wrap both
    forward and backward call separately with the backend compiler_fn - like
    inductor or nvfuser. Intercepting after Aot Autograd presents neat
    abstration, where all the params are lifted as graph inputs, making it easy
    to save the graph as a string.
    """
def run_fwd_maybe_bwd(gm, args, only_fwd: bool = False):
    """
    Runs a forward and possibly backward iteration for a given mod and args.
    """
def same_two_models(gm, opt_gm, example_inputs, only_fwd: bool = False):
    """
    Check two models have same accuracy.
    """
def cast_convert_element_type_to_fp64(model): ...
def cast_to(dtype, model, inputs): ...
def cast_to_fp64(model, inputs): ...
def generate_dynamo_fx_repro_string(model_str, args, compiler_name, check_accuracy: bool = False):
    """
    Generate a repro string for backend-agnostic minified version.
    """
def dump_backend_repro_as_file(gm, args, compiler_name, check_accuracy: bool = False) -> None:
    """
    Saves the repro to a repro.py file
    """
def dump_backend_state(gm, args, compiler_name, check_accuracy: bool = False):
    """
    Dumps the dynamo graph to repro the issue.
    1) It tries to convert Fx GraphModule to a string. If we can, it writes to a
    repro.py file.
    2) If we can't convert Fx GraphModule to a string, we use to_folder to save
    the module and save a tar file.
    """
def backend_accuracy_fails(gm, example_inputs, compiler_fn, only_fwd: bool = False): ...

backend_aot_accuracy_fails: Incomplete
MINIFIER_SPAWNED: bool

def backend_fails(gm, example_inputs, compiler_fn, orig_failure):
    """
    Minifier uses this function to identify if the minified graph module fails
    with the same error.

    One caveat is that minifier can potentially go into a wrong direction when
    the resulting graph module fails for a different reason. To avoid this, we
    save the string for the original exception and check similarity between new
    and old exception. They can be somewhat different in some cases, when the
    exception string depends on the failing node information. So, we have a
    loose similarity metric to guide the minifier path.
    """
def dump_to_minify_after_dynamo(gm, args, compiler_name) -> None: ...
def wrap_backend_debug(unconfigured_compiler_fn, compiler_name: str):
    """
    A minifier decorator that wraps the TorchDynamo produced Fx graph modules.
    As opposed to wrap_compiler_debug, this wrapper intercepts at the
    TorchDynamo produced Fx Graph Module. This makes it backend-agnostic to some
    level, e.g., it is useful for minifying issues related to Aot Autograd
    tracing.  If an error is found, we minify and save the minified repro in
    repro.tar.gz.
    """
def dynamo_minifier_backend(gm, example_inputs, compiler_name): ...
def dynamo_accuracy_minifier_backend(gm, example_inputs, compiler_name): ...
