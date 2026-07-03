from .enums import ExpiryOptionType as ExpiryOptionType
from .exceptions import DatalakeBadOffsetException as DatalakeBadOffsetException, DatalakeIncompleteTransferException as DatalakeIncompleteTransferException, FileNotFoundError as FileNotFoundError, PermissionError as PermissionError
from .lib import DatalakeRESTInterface as DatalakeRESTInterface
from .multiprocessor import multi_processor_change_acl as multi_processor_change_acl
from .retry import ExponentialRetryPolicy as ExponentialRetryPolicy, NoRetryPolicy as NoRetryPolicy
from .utils import ensure_writable as ensure_writable, read_block as read_block
from _typeshed import Incomplete

logger: Incomplete
valid_expire_types: Incomplete

class AzureDLFileSystem:
    '''
    Access Azure DataLake Store as if it were a file-system

    Parameters
    ----------
    store_name: str ("")
        Store name to connect to.
    token: credentials object
        When setting up a new connection, this contains the authorization
        credentials (see `lib.auth()`).
    url_suffix: str (None)
        Domain to send REST requests to. The end-point URL is constructed
        using this and the store_name. If None, use default.
    api_version: str (2018-09-01)
        The API version to target with requests. Changing this value will
        change the behavior of the requests, and can cause unexpected behavior or
        breaking changes. Changes to this value should be undergone with caution.
    per_call_timeout_seconds: float(60)
        This is the timeout for each requests library call.
    kwargs: optional key/values
        See ``lib.auth()``; full list: tenant_id, username, password, client_id,
        client_secret, resource
    '''
    token: Incomplete
    kwargs: Incomplete
    per_call_timeout_seconds: Incomplete
    dirs: Incomplete
    def __init__(self, token: Incomplete | None = None, per_call_timeout_seconds: int = 60, **kwargs) -> None: ...
    @classmethod
    def current(cls):
        """ Return the most recently created AzureDLFileSystem
        """
    azure: Incomplete
    def connect(self) -> None:
        """
        Establish connection object.
        """
    def open(self, path, mode: str = 'rb', blocksize=..., delimiter: Incomplete | None = None):
        """ Open a file for reading or writing

        Parameters
        ----------
        path: string
            Path of file on ADL
        mode: string
            One of 'rb', 'ab' or 'wb'
        blocksize: int
            Size of data-node blocks if reading
        delimiter: byte(s) or None
            For writing delimiter-ended blocks
        """
    def ls(self, path: str = '', detail: bool = False, invalidate_cache: bool = True):
        """
        List all elements under directory specified with path

        Parameters
        ----------
        path: str or AzureDLPath
            Path to query
        detail: bool
            Detailed info or not.
        invalidate_cache: bool
            Whether to invalidate cache or not

        Returns
        -------
        List of elements under directory specified with path
        """
    def info(self, path, invalidate_cache: bool = True, expected_error_code: Incomplete | None = None):
        """
        File information for path

        Parameters
        ----------
        path: str or AzureDLPath
            Path to query
        invalidate_cache: bool
            Whether to invalidate cache or not
        expected_error_code:  int
            Optionally indicates a specific, expected error code, if any.

        Returns
        -------
        File information
        """
    def walk(self, path: str = '', details: bool = False, invalidate_cache: bool = True):
        """
        Get all files below given path

        Parameters
        ----------
        path: str or AzureDLPath
            Path to query
        details: bool
            Whether to include file details
        invalidate_cache: bool
            Whether to invalidate cache

        Returns
        -------
        List of files
        """
    def glob(self, path, details: bool = False, invalidate_cache: bool = True):
        """
        Find files (not directories) by glob-matching.

        Parameters
        ----------
        path: str or AzureDLPath
            Path to query
        details: bool
            Whether to include file details
        invalidate_cache: bool
            Whether to invalidate cache

        Returns
        -------
        List of files
        """
    def du(self, path, total: bool = False, deep: bool = False, invalidate_cache: bool = True):
        """
        Bytes in keys at path

        Parameters
        ----------
        path: str or AzureDLPath
            Path to query
        total: bool
            Return the sum on list
        deep: bool
            Recursively enumerate or just use files under current dir
        invalidate_cache: bool
            Whether to invalidate cache

        Returns
        -------
        List of dict of name:size pairs or total size.
        """
    def df(self, path):
        """ Resource summary of path

        Parameters
        ----------
        path: str
            Path to query
        """
    def chmod(self, path, mod) -> None:
        '''  Change access mode of path

        Note this is not recursive.

        Parameters
        ----------
        path: str
            Location to change
        mod: str
            Octal representation of access, e.g., "0777" for public read/write.
            See [docs](http://hadoop.apache.org/docs/r2.4.1/hadoop-project-dist/hadoop-hdfs/WebHDFS.html#Permission)
        '''
    def set_expiry(self, path, expiry_option, expire_time: Incomplete | None = None) -> None:
        """
        Set or remove the expiration time on the specified file.
        This operation can only be executed against files.

        Note: Folders are not supported.

        Parameters
        ----------
        path: str
            File path to set or remove expiration time
        expire_time: int
            The time that the file will expire, corresponding to the expiry_option that was set
        expiry_option: str
            Indicates the type of expiration to use for the file:
                1. NeverExpire: ExpireTime is ignored.
                2. RelativeToNow: ExpireTime is an integer in milliseconds representing the expiration date relative to when file expiration is updated.
                3. RelativeToCreationDate: ExpireTime is an integer in milliseconds representing the expiration date relative to file creation.
                4. Absolute: ExpireTime is an integer in milliseconds, as a Unix timestamp relative to 1/1/1970 00:00:00.
        """
    def set_acl(self, path, acl_spec, recursive: bool = False, number_of_sub_process: Incomplete | None = None) -> None:
        """
        Set the Access Control List (ACL) for a file or folder.

        Note: this is by default not recursive, and applies only to the file or folder specified.

        Parameters
        ----------
        path: str
            Location to set the ACL on.
        acl_spec: str
            The ACL specification to set on the path in the format
            '[default:]user|group|other:[entity id or UPN]:r|-w|-x|-,[default:]user|group|other:[entity id or UPN]:r|-w|-x|-,...'
        recursive: bool
            Specifies whether to set ACLs recursively or not
        """
    def modify_acl_entries(self, path, acl_spec, recursive: bool = False, number_of_sub_process: Incomplete | None = None) -> None:
        """
        Modify existing Access Control List (ACL) entries on a file or folder.
        If the entry does not exist it is added, otherwise it is updated based on the spec passed in.
        No entries are removed by this process (unlike set_acl).

        Note: this is by default not recursive, and applies only to the file or folder specified.

        Parameters
        ----------
        path: str
            Location to set the ACL entries on.
        acl_spec: str
            The ACL specification to use in modifying the ACL at the path in the format
            '[default:]user|group|other:[entity id or UPN]:r|-w|-x|-,[default:]user|group|other:[entity id or UPN]:r|-w|-x|-,...'
        recursive: bool
            Specifies whether to modify ACLs recursively or not
        """
    def remove_acl_entries(self, path, acl_spec, recursive: bool = False, number_of_sub_process: Incomplete | None = None) -> None:
        """
        Remove existing, named, Access Control List (ACL) entries on a file or folder.
        If the entry does not exist already it is ignored.
        Default entries cannot be removed this way, please use remove_default_acl for that.
        Unnamed entries cannot be removed in this way, please use remove_acl for that.

        Note: this is by default not recursive, and applies only to the file or folder specified.

        Parameters
        ----------
        path: str
            Location to remove the ACL entries.
        acl_spec: str
            The ACL specification to remove from the ACL at the path in the format (note that the permission portion is missing)
            '[default:]user|group|other:[entity id or UPN],[default:]user|group|other:[entity id or UPN],...'
        recursive: bool
            Specifies whether to remove ACLs recursively or not
        """
    def get_acl_status(self, path):
        """
        Gets Access Control List (ACL) entries for the specified file or directory.

        Parameters
        ----------
        path: str
            Location to get the ACL.
        """
    def remove_acl(self, path) -> None:
        """
        Remove the entire, non default, ACL from the file or folder, including unnamed entries.
        Default entries cannot be removed this way, please use remove_default_acl for that.

        Note: this is not recursive, and applies only to the file or folder specified.

        Parameters
        ----------
        path: str
            Location to remove the ACL.
        """
    def remove_default_acl(self, path) -> None:
        """
        Remove the entire default ACL from the folder.
        Default entries do not exist on files, if a file
        is specified, this operation does nothing.

        Note: this is not recursive, and applies only to the folder specified.

        Parameters
        ----------
        path: str
            Location to set the ACL on.
        """
    def chown(self, path, owner: Incomplete | None = None, group: Incomplete | None = None) -> None:
        """
        Change owner and/or owning group

        Note this is not recursive.

        Parameters
        ----------
        path: str
            Location to change
        owner: str
            UUID of owning entity
        group: str
            UUID of group
        """
    def exists(self, path, invalidate_cache: bool = True):
        """
        Does such a file/directory exist?

        Parameters
        ----------
        path: str or AzureDLPath
            Path to query
        invalidate_cache: bool
            Whether to invalidate cache

        Returns
        -------
        True or false depending on whether the path exists.
        """
    def cat(self, path):
        """
        Return contents of file

        Parameters
        ----------
        path: str or AzureDLPath
            Path to query

        Returns
        -------
        Contents of file
        """
    def tail(self, path, size: int = 1024):
        """
        Return last bytes of file

        Parameters
        ----------
        path: str or AzureDLPath
            Path to query
        size: int
            How many bytes to return

        Returns
        -------
        Last(size) bytes of file
        """
    def head(self, path, size: int = 1024):
        """
        Return first bytes of file

        Parameters
        ----------
        path: str or AzureDLPath
            Path to query
        size: int
            How many bytes to return

        Returns
        -------
        First(size) bytes of file
        """
    def get(self, path, filename) -> None:
        """
        Stream data from file at path to local filename

        Parameters
        ----------
        path: str or AzureDLPath
            ADL Path to read
        filename: str or Path
            Local file path to write to

        Returns
        -------
        None
        """
    def put(self, filename, path, delimiter: Incomplete | None = None) -> None:
        """
        Stream data from local filename to file at path

        Parameters
        ----------
        filename: str or Path
            Local file path to read from
        path: str or AzureDLPath
            ADL Path to write to
        delimiter:
            Optional delimeter for delimiter-ended blocks

        Returns
        -------
        None
        """
    def mkdir(self, path) -> None:
        """
        Make new directory

        Parameters
        ----------
        path: str or AzureDLPath
            Path to create directory

        Returns
        -------
        None
        """
    def rmdir(self, path) -> None:
        """
        Remove empty directory

        Parameters
        ----------
        path: str or AzureDLPath
            Directory  path to remove

        Returns
        -------
        None
        """
    def mv(self, path1, path2) -> None:
        """
        Move file between locations on ADL

        Parameters
        ----------
        path1:
            Source Path
        path2:
            Destination path

        Returns
        -------
        None
        """
    def concat(self, outfile, filelist, delete_source: bool = False) -> None:
        """ Concatenate a list of files into one new file

        Parameters
        ----------

        outfile: path
            The file which will be concatenated to. If it already exists,
            the extra pieces will be appended.
        filelist: list of paths
            Existing adl files to concatenate, in order
        delete_source: bool (False)
            If True, assume that the paths to concatenate exist alone in a
            directory, and delete that whole directory when done.

        Returns
        -------
        None
        """
    merge = concat
    def cp(self, path1, path2) -> None:
        """ Not implemented. Copy file between locations on ADL """
    def rm(self, path, recursive: bool = False) -> None:
        """
        Remove a file or directory

        Parameters
        ----------
        path: str or AzureDLPath
            The location to remove.
        recursive: bool (True)
            Whether to remove also all entries below, i.e., which are returned
            by `walk()`.

        Returns
        -------
        None
        """
    def invalidate_cache(self, path: Incomplete | None = None) -> None:
        """
        Remove entry from object file-cache

        Parameters
        ----------
        path: str or AzureDLPath
            Remove the path from object file-cache

        Returns
        -------
        None
        """
    def touch(self, path) -> None:
        """
        Create empty file

        Parameters
        ----------
        path: str or AzureDLPath
            Path of file to create

        Returns
        -------
        None
        """
    def read_block(self, fn, offset, length, delimiter: Incomplete | None = None):
        """ Read a block of bytes from an ADL file

        Starting at ``offset`` of the file, read ``length`` bytes.  If
        ``delimiter`` is set then we ensure that the read starts and stops at
        delimiter boundaries that follow the locations ``offset`` and ``offset
        + length``.  If ``offset`` is zero then we start at zero.  The
        bytestring returned WILL include the end delimiter string.

        If offset+length is beyond the eof, reads to eof.

        Parameters
        ----------
        fn: string
            Path to filename on ADL
        offset: int
            Byte offset to start read
        length: int
            Number of bytes to read
        delimiter: bytes (optional)
            Ensure reading starts and stops at delimiter bytestring

        Examples
        --------
        >>> adl.read_block('data/file.csv', 0, 13)  # doctest: +SKIP
        b'Alice, 100\\nBo'
        >>> adl.read_block('data/file.csv', 0, 13, delimiter=b'\\n')  # doctest: +SKIP
        b'Alice, 100\\nBob, 200\\n'

        Use ``length=None`` to read to the end of the file.
        >>> adl.read_block('data/file.csv', 0, None, delimiter=b'\\n')  # doctest: +SKIP
        b'Alice, 100\\nBob, 200\\nCharlie, 300'

        See Also
        --------
        distributed.utils.read_block
        """
    listdir = ls
    access = exists
    rename = mv
    stat = info
    unlink = rm
    remove = rm

