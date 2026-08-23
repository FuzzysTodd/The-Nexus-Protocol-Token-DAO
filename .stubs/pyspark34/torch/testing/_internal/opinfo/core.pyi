import torch
from _typeshed import Incomplete
from collections.abc import Generator
from dataclasses import dataclass
from torch.testing import make_tensor as make_tensor
from torch.testing._internal.common_device_type import skipCPUIfNoFFT as skipCPUIfNoFFT, tol as tol, toleranceOverride as toleranceOverride
from torch.testing._internal.common_dtype import _dispatch_dtypes, floating_and_complex_types as floating_and_complex_types, floating_and_complex_types_and as floating_and_complex_types_and, floating_types as floating_types
from torch.testing._internal.common_utils import TEST_WITH_ROCM as TEST_WITH_ROCM, is_iterable_of_tensors as is_iterable_of_tensors, noncontiguous_like as noncontiguous_like, torch_to_numpy_dtype_dict as torch_to_numpy_dtype_dict
from torch.testing._internal.opinfo import utils as utils
from typing import Any, Callable, Iterable, List, NamedTuple, Tuple

L: int
M: int
S: int
XS: int

class DecorateInfo:
    """Describes which test, or type of tests, should be wrapped in the given
    decorators when testing an operator. Any test that matches all provided
    arguments will be decorated. The decorators will only be applied if the
    active_if argument is True."""
    decorators: Incomplete
    cls_name: Incomplete
    test_name: Incomplete
    device_type: Incomplete
    dtypes: Incomplete
    active_if: Incomplete
    def __init__(self, decorators, cls_name: Incomplete | None = None, test_name: Incomplete | None = None, *, device_type: Incomplete | None = None, dtypes: Incomplete | None = None, active_if: bool = True) -> None: ...
    def is_active(self, cls_name, test_name, device_type, dtype, param_kwargs): ...

class SampleInput:
    """Represents sample inputs to a function."""
    input: Incomplete
    args: Incomplete
    kwargs: Incomplete
    output_process_fn_grad: Incomplete
    name: Incomplete
    broadcasts_input: Incomplete
    def __init__(self, input, *var_args, args: Incomplete | None = None, kwargs: Incomplete | None = None, output_process_fn_grad: Incomplete | None = None, broadcasts_input: Incomplete | None = None, name: Incomplete | None = None, **var_kwargs) -> None: ...
    def with_metadata(self, *, output_process_fn_grad: Incomplete | None = None, broadcasts_input: Incomplete | None = None, name: Incomplete | None = None): ...
    def summary(self): ...
    def transform(self, f): ...
    def numpy(self): ...
    def noncontiguous(self): ...

class NumericsFilter(NamedTuple):
    condition: Incomplete
    safe_val: Incomplete

class ErrorInput:
    """
    A SampleInput that will cause the operation to throw an error plus information
    about the resulting error.
    """
    sample_input: Incomplete
    error_type: Incomplete
    error_regex: Incomplete
    def __init__(self, sample_input, *, error_type=..., error_regex) -> None: ...

class AliasInfo:
    """Class holds alias information. For example, torch.abs ->
    torch.absolute, torch.Tensor.absolute, torch.Tensor.absolute_
    """
    name: Incomplete
    op: Incomplete
    method_variant: Incomplete
    inplace_variant: Incomplete
    def __init__(self, alias_name) -> None: ...
    def __call__(self, *args, **kwargs): ...

