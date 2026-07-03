from _typeshed import Incomplete
from sympy.testing.pytest import XFAIL as XFAIL
from typing import NamedTuple

def may_xfail(func): ...

class CompilerNotFoundError(FileNotFoundError): ...
class CompileError(Exception):
    """Failure to compile one or more C/C++ source files."""

def get_abspath(path, cwd: str = '.'):
    """ Returns the absolute path.

    Parameters
    ==========

    path : str
        (relative) path.
    cwd : str
        Path to root of relative path.
    """
def make_dirs(path) -> None:
    """ Create directories (equivalent of ``mkdir -p``). """
def copy(src, dst, only_update: bool = False, copystat: bool = True, cwd: Incomplete | None = None, dest_is_dir: bool = False, create_dest_dirs: bool = False):
    """ Variation of ``shutil.copy`` with extra options.

    Parameters
    ==========

    src : str
        Path to source file.
    dst : str
        Path to destination.
    only_update : bool
        Only copy if source is newer than destination
        (returns None if it was newer), default: ``False``.
    copystat : bool
        See ``shutil.copystat``. default: ``True``.
    cwd : str
        Path to working directory (root of relative paths).
    dest_is_dir : bool
        Ensures that dst is treated as a directory. default: ``False``
    create_dest_dirs : bool
        Creates directories if needed.

    Returns
    =======

    Path to the copied file.

    """

class Glob(NamedTuple):
    pathname: Incomplete

class ArbitraryDepthGlob(NamedTuple):
    filename: Incomplete

def glob_at_depth(filename_glob, cwd: Incomplete | None = None): ...
def sha256_of_file(path, nblocks: int = 128):
    """ Computes the SHA256 hash of a file.

    Parameters
    ==========

    path : string
        Path to file to compute hash of.
    nblocks : int
        Number of blocks to read per iteration.

    Returns
    =======

    hashlib sha256 hash object. Use ``.digest()`` or ``.hexdigest()``
    on returned object to get binary or hex encoded string.
    """
def sha256_of_string(string):
    """ Computes the SHA256 hash of a string. """
def pyx_is_cplus(path):
    """
    Inspect a Cython source file (.pyx) and look for comment line like:

    # distutils: language = c++

    Returns True if such a file is present in the file, else False.
    """
def import_module_from_file(filename, only_if_newer_than: Incomplete | None = None):
    """ Imports Python extension (from shared object file)

    Provide a list of paths in `only_if_newer_than` to check
    timestamps of dependencies. import_ raises an ImportError
    if any is newer.

    Word of warning: The OS may cache shared objects which makes
    reimporting same path of an shared object file very problematic.

    It will not detect the new time stamp, nor new checksum, but will
    instead silently use old module. Use unique names for this reason.

    Parameters
    ==========

    filename : str
        Path to shared object.
    only_if_newer_than : iterable of strings
        Paths to dependencies of the shared object.

    Raises
    ======

    ``ImportError`` if any of the files specified in ``only_if_newer_than`` are newer
    than the file given by filename.
    """
def find_binary_of_command(candidates):
    """ Finds binary first matching name among candidates.

    Calls ``which`` from shutils for provided candidates and returns
    first hit.

    Parameters
    ==========

    candidates : iterable of str
        Names of candidate commands

    Raises
    ======

    CompilerNotFoundError if no candidates match.
    """
def unique_list(l):
    """ Uniquify a list (skip duplicate items). """
