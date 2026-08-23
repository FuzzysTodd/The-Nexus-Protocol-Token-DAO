import torch
from .microbatch import Batch
from .skip.layout import SkipLayout
from .skip.tracker import SkipTrackerThroughPotals
from .stream import AbstractStream
from _typeshed import Incomplete
from torch import Tensor, nn
from types import TracebackType
from typing import List, Sequence, Tuple, Type

__all__ = ['Pipeline']

Tensors = Sequence[Tensor]
TensorOrTensors = Tensor | Tensors
ExcInfo = Tuple[Type[BaseException], BaseException, TracebackType]

class Pipeline:
    """The pipeline parallelism for Pipe."""
    partitions: Incomplete
    devices: Incomplete
    copy_streams: Incomplete
    skip_layout: Incomplete
    checkpoint_stop: Incomplete
    def __init__(self, partitions: List[nn.Sequential], devices: List[torch.device], copy_streams: List[List[AbstractStream]], skip_layout: SkipLayout, checkpoint_stop: int) -> None: ...
    def run(self, batches: List[Batch]) -> None:
        """Runs pipeline parallelism.

        It modifies the given batches in place.

        """
    def fence(self, batches: List[Batch], schedule: List[Tuple[int, int]], skip_trackers: List[SkipTrackerThroughPotals]) -> None:
        """Copies micro-batches after computation for the previous
        micro-batches.
        """
    def compute(self, batches: List[Batch], schedule: List[Tuple[int, int]], skip_trackers: List[SkipTrackerThroughPotals]) -> None:
        """Runs tasks with synchronization to copy streams."""