@dataclass
class OpInfo:
    """Operator information and helper functions for acquiring it."""
    name: str
    ref: Callable | None = ...
    aliases: Iterable = ...
    variant_test_name: str = ...
    op: Callable = ...
    method_variant: Callable = ...
    inplace_variant: Callable = ...
    operator_variant: Callable = ...
    inplace_operator_variant: Callable = ...
    skips: Tuple = ...
    decorators: Tuple = ...
    sample_inputs_func: Callable = ...
    reference_inputs_func: Callable = ...
    error_inputs_func: Callable = ...
    sample_inputs_sparse_coo_func: Callable = ...
    sample_inputs_sparse_csr_func: Callable = ...
    sample_inputs_sparse_csc_func: Callable = ...
    sample_inputs_sparse_bsr_func: Callable = ...
    sample_inputs_sparse_bsc_func: Callable = ...
    dtypes: _dispatch_dtypes = ...
    dtypesIfCUDA: _dispatch_dtypes = ...
    dtypesIfROCM: _dispatch_dtypes = ...
    backward_dtypes: _dispatch_dtypes = ...
    backward_dtypesIfCUDA: _dispatch_dtypes = ...
    backward_dtypesIfROCM: _dispatch_dtypes = ...
    supports_out: bool = ...
    supports_autograd: bool = ...
    supports_gradgrad: bool = ...
    supports_fwgrad_bwgrad: bool = ...
    supports_inplace_autograd: bool = ...
    supports_forward_ad: bool = ...
    supports_varargs: bool = ...
    gradcheck_wrapper: Callable = ...
    check_batched_grad: bool = ...
    check_batched_gradgrad: bool = ...
    check_batched_forward_grad: bool = ...
    check_inplace_batched_forward_grad: bool = ...
    gradcheck_nondet_tol: float = ...
    gradcheck_fast_mode: bool = ...
    aten_name: str = ...
    decomp_aten_name: str | None = ...
    aten_backward_name: str | None = ...
    assert_autodiffed: bool = ...
    autodiff_nonfusible_nodes: List[str] = ...
    autodiff_fusible_nodes: List[str] = ...
    supports_sparse: bool = ...
    supports_scripting: bool = ...
    supports_tracing: bool = ...
    supports_sparse_csr: bool = ...
    supports_sparse_csc: bool = ...
    supports_sparse_bsr: bool = ...
    supports_sparse_bsc: bool = ...
    test_conjugated_samples: bool = ...
    test_neg_view: bool = ...
    assert_jit_shape_analysis: bool = ...
    supports_expanded_weight: bool = ...
    is_factory_function: bool = ...
    dynamic_dtypes = ...
    def __post_init__(self): ...
    def __call__(self, *args, **kwargs):
        """Calls the function variant of the operator."""
    def get_op(self):
        """Returns the function variant of the operator, torch.<op_name>."""
    def get_method(self):
        """Returns the method variant of the operator, torch.Tensor.<op_name>.
        Returns None if the operator has no method variant.
        """
    def get_inplace(self):
        """Returns the inplace variant of the operator, torch.Tensor.<op_name>_.
        Returns None if the operator has no inplace variant.
        """
    def get_operator(self):
        """Returns operator variant of the operator, e.g. operator.neg
        Returns None if the operator has no operator variant.
        """
    def get_inplace_operator(self):
        """Returns the inplace operator variant of the operator, e.g operator.iadd
        Returns None if the operator has no inplace operator variant"""
    def conjugate_sample_inputs(self, device, dtype, requires_grad: bool = False, **kwargs):
        """Returns an iterable of SampleInputs but with the tensor input or first
        tensor in a sequence input conjugated.
        """
    def sample_inputs(self, device, dtype, requires_grad: bool = False, **kwargs):
        """
        Returns an iterable of SampleInputs.

        These samples should be sufficient to test the function works correctly
        with autograd, TorchScript, etc.
        """
    def reference_inputs(self, device, dtype, requires_grad: bool = False, **kwargs):
        """
        Returns an iterable of SampleInputs.

        Distinct from sample_inputs() above because this returns an expanded set
        of inputs when reference_inputs_func is defined. If undefined this returns
        the sample inputs.
        """
    def error_inputs(self, device, **kwargs):
        """
        Returns an iterable of ErrorInputs.
        """
    def sample_inputs_sparse(self, layout, device, dtype, requires_grad: bool = False, **kwargs):
        """Returns an iterable of SampleInputs that contain inputs with a
        specified sparse layout.
        """
    def sample_inputs_sparse_coo(self, device, dtype, requires_grad: bool = False, **kwargs):
        """Returns an iterable of SampleInputs that contain inputs with sparse
        coo layout.
        """
    def sample_inputs_sparse_csr(self, device, dtype, requires_grad: bool = False, **kwargs):
        """Returns an iterable of SampleInputs that contain inputs with sparse
        csr layout.
        """
    def sample_inputs_sparse_csc(self, device, dtype, requires_grad: bool = False, **kwargs):
        """Returns an iterable of SampleInputs that contain inputs with sparse
        csc layout.
        """
    def sample_inputs_sparse_bsr(self, device, dtype, requires_grad: bool = False, **kwargs):
        """Returns an iterable of SampleInputs that contain inputs with sparse
        bsr layout.
        """
    def sample_inputs_sparse_bsc(self, device, dtype, requires_grad: bool = False, **kwargs):
        """Returns an iterable of SampleInputs that contain inputs with sparse
        bsc layout.
        """
    def get_decorators(self, test_class, test_name, device, dtype, param_kwargs):
        """Returns the decorators targeting the given test."""
    def supported_dtypes(self, device_type): ...
    def supported_backward_dtypes(self, device_type): ...
    def supports_dtype(self, dtype, device_type): ...
    @property
    def formatted_name(self):
        """Returns a formatted full name for this OpInfo that can be used in test names."""
    def __init__(self, name, ref, aliases, variant_test_name, op, method_variant, inplace_variant, operator_variant, inplace_operator_variant, skips, decorators, sample_inputs_func, reference_inputs_func, error_inputs_func, sample_inputs_sparse_coo_func, sample_inputs_sparse_csr_func, sample_inputs_sparse_csc_func, sample_inputs_sparse_bsr_func, sample_inputs_sparse_bsc_func, dtypes, dtypesIfCUDA, dtypesIfROCM, backward_dtypes, backward_dtypesIfCUDA, backward_dtypesIfROCM, supports_out, supports_autograd, supports_gradgrad, supports_fwgrad_bwgrad, supports_inplace_autograd, supports_forward_ad, supports_varargs, gradcheck_wrapper, check_batched_grad, check_batched_gradgrad, check_batched_forward_grad, check_inplace_batched_forward_grad, gradcheck_nondet_tol, gradcheck_fast_mode, aten_name, decomp_aten_name, aten_backward_name, assert_autodiffed, autodiff_nonfusible_nodes, autodiff_fusible_nodes, supports_sparse, supports_scripting, supports_tracing, supports_sparse_csr, supports_sparse_csc, supports_sparse_bsr, supports_sparse_bsc, test_conjugated_samples, test_neg_view, assert_jit_shape_analysis, supports_expanded_weight, is_factory_function) -> None: ...

