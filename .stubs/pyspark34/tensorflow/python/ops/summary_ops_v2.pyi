import abc
import threading
from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.core.framework import graph_pb2 as graph_pb2, summary_pb2 as summary_pb2
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, smart_cond as smart_cond, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gen_resource_variable_ops as gen_resource_variable_ops, gen_summary_ops as gen_summary_ops, math_ops as math_ops, resource_variable_ops as resource_variable_ops, summary_op_util as summary_op_util
from tensorflow.python.trackable import resource as resource
from tensorflow.python.training import training_util as training_util
from tensorflow.python.util import deprecation as deprecation, tf_contextlib as tf_contextlib
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class _SummaryState(threading.local):
    is_recording: Incomplete
    is_recording_distribution_strategy: bool
    writer: Incomplete
    step: Incomplete
    def __init__(self) -> None: ...

class _SummaryContextManager:
    """Context manager to implement SummaryWriter.as_default()."""
    def __init__(self, writer, step: Incomplete | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *exc): ...

def should_record_summaries():
    """Returns boolean Tensor which is True if summaries will be recorded.

  If no default summary writer is currently registered, this always returns
  False. Otherwise, this reflects the recording condition has been set via
  `tf.summary.record_if()` (except that it may return False for some replicas
  when using `tf.distribute.Strategy`). If no recording condition is active,
  it defaults to True.
  """
def record_if(condition) -> Generator[None, None, None]:
    """Sets summary recording on or off per the provided boolean value.

  The provided value can be a python boolean, a scalar boolean Tensor, or
  or a callable providing such a value; if a callable is passed it will be
  invoked on-demand to determine whether summary writing will occur.  Note that
  when calling record_if() in an eager mode context, if you intend to provide a
  varying condition like `step % 100 == 0`, you must wrap this in a
  callable to avoid immediate eager evaluation of the condition.  In particular,
  using a callable is the only way to have your condition evaluated as part of
  the traced body of an @tf.function that is invoked from within the
  `record_if()` context.

  Args:
    condition: can be True, False, a bool Tensor, or a callable providing such.

  Yields:
    Returns a context manager that sets this value on enter and restores the
    previous value on exit.
  """
def has_default_writer():
    """Returns a boolean indicating whether a default summary writer exists."""
def record_summaries_every_n_global_steps(n, global_step: Incomplete | None = None):
    """Sets the should_record_summaries Tensor to true if global_step % n == 0."""
def always_record_summaries():
    """Sets the should_record_summaries Tensor to always true."""
def never_record_summaries():
    """Sets the should_record_summaries Tensor to always false."""
def get_step():
    """Returns the default summary step for the current thread.

  Returns:
    The step set by `tf.summary.experimental.set_step()` if one has been set,
    otherwise None.
  """
def set_step(step) -> None:
    """Sets the default summary step for the current thread.

  For convenience, this function sets a default value for the `step` parameter
  used in summary-writing functions elsewhere in the API so that it need not
  be explicitly passed in every such invocation. The value can be a constant
  or a variable, and can be retrieved via `tf.summary.experimental.get_step()`.

  Note: when using this with @tf.functions, the step value will be captured at
  the time the function is traced, so changes to the step outside the function
  will not be reflected inside the function unless using a `tf.Variable` step.

  Args:
    step: An `int64`-castable default step value, or None to unset.
  """

class SummaryWriter(metaclass=abc.ABCMeta):
    """Interface representing a stateful summary writer object."""
    def set_as_default(self, step: Incomplete | None = None) -> None:
        """Enables this summary writer for the current thread.

    For convenience, if `step` is not None, this function also sets a default
    value for the `step` parameter used in summary-writing functions elsewhere
    in the API so that it need not be explicitly passed in every such
    invocation. The value can be a constant or a variable.

    Note: when setting `step` in a @tf.function, the step value will be
    captured at the time the function is traced, so changes to the step outside
    the function will not be reflected inside the function unless using
    a `tf.Variable` step.

    Args:
      step: An `int64`-castable default step value, or `None`. When not `None`,
        the current step is modified to the given value. When `None`, the
        current step is not modified.
    """
    def as_default(self, step: Incomplete | None = None):
        """Returns a context manager that enables summary writing.

    For convenience, if `step` is not None, this function also sets a default
    value for the `step` parameter used in summary-writing functions elsewhere
    in the API so that it need not be explicitly passed in every such
    invocation. The value can be a constant or a variable.

    Note: when setting `step` in a @tf.function, the step value will be
    captured at the time the function is traced, so changes to the step outside
    the function will not be reflected inside the function unless using
    a `tf.Variable` step.

    For example, `step` can be used as:

    ```python
    with writer_a.as_default(step=10):
      tf.summary.scalar(tag, value)   # Logged to writer_a with step 10
      with writer_b.as_default(step=20):
        tf.summary.scalar(tag, value) # Logged to writer_b with step 20
      tf.summary.scalar(tag, value)   # Logged to writer_a with step 10
    ```

    Args:
      step: An `int64`-castable default step value, or `None`. When not `None`,
        the current step is captured, replaced by a given one, and the original
        one is restored when the context manager exits. When `None`, the current
        step is not modified (and not restored when the context manager exits).

    Returns:
      The context manager.
    """
    def init(self) -> None:
        """Initializes the summary writer."""
    def flush(self) -> None:
        """Flushes any buffered data."""
    def close(self) -> None:
        """Flushes and closes the summary writer."""

