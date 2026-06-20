from _typeshed import Incomplete
from numba.core import config as config, ir as ir, ir_utils as ir_utils, rewrites as rewrites, types as types, typing as typing, utils as utils
from numba.core.errors import NumbaValueError as NumbaValueError
from numba.core.ir_utils import GuardException as GuardException, compile_to_numba_ir as compile_to_numba_ir, find_callname as find_callname, find_const as find_const, get_call_table as get_call_table, guard as guard, mk_unique_var as mk_unique_var, replace_arg_nodes as replace_arg_nodes, require as require
from numba.core.typing import signature as signature
from numba.core.typing.templates import AbstractTemplate as AbstractTemplate, infer_global as infer_global
from numba.core.utils import OPERATORS_TO_BUILTINS as OPERATORS_TO_BUILTINS
from numba.np import numpy_support as numpy_support

class StencilPass:
    func_ir: Incomplete
    typemap: Incomplete
    calltypes: Incomplete
    array_analysis: Incomplete
    typingctx: Incomplete
    targetctx: Incomplete
    flags: Incomplete
    def __init__(self, func_ir, typemap, calltypes, array_analysis, typingctx, targetctx, flags) -> None: ...
    def run(self) -> None:
        """ Finds all calls to StencilFuncs in the IR and converts them to parfor.
        """
    def replace_return_with_setitem(self, blocks, exit_value_var, parfor_body_exit_label) -> None:
        '''
        Find return statements in the IR and replace them with a SetItem
        call of the value "returned" by the kernel into the result array.
        Returns the block labels that contained return statements.
        '''

def get_stencil_ir(sf, typingctx, args, scope, loc, input_dict, typemap, calltypes):
    """get typed IR from stencil bytecode
    """

class DummyPipeline:
    state: Incomplete
    def __init__(self, typingctx, targetctx, args, f_ir) -> None: ...
