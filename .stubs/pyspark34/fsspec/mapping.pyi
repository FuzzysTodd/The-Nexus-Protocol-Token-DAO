from .core import url_to_fs as url_to_fs
from _typeshed import Incomplete
from collections.abc import MutableMapping
from functools import cached_property as cached_property

class FSMap(MutableMapping):
    """Wrap a FileSystem instance as a mutable wrapping.

    The keys of the mapping become files under the given root, and the
    values (which must be bytes) the contents of those files.

    Parameters
    ----------
    root: string
        prefix for all the files
    fs: FileSystem instance
    check: bool (=True)
        performs a touch at the location, to check for write access.

    Examples
    --------
    >>> fs = FileSystem(**parameters)  # doctest: +SKIP
    >>> d = FSMap('my-data/path/', fs)  # doctest: +SKIP
    or, more likely
    >>> d = fs.get_mapper('my-data/path/')

    >>> d['loc1'] = b'Hello World'  # doctest: +SKIP
    >>> list(d.keys())  # doctest: +SKIP
    ['loc1']
    >>> d['loc1']  # doctest: +SKIP
    b'Hello World'
    """
    fs: Incomplete
    root: Incomplete
    missing_exceptions: Incomplete
    check: Incomplete
    create: Incomplete
    def __init__(self, root, fs, check: bool = False, create: bool = False, missing_exceptions: Incomplete | None = None) -> None: ...
    @cached_property
    def dirfs(self):
        """dirfs instance that can be used with the same keys as the mapper"""
    def clear(self) -> None:
        """Remove all keys below root - empties out mapping"""
    def getitems(self, keys, on_error: str = 'raise'):
        '''Fetch multiple items from the store

        If the backend is async-able, this might proceed concurrently

        Parameters
        ----------
        keys: list(str)
            They keys to be fetched
        on_error : "raise", "omit", "return"
            If raise, an underlying exception will be raised (converted to KeyError
            if the type is in self.missing_exceptions); if omit, keys with exception
            will simply not be included in the output; if "return", all keys are
            included in the output, but the value will be bytes or an exception
            instance.

        Returns
        -------
        dict(key, bytes|exception)
        '''
    def setitems(self, values_dict) -> None:
        """Set the values of multiple items in the store

        Parameters
        ----------
        values_dict: dict(str, bytes)
        """
    def delitems(self, keys) -> None:
        """Remove multiple keys from the store"""
    def __getitem__(self, key, default: Incomplete | None = None):
        """Retrieve data"""
    def pop(self, key, default: Incomplete | None = None):
        """Pop data"""
    def __setitem__(self, key, value) -> None:
        """Store value in key"""
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __delitem__(self, key) -> None:
        """Remove key"""
    def __contains__(self, key) -> bool:
        """Does key exist in mapping?"""
    def __reduce__(self): ...

def maybe_convert(value): ...
def get_mapper(url: str = '', check: bool = False, create: bool = False, missing_exceptions: Incomplete | None = None, alternate_root: Incomplete | None = None, **kwargs):
    '''Create key-value interface for given URL and options

    The URL will be of the form "protocol://location" and point to the root
    of the mapper required. All keys will be file-names below this location,
    and their values the contents of each key.

    Also accepts compound URLs like zip::s3://bucket/file.zip , see ``fsspec.open``.

    Parameters
    ----------
    url: str
        Root URL of mapping
    check: bool
        Whether to attempt to read from the location before instantiation, to
        check that the mapping does exist
    create: bool
        Whether to make the directory corresponding to the root before
        instantiating
    missing_exceptions: None or tuple
        If given, these exception types will be regarded as missing keys and
        return KeyError when trying to read data. By default, you get
        (FileNotFoundError, IsADirectoryError, NotADirectoryError)
    alternate_root: None or str
        In cases of complex URLs, the parser may fail to pick the correct part
        for the mapper root, so this arg can override

    Returns
    -------
    ``FSMap`` instance, the dict-like key-value store.
    '''
