from .error import NvvmError as NvvmError, NvvmSupportError as NvvmSupportError, NvvmWarning as NvvmWarning
from .libs import get_libdevice as get_libdevice, open_cudalib as open_cudalib, open_libdevice as open_libdevice
from _typeshed import Incomplete
from ctypes import c_int, c_void_p
from numba.core import cgutils as cgutils, config as config

logger: Incomplete
ADDRSPACE_GENERIC: int
ADDRSPACE_GLOBAL: int
ADDRSPACE_SHARED: int
ADDRSPACE_CONSTANT: int
ADDRSPACE_LOCAL: int
nvvm_program = c_void_p
nvvm_result = c_int
RESULT_CODE_NAMES: Incomplete

def is_available():
    """
    Return if libNVVM is available
    """

class NVVM:
    """Process-wide singleton.
    """
    def __new__(cls): ...
    def __init__(self) -> None: ...
    @property
    def is_nvvm70(self): ...
    @property
    def data_layout(self): ...
    @property
    def supported_ccs(self): ...
    def get_version(self): ...
    def get_ir_version(self): ...
    def check_error(self, error, msg, exit: bool = False) -> None: ...

class CompilationUnit:
    driver: Incomplete
    def __init__(self) -> None: ...
    def __del__(self) -> None: ...
    def add_module(self, buffer) -> None:
        """
         Add a module level NVVM IR to a compilation unit.
         - The buffer should contain an NVVM module IR either in the bitcode
           representation (LLVM3.0) or in the text representation.
        """
    def lazy_add_module(self, buffer) -> None:
        """
        Lazily add an NVVM IR module to a compilation unit.
        The buffer should contain NVVM module IR either in the bitcode
        representation or in the text representation.
        """
    log: Incomplete
    def compile(self, **options):
        """Perform Compilation

        The valid compiler options are

         *   - -opt=
         *     - 0 (disable optimizations)
         *     - 3 (default, enable optimizations)
         *   - -arch=
         *     - compute_XX where XX is in (35, 37, 50, 52, 53, 60, 61, 62, 70,
         *                                  72, 75, 80, 86, 89, 90).
         *       The default is compute_52.
         *   - -ftz=
         *     - 0 (default, preserve denormal values, when performing
         *          single-precision floating-point operations)
         *     - 1 (flush denormal values to zero, when performing
         *          single-precision floating-point operations)
         *   - -prec-sqrt=
         *     - 0 (use a faster approximation for single-precision
         *          floating-point square root)
         *     - 1 (default, use IEEE round-to-nearest mode for
         *          single-precision floating-point square root)
         *   - -prec-div=
         *     - 0 (use a faster approximation for single-precision
         *          floating-point division and reciprocals)
         *     - 1 (default, use IEEE round-to-nearest mode for
         *          single-precision floating-point division and reciprocals)
         *   - -fma=
         *     - 0 (disable FMA contraction)
         *     - 1 (default, enable FMA contraction)
         *
         """
    def get_log(self): ...

COMPUTE_CAPABILITIES: Incomplete
CTK_SUPPORTED: Incomplete

def ccs_supported_by_ctk(ctk_version): ...
def get_supported_ccs(): ...
def find_closest_arch(mycc):
    """
    Given a compute capability, return the closest compute capability supported
    by the CUDA toolkit.

    :param mycc: Compute capability as a tuple ``(MAJOR, MINOR)``
    :return: Closest supported CC as a tuple ``(MAJOR, MINOR)``
    """
def get_arch_option(major, minor):
    """Matches with the closest architecture option
    """

MISSING_LIBDEVICE_FILE_MSG: str

class LibDevice:
    bc: Incomplete
    def __init__(self) -> None: ...
    def get(self): ...

ir_numba_cas_hack: str
cas_nvvm70: str
cas_nvvm34: str
ir_numba_atomic_binary_template: str
ir_numba_atomic_inc_template: str
ir_numba_atomic_dec_template: str
ir_numba_atomic_minmax_template: str

def ir_cas(Ti): ...
def ir_numba_atomic_binary(T, Ti, OP, FUNC): ...
def ir_numba_atomic_minmax(T, Ti, NAN, OP, PTR_OR_VAL, FUNC): ...
def ir_numba_atomic_inc(T, Tu): ...
def ir_numba_atomic_dec(T, Tu): ...
def llvm_replace(llvmir): ...
def llvm_to_ptx(llvmir, **opts): ...

re_metadata_def: Incomplete
re_metadata_correct_usage: Incomplete
re_metadata_ref: Incomplete
debuginfo_pattern: str
re_metadata_debuginfo: Incomplete
re_attributes_def: Incomplete
supported_attributes: Incomplete
re_getelementptr: Incomplete
re_load: Incomplete
re_call: Incomplete
re_range: Incomplete
re_type_tok: Incomplete
re_annotations: Incomplete
re_unsupported_keywords: Incomplete
re_parenthesized_list: Incomplete
re_spflags: Incomplete
spflagmap: Incomplete

def llvm100_to_70_ir(ir):
    """
    Convert LLVM 10.0 IR for LLVM 7.0.
    """
def llvm100_to_34_ir(ir):
    """
    Convert LLVM 10.0 IR for LLVM 3.4.
    """
def set_cuda_kernel(lfunc) -> None: ...
def add_ir_version(mod) -> None:
    """Add NVVM IR version to module"""
