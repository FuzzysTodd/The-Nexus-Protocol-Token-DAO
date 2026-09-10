import asyncio
import datetime
import typing
import unittest
from _typeshed import Incomplete
from types import TracebackType
from typing import Any, Callable, Dict, Mapping, Sequence, Tuple, Type

bytes_type = bytes
unicode_type = str
basestring_type = str
TimeoutError = asyncio.TimeoutError

class ObjectDict(Dict[str, Any]):
    """Makes a dictionary behave like an object, with attribute-style access."""
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...

class GzipDecompressor:
    """Streaming gzip decompressor.

    The interface is like that of `zlib.decompressobj` (without some of the
    optional arguments, but it understands gzip headers and checksums.
    """
    decompressobj: Incomplete
    def __init__(self) -> None: ...
    def decompress(self, value: bytes, max_length: int = 0) -> bytes:
        """Decompress a chunk, returning newly-available data.

        Some data may be buffered for later processing; `flush` must
        be called when there is no more input data to ensure that
        all data was processed.

        If ``max_length`` is given, some input data may be left over
        in ``unconsumed_tail``; you must retrieve this value and pass
        it back to a future call to `decompress` if it is not empty.
        """
    @property
    def unconsumed_tail(self) -> bytes:
        """Returns the unconsumed portion left over"""
    def flush(self) -> bytes:
        """Return any remaining buffered data not yet returned by decompress.

        Also checks for errors such as truncated input.
        No other methods may be called on this object after `flush`.
        """

def import_object(name: str) -> Any:
    """Imports an object by name.

    ``import_object('x')`` is equivalent to ``import x``.
    ``import_object('x.y.z')`` is equivalent to ``from x.y import z``.

    >>> import tornado.escape
    >>> import_object('tornado.escape') is tornado.escape
    True
    >>> import_object('tornado.escape.utf8') is tornado.escape.utf8
    True
    >>> import_object('tornado') is tornado
    True
    >>> import_object('tornado.missing_module')
    Traceback (most recent call last):
        ...
    ImportError: No module named missing_module
    """
def exec_in(code: Any, glob: Dict[str, Any], loc: Mapping[str, Any] | None | None = None) -> None: ...
def raise_exc_info(exc_info: Tuple[type | None, BaseException | None, TracebackType | None]) -> typing.NoReturn: ...
def errno_from_exception(e: BaseException) -> int | None:
    """Provides the errno from an Exception object.

    There are cases that the errno attribute was not set so we pull
    the errno out of the args but if someone instantiates an Exception
    without any args you will get a tuple error. So this function
    abstracts all that behavior to give you a safe way to get the
    errno.
    """
def re_unescape(s: str) -> str:
    """Unescape a string escaped by `re.escape`.

    May raise ``ValueError`` for regular expressions which could not
    have been produced by `re.escape` (for example, strings containing
    ``\\d`` cannot be unescaped).

    .. versionadded:: 4.4
    """

class Configurable:
    """Base class for configurable interfaces.

    A configurable interface is an (abstract) class whose constructor
    acts as a factory function for one of its implementation subclasses.
    The implementation subclass as well as optional keyword arguments to
    its initializer can be set globally at runtime with `configure`.

    By using the constructor as the factory method, the interface
    looks like a normal class, `isinstance` works as usual, etc.  This
    pattern is most useful when the choice of implementation is likely
    to be a global decision (e.g. when `~select.epoll` is available,
    always use it instead of `~select.select`), or when a
    previously-monolithic class has been split into specialized
    subclasses.

    Configurable subclasses must define the class methods
    `configurable_base` and `configurable_default`, and use the instance
    method `initialize` instead of ``__init__``.

    .. versionchanged:: 5.0

       It is now possible for configuration to be specified at
       multiple levels of a class hierarchy.

    """
    def __new__(cls, *args: Any, **kwargs: Any) -> Any: ...
    @classmethod
    def configurable_base(cls) -> Type[Configurable]:
        """Returns the base class of a configurable hierarchy.

        This will normally return the class in which it is defined.
        (which is *not* necessarily the same as the ``cls`` classmethod
        parameter).

        """
    @classmethod
    def configurable_default(cls) -> Type[Configurable]:
        """Returns the implementation class to be used if none is configured."""
    initialize: Callable[..., None]
    @classmethod
    def configure(cls, impl: None | str | Type[Configurable], **kwargs: Any) -> None:
        """Sets the class to use when the base class is instantiated.

        Keyword arguments will be saved and added to the arguments passed
        to the constructor.  This can be used to set global defaults for
        some parameters.
        """
    @classmethod
    def configured_class(cls) -> Type[Configurable]:
        """Returns the currently configured class."""

class ArgReplacer:
    """Replaces one value in an ``args, kwargs`` pair.

    Inspects the function signature to find an argument by name
    whether it is passed by position or keyword.  For use in decorators
    and similar wrappers.
    """
    name: Incomplete
    arg_pos: Incomplete
    def __init__(self, func: Callable, name: str) -> None: ...
    def get_old_value(self, args: Sequence[Any], kwargs: Dict[str, Any], default: Any = None) -> Any:
        """Returns the old value of the named argument without replacing it.

        Returns ``default`` if the argument is not present.
        """
    def replace(self, new_value: Any, args: Sequence[Any], kwargs: Dict[str, Any]) -> Tuple[Any, Sequence[Any], Dict[str, Any]]:
        """Replace the named argument in ``args, kwargs`` with ``new_value``.

        Returns ``(old_value, args, kwargs)``.  The returned ``args`` and
        ``kwargs`` objects may not be the same as the input objects, or
        the input objects may be mutated.

        If the named argument was not found, ``new_value`` will be added
        to ``kwargs`` and None will be returned as ``old_value``.
        """

def timedelta_to_seconds(td: datetime.timedelta) -> float:
    """Equivalent to ``td.total_seconds()`` (introduced in Python 2.7)."""
def doctests() -> unittest.TestSuite: ...
