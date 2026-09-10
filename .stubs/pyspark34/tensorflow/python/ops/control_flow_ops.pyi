from tensorflow.python.ops.gen_control_flow_ops import *
import abc
from _typeshed import Incomplete
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.core.protobuf import control_flow_pb2 as control_flow_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import composite_tensor as composite_tensor, constant_op as constant_op, dtypes as dtypes, errors as errors, indexed_slices as indexed_slices, ops as ops, tensor_shape as tensor_shape, tensor_spec as tensor_spec, tensor_util as tensor_util, type_spec as type_spec
from tensorflow.python.ops import array_ops as array_ops, gen_array_ops as gen_array_ops, gen_control_flow_ops as gen_control_flow_ops, gen_functional_ops as gen_functional_ops, gen_logging_ops as gen_logging_ops, gen_math_ops as gen_math_ops, math_ops as math_ops, tensor_array_ops as tensor_array_ops
from tensorflow.python.util import compat as compat, deprecation as deprecation, dispatch as dispatch, nest as nest, tf_should_use as tf_should_use, variable_utils as variable_utils
from tensorflow.python.util.lazy_loader import LazyLoader as LazyLoader
from tensorflow.python.util.tf_export import tf_export as tf_export

cond_v2: Incomplete
while_v2: Incomplete
def_function: Incomplete

def Assert(condition, data, summarize: Incomplete | None = None, name: Incomplete | None = None):
    """Asserts that the given condition is true.

  If `condition` evaluates to false, print the list of tensors in `data`.
  `summarize` determines how many entries of the tensors to print.

  Args:
    condition: The condition to evaluate.
    data: The tensors to print out when condition is false.
    summarize: Print this many entries of each tensor.
    name: A name for this operation (optional).

  Returns:
    assert_op: An `Operation` that, when executed, raises a
    `tf.errors.InvalidArgumentError` if `condition` is not true.
    @compatibility(eager)
    returns None
    @end_compatibility

  Raises:
    @compatibility(TF1)
    When in TF V1 mode (that is, outside `tf.function`) Assert needs a control
    dependency on the output to ensure the assertion executes:

  ```python
  # Ensure maximum element of x is smaller or equal to 1
  assert_op = tf.Assert(tf.less_equal(tf.reduce_max(x), 1.), [x])
  with tf.control_dependencies([assert_op]):
    ... code using x ...
  ```

    @end_compatibility
  """
def exit(tensor, name: Incomplete | None = None):
    """Exits the current frame to its parent frame.

  Exit makes its input `tensor` available to the parent frame.

  Args:
    tensor: The tensor to be made available to the parent frame.
    name: A name for this operation (optional).

  Returns:
    The same tensor as `tensor`.
  """
def switch(data, pred, dtype: Incomplete | None = None, name: Incomplete | None = None):
    """Forwards `data` to an output determined by `pred`.

  If `pred` is false, the `data` input is forwarded to the first output.
  Otherwise, the data goes to the second output.

  This op handles `Tensor`s and `IndexedSlices`.

  Args:
    data: The tensor to be forwarded to the appropriate output.
    pred: A scalar that specifies which output port will receive data.
    dtype: Optional element type for the returned tensor. If missing, the type
      is inferred from the type of `value`.
    name: A name for this operation (optional).

  Returns:
    `(output_false, output_true)`: If `pred` is true, data will be forwarded
    to `output_true`, otherwise it goes to `output_false`.
  """
def merge(inputs, name: Incomplete | None = None):
    """Returns the value of an available element of `inputs`.

  This op tests each of the tensors in `inputs` in turn to determine if any of
  them is available. If it finds an available tensor, it returns it and its
  index in `inputs`.

  It is an error if more than one tensor in `inputs` is available. If no tensor
  in `inputs` is available, the returned tensor and index are not set.

  This op handles both `Tensor`s and `IndexedSlices`. If inputs has a mix of
  `Tensor`s and `IndexedSlices`, all inputs are converted to IndexedSlices
  before merging.

  Args:
    inputs: The input tensors, at most one of which is available.
    name: A name for this operation (optional).

  Returns:
    A tuple containing the chosen input tensor and its index in `inputs`.

  Raises:
    ValueError: If any of the inputs is None, or inputs are IndexedSlices and
      some but not all have a dense_shape property.
  """

class ControlFlowContext(metaclass=abc.ABCMeta):
    """The base class for control flow context.

  The usage pattern is a sequence of (Enter, Exit) followed by a final
  ExitResult.

  We maintain the following state for control flow contexts during graph
  construction:
   1. graph has _control_flow_context: the current context used to
      construct new nodes. Changed by ctxt.Enter() and ctxt.Exit()
   2. op has _control_flow_context: the context to which the op belongs.
      Set at the time the op is created. Immutable.
   3. A ControlFlowContext has _outer_context: the context in which this
      context is created. Set at the time a context is created. Immutable.
   4. A ControlFlowContext has _context_stack.
      Pushed and popped by ctxt.Enter() and ctxt.Exit()
  """
    def __init__(self, values_def: Incomplete | None = None, import_scope: Incomplete | None = None) -> None: ...
    @property
    def name(self): ...
    @property
    def outer_context(self):
        """Return the context containing this context."""
    @property
    def grad_state(self) -> None: ...
    @property
    def back_prop(self) -> None: ...
    @abc.abstractmethod
    def to_control_flow_context_def(self, context_def, export_scope: Incomplete | None = None):
        """Serializes this into `context_def`.

    Args:
      context_def: a `ControlFlowContextDef` protocol buffer.
      export_scope: Optional `string`. Name scope to remove.
    """
    def AddName(self, name) -> None: ...
    def Enter(self) -> None:
        """Enter this control flow context."""
    def Exit(self) -> None:
        """Exit this control flow context."""
    def EnterGradientColocation(self, op, gradient_uid) -> None:
        """Start building a gradient colocated with an op."""
    def ExitGradientColocation(self, op, gradient_uid) -> None:
        """Start building a gradient colocated with an op."""
    def ExitResult(self, result):
        """Make a list of tensors available in the outer context."""
    def GetWhileContext(self):
        """Return the while context containing this context."""
    def AddInnerOp(self, op) -> None:
        """Notifies a scope about an operator added to an inner scope."""
    def GetControlPivot(self) -> None:
        """Returns the pivot node for this context, or None."""
    def IsWhileContext(self): ...
    def IsCondContext(self): ...
    def IsXLAContext(self): ...

