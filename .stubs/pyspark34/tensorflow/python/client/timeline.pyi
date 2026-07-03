from _typeshed import Incomplete
from tensorflow.python.platform import build_info as build_info
from typing import NamedTuple

class AllocationMaximum(NamedTuple('AllocationMaximum', [('timestamp', Incomplete), ('num_bytes', Incomplete), ('tensors', Incomplete)])):
    """Stores the maximum allocation for a given allocator within the timelne.

  Parameters:
    timestamp: `tensorflow::Env::NowMicros()` when this maximum was reached.
    num_bytes: the total memory used at this time.
    tensors: the set of tensors allocated at this time.
  """
class StepStatsAnalysis(NamedTuple('StepStatsAnalysis', [('chrome_trace', Incomplete), ('allocator_maximums', Incomplete)])):
    """Stores the step stats analysis output.

  Parameters:
    chrome_trace: A dict containing the chrome trace analysis.
    allocator_maximums: A dict mapping allocator names to AllocationMaximum.
  """

class _ChromeTraceFormatter:
    """A helper class for generating traces in Chrome Trace Format."""
    def __init__(self, show_memory: bool = False) -> None:
        """Constructs a new Chrome Trace formatter."""
    def emit_pid(self, name, pid) -> None:
        """Adds a process metadata event to the trace.

    Args:
      name:  The process name as a string.
      pid:  Identifier of the process as an integer.
    """
    def emit_tid(self, name, pid, tid) -> None:
        """Adds a thread metadata event to the trace.

    Args:
      name:  The thread name as a string.
      pid:  Identifier of the process as an integer.
      tid:  Identifier of the thread as an integer.
    """
    def emit_region(self, timestamp, duration, pid, tid, category, name, args) -> None:
        """Adds a region event to the trace.

    Args:
      timestamp:  The start timestamp of this region as a long integer.
      duration:  The duration of this region as a long integer.
      pid:  Identifier of the process generating this event as an integer.
      tid:  Identifier of the thread generating this event as an integer.
      category: The event category as a string.
      name:  The event name as a string.
      args:  A JSON-compatible dictionary of event arguments.
    """
    def emit_obj_create(self, category, name, timestamp, pid, tid, object_id) -> None:
        """Adds an object creation event to the trace.

    Args:
      category: The event category as a string.
      name:  The event name as a string.
      timestamp:  The timestamp of this event as a long integer.
      pid:  Identifier of the process generating this event as an integer.
      tid:  Identifier of the thread generating this event as an integer.
      object_id: Identifier of the object as an integer.
    """
    def emit_obj_delete(self, category, name, timestamp, pid, tid, object_id) -> None:
        """Adds an object deletion event to the trace.

    Args:
      category: The event category as a string.
      name:  The event name as a string.
      timestamp:  The timestamp of this event as a long integer.
      pid:  Identifier of the process generating this event as an integer.
      tid:  Identifier of the thread generating this event as an integer.
      object_id: Identifier of the object as an integer.
    """
    def emit_obj_snapshot(self, category, name, timestamp, pid, tid, object_id, snapshot) -> None:
        """Adds an object snapshot event to the trace.

    Args:
      category: The event category as a string.
      name:  The event name as a string.
      timestamp:  The timestamp of this event as a long integer.
      pid:  Identifier of the process generating this event as an integer.
      tid:  Identifier of the thread generating this event as an integer.
      object_id: Identifier of the object as an integer.
      snapshot:  A JSON-compatible representation of the object.
    """
    def emit_flow_start(self, name, timestamp, pid, tid, flow_id) -> None:
        """Adds a flow start event to the trace.

    When matched with a flow end event (with the same 'flow_id') this will
    cause the trace viewer to draw an arrow between the start and end events.

    Args:
      name:  The event name as a string.
      timestamp:  The timestamp of this event as a long integer.
      pid:  Identifier of the process generating this event as an integer.
      tid:  Identifier of the thread generating this event as an integer.
      flow_id: Identifier of the flow as an integer.
    """
    def emit_flow_end(self, name, timestamp, pid, tid, flow_id) -> None:
        """Adds a flow end event to the trace.

    When matched with a flow start event (with the same 'flow_id') this will
    cause the trace viewer to draw an arrow between the start and end events.

    Args:
      name:  The event name as a string.
      timestamp:  The timestamp of this event as a long integer.
      pid:  Identifier of the process generating this event as an integer.
      tid:  Identifier of the thread generating this event as an integer.
      flow_id: Identifier of the flow as an integer.
    """
    def emit_counter(self, category, name, pid, timestamp, counter, value) -> None:
        """Emits a record for a single counter.

    Args:
      category: The event category as a string.
      name:  The event name as a string.
      pid:  Identifier of the process generating this event as an integer.
      timestamp:  The timestamp of this event as a long integer.
      counter: Name of the counter as a string.
      value:  Value of the counter as an integer.
    """
    def emit_counters(self, category, name, pid, timestamp, counters) -> None:
        """Emits a counter record for the dictionary 'counters'.

    Args:
      category: The event category as a string.
      name:  The event name as a string.
      pid:  Identifier of the process generating this event as an integer.
      timestamp:  The timestamp of this event as a long integer.
      counters: Dictionary of counter values.
    """
    def format_to_string(self, pretty: bool = False):
        """Formats the chrome trace to a string.

    Args:
      pretty: (Optional.)  If True, produce human-readable JSON output.

    Returns:
      A JSON-formatted string in Chrome Trace format.
    """

