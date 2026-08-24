def path_to_string(path):
    """Convert `PathLike` objects to their string representation.

  If given a non-string typed path object, converts it to its string
  representation.

  If the object passed to `path` is not among the above, then it is
  returned unchanged. This allows e.g. passthrough of file objects
  through this function.

  Args:
    path: `PathLike` object that represents a path

  Returns:
    A string representation of the path argument, if Python support exists.
  """
def ask_to_proceed_with_overwrite(filepath):
    """Produces a prompt asking about overwriting a file.

  Args:
      filepath: the path to the file to be overwritten.

  Returns:
      True if we can proceed with overwrite, False otherwise.
  """
