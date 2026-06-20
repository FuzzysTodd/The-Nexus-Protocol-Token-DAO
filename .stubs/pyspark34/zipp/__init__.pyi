import zipfile
from _typeshed import Incomplete

__all__ = ['Path']

class InitializedState:
    """
    Mix-in to save the initialization state for pickling.
    """
    def __init__(self, *args, **kwargs) -> None: ...

class CompleteDirs(InitializedState, zipfile.ZipFile):
    """
    A ZipFile subclass that ensures that implied directories
    are always included in the namelist.

    >>> list(CompleteDirs._implied_dirs(['foo/bar.txt', 'foo/bar/baz.txt']))
    ['foo/', 'foo/bar/']
    >>> list(CompleteDirs._implied_dirs(['foo/bar.txt', 'foo/bar/baz.txt', 'foo/bar/']))
    ['foo/']
    """
    def namelist(self): ...
    def resolve_dir(self, name):
        """
        If the name represents a directory, return that name
        as a directory (with the trailing slash).
        """
    def getinfo(self, name):
        """
        Supplement getinfo for implied dirs.
        """
    @classmethod
    def make(cls, source):
        """
        Given a source (filename or zipfile), return an
        appropriate CompleteDirs subclass.
        """
    @classmethod
    def inject(cls, zf: zipfile.ZipFile) -> zipfile.ZipFile:
        """
        Given a writable zip file zf, inject directory entries for
        any directories implied by the presence of children.
        """

class FastLookup(CompleteDirs):
    """
    ZipFile subclass to ensure implicit
    dirs exist and are resolved rapidly.
    """
    def namelist(self): ...

class Path:
    """
    A pathlib-compatible interface for zip files.

    Consider a zip file with this structure::

        .
        ├── a.txt
        └── b
            ├── c.txt
            └── d
                └── e.txt

    >>> data = io.BytesIO()
    >>> zf = zipfile.ZipFile(data, 'w')
    >>> zf.writestr('a.txt', 'content of a')
    >>> zf.writestr('b/c.txt', 'content of c')
    >>> zf.writestr('b/d/e.txt', 'content of e')
    >>> zf.filename = 'mem/abcde.zip'

    Path accepts the zipfile object itself or a filename

    >>> path = Path(zf)

    From there, several path operations are available.

    Directory iteration (including the zip file itself):

    >>> a, b = path.iterdir()
    >>> a
    Path('mem/abcde.zip', 'a.txt')
    >>> b
    Path('mem/abcde.zip', 'b/')

    name property:

    >>> b.name
    'b'

    join with divide operator:

    >>> c = b / 'c.txt'
    >>> c
    Path('mem/abcde.zip', 'b/c.txt')
    >>> c.name
    'c.txt'

    Read text:

    >>> c.read_text(encoding='utf-8')
    'content of c'

    existence:

    >>> c.exists()
    True
    >>> (b / 'missing.txt').exists()
    False

    Coercion to string:

    >>> import os
    >>> str(c).replace(os.sep, posixpath.sep)
    'mem/abcde.zip/b/c.txt'

    At the root, ``name``, ``filename``, and ``parent``
    resolve to the zipfile.

    >>> str(path)
    'mem/abcde.zip/'
    >>> path.name
    'abcde.zip'
    >>> path.filename == pathlib.Path('mem/abcde.zip')
    True
    >>> str(path.parent)
    'mem'

    If the zipfile has no filename, such attribtues are not
    valid and accessing them will raise an Exception.

    >>> zf.filename = None
    >>> path.name
    Traceback (most recent call last):
    ...
    TypeError: ...

    >>> path.filename
    Traceback (most recent call last):
    ...
    TypeError: ...

    >>> path.parent
    Traceback (most recent call last):
    ...
    TypeError: ...

    # workaround python/cpython#106763
    >>> pass
    """
    root: Incomplete
    at: Incomplete
    def __init__(self, root, at: str = '') -> None:
        """
        Construct a Path from a ZipFile or filename.

        Note: When the source is an existing ZipFile object,
        its type (__class__) will be mutated to a
        specialized type. If the caller wishes to retain the
        original type, the caller should either create a
        separate ZipFile object or pass a filename.
        """
    def __eq__(self, other):
        """
        >>> Path(zipfile.ZipFile(io.BytesIO(), 'w')) == 'foo'
        False
        """
    def __hash__(self): ...
    def open(self, mode: str = 'r', *args, pwd: Incomplete | None = None, **kwargs):
        """
        Open this entry as text or binary following the semantics
        of ``pathlib.Path.open()`` by passing arguments through
        to io.TextIOWrapper().
        """
    @property
    def name(self): ...
    @property
    def suffix(self): ...
    @property
    def suffixes(self): ...
    @property
    def stem(self): ...
    @property
    def filename(self): ...
    def read_text(self, *args, **kwargs): ...
    def read_bytes(self): ...
    def is_dir(self): ...
    def is_file(self): ...
    def exists(self): ...
    def iterdir(self): ...
    def match(self, path_pattern): ...
    def is_symlink(self):
        """
        Return whether this path is a symlink. Always false (python/cpython#82102).
        """
    def glob(self, pattern): ...
    def rglob(self, pattern): ...
    def relative_to(self, other, *extra): ...
    def joinpath(self, *other): ...
    __truediv__ = joinpath
    @property
    def parent(self): ...
