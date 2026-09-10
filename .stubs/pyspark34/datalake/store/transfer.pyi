from .exceptions import DatalakeIncompleteTransferException as DatalakeIncompleteTransferException
from _typeshed import Incomplete
from typing import NamedTuple

logger: Incomplete

class StateManager:
    """
    Manages state for any hashable object.

    When tracking multiple files and their chunks, each file/chunk can be in
    any valid state for that particular type.

    At the simplest level, we need to set and retrieve an object's current
    state, while only allowing valid states to be used. In addition, we also
    need to give statistics about a group of objects (are all objects in one
    state? how many objects are in each available state?).

    Parameters
    ----------
    states: list of valid states
        Managed objects can only use these defined states.

    Examples
    --------
    >>> StateManager('draft', 'review', 'complete')  # doctest: +SKIP
    <StateManager: draft=0 review=0 complete=0>
    >>> mgr = StateManager('off', 'on')
    >>> mgr['foo'] = 'on'
    >>> mgr['bar'] = 'off'
    >>> mgr['quux'] = 'on'
    >>> mgr  # doctest: +SKIP
    <StateManager: off=1 on=2>
    >>> mgr.contains_all('on')
    False
    >>> mgr['bar'] = 'on'
    >>> mgr.contains_all('on')
    True
    >>> mgr.contains_none('off')
    True

    Internal class used by `ADLTransferClient`.
    """
    def __init__(self, *states) -> None: ...
    @property
    def states(self): ...
    @property
    def objects(self): ...
    def __iter__(self): ...
    def __getitem__(self, obj): ...
    def __setitem__(self, obj, state) -> None: ...
    def contains_all(self, state):
        """ Return whether all managed objects are in the given state """
    def contains_none(self, *states):
        """ Return whether no managed objects are in the given states """

class File(NamedTuple):
    src: Incomplete
    dst: Incomplete
    state: Incomplete
    length: Incomplete
    chunks: Incomplete
    exception: Incomplete

class Chunk(NamedTuple):
    name: Incomplete
    state: Incomplete
    offset: Incomplete
    expected: Incomplete
    actual: Incomplete
    exception: Incomplete

