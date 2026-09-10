from tensorflow.python import pywrap_tfe as pywrap_tfe

class Executor:
    """A class for handling eager execution.

  The default behavior for asynchronous execution is to serialize all ops on
  a single thread. Having different `Executor` objects in different threads
  enables executing ops asynchronously in parallel:

  ```python
  def thread_function():
    executor = executor.Executor(enable_async=True):
    context.set_executor(executor)

  a = threading.Thread(target=thread_function)
  a.start()
  b = threading.Thread(target=thread_function)
  b.start()
  ```
  """
    def __init__(self, handle) -> None: ...
    def __del__(self) -> None: ...
    def is_async(self): ...
    def handle(self): ...
    def wait(self) -> None:
        """Waits for ops dispatched in this executor to finish."""
    def clear_error(self) -> None:
        """Clears errors raised in this executor during execution."""

def new_executor(enable_async, enable_streaming_enqueue: bool = True, in_flight_nodes_limit: int = 0): ...