class CondContext(ControlFlowContext):
    """The context for the conditional construct."""
    def __init__(self, pred: Incomplete | None = None, pivot: Incomplete | None = None, branch: Incomplete | None = None, name: str = 'cond_text', context_def: Incomplete | None = None, import_scope: Incomplete | None = None) -> None:
        """Creates a `CondContext`.

    Args:
      pred: The `boolean` tensor for the conditional predicate.
      pivot: The predicate tensor in this branch.
      branch: 0 or 1 representing this branch.
      name: Name of the `CondContext` python object.
      context_def: Optional `ContextDef` protocol buffer to initialize the
        `CondContext` object from.
      import_scope: Optional `string`. Name scope to add. Only used when
        initialing from protocol buffer.
    """
    @property
    def pred(self): ...
    @property
    def pivot(self): ...
    @property
    def branch(self): ...
    @property
    def grad_state(self): ...
    @property
    def back_prop(self): ...
    def GetControlPivot(self): ...
    def to_proto(self, export_scope: Incomplete | None = None):
        """Converts a `CondContext` to a `CondContextDef` protocol buffer.

    Args:
      export_scope: Optional `string`. Name scope to remove.

    Returns:
      A `CondContextDef` protocol buffer.
    """
    @staticmethod
    def from_proto(context_def, import_scope: Incomplete | None = None):
        """Returns a `CondContext` object created from `context_def`."""
    def to_control_flow_context_def(self, context_def, export_scope: Incomplete | None = None) -> None: ...
    def AddValue(self, val):
        """Add `val` to the current context and its outer context recursively."""
    def AddOp(self, op) -> None: ...
    def BuildCondBranch(self, fn):
        """Add the subgraph defined by fn() to the graph."""
    def IsCondContext(self): ...

def cond(pred, true_fn: Incomplete | None = None, false_fn: Incomplete | None = None, strict: bool = False, name: Incomplete | None = None, fn1: Incomplete | None = None, fn2: Incomplete | None = None):
    """Return `true_fn()` if the predicate `pred` is true else `false_fn()`.

  `true_fn` and `false_fn` both return lists of output tensors. `true_fn` and
  `false_fn` must have the same non-zero number and type of outputs.

  **WARNING**: Any Tensors or Operations created outside of `true_fn` and
  `false_fn` will be executed regardless of which branch is selected at runtime.

  Although this behavior is consistent with the dataflow model of TensorFlow,
  it has frequently surprised users who expected a lazier semantics.
  Consider the following simple program:

  ```python
  z = tf.multiply(a, b)
  result = tf.cond(x < y, lambda: tf.add(x, z), lambda: tf.square(y))
  ```

  If `x < y`, the `tf.add` operation will be executed and `tf.square`
  operation will not be executed. Since `z` is needed for at least one
  branch of the `cond`, the `tf.multiply` operation is always executed,
  unconditionally.

  Note that `cond` calls `true_fn` and `false_fn` *exactly once* (inside the
  call to `cond`, and not at all during `Session.run()`). `cond`
  stitches together the graph fragments created during the `true_fn` and
  `false_fn` calls with some additional graph nodes to ensure that the right
  branch gets executed depending on the value of `pred`.

  `tf.cond` supports nested structures as implemented in
  `tensorflow.python.util.nest`. Both `true_fn` and `false_fn` must return the
  same (possibly nested) value structure of lists, tuples, and/or named tuples.
  Singleton lists and tuples form the only exceptions to this: when returned by
  `true_fn` and/or `false_fn`, they are implicitly unpacked to single values.
  This behavior is disabled by passing `strict=True`.

  Args:
    pred: A scalar determining whether to return the result of `true_fn` or
      `false_fn`.
    true_fn: The callable to be performed if pred is true.
    false_fn: The callable to be performed if pred is false.
    strict: A boolean that enables/disables 'strict' mode; see above.
    name: Optional name prefix for the returned tensors.

  Returns:
    Tensors returned by the call to either `true_fn` or `false_fn`. If the
    callables return a singleton list, the element is extracted from the list.

  Raises:
    TypeError: if `true_fn` or `false_fn` is not callable.
    ValueError: if `true_fn` and `false_fn` do not return the same number of
      tensors, or return tensors of different types.

  Example:

  ```python
  x = tf.constant(2)
  y = tf.constant(5)
  def f1(): return tf.multiply(x, 17)
  def f2(): return tf.add(y, 23)
  r = tf.cond(tf.less(x, y), f1, f2)
  # r is set to f1().
  # Operations in f2 (e.g., tf.add) are not executed.
  ```

  """
def cond_for_tf_v2(pred, true_fn: Incomplete | None = None, false_fn: Incomplete | None = None, name: Incomplete | None = None):
    '''Return `true_fn()` if the predicate `pred` is true else `false_fn()`.

  Note: This op is automatically used in a `tf.function` to convert Python
  if-statements when the predicate is a `tf.Tensor`, unless `autograph=False` is
  explicitly specified in `tf.function` args. For example, the following are
  equivalent:

  >>> @tf.function
  ... def fun1(x,y):
  ...   if x > 0:  # AutoGraph converts if-statement to tf.cond().
  ...     z = y+1
  ...   else:
  ...     z = y-1
  ...   return z
  >>> fun1(tf.constant(7), tf.constant(3)).numpy()
  4

  >>> @tf.function
  ... def fun2(x,y):
  ...   pred = x > 0
  ...   true_fn =  lambda: y+1
  ...   false_fn = lambda: y-1
  ...   return tf.cond(pred, true_fn, false_fn)  # Use tf.cond() explicitly.
  >>> fun1(tf.constant(7), tf.constant(3)).numpy()
  4

  For more information, see [tf.function and AutoGraph guide](
  https://www.tensorflow.org/guide/function#autograph_transformations).

  `true_fn` and `false_fn` both return lists of output tensors. `true_fn` and
  `false_fn` must have the same non-zero number and type of outputs.

  **WARNING**: Any Tensors or Operations created outside of `true_fn` and
  `false_fn` will be executed regardless of which branch is selected at runtime.

  Although this behavior is consistent with the dataflow model of TensorFlow,
  it has frequently surprised users who expected a lazier semantics.
  Consider the following simple program:

  >>> x, y = tf.constant(2, dtype=tf.int32), tf.constant(4, dtype=tf.int32)
  >>> z = tf.multiply(x, y)
  >>> r = tf.cond(x < y, lambda: tf.add(x, z), lambda: tf.square(y))
  >>> r.numpy()
  10

  If `x < y`, the `tf.add` operation will be executed and `tf.square`
  operation will not be executed. Since `z` is needed for at least one
  branch of the `cond`, the `tf.multiply` operation is always executed,
  unconditionally.

  Note that `cond` calls `true_fn` and `false_fn` *exactly once* (inside the
  call to `cond`, and not at all during `Session.run()`). `cond`
  stitches together the graph fragments created during the `true_fn` and
  `false_fn` calls with some additional graph nodes to ensure that the right
  branch gets executed depending on the value of `pred`.

  `tf.cond` supports nested structures as implemented in
  `tensorflow.python.util.nest`. Both `true_fn` and `false_fn` must return the
  same (possibly nested) value structure of lists, tuples, and/or named tuples.
  Singleton lists and tuples form the only exceptions to this: when returned by
  `true_fn` and/or `false_fn`, they are implicitly unpacked to single values.

  Note: It is illegal to "directly" use tensors created inside a cond branch
  outside it, e.g. by storing a reference to a branch tensor in the python
  state. If you need to use a tensor created in a branch function you should
  return it as an output of the branch function and use the output from
  `tf.cond` instead.

  Args:
    pred: A scalar determining whether to return the result of `true_fn` or
      `false_fn`.
    true_fn: The callable to be performed if pred is true.
    false_fn: The callable to be performed if pred is false.
    name: Optional name prefix for the returned tensors.

  Returns:
    Tensors returned by the call to either `true_fn` or `false_fn`. If the
    callables return a singleton list, the element is extracted from the list.

  Raises:
    TypeError: if `true_fn` or `false_fn` is not callable.
    ValueError: if `true_fn` and `false_fn` do not return the same number of
      tensors, or return tensors of different types.

  Example:

  >>> x = tf.constant(2)
  >>> y = tf.constant(5)
  >>> def f1(): return tf.multiply(x, 7)
  >>> def f2(): return tf.add(y, 3)
  >>> r = tf.cond(tf.less(x, y), f1, f2)
  >>> # r is set to f1().
  >>> # Operations in f2 (e.g., tf.add) are not executed.
  >>> r.numpy()
  14

  '''

