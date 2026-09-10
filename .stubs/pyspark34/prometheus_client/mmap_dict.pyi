from _typeshed import Incomplete
from collections.abc import Generator
from typing import List

class MmapedDict:
    """A dict of doubles, backed by an mmapped file.

    The file starts with a 4 byte int, indicating how much of it is used.
    Then 4 bytes of padding.
    There's then a number of entries, consisting of a 4 byte int which is the
    size of the next field, a utf-8 encoded string key, padding to a 8 byte
    alignment, and then a 8 byte float which is the value.

    Not thread safe.
    """
    def __init__(self, filename, read_mode: bool = False) -> None: ...
    @staticmethod
    def read_all_values_from_file(filename): ...
    def read_all_values(self) -> Generator[Incomplete, None, None]:
        """Yield (key, value). No locking is performed."""
    def read_value(self, key): ...
    def write_value(self, key, value) -> None: ...
    def close(self) -> None: ...

def mmap_key(metric_name: str, name: str, labelnames: List[str], labelvalues: List[str], help_text: str) -> str:
    """Format a key for use in the mmap file."""
