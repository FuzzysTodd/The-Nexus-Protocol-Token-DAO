import torch
from _typeshed import Incomplete
from enum import Enum
from functools import cmp_to_key as cmp_to_key
from torch import sym_float as sym_float, sym_int as sym_int, sym_max as sym_max
from typing import Any, Callable, List, Sequence, Tuple, Type, overload

def getnvFuserDtype(dtype: torch.dtype | NumberTypeType):
    """
    Translates from torch.dtype to nvFuser's DataType enum
    """

ShapeType: Incomplete
StrideType = List[int] | Tuple[int, ...]
DimsType = int | List[int] | Tuple[int, ...]
DimsSequenceType = List[int] | Tuple[int, ...]
NumberTypeType = Type[bool] | Type[int] | Type[float] | Type[complex]
NumberType = bool | int | float | complex
Number: Incomplete
Dim = int
IntLike: Incomplete
FloatLike: Incomplete
IntWithoutSymInt = int
FloatWithoutSymFloat = float
DeviceLikeType: Incomplete
Tensor: Incomplete
torch_function_passthrough: Incomplete
TensorLikeType: Incomplete
TensorLike: Incomplete
TensorSequenceType = List[TensorLikeType] | Tuple[TensorLikeType, ...]
TensorOrNumberLikeType = TensorLikeType | NumberType

def same_shape(a: ShapeType, b: ShapeType) -> bool: ...
def compare_tensor_meta(a: TensorLikeType, b: TensorLikeType, check_strides: bool = False):
    """
    Checks that two tensor likes have the same shape,
    dtype and device.

    In the future this will validate additional metadata, like
    strides.
    """
def check_significant_strides(a: TensorLikeType, b: TensorLikeType, *, only_cuda: bool = True) -> Tuple[bool, int | None]: ...
def check_all_strides(a: TensorLikeType, b: TensorLikeType, *, only_cuda: bool = True) -> Tuple[bool, int | None]: ...
def is_contiguous(a: TensorLikeType) -> bool:
    '''
    Tests whether a tensor is contiguous or not.

    Tensors are contiguous when they have no elements,
    one element, or when they have "nested" strides.
    '''
def is_channels_last_contiguous_2d(a: Tensor) -> bool: ...
def is_channels_last_contiguous_3d(a: Tensor) -> bool: ...
def validate_memory_format(memory_format: torch.memory_format): ...
def is_contiguous_for_memory_format(a: Tensor, *, memory_format: torch.memory_format) -> bool: ...
def is_channels_last_contiguous(a: Tensor) -> bool:
    '''
    True when a tensor is channels-last contiguous.

    This requires that:

      - the tensor is conceptually either 4 (NHWC) or 5 (NDHWC) dimensions
      - if we name the tensor\'s dimensions NCHW or NCDHW, then the strides are such that the
        stride of the \'C\' dimension (Cs) is 1 and the strides corresponding to
        each dimension (Xs) can be ordered Cs <= Ws <= Hs <= (Ds) <= Ns and are
        "nested" -- so Ws = Cs * Cl, where Cl is the length of the \'C\' dimension,
        for example.
    '''
def is_non_overlapping_and_dense(a: Tensor) -> bool:
    """
    True when a tensor is non-overlapping and dense.

    A tensor is non-overlapping and dense when there exists a permutation of
    its dimensions that is contiguous.
    """
def compute_elementwise_output_strides(*tensors) -> Tuple[int, ...]:
    """
    Computes the output strides for elementwise operations.
    """
def validate_dim_length(length: int):
    """
    Validates that an object represents a valid
    dimension length.
    """
def validate_shape(shape: ShapeType):
    """
    Validates that a sequence represents a valid shape.
    """
def validate_strides(strides: StrideType):
    """
    Verifies the object specifies valid strides.
    """
def validate_idx(rank: int, idx: int):
    """
    Validates that idx is a valid index for the given shape.
    Assumes the index is already canonicalized.
    """
def validate_dimension_indices(rank: int, indices: DimsSequenceType): ...
def validate_exclusive_idx(rank: int, ex_idx: int):
    """
    Validates that ex_idx is a valid exclusive index
    for the given shape.
    """
def canonicalize_dim(rank: int, idx: int, wrap_scalar: bool = True) -> int: ...
@overload
def canonicalize_dims(rank: int, indices: Sequence[int], wrap_scalar: bool = True) -> Tuple[int, ...]: ...
@overload
def canonicalize_dims(rank: int, indices: int, wrap_scalar: bool = True) -> int: ...
def is_valid_permutation(rank: int, perm: DimsSequenceType) -> bool:
    """
    Validates that perm is a permutation of length rank.
    """
