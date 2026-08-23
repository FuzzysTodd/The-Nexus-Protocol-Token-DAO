from .cudadrv import nvvm as nvvm
from _typeshed import Incomplete
from functools import cached_property as cached_property
from numba.core import cgutils as cgutils, datamodel as datamodel, debuginfo as debuginfo, itanium_mangler as itanium_mangler, types as types, typing as typing
from numba.core.base import BaseContext as BaseContext
from numba.core.callconv import MinimalCallConv as MinimalCallConv
from numba.core.dispatcher import Dispatcher as Dispatcher
from numba.core.errors import NumbaInvalidConfigWarning as NumbaInvalidConfigWarning
from numba.core.typing import cmathdecl as cmathdecl
from numba.cuda import codegen as codegen, nvvmutils as nvvmutils, ufuncs as ufuncs
from numba.cuda.models import cuda_data_manager as cuda_data_manager

class CUDATypingContext(typing.BaseContext):
    def load_additional_registries(self) -> None: ...
    def resolve_value_type(self, val): ...

VALID_CHARS: Incomplete

class CUDATargetContext(BaseContext):
    implement_powi_as_math_call: bool
    strict_alignment: bool
    data_model_manager: Incomplete
    def __init__(self, typingctx, target: str = 'cuda') -> None: ...
    @property
    def DIBuilder(self): ...
    @property
    def enable_boundscheck(self): ...
    def create_module(self, name): ...
    def init(self) -> None: ...
    def load_additional_registries(self) -> None: ...
    def codegen(self): ...
    @property
    def target_data(self): ...
    @cached_property
    def nonconst_module_attrs(self):
        """
        Some CUDA intrinsics are at the module level, but cannot be treated as
        constants, because they are loaded from a special register in the PTX.
        These include threadIdx, blockDim, etc.
        """
    @cached_property
    def call_conv(self): ...
    def mangler(self, name, argtypes, *, abi_tags=(), uid: Incomplete | None = None): ...
    def prepare_cuda_kernel(self, codelib, fndesc, debug, lineinfo, nvvm_options, filename, linenum, max_registers: Incomplete | None = None):
        """
        Adapt a code library ``codelib`` with the numba compiled CUDA kernel
        with name ``fname`` and arguments ``argtypes`` for NVVM.
        A new library is created with a wrapper function that can be used as
        the kernel entry point for the given kernel.

        Returns the new code library and the wrapper function.

        Parameters:

        codelib:       The CodeLibrary containing the device function to wrap
                       in a kernel call.
        fndesc:        The FunctionDescriptor of the source function.
        debug:         Whether to compile with debug.
        lineinfo:      Whether to emit line info.
        nvvm_options:  Dict of NVVM options used when compiling the new library.
        filename:      The source filename that the function is contained in.
        linenum:       The source line that the function is on.
        max_registers: The max_registers argument for the code library.
        """
    def generate_kernel_wrapper(self, library, fndesc, kernel_name, debug, lineinfo, filename, linenum):
        """
        Generate the kernel wrapper in the given ``library``.
        The function being wrapped is described by ``fndesc``.
        The wrapper function is returned.
        """
    def make_constant_array(self, builder, aryty, arr):
        """
        Unlike the parent version.  This returns a a pointer in the constant
        addrspace.
        """
    def insert_const_string(self, mod, string):
        """
        Unlike the parent version.  This returns a a pointer in the constant
        addrspace.
        """
    def insert_string_const_addrspace(self, builder, string):
        """
        Insert a constant string in the constant addresspace and return a
        generic i8 pointer to the data.

        This function attempts to deduplicate.
        """
    def optimize_function(self, func) -> None:
        """Run O1 function passes
        """
    def get_ufunc_info(self, ufunc_key): ...

class CUDACallConv(MinimalCallConv): ...
