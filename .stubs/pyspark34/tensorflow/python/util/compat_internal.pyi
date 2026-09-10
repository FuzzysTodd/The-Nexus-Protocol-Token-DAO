from tensorflow.python.util.compat import as_str_any as as_str_any

def path_to_str(path):
    """Returns the file system path representation of a `PathLike` object,
  else as it is.

  Args:
    path: An object that can be converted to path representation.

  Returns:
    A `str` object.
  """
