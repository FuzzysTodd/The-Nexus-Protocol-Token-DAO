import threading
from tensorflow.python.distribute.cluster_resolver import tpu_cluster_resolver as tpu_cluster_resolver
from tensorflow.python.training import session_run_hook as session_run_hook

class CloudTPUPreemptedHook(session_run_hook.SessionRunHook):
    """The SessionRunHook for preemptible Cloud TPUs.

  This is an implementation of SessionRunHook for the pre-emptible Google Cloud
  TPU service. It attempts to close the session if the TPU is preempted, and
  exits the coordinator process if the session cannot be closed.
  """
    def __init__(self, cluster) -> None: ...
    def after_create_session(self, session, coord) -> None: ...
    def end(self, session) -> None: ...

class _TPUPollingThread(threading.Thread):
    """A thread that polls the state of a TPU node.

  When the node transitions into a TERMINAL state (PREEMPTED, TERMINATED)
  that's considered as not recoverable by the underlying infrastructure,
  it attempts to close the session, and exits the entire process if the
  session.close() stucks.
  """
    daemon: bool
    def __init__(self, cluster, session) -> None: ...
    def stop(self) -> None: ...
    def run(self) -> None: ...
