from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader

distribution_strategy_context: Incomplete

class Tape:
    """Represents a gradient propagation trace."""
    def __init__(self, tape) -> None: ...
    def watched_variables(self): ...

def push_new_tape(persistent: bool = False, watch_accessed_variables: bool = True):
    """Pushes a new tape onto the tape stack."""
def push_tape(tape) -> None:
    """Pushes an existing tape onto the tape stack."""
def watch(tape, tensor) -> None:
    """Marks this tensor to be watched by the given tape."""

class VariableWatcher:
    """A scope that tracks all trainable variable accesses within it.

  This explicitly ignores variables that are not marked as trainable.

  Sample usage:

  var = tf.Variable(0.0)
  with VariableWatcher() as variable_watcher:
    var.assign_add(1.0)

  assert variable_watcher.watched_variables == [var]
  """
    def __init__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def watched_variables(self):
        """Returns a tuple of variables accessed under this scope."""

def watch_variable(tape, variable) -> None:
    """Marks this variable to be watched by the given tape."""
def variable_accessed(variable) -> None:
    """Notifies all tapes in the stack that a variable has been accessed.

  Args:
    variable: variable to be watched.
  """
def variables_accessed(variables) -> None:
    """Notifies all tapes in the stack that variables have been accessed.

  Only trainable variables are marked as accessed.

  Args:
    variables: iterable of variables to mark as accessed.
  """
def pop_tape(tape) -> None:
    """Pops the given tape in the stack."""
def stop_recording() -> Generator[None, None, None]:
    """Stop all gradient recording (backprop and forwardprop)."""
def should_record_backprop(tensors):
    """Returns true if any tape in the stack watches any of these tensors.

  Only takes GradientTapes into account, not forward accumulators.

  Args:
    tensors: Tensors to check, typically inputs to an operation.

  Returns:
    Boolean, whether any tape watches any of `tensors`.
  """
def record_operation(op_type, output_tensors, input_tensors, backward_function, forward_function: Incomplete | None = None) -> None:
    """Records the operation on all tapes in the stack."""
def record_operation_backprop_only(op_type, output_tensors, input_tensors, backward_function) -> None:
    """Records the operation on all backward tapes in the stack."""
def record_operation_forwardprop_only(op_type, output_tensors, input_tensors, backward_function, forwardprop_output_indices) -> None:
    """Records the operation on all forward accumulators in the stack.

  Args:
    op_type: a string for the operation type, used in the backprop code
    output_tensors: a list of Python Tensor objects output by the operation
    input_tensors: a list of input Tensors to the recorded operation
    backward_function: the function to be called to, given the gradients of the
      output tensors, produce the gradients of the input tensors. This function
      is automatically transposed to produce output gradients given input
      gradients.
    forwardprop_output_indices: indicates any output_tensors which contain JVPs.
      Typically these will have come from TFE_Py_PackForwardGradients. May be
      None or an empty sequence if there are no JVP outputs from the operation.
  """
def delete_trace(tensor_id) -> None:
    """Deletes traces for this Tensor from all tapes in the stack."""
def could_possibly_record():
    """Returns True if any tape is active."""
