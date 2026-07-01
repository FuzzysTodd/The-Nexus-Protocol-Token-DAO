from . import hashing as hashing
from ._store_backends import CacheWarning as CacheWarning, FileSystemStoreBackend as FileSystemStoreBackend, StoreBackendBase as StoreBackendBase
from .func_inspect import filter_args as filter_args, format_call as format_call, format_signature as format_signature, get_func_code as get_func_code, get_func_name as get_func_name
from .logger import Logger as Logger, format_time as format_time, pformat as pformat
from _typeshed import Incomplete

FIRST_LINE_TEXT: str

def extract_first_line(func_code):
    """ Extract the first line information from the function code
        text if available.
    """

class JobLibCollisionWarning(UserWarning):
    """ Warn that there might be a collision between names of functions.
    """

def register_store_backend(backend_name, backend) -> None:
    """Extend available store backends.

    The Memory, MemorizeResult and MemorizeFunc objects are designed to be
    agnostic to the type of store used behind. By default, the local file
    system is used but this function gives the possibility to extend joblib's
    memory pattern with other types of storage such as cloud storage (S3, GCS,
    OpenStack, HadoopFS, etc) or blob DBs.

    Parameters
    ----------
    backend_name: str
        The name identifying the store backend being registered. For example,
        'local' is used with FileSystemStoreBackend.
    backend: StoreBackendBase subclass
        The name of a class that implements the StoreBackendBase interface.

    """

class MemorizedResult(Logger):
    """Object representing a cached value.

    Attributes
    ----------
    location: str
        The location of joblib cache. Depends on the store backend used.

    func: function or str
        function whose output is cached. The string case is intended only for
        instantiation based on the output of repr() on another instance.
        (namely eval(repr(memorized_instance)) works).

    argument_hash: str
        hash of the function arguments.

    backend: str
        Type of store backend for reading/writing cache files.
        Default is 'local'.

    mmap_mode: {None, 'r+', 'r', 'w+', 'c'}
        The memmapping mode used when loading from cache numpy arrays. See
        numpy.load for the meaning of the different values.

    verbose: int
        verbosity level (0 means no message).

    timestamp, metadata: string
        for internal use only.
    """
    func_id: Incomplete
    func: Incomplete
    args_id: Incomplete
    store_backend: Incomplete
    mmap_mode: Incomplete
    metadata: Incomplete
    duration: Incomplete
    verbose: Incomplete
    timestamp: Incomplete
    def __init__(self, location, func, args_id, backend: str = 'local', mmap_mode: Incomplete | None = None, verbose: int = 0, timestamp: Incomplete | None = None, metadata: Incomplete | None = None) -> None: ...
    @property
    def argument_hash(self): ...
    def get(self):
        """Read value from cache and return it."""
    def clear(self) -> None:
        """Clear value from cache"""

class NotMemorizedResult:
    """Class representing an arbitrary value.

    This class is a replacement for MemorizedResult when there is no cache.
    """
    value: Incomplete
    valid: bool
    def __init__(self, value) -> None: ...
    def get(self): ...
    def clear(self) -> None: ...

class NotMemorizedFunc:
    """No-op object decorating a function.

    This class replaces MemorizedFunc when there is no cache. It provides an
    identical API but does not write anything on disk.

    Attributes
    ----------
    func: callable
        Original undecorated function.
    """
    func: Incomplete
    def __init__(self, func) -> None: ...
    def __call__(self, *args, **kwargs): ...
    def call_and_shelve(self, *args, **kwargs): ...
    def clear(self, warn: bool = True) -> None: ...
    def call(self, *args, **kwargs): ...
    def check_call_in_cache(self, *args, **kwargs): ...

