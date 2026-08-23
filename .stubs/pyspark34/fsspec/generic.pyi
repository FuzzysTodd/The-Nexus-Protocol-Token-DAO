from .asyn import AsyncFileSystem as AsyncFileSystem, sync_wrapper as sync_wrapper
from .core import filesystem as filesystem, get_filesystem_class as get_filesystem_class, split_protocol as split_protocol, url_to_fs as url_to_fs
from _typeshed import Incomplete

logger: Incomplete

def set_generic_fs(protocol, **storage_options) -> None: ...

default_method: str

def rsync(source, destination, delete_missing: bool = False, source_field: str = 'size', dest_field: str = 'size', update_cond: str = 'different', inst_kwargs: Incomplete | None = None, fs: Incomplete | None = None, **kwargs) -> None:
    '''Sync files between two directory trees

    (experimental)

    Parameters
    ----------
    source: str
        Root of the directory tree to take files from. This must be a directory, but
        do not include any terminating "/" character
    destination: str
        Root path to copy into. The contents of this location should be
        identical to the contents of ``source`` when done. This will be made a
        directory, and the terminal "/" should not be included.
    delete_missing: bool
        If there are paths in the destination that don\'t exist in the
        source and this is True, delete them. Otherwise, leave them alone.
    source_field: str | callable
        If ``update_field`` is "different", this is the key in the info
        of source files to consider for difference. Maybe a function of the
        info dict.
    dest_field: str | callable
        If ``update_field`` is "different", this is the key in the info
        of destination files to consider for difference. May be a function of
        the info dict.
    update_cond: "different"|"always"|"never"
        If "always", every file is copied, regardless of whether it exists in
        the destination. If "never", files that exist in the destination are
        not copied again. If "different" (default), only copy if the info
        fields given by ``source_field`` and ``dest_field`` (usually "size")
        are different. Other comparisons may be added in the future.
    inst_kwargs: dict|None
        If ``fs`` is None, use this set of keyword arguments to make a
        GenericFileSystem instance
    fs: GenericFileSystem|None
        Instance to use if explicitly given. The instance defines how to
        to make downstream file system instances from paths.
    '''

class GenericFileSystem(AsyncFileSystem):
    """Wrapper over all other FS types

    <experimental!>

    This implementation is a single unified interface to be able to run FS operations
    over generic URLs, and dispatch to the specific implementations using the URL
    protocol prefix.

    Note: instances of this FS are always async, even if you never use it with any async
    backend.
    """
    protocol: str
    method: Incomplete
    def __init__(self, default_method: str = 'default', **kwargs) -> None:
        '''

        Parameters
        ----------
        default_method: str (optional)
            Defines how to configure backend FS instances. Options are:
            - "default": instantiate like FSClass(), with no
              extra arguments; this is the default instance of that FS, and can be
              configured via the config system
            - "generic": takes instances from the `_generic_fs` dict in this module,
              which you must populate before use. Keys are by protocol
            - "current": takes the most recently instantiated version of each FS
        '''
    def rsync(self, source, destination, **kwargs) -> None:
        """Sync files between two directory trees

        See `func:rsync` for more details.
        """
    make_many_dirs: Incomplete

async def copy_file_op(fs1, url1, fs2, url2, tempdir: Incomplete | None = None, batch_size: int = 20, on_error: str = 'ignore') -> None: ...
async def maybe_await(cor): ...
