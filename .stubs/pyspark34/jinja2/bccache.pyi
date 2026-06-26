import typing as t
import typing_extensions as te
from .environment import Environment as Environment
from _typeshed import Incomplete

class _MemcachedClient(te.Protocol):
    def get(self, key: str) -> bytes: ...
    def set(self, key: str, value: bytes, timeout: int | None = None) -> None: ...

bc_version: int
bc_magic: Incomplete

class Bucket:
    """Buckets are used to store the bytecode for one template.  It's created
    and initialized by the bytecode cache and passed to the loading functions.

    The buckets get an internal checksum from the cache assigned and use this
    to automatically reject outdated cache material.  Individual bytecode
    cache subclasses don't have to care about cache invalidation.
    """
    environment: Incomplete
    key: Incomplete
    checksum: Incomplete
    def __init__(self, environment: Environment, key: str, checksum: str) -> None: ...
    code: Incomplete
    def reset(self) -> None:
        """Resets the bucket (unloads the bytecode)."""
    def load_bytecode(self, f: t.BinaryIO) -> None:
        """Loads bytecode from a file or file like object."""
    def write_bytecode(self, f: t.IO[bytes]) -> None:
        """Dump the bytecode into the file or file like object passed."""
    def bytecode_from_string(self, string: bytes) -> None:
        """Load bytecode from bytes."""
    def bytecode_to_string(self) -> bytes:
        """Return the bytecode as bytes."""

class BytecodeCache:
    """To implement your own bytecode cache you have to subclass this class
    and override :meth:`load_bytecode` and :meth:`dump_bytecode`.  Both of
    these methods are passed a :class:`~jinja2.bccache.Bucket`.

    A very basic bytecode cache that saves the bytecode on the file system::

        from os import path

        class MyCache(BytecodeCache):

            def __init__(self, directory):
                self.directory = directory

            def load_bytecode(self, bucket):
                filename = path.join(self.directory, bucket.key)
                if path.exists(filename):
                    with open(filename, 'rb') as f:
                        bucket.load_bytecode(f)

            def dump_bytecode(self, bucket):
                filename = path.join(self.directory, bucket.key)
                with open(filename, 'wb') as f:
                    bucket.write_bytecode(f)

    A more advanced version of a filesystem based bytecode cache is part of
    Jinja.
    """
    def load_bytecode(self, bucket: Bucket) -> None:
        """Subclasses have to override this method to load bytecode into a
        bucket.  If they are not able to find code in the cache for the
        bucket, it must not do anything.
        """
    def dump_bytecode(self, bucket: Bucket) -> None:
        """Subclasses have to override this method to write the bytecode
        from a bucket back to the cache.  If it unable to do so it must not
        fail silently but raise an exception.
        """
    def clear(self) -> None:
        """Clears the cache.  This method is not used by Jinja but should be
        implemented to allow applications to clear the bytecode cache used
        by a particular environment.
        """
    def get_cache_key(self, name: str, filename: str | None = None) -> str:
        """Returns the unique hash key for this template name."""
    def get_source_checksum(self, source: str) -> str:
        """Returns a checksum for the source."""
    def get_bucket(self, environment: Environment, name: str, filename: str | None, source: str) -> Bucket:
        """Return a cache bucket for the given template.  All arguments are
        mandatory but filename may be `None`.
        """
    def set_bucket(self, bucket: Bucket) -> None:
        """Put the bucket into the cache."""

class FileSystemBytecodeCache(BytecodeCache):
    """A bytecode cache that stores bytecode on the filesystem.  It accepts
    two arguments: The directory where the cache items are stored and a
    pattern string that is used to build the filename.

    If no directory is specified a default cache directory is selected.  On
    Windows the user's temp directory is used, on UNIX systems a directory
    is created for the user in the system temp directory.

    The pattern can be used to have multiple separate caches operate on the
    same directory.  The default pattern is ``'__jinja2_%s.cache'``.  ``%s``
    is replaced with the cache key.

    >>> bcc = FileSystemBytecodeCache('/tmp/jinja_cache', '%s.cache')

    This bytecode cache supports clearing of the cache using the clear method.
    """
    directory: Incomplete
    pattern: Incomplete
    def __init__(self, directory: str | None = None, pattern: str = '__jinja2_%s.cache') -> None: ...
    def load_bytecode(self, bucket: Bucket) -> None: ...
    def dump_bytecode(self, bucket: Bucket) -> None: ...
    def clear(self) -> None: ...

class MemcachedBytecodeCache(BytecodeCache):
    """This class implements a bytecode cache that uses a memcache cache for
    storing the information.  It does not enforce a specific memcache library
    (tummy's memcache or cmemcache) but will accept any class that provides
    the minimal interface required.

    Libraries compatible with this class:

    -   `cachelib <https://github.com/pallets/cachelib>`_
    -   `python-memcached <https://pypi.org/project/python-memcached/>`_

    (Unfortunately the django cache interface is not compatible because it
    does not support storing binary data, only text. You can however pass
    the underlying cache client to the bytecode cache which is available
    as `django.core.cache.cache._client`.)

    The minimal interface for the client passed to the constructor is this:

    .. class:: MinimalClientInterface

        .. method:: set(key, value[, timeout])

            Stores the bytecode in the cache.  `value` is a string and
            `timeout` the timeout of the key.  If timeout is not provided
            a default timeout or no timeout should be assumed, if it's
            provided it's an integer with the number of seconds the cache
            item should exist.

        .. method:: get(key)

            Returns the value for the cache key.  If the item does not
            exist in the cache the return value must be `None`.

    The other arguments to the constructor are the prefix for all keys that
    is added before the actual cache key and the timeout for the bytecode in
    the cache system.  We recommend a high (or no) timeout.

    This bytecode cache does not support clearing of used items in the cache.
    The clear method is a no-operation function.

    .. versionadded:: 2.7
       Added support for ignoring memcache errors through the
       `ignore_memcache_errors` parameter.
    """
    client: Incomplete
    prefix: Incomplete
    timeout: Incomplete
    ignore_memcache_errors: Incomplete
    def __init__(self, client: _MemcachedClient, prefix: str = 'jinja2/bytecode/', timeout: int | None = None, ignore_memcache_errors: bool = True) -> None: ...
    def load_bytecode(self, bucket: Bucket) -> None: ...
    def dump_bytecode(self, bucket: Bucket) -> None: ...