def sample_inputs_reduction(op_info, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, Incomplete, Incomplete]:
    """Sample inputs for reduction operators."""

class ReductionOpInfo(OpInfo):
    """Reduction operator information.

    An operator is a reduction operator if it reduces one or more dimensions of
    the input tensor to a single value. Reduction operators must implement the
    following signature:

    - `op(input, *args, *, dim=None, keepdim=False, **kwargs) -> Tensor`

    ReductionOpInfo tests that reduction operators implement a consistent API.
    Optional features such as reducing over multiple dimensions are captured in
    the optional keyword parameters of the ReductionOpInfo constructor.

    If a reduction operator does not yet implement the full required API of
    reduction operators, this should be documented by xfailing the failing
    tests rather than adding optional parameters to ReductionOpInfo.

    NOTE
    The API for reduction operators has not yet been finalized and some
    requirements may change.

    See tests in test/test_reductions.py
    """
    identity: Incomplete
    nan_policy: Incomplete
    supports_multiple_dims: Incomplete
    promotes_int_to_float: Incomplete
    promotes_int_to_int64: Incomplete
    complex_to_real: Incomplete
    result_dtype: Incomplete
    generate_args_kwargs: Incomplete
    def __init__(self, name, *, identity: Any | None = None, nan_policy: str | None = None, supports_multiple_dims: bool = True, promotes_int_to_float: bool = False, promotes_int_to_int64: bool = False, result_dtype: torch.dtype | None = None, complex_to_real: bool = False, generate_args_kwargs: Callable = ..., **kwargs) -> None: ...