class _ResourceSummaryWriter(SummaryWriter):
    """Implementation of SummaryWriter using a SummaryWriterInterface resource."""
    def __init__(self, create_fn, init_op_fn) -> None: ...
    def set_as_default(self, step: Incomplete | None = None) -> None:
        """See `SummaryWriter.set_as_default`."""
    def as_default(self, step: Incomplete | None = None):
        """See `SummaryWriter.as_default`."""
    def init(self):
        """See `SummaryWriter.init`."""
    def flush(self):
        """See `SummaryWriter.flush`."""
    def close(self):
        """See `SummaryWriter.close`."""

class _MultiMetaclass(Incomplete, Incomplete): ...

class _TrackableResourceSummaryWriter(_ResourceSummaryWriter, resource.TrackableResource, metaclass=_MultiMetaclass):
    """A `_ResourceSummaryWriter` subclass that implements `TrackableResource`."""
    def __init__(self, create_fn, init_op_fn) -> None: ...

class _LegacyResourceSummaryWriter(SummaryWriter):
    """Legacy resource-backed SummaryWriter for tf.contrib.summary."""
    def __init__(self, resource, init_op_fn) -> None: ...
    def init(self):
        """See `SummaryWriter.init`."""
    def flush(self):
        """See `SummaryWriter.flush`."""
    def close(self):
        """See `SummaryWriter.close`."""

class _NoopSummaryWriter(SummaryWriter):
    """A summary writer that does nothing, for create_noop_writer()."""
    def set_as_default(self, step: Incomplete | None = None) -> None: ...
    def as_default(self, step: Incomplete | None = None) -> Generator[None, None, None]: ...
    def init(self) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...

def initialize(graph: Incomplete | None = None, session: Incomplete | None = None) -> None:
    """Initializes summary writing for graph execution mode.

  This operation is a no-op when executing eagerly.

  This helper method provides a higher-level alternative to using
  `tf.contrib.summary.summary_writer_initializer_op` and
  `tf.contrib.summary.graph`.

  Most users will also want to call `tf.compat.v1.train.create_global_step`
  which can happen before or after this function is called.

  Args:
    graph: A `tf.Graph` or `tf.compat.v1.GraphDef` to output to the writer.
      This function will not write the default graph by default. When
      writing to an event log file, the associated step will be zero.
    session: So this method can call `tf.Session.run`. This defaults
      to `tf.compat.v1.get_default_session`.

  Raises:
    RuntimeError: If  the current thread has no default
      `tf.contrib.summary.SummaryWriter`.
    ValueError: If session wasn't passed and no default session.
  """
def create_file_writer_v2(logdir, max_queue: Incomplete | None = None, flush_millis: Incomplete | None = None, filename_suffix: Incomplete | None = None, name: Incomplete | None = None, experimental_trackable: bool = False):
    """Creates a summary file writer for the given log directory.

  Args:
    logdir: a string specifying the directory in which to write an event file.
    max_queue: the largest number of summaries to keep in a queue; will
     flush once the queue gets bigger than this. Defaults to 10.
    flush_millis: the largest interval between flushes. Defaults to 120,000.
    filename_suffix: optional suffix for the event file name. Defaults to `.v2`.
    name: a name for the op that creates the writer.
    experimental_trackable: a boolean that controls whether the returned writer
      will be a `TrackableResource`, which makes it compatible with SavedModel
      when used as a `tf.Module` property.

  Returns:
    A SummaryWriter object.
  """
