from _typeshed import Incomplete
from llvmlite import binding as binding
from numba.core import cgutils as cgutils, config as config, types as types

incref_decref_ty: Incomplete
meminfo_data_ty: Incomplete

def create_nrt_module(ctx):
    """
    Create an IR module defining the LLVM NRT functions.
    A (IR module, library) tuple is returned.
    """
def compile_nrt_functions(ctx):
    """
    Compile all LLVM NRT functions and return a library containing them.
    The library is created using the given target context.
    """
