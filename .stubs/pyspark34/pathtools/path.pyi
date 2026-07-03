from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['get_dir_walker', 'walk', 'listdir', 'list_directories', 'list_files', 'absolute_path', 'real_absolute_path', 'parent_dir_path']

def get_dir_walker(recursive, topdown: bool = True, followlinks: bool = False):
    """
    Returns a recursive or a non-recursive directory walker.

    :param recursive:
        ``True`` produces a recursive walker; ``False`` produces a non-recursive
        walker.
    :returns:
        A walker function.
    """
def walk(dir_pathname, recursive: bool = True, topdown: bool = True, followlinks: bool = False) -> Generator[Incomplete, None, None]:
    """
    Walks a directory tree optionally recursively. Works exactly like
    :func:`os.walk` only adding the `recursive` argument.

    :param dir_pathname:
        The directory to traverse.
    :param recursive:
        ``True`` for walking recursively through the directory tree;
        ``False`` otherwise.
    :param topdown:
        Please see the documentation for :func:`os.walk`
    :param followlinks:
        Please see the documentation for :func:`os.walk`
    """
def listdir(dir_pathname, recursive: bool = True, topdown: bool = True, followlinks: bool = False) -> Generator[Incomplete, None, None]:
    """
    Enlists all items using their absolute paths in a directory, optionally
    recursively.

    :param dir_pathname:
        The directory to traverse.
    :param recursive:
        ``True`` for walking recursively through the directory tree;
        ``False`` otherwise.
    :param topdown:
        Please see the documentation for :func:`os.walk`
    :param followlinks:
        Please see the documentation for :func:`os.walk`
    """
def list_directories(dir_pathname, recursive: bool = True, topdown: bool = True, followlinks: bool = False) -> Generator[Incomplete, None, None]:
    """
    Enlists all the directories using their absolute paths within the specified
    directory, optionally recursively.

    :param dir_pathname:
        The directory to traverse.
    :param recursive:
        ``True`` for walking recursively through the directory tree;
        ``False`` otherwise.
    :param topdown:
        Please see the documentation for :func:`os.walk`
    :param followlinks:
        Please see the documentation for :func:`os.walk`
    """
def list_files(dir_pathname, recursive: bool = True, topdown: bool = True, followlinks: bool = False) -> Generator[Incomplete, None, None]:
    """
    Enlists all the files using their absolute paths within the specified
    directory, optionally recursively.

    :param dir_pathname:
        The directory to traverse.
    :param recursive:
        ``True`` for walking recursively through the directory tree;
        ``False`` otherwise.
    :param topdown:
        Please see the documentation for :func:`os.walk`
    :param followlinks:
        Please see the documentation for :func:`os.walk`
    """
def absolute_path(path):
    """
    Returns the absolute path for the given path and normalizes the path.

    :param path:
        Path for which the absolute normalized path will be found.
    :returns:
        Absolute normalized path.
    """
def real_absolute_path(path):
    """
    Returns the real absolute normalized path for the given path.

    :param path:
        Path for which the real absolute normalized path will be found.
    :returns:
        Real absolute normalized path.
    """
def parent_dir_path(path):
    """
    Returns the parent directory path.

    :param path:
        Path for which the parent directory will be obtained.
    :returns:
        Parent directory path.
    """
