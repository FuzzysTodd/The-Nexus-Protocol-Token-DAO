import os
from _typeshed import Incomplete
from typing import Any, Callable, NoReturn, Type

StrOrBytesPath = str | bytes | os.PathLike
binding: Incomplete
ffi: Incomplete
lib: Incomplete
no_zero_allocator: Incomplete

def text(charp: Any) -> str:
    """
    Get a native string type representing of the given CFFI ``char*`` object.

    :param charp: A C-style string represented using CFFI.

    :return: :class:`str`
    """
def exception_from_error_queue(exception_type: Type[Exception]) -> NoReturn:
    """
    Convert an OpenSSL library failure into a Python exception.

    When a call to the native OpenSSL library fails, this is usually signalled
    by the return value, and an error code is stored in an error queue
    associated with the current thread. The err library provides functions to
    obtain these error codes and textual error messages.
    """
def make_assert(error: Type[Exception]) -> Callable[[bool], Any]:
    """
    Create an assert function that uses :func:`exception_from_error_queue` to
    raise an exception wrapped by *error*.
    """
def path_bytes(s: StrOrBytesPath) -> bytes:
    """
    Convert a Python path to a :py:class:`bytes` for the path which can be
    passed into an OpenSSL API accepting a filename.

    :param s: A path (valid for os.fspath).

    :return: An instance of :py:class:`bytes`.
    """
def byte_string(s: str) -> bytes: ...

UNSPECIFIED: Incomplete

def text_to_bytes_and_warn(label: str, obj: Any) -> Any:
    """
    If ``obj`` is text, emit a warning that it should be bytes instead and try
    to convert it to bytes automatically.

    :param str label: The name of the parameter from which ``obj`` was taken
        (so a developer can easily find the source of the problem and correct
        it).

    :return: If ``obj`` is the text string type, a ``bytes`` object giving the
        UTF-8 encoding of that text is returned.  Otherwise, ``obj`` itself is
        returned.
    """
