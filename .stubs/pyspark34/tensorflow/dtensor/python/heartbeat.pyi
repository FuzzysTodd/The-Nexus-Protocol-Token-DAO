import threading
from tensorflow.dtensor.python import config as config
from tensorflow.python.framework import constant_op as constant_op, ops as ops
from tensorflow.python.ops.collective_ops import all_reduce as all_reduce

def start(period: int) -> threading.Event:
    """Starts a persistent thread exchanging heartbeats between workers.

  Args:
    period: Heartbeat interval in seconds. Heartbeat timeout is set to the
      larger of `period` - 10 and 2s.

  Returns:
    A threading.Event object. Users can choose to call its set() method to shut
    down the heartbeat service gracefully. This isn't necessary in most cases,
    because the heartbeat service automatically shuts down at successful program
    exit through atexit handlers. But in situations when atexit handlers are not
    invoked, such as when multiprocessing processes exit in tests, users can
    manually request a shutdown.
  """
