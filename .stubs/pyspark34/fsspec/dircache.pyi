from _typeshed import Incomplete
from collections.abc import MutableMapping

class DirCache(MutableMapping):
    '''
    Caching of directory listings, in a structure like::

        {"path0": [
            {"name": "path0/file0",
             "size": 123,
             "type": "file",
             ...
            },
            {"name": "path0/file1",
            },
            ...
            ],
         "path1": [...]
        }

    Parameters to this class control listing expiry or indeed turn
    caching off
    '''
    use_listings_cache: Incomplete
    listings_expiry_time: Incomplete
    max_paths: Incomplete
    def __init__(self, use_listings_cache: bool = True, listings_expiry_time: Incomplete | None = None, max_paths: Incomplete | None = None, **kwargs) -> None:
        """

        Parameters
        ----------
        use_listings_cache: bool
            If False, this cache never returns items, but always reports KeyError,
            and setting items has no effect
        listings_expiry_time: int or float (optional)
            Time in seconds that a listing is considered valid. If None,
            listings do not expire.
        max_paths: int (optional)
            The number of most recent listings that are considered valid; 'recent'
            refers to when the entry was set.
        """
    def __getitem__(self, item): ...
    def clear(self) -> None: ...
    def __len__(self) -> int: ...
    def __contains__(self, item) -> bool: ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __iter__(self): ...
    def __reduce__(self): ...
