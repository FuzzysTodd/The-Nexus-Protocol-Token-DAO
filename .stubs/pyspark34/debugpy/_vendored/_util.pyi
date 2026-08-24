from _typeshed import Incomplete
from collections.abc import Generator

def cwd(dirname) -> Generator[Incomplete, None, None]:
    """A context manager for operating in a different directory."""
def iter_all_files(root, prune_dir: Incomplete | None = None, exclude_file: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """Yield (dirname, basename, filename) for each file in the tree.

    This is an alternative to os.walk() that flattens out the tree and
    with filtering.
    """
def iter_tree(root, prune_dir: Incomplete | None = None, exclude_file: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """Yield (dirname, files) for each directory in the tree.

    The list of files is actually a list of (basename, filename).

    This is an alternative to os.walk() with filtering."""
