from . import numpy_pickle as numpy_pickle
from .backports import concurrency_safe_rename as concurrency_safe_rename
from .disk import memstr_to_bytes as memstr_to_bytes, mkdirp as mkdirp, rm_subdirs as rm_subdirs
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from typing import NamedTuple

class CacheItemInfo(NamedTuple):
    path: Incomplete
    size: Incomplete
    last_access: Incomplete

class CacheWarning(Warning):
    """Warning to capture dump failures except for PicklingError."""

def concurrency_safe_write(object_to_write, filename, write_func):
    """Writes an object into a unique file in a concurrency-safe way."""

class StoreBackendBase(metaclass=ABCMeta):
    """Helper Abstract Base Class which defines all methods that
       a StorageBackend must implement."""
    location: Incomplete
    @abstractmethod
    def create_location(self, location):
        """Creates a location on the store.

        Parameters
        ----------
        location: string
            The location in the store. On a filesystem, this corresponds to a
            directory.
        """
    @abstractmethod
    def clear_location(self, location):
        """Clears a location on the store.

        Parameters
        ----------
        location: string
            The location in the store. On a filesystem, this corresponds to a
            directory or a filename absolute path
        """
    @abstractmethod
    def get_items(self):
        """Returns the whole list of items available in the store.

        Returns
        -------
        The list of items identified by their ids (e.g filename in a
        filesystem).
        """
    @abstractmethod
    def configure(self, location, verbose: int = 0, backend_options=...):
        """Configures the store.

        Parameters
        ----------
        location: string
            The base location used by the store. On a filesystem, this
            corresponds to a directory.
        verbose: int
            The level of verbosity of the store
        backend_options: dict
            Contains a dictionary of named parameters used to configure the
            store backend.
        """

class StoreBackendMixin:
    """Class providing all logic for managing the store in a generic way.

    The StoreBackend subclass has to implement 3 methods: create_location,
    clear_location and configure. The StoreBackend also has to provide
    a private _open_item, _item_exists and _move_item methods. The _open_item
    method has to have the same signature as the builtin open and return a
    file-like object.
    """
    def load_item(self, path, verbose: int = 1, msg: Incomplete | None = None):
        """Load an item from the store given its path as a list of
           strings."""
    def dump_item(self, path, item, verbose: int = 1) -> None:
        """Dump an item in the store at the path given as a list of
           strings."""
    def clear_item(self, path) -> None:
        """Clear the item at the path, given as a list of strings."""
    def contains_item(self, path):
        """Check if there is an item at the path, given as a list of
           strings"""
    def get_item_info(self, path):
        """Return information about item."""
    def get_metadata(self, path):
        """Return actual metadata of an item."""
    def store_metadata(self, path, metadata) -> None:
        """Store metadata of a computation."""
    def contains_path(self, path):
        """Check cached function is available in store."""
    def clear_path(self, path) -> None:
        """Clear all items with a common path in the store."""
    def store_cached_func_code(self, path, func_code: Incomplete | None = None) -> None:
        """Store the code of the cached function."""
    def get_cached_func_code(self, path):
        """Store the code of the cached function."""
    def get_cached_func_info(self, path):
        """Return information related to the cached function if it exists."""
    def clear(self) -> None:
        """Clear the whole store content."""
    def enforce_store_limits(self, bytes_limit, items_limit: Incomplete | None = None, age_limit: Incomplete | None = None) -> None:
        """
        Remove the store's oldest files to enforce item, byte, and age limits.
        """

class FileSystemStoreBackend(StoreBackendBase, StoreBackendMixin):
    """A StoreBackend used with local or network file systems."""
    def clear_location(self, location) -> None:
        """Delete location on store."""
    def create_location(self, location) -> None:
        """Create object location on store"""
    def get_items(self):
        """Returns the whole list of items available in the store."""
    location: Incomplete
    compress: Incomplete
    mmap_mode: Incomplete
    verbose: Incomplete
    def configure(self, location, verbose: int = 1, backend_options: Incomplete | None = None) -> None:
        """Configure the store backend.

        For this backend, valid store options are 'compress' and 'mmap_mode'
        """
