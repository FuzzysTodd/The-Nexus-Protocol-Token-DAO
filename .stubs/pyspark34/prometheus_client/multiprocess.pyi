from .metrics import Gauge as Gauge
from .metrics_core import Metric as Metric
from .mmap_dict import MmapedDict as MmapedDict
from .samples import Sample as Sample
from .utils import floatToGoString as floatToGoString
from _typeshed import Incomplete

FileNotFoundError = IOError

class MultiProcessCollector:
    """Collector for files for multi-process mode."""
    def __init__(self, registry, path: Incomplete | None = None) -> None: ...
    @staticmethod
    def merge(files, accumulate: bool = True):
        """Merge metrics from given mmap files.

        By default, histograms are accumulated, as per prometheus wire format.
        But if writing the merged data back to mmap files, use
        accumulate=False to avoid compound accumulation.
        """
    def collect(self): ...

def mark_process_dead(pid, path: Incomplete | None = None) -> None:
    """Do bookkeeping for when one process dies in a multi-process setup."""
