from torch._C import *
from torch._C._VariableFunctions import *
from .functional import *
import builtins
from ._lobpcg import lobpcg as lobpcg
from ._tensor import Tensor as Tensor
from ._tensor_str import set_printoptions as set_printoptions
from .random import get_rng_state as get_rng_state, initial_seed as initial_seed, manual_seed as manual_seed, seed as seed, set_rng_state as set_rng_state
from .serialization import load as load, save as save
from .storage import TypedStorage as TypedStorage, UntypedStorage as UntypedStorage, _LegacyStorage
from _typeshed import Incomplete
from math import e as e, inf as inf, nan as nan, pi as pi
from torch.autograd import enable_grad as enable_grad, inference_mode as inference_mode, no_grad as no_grad
from torch.func import vmap as vmap
from typing import Any, Callable, Dict

__all__ = ['typename', 'is_tensor', 'is_storage', 'set_default_tensor_type', 'set_default_device', 'set_rng_state', 'get_rng_state', 'manual_seed', 'initial_seed', 'seed', 'save', 'load', 'set_printoptions', 'chunk', 'split', 'stack', 'matmul', 'no_grad', 'enable_grad', 'rand', 'randn', 'inference_mode', 'DoubleStorage', 'FloatStorage', 'LongStorage', 'IntStorage', 'ShortStorage', 'CharStorage', 'ByteStorage', 'BoolStorage', 'TypedStorage', 'UntypedStorage', 'DoubleTensor', 'FloatTensor', 'LongTensor', 'IntTensor', 'ShortTensor', 'CharTensor', 'ByteTensor', 'BoolTensor', 'Tensor', 'lobpcg', 'use_deterministic_algorithms', 'are_deterministic_algorithms_enabled', 'is_deterministic_algorithms_warn_only_enabled', 'set_deterministic_debug_mode', 'get_deterministic_debug_mode', 'set_float32_matmul_precision', 'get_float32_matmul_precision', 'set_warn_always', 'is_warn_always_enabled', 'SymInt', 'SymFloat', 'SymBool', 'sym_not', 'sym_int', 'sym_float', 'sym_max', 'sym_min', 'compile', 'vmap', 'e', 'pi', 'nan', 'inf']

class SymInt:
    """
    Like an int (including magic methods), but redirects all operations on the
    wrapped node. This is used in particular to symbolically record operations
    in the symbolic shape workflow.
    """
    node: Incomplete
    def __init__(self, node) -> None: ...
    def __bool__(self) -> bool: ...
    def __int__(self) -> int: ...
    def __eq__(self, other: object) -> builtins.bool: ...
    def __lt__(self, other) -> builtins.bool: ...
    def __gt__(self, other) -> builtins.bool: ...
    def __le__(self, other) -> builtins.bool: ...
    def __ge__(self, other) -> builtins.bool: ...
    def __sym_max__(self, other) -> None: ...
    def __sym_min__(self, other) -> None: ...
    def __sym_float__(self) -> None: ...

class SymFloat:
    """
    Like an float (including magic methods), but redirects all operations on the
    wrapped node. This is used in particular to symbolically record operations
    in the symbolic shape workflow.
    """
    node: Incomplete
    def __init__(self, node) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> builtins.bool: ...
    def __lt__(self, other) -> builtins.bool: ...
    def __gt__(self, other) -> builtins.bool: ...
    def __le__(self, other) -> builtins.bool: ...
    def __ge__(self, other) -> builtins.bool: ...
    def __sym_max__(self, other) -> None: ...
    def __sym_min__(self, other) -> None: ...
    def __sym_int__(self) -> None: ...

class SymBool:
    """
    Like an bool (including magic methods), but redirects all operations on the
    wrapped node. This is used in particular to symbolically record operations
    in the symbolic shape workflow.

    Unlike regular bools, regular boolean operators will force extra guards instead
    of symbolically evaluate.  Use the bitwise operators instead to handle this.
    """
    node: Incomplete
    def __init__(self, node) -> None: ...
    def __bool__(self) -> bool: ...
    def __and__(self, other) -> SymBool: ...
    def __or__(self, other) -> SymBool: ...
    def __sym_not__(self) -> SymBool: ...