class AzureDLFile:
    """
    Open ADL key as a file. Data is only loaded and cached on demand.

    Parameters
    ----------
    azure: azure connection
    path: AzureDLPath
        location of file
    mode: str {'wb', 'rb', 'ab'}
    blocksize: int
        Size of the write or read-ahead buffer. For writing(and appending, will be
        truncated to 4MB (2**22).
    delimiter: bytes or None
        If specified and in write mode, each flush will send data terminating
        on this bytestring, potentially leaving some data in the buffer.

    Examples
    --------
    >>> adl = AzureDLFileSystem()  # doctest: +SKIP
    >>> with adl.open('my-dir/my-file.txt', mode='rb') as f:  # doctest: +SKIP
    ...     f.read(10)  # doctest: +SKIP

    See Also
    --------
    AzureDLFileSystem.open: used to create AzureDLFile objects
    """
    mode: Incomplete
    path: Incomplete
    azure: Incomplete
    cache: bytes
    loc: int
    delimiter: Incomplete
    start: int
    end: int
    closed: bool
    trim: bool
    buffer: Incomplete
    blocksize: Incomplete
    filesessionid: Incomplete
    leaseid: Incomplete
    size: Incomplete
    def __init__(self, azure, path, mode: str = 'rb', blocksize=..., delimiter: Incomplete | None = None) -> None: ...
    def info(self):
        """ File information about this path """
    def tell(self):
        """ Current file location """
    def seek(self, loc, whence: int = 0):
        """ Set current file location

        Parameters
        ----------
        loc: int
            byte location
        whence: {0, 1, 2}
            from start of file, current location or end of file, resp.
        """
    def readline(self, length: int = -1):
        """
        Read and return a line from the stream.

        If length is specified, at most size bytes will be read.
        """
    def __next__(self): ...
    next = __next__
    def __iter__(self): ...
    def readlines(self):
        """ Return all lines in a file as a list """
    def read(self, length: int = -1):
        """
        Return data from cache, or fetch pieces as necessary

        Parameters
        ----------
        length: int (-1)
            Number of bytes to read; if <0, all remaining bytes.
        """
    read1 = read
    def readinto(self, b):
        """
        Reads data into buffer b


        Parameters
        ----------
        b: bytearray
            Buffer to which bytes are read into

        Returns
        -------
        Returns number of bytes read.
        """
    def write(self, data):
        """
        Write data to buffer.

        Buffer only sent to ADL on flush() or if buffer is bigger than
        blocksize.

        Parameters
        ----------
        data: bytes
            Set of bytes to be written.
        """
    def flush(self, syncFlag: str = 'METADATA', force: bool = False) -> None:
        """
        Write buffered data to ADL.

        Without delimiter: Uploads the current buffer.

        With delimiter: writes an amount of data less than or equal to the
        block-size, which ends on the delimiter, until buffer is smaller than
        the blocksize. If there is no delimiter in a block uploads whole block.

        If force=True, flushes all data in the buffer, even if it doesn't end
        with a delimiter; appropriate when closing the file.
        """
    def close(self) -> None:
        """ Close file

        If in write mode, causes flush of any unwritten data.
        """
    def readable(self):
        """Return whether the AzureDLFile was opened for reading"""
    def seekable(self):
        """Return whether the AzureDLFile is seekable (only in read mode)"""
    def writable(self):
        """Return whether the AzureDLFile was opened for writing"""
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...

class AzureDLPath(Incomplete):
    """
    Subclass of native object-oriented filesystem path.

    This is used as a convenience class for reducing boilerplate and
    eliminating differences between system-dependent paths.

    We subclass the system's concrete pathlib class due to this issue:

    http://stackoverflow.com/questions/29850801/subclass-pathlib-path-fails

    Parameters
    ----------
    path: AzureDLPath or string
        location of file or directory

    Examples
    --------
    >>> p1 = AzureDLPath('/Users/foo')  # doctest: +SKIP
    >>> p2 = AzureDLPath(p1.name)  # doctest: +SKIP
    """
    def __contains__(self, s) -> bool:
        """ Return whether string is contained in path. """
    @property
    def globless_prefix(self):
        """ Return shortest path prefix without glob quantifiers. """
    def startswith(self, prefix, *args, **kwargs):
        """ Return whether string starts with the prefix.

        This is equivalent to `str.startswith`.
        """
    def trim(self):
        """ Return path without anchor (concatenation of drive and root). """