def create_file_writer(logdir, max_queue: Incomplete | None = None, flush_millis: Incomplete | None = None, filename_suffix: Incomplete | None = None, name: Incomplete | None = None):
    """Creates a summary file writer in the current context under the given name.

  Args:
    logdir: a string, or None. If a string, creates a summary file writer
     which writes to the directory named by the string. If None, returns
     a mock object which acts like a summary writer but does nothing,
     useful to use as a context manager.
    max_queue: the largest number of summaries to keep in a queue; will
     flush once the queue gets bigger than this. Defaults to 10.
    flush_millis: the largest interval between flushes. Defaults to 120,000.
    filename_suffix: optional suffix for the event file name. Defaults to `.v2`.
    name: Shared name for this SummaryWriter resource stored to default
      Graph. Defaults to the provided logdir prefixed with `logdir:`. Note: if a
      summary writer resource with this shared name already exists, the returned
      SummaryWriter wraps that resource and the other arguments have no effect.

  Returns:
    Either a summary writer or an empty object which can be used as a
    summary writer.
  """
def create_noop_writer():
    """Returns a summary writer that does nothing.

  This is useful as a placeholder in code that expects a context manager.
  """
def all_v2_summary_ops():
    """Returns all V2-style summary ops defined in the current default graph.

  This includes ops from TF 2.0 tf.summary and TF 1.x tf.contrib.summary (except
  for `tf.contrib.summary.graph` and `tf.contrib.summary.import_event`), but
  does *not* include TF 1.x tf.summary ops.

  Returns:
    List of summary ops, or None if called under eager execution.
  """
def summary_writer_initializer_op():
    """Graph-mode only. Returns the list of ops to create all summary writers.

  Returns:
    The initializer ops.

  Raises:
    RuntimeError: If in Eager mode.
  """
