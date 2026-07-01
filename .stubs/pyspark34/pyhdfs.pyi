from _typeshed import Incomplete
from collections.abc import Generator

basestring = str
NotADirectoryError = OSError
DEFAULT_PORT: int
WEBHDFS_PATH: str
__version__: str

class HdfsException(Exception):
    """Base class for all errors while communicating with WebHDFS server"""
class HdfsNoServerException(HdfsException):
    """The client was not able to reach any of the given servers"""

class HdfsHttpException(HdfsException):
    """The client was able to talk to the server but got a HTTP error code.

    :param message: Exception message
    :param exception: Name of the exception
    :param javaClassName: Java class name of the exception
    :param status_code: HTTP status code
    :type status_code: int
    :param kwargs: any extra attributes in case Hadoop adds more stuff
    """
    message: Incomplete
    exception: Incomplete
    status_code: Incomplete
    def __init__(self, message, exception, status_code, **kwargs) -> None: ...

class HdfsIllegalArgumentException(HdfsHttpException): ...
class HdfsHadoopIllegalArgumentException(HdfsIllegalArgumentException): ...
class HdfsInvalidPathException(HdfsHadoopIllegalArgumentException): ...
class HdfsUnsupportedOperationException(HdfsHttpException): ...
class HdfsSecurityException(HdfsHttpException): ...
class HdfsIOException(HdfsHttpException): ...
class HdfsQuotaExceededException(HdfsIOException): ...
class HdfsNSQuotaExceededException(HdfsQuotaExceededException): ...
class HdfsDSQuotaExceededException(HdfsQuotaExceededException): ...
class HdfsAccessControlException(HdfsIOException): ...
class HdfsFileAlreadyExistsException(HdfsIOException): ...
class HdfsPathIsNotEmptyDirectoryException(HdfsIOException): ...
class HdfsRemoteException(HdfsIOException): ...
class HdfsRetriableException(HdfsIOException): ...
class HdfsStandbyException(HdfsIOException): ...
class HdfsSnapshotException(HdfsIOException): ...
class HdfsFileNotFoundException(HdfsIOException): ...
class HdfsRuntimeException(HdfsHttpException): ...

class _BoilerplateClass(dict):
    """Turns a dictionary into a nice looking object with a pretty repr.

    Unlike namedtuple, this class is very lenient. It will not error out when it gets extra
    attributes. This lets us tolerate new HDFS features without any code change at the expense of
    higher chance of error / more black magic.
    """
    __dict__: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class ContentSummary(_BoilerplateClass):
    """
    :param spaceQuota: The disk space quota.
    :type spaceQuota: int
    :param fileCount: The number of files.
    :type fileCount: int
    :param quota: The namespace quota of this directory.
    :type quota: int
    :param directoryCount: The number of directories.
    :type directoryCount: int
    :param spaceConsumed: The disk space consumed by the content.
    :type spaceConsumed: int
    :param length: The number of bytes used by the content.
    :type length: int
    """
class FileChecksum(_BoilerplateClass):
    """
    :param algorithm: The name of the checksum algorithm.
    :type algorithm: str
    :param length: The length of the bytes (not the length of the string).
    :type length: int
    :param bytes: The byte sequence of the checksum in hexadecimal.
    :type bytes: str
    """
class FileStatus(_BoilerplateClass):
    """
    :param owner: The user who is the owner.
    :type owner: str
    :param modificationTime: The modification time.
    :type modificationTime: int
    :param symlink: The link target of a symlink.
    :type symlink: str
    :param childrenNum: The number of children.
    :type childrenNum: int
    :param pathSuffix: The path suffix.
    :type pathSuffix: str
    :param blockSize: The block size of a file.
    :type blockSize: int
    :param length: The number of bytes in a file.
    :type length: int
    :param replication: The number of replication of a file.
    :type replication: int
    :param permission: The permission represented as a octal string.
    :type permission: str
    :param fileId: The inode ID.
    :type fileId: int
    :param type: The type of the path object - FILE, DIRECTORY, or SYMLINK.
    :type type: str
    :param group: The group owner.
    :type group: str
    :param accessTime: The access time.
    :type accessTime: int
    """