class WhileContext(ControlFlowContext):
    """The context for the loop construct."""
    def __init__(self, maximum_iterations: Incomplete | None = None, parallel_iterations: int = 10, back_prop: bool = True, swap_memory: bool = False, name: str = 'while_context', grad_state: Incomplete | None = None, context_def: Incomplete | None = None, import_scope: Incomplete | None = None) -> None:
        '''"Creates a `WhileContext`.

    Args:
      maximum_iterations: Optional upper bound on number of loop iterations.
      parallel_iterations: The number of iterations allowed to run in parallel.
      back_prop: Whether backprop is enabled for this while loop.
      swap_memory: Whether GPU-CPU memory swap is enabled for this loop.
      name: Optional name prefix for the returned tensors.
      grad_state: The gradient loop state.
      context_def: Optional `WhileContextDef` protocol buffer to initialize the
        `Whilecontext` python object from.
      import_scope: Optional `string`. Name scope to add. Only used when
        initialing from protocol buffer.
    '''
    @property
    def maximum_iterations(self):
        """The maximum number of iterations that will be executed."""
    @property
    def parallel_iterations(self):
        """The number of iterations allowed to run in parallel."""
    @property
    def back_prop(self):
        """True iff backprop is enabled for this while loop."""
    @property
    def swap_memory(self):
        """True iff GPU-CPU memory swap is enabled for this while loop."""
    @property
    def pivot(self):
        """The boolean tensor representing the loop termination condition."""
    @property
    def loop_enters(self):
        """The list of enter tensors for loop variables."""
    @property
    def loop_exits(self):
        """The list of exit tensors for loop variables."""
    @property
    def grad_state(self):
        """The gradient loop state."""
    def to_proto(self, export_scope: Incomplete | None = None):
        """Converts a `WhileContext` to a `WhileContextDef` protocol buffer.

    Args:
      export_scope: Optional `string`. Name scope to remove.

    Returns:
      A `WhileContextDef` protocol buffer.
    """
    def to_control_flow_context_def(self, context_def, export_scope: Incomplete | None = None) -> None: ...
    @staticmethod
    def from_proto(context_def, import_scope: Incomplete | None = None):
        """Returns a `WhileContext` object created from `context_def`.

    Args:
      context_def: A `WhileContextDef` protocol buffer.
      import_scope: Optional `string`. Name scope to add.

    Returns:
      A `WhileContext` Python object.
    """
    def GetWhileContext(self): ...
    def GetControlPivot(self): ...
    def AddValue(self, val):
        """Add `val` to the current context and its outer context recursively."""
    def AddOp(self, op) -> None:
        """Add `op` to the current context."""
    def AddForwardLoopCounter(self, outer_grad_state):
        """Adds a loop that counts the number of iterations.

    This is added to the forward loop at the time when we start to
    create the loop for backprop gradient computation. Called in
    the outer context of this forward context.

    The pseudocode is:
      `n = 0; while (_pivot) { n++; }`

    Note that a control dependency is added to `n` to ensure the correct
    execution order of stack push ops.

    Args:
      outer_grad_state: The outer grad state. None if not nested.

    Returns:
      The number of iterations taken by the forward loop and the loop index.
    """
    def AddBackpropLoopCounter(self, count, outer_grad_state):
        """Add the backprop loop that controls the iterations.

    This is added to the backprop loop. It is used to control the loop
    termination of the backprop loop. Called in the outer context of
    this grad context.

    The pseudocode is:
      `n = count; while (n >= 1) { n--; }`

    Note that a control dependency is added to `final_zero` to ensure the
    correct execution order of stack pop ops.

    Args:
      count: The number of iterations for backprop.
      outer_grad_state: The outer grad state. None if not nested.

    Returns:
      The loop index.
    """
    def AddBackpropAccumulator(self, op, grad):
        """Add an accumulation loop for every loop invariant.

    This is added to the backprop loop. It is used to accumulate partial
    gradients within each loop iteration. Called when in the gradient while
    context.

    The pseudocode is:
      ```
      acc = 0.0;
      while (_pivot) {
        acc += grad;
      }
      ```

    Args:
      op: The Enter op for a loop invariant.
      grad: The partial gradient of an iteration for a loop invariant.

    Returns:
      The gradient for a loop invariant.
    """
    def AddBackpropIndexedSlicesAccumulator(self, op, grad):
        """This is used for accumulating gradients that are IndexedSlices.

    This is essentially the equivalent of AddBackpropAccumulator but optimized
    for things like updating embeddings from within a while loop.

    Args:
      op: The Enter op for a loop invariant.
      grad: The partial gradients represented as an IndexedSlices.

    Returns:
      The accumulated IndexedSlices gradient of the loop invariant.
    """
    def BuildLoop(self, pred, body, loop_vars, shape_invariants, return_same_structure):
        """Add the loop termination condition and body to the graph."""
    def IsWhileContext(self): ...