def reference_inputs_elementwise_binary(op, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, Incomplete, None]: ...
def make_error_inputs_elementwise_binary(error_inputs_func): ...
def generate_elementwise_binary_tensors(op, *, device, dtype, requires_grad: bool = False, exclude_zero: bool = False) -> Generator[Incomplete, None, None]: ...
def generate_elementwise_binary_arbitrarily_strided_tensors(op, *, device, dtype, requires_grad: bool = False, exclude_zero: bool = False) -> Generator[Incomplete, None, None]: ...
def generate_elementwise_binary_small_value_tensors(op, *, device, dtype, requires_grad: bool = False, exclude_zero: Incomplete | None = None) -> Generator[Incomplete, None, Incomplete]: ...
def generate_elementwise_binary_large_value_tensors(op, *, device, dtype, requires_grad: bool = False) -> Generator[Incomplete, None, Incomplete]: ...
def generate_elementwise_binary_extremal_value_tensors(op, *, device, dtype, requires_grad: bool = False) -> Generator[Incomplete, None, Incomplete]: ...
def generate_elementwise_binary_broadcasting_tensors(op, *, device, dtype, requires_grad: bool = False, exclude_zero: bool = False) -> Generator[Incomplete, None, None]: ...
def generate_elementwise_binary_with_scalar_samples(op, *, device, dtype, requires_grad: bool = False) -> Generator[Incomplete, None, None]: ...
def generate_elementwise_binary_with_scalar_and_type_promotion_samples(op, *, device, dtype, requires_grad: bool = False) -> Generator[Incomplete, None, None]: ...
def generate_elementwise_binary_noncontiguous_tensors(op, *, device, dtype, requires_grad: bool = False, exclude_zero: bool = False) -> Generator[Incomplete, None, None]: ...
def sample_inputs_elementwise_binary(op, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]: ...

class BinaryUfuncInfo(OpInfo):
    """Operator information for 'universal binary functions (binary ufuncs).'
    These are functions of two tensors with common properties like:
      - they are elementwise functions
      - the output shape is determined by the input shape
      - they typically have method and inplace variants
      - they typically support the out kwarg
      - they typically have NumPy or SciPy references
    See NumPy's universal function documentation
    (https://numpy.org/doc/stable/reference/ufuncs.html) for more details
    about the concept of ufuncs.
    """
    lhs_make_tensor_kwargs: Incomplete
    rhs_make_tensor_kwargs: Incomplete
    promotes_int_to_float: Incomplete
    always_returns_bool: Incomplete
    supports_rhs_python_scalar: Incomplete
    supports_one_python_scalar: Incomplete
    supports_two_python_scalars: Incomplete
    def __init__(self, name, *, sample_inputs_func=..., reference_inputs_func=..., error_inputs_func: Incomplete | None = None, lhs_make_tensor_kwargs: Incomplete | None = None, rhs_make_tensor_kwargs: Incomplete | None = None, promotes_int_to_float: bool = False, always_returns_bool: bool = False, supports_rhs_python_scalar: bool = True, supports_one_python_scalar: bool = False, supports_two_python_scalars: bool = False, **kwargs) -> None: ...

def sample_inputs_elementwise_unary(op_info, device, dtype, requires_grad, op_kwargs: Incomplete | None = None, **kwargs) -> Generator[Incomplete, None, None]: ...
def generate_elementwise_unary_tensors(op, *, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, None, None]: ...
def generate_elementwise_unary_small_value_tensors(op, *, device, dtype, requires_grad: bool = False) -> Generator[Incomplete, None, None]: ...
def generate_elementwise_unary_large_value_tensors(op, *, device, dtype, requires_grad: bool = False) -> Generator[Incomplete, None, None]: ...
def generate_elementwise_unary_extremal_value_tensors(op, *, device, dtype, requires_grad: bool = False) -> Generator[Incomplete, None, None]: ...
def generate_elementwise_unary_noncontiguous_tensors(op, *, device, dtype, requires_grad: bool = False) -> Generator[Incomplete, None, None]: ...
def generate_elementwise_unary_arbitrarily_strided_tensors(op, *, device, dtype, requires_grad: bool = False) -> Generator[Incomplete, None, None]: ...
def reference_inputs_elementwise_unary(op, device, dtype, requires_grad, **kwargs) -> Generator[Incomplete, Incomplete, None]: ...

