from _typeshed import Incomplete
from torch.testing._internal.common_cuda import TEST_CUDA as TEST_CUDA
from torch.testing._internal.common_dtype import _dispatch_dtypes, all_types as all_types, all_types_and as all_types_and, all_types_and_complex as all_types_and_complex, all_types_and_complex_and as all_types_and_complex_and, all_types_and_half as all_types_and_half, complex_types as complex_types, floating_and_complex_types as floating_and_complex_types, floating_and_complex_types_and as floating_and_complex_types_and, floating_types as floating_types, floating_types_and as floating_types_and, floating_types_and_half as floating_types_and_half, integral_types as integral_types, integral_types_and as integral_types_and
from torch.testing._internal.common_utils import torch_to_numpy_dtype_dict as torch_to_numpy_dtype_dict

COMPLETE_DTYPES_DISPATCH: Incomplete
EXTENSIBLE_DTYPE_DISPATCH: Incomplete
DEVICES: Incomplete

class _dynamic_dispatch_dtypes(_dispatch_dtypes): ...

def get_supported_dtypes(op, sample_inputs_fn, device_type): ...
def dtypes_dispatch_hint(dtypes): ...
def is_dynamic_dtype_set(op): ...
def str_format_dynamic_dtype(op): ...
def np_unary_ufunc_integer_promotion_wrapper(fn): ...
def reference_reduction_numpy(f, supports_keepdims: bool = True):
    """Wraps a NumPy reduction operator.

    The wrapper function will forward dim, keepdim, mask, and identity
    kwargs to the wrapped function as the NumPy equivalent axis,
    keepdims, where, and initiak kwargs, respectively.

    Args:
        f: NumPy reduction operator to wrap
        supports_keepdims (bool, optional): Whether the NumPy operator accepts
            keepdims parameter. If it does not, the wrapper will manually unsqueeze
            the reduced dimensions if it was called with keepdim=True. Defaults to True.

    Returns:
        Wrapped function

    """
def prod_numpy(a, *args, **kwargs):
    """
    The function will call np.prod with type as np.int64 if the input type
    is int or uint64 if is uint. This is necessary because windows np.prod uses by default
    int32 while on linux it uses int64.
    This is for fixing integer overflow https://github.com/pytorch/pytorch/issues/77320

    Returns:
        np.prod of input
    """
