from _typeshed import Incomplete

class NvvmSupportError(ImportError): ...

class NVVM:
    def __init__(self) -> None: ...

CompilationUnit: Incomplete
llvm_to_ptx: Incomplete
set_cuda_kernel: Incomplete
get_arch_option: Incomplete
LibDevice: Incomplete
NvvmError: Incomplete

def is_available(): ...
def get_supported_ccs(): ...