class MemorizedFunc(Logger):
    """Callable object decorating a function for caching its return value
    each time it is called.

    Methods are provided to inspect the cache or clean it.

    Attributes
    ----------
    func: callable
        The original, undecorated, function.

    location: string
        The location of joblib cache. Depends on the store backend used.

    backend: str
        Type of store backend for reading/writing cache files.
        Default is 'local', in which case the location is the path to a
        disk storage.

    ignore: list or None
        List of variable names to ignore when choosing whether to
        recompute.

    mmap_mode: {None, 'r+', 'r', 'w+', 'c'}
        The memmapping mode used when loading from cache
        numpy arrays. See numpy.load for the meaning of the different
        values.

    compress: boolean, or integer
        Whether to zip the stored data on disk. If an integer is
        given, it should be between 1 and 9, and sets the amount
        of compression. Note that compressed arrays cannot be
        read by memmapping.

    verbose: int, optional
        The verbosity flag, controls messages that are issued as
        the function is evaluated.

    cache_validation_callback: callable, optional
        Callable to check if a result in cache is valid or is to be recomputed.
        When the function is called with arguments for which a cache exists,
        the callback is called with the cache entry's metadata as its sole
        argument. If it returns True, the cached result is returned, else the
        cache for these arguments is cleared and the result is recomputed.
    """
    mmap_mode: Incomplete
    compress: Incomplete
    func: Incomplete
    cache_validation_callback: Incomplete
    ignore: Incomplete
    store_backend: Incomplete
    timestamp: Incomplete
    __doc__: Incomplete
    def __init__(self, func, location, backend: str = 'local', ignore: Incomplete | None = None, mmap_mode: Incomplete | None = None, compress: bool = False, verbose: int = 1, timestamp: Incomplete | None = None, cache_validation_callback: Incomplete | None = None) -> None: ...
    @property
    def func_code_info(self): ...
    def call_and_shelve(self, *args, **kwargs):
        '''Call wrapped function, cache result and return a reference.

        This method returns a reference to the cached result instead of the
        result itself. The reference object is small and pickeable, allowing
        to send or store it easily. Call .get() on reference object to get
        result.

        Returns
        -------
        cached_result: MemorizedResult or NotMemorizedResult
            reference to the value returned by the wrapped function. The
            class "NotMemorizedResult" is used when there is no cache
            activated (e.g. location=None in Memory).
        '''
    def __call__(self, *args, **kwargs): ...
    def check_call_in_cache(self, *args, **kwargs):
        """Check if function call is in the memory cache.

        Does not call the function or do any work besides func inspection
        and arg hashing.

        Returns
        -------
        is_call_in_cache: bool
            Whether or not the result of the function has been cached
            for the input arguments that have been passed.
        """
    def clear(self, warn: bool = True) -> None:
        """Empty the function's cache."""
    def call(self, *args, **kwargs):
        """Force the execution of the function with the given arguments.

        The output values will be persisted, i.e., the cache will be updated
        with any new values.

        Parameters
        ----------
        *args: arguments
            The arguments.
        **kwargs: keyword arguments
            Keyword arguments.

        Returns
        -------
        output : object
            The output of the function call.
        metadata : dict
            The metadata associated with the call.
        """