def summary_scope(name, default_name: str = 'summary', values: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    '''Experimental context manager for use when defining a custom summary op.

  This behaves similarly to `tf.name_scope`, except that it returns a generated
  summary tag in addition to the scope name. The tag is structurally similar to
  the scope name - derived from the user-provided name, prefixed with enclosing
  name scopes if any - but we relax the constraint that it be uniquified, as
  well as the character set limitation (so the user-provided name can contain
  characters not legal for scope names; in the scope name these are removed).

  This makes the summary tag more predictable and consistent for the user.

  For example, to define a new summary op called `my_op`:

  ```python
  def my_op(name, my_value, step):
    with tf.summary.summary_scope(name, "MyOp", [my_value]) as (tag, scope):
      my_value = tf.convert_to_tensor(my_value)
      return tf.summary.write(tag, my_value, step=step)
  ```

  Args:
    name: string name for the summary.
    default_name: Optional; if provided, used as default name of the summary.
    values: Optional; passed as `values` parameter to name_scope.

  Yields:
    A tuple `(tag, scope)` as described above.
  '''
def write(tag, tensor, step: Incomplete | None = None, metadata: Incomplete | None = None, name: Incomplete | None = None):
    """Writes a generic summary to the default SummaryWriter if one exists.

  This exists primarily to support the definition of type-specific summary ops
  like scalar() and image(), and is not intended for direct use unless defining
  a new type-specific summary op.

  Args:
    tag: string tag used to identify the summary (e.g. in TensorBoard), usually
      generated with `tf.summary.summary_scope`
    tensor: the Tensor holding the summary data to write or a callable that
      returns this Tensor. If a callable is passed, it will only be called when
      a default SummaryWriter exists and the recording condition specified by
      `record_if()` is met.
    step: Explicit `int64`-castable monotonic step value for this summary. If
      omitted, this defaults to `tf.summary.experimental.get_step()`, which must
      not be None.
    metadata: Optional SummaryMetadata, as a proto or serialized bytes
    name: Optional string name for this op.

  Returns:
    True on success, or false if no summary was written because no default
    summary writer was available.

  Raises:
    ValueError: if a default writer exists, but no step was provided and
      `tf.summary.experimental.get_step()` is None.
  """
def write_raw_pb(tensor, step: Incomplete | None = None, name: Incomplete | None = None):
    """Writes a summary using raw `tf.compat.v1.Summary` protocol buffers.

  Experimental: this exists to support the usage of V1-style manual summary
  writing (via the construction of a `tf.compat.v1.Summary` protocol buffer)
  with the V2 summary writing API.

  Args:
    tensor: the string Tensor holding one or more serialized `Summary` protobufs
    step: Explicit `int64`-castable monotonic step value for this summary. If
      omitted, this defaults to `tf.summary.experimental.get_step()`, which must
      not be None.
    name: Optional string name for this op.

  Returns:
    True on success, or false if no summary was written because no default
    summary writer was available.

  Raises:
    ValueError: if a default writer exists, but no step was provided and
      `tf.summary.experimental.get_step()` is None.
  """
def summary_writer_function(name, tensor, function, family: Incomplete | None = None):
    """Helper function to write summaries.

  Args:
    name: name of the summary
    tensor: main tensor to form the summary
    function: function taking a tag and a scope which writes the summary
    family: optional, the summary's family

  Returns:
    The result of writing the summary.
  """
def generic(name, tensor, metadata: Incomplete | None = None, family: Incomplete | None = None, step: Incomplete | None = None):
    """Writes a tensor summary if possible."""
def scalar(name, tensor, family: Incomplete | None = None, step: Incomplete | None = None):
    """Writes a scalar summary if possible.

  Unlike `tf.contrib.summary.generic` this op may change the dtype
  depending on the writer, for both practical and efficiency concerns.

  Args:
    name: An arbitrary name for this summary.
    tensor: A `tf.Tensor` Must be one of the following types:
      `float32`, `float64`, `int32`, `int64`, `uint8`, `int16`,
      `int8`, `uint16`, `half`, `uint32`, `uint64`.
    family: Optional, the summary's family.
    step: The `int64` monotonic step variable, which defaults
      to `tf.compat.v1.train.get_global_step`.

  Returns:
    The created `tf.Operation` or a `tf.no_op` if summary writing has
    not been enabled for this context.
  """
def histogram(name, tensor, family: Incomplete | None = None, step: Incomplete | None = None):
    """Writes a histogram summary if possible."""
def image(name, tensor, bad_color: Incomplete | None = None, max_images: int = 3, family: Incomplete | None = None, step: Incomplete | None = None):
    """Writes an image summary if possible."""
def audio(name, tensor, sample_rate, max_outputs, family: Incomplete | None = None, step: Incomplete | None = None):
    """Writes an audio summary if possible."""
def graph_v1(param, step: Incomplete | None = None, name: Incomplete | None = None):
    """Writes a TensorFlow graph to the summary interface.

  The graph summary is, strictly speaking, not a summary. Conditions
  like `tf.summary.should_record_summaries` do not apply. Only
  a single graph can be associated with a particular run. If multiple
  graphs are written, then only the last one will be considered by
  TensorBoard.

  When not using eager execution mode, the user should consider passing
  the `graph` parameter to `tf.compat.v1.summary.initialize` instead of
  calling this function. Otherwise special care needs to be taken when
  using the graph to record the graph.

  Args:
    param: A `tf.Tensor` containing a serialized graph proto. When
      eager execution is enabled, this function will automatically
      coerce `tf.Graph`, `tf.compat.v1.GraphDef`, and string types.
    step: The global step variable. This doesn't have useful semantics
      for graph summaries, but is used anyway, due to the structure of
      event log files. This defaults to the global step.
    name: A name for the operation (optional).

  Returns:
    The created `tf.Operation` or a `tf.no_op` if summary writing has
    not been enabled for this context.

  Raises:
    TypeError: If `param` isn't already a `tf.Tensor` in graph mode.
  """
def graph(graph_data):
    '''Writes a TensorFlow graph summary.

  Write an instance of `tf.Graph` or `tf.compat.v1.GraphDef` as summary only
  in an eager mode. Please prefer to use the trace APIs (`tf.summary.trace_on`,
  `tf.summary.trace_off`, and `tf.summary.trace_export`) when using
  `tf.function` which can automatically collect and record graphs from
  executions.

  Usage Example:
  ```py
  writer = tf.summary.create_file_writer("/tmp/mylogs")

  @tf.function
  def f():
    x = constant_op.constant(2)
    y = constant_op.constant(3)
    return x**y

  with writer.as_default():
    tf.summary.graph(f.get_concrete_function().graph)

  # Another example: in a very rare use case, when you are dealing with a TF v1
  # graph.
  graph = tf.Graph()
  with graph.as_default():
    c = tf.constant(30.0)
  with writer.as_default():
    tf.summary.graph(graph)
  ```

  Args:
    graph_data: The TensorFlow graph to write, as a `tf.Graph` or a
      `tf.compat.v1.GraphDef`.

  Returns:
    True on success, or False if no summary was written because no default
    summary writer was available.

  Raises:
    ValueError: `graph` summary API is invoked in a graph mode.
  '''
def import_event(tensor, name: Incomplete | None = None):
    """Writes a `tf.compat.v1.Event` binary proto.

  This can be used to import existing event logs into a new summary writer sink.
  Please note that this is lower level than the other summary functions and
  will ignore the `tf.summary.should_record_summaries` setting.

  Args:
    tensor: A `tf.Tensor` of type `string` containing a serialized
      `tf.compat.v1.Event` proto.
    name: A name for the operation (optional).

  Returns:
    The created `tf.Operation`.
  """
def flush(writer: Incomplete | None = None, name: Incomplete | None = None):
    """Forces summary writer to send any buffered data to storage.

  This operation blocks until that finishes.

  Args:
    writer: The `tf.summary.SummaryWriter` to flush. If None, the current
      default writer will be used instead; if there is no current writer, this
      returns `tf.no_op`.
    name: Ignored legacy argument for a name for the operation.

  Returns:
    The created `tf.Operation`.
  """
def legacy_raw_flush(writer: Incomplete | None = None, name: Incomplete | None = None):
    """Legacy version of flush() that accepts a raw resource tensor for `writer`.

  Do not use this function in any new code. Not supported and not part of the
  public TF APIs.

  Args:
    writer: The `tf.summary.SummaryWriter` to flush. If None, the current
      default writer will be used instead; if there is no current writer, this
      returns `tf.no_op`. For this legacy version only, also accepts a raw
      resource tensor pointing to the underlying C++ writer resource.
    name: Ignored legacy argument for a name for the operation.

  Returns:
    The created `tf.Operation`.
  """
def eval_dir(model_dir, name: Incomplete | None = None):
    """Construct a logdir for an eval summary writer."""
def create_summary_file_writer(*args, **kwargs):
    """Please use `tf.contrib.summary.create_file_writer`."""
def run_metadata(name, data, step: Incomplete | None = None):
    """Writes entire RunMetadata summary.

  A RunMetadata can contain DeviceStats, partition graphs, and function graphs.
  Please refer to the proto for definition of each field.

  Args:
    name: A name for this summary. The summary tag used for TensorBoard will be
      this name prefixed by any active name scopes.
    data: A RunMetadata proto to write.
    step: Explicit `int64`-castable monotonic step value for this summary. If
      omitted, this defaults to `tf.summary.experimental.get_step()`, which must
      not be None.

  Returns:
    True on success, or false if no summary was written because no default
    summary writer was available.

  Raises:
    ValueError: if a default writer exists, but no step was provided and
      `tf.summary.experimental.get_step()` is None.
  """
def run_metadata_graphs(name, data, step: Incomplete | None = None):
    """Writes graphs from a RunMetadata summary.

  Args:
    name: A name for this summary. The summary tag used for TensorBoard will be
      this name prefixed by any active name scopes.
    data: A RunMetadata proto to write.
    step: Explicit `int64`-castable monotonic step value for this summary. If
      omitted, this defaults to `tf.summary.experimental.get_step()`, which must
      not be None.

  Returns:
    True on success, or false if no summary was written because no default
    summary writer was available.

  Raises:
    ValueError: if a default writer exists, but no step was provided and
      `tf.summary.experimental.get_step()` is None.
  """

class _TraceContext(NamedTuple):
    graph: Incomplete
    profiler: Incomplete

def trace_on(graph: bool = True, profiler: bool = False) -> None:
    """Starts a trace to record computation graphs and profiling information.

  Must be invoked in eager mode.

  When enabled, TensorFlow runtime will collect information that can later be
  exported and consumed by TensorBoard. The trace is activated across the entire
  TensorFlow runtime and affects all threads of execution.

  To stop the trace and export the collected information, use
  `tf.summary.trace_export`. To stop the trace without exporting, use
  `tf.summary.trace_off`.

  Args:
    graph: If True, enables collection of executed graphs. It includes ones from
        tf.function invocation and ones from the legacy graph mode. The default
        is True.
    profiler: If True, enables the advanced profiler. Enabling profiler
        implicitly enables the graph collection. The profiler may incur a high
        memory overhead. The default is False.

  """
def trace_export(name, step: Incomplete | None = None, profiler_outdir: Incomplete | None = None) -> None:
    """Stops and exports the active trace as a Summary and/or profile file.

  Stops the trace and exports all metadata collected during the trace to the
  default SummaryWriter, if one has been set.

  Args:
    name: A name for the summary to be written.
    step: Explicit `int64`-castable monotonic step value for this summary. If
      omitted, this defaults to `tf.summary.experimental.get_step()`, which must
      not be None.
    profiler_outdir: Output directory for profiler. It is required when profiler
      is enabled when trace was started. Otherwise, it is ignored.

  Raises:
    ValueError: if a default writer exists, but no step was provided and
      `tf.summary.experimental.get_step()` is None.
  """
def trace_off() -> None:
    """Stops the current trace and discards any collected information."""