def while_loop_v2(cond, body, loop_vars, shape_invariants: Incomplete | None = None, parallel_iterations: int = 10, back_prop: bool = True, swap_memory: bool = False, maximum_iterations: Incomplete | None = None, name: Incomplete | None = None):
    '''Repeat `body` while the condition `cond` is true.

  Note: This op is automatically used in a `tf.function` to convert Python for-
  and while- loops when the loop variable is a `tf.Tensor`, unless
  `autograph=False` is explicitly specified in `tf.function` args. For example,
  the following are equivalent:

  >>> @tf.function
  ... def sumSquare(n):
  ...   i, result = tf.constant(0), tf.constant(0)
  ...   while i < n: # AutoGraph converts while-loop to tf.while_loop().
  ...     result += i * i
  ...     i += 1
  ...   return result
  >>> sumSquare(10).numpy()
  285

  >>> @tf.function
  ... def sumSquare2(n):
  ...   i, result = tf.constant(0), tf.constant(0)
  ...   c = lambda i, _: tf.less(i, n)
  ...   b = lambda i, result: (i + 1, result + i * i)
  ...   return tf.while_loop(c, b, [i, result])[1]
  >>> sumSquare2(10).numpy()
  285

  For more information, see [tf.function and AutoGraph guide
  ](https://www.tensorflow.org/guide/function#autograph_transformations).

  `cond` is a callable returning a boolean scalar tensor. `body` is a callable
  returning a (possibly nested) tuple, namedtuple or list of tensors of the same
  arity (length and structure) and types as `loop_vars`. `loop_vars` is a
  (possibly nested) tuple, namedtuple or list of tensors that is passed to both
  `cond` and `body`. `cond` and `body` both take as many arguments as there are
  `loop_vars`.

  In addition to regular Tensors or IndexedSlices, the body may accept and
  return TensorArray objects.  The flows of the TensorArray objects will
  be appropriately forwarded between loops and during gradient calculations.

  Note that `while_loop` calls `cond` and `body` *exactly once* (inside the
  call to `while_loop`, and not at all during `Session.run()`). `while_loop`
  stitches together the graph fragments created during the `cond` and `body`
  calls with some additional graph nodes to create the graph flow that
  repeats `body` until `cond` returns false.

  For correctness, `tf.while_loop()` strictly enforces shape invariants for
  the loop variables. A shape invariant is a (possibly partial) shape that
  is unchanged across the iterations of the loop. An error will be raised
  if the shape of a loop variable after an iteration is determined to be more
  general than or incompatible with its shape invariant. For example, a shape
  of `[11, None]` is more general than a shape of `[11, 17]`, and `[11, 21]` is
  not compatible with `[11, 17]`. By default (if the argument `shape_invariants`
  is not specified), it is assumed that the initial shape of each tensor in
  `loop_vars` is the same in every iteration. The `shape_invariants` argument
  allows the caller to specify a less specific shape invariant for each loop
  variable, which is needed if the shape varies between iterations. The
  `tf.Tensor.set_shape`
  function may also be used in the `body` function to indicate that
  the output loop variable has a particular shape. The shape invariant for
  SparseTensor and IndexedSlices are treated specially as follows:

  a) If a loop variable is a SparseTensor, the shape invariant must be
  `TensorShape([r])` where `r` is the rank of the dense tensor represented
  by the sparse tensor. It means the shapes of the three tensors of the
  SparseTensor are `([None], [None, r], [r])`. NOTE: The shape invariant here
  is the shape of the SparseTensor.dense_shape property. It must be the shape of
  a vector.

  b) If a loop variable is an IndexedSlices, the shape invariant must be
  a shape invariant of the values tensor of the IndexedSlices. It means
  the shapes of the three tensors of the IndexedSlices are `(shape, [shape[0]],
  [shape.ndims])`.

  `while_loop` implements non-strict semantics, enabling multiple iterations
  to run in parallel. The maximum number of parallel iterations can be
  controlled by `parallel_iterations`, which gives users some control over
  memory consumption and execution order. For correct programs, `while_loop`
  should return the same result for any `parallel_iterations > 0`.

  For training, TensorFlow stores the tensors that are produced in the
  forward inference and are needed in back propagation. These tensors are a
  main source of memory consumption and often cause OOM errors when training
  on GPUs. When the flag swap_memory is true, we swap out these tensors from
  GPU to CPU. This for example allows us to train RNN models with very long
  sequences and large batches.

  Args:
    cond: A callable that represents the termination condition of the loop.
    body: A callable that represents the loop body.
    loop_vars: A (possibly nested) tuple, namedtuple or list of numpy array,
      `Tensor`, and `TensorArray` objects.
    shape_invariants: The shape invariants for the loop variables.
    parallel_iterations: The number of iterations allowed to run in parallel. It
      must be a positive integer.
    back_prop: (optional) Deprecated. False disables support for back
      propagation. Prefer using `tf.stop_gradient` instead.
    swap_memory: Whether GPU-CPU memory swap is enabled for this loop.
    maximum_iterations: Optional maximum number of iterations of the while loop
      to run.  If provided, the `cond` output is AND-ed with an additional
      condition ensuring the number of iterations executed is no greater than
      `maximum_iterations`.
    name: Optional name prefix for the returned tensors.

  Returns:
    The output tensors for the loop variables after the loop. The return value
      has the same structure as `loop_vars`.

  Raises:
    TypeError: if `cond` or `body` is not callable.
    ValueError: if `loop_vars` is empty.

  Example:

  >>> i = tf.constant(0)
  >>> c = lambda i: tf.less(i, 10)
  >>> b = lambda i: (tf.add(i, 1), )
  >>> r = tf.while_loop(c, b, [i])[0]
  >>> r.numpy()
  10

  Example with nesting and a namedtuple:

  >>> import collections
  >>> Pair = collections.namedtuple(\'Pair\', \'j, k\')
  >>> ijk_0 = (tf.constant(0), Pair(tf.constant(1), tf.constant(2)))
  >>> c = lambda i, p: i < 10
  >>> b = lambda i, p: (i + 1, Pair((p.j + p.k), (p.j - p.k)))
  >>> ijk_final = tf.while_loop(c, b, ijk_0)[1]
  >>> ijk_final[0].numpy(), ijk_final[1].numpy()
  (32, 64)

  Example using shape_invariants:

  >>> i0 = tf.constant(0)
  >>> m0 = tf.ones([2, 2])
  >>> c = lambda i, m: i < 10
  >>> b = lambda i, m: [i+1, tf.concat([m, m], axis=0)]
  >>> tf.while_loop(
  ...     c, b, loop_vars=[i0, m0],
  ...     shape_invariants=[i0.get_shape(), tf.TensorShape([None, 2])])[1]
  <tf.Tensor: shape=(2048, 2), dtype=float32, numpy=...>

  Example which demonstrates non-strict semantics: In the following
  example, the final value of `counter` does not depend on `x`. So
  the `while_loop` can increment the counter parallel to updates of `x`.
  However, because the loop counter at one loop iteration depends
  on the value at the previous iteration, the loop counter itself cannot
  be incremented in parallel. Hence if we just want the final value of the
  counter (which we print on the line `print(sess.run(i))`), then
  `x` will never be incremented, but the counter will be updated on a
  single thread. Conversely, if we want the value of the output (which we
  print on the line `print(sess.run(out).shape)`), then the counter may be
  incremented on its own thread, while `x` can be incremented in
  parallel on a separate thread. In the extreme case, it is conceivable
  that the thread incrementing the counter runs until completion before
  `x` is incremented even a single time. The only thing that can never
  happen is that the thread updating `x` can never get ahead of the
  counter thread because the thread incrementing `x` depends on the value
  of the counter.

  >>> with tf.compat.v1.Session() as sess:
  ...   n = 10
  ...   c = lambda i, x: i < n
  ...   b = lambda i, x: (
  ...       tf.compat.v1.Print(i + 1, [i], "Updating i based on i == "),
  ...       # Let x depend on i
  ...       tf.compat.v1.Print(x + i, [i], "Updating x based on i == "))
  ...
  ...   # Make x to be a big matrix so its updating thread would run slowly
  ...   x = tf.zeros([1000, 100], dtype=tf.int32)
  ...   counter = tf.constant(0)
  ...   counter_out, x_out = tf.while_loop(c, b, (counter, x))
  ...
  ...   # The following line may increment the counter and x in parallel.
  ...   # The counter thread may get ahead of the x thread, but not the
  ...   # other way around. For example, the log may contain these messages:
  ...   # ```
  ...   # Updating i based on i == [9]
  ...   # Updating x based on i == [3]
  ...   # ```
  ...   # meaning that the counter(i) thread is on iteration 9,
  ...   # while the x thread is on iteration 3.
  ...   print(sess.run(x_out).shape)
  (1000, 100)

  '''
