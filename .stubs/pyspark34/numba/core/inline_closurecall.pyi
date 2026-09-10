from _typeshed import Incomplete
from numba.core import config as config, errors as errors, ir as ir, ir_utils as ir_utils, postproc as postproc, rewrites as rewrites, types as types, typing as typing
from numba.core.analysis import compute_cfg_from_blocks as compute_cfg_from_blocks, compute_live_variables as compute_live_variables, compute_use_defs as compute_use_defs
from numba.core.ir_utils import GuardException as GuardException, add_offset_to_labels as add_offset_to_labels, canonicalize_array_math as canonicalize_array_math, dead_code_elimination as dead_code_elimination, find_build_sequence as find_build_sequence, find_callname as find_callname, find_topo_order as find_topo_order, get_definition as get_definition, get_ir_of_code as get_ir_of_code, get_np_ufunc_typ as get_np_ufunc_typ, guard as guard, merge_adjacent_blocks as merge_adjacent_blocks, next_label as next_label, remove_dels as remove_dels, rename_labels as rename_labels, replace_vars as replace_vars, require as require, simplify_CFG as simplify_CFG
from numba.parfors.parfor import internal_prange as internal_prange

enable_inline_arraycall: bool

def callee_ir_validator(func_ir) -> None:
    """Checks the IR of a callee is supported for inlining
    """

class InlineClosureCallPass:
    """InlineClosureCallPass class looks for direct calls to locally defined
    closures, and inlines the body of the closure function to the call site.
    """
    func_ir: Incomplete
    parallel_options: Incomplete
    swapped: Incomplete
    typed: Incomplete
    def __init__(self, func_ir, parallel_options, swapped={}, typed: bool = False) -> None: ...
    def run(self):
        """Run inline closure call pass.
        """

def check_reduce_func(func_ir, func_var):
    """Checks the function at func_var in func_ir to make sure it's amenable
    for inlining. Returns the function itself"""

class InlineWorker:
    """ A worker class for inlining, this is a more advanced version of
    `inline_closure_call` in that it permits inlining from function type, Numba
    IR and code object. It also, runs the entire untyped compiler pipeline on
    the inlinee to ensure that it is transformed as though it were compiled
    directly.
    """
    typingctx: Incomplete
    targetctx: Incomplete
    locals: Incomplete
    pipeline: Incomplete
    flags: Incomplete
    validator: Incomplete
    debug_print: Incomplete
    typemap: Incomplete
    calltypes: Incomplete
    def __init__(self, typingctx: Incomplete | None = None, targetctx: Incomplete | None = None, locals: Incomplete | None = None, pipeline: Incomplete | None = None, flags: Incomplete | None = None, validator=..., typemap: Incomplete | None = None, calltypes: Incomplete | None = None) -> None:
        """
        Instantiate a new InlineWorker, all arguments are optional though some
        must be supplied together for certain use cases. The methods will refuse
        to run if the object isn't configured in the manner needed. Args are the
        same as those in a numba.core.Compiler.state, except the validator which
        is a function taking Numba IR and validating it for use when inlining
        (this is optional and really to just provide better error messages about
        things which the inliner cannot handle like yield in closure).
        """
    def inline_ir(self, caller_ir, block, i, callee_ir, callee_freevars, arg_typs: Incomplete | None = None):
        """ Inlines the callee_ir in the caller_ir at statement index i of block
        `block`, callee_freevars are the free variables for the callee_ir. If
        the callee_ir is derived from a function `func` then this is
        `func.__code__.co_freevars`. If `arg_typs` is given and the InlineWorker
        instance was initialized with a typemap and calltypes then they will be
        appropriately updated based on the arg_typs.
        """
    def inline_function(self, caller_ir, block, i, function, arg_typs: Incomplete | None = None):
        """ Inlines the function in the caller_ir at statement index i of block
        `block`. If `arg_typs` is given and the InlineWorker instance was
        initialized with a typemap and calltypes then they will be appropriately
        updated based on the arg_typs.
        """
    def run_untyped_passes(self, func, enable_ssa: bool = False):
        """
        Run the compiler frontend's untyped passes over the given Python
        function, and return the function's canonical Numba IR.

        Disable SSA transformation by default, since the call site won't be in
        SSA form and self.inline_ir depends on this being the case.
        """
    def update_type_and_call_maps(self, callee_ir, arg_typs) -> None:
        """ Updates the type and call maps based on calling callee_ir with
        arguments from arg_typs"""

def inline_closure_call(func_ir, glbls, block, i, callee, typingctx: Incomplete | None = None, targetctx: Incomplete | None = None, arg_typs: Incomplete | None = None, typemap: Incomplete | None = None, calltypes: Incomplete | None = None, work_list: Incomplete | None = None, callee_validator: Incomplete | None = None, replace_freevars: bool = True):
    """Inline the body of `callee` at its callsite (`i`-th instruction of
    `block`)

    `func_ir` is the func_ir object of the caller function and `glbls` is its
    global variable environment (func_ir.func_id.func.__globals__).
    `block` is the IR block of the callsite and `i` is the index of the
    callsite's node. `callee` is either the called function or a
    make_function node. `typingctx`, `typemap` and `calltypes` are typing
    data structures of the caller, available if we are in a typed pass.
    `arg_typs` includes the types of the arguments at the callsite.
    `callee_validator` is an optional callable which can be used to validate the
    IR of the callee to ensure that it contains IR supported for inlining, it
    takes one argument, the func_ir of the callee

    Returns IR blocks of the callee and the variable renaming dictionary used
    for them to facilitate further processing of new blocks.
    """

class RewriteArrayOfConsts(rewrites.Rewrite):
    """The RewriteArrayOfConsts class is responsible for finding
    1D array creations from a constant list, and rewriting it into
    direct initialization of array elements without creating the list.
    """
    typingctx: Incomplete
    def __init__(self, state, *args, **kws) -> None: ...
    crnt_block: Incomplete
    new_body: Incomplete
    def match(self, func_ir, block, typemap, calltypes): ...
    def apply(self): ...
