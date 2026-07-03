from _typeshed import Incomplete

Pickler: Incomplete

class _ConsistentSet:
    """ Class used to ensure the hash of Sets is preserved
        whatever the order of its items.
    """
    def __init__(self, set_sequence) -> None: ...

class _MyHash:
    """ Class used to hash objects that won't normally pickle """
    args: Incomplete
    def __init__(self, *args) -> None: ...

class Hasher(Pickler):
    """ A subclass of pickler, to do cryptographic hashing, rather than
        pickling.
    """
    stream: Incomplete
    def __init__(self, hash_name: str = 'md5') -> None: ...
    def hash(self, obj, return_digest: bool = True): ...
    def save(self, obj) -> None: ...
    def memoize(self, obj) -> None: ...
    def save_global(self, obj, name: Incomplete | None = None, pack=...) -> None: ...
    dispatch: Incomplete
    def save_set(self, set_items) -> None: ...

class NumpyHasher(Hasher):
    """ Special case the hasher for when numpy is loaded.
    """
    coerce_mmap: Incomplete
    np: Incomplete
    def __init__(self, hash_name: str = 'md5', coerce_mmap: bool = False) -> None:
        """
            Parameters
            ----------
            hash_name: string
                The hash algorithm to be used
            coerce_mmap: boolean
                Make no difference between np.memmap and np.ndarray
                objects.
        """
    def save(self, obj) -> None:
        """ Subclass the save method, to hash ndarray subclass, rather
            than pickling them. Off course, this is a total abuse of
            the Pickler class.
        """

def hash(obj, hash_name: str = 'md5', coerce_mmap: bool = False):
    """ Quick calculation of a hash to identify uniquely Python objects
        containing numpy arrays.

        Parameters
        ----------
        hash_name: 'md5' or 'sha1'
            Hashing algorithm used. sha1 is supposedly safer, but md5 is
            faster.
        coerce_mmap: boolean
            Make no difference between np.memmap and np.ndarray
    """
