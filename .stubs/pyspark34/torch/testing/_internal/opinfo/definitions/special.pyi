from _typeshed import Incomplete
from collections.abc import Generator
from torch.testing import make_tensor as make_tensor
from torch.testing._internal.common_device_type import precisionOverride as precisionOverride, tol as tol, toleranceOverride as toleranceOverride
from torch.testing._internal.common_dtype import all_types_and as all_types_and, floating_types as floating_types
from torch.testing._internal.common_utils import TEST_SCIPY as TEST_SCIPY, torch_to_numpy_dtype_dict as torch_to_numpy_dtype_dict
from torch.testing._internal.opinfo.core import BinaryUfuncInfo as BinaryUfuncInfo, DecorateInfo as DecorateInfo, L as L, NumericsFilter as NumericsFilter, OpInfo as OpInfo, S as S, SampleInput as SampleInput, UnaryUfuncInfo as UnaryUfuncInfo
from torch.testing._internal.opinfo.refs import ElementwiseBinaryPythonRefInfo as ElementwiseBinaryPythonRefInfo, ElementwiseUnaryPythonRefInfo as ElementwiseUnaryPythonRefInfo
from torch.testing._internal.opinfo.utils import np_unary_ufunc_integer_promotion_wrapper as np_unary_ufunc_integer_promotion_wrapper
from typing import List

def sample_inputs_i0_i1(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]: ...
def sample_inputs_polygamma(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]: ...
def reference_polygamma(x, n): ...
def sample_inputs_entr(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]: ...

op_db: List[OpInfo]
python_ref_db: List[OpInfo]
