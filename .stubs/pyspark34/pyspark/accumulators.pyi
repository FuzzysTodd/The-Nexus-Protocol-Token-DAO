import socketserver as SocketServer
import socketserver.BaseRequestHandler
from _typeshed import Incomplete
from typing import Callable, Generic, Tuple, Type, TypeVar

__all__ = ['Accumulator', 'AccumulatorParam']

T = TypeVar('T')
U = TypeVar('U', bound='SupportsIAdd')

class Accumulator(Generic[T]):
    '''
    A shared variable that can be accumulated, i.e., has a commutative and associative "add"
    operation. Worker tasks on a Spark cluster can add values to an Accumulator with the `+=`
    operator, but only the driver program is allowed to access its value, using `value`.
    Updates from the workers get propagated automatically to the driver program.

    While :class:`SparkContext` supports accumulators for primitive data types like :class:`int` and
    :class:`float`, users can also define accumulators for custom types by providing a custom
    :py:class:`AccumulatorParam` object. Refer to its doctest for an example.

    Examples
    --------
    >>> a = sc.accumulator(1)
    >>> a.value
    1
    >>> a.value = 2
    >>> a.value
    2
    >>> a += 5
    >>> a.value
    7
    >>> sc.accumulator(1.0).value
    1.0
    >>> sc.accumulator(1j).value
    1j
    >>> rdd = sc.parallelize([1,2,3])
    >>> def f(x):
    ...     global a
    ...     a += x
    >>> rdd.foreach(f)
    >>> a.value
    13
    >>> b = sc.accumulator(0)
    >>> def g(x):
    ...     b.add(x)
    >>> rdd.foreach(g)
    >>> b.value
    6

    >>> rdd.map(lambda x: a.value).collect() # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    Py4JJavaError: ...

    >>> def h(x):
    ...     global a
    ...     a.value = 7
    >>> rdd.foreach(h) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    Py4JJavaError: ...

    >>> sc.accumulator([1.0, 2.0, 3.0]) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: ...
    '''
    aid: Incomplete
    accum_param: Incomplete
    def __init__(self, aid: int, value: T, accum_param: AccumulatorParam[T]) -> None:
        """Create a new Accumulator with a given initial value and AccumulatorParam object"""
    def __reduce__(self) -> Tuple[Callable[[int, T, AccumulatorParam[T]], 'Accumulator[T]'], Tuple[int, T, 'AccumulatorParam[T]']]:
        """Custom serialization; saves the zero value from our AccumulatorParam"""
    @property
    def value(self) -> T:
        """Get the accumulator's value; only usable in driver program"""
    @value.setter
    def value(self, value: T) -> None:
        """Sets the accumulator's value; only usable in driver program"""
    def add(self, term: T) -> None:
        """Adds a term to this accumulator's value"""
    def __iadd__(self, term: T) -> Accumulator[T]:
        """The += operator; adds a term to this accumulator's value"""

class AccumulatorParam(Generic[T]):
    """
    Helper object that defines how to accumulate values of a given type.

    Examples
    --------
    >>> from pyspark.accumulators import AccumulatorParam
    >>> class VectorAccumulatorParam(AccumulatorParam):
    ...     def zero(self, value):
    ...         return [0.0] * len(value)
    ...     def addInPlace(self, val1, val2):
    ...         for i in range(len(val1)):
    ...              val1[i] += val2[i]
    ...         return val1
    >>> va = sc.accumulator([1.0, 2.0, 3.0], VectorAccumulatorParam())
    >>> va.value
    [1.0, 2.0, 3.0]
    >>> def g(x):
    ...     global va
    ...     va += [x] * 3
    >>> rdd = sc.parallelize([1,2,3])
    >>> rdd.foreach(g)
    >>> va.value
    [7.0, 8.0, 9.0]
    """
    def zero(self, value: T) -> T:
        '''
        Provide a "zero value" for the type, compatible in dimensions with the
        provided `value` (e.g., a zero vector)
        '''
    def addInPlace(self, value1: T, value2: T) -> T:
        """
        Add two values of the accumulator's data type, returning a new value;
        for efficiency, can also update `value1` in place and return it.
        """

class AddingAccumulatorParam(AccumulatorParam[U]):
    """
    An AccumulatorParam that uses the + operators to add values. Designed for simple types
    such as integers, floats, and lists. Requires the zero value for the underlying type
    as a parameter.
    """
    zero_value: Incomplete
    def __init__(self, zero_value: U) -> None: ...
    def zero(self, value: U) -> U: ...
    def addInPlace(self, value1: U, value2: U) -> U: ...

class _UpdateRequestHandler(SocketServer.StreamRequestHandler):
    """
    This handler will keep polling updates from the same socket until the
    server is shutdown.
    """
    def handle(self) -> None: ...

class AccumulatorServer(SocketServer.TCPServer):
    auth_token: Incomplete
    def __init__(self, server_address: Tuple[str, int], RequestHandlerClass: Type['socketserver.BaseRequestHandler'], auth_token: str) -> None: ...
    server_shutdown: bool
    def shutdown(self) -> None: ...
