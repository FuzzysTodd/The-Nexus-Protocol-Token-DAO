from _typeshed import Incomplete
from tensorflow.python.util.tf_export import tf_export as tf_export

def as_bytes(bytes_or_text, encoding: str = 'utf-8'):
    """Converts `bytearray`, `bytes`, or unicode python input types to `bytes`.

  Uses utf-8 encoding for text by default.

  Args:
    bytes_or_text: A `bytearray`, `bytes`, `str`, or `unicode` object.
    encoding: A string indicating the charset for encoding unicode.

  Returns:
    A `bytes` object.

  Raises:
    TypeError: If `bytes_or_text` is not a binary or unicode string.
  """
def as_text(bytes_or_text, encoding: str = 'utf-8'):
    """Converts any string-like python input types to unicode.

  Returns the input as a unicode string. Uses utf-8 encoding for text
  by default.

  Args:
    bytes_or_text: A `bytes`, `str`, or `unicode` object.
    encoding: A string indicating the charset for decoding unicode.

  Returns:
    A `unicode` (Python 2) or `str` (Python 3) object.

  Raises:
    TypeError: If `bytes_or_text` is not a binary or unicode string.
  """
def as_str(bytes_or_text, encoding: str = 'utf-8'): ...
def as_str_any(value, encoding: str = 'utf-8'):
    """Converts input to `str` type.

     Uses `str(value)`, except for `bytes` typed inputs, which are converted
     using `as_str`.

  Args:
    value: A object that can be converted to `str`.
    encoding: Encoding for `bytes` typed inputs.

  Returns:
    A `str` object.
  """
def path_to_str(path):
    """Converts input which is a `PathLike` object to `str` type.

  Converts from any python constant representation of a `PathLike` object to
  a string. If the input is not a `PathLike` object, simply returns the input.

  Args:
    path: An object that can be converted to path representation.

  Returns:
    A `str` object.

  Usage:
    In case a simplified `str` version of the path is needed from an
    `os.PathLike` object.

  Examples:
  ```python
  $ tf.compat.path_to_str('C:\\XYZ\\tensorflow\\./.././tensorflow')
  'C:\\XYZ\\tensorflow\\./.././tensorflow' # Windows OS
  $ tf.compat.path_to_str(Path('C:\\XYZ\\tensorflow\\./.././tensorflow'))
  'C:\\XYZ\\tensorflow\\..\\tensorflow' # Windows OS
  $ tf.compat.path_to_str(Path('./corpus'))
  'corpus' # Linux OS
  $ tf.compat.path_to_str('./.././Corpus')
  './.././Corpus' # Linux OS
  $ tf.compat.path_to_str(Path('./.././Corpus'))
  '../Corpus' # Linux OS
  $ tf.compat.path_to_str(Path('./..////../'))
  '../..' # Linux OS

  ```
  """
def path_to_bytes(path):
    """Converts input which is a `PathLike` object to `bytes`.

  Converts from any python constant representation of a `PathLike` object
  or `str` to bytes.

  Args:
    path: An object that can be converted to path representation.

  Returns:
    A `bytes` object.

  Usage:
    In case a simplified `bytes` version of the path is needed from an
    `os.PathLike` object.
  """

integral_types: Incomplete
real_types: Incomplete
complex_types: Incomplete
bytes_or_text_types: Incomplete
