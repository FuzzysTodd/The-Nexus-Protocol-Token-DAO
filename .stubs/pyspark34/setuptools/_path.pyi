def ensure_directory(path) -> None:
    """Ensure that the parent directory of `path` exists"""
def same_path(p1: _Path, p2: _Path) -> bool:
    '''Differs from os.path.samefile because it does not require paths to exist.
    Purely string based (no comparison between i-nodes).
    >>> same_path("a/b", "./a/b")
    True
    >>> same_path("a/b", "a/./b")
    True
    >>> same_path("a/b", "././a/b")
    True
    >>> same_path("a/b", "./a/b/c/..")
    True
    >>> same_path("a/b", "../a/b/c")
    False
    >>> same_path("a", "a/b")
    False
    '''
def normpath(filename: _Path) -> str:
    """Normalize a file/dir name for comparison purposes."""