def is_same_shape(a: Sequence, b: Sequence) -> bool:
    """
    Compares two shapes a and b, returning True if they are the same
    (their ranks and corresponding lengths match) and False otherwise.
    """
def is_cpu_scalar_tensor(a: Any) -> bool: ...
def check_same_device(*args, allow_cpu_scalar_tensors) -> None:
    """
    Checks that all Tensors in args have the same device.

    Raises a RuntimeError when:
      - args contains an object whose type is not Tensor or Number
      - two Tensor objects in args have different devices, unless one is a CPU scalar tensor and allow_cpu_scalar_tensors is True
    """
def canonicalize_device(device: DeviceLikeType) -> torch.device: ...
def check_same_shape(*args, allow_cpu_scalar_tensors: bool):
    """
    Checks that all Tensors in args have the same shape.

    Raises a RuntimeError when:
      - args contains an object whose type is not Tensor or Number
      - two Tensor objects in args have different devices
    """
def extract_shape(*args, allow_cpu_scalar_tensors: bool) -> ShapeType | None: ...
def extract_dims_from_varargs(dims: DimsSequenceType | Tuple[DimsSequenceType, ...]) -> DimsSequenceType: ...
def extract_shape_from_varargs(shape: ShapeType | Tuple[ShapeType], validate: bool = True) -> Tuple[int, ...]:
    """
    Returns a shape from varargs.

    In PyTorch, operations that accept shapes often accept them as varargs, like
    foo(*shape). However a user can pass the shape as a sequence of integers,
    like this:

      foo(1, 2, 3)

    or as a sequence of integers

      foo((1, 2, 3))

    In the first case shape will be a tuple of integers, and in the second case it's a tuple
    containing a tuple of integers. This validates those inputs and canonicalizes them
    to a tuple of integers.
    """
def infer_size(shape: ShapeType, numel: int) -> Tuple[int, ...]:
    """
    Infers the size of a dim with size -1, if it exists.
    Also checks that new shape is compatible with the number of elements.
    """
def is_boolean_dtype(dtype: torch.dtype) -> bool: ...
def is_integer_dtype(dtype: torch.dtype) -> bool: ...
def is_low_precision_dtype(dtype: torch.dtype) -> bool: ...
def is_float_dtype(dtype: torch.dtype) -> bool: ...
def is_complex_dtype(dtype: torch.dtype) -> bool: ...
def is_grad_dtype(dtype: torch.dtype) -> bool:
    """
    Checks if the dtype can require a gradient.
    """
def corresponding_real_dtype(dtype: torch.dtype) -> torch.dtype: ...
def corresponding_complex_dtype(dtype: torch.dtype) -> torch.dtype: ...
def dtype_to_type(dtype: torch.dtype) -> type:
    '''
    Computes the corresponding Python type (AKA "type kind") for the
    given dtype.
    '''
def dtype_to_type_ctor(dtype: torch.dtype) -> Callable[[NumberType], NumberType]:
    """
    Computes the corresponding Python type constructor for the
    given dtype.
    """
def type_to_dtype(typ: type) -> torch.dtype:
    """
    Computes the corresponding dtype for a Number type.
    """
def get_dtype(x: torch.Tensor | NumberType): ...
def check_fp_or_complex(dtype: torch.dtype, fn_name: str, allow_low_precision_dtypes: bool = True):
    """
    Checks whether the input is floating point or complex.
    If allow_low_precision_dtypes is True, it allows having float16, bfloat16, and complex32
    """
def check_is_matrix(A: TensorLikeType, f_name: str, arg_name: str = 'A'): ...
def get_higher_type(a: type, b: type) -> type:
    """
    Returns the higher of the two given Number types.

    The types are ordered bool -> int -> float -> complex.
    """
def get_higher_dtype(a: torch.dtype | TensorLikeType | NumberType | None, b: torch.dtype | TensorLikeType | NumberType | None) -> torch.dtype | None:
    '''
    Computes the "lowest" datatype that is weakly
    "higher" than both a and b.
    '''
def check_pin_memory(pin_memory: bool): ...
def check_layout(layout: torch.layout): ...
def is_weakly_lesser_type(a: type, b: type) -> bool:
    '''
    Compares two types, a and b, returning True if a is weakly "less" than b.

    The comparison is determined by the following type ordering: bool, int, float, complex.
    '''
