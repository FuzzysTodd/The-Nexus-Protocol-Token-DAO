import abc
import torch
from _typeshed import Incomplete
from typing import Any, Callable, Dict, List, Sequence, Tuple, Type

NUMPY_AVAILABLE: bool

class ErrorMeta(Exception):
    """Internal testing exception that makes that carries error metadata."""
    type: Incomplete
    msg: Incomplete
    id: Incomplete
    def __init__(self, type: Type[Exception], msg: str, *, id: Tuple[Any, ...] = ()) -> None: ...
    def to_error(self, msg: str | Callable[[str], str] | None = None) -> Exception: ...

def default_tolerances(*inputs: torch.Tensor | torch.dtype, dtype_precisions: Dict[torch.dtype, Tuple[float, float]] | None = None) -> Tuple[float, float]:
    """Returns the default absolute and relative testing tolerances for a set of inputs based on the dtype.

    See :func:`assert_close` for a table of the default tolerance for each dtype.

    Returns:
        (Tuple[float, float]): Loosest tolerances of all input dtypes.
    """
def get_tolerances(*inputs: torch.Tensor | torch.dtype, rtol: float | None, atol: float | None, id: Tuple[Any, ...] = ()) -> Tuple[float, float]:
    """Gets absolute and relative to be used for numeric comparisons.

    If both ``rtol`` and ``atol`` are specified, this is a no-op. If both are not specified, the return value of
    :func:`default_tolerances` is used.

    Raises:
        ErrorMeta: With :class:`ValueError`, if only ``rtol`` or ``atol`` is specified.

    Returns:
        (Tuple[float, float]): Valid absolute and relative tolerances.
    """
def make_scalar_mismatch_msg(actual: int | float | complex, expected: int | float | complex, *, rtol: float, atol: float, identifier: str | Callable[[str], str] | None = None) -> str:
    '''Makes a mismatch error message for scalars.

    Args:
        actual (Union[int, float, complex]): Actual scalar.
        expected (Union[int, float, complex]): Expected scalar.
        rtol (float): Relative tolerance.
        atol (float): Absolute tolerance.
        identifier (Optional[Union[str, Callable[[str], str]]]): Optional description for the scalars. Can be passed
            as callable in which case it will be called by the default value to create the description at runtime.
            Defaults to "Scalars".
    '''
def make_tensor_mismatch_msg(actual: torch.Tensor, expected: torch.Tensor, mismatches: torch.Tensor, *, rtol: float, atol: float, identifier: str | Callable[[str], str] | None = None):
    '''Makes a mismatch error message for tensors.

    Args:
        actual (torch.Tensor): Actual tensor.
        expected (torch.Tensor): Expected tensor.
        mismatches (torch.Tensor): Boolean mask of the same shape as ``actual`` and ``expected`` that indicates the
            location of mismatches.
        rtol (float): Relative tolerance.
        atol (float): Absolute tolerance.
        identifier (Optional[Union[str, Callable[[str], str]]]): Optional description for the tensors. Can be passed
            as callable in which case it will be called by the default value to create the description at runtime.
            Defaults to "Tensor-likes".
    '''

class UnsupportedInputs(Exception):
    """Exception to be raised during the construction of a :class:`Pair` in case it doesn't support the inputs."""

class Pair(abc.ABC, metaclass=abc.ABCMeta):
    """ABC for all comparison pairs to be used in conjunction with :func:`assert_equal`.

    Each subclass needs to overwrite :meth:`Pair.compare` that performs the actual comparison.

    Each pair receives **all** options, so select the ones applicable for the subclass and forward the rest to the
    super class. Raising an :class:`UnsupportedInputs` during constructions indicates that the pair is not able to
    handle the inputs and the next pair type will be tried.

    All other errors should be raised as :class:`ErrorMeta`. After the instantiation, :meth:`Pair._make_error_meta` can
    be used to automatically handle overwriting the message with a user supplied one and id handling.
    """
    actual: Incomplete
    expected: Incomplete
    id: Incomplete
    def __init__(self, actual: Any, expected: Any, *, id: Tuple[Any, ...] = (), **unknown_parameters: Any) -> None: ...
    @abc.abstractmethod
    def compare(self) -> None:
        """Compares the inputs and raises an :class`ErrorMeta` in case they mismatch."""
    def extra_repr(self) -> Sequence[str | Tuple[str, Any]]:
        """Returns extra information that will be included in the representation.

        Should be overwritten by all subclasses that use additional options. The representation of the object will only
        be surfaced in case we encounter an unexpected error and thus should help debug the issue. Can be a sequence of
        key-value-pairs or attribute names.
        """