def while_loop(cond, body, loop_vars, shape_invariants: Incomplete | None = None, parallel_iterations: int = 10, back_prop: bool = True, swap_memory: bool = False, name: Incomplete | None = None, maximum_iterations: Incomplete | None = None, return_same_structure: bool = False):
    '''Repeat `body` while the condition `cond` is true.

  `cond` is a callable returning a boolean scalar tensor. `body` is a callable
  returning a (possibly nested) tuple, namedtuple or list of tensors of the same
  arity (length and structure) and types as `loop_vars`. `loop_vars` is a
  (possibly nested) tuple, namedtuple or list of tensors that is passed to both
  `cond` and `body`. `cond` and `body` both take as many arguments as there are
  `loop_vars`.

  In addition to regular Tensors or IndexedSlices, the body may accept and
  return TensorArray objects.  The flows of the TensorArray objects will
  be appropriately forwarded between loops and during gradient calculations.

  Note that `while_loop` calls `cond` and `body` *exactly once* (inside the
  call to `while_loop`, and not at all during `Session.run()`). `while_loop`
  stitches together the graph fragments created during the `cond` and `body`
  calls with some additional graph nodes to create the graph flow that
  repeats `body` until `cond` returns false.

  For correctness, `tf.while_loop()` strictly enforces shape invariants for
  the loop variables. A shape invariant is a (possibly partial) shape that
  is unchanged across the iterations of the loop. An error will be raised
  if the shape of a loop variable after an iteration is determined to be more
  general than or incompatible with its shape invariant. For example, a shape
  of [11, None] is more general than a shape of [11, 17], and [11, 21] is not
  compatible with [11, 17]. By default (if the argument `shape_invariants` is
  not specified), it is assumed that the initial shape of each tensor in
  `loop_vars` is the same in every iteration. The `shape_invariants` argument
  allows the caller to specify a less specific shape invariant for each loop
  variable, which is needed if the shape varies between iterations. The
  `tf.Tensor.set_shape`
  function may also be used in the `body` function to indicate that
  the output loop variable has a particular shape. The shape invariant for
  SparseTensor and IndexedSlices are treated specially as follows:

  a) If a loop variable is a SparseTensor, the shape invariant must be
  TensorShape([r]) where r is the rank of the dense tensor represented
  by the sparse tensor. It means the shapes of the three tensors of the
  SparseTensor are ([None], [None, r], [r]). NOTE: The shape invariant here
  is the shape of the SparseTensor.dense_shape property. It must be the shape of
  a vector.

  b) If a loop variable is an IndexedSlices, the shape invariant must be
  a shape invariant of the values tensor of the IndexedSlices. It means
  the shapes of the three tensors of the IndexedSlices are (shape, [shape[0]],
  [shape.ndims]).

  `while_loop` implements non-strict semantics, enabling multiple iterations
  to run in parallel. The maximum number of parallel iterations can be
  controlled by `parallel_iterations`, which gives users some control over
  memory consumption and execution order. For correct programs, `while_loop`
  should return the same result for any parallel_iterations > 0.

  For training, TensorFlow stores the tensors that are produced in the
  forward inference and are needed in back propagation. These tensors are a
  main source of memory consumption and often cause OOM errors when training
  on GPUs. When the flag swap_memory is true, we swap out these tensors from
  GPU to CPU. This for example allows us to train RNN models with very long
  sequences and large batches.

  Args:
    cond: A callable that represents the termination condition of the loop.
    body: A callable that represents the loop body.
    loop_vars: A (possibly nested) tuple, namedtuple or list of numpy array,
      `Tensor`, and `TensorArray` objects.
    shape_invariants: The shape invariants for the loop variables.
    parallel_iterations: The number of iterations allowed to run in parallel. It
      must be a positive integer.
    back_prop: Whether backprop is enabled for this while loop.
    swap_memory: Whether GPU-CPU memory swap is enabled for this loop.
    name: Optional name prefix for the returned tensors.
    maximum_iterations: Optional maximum number of iterations of the while loop
      to run.  If provided, the `cond` output is AND-ed with an additional
      condition ensuring the number of iterations executed is no greater than
      `maximum_iterations`.
    return_same_structure: If True, output has same structure as `loop_vars`. If
      eager execution is enabled, this is ignored (and always treated as True).

  Returns:
    The output tensors for the loop variables after the loop.
     If `return_same_structure` is True, the return value has the same
     structure as `loop_vars`.
     If `return_same_structure` is False, the return value is a Tensor,
     TensorArray or IndexedSlice if the length of `loop_vars` is 1, or a list
     otherwise.

  Raises:
    TypeError: if `cond` or `body` is not callable.
    ValueError: if `loop_vars` is empty.

  Example:

  ```python
  i = tf.constant(0)
  c = lambda i: tf.less(i, 10)
  b = lambda i: tf.add(i, 1)
  r = tf.while_loop(c, b, [i])
  ```

  Example with nesting and a namedtuple:

  ```python
  import collections
  Pair = collections.namedtuple(\'Pair\', \'j, k\')
  ijk_0 = (tf.constant(0), Pair(tf.constant(1), tf.constant(2)))
  c = lambda i, p: i < 10
  b = lambda i, p: (i + 1, Pair((p.j + p.k), (p.j - p.k)))
  ijk_final = tf.while_loop(c, b, ijk_0)
  ```

  Example using shape_invariants:

  ```python
  i0 = tf.constant(0)
  m0 = tf.ones([2, 2])
  c = lambda i, m: i < 10
  b = lambda i, m: [i+1, tf.concat([m, m], axis=0)]
  tf.while_loop(
      c, b, loop_vars=[i0, m0],
      shape_invariants=[i0.get_shape(), tf.TensorShape([None, 2])])
  ```

  Example which demonstrates non-strict semantics: In the following
  example, the final value of the counter `i` does not depend on `x`. So
  the `while_loop` can increment the counter parallel to updates of `x`.
  However, because the loop counter at one loop iteration depends
  on the value at the previous iteration, the loop counter itself cannot
  be incremented in parallel. Hence if we just want the final value of the
  counter (which we print on the line `print(sess.run(i))`), then
  `x` will never be incremented, but the counter will be updated on a
  single thread. Conversely, if we want the value of the output (which we
  print on the line `print(sess.run(out).shape)`), then the counter may be
  incremented on its own thread, while `x` can be incremented in
  parallel on a separate thread. In the extreme case, it is conceivable
  that the thread incrementing the counter runs until completion before
  `x` is incremented even a single time. The only thing that can never
  happen is that the thread updating `x` can never get ahead of the
  counter thread because the thread incrementing `x` depends on the value
  of the counter.

  ```python
  import tensorflow as tf

  n = 10000
  x = tf.constant(list(range(n)))
  c = lambda i, x: i < n
  b = lambda i, x: (tf.compat.v1.Print(i + 1, [i]), tf.compat.v1.Print(x + 1,
  [i], "x:"))
  i, out = tf.while_loop(c, b, (0, x))
  with tf.compat.v1.Session() as sess:
      print(sess.run(i))  # prints [0] ... [9999]

      # The following line may increment the counter and x in parallel.
      # The counter thread may get ahead of the other thread, but not the
      # other way around. So you may see things like
      # [9996] x:[9987]
      # meaning that the counter thread is on iteration 9996,
      # while the other thread is on iteration 9987
      print(sess.run(out).shape)
  ```

  '''
