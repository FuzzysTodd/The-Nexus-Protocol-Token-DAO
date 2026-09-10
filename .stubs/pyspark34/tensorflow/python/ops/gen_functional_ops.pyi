from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def case(branch_index, input, Tout, branches, output_shapes=[], name: Incomplete | None = None):
    """An n-way switch statement which calls a single branch function.

      An n-way switch statement, implementing the following:
      ```
      switch (branch_index) {
        case 0:
          output = branches[0](input);
          break;
        case 1:
          output = branches[1](input);
          break;
        ...
        case [[nbranches-1]]:
        default:
          output = branches[nbranches-1](input);
          break;
      }
      ```

  Args:
    branch_index: A `Tensor` of type `int32`.
      The branch selector, an int32 Tensor.
    input: A list of `Tensor` objects.
      A list of input tensors passed to the branch function.
    Tout: A list of `tf.DTypes`. A list of output types.
    branches: A list of functions decorated with @Defun that has length `>= 1`.
            A list of functions each of which takes 'inputs' and returns a list of
            tensors, whose types are the same as what every other branch returns.
    output_shapes: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Tout`.
  """

Case: Incomplete

def case_eager_fallback(branch_index, input, Tout, branches, output_shapes, name, ctx): ...
def device_index(device_names, name: Incomplete | None = None):
    """Return the index of device the op runs.

  Given a list of device names, this operation returns the index of the device
  this op runs. The length of the list is returned in two cases:
  (1) Device does not exist in the given device list.
  (2) It is in XLA compilation.

  Args:
    device_names: A list of `strings`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

DeviceIndex: Incomplete

def device_index_eager_fallback(device_names, name, ctx): ...
def fake_param(dtype, shape, name: Incomplete | None = None):
    """  This op is used as a placeholder in If branch functions. It doesn't provide a
  valid output when run, so must either be removed (e.g. replaced with a
  function input) or guaranteed not to be used (e.g. if mirroring an
  intermediate output needed for the gradient computation of the other branch).

  Args:
    dtype: A `tf.DType`. The type of the output.
    shape: A `tf.TensorShape` or list of `ints`.
          The purported shape of the output. This is only used for shape inference;
          the output will not necessarily have this shape. Can be a partial shape.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """

FakeParam: Incomplete

def fake_param_eager_fallback(dtype, shape, name, ctx): ...

For: Incomplete
If: Incomplete

def partitioned_call(args, Tout, f, config: str = '', config_proto: str = '', executor_type: str = '', name: Incomplete | None = None):
    '''returns `f(inputs)`, where `f`\'s body is placed and partitioned.

  Asynchronously executes a function, potentially across multiple devices but
  within a single process. The kernel places and partitions a given function\'s
  underlying graph, and executes each of the partitioned subgraphs as a function.

  Args:
    args: A list of `Tensor` objects. A list of input tensors.
    Tout: A list of `tf.DTypes`. A list of output types.
    f: A function decorated with @Defun.
            A function that takes \'args\', a list of tensors, and returns \'output\',
            another list of tensors. Input and output types are specified by \'Tin\'
            and \'Tout\'. The function body of f will be placed and partitioned across
            devices, setting this op apart from the regular Call op.
    config: An optional `string`. Defaults to `""`.
    config_proto: An optional `string`. Defaults to `""`.
    executor_type: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Tout`.
  '''

PartitionedCall: Incomplete

def partitioned_call_eager_fallback(args, Tout, f, config, config_proto, executor_type, name, ctx): ...
def remote_call(target, args, Tout, f, name: Incomplete | None = None):
    """Runs function `f` on a remote device indicated by `target`.

  Args:
    target: A `Tensor` of type `string`.
      A fully specified device name where we want to run the function.
    args: A list of `Tensor` objects. A list of arguments for the function.
    Tout: A list of `tf.DTypes` that has length `>= 1`.
      The type list for the return values.
    f: A function decorated with @Defun. The function to run remotely.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Tout`.
  """

RemoteCall: Incomplete

def remote_call_eager_fallback(target, args, Tout, f, name, ctx): ...
def stateful_partitioned_call(args, Tout, f, config: str = '', config_proto: str = '', executor_type: str = '', name: Incomplete | None = None):
    '''returns `f(inputs)`, where `f`\'s body is placed and partitioned.

  Args:
    args: A list of `Tensor` objects. A list of input tensors.
    Tout: A list of `tf.DTypes`. A list of output types.
    f: A function decorated with @Defun.
            A function that takes \'args\', a list of tensors, and returns \'output\',
            another list of tensors. Input and output types are specified by \'Tin\'
            and \'Tout\'. The function body of f will be placed and partitioned across
            devices, setting this op apart from the regular Call op. This op is
            stateful.
    config: An optional `string`. Defaults to `""`.
    config_proto: An optional `string`. Defaults to `""`.
    executor_type: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Tout`.
  '''

StatefulPartitionedCall: Incomplete

def stateful_partitioned_call_eager_fallback(args, Tout, f, config, config_proto, executor_type, name, ctx): ...
def stateless_case(branch_index, input, Tout, branches, output_shapes=[], name: Incomplete | None = None):
    """An n-way switch statement which calls a single branch function.

      An n-way switch statement, implementing the following:
      ```
      switch (branch_index) {
        case 0:
          output = branches[0](input);
          break;
        case 1:
          output = branches[1](input);
          break;
        ...
        case [[nbranches-1]]:
        default:
          output = branches[nbranches-1](input);
          break;
      }
      ```

      This should only be used when the none of branches has stateful ops.

  Args:
    branch_index: A `Tensor` of type `int32`.
      The branch selector, an int32 Tensor.
    input: A list of `Tensor` objects.
      A list of input tensors passed to the branch function.
    Tout: A list of `tf.DTypes`. A list of output types.
    branches: A list of functions decorated with @Defun that has length `>= 1`.
            A list of functions each of which takes 'inputs' and returns a list of
            tensors, whose types are the same as what every other branch returns.
    output_shapes: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Tout`.
  """

StatelessCase: Incomplete

def stateless_case_eager_fallback(branch_index, input, Tout, branches, output_shapes, name, ctx): ...
def stateless_if(cond, input, Tout, then_branch, else_branch, output_shapes=[], name: Incomplete | None = None):
    """output = cond ? then_branch(input) : else_branch(input)

  Args:
    cond: A `Tensor`.
            A Tensor. If the tensor is a scalar of non-boolean type, the
            scalar is converted to a boolean according to the
            following rule: if the scalar is a numerical value, non-zero means
            `True` and zero means False; if the scalar is a string, non-empty
            means `True` and empty means `False`. If the tensor is not a scalar,
            being empty means False and being non-empty means True.

            This should only be used when the if then/else body functions do not
            have stateful ops.
    input: A list of `Tensor` objects. A list of input tensors.
    Tout: A list of `tf.DTypes`. A list of output types.
    then_branch: A function decorated with @Defun.
            A function that takes 'inputs' and returns a list of tensors, whose
            types are the same as what else_branch returns.
    else_branch: A function decorated with @Defun.
          A function that takes 'inputs' and returns a list of tensors, whose
          types are the same as what then_branch returns.
    output_shapes: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Tout`.
  """

StatelessIf: Incomplete

def stateless_if_eager_fallback(cond, input, Tout, then_branch, else_branch, output_shapes, name, ctx): ...
def stateless_while(input, cond, body, output_shapes=[], parallel_iterations: int = 10, name: Incomplete | None = None):
    """output = input; While (Cond(output)) { output = Body(output) }

  Args:
    input: A list of `Tensor` objects.
      A list of input tensors whose types are T.
    cond: A function decorated with @Defun.
            A function takes 'input' and returns a tensor.  If the tensor is
            a scalar of non-boolean, the scalar is converted to a boolean
            according to the following rule: if the scalar is a numerical
            value, non-zero means True and zero means False; if the scalar is
            a string, non-empty means True and empty means False. If the
            tensor is not a scalar, non-emptiness means True and False
            otherwise.

            This should only be used when the while condition and body functions
            do not have stateful ops.
    body: A function decorated with @Defun.
            A function that takes a list of tensors and returns another
            list of tensors. Both lists have the same types as specified
            by T.
    output_shapes: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[]`.
    parallel_iterations: An optional `int`. Defaults to `10`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects. Has the same type as `input`.
  """

StatelessWhile: Incomplete

def stateless_while_eager_fallback(input, cond, body, output_shapes, parallel_iterations, name, ctx): ...
def symbolic_gradient(input, Tout, f, name: Incomplete | None = None):
    """Computes the gradient function for function f via backpropagation.

  Args:
    input: A list of `Tensor` objects. a list of input tensors of size N + M;
    Tout: A list of `tf.DTypes` that has length `>= 1`.
      the type list for the input list.
    f: A function decorated with @Defun.
      The function we want to compute the gradient for.

      The function 'f' must be a numerical function which takes N inputs and
      produces M outputs. Its gradient function 'g', which is computed by
      this SymbolicGradient op is a function taking N + M inputs and
      produces N outputs.

      I.e. if we have
         (y1, y2, ..., y_M) = f(x1, x2, ..., x_N),
      then, g is
         (dL/dx1, dL/dx2, ..., dL/dx_N) = g(x1, x2, ..., x_N,
                                           dL/dy1, dL/dy2, ..., dL/dy_M),

      where L is a scalar-value function of (x1, x2, ..., xN) (e.g., the
      loss function). dL/dx_i is the partial derivative of L with respect
      to x_i.

      (Needs some math expert to say the comment above better.)
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Tout`.
  """

SymbolicGradient: Incomplete

def symbolic_gradient_eager_fallback(input, Tout, f, name, ctx): ...
def to_bool(input, name: Incomplete | None = None):
    '''Converts a tensor to a scalar predicate.

  Converts a tensor to a scalar predicate with the following rules:

  - For 0D tensors, truthiness is determined by comparing against a "zero"
    value. For numerical types it is the obvious zero. For strings it is the
    empty string.

  - For >0D tensors, truthiness is determined by looking at the number of
    elements. If has zero elements, then the result is false. Otherwise the
    result is true.

  This matches the behavior of If and While for determining if a tensor counts
  as true/false for a branch condition.

  Args:
    input: A `Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  '''

ToBool: Incomplete

def to_bool_eager_fallback(input, name, ctx): ...

While: Incomplete
