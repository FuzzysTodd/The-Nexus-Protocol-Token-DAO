from _typeshed import Incomplete
from collections.abc import Generator
from torch.testing._internal.common_dtype import floating_types as floating_types
from torch.testing._internal.common_utils import TEST_SCIPY as TEST_SCIPY
from torch.testing._internal.opinfo.core import DecorateInfo as DecorateInfo, ErrorInput as ErrorInput, OpInfo as OpInfo, SampleInput as SampleInput
from typing import Callable, List, Tuple

def sample_inputs_window(op_info, device, dtype, requires_grad, *args, **kwargs) -> Generator[Incomplete, None, None]:
    """Base function used to create sample inputs for windows.

    For additional required args you should use *args, as well as **kwargs for
    additional keyword arguments.
    """
def reference_inputs_window(op_info, device, dtype, requires_grad, *args, **kwargs) -> Generator[Incomplete, Incomplete, None]:
    """Reference inputs function to use for windows which have a common signature, i.e.,
    window size and sym only.

    Implement other special functions for windows that have a specific signature.
    See exponential and gaussian windows for instance.
    """
def reference_inputs_exponential_window(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, Incomplete, None]: ...
def reference_inputs_gaussian_window(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, Incomplete, None]: ...
def reference_inputs_kaiser_window(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, Incomplete, None]: ...
def reference_inputs_general_cosine_window(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, Incomplete, None]: ...
def reference_inputs_general_hamming_window(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, Incomplete, None]: ...
def error_inputs_window(op_info, device, *args, **kwargs) -> Generator[Incomplete, None, None]: ...
def error_inputs_exponential_window(op_info, device, **kwargs) -> Generator[Incomplete, Incomplete, None]: ...
def error_inputs_gaussian_window(op_info, device, **kwargs) -> Generator[Incomplete, Incomplete, None]: ...
def error_inputs_kaiser_window(op_info, device, **kwargs) -> Generator[Incomplete, Incomplete, None]: ...
def error_inputs_general_cosine_window(op_info, device, **kwargs) -> Generator[Incomplete, Incomplete, None]: ...
def reference_signal_window(fn: Callable):
    """Wrapper for scipy signal window references.

    Discards keyword arguments for window reference functions that don't have a matching signature with
    torch, e.g., gaussian window.
    """
def make_signal_windows_opinfo(name: str, ref: Callable, sample_inputs_func: Callable, reference_inputs_func: Callable, error_inputs_func: Callable, *, skips: Tuple[DecorateInfo, ...] = ()):
    """Helper function to create OpInfo objects related to different windows."""

op_db: List[OpInfo]