def sym_not(a):
    """ SymInt-aware utility for logical negation.

    Args:
        a (SymBool or bool): Object to negate
    """
def sym_float(a):
    """ SymInt-aware utility for float casting.

    Args:
        a (SymInt, SymFloat, or object): Object to cast
    """
def sym_int(a):
    """ SymInt-aware utility for int casting.

    Args:
        a (SymInt, SymFloat, or object): Object to cast
    """
def sym_max(a, b):
    """ SymInt-aware utility for max()."""
def sym_min(a, b):
    """ SymInt-aware utility for max()."""
def typename(o): ...
def is_tensor(obj):
    """Returns True if `obj` is a PyTorch tensor.

    Note that this function is simply doing ``isinstance(obj, Tensor)``.
    Using that ``isinstance`` check is better for typechecking with mypy,
    and more explicit - so it's recommended to use that instead of
    ``is_tensor``.

    Args:
        obj (Object): Object to test
    Example::

        >>> x = torch.tensor([1, 2, 3])
        >>> torch.is_tensor(x)
        True

    """
def is_storage(obj):
    """Returns True if `obj` is a PyTorch storage object.

    Args:
        obj (Object): Object to test
    """
def set_default_device(device) -> None:
    '''Sets the default ``torch.Tensor`` to be allocated on ``device``.  This
    does not affect factory function calls which are called with an explicit
    ``device`` argument.  Factory calls will be performed as if they
    were passed ``device`` as an argument.

    To only temporarily change the default device instead of setting it
    globally, use ``with torch.device(device):`` instead.

    The default device is initially ``cpu``.  If you set the default tensor
    device to another device (e.g., ``cuda``) without a device index, tensors
    will be allocated on whatever the current device for the device type,
    even after :func:`torch.cuda.set_device` is called.

    .. warning::

        This function imposes a slight performance cost on every Python
        call to the torch API (not just factory functions).  If this
        is causing problems for you, please comment on
        https://github.com/pytorch/pytorch/issues/92701

    Args:
        device (device or string): the device to set as default

    Example::

        >>> # xdoctest: +SKIP("requires cuda, changes global state")
        >>> torch.tensor([1.2, 3]).device
        device(type=\'cpu\')
        >>> torch.set_default_device(\'cuda\')  # current device is 0
        >>> torch.tensor([1.2, 3]).device
        device(type=\'cuda\', index=0)
        >>> torch.set_default_device(\'cuda:1\')
        >>> torch.tensor([1.2, 3]).device
        device(type=\'cuda\', index=1)

    '''
def set_default_tensor_type(t) -> None:
    '''Sets the default ``torch.Tensor`` type to floating point tensor type
    ``t``. This type will also be used as default floating point type for
    type inference in :func:`torch.tensor`.

    The default floating point tensor type is initially ``torch.FloatTensor``.

    Args:
        t (type or string): the floating point tensor type or its name

    Example::

        >>> # xdoctest: +SKIP("Other tests may have changed the default type. Can we reset it?")
        >>> torch.tensor([1.2, 3]).dtype    # initial default for floating point is torch.float32
        torch.float32
        >>> torch.set_default_tensor_type(torch.DoubleTensor)
        >>> torch.tensor([1.2, 3]).dtype    # a new floating point tensor
        torch.float64

    '''
