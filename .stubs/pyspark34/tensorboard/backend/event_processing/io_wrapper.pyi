from _typeshed import Incomplete
from collections.abc import Generator
from tensorboard.compat import tf as tf
from tensorboard.util import io_util as io_util, tb_logging as tb_logging

logger: Incomplete

def PathSeparator(path): ...
def IsTensorFlowEventsFile(path):
    """Check the path name to see if it is probably a TF Events file.

    Args:
      path: A file path to check if it is an event file.

    Raises:
      ValueError: If the path is an empty string.

    Returns:
      If path is formatted like a TensorFlowEventsFile. Dummy files such as
        those created with the '.profile-empty' suffixes and meant to hold
        no `Summary` protos are treated as true TensorFlowEventsFiles. For
        background, see: https://github.com/tensorflow/tensorboard/issues/2084.
    """
def IsSummaryEventsFile(path):
    """Check whether the path is probably a TF Events file containing Summary.

    Args:
      path: A file path to check if it is an event file containing `Summary`
        protos.

    Returns:
      If path is formatted like a TensorFlowEventsFile. Dummy files such as
        those created with the '.profile-empty' suffixes and meant to hold
        no `Summary` protos  are treated as `False`. For background, see:
        https://github.com/tensorflow/tensorboard/issues/2084.
    """
def ListDirectoryAbsolute(directory):
    """Yields all files in the given directory.

    The paths are absolute.
    """
def ListRecursivelyViaGlobbing(top) -> Generator[Incomplete, None, None]:
    """Recursively lists all files within the directory.

    This method does not list subdirectories (in addition to regular files), and
    the file paths are all absolute. If the directory does not exist, this yields
    nothing.

    This method does so by glob-ing deeper and deeper directories, ie
    foo/*, foo/*/*, foo/*/*/* and so on until all files are listed. All file
    paths are absolute, and this method lists subdirectories too.

    For certain file systems, globbing via this method may prove significantly
    faster than recursively walking a directory. Specifically, TF file systems
    that implement TensorFlow's FileSystem.GetMatchingPaths method could save
    costly disk reads by using this method. However, for other file systems, this
    method might prove slower because the file system performs a walk per call to
    glob (in which case it might as well just perform 1 walk).

    Args:
      top: A path to a directory.

    Yields:
      A (dir_path, file_paths) tuple for each directory/subdirectory.
    """
def ListRecursivelyViaWalking(top) -> Generator[Incomplete, None, None]:
    """Walks a directory tree, yielding (dir_path, file_paths) tuples.

    For each of `top` and its subdirectories, yields a tuple containing the path
    to the directory and the path to each of the contained files.  Note that
    unlike os.Walk()/tf.io.gfile.walk()/ListRecursivelyViaGlobbing, this does not
    list subdirectories. The file paths are all absolute. If the directory does
    not exist, this yields nothing.

    Walking may be incredibly slow on certain file systems.

    Args:
      top: A path to a directory.

    Yields:
      A (dir_path, file_paths) tuple for each directory/subdirectory.
    """
def GetLogdirSubdirectories(path):
    """Obtains all subdirectories with events files.

    The order of the subdirectories returned is unspecified. The internal logic
    that determines order varies by scenario.

    Args:
      path: The path to a directory under which to find subdirectories.

    Returns:
      A tuple of absolute paths of all subdirectories each with at least 1 events
      file directly within the subdirectory.

    Raises:
      ValueError: If the path passed to the method exists and is not a directory.
    """
