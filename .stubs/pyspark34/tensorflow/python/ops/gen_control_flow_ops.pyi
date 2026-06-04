from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

def abort(error_msg: str = '', exit_without_error: bool = False, name: Incomplete | None = None):
    '''Raise a exception to abort the process when called.

  If exit_without_error is true, the process will exit normally,
  otherwise it will exit with a SIGABORT signal.

  Returns nothing but an exception.

  Args:
    error_msg: An optional `string`. Defaults to `""`.
      A string which is the message associated with the exception.
    exit_without_error: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

Abort: Incomplete

def abort_eager_fallback(error_msg, exit_without_error, name, ctx): ...
def control_trigger(name: Incomplete | None = None):
    """Does nothing. Serves as a control trigger for scheduling.

  Only useful as a placeholder for control edges.

  Args:
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

ControlTrigger: Incomplete

def control_trigger_eager_fallback(name, ctx): ...
def enter(data, frame_name, is_constant: bool = False, parallel_iterations: int = 10, name: Incomplete | None = None):
    """Creates or finds a child frame, and makes `data` available to the child frame.

  This op is used together with `Exit` to create loops in the graph.
  The unique `frame_name` is used by the `Executor` to identify frames. If
  `is_constant` is true, `output` is a constant in the child frame; otherwise
  it may be changed in the child frame. At most `parallel_iterations` iterations
  are run in parallel in the child frame.

  Args:
    data: A `Tensor`. The tensor to be made available to the child frame.
    frame_name: A `string`. The name of the child frame.
    is_constant: An optional `bool`. Defaults to `False`.
      If true, the output is constant within the child frame.
    parallel_iterations: An optional `int`. Defaults to `10`.
      The number of iterations allowed to run in parallel.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  """

Enter: Incomplete

def enter_eager_fallback(data, frame_name, is_constant, parallel_iterations, name, ctx): ...

Exit: Incomplete

def loop_cond(input, name: Incomplete | None = None):
    '''Forwards the input to the output.

  This operator represents the loop termination condition used by the
  "pivot" switches of a loop.

  Args:
    input: A `Tensor` of type `bool`.
      A boolean scalar, representing the branch predicate of the Switch op.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  '''

LoopCond: Incomplete

def loop_cond_eager_fallback(input, name, ctx): ...

class _MergeOutput(NamedTuple):
    output: Incomplete
    value_index: Incomplete

def merge(inputs, name: Incomplete | None = None):
    """Forwards the value of an available tensor from `inputs` to `output`.

  `Merge` waits for at least one of the tensors in `inputs` to become available.
  It is usually combined with `Switch` to implement branching.

  `Merge` forwards the first tensor to become available to `output`, and sets
  `value_index` to its index in `inputs`.

  Args:
    inputs: A list of at least 1 `Tensor` objects with the same type.
      The input tensors, exactly one of which will become available.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output, value_index).

    output: A `Tensor`. Has the same type as `inputs`.
    value_index: A `Tensor` of type `int32`.
  """

Merge: Incomplete

def merge_eager_fallback(inputs, name, ctx): ...
def next_iteration(data, name: Incomplete | None = None):
    """Makes its input available to the next iteration.

  Args:
    data: A `Tensor`. The tensor to be made available to the next iteration.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  """

NextIteration: Incomplete

def next_iteration_eager_fallback(data, name, ctx): ...
def no_op(name: Incomplete | None = None):
    """Does nothing. Only useful as a placeholder for control edges.

  Args:
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

NoOp: Incomplete

def no_op_eager_fallback(name, ctx): ...
def ref_enter(data, frame_name, is_constant: bool = False, parallel_iterations: int = 10, name: Incomplete | None = None):
    """Creates or finds a child frame, and makes `data` available to the child frame.

  The unique `frame_name` is used by the `Executor` to identify frames. If
  `is_constant` is true, `output` is a constant in the child frame; otherwise
  it may be changed in the child frame. At most `parallel_iterations` iterations
  are run in parallel in the child frame.

  Args:
    data: A mutable `Tensor`.
      The tensor to be made available to the child frame.
    frame_name: A `string`. The name of the child frame.
    is_constant: An optional `bool`. Defaults to `False`.
      If true, the output is constant within the child frame.
    parallel_iterations: An optional `int`. Defaults to `10`.
      The number of iterations allowed to run in parallel.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `data`.
  """

RefEnter: Incomplete

def ref_enter_eager_fallback(data, frame_name, is_constant, parallel_iterations, name, ctx) -> None: ...
def ref_exit(data, name: Incomplete | None = None):
    """Exits the current frame to its parent frame.

  Exit makes its input `data` available to the parent frame.

  Args:
    data: A mutable `Tensor`.
      The tensor to be made available to the parent frame.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `data`.
  """

RefExit: Incomplete

def ref_exit_eager_fallback(data, name, ctx) -> None: ...

class _RefMergeOutput(NamedTuple):
    output: Incomplete
    value_index: Incomplete

def ref_merge(inputs, name: Incomplete | None = None):
    """Forwards the value of an available tensor from `inputs` to `output`.

  `Merge` waits for at least one of the tensors in `inputs` to become available.
  It is usually combined with `Switch` to implement branching.

  `Merge` forwards the first tensor for become available to `output`, and sets
  `value_index` to its index in `inputs`.

  Args:
    inputs: A list of at least 1 mutable `Tensor` objects with the same type.
      The input tensors, exactly one of which will become available.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output, value_index).

    output: A mutable `Tensor`. Has the same type as `inputs`.
    value_index: A `Tensor` of type `int32`.
  """

RefMerge: Incomplete

def ref_merge_eager_fallback(inputs, name, ctx) -> None: ...
def ref_next_iteration(data, name: Incomplete | None = None):
    """Makes its input available to the next iteration.

  Args:
    data: A mutable `Tensor`.
      The tensor to be made available to the next iteration.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `data`.
  """

RefNextIteration: Incomplete

def ref_next_iteration_eager_fallback(data, name, ctx) -> None: ...
def ref_select(index, inputs, name: Incomplete | None = None):
    """Forwards the `index`th element of `inputs` to `output`.

  Args:
    index: A `Tensor` of type `int32`.
      A scalar that determines the input that gets selected.
    inputs: A list of at least 1 mutable `Tensor` objects with the same type.
      A list of ref tensors, one of which will be forwarded to `output`.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `inputs`.
  """

RefSelect: Incomplete

def ref_select_eager_fallback(index, inputs, name, ctx) -> None: ...

class _RefSwitchOutput(NamedTuple):
    output_false: Incomplete
    output_true: Incomplete

def ref_switch(data, pred, name: Incomplete | None = None):
    """Forwards the ref tensor `data` to the output port determined by `pred`.

  If `pred` is true, the `data` input is forwarded to `output_true`. Otherwise,
  the data goes to `output_false`.

  See also `Switch` and `Merge`.

  Args:
    data: A mutable `Tensor`.
      The ref tensor to be forwarded to the appropriate output.
    pred: A `Tensor` of type `bool`.
      A scalar that specifies which output port will receive data.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_false, output_true).

    output_false: A mutable `Tensor`. Has the same type as `data`.
    output_true: A mutable `Tensor`. Has the same type as `data`.
  """

RefSwitch: Incomplete

def ref_switch_eager_fallback(data, pred, name, ctx) -> None: ...

class _SwitchOutput(NamedTuple):
    output_false: Incomplete
    output_true: Incomplete

def switch(data, pred, name: Incomplete | None = None):
    """Forwards `data` to the output port determined by `pred`.

  If `pred` is true, the `data` input is forwarded to `output_true`. Otherwise,
  the data goes to `output_false`.

  See also `RefSwitch` and `Merge`.

  Args:
    data: A `Tensor`. The tensor to be forwarded to the appropriate output.
    pred: A `Tensor` of type `bool`.
      A scalar that specifies which output port will receive data.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_false, output_true).

    output_false: A `Tensor`. Has the same type as `data`.
    output_true: A `Tensor`. Has the same type as `data`.
  """

Switch: Incomplete

def switch_eager_fallback(data, pred, name, ctx): ...
