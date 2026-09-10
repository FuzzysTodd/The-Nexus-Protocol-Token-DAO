from _typeshed import Incomplete
from torch.utils import cpp_extension as cpp_extension
from torch.utils.benchmark.utils._stubs import CallgrindModuleType as CallgrindModuleType, TimeitModuleType as TimeitModuleType
from typing import List

LOCK: Incomplete
SOURCE_ROOT: Incomplete
CXX_FLAGS: List[str] | None
EXTRA_INCLUDE_PATHS: List[str]
CONDA_PREFIX: Incomplete
COMPAT_CALLGRIND_BINDINGS: CallgrindModuleType | None

def get_compat_bindings() -> CallgrindModuleType: ...
def compile_timeit_template(*, stmt: str, setup: str, global_setup: str) -> TimeitModuleType: ...
def compile_callgrind_template(*, stmt: str, setup: str, global_setup: str) -> str: ...
