from .memory import MemoryFile as MemoryFile
from _typeshed import Incomplete
from fsspec.spec import AbstractFileSystem as AbstractFileSystem

class GitFileSystem(AbstractFileSystem):
    """Browse the files of a local git repo at any hash/tag/branch

    (experimental backend)
    """
    root_marker: str
    cachable: bool
    repo: Incomplete
    ref: Incomplete
    def __init__(self, path: Incomplete | None = None, fo: Incomplete | None = None, ref: Incomplete | None = None, **kwargs) -> None:
        '''

        Parameters
        ----------
        path: str (optional)
            Local location of the repo (uses current directory if not given).
            May be deprecated in favour of ``fo``. When used with a higher
            level function such as fsspec.open(), may be of the form
            "git://[path-to-repo[:]][ref@]path/to/file" (but the actual
            file path should not contain "@" or ":").
        fo: str (optional)
            Same as ``path``, but passed as part of a chained URL. This one
            takes precedence if both are given.
        ref: str (optional)
            Reference to work with, could be a hash, tag or branch name. Defaults
            to current working tree. Note that ``ls`` and ``open`` also take hash,
            so this becomes the default for those operations
        kwargs
        '''
    def ls(self, path, detail: bool = True, ref: Incomplete | None = None, **kwargs): ...
    def ukey(self, path, ref: Incomplete | None = None): ...
