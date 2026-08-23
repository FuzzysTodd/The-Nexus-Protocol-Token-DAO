import torch
from _typeshed import Incomplete

class Stream(torch._C._CudaStreamBase):
    """Wrapper around a CUDA stream.

    A CUDA stream is a linear sequence of execution that belongs to a specific
    device, independent from other streams.  See :ref:`cuda-semantics` for
    details.

    Args:
        device(torch.device or int, optional): a device on which to allocate
            the stream. If :attr:`device` is ``None`` (default) or a negative
            integer, this will use the current device.
        priority(int, optional): priority of the stream. Can be either
            -1 (high priority) or 0 (low priority). By default, streams have
            priority 0.

    .. note:: Although CUDA versions >= 11 support more than two levels of
        priorities, in PyTorch, we only support two levels of priorities.
    """
    def __new__(cls, device: Incomplete | None = None, priority: int = 0, **kwargs): ...
    def wait_event(self, event) -> None:
        """Makes all future work submitted to the stream wait for an event.

        Args:
            event (torch.cuda.Event): an event to wait for.

        .. note:: This is a wrapper around ``cudaStreamWaitEvent()``: see
           `CUDA Stream documentation`_ for more info.

           This function returns without waiting for :attr:`event`: only future
           operations are affected.

        .. _CUDA Stream documentation:
           https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__STREAM.html
        """
    def wait_stream(self, stream) -> None:
        """Synchronizes with another stream.

        All future work submitted to this stream will wait until all kernels
        submitted to a given stream at the time of call complete.

        Args:
            stream (Stream): a stream to synchronize.

        .. note:: This function returns without waiting for currently enqueued
           kernels in :attr:`stream`: only future operations are affected.
        """
    def record_event(self, event: Incomplete | None = None):
        """Records an event.

        Args:
            event (torch.cuda.Event, optional): event to record. If not given, a new one
                will be allocated.

        Returns:
            Recorded event.
        """
    def query(self):
        """Checks if all the work submitted has been completed.

        Returns:
            A boolean indicating if all kernels in this stream are completed."""
    def synchronize(self) -> None:
        """Wait for all the kernels in this stream to complete.

        .. note:: This is a wrapper around ``cudaStreamSynchronize()``: see
           `CUDA Stream documentation`_ for more info.
        """
    def __eq__(self, o): ...
    def __hash__(self): ...

class ExternalStream(Stream):
    """Wrapper around an externally allocated CUDA stream.

    This class is used to wrap streams allocated in other libraries in order
    to facilitate data exchange and multi-library interactions.

    .. note:: This class doesn't manage the stream life-cycle, it is the user
       responsibility to keep the referenced stream alive while this class is
       being used.

    Args:
        stream_ptr(int): Integer representation of the `cudaStream_t` value.
            allocated externally.
        device(torch.device or int, optional): the device where the stream
            was originally allocated. if device is specified incorrectly,
            subsequent launches using this stream may fail.
    """
    def __new__(cls, stream_ptr, device: Incomplete | None = None, **kwargs): ...

class Event(torch._C._CudaEventBase):
    """Wrapper around a CUDA event.

    CUDA events are synchronization markers that can be used to monitor the
    device's progress, to accurately measure timing, and to synchronize CUDA
    streams.

    The underlying CUDA events are lazily initialized when the event is first
    recorded or exported to another process. After creation, only streams on the
    same device may record the event. However, streams on any device can wait on
    the event.

    Args:
        enable_timing (bool, optional): indicates if the event should measure time
            (default: ``False``)
        blocking (bool, optional): if ``True``, :meth:`wait` will be blocking (default: ``False``)
        interprocess (bool): if ``True``, the event can be shared between processes
            (default: ``False``)

    .. _CUDA Event Documentation:
       https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__EVENT.html
    """
    def __new__(cls, enable_timing: bool = False, blocking: bool = False, interprocess: bool = False): ...
    @classmethod
    def from_ipc_handle(cls, device, handle):
        """Reconstruct an event from an IPC handle on the given device."""
    def record(self, stream: Incomplete | None = None) -> None:
        """Records the event in a given stream.

        Uses ``torch.cuda.current_stream()`` if no stream is specified. The
        stream's device must match the event's device."""
    def wait(self, stream: Incomplete | None = None) -> None:
        """Makes all future work submitted to the given stream wait for this
        event.

        Use ``torch.cuda.current_stream()`` if no stream is specified.

        .. note:: This is a wrapper around ``cudaStreamWaitEvent()``: see
            `CUDA Event documentation`_ for more info.
        """
    def query(self):
        """Checks if all work currently captured by event has completed.

        Returns:
            A boolean indicating if all work currently captured by event has
            completed.
        """
    def elapsed_time(self, end_event):
        """Returns the time elapsed in milliseconds after the event was
        recorded and before the end_event was recorded.
        """
    def synchronize(self) -> None:
        """Waits for the event to complete.

        Waits until the completion of all work currently captured in this event.
        This prevents the CPU thread from proceeding until the event completes.

         .. note:: This is a wrapper around ``cudaEventSynchronize()``: see
            `CUDA Event documentation`_ for more info.
        """
    def ipc_handle(self):
        """Returns an IPC handle of this event. If not recorded yet, the event
        will use the current device. """
