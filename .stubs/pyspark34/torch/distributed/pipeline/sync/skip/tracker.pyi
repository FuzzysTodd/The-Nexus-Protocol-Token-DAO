import threading
from ..checkpoint import is_checkpointing as is_checkpointing
from ..dependency import fork as fork, join as join
from ..microbatch import Batch as Batch
from ..stream import AbstractStream as AbstractStream
from .layout import SkipLayout as SkipLayout
from .namespace import Namespace as Namespace
from .portal import Portal as Portal
from _typeshed import Incomplete
from torch import Tensor as Tensor
from typing import Generator

class SkipTracker:
    """Tracks saved skip tensors.

    It will update the given micro-batch in place. This is because when it
    manipulates the underlying skip tensors, the current micro-batch also has
    to be connected with the skip tensors.

    One thread has one skip tracker. Call :func:`current_skip_tracker` to get
    the skip tracker on the current thread.

    """
    tensors: Incomplete
    def __init__(self) -> None: ...
    def save(self, batch: Batch, ns: Namespace, name: str, tensor: Tensor | None) -> None: ...
    def load(self, batch: Batch, ns: Namespace, name: str) -> Tensor | None: ...
    def copy(self, batch: Batch, prev_stream: AbstractStream, next_stream: AbstractStream, ns: Namespace, name: str) -> None: ...

class SkipTrackerThroughPotals(SkipTracker):
    """Tracks saved skip tensors through portals. The skip tensors will be
    hidden in portals so that the autograd engine does not need to track them.

    This tracker is only used when the training or evaluating module is wrapped
    with :class:`torchpipe.Pipe`.

    """
    skip_layout: Incomplete
    portals: Incomplete
    def __init__(self, skip_layout: SkipLayout) -> None: ...
    def save(self, batch: Batch, ns: Namespace, name: str, tensor: Tensor | None) -> None:
        """Saves the stashed skip tensor in a portal. The portal is then
        connected to the given micro-batch with :class:`Join`.
        """
    def load(self, batch: Batch, ns: Namespace, name: str) -> Tensor | None:
        """Loads a skip tensor from the corresponding portal to pop. The given
        micro-batch is connected to the portal with :class:`Fork`.
        """
    def copy(self, batch: Batch, prev_stream: AbstractStream, next_stream: AbstractStream, ns: Namespace, name: str) -> None:
        """Copies the skip tensor in the corresponding portal. The given
        micro-batch and the portal will be tied with :class:`Fork` and
        :class:`Join`.
        """

class ThreadLocal(threading.local):
    skip_tracker: Incomplete
    def __init__(self) -> None: ...

thread_local: Incomplete

def use_skip_tracker(skip_tracker: SkipTracker) -> Generator[None, None, None]:
    """Registers the given skip tracker on the current thread within a
    context::

        with use_skip_tracker(my_skip_tracker):
            ...

    """
def current_skip_tracker() -> SkipTracker:
    """Gets the skip tracker on the current thread."""
