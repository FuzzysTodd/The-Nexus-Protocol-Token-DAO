from _typeshed import Incomplete
from collections.abc import Generator
from torch.testing import make_tensor as make_tensor
from torch.testing._internal.common_cuda import SM53OrLater as SM53OrLater
from torch.testing._internal.common_device_type import precisionOverride as precisionOverride
from torch.testing._internal.common_dtype import all_types_and as all_types_and, all_types_and_complex_and as all_types_and_complex_and
from torch.testing._internal.common_utils import TEST_SCIPY as TEST_SCIPY, TEST_WITH_ROCM as TEST_WITH_ROCM
from torch.testing._internal.opinfo.core import DecorateInfo as DecorateInfo, ErrorInput as ErrorInput, OpInfo as OpInfo, SampleInput as SampleInput, SpectralFuncInfo as SpectralFuncInfo, SpectralFuncType as SpectralFuncType
from torch.testing._internal.opinfo.refs import PythonRefInfo as PythonRefInfo
from typing import List

has_scipy_fft: bool

class SpectralFuncPythonRefInfo(SpectralFuncInfo):
    """
    An OpInfo for a Python reference of an elementwise unary operation.
    """
    torch_opinfo_name: Incomplete
    torch_opinfo: Incomplete
    supports_nvfuser: Incomplete
    def __init__(self, name, *, op: Incomplete | None = None, torch_opinfo_name, torch_opinfo_variant: str = '', supports_nvfuser: bool = True, **kwargs) -> None: ...

def error_inputs_fft(op_info, device, **kwargs) -> Generator[Incomplete, None, None]: ...
def error_inputs_fftn(op_info, device, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_fftshift(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, Incomplete]: ...

op_db: List[OpInfo]
python_ref_db: List[OpInfo]