def can_safe_cast_to(*, cast_to: torch.dtype, cast_from: torch.dtype) -> bool: ...
def check_same_dtype(*args) -> None:
    """
    Checks that all Tensors in args have the same device and that all Numbers have the
    same corresponding Python type.

    Raises a RuntimeError when:
      - args contains an object whose type is not Tensor or Number
      - two Tensors objects in args have different dtypes
      - two Number objects in args have different types
      - there are Tensors and Numbers in args, and one of those Tensors corresponding
          Python types is different from the type of one of those Numbers
    """
def get_computation_dtype(dtype: torch.dtype) -> torch.dtype: ...
def get_acc_type(dtype: torch.dtype, device: torch.device) -> torch.dtype: ...

class ELEMENTWISE_TYPE_PROMOTION_KIND(Enum):
    DEFAULT: Incomplete
    NO_OPMATH: Incomplete
    INT_TO_FLOAT: Incomplete
    ALWAYS_BOOL: Incomplete
    COMPLEX_TO_FLOAT: Incomplete
    BOOL_TO_LONG: Incomplete

class REDUCTION_OUTPUT_TYPE_KIND(Enum):
    SAME: Incomplete
    COMPLEX_TO_FLOAT: Incomplete
    KEEP_PROMOTED_TYPE: Incomplete
    ALWAYS_BOOL: Incomplete

class RETURN_TYPE(Enum):
    NEW: Incomplete
    VIEW: Incomplete
    INPLACE: Incomplete

def number_type(x: NumberType | torch.SymInt | torch.SymFloat) -> Type: ...
def elementwise_dtypes(*_args, type_promotion_kind: ELEMENTWISE_TYPE_PROMOTION_KIND) -> Tuple[torch.dtype, torch.dtype]:
    '''
    Computes the computation and result dtypes for elementwise type promotion
    on the given arguments and with the given elementwise type promotion kind.

    Note that not all inputs to an elementwise operation necessarily participate in type promotion.
    For example, the "alpha" parameter of torch.add does not participate in type promotion,
    although it may be cast to the Python type corresponding to the computation dtype that
    the type promotion algorithm determines.

    Default elementwise type promotion, which all other type promotion kinds tweak (see below),
    first decides which of four ordered types to use:

    bool -> integer -> floating point -> complex

    The selected type is the "lowest" type in the above list such that all number arguments
    have a weakly "lower" type and all tensor arguments have a weakly lower corresponding
    type for their dtype.

    Once the type is determined, the particular result dtype is found. The dtypes are
    partially ordered as follows:

    bool -> uint8, int8 -> int16 -> int32 -> int64 ->
      float16, bfloat16 -> float32 -> float64 -> complex32 -> complex64 -> complex128

    The result dtype is selected by:
      - if no tensor\'s dtype has the same corresponding type as the one selected,
          then the result dtype is the (default) dtype corresponding to the selected type
          (for example, 1.5 + an integer tensor has a result dtype of the default floating point dtype)
      - if the result type is complex then the dtype is:
        -  the default complex dtype if there are no floating point or complex tensors
        -  if there are floating point or complex tensors with one or more dimensions, then
            the complex dtype corresponding to the highest corresponding complex dtype among those tensors
            (for example, double + cfloat -> cdouble)
        -  if there are only floating point or complex tensors with zero dimensions, then
            the complex dtype corresponding to the highest corresponding complex dtype among those tensors
      - if the first two cases do not apply, the result dtype is the highest dtype among
          all tensors with one or more dimensions of the output type, and if there are no such
          tensors then it\'s the highest dtype among all tensors with zero dimensions of the output type
          (for example, long + half -> half, even if the half tensor has zero dimensions)

    The "corresponding complex dtypes" are:
      float16    -> complex32
      bfloat16   -> complex64
      float32    -> complex64
      float64    -> complex128
      complex32  -> complex32
      complex64  -> complex64
      complex128 -> complex128

    The DEFAULT type promotion kind computes per above, and then uses the result dtype to pick a computation
    dtype by mapping low precision floating point and complex dtypes as follows:

      float16   -> float32
      bfloat16  -> float32
      complex32 -> complex64

    This is referred to as "op math", and the NO_OPMATH type promotion kind disables this mapping, making the
    computation dtype the same as the result dtype when it\'s selected. NO_OPMATH is appropriate for kernels
    which perform no mathematical operations on their tensors (see below for examples).

    The INT_TO_FLOAT type promotion kind maps boolean and integer maps result dtypes to the default floating point dtype,
    and computation dtypes to the appropriate op math dtype.

    The COMPLEX_TO_FLOAT type promotion kind maps complex result dtypes to the corresponding float dtype, following this
    mapping:

        complex32  -> float16
        complex64  -> float32
        complex128 -> float64

    Note that COMPLEX_TO_FLOAT derives the computation dtype as the DEFAULT setting does.

    The BOOL_TO_LONG type promotion kind maps boolean computation and result dtypes to long.

    The ALWAYS_BOOL type promotion kind always sets the result dtype to bool.

    Example operators for each type promotion option:
      DEFAULT                 : add
      NO_OPMATH               : where, nextafter, cat
      INT_TO_FLOAT            : sin
      COMPLEX_TO_FLOAT        : abs
      BOOL_TO_LONG            : pow
      ALWAYS_BOOL             : eq

    '''
