from _typeshed import Incomplete
from fsspec import filesystem as filesystem
from fsspec.spec import AbstractBufferedFile as AbstractBufferedFile, AbstractFileSystem as AbstractFileSystem
from fsspec.utils import infer_storage_options as infer_storage_options

class DaskWorkerFileSystem(AbstractFileSystem):
    """View files accessible to a worker as any other remote file-system

    When instances are run on the worker, uses the real filesystem. When
    run on the client, they call the worker to provide information or data.

    **Warning** this implementation is experimental, and read-only for now.
    """
    target_protocol: Incomplete
    target_options: Incomplete
    worker: Incomplete
    client: Incomplete
    fs: Incomplete
    def __init__(self, target_protocol: Incomplete | None = None, target_options: Incomplete | None = None, fs: Incomplete | None = None, client: Incomplete | None = None, **kwargs) -> None: ...
    def mkdir(self, *args, **kwargs) -> None: ...
    def rm(self, *args, **kwargs) -> None: ...
    def copy(self, *args, **kwargs) -> None: ...
    def mv(self, *args, **kwargs) -> None: ...
    def ls(self, *args, **kwargs): ...
    def fetch_range(self, path, mode, start, end): ...

class DaskFile(AbstractBufferedFile):
    def __init__(self, mode: str = 'rb', **kwargs) -> None: ...
