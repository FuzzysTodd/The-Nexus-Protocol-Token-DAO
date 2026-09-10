import abc
from abc import ABCMeta, abstractmethod
from numba.core import compiler as compiler, config as config
from numba.core.base import BaseContext as BaseContext
from numba.core.codegen import CodeLibrary as CodeLibrary
from numba.core.compiler import CompileResult as CompileResult
from numba.core.errors import NumbaWarning as NumbaWarning
from numba.core.serialize import dumps as dumps
from numba.misc.appdirs import AppDirs as AppDirs

class _Cache(metaclass=ABCMeta):
    @property
    @abc.abstractmethod
    def cache_path(self):
        """
        The base filesystem path of this cache (for example its root folder).
        """
    @abstractmethod
    def load_overload(self, sig, target_context):
        """
        Load an overload for the given signature using the target context.
        The saved object must be returned if successful, None if not found
        in the cache.
        """
    @abstractmethod
    def save_overload(self, sig, data):
        """
        Save the overload for the given signature.
        """
    @abstractmethod
    def enable(self):
        """
        Enable the cache.
        """
    @abstractmethod
    def disable(self):
        """
        Disable the cache.
        """
    @abstractmethod
    def flush(self):
        """
        Flush the cache.
        """

class NullCache(_Cache):
    @property
    def cache_path(self) -> None: ...
    def load_overload(self, sig, target_context) -> None: ...
    def save_overload(self, sig, cres) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def flush(self) -> None: ...

class _CacheLocator(metaclass=ABCMeta):
    """
    A filesystem locator for caching a given function.
    """
    def ensure_cache_path(self) -> None: ...
    @abstractmethod
    def get_cache_path(self):
        """
        Return the directory the function is cached in.
        """
    @abstractmethod
    def get_source_stamp(self):
        """
        Get a timestamp representing the source code's freshness.
        Can return any picklable Python object.
        """
    @abstractmethod
    def get_disambiguator(self):
        """
        Get a string disambiguator for this locator's function.
        It should allow disambiguating different but similarly-named functions.
        """
    @classmethod
    def from_function(cls, py_func, py_file) -> None:
        """
        Create a locator instance for the given function located in the
        given file.
        """
    @classmethod
    def get_suitable_cache_subpath(cls, py_file):
        """Given the Python file path, compute a suitable path inside the
        cache directory.

        This will reduce a file path that is too long, which can be a problem
        on some operating system (i.e. Windows 7).
        """

class _SourceFileBackedLocatorMixin:
    """
    A cache locator mixin for functions which are backed by a well-known
    Python source file.
    """
    def get_source_stamp(self): ...
    def get_disambiguator(self): ...
    @classmethod
    def from_function(cls, py_func, py_file): ...

class _UserProvidedCacheLocator(_SourceFileBackedLocatorMixin, _CacheLocator):
    """
    A locator that always point to the user provided directory in
    `numba.config.CACHE_DIR`
    """
    def __init__(self, py_func, py_file) -> None: ...
    def get_cache_path(self): ...
    @classmethod
    def from_function(cls, py_func, py_file): ...

class _InTreeCacheLocator(_SourceFileBackedLocatorMixin, _CacheLocator):
    """
    A locator for functions backed by a regular Python module with a
    writable __pycache__ directory.
    """
    def __init__(self, py_func, py_file) -> None: ...
    def get_cache_path(self): ...

class _UserWideCacheLocator(_SourceFileBackedLocatorMixin, _CacheLocator):
    """
    A locator for functions backed by a regular Python module or a
    frozen executable, cached into a user-wide cache directory.
    """
    def __init__(self, py_func, py_file) -> None: ...
    def get_cache_path(self): ...
    @classmethod
    def from_function(cls, py_func, py_file): ...

class _IPythonCacheLocator(_CacheLocator):
    """
    A locator for functions entered at the IPython prompt (notebook or other).
    """
    def __init__(self, py_func, py_file) -> None: ...
    def get_cache_path(self): ...
    def get_source_stamp(self): ...
    def get_disambiguator(self): ...
    @classmethod
    def from_function(cls, py_func, py_file): ...

class CacheImpl(metaclass=ABCMeta):
    """
    Provides the core machinery for caching.
    - implement how to serialize and deserialize the data in the cache.
    - control the filename of the cache.
    - provide the cache locator
    """
    def __init__(self, py_func) -> None: ...
    def get_filename_base(self, fullname, abiflags): ...
    @property
    def filename_base(self): ...
    @property
    def locator(self): ...
    @abstractmethod
    def reduce(self, data):
        """Returns the serialized form the data"""
    @abstractmethod
    def rebuild(self, target_context, reduced_data):
        """Returns the de-serialized form of the *reduced_data*"""
    @abstractmethod
    def check_cachable(self, data):
        """Returns True if the given data is cachable; otherwise, returns False."""

class CompileResultCacheImpl(CacheImpl):
    """
    Implements the logic to cache CompileResult objects.
    """
    def reduce(self, cres):
        """
        Returns a serialized CompileResult
        """
    def rebuild(self, target_context, payload):
        """
        Returns the unserialized CompileResult
        """
    def check_cachable(self, cres):
        """
        Check cachability of the given compile result.
        """

class CodeLibraryCacheImpl(CacheImpl):
    """
    Implements the logic to cache CodeLibrary objects.
    """
    def reduce(self, codelib):
        """
        Returns a serialized CodeLibrary
        """
    def rebuild(self, target_context, payload):
        """
        Returns the unserialized CodeLibrary
        """
    def check_cachable(self, codelib):
        """
        Check cachability of the given CodeLibrary.
        """
    def get_filename_base(self, fullname, abiflags): ...

class IndexDataCacheFile:
    """
    Implements the logic for the index file and data file used by a cache.
    """
    def __init__(self, cache_path, filename_base, source_stamp) -> None: ...
    def flush(self) -> None: ...
    def save(self, key, data) -> None:
        """
        Save a new cache entry with *key* and *data*.
        """
    def load(self, key):
        """
        Load a cache entry with *key*.
        """

class Cache(_Cache):
    '''
    A per-function compilation cache.  The cache saves data in separate
    data files and maintains information in an index file.

    There is one index file per function and Python version
    ("function_name-<lineno>.pyXY.nbi") which contains a mapping of
    signatures and architectures to data files.
    It is prefixed by a versioning key and a timestamp of the Python source
    file containing the function.

    There is one data file ("function_name-<lineno>.pyXY.<number>.nbc")
    per function, function signature, target architecture and Python version.

    Separate index and data files per Python version avoid pickle
    compatibility problems.

    Note:
    This contains the driver logic only.  The core logic is provided
    by a subclass of ``CacheImpl`` specified as *_impl_class* in the subclass.
    '''
    def __init__(self, py_func) -> None: ...
    @property
    def cache_path(self): ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def flush(self) -> None: ...
    def load_overload(self, sig, target_context):
        """
        Load and recreate the cached object for the given signature,
        using the *target_context*.
        """
    def save_overload(self, sig, data) -> None:
        """
        Save the data for the given signature in the cache.
        """

class FunctionCache(Cache):
    """
    Implements Cache that saves and loads CompileResult objects.
    """

def make_library_cache(prefix):
    """
    Create a Cache class for additional compilation features to cache their
    result for reuse.  The cache is saved in filename pattern like
    in ``FunctionCache`` but with additional *prefix* as specified.
    """
