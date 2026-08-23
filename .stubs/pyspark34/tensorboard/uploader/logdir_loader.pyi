from _typeshed import Incomplete
from tensorboard.backend.event_processing import directory_watcher as directory_watcher, io_wrapper as io_wrapper
from tensorboard.util import tb_logging as tb_logging

logger: Incomplete

class LogdirLoader:
    '''Loader for a root log directory, maintaining multiple DirectoryLoaders.

    This class takes a root log directory and a factory for DirectoryLoaders, and
    maintains one DirectoryLoader per "logdir subdirectory" of the root logdir.

    Note that this class is not thread-safe.
    '''
    def __init__(self, logdir, directory_loader_factory) -> None:
        """Constructs a new LogdirLoader.

        Args:
          logdir: The root log directory to load from.
          directory_loader_factory: A factory for creating DirectoryLoaders. The
            factory should take a path and return a DirectoryLoader.

        Raises:
          ValueError: If logdir or directory_loader_factory are None.
        """
    def synchronize_runs(self) -> None:
        """Finds new runs within `logdir` and makes `DirectoryLoaders` for
        them.

        In addition, any existing `DirectoryLoader` whose run directory
        no longer exists will be deleted.
        """
    def get_run_events(self):
        """Returns tf.Event generators for each run's `DirectoryLoader`.

        Warning: the generators are stateful and consuming them will affect the
        results of any other existing generators for that run; calling code should
        ensure it takes events from only a single generator per run at a time.

        Returns:
          Dictionary containing an entry for each run, mapping the run name to a
          generator yielding tf.Event protobuf objects loaded from that run.
        """
