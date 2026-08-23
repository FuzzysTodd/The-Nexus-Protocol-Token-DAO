from .cudadrv import devices as devices, driver as driver, nvvm as nvvm, runtime as runtime
from _typeshed import Incomplete
from numba.core import config as config, serialize as serialize
from numba.core.codegen import CodeLibrary as CodeLibrary, Codegen as Codegen
from numba.cuda.cudadrv.libs import get_cudalib as get_cudalib

CUDA_TRIPLE: str

def disassemble_cubin(cubin): ...

class CUDACodeLibrary(serialize.ReduceMixin, CodeLibrary):
    """
    The CUDACodeLibrary generates PTX, SASS, cubins for multiple different
    compute capabilities. It also loads cubins to multiple devices (via
    get_cufunc), which may be of different compute capabilities.
    """
    needs_cudadevrt: bool
    def __init__(self, codegen, name, entry_name: Incomplete | None = None, max_registers: Incomplete | None = None, nvvm_options: Incomplete | None = None) -> None:
        """
        codegen:
            Codegen object.
        name:
            Name of the function in the source.
        entry_name:
            Name of the kernel function in the binary, if this is a global
            kernel and not a device function.
        max_registers:
            The maximum register usage to aim for when linking.
        nvvm_options:
                Dict of options to pass to NVVM.
        """
    @property
    def llvm_strs(self): ...
    def get_llvm_str(self): ...
    def get_asm_str(self, cc: Incomplete | None = None): ...
    def get_cubin(self, cc: Incomplete | None = None): ...
    def get_cufunc(self): ...
    def get_linkerinfo(self, cc): ...
    def get_sass(self, cc: Incomplete | None = None): ...
    def add_ir_module(self, mod) -> None: ...
    def add_linking_library(self, library) -> None: ...
    def add_linking_file(self, filepath) -> None: ...
    def get_function(self, name): ...
    @property
    def modules(self): ...
    @property
    def linking_libraries(self): ...
    def finalize(self) -> None: ...

class JITCUDACodegen(Codegen):
    """
    This codegen implementation for CUDA only generates optimized LLVM IR.
    Generation of PTX code is done separately (see numba.cuda.compiler).
    """
    def __init__(self, module_name) -> None: ...
    def magic_tuple(self):
        """
        Return a tuple unambiguously describing the codegen behaviour.
        """