class ObjectPair(Pair):
    """Pair for any type of inputs that will be compared with the `==` operator.

    .. note::

        Since this will instantiate for any kind of inputs, it should only be used as fallback after all other pairs
        couldn't handle the inputs.

    """
    def compare(self) -> None: ...

class NonePair(Pair):
    """Pair for ``None`` inputs."""
    def __init__(self, actual: Any, expected: Any, **other_parameters: Any) -> None: ...
    def compare(self) -> None: ...

class BooleanPair(Pair):
    """Pair for :class:`bool` inputs.

    .. note::

        If ``numpy`` is available, also handles :class:`numpy.bool_` inputs.

    """
    def __init__(self, actual: Any, expected: Any, *, id: Tuple[Any, ...], **other_parameters: Any) -> None: ...
    def compare(self) -> None: ...

class NumberPair(Pair):
    """Pair for Python number (:class:`int`, :class:`float`, and :class:`complex`) inputs.

    .. note::

        If ``numpy`` is available, also handles :class:`numpy.number` inputs.

    Kwargs:
        rtol (Optional[float]): Relative tolerance. If specified ``atol`` must also be specified. If omitted, default
            values based on the type are selected with the below table.
        atol (Optional[float]): Absolute tolerance. If specified ``rtol`` must also be specified. If omitted, default
            values based on the type are selected with the below table.
        equal_nan (bool): If ``True``, two ``NaN`` values are considered equal. Defaults to ``False``.
        check_dtype (bool): If ``True``, the type of the inputs will be checked for equality. Defaults to ``False``.

    The following table displays correspondence between Python number type and the ``torch.dtype``'s. See
    :func:`assert_close` for the corresponding tolerances.

    +------------------+-------------------------------+
    | ``type``         | corresponding ``torch.dtype`` |
    +==================+===============================+
    | :class:`int`     | :attr:`~torch.int64`          |
    +------------------+-------------------------------+
    | :class:`float`   | :attr:`~torch.float64`        |
    +------------------+-------------------------------+
    | :class:`complex` | :attr:`~torch.complex64`      |
    +------------------+-------------------------------+
    """
    equal_nan: Incomplete
    check_dtype: Incomplete
    def __init__(self, actual: Any, expected: Any, *, id: Tuple[Any, ...] = (), rtol: float | None = None, atol: float | None = None, equal_nan: bool = False, check_dtype: bool = False, **other_parameters: Any) -> None: ...
    def compare(self) -> None: ...
    def extra_repr(self) -> Sequence[str]: ...

class TensorLikePair(Pair):
    """Pair for :class:`torch.Tensor`-like inputs.

    Kwargs:
        allow_subclasses (bool):
        rtol (Optional[float]): Relative tolerance. If specified ``atol`` must also be specified. If omitted, default
            values based on the type are selected. See :func:assert_close: for details.
        atol (Optional[float]): Absolute tolerance. If specified ``rtol`` must also be specified. If omitted, default
            values based on the type are selected. See :func:assert_close: for details.
        equal_nan (bool): If ``True``, two ``NaN`` values are considered equal. Defaults to ``False``.
        check_device (bool): If ``True`` (default), asserts that corresponding tensors are on the same
            :attr:`~torch.Tensor.device`. If this check is disabled, tensors on different
            :attr:`~torch.Tensor.device`'s are moved to the CPU before being compared.
        check_dtype (bool): If ``True`` (default), asserts that corresponding tensors have the same ``dtype``. If this
            check is disabled, tensors with different ``dtype``'s are promoted  to a common ``dtype`` (according to
            :func:`torch.promote_types`) before being compared.
        check_layout (bool): If ``True`` (default), asserts that corresponding tensors have the same ``layout``. If this
            check is disabled, tensors with different ``layout``'s are converted to strided tensors before being
            compared.
        check_stride (bool): If ``True`` and corresponding tensors are strided, asserts that they have the same stride.
    """
    equal_nan: Incomplete
    check_device: Incomplete
    check_dtype: Incomplete
    check_layout: Incomplete
    check_stride: Incomplete
    def __init__(self, actual: Any, expected: Any, *, id: Tuple[Any, ...] = (), allow_subclasses: bool = True, rtol: float | None = None, atol: float | None = None, equal_nan: bool = False, check_device: bool = True, check_dtype: bool = True, check_layout: bool = True, check_stride: bool = False, **other_parameters: Any) -> None: ...
    def compare(self) -> None: ...
    def extra_repr(self) -> Sequence[str]: ...

