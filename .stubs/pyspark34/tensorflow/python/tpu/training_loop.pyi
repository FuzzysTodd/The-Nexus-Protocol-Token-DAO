from tensorflow.python.compiler.xla import xla as xla
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops
from tensorflow.python.tpu import tensor_tracer as tensor_tracer, tpu_feed as tpu_feed, tpu_function as tpu_function
from tensorflow.python.types import core as core_types
from typing import Any, Callable, Iterable, List, Optional, Union

def while_loop(condition: Callable[..., Any], body: Callable[..., Any], inputs: Optional[List[Any]] = None, infeed_queue: Optional[tpu_feed.InfeedQueue] = None, name: Any = None) -> Any:
    """Builds a training loop for TPUs.

  The set of loop-carried tensors corresponds to `inputs`.  Both
  `condition` and `body` take the current value of the loop-carried
  tensors. 'body' additionally takes a tuple of infeed from
  infeed_queue if infeed_queue is not None. `condition` must return a
  single boolean value that determines whether iteration
  continues. `body` must return an updated list of values for the
  loop-carried tensors.

  Args:
    condition: a Python function that builds the loop condition.
    body: a Python function that builds the loop body.
    inputs: a list of initial values passed into the training loop, or None
      (equivalent to an empty list).
    infeed_queue: if not None, the infeed queue from which to append a tuple of
      arguments as inputs to condition.
    name: (Deprecated) Does nothing.

  Returns:
    The final values of the loop-carried tensors.

  Raises:
    TypeError: if body or condition has the wrong signature.
  """
def repeat(n: int, body: Callable[..., Union[core_types.TensorLike, Iterable]], inputs: Optional[List[core_types.TensorLike]] = None, infeed_queue: Optional[tpu_feed.InfeedQueue] = None, name: Any = None) -> List[core_types.TensorLike]:
    """Builds a training loop that executes a fixed number of iterations.

  The set of loop-carried tensors correspond to `inputs`.
  `body` must be a function that takes and returns the values of the
  loop-carried tensors.

  Args:
    n: the number of loop iterations
    body: a Python function that builds the loop body.
    inputs: a list of initial values passed into the training loop or None
      (equivalent to an empty list).
    infeed_queue: if not None, the infeed queue from which to append a tuple of
      arguments as inputs to condition.
    name: (Deprecated) Does nothing.

  Returns:
    The final values of the loop-carried tensors.
  Raises:
    ValueError: if there is a type error.
  """
