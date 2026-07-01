from _typeshed import Incomplete
from collections.abc import Generator
from tensorboard.backend.event_processing import io_wrapper as io_wrapper
from tensorboard.compat import tf as tf
from tensorboard.util import io_util as io_util, tb_logging as tb_logging

logger: Incomplete

class DirectoryWatcher:
    """A DirectoryWatcher wraps a loader to load from a sequence of paths.

    A loader reads a path and produces some kind of values as an iterator. A
    DirectoryWatcher takes a directory, a factory for loaders, and optionally a
    path filter and watches all the paths inside that directory.

    This class is only valid under the assumption that only one path will be
    written to by the data source at a time and that once the source stops writing
    to a path, it will start writing to a new path that's lexicographically
    greater and never come back. It uses some heuristics to check whether this is
    true based on tracking changes to the files' sizes, but the check can have
    false negatives. However, it should have no false positives.
    """
    def __init__(self, directory, loader_factory, path_filter=...) -> None:
        """Constructs a new DirectoryWatcher.

        Args:
          directory: The directory to load files from.
          loader_factory: A factory for creating loaders. The factory should take a
            path and return an object that has a Load method returning an
            iterator that will yield all events that have not been yielded yet.
          path_filter: If specified, only paths matching this filter are loaded.

        Raises:
          ValueError: If path_provider or loader_factory are None.
        """
    def Load(self) -> Generator[Incomplete, None, None]:
        """Loads new values.

        The watcher will load from one path at a time; as soon as that path stops
        yielding events, it will move on to the next path. We assume that old paths
        are never modified after a newer path has been written. As a result, Load()
        can be called multiple times in a row without losing events that have not
        been yielded yet. In other words, we guarantee that every event will be
        yielded exactly once.

        Yields:
          All values that have not been yielded yet.

        Raises:
          DirectoryDeletedError: If the directory has been permanently deleted
            (as opposed to being temporarily unavailable).
        """
    def OutOfOrderWritesDetected(self):
        """Returns whether any out-of-order writes have been detected.

        Out-of-order writes are only checked as part of the Load() iterator. Once an
        out-of-order write is detected, this function will always return true.

        Note that out-of-order write detection is not performed on GCS paths, so
        this function will always return false.

        Returns:
          Whether any out-of-order write has ever been detected by this watcher.
        """

class DirectoryDeletedError(Exception):
    """Thrown by Load() when the directory is *permanently* gone.

    We distinguish this from temporary errors so that other code can
    decide to drop all of our data only when a directory has been
    intentionally deleted, as opposed to due to transient filesystem
    errors.
    """
