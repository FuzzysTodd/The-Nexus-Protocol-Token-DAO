from tensorflow.python.util.tf_export import tf_export as tf_export

def load_resource(path):
    """Load the resource at given path, where path is relative to tensorflow/.

  Args:
    path: a string resource path relative to tensorflow/.

  Returns:
    The contents of that resource.

  Raises:
    IOError: If the path is not found, or the resource can't be opened.
  """
def get_data_files_path():
    """Get a direct path to the data files colocated with the script.

  Returns:
    The directory where files specified in data attribute of py_test
    and py_binary are stored.
  """
def get_root_dir_with_all_resources():
    """Get a root directory containing all the data attributes in the build rule.

  Returns:
    The path to the specified file present in the data attribute of py_test
    or py_binary. Falls back to returning the same as get_data_files_path if it
    fails to detect a bazel runfiles directory.
  """
def get_path_to_datafile(path):
    """Get the path to the specified file in the data dependencies.

  The path is relative to tensorflow/

  Args:
    path: a string resource path relative to tensorflow/

  Returns:
    The path to the specified file present in the data attribute of py_test
    or py_binary.

  Raises:
    IOError: If the path is not found, or the resource can't be opened.
  """
def readahead_file_path(path, readahead: str = '128M'):
    """Readahead files not implemented; simply returns given path."""