class _TensorTracker:
    """An internal class to track the lifetime of a Tensor."""
    def __init__(self, name, object_id, timestamp, pid, allocator, num_bytes) -> None:
        """Creates an object to track tensor references.

    This class is not thread safe and is intended only for internal use by
    the 'Timeline' class in this file.

    Args:
      name:  The name of the Tensor as a string.
      object_id:  Chrome Trace object identifier assigned for this Tensor.
      timestamp:  The creation timestamp of this event as a long integer.
      pid:  Process identifier of the associated device, as an integer.
      allocator:  Name of the allocator used to create the Tensor.
      num_bytes:  Number of bytes allocated (long integer).

    Returns:
      A 'TensorTracker' object.
    """
    @property
    def name(self):
        """Name of this tensor."""
    @property
    def pid(self):
        """ID of the process which created this tensor (an integer)."""
    @property
    def create_time(self):
        """Timestamp when this tensor was created (long integer)."""
    @property
    def object_id(self):
        """Returns the object identifier of this tensor (integer)."""
    @property
    def num_bytes(self):
        """Size of this tensor in bytes (long integer)."""
    @property
    def allocator(self):
        """Name of the allocator used to create this tensor (string)."""
    @property
    def last_unref(self):
        """Last unreference timestamp of this tensor (long integer)."""
    def add_ref(self, timestamp) -> None:
        """Adds a reference to this tensor with the specified timestamp.

    Args:
      timestamp:  Timestamp of object reference as an integer.
    """
    def add_unref(self, timestamp) -> None:
        """Adds an unref to this tensor with the specified timestamp.

    Args:
      timestamp:  Timestamp of object unreference as an integer.
    """

class Timeline:
    """A class for visualizing execution timelines of TensorFlow steps."""
    def __init__(self, step_stats, graph: Incomplete | None = None) -> None:
        """Constructs a new Timeline.

    A 'Timeline' is used for visualizing the execution of a TensorFlow
    computation.  It shows the timings and concurrency of execution at
    the granularity of TensorFlow Ops.
    This class is not thread safe.

    Args:
      step_stats: The 'StepStats' proto recording execution times.
      graph: (Optional) The 'Graph' that was executed.
    """
    def analyze_step_stats(self, show_dataflow: bool = True, show_memory: bool = True, op_time: str = 'schedule'):
        '''Analyze the step stats and format it into Chrome Trace Format.

    Args:
      show_dataflow: (Optional.) If True, add flow events to the trace
        connecting producers and consumers of tensors.
      show_memory: (Optional.) If True, add object snapshot events to the trace
        showing the sizes and lifetimes of tensors.
      op_time: (Optional.) How the execution time of op is shown in timeline.
        Possible values are "schedule", "gpu" and "all". "schedule" will show op
        from the time it is scheduled to the end of the scheduling. Notice by
        the end of its scheduling its async kernels may not start yet. It is
        shown using the default value from step_stats. "gpu" will show op with
        the execution time of its kernels on GPU. "all" will show op from the
        start of its scheduling to the end of its last kernel.

    Returns:
      A \'StepStatsAnalysis\' object.
    '''
    def generate_chrome_trace_format(self, show_dataflow: bool = True, show_memory: bool = False, op_time: str = 'schedule'):
        '''Produces a trace in Chrome Trace Format.

    Args:
      show_dataflow: (Optional.) If True, add flow events to the trace
        connecting producers and consumers of tensors.
      show_memory: (Optional.) If True, add object snapshot events to the trace
        showing the sizes and lifetimes of tensors.
      op_time: (Optional.) How the execution time of op is shown in timeline.
        Possible values are "schedule", "gpu" and "all".
        "schedule" will show op from the time it is scheduled to the end of
          the scheduling.
          Notice by the end of its scheduling its async kernels may not start
          yet. It is shown using the default value from step_stats.
        "gpu" will show op with the execution time of its kernels on GPU.
        "all" will show op from the start of its scheduling to the end of
          its last kernel.

    Returns:
      A JSON formatted string in Chrome Trace format.
    '''
