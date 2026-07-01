from .core import AzureDLPath as AzureDLPath
from .exceptions import FileExistsError as FileExistsError, FileNotFoundError as FileNotFoundError
from .retry import ExponentialRetryPolicy as ExponentialRetryPolicy
from .transfer import ADLTransferClient as ADLTransferClient
from .utils import datadir as datadir, read_block as read_block, tokenize as tokenize
from _typeshed import Incomplete

logger: Incomplete

def save(instance, filename, keep: bool = True) -> None: ...
def load(filename): ...

class ADLDownloader:
    """ Download remote file(s) using chunks and threads

    Launches multiple threads for efficient downloading, with `chunksize`
    assigned to each. The remote path can be a single file, a directory
    of files or a glob pattern.

    Parameters
    ----------
    adlfs: ADL filesystem instance
    rpath: str
        remote path/globstring to use to find remote files. Recursive glob
        patterns using `**` are not supported.
    lpath: str
        local path. If downloading a single file, will write to this specific
        file, unless it is an existing directory, in which case a file is
        created within it. If downloading multiple files, this is the root
        directory to write within. Will create directories as required.
    nthreads: int [None]
        Number of threads to use. If None, uses the number of cores.
    chunksize: int [2**28]
        Number of bytes for a chunk. Large files are split into chunks. Files
        smaller than this number will always be transferred in a single thread.
    buffersize: int [2**22]
        Ignored in curret implementation.
        Number of bytes for internal buffer. This block cannot be bigger than
        a chunk and cannot be smaller than a block.
    blocksize: int [2**22]
        Number of bytes for a block. Within each chunk, we write a smaller
        block for each API call. This block cannot be bigger than a chunk.
    client: ADLTransferClient [None]
        Set an instance of ADLTransferClient when finer-grained control over
        transfer parameters is needed. Ignores `nthreads` and `chunksize` set
        by constructor.
    run: bool [True]
        Whether to begin executing immediately.
    overwrite: bool [False]
        Whether to forcibly overwrite existing files/directories. If False and
        local path is a directory, will quit regardless if any files would be
        overwritten or not. If True, only matching filenames are actually
        overwritten.
    progress_callback: callable [None]
        Callback for progress with signature function(current, total) where
        current is the number of bytes transfered so far, and total is the
        size of the blob, or None if the total size is unknown.
    timeout: int (0)
        Default value 0 means infinite timeout. Otherwise time in seconds before the
        process will stop and raise an exception if  transfer is still in progress

    See Also
    --------
    azure.datalake.store.transfer.ADLTransferClient
    """
    client: Incomplete
    rpath: Incomplete
    lpath: Incomplete
    def __init__(self, adlfs, rpath, lpath, nthreads: Incomplete | None = None, chunksize=..., buffersize=..., blocksize=..., client: Incomplete | None = None, run: bool = True, overwrite: bool = False, verbose: bool = False, progress_callback: Incomplete | None = None, timeout: int = 0) -> None: ...
    def save(self, keep: bool = True) -> None:
        """ Persist this download

        Saves a copy of this transfer process in its current state to disk.
        This is done automatically for a running transfer, so that as a chunk
        is completed, this is reflected. Thus, if a transfer is interrupted,
        e.g., by user action, the transfer can be restarted at another time.
        All chunks that were not already completed will be restarted at that
        time.

        See methods ``load`` to retrieved saved transfers and ``run`` to
        resume a stopped transfer.

        Parameters
        ----------
        keep: bool (True)
            If True, transfer will be saved if some chunks remain to be
            completed; the transfer will be sure to be removed otherwise.
        """
    @staticmethod
    def load():
        """ Load list of persisted transfers from disk, for possible resumption.

        Returns
        -------
            A dictionary of download instances. The hashes are auto-
            generated unique. The state of the chunks completed, errored, etc.,
            can be seen in the status attribute. Instances can be resumed with
            ``run()``.
        """
    @staticmethod
    def clear_saved() -> None:
        """ Remove references to all persisted downloads.
        """
    @property
    def hash(self): ...
    def run(self, nthreads: Incomplete | None = None, monitor: bool = True) -> None:
        """ Populate transfer queue and execute downloads

        Parameters
        ----------
        nthreads: int [None]
            Override default nthreads, if given
        monitor: bool [True]
            To watch and wait (block) until completion.
        """
    def active(self):
        """ Return whether the downloader is active """
    def successful(self):
        """
        Return whether the downloader completed successfully.

        It will raise AssertionError if the downloader is active.
        """

