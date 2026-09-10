from enum import Enum

class _SnapshotState(Enum):
    """
    These are the snapshotting-related states that IterDataPipes can be in.
    `NotStarted` - allows you to restore a snapshot and create an iterator with reset
    `Restored` - cannot restore again, allows you to create an iterator without resetting the DataPipe
    `Iterating` - can restore, will reset if you create a new iterator
    """
    NotStarted: int
    Restored: int
    Iterating: int

def hook_iterator(namespace, profile_name):
    """
    Hook that is applied to all `__iter__` of metaclass `_DataPipeMeta`. This is done for the purpose of
    profiling and checking if an iterator is still valid.
    """
