from _typeshed import Incomplete
from collections.abc import Generator
from tensorboard.backend.event_processing import directory_watcher as directory_watcher, io_wrapper as io_wrapper
from tensorboard.compat import tf as tf
from tensorboard.util import tb_logging as tb_logging

logger: Incomplete

class DirectoryLoader:
    '''Loader for an entire directory, maintaining multiple active file
    loaders.

    This class takes a directory, a factory for loaders, and optionally a
    path filter and watches all the paths inside that directory for new data.
    Each file loader created by the factory must read a path and produce an
    iterator of (timestamp, value) pairs.

    Unlike DirectoryWatcher, this class does not assume that only one file
    receives new data at a time; there can be arbitrarily many active files.
    However, any file whose maximum load timestamp fails an "active" predicate
    will be marked as inactive and no longer checked for new data.
    '''
    def __init__(self, directory, loader_factory, path_filter=..., active_filter=...) -> None:
        """Constructs a new MultiFileDirectoryLoader.

        Args:
          directory: The directory to load files from.
          loader_factory: A factory for creating loaders. The factory should take a
            path and return an object that has a Load method returning an iterator
            yielding (unix timestamp as float, value) pairs for any new data
          path_filter: If specified, only paths matching this filter are loaded.
          active_filter: If specified, any loader whose maximum load timestamp does
            not pass this filter will be marked as inactive and no longer read.

        Raises:
          ValueError: If directory or loader_factory are None.
        """
    def Load(self) -> Generator[Incomplete, None, None]:
        """Loads new values from all active files.

        Yields:
          All values that have not been yielded yet.

        Raises:
          DirectoryDeletedError: If the directory has been permanently deleted
            (as opposed to being temporarily unavailable).
        """