class ADLTransferClient:
    """
    Client for transferring data from/to Azure DataLake Store

    This is intended as the underlying class for `ADLDownloader` and
    `ADLUploader`. If necessary, it can be used directly for additional
    control.

    Parameters
    ----------
    adlfs: ADL filesystem instance
    name: str
        Unique ID used for persistence.
    transfer: callable
        Function or callable object invoked when transferring chunks. See
        ``Function Signatures``.
    merge: callable [None]
        Function or callable object invoked when merging chunks. For each file
        containing only one chunk, no merge function will be called, even if
        provided. If None, then merging is skipped. See
        ``Function Signatures``.
    nthreads: int [None]
        Number of threads to use (minimum is 1). If None, uses the number of
        cores.
    chunksize: int [2**28]
        Number of bytes for a chunk. Large files are split into chunks. Files
        smaller than this number will always be transferred in a single thread.
    buffersize: int [2**25]
        Number of bytes for internal buffer. This block cannot be bigger than
        a chunk and cannot be smaller than a block.
    blocksize: int [2**25]
        Number of bytes for a block. Within each chunk, we write a smaller
        block for each API call. This block cannot be bigger than a chunk.
    chunked: bool [True]
        If set, each transferred chunk is stored in a separate file until
        chunks are gathered into a single file. Otherwise, each chunk will be
        written into the same destination file.
    unique_temporary: bool [True]
        If set, transferred chunks are written into a unique temporary
        directory.
    persist_path: str [None]
        Path used for persisting a client's state. If None, then `save()`
        and `load()` will be empty operations.
    delimiter: byte(s) or None
        If set, will transfer blocks using delimiters, as well as split
        files for transferring on that delimiter.
    parent: ADLDownloader, ADLUploader or None
        In typical usage, the transfer client is created in the context of an
        upload or download, which can be persisted between sessions.        
    progress_callback: callable [None]
        Callback for progress with signature function(current, total) where
        current is the number of bytes transferred so far, and total is the
        size of the blob, or None if the total size is unknown.
    timeout: int (0)
        Default value 0 means infinite timeout. Otherwise time in seconds before the
        process will stop and raise an exception if  transfer is still in progress

    Temporary Files
    ---------------

    When a merge step is available, the client will write chunks to temporary
    files before merging. The exact temporary file looks like this in
    pseudo-BNF:

    >>> # {dirname}/{basename}.segments[.{unique_str}]/{basename}_{offset}

    Function Signatures
    -------------------

    To perform the actual work needed by the client, the user must pass in two
    callables, `transfer` and `merge`. If merge is not provided, then the
    merge step will be skipped.

    The `transfer` callable has the function signature,
    `fn(adlfs, src, dst, offset, size, buffersize, blocksize, shutdown_event)`.
    `adlfs` is the ADL filesystem instance. `src` and `dst` refer to the source
    and destination of the respective file transfer. `offset` is the location
    in `src` to read `size` bytes from. `buffersize` is the number of bytes
    used for internal buffering before transfer. `blocksize` is the number of
    bytes in a chunk to write at one time. The callable should return an
    integer representing the number of bytes written.

    The `merge` callable has the function signature,
    `fn(adlfs, outfile, files, shutdown_event)`. `adlfs` is the ADL filesystem
    instance. `outfile` is the result of merging `files`.

    For both transfer callables, `shutdown_event` is optional. In particular,
    `shutdown_event` is a `threading.Event` that is passed to the callable.
    The event will be set when a shutdown is requested. It is good practice
    to listen for this.

    Internal State
    --------------

    self._fstates: StateManager
        This captures the current state of each transferred file.
    self._files: dict
        Using a tuple of the file source/destination as the key, this
        dictionary stores the file metadata and all chunk states. The
        dictionary key is `(src, dst)` and the value is
        `dict(length, cstates, exception)`.
    self._chunks: dict
        Using a tuple of the chunk name/offset as the key, this dictionary
        stores the chunk metadata and has a reference to the chunk's parent
        file. The dictionary key is `(name, offset)` and the value is
        `dict(parent=(src, dst), expected, actual, exception)`.
    self._ffutures: dict
        Using a Future object as the key, this dictionary provides a reverse
        lookup for the file associated with the given future. The returned
        value is the file's primary key, `(src, dst)`.
    self._cfutures: dict
        Using a Future object as the key, this dictionary provides a reverse
        lookup for the chunk associated with the given future. The returned
        value is the chunk's primary key, `(name, offset)`.

    See Also
    --------
    azure.datalake.store.multithread.ADLDownloader
    azure.datalake.store.multithread.ADLUploader
    """
    verbose: Incomplete
    def __init__(self, adlfs, transfer, merge: Incomplete | None = None, nthreads: Incomplete | None = None, chunksize=..., blocksize=..., chunked: bool = True, unique_temporary: bool = True, delimiter: Incomplete | None = None, parent: Incomplete | None = None, verbose: bool = False, buffersize=..., progress_callback: Incomplete | None = None, timeout: int = 0) -> None: ...
    def submit(self, src, dst, length) -> None:
        """
        Split a given file into chunks.

        All submitted files/chunks start in the `pending` state until `run()`
        is called.
        """
    @property
    def active(self):
        """ Return whether the transfer is active """
    @property
    def successful(self):
        """
        Return whether the transfer completed successfully.

        It will raise AssertionError if the transfer is active.
        """
    @property
    def progress(self):
        """ Return a summary of all transferred file/chunks """
    @property
    def status(self): ...
    def run(self, nthreads: Incomplete | None = None, monitor: bool = True, before_start: Incomplete | None = None) -> None: ...
    def shutdown(self) -> None:
        """
        Shutdown task threads in an orderly fashion.

        Within the context of this method, we disable Ctrl+C keystroke events
        until all threads have exited. We re-enable Ctrl+C keystroke events
        before leaving.
        """
    def monitor(self, poll: float = 0.1, timeout: int = 0) -> None:
        """ Wait for download to happen """
    def save(self, keep: bool = True) -> None: ...
