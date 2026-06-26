from gitdb.util import LazyMixin

__all__ = ['ObjectDBR', 'ObjectDBW', 'FileDBBase', 'CompoundDB', 'CachingDB']

class ObjectDBR:
    """Defines an interface for object database lookup.
    Objects are identified either by their 20 byte bin sha"""
    def __contains__(self, sha) -> bool: ...
    def has_object(self, sha) -> None:
        """
        Whether the object identified by the given 20 bytes
            binary sha is contained in the database

        :return: True if the object identified by the given 20 bytes
            binary sha is contained in the database"""
    def info(self, sha) -> None:
        """ :return: OInfo instance
        :param sha: bytes binary sha
        :raise BadObject:"""
    def stream(self, sha) -> None:
        """:return: OStream instance
        :param sha: 20 bytes binary sha
        :raise BadObject:"""
    def size(self) -> None:
        """:return: amount of objects in this database"""
    def sha_iter(self) -> None:
        """Return iterator yielding 20 byte shas for all objects in this data base"""

class ObjectDBW:
    """Defines an interface to create objects in the database"""
    def __init__(self, *args, **kwargs) -> None: ...
    def set_ostream(self, stream):
        """
        Adjusts the stream to which all data should be sent when storing new objects

        :param stream: if not None, the stream to use, if None the default stream
            will be used.
        :return: previously installed stream, or None if there was no override
        :raise TypeError: if the stream doesn't have the supported functionality"""
    def ostream(self):
        """
        Return the output stream

        :return: overridden output stream this instance will write to, or None
            if it will write to the default stream"""
    def store(self, istream) -> None:
        """
        Create a new object in the database
        :return: the input istream object with its sha set to its corresponding value

        :param istream: IStream compatible instance. If its sha is already set
            to a value, the object will just be stored in the our database format,
            in which case the input stream is expected to be in object format ( header + contents ).
        :raise IOError: if data could not be written"""

class FileDBBase:
    """Provides basic facilities to retrieve files of interest, including
    caching facilities to help mapping hexsha's to objects"""
    def __init__(self, root_path) -> None:
        """Initialize this instance to look for its files at the given root path
        All subsequent operations will be relative to this path
        :raise InvalidDBRoot:
        **Note:** The base will not perform any accessablity checking as the base
            might not yet be accessible, but become accessible before the first
            access."""
    def root_path(self):
        """:return: path at which this db operates"""
    def db_path(self, rela_path):
        """
        :return: the given relative path relative to our database root, allowing
            to pontentially access datafiles"""

class CachingDB:
    """A database which uses caches to speed-up access"""
    def update_cache(self, force: bool = False) -> None:
        """
        Call this method if the underlying data changed to trigger an update
        of the internal caching structures.

        :param force: if True, the update must be performed. Otherwise the implementation
            may decide not to perform an update if it thinks nothing has changed.
        :return: True if an update was performed as something change indeed"""

class CompoundDB(ObjectDBR, LazyMixin, CachingDB):
    """A database which delegates calls to sub-databases.

    Databases are stored in the lazy-loaded _dbs attribute.
    Define _set_cache_ to update it with your databases"""
    def has_object(self, sha): ...
    def info(self, sha): ...
    def stream(self, sha): ...
    def size(self):
        """:return: total size of all contained databases"""
    def sha_iter(self): ...
    def databases(self):
        """:return: tuple of database instances we use for lookups"""
    def update_cache(self, force: bool = False): ...
    def partial_to_complete_sha_hex(self, partial_hexsha):
        """
        :return: 20 byte binary sha1 from the given less-than-40 byte hexsha (bytes or str)
        :param partial_hexsha: hexsha with less than 40 byte
        :raise AmbiguousObjectName: """