def use_deterministic_algorithms(mode, *, warn_only: bool = False) -> None:
    ''' Sets whether PyTorch operations must use "deterministic"
    algorithms. That is, algorithms which, given the same input, and when
    run on the same software and hardware, always produce the same output.
    When enabled, operations will use deterministic algorithms when available,
    and if only nondeterministic algorithms are available they will throw a
    :class:`RuntimeError` when called.

    .. note:: This setting alone is not always enough to make an application
        reproducible. Refer to :ref:`reproducibility` for more information.

    .. note:: :func:`torch.set_deterministic_debug_mode` offers an alternative
        interface for this feature.

    The following normally-nondeterministic operations will act
    deterministically when ``mode=True``:

        * :class:`torch.nn.Conv1d` when called on CUDA tensor
        * :class:`torch.nn.Conv2d` when called on CUDA tensor
        * :class:`torch.nn.Conv3d` when called on CUDA tensor
        * :class:`torch.nn.ConvTranspose1d` when called on CUDA tensor
        * :class:`torch.nn.ConvTranspose2d` when called on CUDA tensor
        * :class:`torch.nn.ConvTranspose3d` when called on CUDA tensor
        * :func:`torch.bmm` when called on sparse-dense CUDA tensors
        * :func:`torch.Tensor.__getitem__` when attempting to differentiate a CPU tensor
          and the index is a list of tensors
        * :func:`torch.Tensor.index_put` with ``accumulate=False``
        * :func:`torch.Tensor.index_put` with ``accumulate=True`` when called on a CPU
          tensor
        * :func:`torch.Tensor.put_` with ``accumulate=True`` when called on a CPU
          tensor
        * :func:`torch.Tensor.scatter_add_` when called on a CUDA tensor
        * :func:`torch.gather` when called on a CUDA tensor that requires grad
        * :func:`torch.index_add` when called on CUDA tensor
        * :func:`torch.index_select` when attempting to differentiate a CUDA tensor
        * :func:`torch.repeat_interleave` when attempting to differentiate a CUDA tensor
        * :func:`torch.Tensor.index_copy` when called on a CPU or CUDA tensor

    The following normally-nondeterministic operations will throw a
    :class:`RuntimeError` when ``mode=True``:

        * :class:`torch.nn.AvgPool3d` when attempting to differentiate a CUDA tensor
        * :class:`torch.nn.AdaptiveAvgPool2d` when attempting to differentiate a CUDA tensor
        * :class:`torch.nn.AdaptiveAvgPool3d` when attempting to differentiate a CUDA tensor
        * :class:`torch.nn.MaxPool3d` when attempting to differentiate a CUDA tensor
        * :class:`torch.nn.AdaptiveMaxPool2d` when attempting to differentiate a CUDA tensor
        * :class:`torch.nn.FractionalMaxPool2d` when attempting to differentiate a CUDA tensor
        * :class:`torch.nn.FractionalMaxPool3d` when attempting to differentiate a CUDA tensor
        * :class:`torch.nn.MaxUnpool1d`
        * :class:`torch.nn.MaxUnpool2d`
        * :class:`torch.nn.MaxUnpool3d`
        * :func:`torch.nn.functional.interpolate` when attempting to differentiate a CUDA tensor
          and one of the following modes is used:

          - ``linear``
          - ``bilinear``
          - ``bicubic``
          - ``trilinear``

        * :class:`torch.nn.ReflectionPad1d` when attempting to differentiate a CUDA tensor
        * :class:`torch.nn.ReflectionPad2d` when attempting to differentiate a CUDA tensor
        * :class:`torch.nn.ReflectionPad3d` when attempting to differentiate a CUDA tensor
        * :class:`torch.nn.ReplicationPad1d` when attempting to differentiate a CUDA tensor
        * :class:`torch.nn.ReplicationPad2d` when attempting to differentiate a CUDA tensor
        * :class:`torch.nn.ReplicationPad3d` when attempting to differentiate a CUDA tensor
        * :class:`torch.nn.NLLLoss` when called on a CUDA tensor
        * :class:`torch.nn.CTCLoss` when attempting to differentiate a CUDA tensor
        * :class:`torch.nn.EmbeddingBag` when attempting to differentiate a CUDA tensor when
          ``mode=\'max\'``
        * :func:`torch.Tensor.put_` when ``accumulate=False``
        * :func:`torch.Tensor.put_` when ``accumulate=True`` and called on a CUDA tensor
        * :func:`torch.histc` when called on a CUDA tensor
        * :func:`torch.bincount` when called on a CUDA tensor
        * :func:`torch.kthvalue` with called on a CUDA tensor
        * :func:`torch.median` with indices output when called on a CUDA tensor
        * :func:`torch.nn.functional.grid_sample` when attempting to differentiate a CUDA tensor
        * :func:`torch.cumsum` when called on a CUDA tensor when dtype is floating point or complex

    A handful of CUDA operations are nondeterministic if the CUDA version is
    10.2 or greater, unless the environment variable ``CUBLAS_WORKSPACE_CONFIG=:4096:8``
    or ``CUBLAS_WORKSPACE_CONFIG=:16:8`` is set. See the CUDA documentation for more
    details: `<https://docs.nvidia.com/cuda/cublas/index.html#cublasApi_reproducibility>`_
    If one of these environment variable configurations is not set, a :class:`RuntimeError`
    will be raised from these operations when called with CUDA tensors:

        * :func:`torch.mm`
        * :func:`torch.mv`
        * :func:`torch.bmm`

    Note that deterministic operations tend to have worse performance than
    nondeterministic operations.

    .. note::

        This flag does not detect or prevent nondeterministic behavior caused
        by calling an inplace operation on a tensor with an internal memory
        overlap or by giving such a tensor as the :attr:`out` argument for an
        operation. In these cases, multiple writes of different data may target
        a single memory location, and the order of writes is not guaranteed.

    Args:
        mode (:class:`bool`): If True, makes potentially nondeterministic
            operations switch to a deterministic algorithm or throw a runtime
            error. If False, allows nondeterministic operations.

    Keyword args:
        warn_only (:class:`bool`, optional): If True, operations that do not
            have a deterministic implementation will throw a warning instead of
            an error. Default: ``False``

    Example::

        >>> # xdoctest: +SKIP
        >>> torch.use_deterministic_algorithms(True)

        # Forward mode nondeterministic error
        >>> torch.randn(10, device=\'cuda\').kthvalue(0)
        ...
        RuntimeError: kthvalue CUDA does not have a deterministic implementation...

        # Backward mode nondeterministic error
        >>> torch.nn.AvgPool3d(1)(torch.randn(3, 4, 5, 6, requires_grad=True).cuda()).sum().backward()
        ...
        RuntimeError: avg_pool3d_backward_cuda does not have a deterministic implementation...
    '''
