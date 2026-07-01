from _typeshed import Incomplete
from collections.abc import Generator
from tensorboard import data_compat as data_compat, dataclass_compat as dataclass_compat
from tensorboard.compat import tf as tf
from tensorboard.compat.proto import event_pb2 as event_pb2
from tensorboard.util import platform_util as platform_util, tb_logging as tb_logging

logger: Incomplete

class _PyRecordReaderIterator:
    """Python iterator for TF Records based on PyRecordReader."""
    def __init__(self, py_record_reader_new, file_path) -> None:
        """Constructs a _PyRecordReaderIterator for the given file path.

        Args:
          py_record_reader_new: pywrap_tensorflow.PyRecordReader_New
          file_path: file path of the tfrecord file to read
        """
    def __iter__(self): ...
    def __next__(self): ...
    next = __next__

class RawEventFileLoader:
    """An iterator that yields Event protos as serialized bytestrings."""
    def __init__(self, file_path, detect_file_replacement: bool = False) -> None:
        """Constructs a RawEventFileLoader for the given file path.

        Args:
          file_path: the event file path to read from
          detect_file_replacement: if True, when Load() is called, the loader
              will make a stat() call to check the size of the file. If it sees
              that the file has grown, it will reopen the file entirely (while
              preserving the current offset) before attempting to read from it.
              Otherwise, Load() will simply poll at EOF for new data.
        """
    def Load(self) -> Generator[Incomplete, None, None]:
        """Loads all new events from disk as raw serialized proto bytestrings.

        Calling Load multiple times in a row will not 'drop' events as long as the
        return value is not iterated over.

        Yields:
          All event proto bytestrings in the file that have not been yielded yet.
        """
    def CheckForIncreasedFileSize(self):
        """Stats the file to get its updated size, returning True if it grew.

        If the stat call fails or reports a smaller size than was previously
        seen, then any previously cached size is left unchanged.

        Returns:
            boolean or None: True if the file size increased; False if it was
                the same or decreased; or None if neither case could be detected
                (either because the previous size had not been recorded yet, or
                because the stat call for the current size failed).
        """

class LegacyEventFileLoader(RawEventFileLoader):
    """An iterator that yields parsed Event protos."""
    def Load(self) -> Generator[Incomplete, None, None]:
        """Loads all new events from disk.

        Calling Load multiple times in a row will not 'drop' events as long as the
        return value is not iterated over.

        Yields:
          All events in the file that have not been yielded yet.
        """

class EventFileLoader(LegacyEventFileLoader):
    """An iterator that passes events through read-time compat layers.

    Specifically, this includes `data_compat` and `dataclass_compat`.
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def Load(self) -> Generator[Incomplete, None, None]: ...

class TimestampedEventFileLoader(EventFileLoader):
    """An iterator that yields (UNIX timestamp float, Event proto) pairs."""
    def Load(self) -> Generator[Incomplete, None, None]:
        """Loads all new events and their wall time values from disk.

        Calling Load multiple times in a row will not 'drop' events as long as the
        return value is not iterated over.

        Yields:
          Pairs of (UNIX timestamp float, Event proto) for all events in the file
          that have not been yielded yet.
        """
