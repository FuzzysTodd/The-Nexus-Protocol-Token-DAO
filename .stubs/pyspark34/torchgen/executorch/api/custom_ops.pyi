from dataclasses import dataclass
from torchgen import dest as dest
from torchgen.api.types import DispatcherSignature as DispatcherSignature
from torchgen.context import method_with_native_function as method_with_native_function
from torchgen.model import BackendIndex as BackendIndex, DispatchKey as DispatchKey, NativeFunction as NativeFunction, Variant as Variant
from torchgen.selective_build.selector import SelectiveBuilder as SelectiveBuilder
from torchgen.utils import Target as Target, concatMap as concatMap
from typing import Sequence, Tuple

@dataclass(frozen=True)
class ComputeNativeFunctionStub:
    def __call__(self, f: NativeFunction) -> str | None: ...

def gen_custom_ops_registration(*, native_functions: Sequence[NativeFunction], selector: SelectiveBuilder, backend_index: BackendIndex, rocm: bool) -> Tuple[str, str]:
    """
    Generate custom ops registration code for dest.RegisterDispatchKey.

    :param native_functions: a sequence of `NativeFunction`
    :param selector: for selective build.
    :param backend_index: kernels for all the ops.
    :param rocm: bool for dest.RegisterDispatchKey.
    :return: generated C++ code to register custom operators into PyTorch
    """
