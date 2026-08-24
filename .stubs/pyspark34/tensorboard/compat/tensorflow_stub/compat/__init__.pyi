from tensorboard.compat.tensorflow_stub.compat.v1 import *
from _typeshed import Incomplete

def as_bytes(bytes_or_text, encoding: str = 'utf-8'):
    """Converts either bytes or unicode to `bytes`, using utf-8 encoding for
    text.

    Args:
    bytes_or_text: A `bytes`, `str`, or `unicode` object.
    encoding: A string indicating the charset for encoding unicode.

    Returns:
    A `bytes` object.

    Raises:
    TypeError: If `bytes_or_text` is not a binary or unicode string.
    """
def as_text(bytes_or_text, encoding: str = 'utf-8'):
    """Returns the given argument as a unicode string.

    Args:
    bytes_or_text: A `bytes`, `str`, or `unicode` object.
    encoding: A string indicating the charset for decoding unicode.

    Returns:
    A `unicode` (Python 2) or `str` (Python 3) object.

    Raises:
    TypeError: If `bytes_or_text` is not a binary or unicode string.
    """
as_str = as_text

def as_str_any(value):
    """Converts to `str` as `str(value)`, but use `as_str` for `bytes`.

    Args:
    value: A object that can be converted to `str`.

    Returns:
    A `str` object.
    """
def path_to_str(path):
    """Returns the file system path representation of a `PathLike` object, else
    as it is.

    Args:
    path: An object that can be converted to path representation.

    Returns:
    A `str` object.
    """

integral_types: Incomplete
real_types: Incomplete
complex_types: Incomplete
bytes_or_text_types: Incomplete