def reduction_dtypes(arg, output_dtype_kind: REDUCTION_OUTPUT_TYPE_KIND, dtype: torch.dtype | None = None) -> Tuple[torch.dtype, torch.dtype | None]: ...
def make_contiguous_strides_for(shape: ShapeType, row_major: bool = True) -> Tuple[int, ...]:
    """
    Returns the strides of a contiguous tensor if row_major
    If row_major=True, it returns the strides of a contiguous batch of Fortran-contiguous matrices
    This is often used when calling external libraries like BLAS/LAPACK/cuSolver...
    """
def make_channels_last_2d_strides_for(shape: ShapeType) -> Tuple[int, ...]: ...
def make_channels_last_3d_strides_for(shape: ShapeType) -> Tuple[int, ...]: ...
def make_channels_last_strides_for(shape: ShapeType) -> Tuple[int, ...]: ...
def compute_reduction_output_shape(shape: ShapeType, dimensions: Sequence) -> Tuple[int, ...]: ...
def validate_no_repeating_dims(dims: Sequence): ...
def reduction_dims(shape: ShapeType, dims: Sequence | None) -> Tuple[int, ...]: ...
def set_correction(unbiased: bool | None = None, correction: int | None = None): ...
def compute_required_storage_length(shape: ShapeType, strides: StrideType, storage_offset: int) -> int:
    """Computes the minimum storage size to hold the given tensor geometry.

    Example
    =======

    This is the size of a newly allocated tensor's storage, in units of elements

    >>> t = torch.empty((10, 20))
    >>> compute_required_storage_length(t.shape, t.stride(), t.storage_offset())
    200

    >>> # xdoctest: +SKIP(failing)
    >>> t2 = torch.empty_strided((1, 2, 3), (5, 7, 11))
    >>> size = compute_required_storage_length(t2.shape, t2.stride(), t2.storage_offset())
    >>> size == t.storage().size()
    True

    A valid tensor may have a larger storage size, but never smaller

    >>> slice = torch.empty(100)[20:40]
    >>> slice.storage().size()
    100

    >>> compute_required_storage_length(slice.shape, slice.stride(), slice.storage_offset())
    40

    """
def check_in_bounds_for_storage(a: torch.TypedStorage, shape: ShapeType, strides: StrideType, storage_offset: int):
    """
    Determines if the given shape, strides, and offset are valid for the given storage.
    """
def check(b: bool, s: Callable[[], str], exc_type: Type[Exception] = ...) -> None:
    """
    Helper function for raising an error_type (default: RuntimeError) if a boolean condition fails.
    Error message is a callable producing a string (to avoid wasting time
    string formatting in non-error case, and also to make it easier for torchdynamo
    to trace.)
    """
def are_strides_like_channels_last(shape: Sequence[int], strides: Sequence[int]) -> bool: ...
def suggest_memory_format(x: TensorLikeType) -> torch.memory_format: ...
def prod(xs: Sequence[NumberType]) -> NumberType:
    """Product of elements in input sequence. Returns 1 for empty sequence"""
def is_expandable_to(shape: ShapeType, desired: ShapeType) -> bool:
    """Checks if a shape can be expanded to another shape.
    This is equivalent to checking if the two shapes are broadcastable.
    """
def mask_tensor(mask: TensorLikeType, t: TensorLikeType):
    """
    Similar to torch.where(mask, t, 0) but if t is boolean,
    result is also boolean and not promoted to int.
    """
def get_aten_op(fn: Callable, name: str):
    """
    Given the __module__ of reference and its name, it returns
    (our best guess of) the ATen name of the associated operation

    Note: In ATen, the __name__ of a function within a module often
    starts by the module name. E.g. linalg_eigh, or special_zeta
    """
def dtype_or_default(dtype: torch.dtype | None) -> torch.dtype: ...
def device_or_default(device: torch.device | None) -> torch.device: ...
def layout_or_default(layout: torch.layout | None) -> torch.layout: ...
def clone_preserve_strides(x): ...