def with_dependencies(dependencies, output_tensor, name: Incomplete | None = None):
    """Produces the content of `output_tensor` only after `dependencies`.

  In some cases, a user may want the output of an operation to be
  consumed externally only after some other dependencies have run
  first. This function ensures returns `output_tensor`, but only after all
  operations in `dependencies` have run. Note that this means that there is
  no guarantee that `output_tensor` will be evaluated after any `dependencies`
  have run.

  See also `tf.tuple` and `tf.group`.

  Args:
    dependencies: Iterable of operations to run before this op finishes.
    output_tensor: A `Tensor` or `IndexedSlices` that will be returned.
    name: (Optional) A name for this operation.

  Returns:
    Same as `output_tensor`.

  Raises:
    TypeError: if `output_tensor` is not a `Tensor` or `IndexedSlices`.
  """
def group(*inputs, **kwargs):
    """Create an op that groups multiple operations.

  When this op finishes, all ops in `inputs` have finished. This op has no
  output.

  Note: *In TensorFlow 2 with eager and/or Autograph, you should not require
  this method, as ops execute in the expected order thanks to automatic control
  dependencies.* Only use `tf.group` when working with v1
  `tf.Graph` code.

  When operating in a v1-style graph context, ops are not executed in the same
  order as specified in the code; TensorFlow will attempt to execute ops in
  parallel or in an order convenient to the result it is computing.  `tf.group`
  allows you to request that one or more results finish before execution
  continues.

  `tf.group` creates a single op (of type `NoOp`), and then adds appropriate
  control dependencies.  Thus, `c = tf.group(a, b)` will compute the same graph
  as this:

      with tf.control_dependencies([a, b]):
          c = tf.no_op()

  See also `tf.tuple` and
  `tf.control_dependencies`.

  Args:
    *inputs: Zero or more tensors to group.
    name: A name for this operation (optional).

  Returns:
    An Operation that executes all its inputs.

  Raises:
    ValueError: If an unknown keyword argument is provided.
  """
