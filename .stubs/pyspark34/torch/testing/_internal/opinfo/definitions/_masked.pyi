from _typeshed import Incomplete
from collections.abc import Generator
from torch.testing import make_tensor as make_tensor
from torch.testing._internal.common_device_type import tol as tol, toleranceOverride as toleranceOverride
from torch.testing._internal.common_dtype import all_types_and as all_types_and, all_types_and_complex_and as all_types_and_complex_and, complex_types as complex_types, floating_and_complex_types_and as floating_and_complex_types_and, floating_types_and as floating_types_and, integral_types as integral_types
from torch.testing._internal.opinfo.core import DecorateInfo as DecorateInfo, M as M, OpInfo as OpInfo, ReductionOpInfo as ReductionOpInfo, S as S, SampleInput as SampleInput, gradcheck_wrapper_masked_operation as gradcheck_wrapper_masked_operation, gradcheck_wrapper_masked_pointwise_operation as gradcheck_wrapper_masked_pointwise_operation, sample_inputs_reduction as sample_inputs_reduction
from torch.testing._internal.opinfo.utils import prod_numpy as prod_numpy, reference_reduction_numpy as reference_reduction_numpy
from typing import List

def sample_inputs_softmax_variant(op_info, device, dtype, requires_grad, with_dtype: bool = False, use_zero_dimensions: bool = True, **kwargs): ...
def sample_inputs_masked_reduction(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]:
    """Sample inputs for masked reduction operators.

    Masked reduction operator is a reduction operator with trailing
    mask optional argument. A mask is a bool tensor with the same
    shape as input or a shape that is broadcastable to input shape.
    """
def sample_inputs_sparse_coo_masked_reduction(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]:
    """Sample inputs for masked reduction operators that support inputs
    with sparse coo layouts.
    """
def sample_inputs_sparse_csr_masked_reduction(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]:
    """Sample inputs for masked reduction operators that support inputs
    with sparse csr layouts.
    """
def sample_inputs_masked_norm(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]:
    """Sample inputs for masked norm."""
def reference_masked_std_var(numpy_fn): ...
def sample_inputs_masked_std_var(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]:
    """Sample inputs for masked std/var."""
def sample_inputs_masked_softmax(op_info, device, dtype, requires_grad, with_dtype: bool = False, **kwargs) -> Generator[Incomplete, None, None]:
    """Sample inputs for masked softmax, log_softmax, and softmin.

    Masked normalization operator is a reduction operator with
    trailing mask optional argument. A mask is a bool tensor with the
    same shape as input or a shape that is broadcastable to input
    shape.
    """
def sample_inputs_masked_cumops(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]:
    """Sample inputs for masked cumsum and cumprod."""
def sample_inputs_masked_logaddexp(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]:
    """Sample inputs for masked logaddexp."""
def sample_inputs_masked_normalize(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]:
    """Sample inputs for masked normalize."""

op_db: List[OpInfo]