def originate_pairs(actual: Any, expected: Any, *, pair_types: Sequence[Type[Pair]], sequence_types: Tuple[Type, ...] = ..., mapping_types: Tuple[Type, ...] = ..., id: Tuple[Any, ...] = (), **options: Any) -> List[Pair]:
    """Originates pairs from the individual inputs.

    ``actual`` and ``expected`` can be possibly nested :class:`~collections.abc.Sequence`'s or
    :class:`~collections.abc.Mapping`'s. In this case the pairs are originated by recursing through them.

    Args:
        actual (Any): Actual input.
        expected (Any): Expected input.
        pair_types (Sequence[Type[Pair]]): Sequence of pair types that will be tried to construct with the inputs.
            First successful pair will be used.
        sequence_types (Tuple[Type, ...]): Optional types treated as sequences that will be checked elementwise.
        mapping_types (Tuple[Type, ...]): Optional types treated as mappings that will be checked elementwise.
        id (Tuple[Any, ...]): Optional id of a pair that will be included in an error message.
        **options (Any): Options passed to each pair during construction.

    Raises:
        ErrorMeta: With :class`AssertionError`, if the inputs are :class:`~collections.abc.Sequence`'s, but their
            length does not match.
        ErrorMeta: With :class`AssertionError`, if the inputs are :class:`~collections.abc.Mapping`'s, but their set of
            keys do not match.
        ErrorMeta: With :class`TypeError`, if no pair is able to handle the inputs.
        ErrorMeta: With any expected exception that happens during the construction of a pair.

    Returns:
        (List[Pair]): Originated pairs.
    """
def not_close_error_metas(actual: Any, expected: Any, *, pair_types: Sequence[Type[Pair]] = ..., sequence_types: Tuple[Type, ...] = ..., mapping_types: Tuple[Type, ...] = ..., **options: Any) -> List[ErrorMeta]:
    """Asserts that inputs are equal.

    ``actual`` and ``expected`` can be possibly nested :class:`~collections.abc.Sequence`'s or
    :class:`~collections.abc.Mapping`'s. In this case the comparison happens elementwise by recursing through them.

    Args:
        actual (Any): Actual input.
        expected (Any): Expected input.
        pair_types (Sequence[Type[Pair]]): Sequence of :class:`Pair` types that will be tried to construct with the
            inputs. First successful pair will be used. Defaults to only using :class:`ObjectPair`.
        sequence_types (Tuple[Type, ...]): Optional types treated as sequences that will be checked elementwise.
        mapping_types (Tuple[Type, ...]): Optional types treated as mappings that will be checked elementwise.
        **options (Any): Options passed to each pair during construction.
    """
