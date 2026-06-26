import http.server
from _typeshed import Incomplete
from collections.abc import Generator
from jax._src import traceback_util as traceback_util, xla_bridge as xla_bridge
from jax._src.lib import xla_client as xla_client
from typing import Callable

logger: Incomplete

def start_server(port: int) -> xla_client.profiler.ProfilerServer:
    '''Starts the profiler server on port `port`.

  Using the "TensorFlow profiler" feature in `TensorBoard
  <https://www.tensorflow.org/tensorboard>`_ 2.2 or newer, you can
  connect to the profiler server and sample execution traces that show CPU,
  GPU, and/or TPU device activity.
  '''
def stop_server() -> None:
    """Stops the running profiler server."""

class _ProfileState:
    profile_session: Incomplete
    log_dir: Incomplete
    create_perfetto_link: bool
    create_perfetto_trace: bool
    lock: Incomplete
    def __init__(self) -> None: ...

def start_trace(log_dir, create_perfetto_link: bool = False, create_perfetto_trace: bool = False) -> None:
    """Starts a profiler trace.

  The trace will capture CPU, GPU, and/or TPU activity, including Python
  functions and JAX on-device operations. Use :func:`stop_trace` to end the trace
  and save the results to ``log_dir``.

  The resulting trace can be viewed with TensorBoard. Note that TensorBoard
  doesn't need to be running when collecting the trace.

  Only once trace may be collected a time. A RuntimeError will be raised if
  :func:`start_trace` is called while another trace is running.

  Args:
    log_dir: The directory to save the profiler trace to (usually the
      TensorBoard log directory).
    create_perfetto_link: A boolean which, if true, creates and prints link to
      the Perfetto trace viewer UI (https://ui.perfetto.dev). The program will
      block until the link is opened and Perfetto loads the trace.
    create_perfetto_trace: A boolean which, if true, additionally dumps a
      ``perfetto_trace.json.gz`` file that is compatible for upload with the
      Perfetto trace viewer UI (https://ui.perfetto.dev). The file will also be
      generated if ``create_perfetto_link`` is true. This could be useful if you
      want to generate a Perfetto-compatible trace without blocking the
      process.
  """

class _PerfettoServer(http.server.SimpleHTTPRequestHandler):
    """Handles requests from `ui.perfetto.dev` for the `trace.json`"""
    def end_headers(self): ...
    def do_GET(self): ...
    def do_POST(self) -> None: ...

def stop_trace() -> None:
    """Stops the currently-running profiler trace.

  The trace will be saved to the ``log_dir`` passed to the corresponding
  :func:`start_trace` call. Raises a RuntimeError if a trace hasn't been started.
  """
def trace(log_dir, create_perfetto_link: bool = False, create_perfetto_trace: bool = False) -> Generator[None, None, None]:
    """Context manager to take a profiler trace.

  The trace will capture CPU, GPU, and/or TPU activity, including Python
  functions and JAX on-device operations.

  The resulting trace can be viewed with TensorBoard. Note that TensorBoard
  doesn't need to be running when collecting the trace.

  Only once trace may be collected a time. A RuntimeError will be raised if a
  trace is started while another trace is running.

  Args:
    log_dir: The directory to save the profiler trace to (usually the
      TensorBoard log directory).
    create_perfetto_link: A boolean which, if true, creates and prints link to
      the Perfetto trace viewer UI (https://ui.perfetto.dev). The program will
      block until the link is opened and Perfetto loads the trace.
    create_perfetto_trace: A boolean which, if true, additionally dumps a
      ``perfetto_trace.json.gz`` file that is compatible for upload with the
      Perfetto trace viewer UI (https://ui.perfetto.dev). The file will also be
      generated if ``create_perfetto_link`` is true. This could be useful if you
      want to generate a Perfetto-compatible trace without blocking the
      process.
  """

class TraceAnnotation(xla_client.profiler.TraceMe):
    '''Context manager that generates a trace event in the profiler.

  The trace event spans the duration of the code enclosed by the context.

  For example:

  >>> x = jnp.ones((1000, 1000))
  >>> with jax.profiler.TraceAnnotation("my_label"):
  ...   result = jnp.dot(x, x.T).block_until_ready()

  This will cause a "my_label" event to show up on the trace timeline if the
  event occurs while the process is being traced.
  '''

class StepTraceAnnotation(TraceAnnotation):
    '''Context manager that generates a step trace event in the profiler.

  The step trace event spans the duration of the code enclosed by the context.
  The profiler will provide the performance analysis for each step trace event.

  For example, it can be used to mark training steps and enable the profiler to
  provide the performance analysis per step:

  >>> while global_step < NUM_STEPS:                                           # doctest: +SKIP
  ...   with jax.profiler.StepTraceAnnotation("train", step_num=global_step):  # doctest: +SKIP
  ...     train_step()                                                         # doctest: +SKIP
  ...     global_step += 1                                                     # doctest: +SKIP

  This will cause a "train xx" event to show up on the trace timeline if the
  event occurs while the process is being traced by TensorBoard. In addition,
  if using accelerators, the device trace timeline will also show a "train xx"
  event. Note that "step_num" can be set as a keyword argument to pass the
  global step number to the profiler.

  '''
    def __init__(self, name: str, **kwargs) -> None: ...

def annotate_function(func: Callable, name: str | None = None, **decorator_kwargs):
    '''Decorator that generates a trace event for the execution of a function.

  For example:

  >>> @jax.profiler.annotate_function
  ... def f(x):
  ...   return jnp.dot(x, x.T).block_until_ready()
  >>>
  >>> result = f(jnp.ones((1000, 1000)))

  This will cause an "f" event to show up on the trace timeline if the
  function execution occurs while the process is being traced by TensorBoard.

  Arguments can be passed to the decorator via :py:func:`functools.partial`.

  >>> from functools import partial

  >>> @partial(jax.profiler.annotate_function, name="event_name")
  ... def f(x):
  ...   return jnp.dot(x, x.T).block_until_ready()

  >>> result = f(jnp.ones((1000, 1000)))
  '''
def device_memory_profile(backend: str | None = None) -> bytes:
    """Captures a JAX device memory profile as ``pprof``-format protocol buffer.

  A device memory profile is a snapshot of the state of memory, that describes the JAX
  :class:`~jax.Array` and executable objects present in memory and their
  allocation sites.

  For more information how to use the device memory profiler, see
  :doc:`/device_memory_profiling`.

  The profiling system works by instrumenting JAX on-device allocations,
  capturing a Python stack trace for each allocation. The instrumentation is
  always enabled; :func:`device_memory_profile` provides an API to capture it.

  The output of :func:`device_memory_profile` is a binary protocol buffer that
  can be interpreted and visualized by the `pprof tool
  <https://github.com/google/pprof>`_.

  Args:
    backend: optional; the name of the JAX backend for which the device memory
      profile should be collected.

  Returns:
    A byte string containing a binary `pprof`-format protocol buffer.
  """
def save_device_memory_profile(filename, backend: str | None = None) -> None:
    """Collects a device memory profile and writes it to a file.

  :func:`save_device_memory_profile` is a convenience wrapper around :func:`device_memory_profile`
  that saves its output to a ``filename``. See the
  :func:`device_memory_profile` documentation for more information.

  Args:
    filename: the filename to which the profile should be written.
    backend: optional; the name of the JAX backend for which the device memory
      profile should be collected.
  """
