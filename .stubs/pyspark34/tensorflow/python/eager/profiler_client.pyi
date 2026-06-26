from tensorflow.python.util.deprecation import deprecated as deprecated

def start_tracing(service_addr, logdir, duration_ms, worker_list: str = '', include_dataset_ops: bool = True, num_tracing_attempts: int = 3) -> None:
    """Sends grpc requests to profiler server to perform on-demand profiling.

  This method will block caller thread until receives tracing result.

  Args:
    service_addr: Address of profiler service e.g. localhost:6009.
    logdir: Path of TensorBoard log directory e.g. /tmp/tb_log.
    duration_ms: Duration of tracing or monitoring in ms.
    worker_list: The list of worker TPUs that we are about to profile in the
      current session. (TPU only)
    include_dataset_ops: Set to false to profile longer traces.
    num_tracing_attempts: Automatically retry N times when no trace event is
      collected.

  Raises:
    UnavailableError: If no trace event is collected.
  """
def monitor(service_addr, duration_ms, monitoring_level: int = 1, display_timestamp: bool = False):
    """Sends grpc requests to profiler server to perform on-demand monitoring.

  This method will block caller thread until receives monitoring result.

  Args:
    service_addr: Address of profiler service e.g. localhost:6009.
    duration_ms: Duration of tracing or monitoring in ms.
    monitoring_level: Choose a monitoring level between 1 and 2 to monitor your
      job. Level 2 is more verbose than level 1 and shows more metrics.
    display_timestamp: Set to true to display timestamp in monitoring result.

  Returns:
    A string of monitoring output.
  """
