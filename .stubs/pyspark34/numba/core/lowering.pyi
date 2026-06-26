from _typeshed import Incomplete
from numba.core import cgutils as cgutils, config as config, debuginfo as debuginfo, funcdesc as funcdesc, generators as generators, ir as ir, ir_utils as ir_utils, removerefctpass as removerefctpass, targetconfig as targetconfig, types as types, typing as typing, utils as utils
from numba.core.analysis import compute_use_defs as compute_use_defs, must_use_alloca as must_use_alloca
from numba.core.environment import Environment as Environment
from numba.core.errors import LiteralTypingError as LiteralTypingError, LoweringError as LoweringError, NumbaDebugInfoWarning as NumbaDebugInfoWarning, TypingError as TypingError, UnsupportedError as UnsupportedError, new_error_context as new_error_context
from numba.core.funcdesc import default_mangler as default_mangler
from numba.misc.firstlinefinder import get_func_body_first_lineno as get_func_body_first_lineno
from typing import NamedTuple

class _VarArgItem(NamedTuple):
    vararg: Incomplete
    index: Incomplete

class BaseLower:
    """
    Lower IR to LLVM
    """
    library: Incomplete
    fndesc: Incomplete
    blocks: Incomplete
    func_ir: Incomplete
    generator_info: Incomplete
    metadata: Incomplete
    flags: Incomplete
    module: Incomplete
    env: Incomplete
    blkmap: Incomplete
    pending_phis: Incomplete
    varmap: Incomplete
    firstblk: Incomplete
    loc: int
    context: Incomplete
    defn_loc: Incomplete
    debuginfo: Incomplete
    def __init__(self, context, library, fndesc, func_ir, metadata: Incomplete | None = None) -> None: ...
    @property
    def call_conv(self): ...
    def init(self) -> None: ...
    pyapi: Incomplete
    env_manager: Incomplete
    env_body: Incomplete
    envarg: Incomplete
    def init_pyapi(self) -> None:
        """
        Init the Python API and Environment Manager for the function being
        lowered.
        """
    def pre_lower(self) -> None:
        """
        Called before lowering all blocks.
        """
    def post_lower(self) -> None:
        """
        Called after all blocks are lowered
        """
    def pre_block(self, block) -> None:
        """
        Called before lowering a block.
        """
    def post_block(self, block) -> None:
        """
        Called after lowering a block.
        """
    def return_dynamic_exception(self, exc_class, exc_args, nb_types, loc: Incomplete | None = None) -> None: ...
    def return_exception(self, exc_class, exc_args: Incomplete | None = None, loc: Incomplete | None = None) -> None:
        """Propagate exception to the caller.
        """
    def set_exception(self, exc_class, exc_args: Incomplete | None = None, loc: Incomplete | None = None) -> None:
        """Set exception state in the current function.
        """
    def emit_environment_object(self) -> None:
        """Emit a pointer to hold the Environment object.
        """
    genlower: Incomplete
    gentype: Incomplete
    def lower(self) -> None: ...
    fnargs: Incomplete
    def extract_function_arguments(self): ...
    def lower_normal_function(self, fndesc) -> None:
        """
        Lower non-generator *fndesc*.
        """
    def lower_function_body(self):
        """
        Lower the current function's body, and return the entry block.
        """
    def lower_block(self, block) -> None:
        """
        Lower the given block.
        """
    def create_cpython_wrapper(self, release_gil: bool = False) -> None:
        """
        Create CPython wrapper(s) around this function (or generator).
        """
    def create_cfunc_wrapper(self) -> None:
        """
        Create C wrapper around this function.
        """
    function: Incomplete
    entry_block: Incomplete
    builder: Incomplete
    call_helper: Incomplete
    def setup_function(self, fndesc) -> None: ...
    def typeof(self, varname): ...
    def debug_print(self, msg) -> None: ...
    def print_variable(self, msg, varname) -> None:
        """Helper to emit ``print(msg, varname)`` for debugging.

        Parameters
        ----------
        msg : str
            Literal string to be printed.
        varname : str
            A variable name whose value will be printed.
        """

class Lower(BaseLower):
    GeneratorLower: Incomplete
    def init(self) -> None: ...
    def pre_block(self, block) -> None: ...
    def post_block(self, block) -> None: ...
    def lower_inst(self, inst): ...
    def lower_setitem(self, target_var, index_var, value_var, signature): ...
    def lower_try_dynamic_raise(self, inst) -> None: ...
    def lower_dynamic_raise(self, inst) -> None: ...
    def lower_static_raise(self, inst) -> None: ...
    def lower_static_try_raise(self, inst) -> None: ...
    def lower_assign(self, ty, inst): ...
    def lower_yield(self, retty, inst): ...
    def lower_binop(self, resty, expr, op): ...
    def lower_getitem(self, resty, expr, value, index, signature): ...
    def fold_call_args(self, fnty, signature, pos_args, vararg, kw_args): ...
    def lower_print(self, inst) -> None:
        """
        Lower a ir.Print()
        """
    def lower_call(self, resty, expr): ...
    def lower_expr(self, resty, expr): ...
    def getvar(self, name):
        """
        Get a pointer to the given variable's slot.
        """
    def loadvar(self, name):
        """
        Load the given variable's value.
        """
    def storevar(self, value, name, argidx: Incomplete | None = None) -> None:
        """
        Store the value into the given variable.
        """
    def delvar(self, name) -> None:
        """
        Delete the given variable.
        """
    def alloca(self, name, type): ...
    def alloca_lltype(self, name, lltype, datamodel: Incomplete | None = None): ...
    def incref(self, typ, val) -> None: ...
    def decref(self, typ, val) -> None: ...
