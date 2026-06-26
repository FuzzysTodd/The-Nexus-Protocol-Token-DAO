import threading
from _typeshed import Incomplete
from tensorflow.core.protobuf import config_pb2 as config_pb2
from tensorflow.core.util import event_pb2 as event_pb2
from tensorflow.python.framework import dtypes as dtypes, errors as errors, ops as ops
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.tpu.ops import tpu_ops as tpu_ops
from tensorflow.python.training import session_run_hook as session_run_hook, training_util as training_util

class CoordinatorResetError(errors.AbortedError):
    """Raised when the monitored session should reset."""
    def __init__(self) -> None: ...

class WorkerHeartbeatManager:
    """Manages the status/heartbeat monitor for a set of workers."""
    def __init__(self, session, devices, heartbeat_ops, request_placeholder) -> None:
        """Construct a new WorkerHeartbeatManager.

    (Prefer using `WorkerHeartbeatManager.from_devices` when possible.)

    Args:
      session: `tf.compat.v1.Session`, session to use for heartbeat operations.
      devices: `list[string]` Set of devices to connect to.
      heartbeat_ops: `list[tf.Operation]` Heartbeat operations.
      request_placeholder: `tf.Placeholder[String]` Placeholder used to specify
        the WorkerHeartbeatRequest protocol buffer.
    """
    @staticmethod
    def from_devices(session, devices):
        """Construct a heartbeat manager for the given devices."""
    def num_workers(self): ...
    def configure(self, message) -> None:
        """Configure heartbeat manager for all devices.

    Args:
      message: `event_pb2.WorkerHeartbeatRequest`
    Returns: `None`
    """
    def ping(self, request: Incomplete | None = None, timeout_in_ms: int = 60000):
        """Ping all workers, returning the parsed status results."""
    def lame_workers(self):
        """Ping all workers, returning manager containing lame workers (or None)."""
    def shutdown(self, wait_time_in_ms: int = 60000, exit_code: int = 0) -> None:
        """Shutdown all workers after `shutdown_timeout_secs`."""

def all_worker_devices(session):
    """Return a list of devices for each worker in the system."""

class WatchdogManager(threading.Thread):
    """Configures worker watchdog timer and handles periodic pings.

  Usage:
    # Ping workers every minute, shutting down workers if they haven't received
    # a ping after 1 hour.
    watchdog_manager = WatchdogManager(
      ping_interval=60, shutdown_timeout=3600
    )

    # Use as a context manager, resetting watchdog on context exit:
    with watchdog_manager:
      session.run(...)

    # Or setup globally; watchdog will remain active until program exit.
    watchdog_manager.configure_and_run()
  """
    ping_interval: Incomplete
    shutdown_timeout: Incomplete
    daemon: bool
    def __init__(self, session, devices: Incomplete | None = None, ping_interval: int = 60, shutdown_timeout=...) -> None:
        """Initialize a watchdog manager.

    Args:
      session: Session connected to worker devices.  A cloned session and graph
        will be created for managing worker pings.
      devices: Set of devices to monitor.  If none, all workers will be
        monitored.
      ping_interval: Time, in seconds, between watchdog pings.
      shutdown_timeout: Time, in seconds, before watchdog timeout.
    """
    def configure_and_run(self) -> None: ...
    def stop(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def run(self) -> None: ...

def start_worker_watchdog(session, devices: Incomplete | None = None, ping_interval: int = 60, shutdown_timeout: int = 3600) -> None:
    """Start global worker watchdog to shutdown workers on coordinator exit."""
def stop_worker_watchdog() -> None:
    """Stop global worker watchdog."""

class GracefulShutdownHook(session_run_hook.SessionRunHook):
    """Session hook that watches for shutdown events.

  If a shutdown is indicated, `saver.save(checkpoint_prefix)` is executed, and a
  SystemShutdown exception is raised to terminate the main session.  If `saver`
  is None the `SAVERS` collection will be read to find a saver.

  `on_shutdown_hooks` is an optional list of functions that should be called
  after checkpointing.  The function is called with (`run_context`,
  `all_workers`, `lame_workers`).

  If `heartbeat_group` is not specified, it will default to all CPU workers
  in the system.
  """
    def __init__(self, checkpoint_prefix, saver: Incomplete | None = None, on_shutdown_hooks: Incomplete | None = None) -> None: ...
    def after_create_session(self, training_session, coord) -> None: ...
    def saver(self): ...
    def after_run(self, run_context, run_values) -> None: ...

class ResetComputation:
    """Hook to reset a TPUEstimator computation loop.

  This hook shuts down all workers and resets the monitored session loop by
  throwing a CoordinatorResetError.
  """
    def __init__(self) -> None: ...
    def __call__(self, run_context, all_workers, lame_workers) -> None: ...

class ShutdownLameWorkers:
    """Shutdown lamed workers.

  Processing will continue normally (typically by waiting for the down
  workers to be restarted).
  """
    def __init__(self) -> None: ...
    def __call__(self, run_context, all_workers, lame_workers) -> None: ...

class ShutdownAllWorkers:
    """Shutdown all workers.

  Processing will continue normally (typically by waiting for the down
  workers to be restarted).
  """
    def __init__(self) -> None: ...
    def __call__(self, run_context, all_workers, lame_workers) -> None: ...