class Memory(Logger):
    """ A context object for caching a function's return value each time it
        is called with the same input arguments.

        All values are cached on the filesystem, in a deep directory
        structure.

        Read more in the :ref:`User Guide <memory>`.

        Parameters
        ----------
        location: str, pathlib.Path or None
            The path of the base directory to use as a data store
            or None. If None is given, no caching is done and
            the Memory object is completely transparent. This option
            replaces cachedir since version 0.12.

        backend: str, optional
            Type of store backend for reading/writing cache files.
            Default: 'local'.
            The 'local' backend is using regular filesystem operations to
            manipulate data (open, mv, etc) in the backend.

        mmap_mode: {None, 'r+', 'r', 'w+', 'c'}, optional
            The memmapping mode used when loading from cache
            numpy arrays. See numpy.load for the meaning of the
            arguments.

        compress: boolean, or integer, optional
            Whether to zip the stored data on disk. If an integer is
            given, it should be between 1 and 9, and sets the amount
            of compression. Note that compressed arrays cannot be
            read by memmapping.

        verbose: int, optional
            Verbosity flag, controls the debug messages that are issued
            as functions are evaluated.

        bytes_limit: int | str, optional
            Limit in bytes of the size of the cache. By default, the size of
            the cache is unlimited. When reducing the size of the cache,
            ``joblib`` keeps the most recently accessed items first. If a
            str is passed, it is converted to a number of bytes using units
            { K | M | G} for kilo, mega, giga.

            **Note:** You need to call :meth:`joblib.Memory.reduce_size` to
            actually reduce the cache size to be less than ``bytes_limit``.

            **Note:** This argument has been deprecated. One should give the
            value of ``bytes_limit`` directly in
            :meth:`joblib.Memory.reduce_size`.

        backend_options: dict, optional
            Contains a dictionary of named parameters used to configure
            the store backend.
    """
    mmap_mode: Incomplete
    timestamp: Incomplete
    bytes_limit: Incomplete
    backend: Incomplete
    compress: Incomplete
    backend_options: Incomplete
    location: Incomplete
    store_backend: Incomplete
    def __init__(self, location: Incomplete | None = None, backend: str = 'local', mmap_mode: Incomplete | None = None, compress: bool = False, verbose: int = 1, bytes_limit: Incomplete | None = None, backend_options: Incomplete | None = None) -> None: ...
    def cache(self, func: Incomplete | None = None, ignore: Incomplete | None = None, verbose: Incomplete | None = None, mmap_mode: bool = False, cache_validation_callback: Incomplete | None = None):
        """ Decorates the given function func to only compute its return
            value for input arguments not cached on disk.

            Parameters
            ----------
            func: callable, optional
                The function to be decorated
            ignore: list of strings
                A list of arguments name to ignore in the hashing
            verbose: integer, optional
                The verbosity mode of the function. By default that
                of the memory object is used.
            mmap_mode: {None, 'r+', 'r', 'w+', 'c'}, optional
                The memmapping mode used when loading from cache
                numpy arrays. See numpy.load for the meaning of the
                arguments. By default that of the memory object is used.
            cache_validation_callback: callable, optional
                Callable to validate whether or not the cache is valid. When
                the cached function is called with arguments for which a cache
                exists, this callable is called with the metadata of the cached
                result as its sole argument. If it returns True, then the
                cached result is returned, else the cache for these arguments
                is cleared and recomputed.

            Returns
            -------
            decorated_func: MemorizedFunc object
                The returned object is a MemorizedFunc object, that is
                callable (behaves like a function), but offers extra
                methods for cache lookup and management. See the
                documentation for :class:`joblib.memory.MemorizedFunc`.
        """
    def clear(self, warn: bool = True) -> None:
        """ Erase the complete cache directory.
        """
    def reduce_size(self, bytes_limit: Incomplete | None = None, items_limit: Incomplete | None = None, age_limit: Incomplete | None = None) -> None:
        """Remove cache elements to make the cache fit its limits.

        The limitation can impose that the cache size fits in ``bytes_limit``,
        that the number of cache items is no more than ``items_limit``, and
        that all files in cache are not older than ``age_limit``.

        Parameters
        ----------
        bytes_limit: int | str, optional
            Limit in bytes of the size of the cache. By default, the size of
            the cache is unlimited. When reducing the size of the cache,
            ``joblib`` keeps the most recently accessed items first. If a
            str is passed, it is converted to a number of bytes using units
            { K | M | G} for kilo, mega, giga.

        items_limit: int, optional
            Number of items to limit the cache to.  By default, the number of
            items in the cache is unlimited.  When reducing the size of the
            cache, ``joblib`` keeps the most recently accessed items first.

        age_limit: datetime.timedelta, optional
            Maximum age of items to limit the cache to.  When reducing the size
            of the cache, any items last accessed more than the given length of
            time ago are deleted.
        """
    def eval(self, func, *args, **kwargs):
        """ Eval function func with arguments `*args` and `**kwargs`,
            in the context of the memory.

            This method works similarly to the builtin `apply`, except
            that the function is called only if the cache is not
            up to date.

        """

def expires_after(days: int = 0, seconds: int = 0, microseconds: int = 0, milliseconds: int = 0, minutes: int = 0, hours: int = 0, weeks: int = 0):
    """Helper cache_validation_callback to force recompute after a duration.

    Parameters
    ----------
    days, seconds, microseconds, milliseconds, minutes, hours, weeks: numbers
        argument passed to a timedelta.
    """