def assert_close(actual: Any, expected: Any, *, allow_subclasses: bool = True, rtol: float | None = None, atol: float | None = None, equal_nan: bool = False, check_device: bool = True, check_dtype: bool = True, check_layout: bool = True, check_stride: bool = False, msg: str | Callable[[str], str] | None = None):
    '''Asserts that ``actual`` and ``expected`` are close.

    If ``actual`` and ``expected`` are strided, non-quantized, real-valued, and finite, they are considered close if

    .. math::

        \\lvert \\text{actual} - \\text{expected} \\rvert \\le \\texttt{atol} + \\texttt{rtol} \\cdot \\lvert \\text{expected} \\rvert

    Non-finite values (``-inf`` and ``inf``) are only considered close if and only if they are equal. ``NaN``\'s are
    only considered equal to each other if ``equal_nan`` is ``True``.

    In addition, they are only considered close if they have the same

    - :attr:`~torch.Tensor.device` (if ``check_device`` is ``True``),
    - ``dtype`` (if ``check_dtype`` is ``True``),
    - ``layout`` (if ``check_layout`` is ``True``), and
    - stride (if ``check_stride`` is ``True``).

    If either ``actual`` or ``expected`` is a meta tensor, only the attribute checks will be performed.

    If ``actual`` and ``expected`` are sparse (either having COO, CSR, CSC, BSR, or BSC layout), their strided members are
    checked individually. Indices, namely ``indices`` for COO, ``crow_indices`` and ``col_indices`` for CSR and BSR,
    or ``ccol_indices``  and ``row_indices`` for CSC and BSC layouts, respectively,
    are always checked for equality whereas the values are checked for closeness according to the definition above.

    If ``actual`` and ``expected`` are quantized, they are considered close if they have the same
    :meth:`~torch.Tensor.qscheme` and the result of :meth:`~torch.Tensor.dequantize` is close according to the
    definition above.

    ``actual`` and ``expected`` can be :class:`~torch.Tensor`\'s or any tensor-or-scalar-likes from which
    :class:`torch.Tensor`\'s can be constructed with :func:`torch.as_tensor`. Except for Python scalars the input types
    have to be directly related. In addition, ``actual`` and ``expected`` can be :class:`~collections.abc.Sequence`\'s
    or :class:`~collections.abc.Mapping`\'s in which case they are considered close if their structure matches and all
    their elements are considered close according to the above definition.

    .. note::

        Python scalars are an exception to the type relation requirement, because their :func:`type`, i.e.
        :class:`int`, :class:`float`, and :class:`complex`, is equivalent to the ``dtype`` of a tensor-like. Thus,
        Python scalars of different types can be checked, but require ``check_dtype=False``.

    Args:
        actual (Any): Actual input.
        expected (Any): Expected input.
        allow_subclasses (bool): If ``True`` (default) and except for Python scalars, inputs of directly related types
            are allowed. Otherwise type equality is required.
        rtol (Optional[float]): Relative tolerance. If specified ``atol`` must also be specified. If omitted, default
            values based on the :attr:`~torch.Tensor.dtype` are selected with the below table.
        atol (Optional[float]): Absolute tolerance. If specified ``rtol`` must also be specified. If omitted, default
            values based on the :attr:`~torch.Tensor.dtype` are selected with the below table.
        equal_nan (Union[bool, str]): If ``True``, two ``NaN`` values will be considered equal.
        check_device (bool): If ``True`` (default), asserts that corresponding tensors are on the same
            :attr:`~torch.Tensor.device`. If this check is disabled, tensors on different
            :attr:`~torch.Tensor.device`\'s are moved to the CPU before being compared.
        check_dtype (bool): If ``True`` (default), asserts that corresponding tensors have the same ``dtype``. If this
            check is disabled, tensors with different ``dtype``\'s are promoted  to a common ``dtype`` (according to
            :func:`torch.promote_types`) before being compared.
        check_layout (bool): If ``True`` (default), asserts that corresponding tensors have the same ``layout``. If this
            check is disabled, tensors with different ``layout``\'s are converted to strided tensors before being
            compared.
        check_stride (bool): If ``True`` and corresponding tensors are strided, asserts that they have the same stride.
        msg (Optional[Union[str, Callable[[str], str]]]): Optional error message to use in case a failure occurs during
            the comparison. Can also passed as callable in which case it will be called with the generated message and
            should return the new message.

    Raises:
        ValueError: If no :class:`torch.Tensor` can be constructed from an input.
        ValueError: If only ``rtol`` or ``atol`` is specified.
        AssertionError: If corresponding inputs are not Python scalars and are not directly related.
        AssertionError: If ``allow_subclasses`` is ``False``, but corresponding inputs are not Python scalars and have
            different types.
        AssertionError: If the inputs are :class:`~collections.abc.Sequence`\'s, but their length does not match.
        AssertionError: If the inputs are :class:`~collections.abc.Mapping`\'s, but their set of keys do not match.
        AssertionError: If corresponding tensors do not have the same :attr:`~torch.Tensor.shape`.
        AssertionError: If ``check_layout`` is ``True``, but corresponding tensors do not have the same
            :attr:`~torch.Tensor.layout`.
        AssertionError: If only one of corresponding tensors is quantized.
        AssertionError: If corresponding tensors are quantized, but have different :meth:`~torch.Tensor.qscheme`\'s.
        AssertionError: If ``check_device`` is ``True``, but corresponding tensors are not on the same
            :attr:`~torch.Tensor.device`.
        AssertionError: If ``check_dtype`` is ``True``, but corresponding tensors do not have the same ``dtype``.
        AssertionError: If ``check_stride`` is ``True``, but corresponding strided tensors do not have the same stride.
        AssertionError: If the values of corresponding tensors are not close according to the definition above.

    The following table displays the default ``rtol`` and ``atol`` for different ``dtype``\'s. In case of mismatching
    ``dtype``\'s, the maximum of both tolerances is used.

    +---------------------------+------------+----------+
    | ``dtype``                 | ``rtol``   | ``atol`` |
    +===========================+============+==========+
    | :attr:`~torch.float16`    | ``1e-3``   | ``1e-5`` |
    +---------------------------+------------+----------+
    | :attr:`~torch.bfloat16`   | ``1.6e-2`` | ``1e-5`` |
    +---------------------------+------------+----------+
    | :attr:`~torch.float32`    | ``1.3e-6`` | ``1e-5`` |
    +---------------------------+------------+----------+
    | :attr:`~torch.float64`    | ``1e-7``   | ``1e-7`` |
    +---------------------------+------------+----------+
    | :attr:`~torch.complex32`  | ``1e-3``   | ``1e-5`` |
    +---------------------------+------------+----------+
    | :attr:`~torch.complex64`  | ``1.3e-6`` | ``1e-5`` |
    +---------------------------+------------+----------+
    | :attr:`~torch.complex128` | ``1e-7``   | ``1e-7`` |
    +---------------------------+------------+----------+
    | :attr:`~torch.quint8`     | ``1.3e-6`` | ``1e-5`` |
    +---------------------------+------------+----------+
    | :attr:`~torch.quint2x4`   | ``1.3e-6`` | ``1e-5`` |
    +---------------------------+------------+----------+
    | :attr:`~torch.quint4x2`   | ``1.3e-6`` | ``1e-5`` |
    +---------------------------+------------+----------+
    | :attr:`~torch.qint8`      | ``1.3e-6`` | ``1e-5`` |
    +---------------------------+------------+----------+
    | :attr:`~torch.qint32`     | ``1.3e-6`` | ``1e-5`` |
    +---------------------------+------------+----------+
    | other                     | ``0.0``    | ``0.0``  |
    +---------------------------+------------+----------+

    .. note::

        :func:`~torch.testing.assert_close` is highly configurable with strict default settings. Users are encouraged
        to :func:`~functools.partial` it to fit their use case. For example, if an equality check is needed, one might
        define an ``assert_equal`` that uses zero tolerances for every ``dtype`` by default:

        >>> import functools
        >>> assert_equal = functools.partial(torch.testing.assert_close, rtol=0, atol=0)
        >>> assert_equal(1e-9, 1e-10)
        Traceback (most recent call last):
        ...
        AssertionError: Scalars are not equal!
        <BLANKLINE>
        Absolute difference: 9.000000000000001e-10
        Relative difference: 9.0

    Examples:
        >>> # tensor to tensor comparison
        >>> expected = torch.tensor([1e0, 1e-1, 1e-2])
        >>> actual = torch.acos(torch.cos(expected))
        >>> torch.testing.assert_close(actual, expected)

        >>> # scalar to scalar comparison
        >>> import math
        >>> expected = math.sqrt(2.0)
        >>> actual = 2.0 / math.sqrt(2.0)
        >>> torch.testing.assert_close(actual, expected)

        >>> # numpy array to numpy array comparison
        >>> import numpy as np
        >>> expected = np.array([1e0, 1e-1, 1e-2])
        >>> actual = np.arccos(np.cos(expected))
        >>> torch.testing.assert_close(actual, expected)

        >>> # sequence to sequence comparison
        >>> import numpy as np
        >>> # The types of the sequences do not have to match. They only have to have the same
        >>> # length and their elements have to match.
        >>> expected = [torch.tensor([1.0]), 2.0, np.array(3.0)]
        >>> actual = tuple(expected)
        >>> torch.testing.assert_close(actual, expected)

        >>> # mapping to mapping comparison
        >>> from collections import OrderedDict
        >>> import numpy as np
        >>> foo = torch.tensor(1.0)
        >>> bar = 2.0
        >>> baz = np.array(3.0)
        >>> # The types and a possible ordering of mappings do not have to match. They only
        >>> # have to have the same set of keys and their elements have to match.
        >>> expected = OrderedDict([("foo", foo), ("bar", bar), ("baz", baz)])
        >>> actual = {"baz": baz, "bar": bar, "foo": foo}
        >>> torch.testing.assert_close(actual, expected)

        >>> expected = torch.tensor([1.0, 2.0, 3.0])
        >>> actual = expected.clone()
        >>> # By default, directly related instances can be compared
        >>> torch.testing.assert_close(torch.nn.Parameter(actual), expected)
        >>> # This check can be made more strict with allow_subclasses=False
        >>> torch.testing.assert_close(
        ...     torch.nn.Parameter(actual), expected, allow_subclasses=False
        ... )
        Traceback (most recent call last):
        ...
        TypeError: No comparison pair was able to handle inputs of type
        <class \'torch.nn.parameter.Parameter\'> and <class \'torch.Tensor\'>.
        >>> # If the inputs are not directly related, they are never considered close
        >>> torch.testing.assert_close(actual.numpy(), expected)
        Traceback (most recent call last):
        ...
        TypeError: No comparison pair was able to handle inputs of type <class \'numpy.ndarray\'>
        and <class \'torch.Tensor\'>.
        >>> # Exceptions to these rules are Python scalars. They can be checked regardless of
        >>> # their type if check_dtype=False.
        >>> torch.testing.assert_close(1.0, 1, check_dtype=False)

        >>> # NaN != NaN by default.
        >>> expected = torch.tensor(float("Nan"))
        >>> actual = expected.clone()
        >>> torch.testing.assert_close(actual, expected)
        Traceback (most recent call last):
        ...
        AssertionError: Scalars are not close!
        <BLANKLINE>
        Absolute difference: nan (up to 1e-05 allowed)
        Relative difference: nan (up to 1.3e-06 allowed)
        >>> torch.testing.assert_close(actual, expected, equal_nan=True)

        >>> expected = torch.tensor([1.0, 2.0, 3.0])
        >>> actual = torch.tensor([1.0, 4.0, 5.0])
        >>> # The default error message can be overwritten.
        >>> torch.testing.assert_close(actual, expected, msg="Argh, the tensors are not close!")
        Traceback (most recent call last):
        ...
        AssertionError: Argh, the tensors are not close!
        >>> # If msg is a callable, it can be used to augment the generated message with
        >>> # extra information
        >>> torch.testing.assert_close(
        ...     actual, expected, msg=lambda msg: f"Header\\n\\n{msg}\\n\\nFooter"
        ... )
        Traceback (most recent call last):
        ...
        AssertionError: Header
        <BLANKLINE>
        Tensor-likes are not close!
        <BLANKLINE>
        Mismatched elements: 2 / 3 (66.7%)
        Greatest absolute difference: 2.0 at index (1,) (up to 1e-05 allowed)
        Greatest relative difference: 1.0 at index (1,) (up to 1.3e-06 allowed)
        <BLANKLINE>
        Footer
    '''
def assert_allclose(actual: Any, expected: Any, rtol: float | None = None, atol: float | None = None, equal_nan: bool = True, msg: str = '') -> None:
    """
    .. warning::

       :func:`torch.testing.assert_allclose` is deprecated since ``1.12`` and will be removed in a future release.
       Please use :func:`torch.testing.assert_close` instead. You can find detailed upgrade instructions
       `here <https://github.com/pytorch/pytorch/issues/61844>`_.
    """