def are_deterministic_algorithms_enabled():
    """Returns True if the global deterministic flag is turned on. Refer to
    :func:`torch.use_deterministic_algorithms` documentation for more details.
    """
def is_deterministic_algorithms_warn_only_enabled():
    """Returns True if the global deterministic flag is set to warn only.
    Refer to :func:`torch.use_deterministic_algorithms` documentation for more
    details.
    """
def set_deterministic_debug_mode(debug_mode: builtins.int | str) -> None:
    '''Sets the debug mode for deterministic operations.

    .. note:: This is an alternative interface for
        :func:`torch.use_deterministic_algorithms`. Refer to that function\'s
        documentation for details about affected operations.

    Args:
        debug_mode(str or int): If "default" or 0, don\'t error or warn on
            nondeterministic operations. If "warn" or 1, warn on
            nondeterministic operations. If "error" or 2, error on
            nondeterministic operations.
    '''
def get_deterministic_debug_mode() -> builtins.int:
    """Returns the current value of the debug mode for deterministic
    operations. Refer to :func:`torch.set_deterministic_debug_mode`
    documentation for more details.
    """
def get_float32_matmul_precision() -> builtins.str:
    """Returns the current value of float32 matrix multiplication precision. Refer to
    :func:`torch.set_float32_matmul_precision` documentation for more details.
    """
def set_float32_matmul_precision(precision) -> None:
    '''Sets the internal precision of float32 matrix multiplications.

    Running float32 matrix multiplications in lower precision may significantly increase
    performance, and in some programs the loss of precision has a negligible impact.

    Supports three settings:

        * "highest", float32 matrix multiplications use the float32 datatype for
          internal computations.
        * "high", float32 matrix multiplications use the TensorFloat32 or bfloat16_3x
          datatypes for internal computations, if fast matrix multiplication algorithms
          using those datatypes internally are available. Otherwise float32
          matrix multiplications are computed as if the precision is "highest".
        * "medium", float32 matrix multiplications use the bfloat16 datatype for
          internal computations, if a fast matrix multiplication algorithm
          using that datatype internally is available. Otherwise float32
          matrix multiplications are computed as if the precision is "high".

    .. note::

        This does not change the output dtype of float32 matrix multiplications,
        it controls how the internal computation of the matrix multiplication is performed.

    .. note::

        This does not change the precision of convolution operations. Other flags,
        like `torch.backends.cudnn.allow_tf32`, may control the precision of convolution
        operations.

    .. note::

        This flag currently only affects one native device type: CUDA.
        If "high" or "medium" are set then the TensorFloat32 datatype will be used
        when computing float32 matrix multiplications, equivalent to setting
        `torch.backends.cuda.matmul.allow_tf32 = True`. When "highest" (the default)
        is set then the float32 datatype is used for internal computations, equivalent
        to setting `torch.backends.cuda.matmul.allow_tf32 = False`.

    Args:
        precision(str): can be set to "highest" (default), "high", or "medium" (see above).

    '''
