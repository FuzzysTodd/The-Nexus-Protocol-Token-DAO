from tensorflow.python.framework import ops as ops
from tensorflow.python.summary.writer.writer import FileWriter as FileWriter
from tensorflow.python.util.tf_export import tf_export as tf_export

class FileWriterCache:
    """Cache for file writers.

  This class caches file writers, one per directory.
  """
    @staticmethod
    def clear() -> None:
        """Clear cached summary writers. Currently only used for unit tests."""
    @staticmethod
    def get(logdir):
        """Returns the FileWriter for the specified directory.

    Args:
      logdir: str, name of the directory.

    Returns:
      A `FileWriter`.
    """