def tuple_v2(tensors, control_inputs: Incomplete | None = None, name: Incomplete | None = None):
    """Groups tensors together.

  The returned tensors have the same value as the input tensors, but they
  are computed only after all the input tensors have been computed.

  Note: *In TensorFlow 2 with eager and/or Autograph, you should not require
  this method, as ops execute in the expected order thanks to automatic control
  dependencies.* Only use `tf.tuple` when working with v1 `tf.Graph` code.

  See also `tf.group` and `tf.control_dependencies`.

  Example:
  >>> with tf.Graph().as_default():
  ...   with tf.compat.v1.Session() as sess:
  ...     v = tf.Variable(0.0)
  ...     a = tf.constant(1.0)
  ...     sess.run(tf.compat.v1.global_variables_initializer())
  ...     for i in range(5):
  ...       update_op = v.assign_add(1.0)
  ...       b = a + v
  ...       res_b = sess.run(b)
  ...       res_v = sess.run(v)
  ...       print(res_v)
  0.0
  0.0
  0.0
  0.0
  0.0

  >>> with tf.Graph().as_default():
  ...   with tf.compat.v1.Session() as sess:
  ...     v = tf.Variable(0.0)
  ...     a = tf.constant(1.0)
  ...     sess.run(tf.compat.v1.global_variables_initializer())
  ...     for i in range(5):
  ...       update_op = v.assign_add(1.0)
  ...       calc = [a + v]
  ...       # `tf.tuple` ensures `update_op` is run before `b`
  ...       b = tf.tuple(calc, [tf.group(update_op)])
  ...       res_b = sess.run(b)
  ...       res_v = sess.run(v)
  ...       print(res_v)
  1.0
  2.0
  3.0
  4.0
  5.0


  Args:
    tensors: A list of `Tensor`s or `IndexedSlices`, some entries can be `None`.
    control_inputs: List of additional ops to finish before returning.
    name: (optional) A name to use as a `name_scope` for the operation.

  Returns:
    Same as `tensors`.

  Raises:
    ValueError: If `tensors` does not contain any `Tensor` or `IndexedSlices`.
    TypeError: If `control_inputs` is not a list of `Operation` or `Tensor`
      objects.

  """
def tuple(tensors, name: Incomplete | None = None, control_inputs: Incomplete | None = None):
    '''Group tensors together.

  This creates a tuple of tensors with the same values as the `tensors`
  argument, except that the value of each tensor is only returned after the
  values of all tensors have been computed.

  `control_inputs` contains additional ops that have to finish before this op
  finishes, but whose outputs are not returned.

  This can be used as a "join" mechanism for parallel computations: all the
  argument tensors can be computed in parallel, but the values of any tensor
  returned by `tuple` are only available after all the parallel computations
  are done.

  See also `tf.group` and
  `tf.control_dependencies`.

  Args:
    tensors: A list of `Tensor`s or `IndexedSlices`, some entries can be `None`.
    name: (optional) A name to use as a `name_scope` for the operation.
    control_inputs: List of additional ops to finish before returning.

  Returns:
    Same as `tensors`.

  Raises:
    ValueError: If `tensors` does not contain any `Tensor` or `IndexedSlices`.
    TypeError: If `control_inputs` is not a list of `Operation` or `Tensor`
      objects.

  '''
def case_v2(pred_fn_pairs, default: Incomplete | None = None, exclusive: bool = False, strict: bool = False, name: str = 'case'):
    '''Create a case operation.

  See also `tf.switch_case`.

  The `pred_fn_pairs` parameter is a list of pairs of size N.
  Each pair contains a boolean scalar tensor and a python callable that
  creates the tensors to be returned if the boolean evaluates to True.
  `default` is a callable generating a list of tensors. All the callables
  in `pred_fn_pairs` as well as `default` (if provided) should return the same
  number and types of tensors.

  If `exclusive==True`, all predicates are evaluated, and an exception is
  thrown if more than one of the predicates evaluates to `True`.
  If `exclusive==False`, execution stops at the first predicate which
  evaluates to True, and the tensors generated by the corresponding function
  are returned immediately. If none of the predicates evaluate to True, this
  operation returns the tensors generated by `default`.

  `tf.case` supports nested structures as implemented in
  `tf.nest`. All of the callables must return the same (possibly nested) value
  structure of lists, tuples, and/or named tuples. Singleton lists and tuples
  form the only exceptions to this: when returned by a callable, they are
  implicitly unpacked to single values. This behavior is disabled by passing
  `strict=True`.

  @compatibility(v2)
  `pred_fn_pairs` could be a dictionary in v1. However, tf.Tensor and
  tf.Variable are no longer hashable in v2, so cannot be used as a key for a
  dictionary.  Please use a list or a tuple instead.
  @end_compatibility


  **Example 1:**

  Pseudocode:

  ```
  if (x < y) return 17;
  else return 23;
  ```

  Expressions:

  ```python
  f1 = lambda: tf.constant(17)
  f2 = lambda: tf.constant(23)
  r = tf.case([(tf.less(x, y), f1)], default=f2)
  ```

  **Example 2:**

  Pseudocode:

  ```
  if (x < y && x > z) raise OpError("Only one predicate may evaluate to True");
  if (x < y) return 17;
  else if (x > z) return 23;
  else return -1;
  ```

  Expressions:

  ```python
  def f1(): return tf.constant(17)
  def f2(): return tf.constant(23)
  def f3(): return tf.constant(-1)
  r = tf.case([(tf.less(x, y), f1), (tf.greater(x, z), f2)],
           default=f3, exclusive=True)
  ```

  Args:
    pred_fn_pairs: List of pairs of a boolean scalar tensor and a callable which
      returns a list of tensors.
    default: Optional callable that returns a list of tensors.
    exclusive: True iff at most one predicate is allowed to evaluate to `True`.
    strict: A boolean that enables/disables \'strict\' mode; see above.
    name: A name for this operation (optional).

  Returns:
    The tensors returned by the first pair whose predicate evaluated to True, or
    those returned by `default` if none does.

  Raises:
    TypeError: If `pred_fn_pairs` is not a list/tuple.
    TypeError: If `pred_fn_pairs` is a list but does not contain 2-tuples.
    TypeError: If `fns[i]` is not callable for any i, or `default` is not
               callable.
  '''
