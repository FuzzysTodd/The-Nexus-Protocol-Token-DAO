from _typeshed import Incomplete
from fsspec import __version__ as __version__
from fsspec.core import url_to_fs as url_to_fs
from fuse import Operations

logger: Incomplete

class FUSEr(Operations):
    fs: Incomplete
    cache: Incomplete
    root: Incomplete
    counter: int
    def __init__(self, fs, path, ready_file: bool = False) -> None: ...
    def getattr(self, path, fh: Incomplete | None = None): ...
    def readdir(self, path, fh): ...
    def mkdir(self, path, mode): ...
    def rmdir(self, path): ...
    def read(self, path, size, offset, fh): ...
    def write(self, path, data, offset, fh): ...
    def create(self, path, flags, fi: Incomplete | None = None): ...
    def open(self, path, flags): ...
    def truncate(self, path, length, fh: Incomplete | None = None) -> None: ...
    def unlink(self, path) -> None: ...
    def release(self, path, fh): ...
    def chmod(self, path, mode): ...

def run(fs, path, mount_point, foreground: bool = True, threads: bool = False, ready_file: bool = False, ops_class=...):
    '''Mount stuff in a local directory

    This uses fusepy to make it appear as if a given path on an fsspec
    instance is in fact resident within the local file-system.

    This requires that fusepy by installed, and that FUSE be available on
    the system (typically requiring a package to be installed with
    apt, yum, brew, etc.).

    Parameters
    ----------
    fs: file-system instance
        From one of the compatible implementations
    path: str
        Location on that file-system to regard as the root directory to
        mount. Note that you typically should include the terminating "/"
        character.
    mount_point: str
        An empty directory on the local file-system where the contents of
        the remote path will appear.
    foreground: bool
        Whether or not calling this function will block. Operation will
        typically be more stable if True.
    threads: bool
        Whether or not to create threads when responding to file operations
        within the mounter directory. Operation will typically be more
        stable if False.
    ready_file: bool
        Whether the FUSE process is ready. The ``.fuse_ready`` file will
        exist in the ``mount_point`` directory if True. Debugging purpose.
    ops_class: FUSEr or Subclass of FUSEr
        To override the default behavior of FUSEr. For Example, logging
        to file.

    '''
def main(args):
    """Mount filesystem from chained URL to MOUNT_POINT.

    Examples:

    python3 -m fsspec.fuse memory /usr/share /tmp/mem

    python3 -m fsspec.fuse local /tmp/source /tmp/local \\\n            -l /tmp/fsspecfuse.log

    You can also mount chained-URLs and use special settings:

    python3 -m fsspec.fuse 'filecache::zip::file://data.zip' \\\n            / /tmp/zip \\\n            -o 'filecache-cache_storage=/tmp/simplecache'

    You can specify the type of the setting by using `[int]` or `[bool]`,
    (`true`, `yes`, `1` represents the Boolean value `True`):

    python3 -m fsspec.fuse 'simplecache::ftp://ftp1.at.proftpd.org' \\\n            /historic/packages/RPMS /tmp/ftp \\\n            -o 'simplecache-cache_storage=/tmp/simplecache' \\\n            -o 'simplecache-check_files=false[bool]' \\\n            -o 'ftp-listings_expiry_time=60[int]' \\\n            -o 'ftp-username=anonymous' \\\n            -o 'ftp-password=xieyanbo'
    """
