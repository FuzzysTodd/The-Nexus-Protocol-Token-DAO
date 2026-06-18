import threading
from pyspark import SparkContext
from typing import Any, Callable, Generic, Iterator, Tuple, TypeVar, overload
from typing.io import BinaryIO

__all__ = ['Broadcast']

T = TypeVar('T')

class Broadcast(Generic[T]):
    """
    A broadcast variable created with :meth:`SparkContext.broadcast`.
    Access its value through :attr:`value`.

    Examples
    --------
    >>> b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])
    >>> b.value
    [1, 2, 3, 4, 5]
    >>> spark.sparkContext.parallelize([0, 0]).flatMap(lambda x: b.value).collect()
    [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    >>> b.unpersist()

    >>> large_broadcast = spark.sparkContext.broadcast(range(10000))
    """
    @overload
    def __init__(self, sc: SparkContext, value: T, pickle_registry: BroadcastPickleRegistry) -> None: ...
    @overload
    def __init__(self, *, path: str) -> None: ...
    @overload
    def __init__(self, *, sock_file: str) -> None: ...
    def dump(self, value: T, f: BinaryIO) -> None:
        '''
        Write a pickled representation of value to the open file or socket.
        The protocol pickle is HIGHEST_PROTOCOL.

        Parameters
        ----------
        value : T
            Value to write.

        f : :class:`BinaryIO`
            File or socket where the pickled value will be stored.

        Examples
        --------
        >>> import os
        >>> import tempfile

        >>> b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])

        Write a pickled representation of `b` to the open temp file.

        >>> with tempfile.TemporaryDirectory() as d:
        ...     path = os.path.join(d, "test.txt")
        ...     with open(path, "wb") as f:
        ...         b.dump(b.value, f)
        '''
    def load_from_path(self, path: str) -> T:
        '''
        Read the pickled representation of an object from the open file and
        return the reconstituted object hierarchy specified therein.

        Parameters
        ----------
        path : str
            File path where reads the pickled value.

        Returns
        -------
        T
            The object hierarchy specified therein reconstituted
            from the pickled representation of an object.

        Examples
        --------
        >>> import os
        >>> import tempfile

        >>> b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])
        >>> c = spark.sparkContext.broadcast(1)

        Read the pickled representation of value fron temp file.

        >>> with tempfile.TemporaryDirectory() as d:
        ...     path = os.path.join(d, "test.txt")
        ...     with open(path, "wb") as f:
        ...         b.dump(b.value, f)
        ...     c.load_from_path(path)
        [1, 2, 3, 4, 5]
        '''
    def load(self, file: BinaryIO) -> T:
        '''
        Read a pickled representation of value from the open file or socket.

        Parameters
        ----------
        file : :class:`BinaryIO`
            File or socket where the pickled value will be read.

        Returns
        -------
        T
            The object hierarchy specified therein reconstituted
            from the pickled representation of an object.

        Examples
        --------
        >>> import os
        >>> import tempfile

        >>> b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])
        >>> c = spark.sparkContext.broadcast(1)

        Read the pickled representation of value from the open temp file.

        >>> with tempfile.TemporaryDirectory() as d:
        ...     path = os.path.join(d, "test.txt")
        ...     with open(path, "wb") as f:
        ...         b.dump(b.value, f)
        ...     with open(path, "rb") as f:
        ...         c.load(f)
        [1, 2, 3, 4, 5]
        '''
    @property
    def value(self) -> T:
        """Return the broadcasted value"""
    def unpersist(self, blocking: bool = False) -> None:
        """
        Delete cached copies of this broadcast on the executors. If the
        broadcast is used after this is called, it will need to be
        re-sent to each executor.

        Parameters
        ----------
        blocking : bool, optional, default False
            Whether to block until unpersisting has completed.

        Examples
        --------
        >>> b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])

        Delete cached copies of this broadcast on the executors

        >>> b.unpersist()
        """
    def destroy(self, blocking: bool = False) -> None:
        """
        Destroy all data and metadata related to this broadcast variable.
        Use this with caution; once a broadcast variable has been destroyed,
        it cannot be used again.

        .. versionchanged:: 3.0.0
           Added optional argument `blocking` to specify whether to block until all
           blocks are deleted.

        Parameters
        ----------
        blocking : bool, optional, default False
            Whether to block until unpersisting has completed.

        Examples
        --------
        >>> b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])

        Destroy all data and metadata related to this broadcast variable

        >>> b.destroy()
        """
    def __reduce__(self) -> Tuple[Callable[[int], 'Broadcast[T]'], Tuple[int]]: ...

class BroadcastPickleRegistry(threading.local):
    """Thread-local registry for broadcast variables that have been pickled"""
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator[Broadcast[Any]]: ...
    def add(self, bcast: Broadcast[Any]) -> None: ...
    def clear(self) -> None: ...