def case(pred_fn_pairs, default: Incomplete | None = None, exclusive: bool = False, strict: bool = False, name: str = 'case'):
    '''Create a case operation.

  See also `tf.switch_case`.

  The `pred_fn_pairs` parameter is a dict or list of pairs of size N.
  Each pair contains a boolean scalar tensor and a python callable that
  creates the tensors to be returned if the boolean evaluates to True.
  `default` is a callable generating a list of tensors. All the callables
  in `pred_fn_pairs` as well as `default` (if provided) should return the same
  number and types of tensors.

  If `exclusive==True`, all predicates are evaluated, and an exception is
  thrown if more than one of the predicates evaluates to `True`.
  If `exclusive==False`, execution stops at the first predicate which
  evaluates to True, and the tensors generated by the corresponding function
  are returned immediately. If none of the predicates evaluate to True, this
  operation returns the tensors generated by `default`.

  `tf.case` supports nested structures as implemented in
  `tf.nest`. All of the callables must return the same (possibly nested) value
  structure of lists, tuples, and/or named tuples. Singleton lists and tuples
  form the only exceptions to this: when returned by a callable, they are
  implicitly unpacked to single values. This behavior is disabled by passing
  `strict=True`.

  If an unordered dictionary is used for `pred_fn_pairs`, the order of the
  conditional tests is not guaranteed. However, the order is guaranteed to be
  deterministic, so that variables created in conditional branches are created
  in fixed order across runs.

  @compatibility(eager)
  Unordered dictionaries are not supported in eager mode when `exclusive=False`.
  Use a list of tuples instead.
  @end_compatibility


  **Example 1:**

  Pseudocode:

  ```
  if (x < y) return 17;
  else return 23;
  ```

  Expressions:

  ```python
  f1 = lambda: tf.constant(17)
  f2 = lambda: tf.constant(23)
  r = tf.case([(tf.less(x, y), f1)], default=f2)
  ```

  **Example 2:**

  Pseudocode:

  ```
  if (x < y && x > z) raise OpError("Only one predicate may evaluate to True");
  if (x < y) return 17;
  else if (x > z) return 23;
  else return -1;
  ```

  Expressions:

  ```python
  def f1(): return tf.constant(17)
  def f2(): return tf.constant(23)
  def f3(): return tf.constant(-1)
  r = tf.case({tf.less(x, y): f1, tf.greater(x, z): f2},
           default=f3, exclusive=True)
  ```

  Args:
    pred_fn_pairs: Dict or list of pairs of a boolean scalar tensor and a
      callable which returns a list of tensors.
    default: Optional callable that returns a list of tensors.
    exclusive: True iff at most one predicate is allowed to evaluate to `True`.
    strict: A boolean that enables/disables \'strict\' mode; see above.
    name: A name for this operation (optional).

  Returns:
    The tensors returned by the first pair whose predicate evaluated to True, or
    those returned by `default` if none does.

  Raises:
    TypeError: If `pred_fn_pairs` is not a list/dictionary.
    TypeError: If `pred_fn_pairs` is a list but does not contain 2-tuples.
    TypeError: If `fns[i]` is not callable for any i, or `default` is not
               callable.
  '''
def switch_case(branch_index, branch_fns, default: Incomplete | None = None, name: str = 'switch_case'):
    """Create a switch/case operation, i.e. an integer-indexed conditional.

  See also `tf.case`.

  This op can be substantially more efficient than `tf.case` when exactly one
  branch will be selected. `tf.switch_case` is more like a C++ switch/case
  statement than `tf.case`, which is more like an if/elif/elif/else chain.

  The `branch_fns` parameter is either a dict from `int` to callables, or list
  of (`int`, callable) pairs, or simply a list of callables (in which case the
  index is implicitly the key). The `branch_index` `Tensor` is used to select an
  element in `branch_fns` with matching `int` key, falling back to `default`
  if none match, or `max(keys)` if no `default` is provided. The keys must form
  a contiguous set from `0` to `len(branch_fns) - 1`.

  `tf.switch_case` supports nested structures as implemented in `tf.nest`. All
  callables must return the same (possibly nested) value structure of lists,
  tuples, and/or named tuples.

  **Example:**

  Pseudocode:

  ```c++
  switch (branch_index) {  // c-style switch
    case 0: return 17;
    case 1: return 31;
    default: return -1;
  }
  ```
  or
  ```python
  branches = {0: lambda: 17, 1: lambda: 31}
  branches.get(branch_index, lambda: -1)()
  ```

  Expressions:

  ```python
  def f1(): return tf.constant(17)
  def f2(): return tf.constant(31)
  def f3(): return tf.constant(-1)
  r = tf.switch_case(branch_index, branch_fns={0: f1, 1: f2}, default=f3)
  # Equivalent: tf.switch_case(branch_index, branch_fns={0: f1, 1: f2, 2: f3})
  ```

  Args:
    branch_index: An int Tensor specifying which of `branch_fns` should be
      executed.
    branch_fns: A `dict` mapping `int`s to callables, or a `list` of
      (`int`, callable) pairs, or simply a list of callables (in which case the
      index serves as the key). Each callable must return a matching structure
      of tensors.
    default: Optional callable that returns a structure of tensors.
    name: A name for this operation (optional).

  Returns:
    The tensors returned by the callable identified by `branch_index`, or those
    returned by `default` if no key matches and `default` was provided, or those
    returned by the max-keyed `branch_fn` if no `default` is provided.

  Raises:
    TypeError: If `branch_fns` is not a list/dictionary.
    TypeError: If `branch_fns` is a list but does not contain 2-tuples or
               callables.
    TypeError: If `fns[i]` is not callable for any i, or `default` is not
               callable.
  """
def execute_fn_for_device(device_branch_fns, default_fn, name: str = 'execute_fn'):
    '''Executes one of the provided callables based on the device placement.

  This API is used when the implementations for high level function depend on
  the underlying device placement. It takes a dictionary of device type to
  callables. The device type includes "CPU", "GPU", "TPU", etc. When the type of
  the device where to run this op matches the key in \'device_branch_fns\',
  the corresponding callable is executed, falling back to \'default_fn\' if none
  matches.

  **Example:**
  ```python
  def f1(): return tf.constant(1)
  def f2(): return tf.constant(2)
  r = tf.execute_fn_for_device({"CPU": f1, "GPU": f2}, default_fn=f1)
  ```
  \'r\' is evaluated as 1 when it runs on CPU, 2 running on GPU, 1 running on
  any other device types.


  Args:
    device_branch_fns: a dictionary of device types to the callables. Each
      callable must return a matching structure of tensors.
    default_fn: fallback callable when the underlying device does not match any
      key in the \'device_branch_fns\'.
    name: A name for this operation (optional).

  Returns:
    The tensors returned by the callable identified by device type during
    execution, or those returned by \'default_fn\' if no key matches.
  '''

class XLAControlFlowContext(ControlFlowContext):
    """Base class for XLA and TPU control flow contexts."""
    def __init__(self) -> None: ...
    def to_control_flow_context_def(self, context_def, export_scope: Incomplete | None = None) -> None: ...
    def IsXLAContext(self): ...
    def AddOp(self, _) -> None: ...
    def AddValue(self, x): ...
    def RequiresUniqueFunctionRetracing(self):
        """Returns whether the tf.function should be retraced if the context changes.
    """

def get_enclosing_xla_context():
    """Recursively find and return the XLAControlFlowContext."""
def from_control_flow_context_def(context_def, import_scope: Incomplete | None = None):
    """Deserializes `context_def` into the appropriate ControlFlowContext.

  Args:
    context_def: ControlFlowContextDef proto
    import_scope: Optional `string`. Name scope to add.

  Returns:
    A ControlFlowContext subclass
  """