class HdfsClient:
    """HDFS client backed by WebHDFS.

    All functions take arbitrary query parameters to pass to WebHDFS, in addition to any documented
    keyword arguments. In particular, any function will accept ``user.name``, which for convenience
    may be passed as ``user_name``.

    If multiple HA NameNodes are given, all functions submit HTTP requests to both NameNodes until
    they find the active NameNode.

    :param hosts: List of NameNode HTTP host:port strings, either as ``list`` or a comma separated
        string. Port defaults to 50070 if left unspecified.
    :type hosts: list or str
    :param randomize_hosts: By default randomize host selection.
    :type randomize_hosts: bool
    :param user_name: What Hadoop user to run as. Defaults to the ``HADOOP_USER_NAME`` environment
        variable if present, otherwise ``getpass.getuser()``.
    :param timeout: How long to wait on a single NameNode in seconds before moving on.
        In some cases the standby NameNode can be unresponsive (e.g. loading fsimage or
        checkpointing), so we don't want to block on it.
    :type timeout: float
    :param max_tries: How many times to retry a request for each NameNode. If NN1 is standby and NN2
        is active, we might first contact NN1 and then observe a failover to NN1 when we contact
        NN2. In this situation we want to retry against NN1.
    :type max_tries: int
    :param retry_delay: How long to wait in seconds before going through NameNodes again
    :type retry_delay: float
    :param webhdfs_path: The HTTP URL format in webhdfs request is
        ``http://<HOST>:<HTTP_PORT><WEBHDFS_PATH><PATH>?op=...``, this param could set WEBHDFS_PATH
        as the customized one, and the default value of WEBHDFS_PATH is '/webhdfs/v1'
    :type webhdfs_path: str
    :param requests_session: A ``requests.Session`` object for advanced usage. If absent, this
        class will use the default requests behavior of making a new session per HTTP request.
        Caller is responsible for closing session.
    :param requests_kwargs: Additional ``**kwargs`` to pass to requests
    """
    randomize_hosts: Incomplete
    hosts: Incomplete
    timeout: Incomplete
    max_tries: Incomplete
    retry_delay: Incomplete
    user_name: Incomplete
    def __init__(self, hosts: str = 'localhost', randomize_hosts: bool = True, user_name: Incomplete | None = None, timeout: int = 20, max_tries: int = 2, retry_delay: int = 5, webhdfs_path: str = '/webhdfs/v1', requests_session: Incomplete | None = None, requests_kwargs: Incomplete | None = None) -> None:
        """Create a new HDFS client"""
    def create(self, path, data, **kwargs) -> None:
        """Create a file at the given path.

        :param data: ``bytes`` or a ``file``-like object to upload
        :param overwrite: If a file already exists, should it be overwritten?
        :type overwrite: bool
        :param blocksize: The block size of a file.
        :type blocksize: long
        :param replication: The number of replications of a file.
        :type replication: short
        :param permission: The permission of a file/directory. Any radix-8 integer (leading zeros
            may be omitted.)
        :type permission: octal
        :param buffersize: The size of the buffer used in transferring data.
        :type buffersize: int
        """
    def append(self, path, data, **kwargs) -> None:
        """Append to the given file.

        :param data: ``bytes`` or a ``file``-like object
        :param buffersize: The size of the buffer used in transferring data.
        :type buffersize: int
        """
    def concat(self, target, sources, **kwargs) -> None:
        """Concat existing files together.

        Conditions:

        - The last block in the target file (``path``) must be full.
        - All blocks must be the same size, except possibly the last block.

        :param target: the path to the target destination.
        :param sources: the paths to the sources to use for the concatenation.
        :type sources: list
        """
    def open(self, path, **kwargs):
        """Return a file-like object for reading the given HDFS path.

        :param offset: The starting byte position.
        :type offset: long
        :param length: The number of bytes to be processed.
        :type length: long
        :param buffersize: The size of the buffer used in transferring data.
        :type buffersize: int
        :rtype: file-like object
        """
    def mkdirs(self, path, **kwargs):
        """Create a directory with the provided permission.

        The permission of the directory is set to be the provided permission as in setPermission,
        not permission&~umask.

        :param permission: The permission of a file/directory. Any radix-8 integer (leading zeros
            may be omitted.)
        :type permission: octal
        :returns: true if the directory creation succeeds; false otherwise
        :rtype: bool
        """
    def create_symlink(self, link, destination, **kwargs) -> None:
        """Create a symbolic link at ``link`` pointing to ``destination``.

        :param link: the path to be created that points to target
        :param destination: the target of the symbolic link
        :param createParent: If the parent directories do not exist, should they be created?
        :type createParent: bool
        :raises HdfsUnsupportedOperationException: This feature doesn't actually work, at least on
            CDH 5.3.0.
        """
    def rename(self, path, destination, **kwargs):
        """Renames Path src to Path dst.

        :returns: true if rename is successful
        :rtype: bool
        """
    def delete(self, path, **kwargs):
        """Delete a file.

        :param recursive: If path is a directory and set to true, the directory is deleted else
            throws an exception. In case of a file the recursive can be set to either true or false.
        :type recursive: bool
        :returns: true if delete is successful else false.
        :rtype: bool
        """
    def get_file_status(self, path, **kwargs):
        """Return a :py:class:`FileStatus` object that represents the path."""
    def list_status(self, path, **kwargs):
        """List the statuses of the files/directories in the given path if the path is a directory.

        :rtype: ``list`` of :py:class:`FileStatus` objects
        """
    def get_content_summary(self, path, **kwargs):
        """Return the :py:class:`ContentSummary` of a given Path."""
    def get_file_checksum(self, path, **kwargs):
        """Get the checksum of a file.

        :rtype: :py:class:`FileChecksum`
        """
    def get_home_directory(self, **kwargs):
        """Return the current user's home directory in this filesystem."""
    def set_permission(self, path, **kwargs) -> None:
        """Set permission of a path.

        :param permission: The permission of a file/directory. Any radix-8 integer (leading zeros
            may be omitted.)
        :type permission: octal
        """
    def set_owner(self, path, **kwargs) -> None:
        """Set owner of a path (i.e. a file or a directory).

        The parameters owner and group cannot both be null.

        :param owner: user
        :param group: group
        """
    def set_replication(self, path, **kwargs):
        """Set replication for an existing file.

        :param replication: new replication
        :type replication: short
        :returns: true if successful; false if file does not exist or is a directory
        :rtype: bool
        """
    def set_times(self, path, **kwargs) -> None:
        """Set access time of a file.

        :param modificationtime: Set the modification time of this file. The number of milliseconds
            since Jan 1, 1970.
        :type modificationtime: long
        :param accesstime: Set the access time of this file. The number of milliseconds since Jan 1
            1970.
        :type accesstime: long
        """
    def set_xattr(self, path, xattr_name, xattr_value, flag, **kwargs) -> None:
        """Set an xattr of a file or directory.

        :param xattr_name: The name must be prefixed with the namespace followed by ``.``. For
            example, ``user.attr``.
        :param flag: ``CREATE`` or ``REPLACE``
        """
    def remove_xattr(self, path, xattr_name, **kwargs) -> None:
        """Remove an xattr of a file or directory."""
    def get_xattrs(self, path, xattr_name: Incomplete | None = None, encoding: str = 'text', **kwargs):
        """Get one or more xattr values for a file or directory.

        :param xattr_name: ``str`` to get one attribute, ``list`` to get multiple attributes,
            ``None`` to get all attributes.
        :param encoding: ``text`` | ``hex`` | ``base64``, defaults to ``text``

        :returns: Dictionary mapping xattr name to value. With text encoding, the value will be a
            unicode string. With hex or base64 encoding, the value will be a byte array.
        :rtype: dict
        """
    def list_xattrs(self, path, **kwargs):
        """Get all of the xattr names for a file or directory.

        :rtype: list
        """
    def create_snapshot(self, path, **kwargs):
        """Create a snapshot

        :param path: The directory where snapshots will be taken
        :param snapshotname: The name of the snapshot
        :returns: the snapshot path
        """
    def delete_snapshot(self, path, snapshotname, **kwargs) -> None:
        """Delete a snapshot of a directory"""
    def rename_snapshot(self, path, oldsnapshotname, snapshotname, **kwargs) -> None:
        """Rename a snapshot"""
    def listdir(self, path, **kwargs):
        """Return a list containing names of files in the given path"""
    def exists(self, path, **kwargs):
        """Return true if the given path exists"""
    def walk(self, top, topdown: bool = True, onerror: Incomplete | None = None, **kwargs) -> Generator[Incomplete, None, None]:
        """See ``os.walk`` for documentation"""
    def copy_from_local(self, localsrc, dest, **kwargs) -> None:
        """Copy a single file from the local file system to ``dest``

        Takes all arguments that :py:meth:`create` takes.
        """
    def copy_to_local(self, src, localdest, **kwargs) -> None:
        """Copy a single file from ``src`` to the local file system

        Takes all arguments that :py:meth:`open` takes.
        """
    def get_active_namenode(self, max_staleness: Incomplete | None = None):
        """Return the address of the currently active NameNode.

        :param max_staleness: This function caches the active NameNode. If this age of this cached
            result is less than ``max_staleness`` seconds, return it. Otherwise, or if this
            parameter is None, do a lookup.
        :type max_staleness: float
        :raises HdfsNoServerException: can't find an active NameNode
        """