class UnaryUfuncInfo(OpInfo):
    """Operator information for 'universal unary functions (unary ufuncs).'
    These are functions of a single tensor with common properties like:
      - they are elementwise functions
      - the input shape is the output shape
      - they typically have method and inplace variants
      - they typically support the out kwarg
      - they typically have NumPy or SciPy references
    See NumPy's universal function documentation
    (https://numpy.org/doc/1.18/reference/ufuncs.html) for more details
    about the concept of ufuncs.
    """
    domain: Incomplete
    handles_complex_extremal_values: Incomplete
    handles_large_floats: Incomplete
    supports_complex_to_float: Incomplete
    reference_numerics_filter: Incomplete
    sample_kwargs: Incomplete
    def __init__(self, name, *, dtypes=..., domain=(None, None), handles_complex_extremal_values: bool = True, handles_large_floats: bool = True, supports_complex_to_float: bool = False, sample_inputs_func=..., reference_inputs_func=..., sample_kwargs=..., reference_numerics_filter: Incomplete | None = None, **kwargs) -> None: ...

def sample_inputs_spectral_ops(self, device, dtype, requires_grad: bool = False, **kwargs) -> Generator[Incomplete, Incomplete, None]: ...

SpectralFuncType: Incomplete

class SpectralFuncInfo(OpInfo):
    """Operator information for torch.fft transforms."""
    ref: Incomplete
    ndimensional: Incomplete
    def __init__(self, name, *, ref: Incomplete | None = None, dtypes=..., ndimensional: SpectralFuncType, sample_inputs_func=..., decorators: Incomplete | None = None, **kwargs) -> None: ...

class ShapeFuncInfo(OpInfo):
    """Early version of a specialized OpInfo for Shape manipulating operations like tile and roll"""
    ref: Incomplete
    def __init__(self, name, *, ref, dtypes=..., dtypesIfCUDA: Incomplete | None = None, dtypesIfROCM: Incomplete | None = None, sample_inputs_func: Incomplete | None = None, **kwargs) -> None: ...

def sample_inputs_foreach(self, device, dtype, N, *, noncontiguous: bool = False, same_size: bool = False, low: Incomplete | None = None, high: Incomplete | None = None): ...
def get_foreach_method_names(name): ...

class ForeachFuncInfo(OpInfo):
    """Early version of a specialized OpInfo for foreach functions"""
    method_variant: Incomplete
    inplace_variant: Incomplete
    ref: Incomplete
    ref_inplace: Incomplete
    supports_alpha_param: Incomplete
    def __init__(self, name, dtypes=..., dtypesIfCUDA=..., dtypesIfROCM: Incomplete | None = None, supports_alpha_param: bool = False, sample_inputs_func=..., supports_autograd: bool = False, **kwargs) -> None: ...

def gradcheck_wrapper_hermitian_input(op, input, *args, **kwargs):
    """Gradcheck wrapper for functions that take Hermitian matrices as input.

    They require a modified function because the finite-difference algorithm
    for calculating derivatives does not preserve the Hermitian property of the input.
    """
def gradcheck_wrapper_triangular_input(op, *args, upper: bool = False, idx: int = 0, **kwargs):
    """Gradcheck wrapper for functions that take lower or upper triangular matrices as input.

    They require a modified function because the finite-difference algorithm
    for calculating derivatives does not preserve the triangular property of the input.
    `idx` is used to specific which `args[idx]` is to be triangularized.
    """
def gradcheck_wrapper_triangular_input_real_positive_diagonal(op, *args, upper: bool = False, idx: int = 0, **kwargs):
    """Gradcheck wrapper for functions that take lower/upper triangular matrices
    with real and positive diagonals, for example, cholesky-like operations.
    """
def gradcheck_wrapper_masked_operation(op, input, *args, **kwargs):
    """Gradcheck wrapper for masked operations.

    When mask is specified, replaces masked-out elements with zeros.

    Use for operations that produce non-finite masked-out elements,
    for instance, for minimum and maximum reductions.
    """
def gradcheck_wrapper_masked_pointwise_operation(op, input, *args, **kwargs):
    """Gradcheck wrapper for masked pointwise operations. Assumes that the result
    will be masked iff both tensors are masked at a specific index

    When mask is specified, replaces masked-out elements with zeros.

    Use for operations that produce non-finite masked-out elements,
    for instance, for minimum and maximum reductions.
    """
def clone_sample(sample, **kwargs):
    """
    Given a SampleInput, this function analyzes its input, args and kwargs,
    and produces a copy with each non-Tensor entry being copied by reference,
    and with each Tensor entry cloned with `t.clone().requires_grad_(t.requires_grad)`
    """