def set_warn_always(b) -> None:
    """When this flag is False (default) then some PyTorch warnings may only
    appear once per process. This helps avoid excessive warning information.
    Setting it to True causes these warnings to always appear, which may be
    helpful when debugging.

    Args:
        b (:class:`bool`): If True, force warnings to always be emitted
                           If False, set to the default behaviour
    """
def is_warn_always_enabled():
    """Returns True if the global warn_always flag is turned on. Refer to
    :func:`torch.set_warn_always` documentation for more details.
    """

class ByteStorage(_LegacyStorage):
    def dtype(self): ...

class DoubleStorage(_LegacyStorage):
    def dtype(self): ...

class FloatStorage(_LegacyStorage):
    def dtype(self): ...

class HalfStorage(_LegacyStorage):
    def dtype(self): ...

class LongStorage(_LegacyStorage):
    def dtype(self): ...

class IntStorage(_LegacyStorage):
    def dtype(self): ...

class ShortStorage(_LegacyStorage):
    def dtype(self): ...

class CharStorage(_LegacyStorage):
    def dtype(self): ...

class BoolStorage(_LegacyStorage):
    def dtype(self): ...

class BFloat16Storage(_LegacyStorage):
    def dtype(self): ...

class ComplexDoubleStorage(_LegacyStorage):
    def dtype(self): ...

class ComplexFloatStorage(_LegacyStorage):
    def dtype(self): ...

class QUInt8Storage(_LegacyStorage):
    def dtype(self): ...

class QInt8Storage(_LegacyStorage):
    def dtype(self): ...

class QInt32Storage(_LegacyStorage):
    def dtype(self): ...

class QUInt4x2Storage(_LegacyStorage):
    def dtype(self): ...

class QUInt2x4Storage(_LegacyStorage):
    def dtype(self): ...
py_float = float
py_int = int
legacy_contiguous_format = contiguous_format

class _TorchCompileInductorWrapper:
    compiler_name: str
    config: Incomplete
    dynamic: Incomplete
    def __init__(self, mode, options, dynamic) -> None: ...
    def __eq__(self, other): ...
    def apply_mode(self, mode: str | None): ...
    def apply_options(self, options: Dict[str, Any] | None): ...
    def __call__(self, model_, inputs_): ...

def compile(model: Callable | None = None, *, fullgraph: builtins.bool = False, dynamic: builtins.bool = False, backend: str | Callable = 'inductor', mode: str | None = None, options: Dict[str, str | builtins.int | builtins.bool] | None = None, disable: builtins.bool = False) -> Callable:
    '''
    Optimizes given model/function using TorchDynamo and specified backend.

    Args:
       model (Callable): Module/function to optimize
       fullgraph (bool): Whether it is ok to break model into several subgraphs
       dynamic (bool): Use dynamic shape tracing
       backend (str or Callable): backend to be used
       mode (str): Can be either "default", "reduce-overhead" or "max-autotune"
       options (dict): A dictionary of options to pass to the backend.
       disable (bool): Turn torch.compile() into a no-op for testing

    Example::

        @torch.compile(options={"matmul-padding": True}, fullgraph=True)
        def foo(x):
            return torch.sin(x) + torch.cos(x)

    '''

# Names in __all__ with no definition:
#   BoolTensor
#   ByteTensor
#   CharTensor
#   DoubleTensor
#   FloatTensor
#   IntTensor
#   LongTensor
#   ShortTensor
#   chunk
#   matmul
#   rand
#   randn
#   split
#   stack
