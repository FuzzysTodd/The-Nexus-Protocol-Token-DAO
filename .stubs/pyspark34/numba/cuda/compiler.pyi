from _typeshed import Incomplete
from numba.core import compiler as compiler, config as config, funcdesc as funcdesc, sigutils as sigutils, types as types, typing as typing
from numba.core.compiler import CompileResult as CompileResult, CompilerBase as CompilerBase, DefaultPassBuilder as DefaultPassBuilder, Flags as Flags, Option as Option, sanitize_compile_result_entries as sanitize_compile_result_entries
from numba.core.compiler_lock import global_compiler_lock as global_compiler_lock
from numba.core.compiler_machinery import AnalysisPass as AnalysisPass, LoweringPass as LoweringPass, PassManager as PassManager, register_pass as register_pass
from numba.core.errors import NumbaInvalidConfigWarning as NumbaInvalidConfigWarning, TypingError as TypingError
from numba.core.typed_passes import AnnotateTypes as AnnotateTypes, IRLegalization as IRLegalization, NativeLowering as NativeLowering
from numba.core.typing.templates import ConcreteTemplate as ConcreteTemplate
from numba.cuda.api import get_current_device as get_current_device

class CUDAFlags(Flags):
    nvvm_options: Incomplete
    compute_capability: Incomplete

class CUDACompileResult(CompileResult):
    @property
    def entry_point(self): ...

def cuda_compile_result(**entries): ...

class CUDABackend(LoweringPass):
    def __init__(self) -> None: ...
    def run_pass(self, state):
        """
        Back-end: Packages lowering output in a compile result
        """

class CreateLibrary(LoweringPass):
    """
    Create a CUDACodeLibrary for the NativeLowering pass to populate. The
    NativeLowering pass will create a code library if none exists, but we need
    to set it up with nvvm_options from the flags if they are present.
    """
    def __init__(self) -> None: ...
    def run_pass(self, state): ...

class CUDALegalization(AnalysisPass):
    def __init__(self) -> None: ...
    def run_pass(self, state): ...

class CUDACompiler(CompilerBase):
    def define_pipelines(self): ...
    def define_cuda_lowering_pipeline(self, state): ...

def compile_cuda(pyfunc, return_type, args, debug: bool = False, lineinfo: bool = False, inline: bool = False, fastmath: bool = False, nvvm_options: Incomplete | None = None, cc: Incomplete | None = None): ...
def compile_ptx(pyfunc, sig, debug: bool = False, lineinfo: bool = False, device: bool = False, fastmath: bool = False, cc: Incomplete | None = None, opt: bool = True):
    """Compile a Python function to PTX for a given set of argument types.

    :param pyfunc: The Python function to compile.
    :param sig: The signature representing the function's input and output
                types.
    :param debug: Whether to include debug info in the generated PTX.
    :type debug: bool
    :param lineinfo: Whether to include a line mapping from the generated PTX
                     to the source code. Usually this is used with optimized
                     code (since debug mode would automatically include this),
                     so we want debug info in the LLVM but only the line
                     mapping in the final PTX.
    :type lineinfo: bool
    :param device: Whether to compile a device function. Defaults to ``False``,
                   to compile global kernel functions.
    :type device: bool
    :param fastmath: Whether to enable fast math flags (ftz=1, prec_sqrt=0,
                     prec_div=, and fma=1)
    :type fastmath: bool
    :param cc: Compute capability to compile for, as a tuple
               ``(MAJOR, MINOR)``. Defaults to ``(5, 0)``.
    :type cc: tuple
    :param opt: Enable optimizations. Defaults to ``True``.
    :type opt: bool
    :return: (ptx, resty): The PTX code and inferred return type
    :rtype: tuple
    """
def compile_ptx_for_current_device(pyfunc, sig, debug: bool = False, lineinfo: bool = False, device: bool = False, fastmath: bool = False, opt: bool = True):
    """Compile a Python function to PTX for a given set of argument types for
    the current device's compute capabilility. This calls :func:`compile_ptx`
    with an appropriate ``cc`` value for the current device."""
def declare_device_function(name, restype, argtypes): ...
def declare_device_function_template(name, restype, argtypes): ...

class ExternFunction:
    name: Incomplete
    sig: Incomplete
    def __init__(self, name, sig) -> None: ...