def get_chunk(adlfs, src, dst, offset, size, buffersize, blocksize, shutdown_event: Incomplete | None = None, retries: int = 10, delay: float = 0.01, backoff: int = 3):
    """ Download a piece of a remote file and write locally

    Internal function used by `download`.
    """

class ADLUploader:
    """ Upload local file(s) using chunks and threads

    Launches multiple threads for efficient uploading, with `chunksize`
    assigned to each. The path can be a single file, a directory
    of files or a glob pattern.

    Parameters
    ----------
    adlfs: ADL filesystem instance
    rpath: str
        remote path to upload to; if multiple files, this is the dircetory
        root to write within
    lpath: str
        local path. Can be single file, directory (in which case, upload
        recursively) or glob pattern. Recursive glob patterns using `**` are
        not supported.
    nthreads: int [None]
        Number of threads to use. If None, uses the number of cores.
    chunksize: int [2**28]
        Number of bytes for a chunk. Large files are split into chunks. Files
        smaller than this number will always be transferred in a single thread.
    buffersize: int [2**22]
        Number of bytes for internal buffer. This block cannot be bigger than
        a chunk and cannot be smaller than a block.
    blocksize: int [2**22]
        Number of bytes for a block. Within each chunk, we write a smaller
        block for each API call. This block cannot be bigger than a chunk.
    client: ADLTransferClient [None]
        Set an instance of ADLTransferClient when finer-grained control over
        transfer parameters is needed. Ignores `nthreads` and `chunksize`
        set by constructor.
    run: bool [True]
        Whether to begin executing immediately.
    overwrite: bool [False]
        Whether to forcibly overwrite existing files/directories. If False and
        remote path is a directory, will quit regardless if any files would be
        overwritten or not. If True, only matching filenames are actually
        overwritten.
    progress_callback: callable [None]
        Callback for progress with signature function(current, total) where
        current is the number of bytes transfered so far, and total is the
        size of the blob, or None if the total size is unknown.
    timeout: int (0)
        Default value 0 means infinite timeout. Otherwise time in seconds before the
        process will stop and raise an exception if  transfer is still in progress

    See Also
    --------
    azure.datalake.store.transfer.ADLTransferClient
    """
    client: Incomplete
    rpath: Incomplete
    lpath: Incomplete
    def __init__(self, adlfs, rpath, lpath, nthreads: Incomplete | None = None, chunksize=..., buffersize=..., blocksize=..., client: Incomplete | None = None, run: bool = True, overwrite: bool = False, verbose: bool = False, progress_callback: Incomplete | None = None, timeout: int = 0) -> None: ...
    def save(self, keep: bool = True) -> None:
        """ Persist this upload

        Saves a copy of this transfer process in its current state to disk.
        This is done automatically for a running transfer, so that as a chunk
        is completed, this is reflected. Thus, if a transfer is interrupted,
        e.g., by user action, the transfer can be restarted at another time.
        All chunks that were not already completed will be restarted at that
        time.

        See methods ``load`` to retrieved saved transfers and ``run`` to
        resume a stopped transfer.

        Parameters
        ----------
        keep: bool (True)
            If True, transfer will be saved if some chunks remain to be
            completed; the transfer will be sure to be removed otherwise.
        """
    @staticmethod
    def load():
        """ Load list of persisted transfers from disk, for possible resumption.

        Returns
        -------
            A dictionary of upload instances. The hashes are auto
            generated unique. The state of the chunks completed, errored, etc.,
            can be seen in the status attribute. Instances can be resumed with
            ``run()``.
        """
    @staticmethod
    def clear_saved() -> None:
        """ Remove references to all persisted uploads.
        """
    @property
    def hash(self): ...
    def run(self, nthreads: Incomplete | None = None, monitor: bool = True) -> None:
        """ Populate transfer queue and execute downloads

        Parameters
        ----------
        nthreads: int [None]
            Override default nthreads, if given
        monitor: bool [True]
            To watch and wait (block) until completion.
        """
    def active(self):
        """ Return whether the uploader is active """
    def successful(self):
        """
        Return whether the uploader completed successfully.

        It will raise AssertionError if the uploader is active.
        """

def put_chunk(adlfs, src, dst, offset, size, buffersize, blocksize, delimiter: Incomplete | None = None, shutdown_event: Incomplete | None = None):
    """ Upload a piece of a local file

    Internal function used by `upload`.
    """
def merge_chunks(adlfs, outfile, files, shutdown_event: Incomplete | None = None, overwrite: bool = False): ...
