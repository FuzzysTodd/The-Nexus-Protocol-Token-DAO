import abc
from _typeshed import Incomplete
from tensorflow.python.distribute import distribute_lib as distribute_lib, distribute_utils as distribute_utils
from tensorflow.python.eager import backprop as backprop, context as context
from tensorflow.python.framework import dtypes as dtypes, indexed_slices as indexed_slices, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, gradients as gradients, math_ops as math_ops, resource_variable_ops as resource_variable_ops, state_ops as state_ops, variable_scope as variable_scope, variables as variables
from tensorflow.python.trackable import base as trackable
from tensorflow.python.training import slot_creator as slot_creator
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export

def get_filtered_grad_fn(grad_fn): ...

class _OptimizableVariable(metaclass=abc.ABCMeta):
    """Interface for abstracting over variables in the optimizers."""
    @abc.abstractmethod
    def target(self):
        """Returns the optimization target for this variable."""
    @abc.abstractmethod
    def update_op(self, optimizer, g):
        """Returns the update ops for updating the variable."""

class _RefVariableProcessor(_OptimizableVariable):
    """Processor for Variable."""
    def __init__(self, v) -> None: ...
    def target(self): ...
    def update_op(self, optimizer, g): ...

class _DenseReadResourceVariableProcessor(_OptimizableVariable):
    """Processor for dense ResourceVariables."""
    def __init__(self, v) -> None: ...
    def target(self): ...
    def update_op(self, optimizer, g): ...

class _DenseResourceVariableProcessor(_OptimizableVariable):
    """Processor for dense ResourceVariables."""
    def __init__(self, v) -> None: ...
    def target(self): ...
    def update_op(self, optimizer, g): ...

class _TensorProcessor(_OptimizableVariable):
    """Processor for ordinary Tensors.

  Even though a Tensor can't really be updated, sometimes it is useful to
  compute the gradients with respect to a Tensor using the optimizer. Updating
  the Tensor is, of course, unsupported.
  """
    def __init__(self, v) -> None: ...
    def target(self): ...
    def update_op(self, optimizer, g) -> None: ...

class Optimizer(trackable.Trackable):
    '''Base class for optimizers.

  This class defines the API to add Ops to train a model.  You never use this
  class directly, but instead instantiate one of its subclasses such as
  `GradientDescentOptimizer`, `AdagradOptimizer`, or `MomentumOptimizer`.

  ### Usage

  ```python
  # Create an optimizer with the desired parameters.
  opt = GradientDescentOptimizer(learning_rate=0.1)
  # Add Ops to the graph to minimize a cost by updating a list of variables.
  # "cost" is a Tensor, and the list of variables contains tf.Variable
  # objects.
  opt_op = opt.minimize(cost, var_list=<list of variables>)
  ```

  In the training program you will just have to run the returned Op.

  ```python
  # Execute opt_op to do one step of training:
  opt_op.run()
  ```

  ### Processing gradients before applying them.

  Calling `minimize()` takes care of both computing the gradients and
  applying them to the variables.  If you want to process the gradients
  before applying them you can instead use the optimizer in three steps:

  1.  Compute the gradients with `compute_gradients()`.
  2.  Process the gradients as you wish.
  3.  Apply the processed gradients with `apply_gradients()`.

  Example:

  ```python
  # Create an optimizer.
  opt = GradientDescentOptimizer(learning_rate=0.1)

  # Compute the gradients for a list of variables.
  grads_and_vars = opt.compute_gradients(loss, <list of variables>)

  # grads_and_vars is a list of tuples (gradient, variable).  Do whatever you
  # need to the \'gradient\' part, for example cap them, etc.
  capped_grads_and_vars = [(MyCapper(gv[0]), gv[1]) for gv in grads_and_vars]

  # Ask the optimizer to apply the capped gradients.
  opt.apply_gradients(capped_grads_and_vars)
  ```

  ### Gating Gradients

  Both `minimize()` and `compute_gradients()` accept a `gate_gradients`
  argument that controls the degree of parallelism during the application of
  the gradients.

  The possible values are: `GATE_NONE`, `GATE_OP`, and `GATE_GRAPH`.

  <b>`GATE_NONE`</b>: Compute and apply gradients in parallel.  This provides
  the maximum parallelism in execution, at the cost of some non-reproducibility
  in the results.  For example the two gradients of `matmul` depend on the input
  values: With `GATE_NONE` one of the gradients could be applied to one of the
  inputs _before_ the other gradient is computed resulting in non-reproducible
  results.

  <b>`GATE_OP`</b>: For each Op, make sure all gradients are computed before
  they are used.  This prevents race conditions for Ops that generate gradients
  for multiple inputs where the gradients depend on the inputs.

  <b>`GATE_GRAPH`</b>: Make sure all gradients for all variables are computed
  before any one of them is used.  This provides the least parallelism but can
  be useful if you want to process all gradients before applying any of them.

  ### Slots

  Some optimizer subclasses, such as `MomentumOptimizer` and `AdagradOptimizer`
  allocate and manage additional variables associated with the variables to
  train.  These are called <i>Slots</i>.  Slots have names and you can ask the
  optimizer for the names of the slots that it uses.  Once you have a slot name
  you can ask the optimizer for the variable it created to hold the slot value.

  This can be useful if you want to log debug a training algorithm, report stats
  about the slots, etc.

  @compatibility(TF2)
  `tf.compat.v1.train.Optimizer` can be used in eager mode and `tf.function`,
  but it is not recommended. Please use the subclasses of
  `tf.keras.optimizers.Optimizer` instead in TF2. Please see [Basic training
  loops](https://www.tensorflow.org/guide/basic_training_loops) or
  [Writing a training loop from scratch]
  (https://www.tensorflow.org/guide/keras/writing_a_training_loop_from_scratch)
  for examples.

  If your TF1 code contains a `tf.compat.v1.train.Optimizer` symbol, whether it
  is used with or without a `tf.estimator.Estimator`, you cannot simply replace
  that with the corresponding `tf.keras.optimizers.Optimizer`s. To migrate to
  TF2, it is advised the whole training program used with `Estimator` to be
  migrated to Keras `Model.fit` based or TF2 custom training loops.

  #### Structural Mapping to Native TF2

  Before:

  ```python
  sgd_op = tf.compat.v1.train.GradientDescentOptimizer(3.0)
  opt_op = sgd_op.minimize(cost, global_step, [var0, var1])
  opt_op.run(session=session)
  ```

  After:

  ```python
  sgd = tf.keras.optimizers.SGD(3.0)
  sgd.minimize(cost_fn, [var0, var1])
  ```

  #### How to Map Arguments

  | TF1 Arg Name          | TF2 Arg Name    | Note                       |
  | :-------------------- | :-------------- | :------------------------- |
  | `use_locking`         | Not supported   | -                          |
  | `name`                | `name. `        | -                          |

  #### Before & After Usage Example

  Before:

  >>> g = tf.compat.v1.Graph()
  >>> with g.as_default():
  ...   var0 = tf.compat.v1.Variable([1.0, 2.0])
  ...   var1 = tf.compat.v1.Variable([3.0, 4.0])
  ...   cost = 5 * var0 + 3 * var1
  ...   global_step = tf.compat.v1.Variable(
  ...       tf.compat.v1.zeros([], tf.compat.v1.int64), name=\'global_step\')
  ...   init_op = tf.compat.v1.initialize_all_variables()
  ...   sgd_op = tf.compat.v1.train.GradientDescentOptimizer(3.0)
  ...   opt_op = sgd_op.minimize(cost, global_step, [var0, var1])
  >>> session = tf.compat.v1.Session(graph=g)
  >>> session.run(init_op)
  >>> opt_op.run(session=session)
  >>> print(session.run(var0))
  [-14. -13.]


  After:
  >>> var0 = tf.Variable([1.0, 2.0])
  >>> var1 = tf.Variable([3.0, 4.0])
  >>> cost_fn = lambda: 5 * var0 + 3 * var1
  >>> sgd = tf.keras.optimizers.SGD(3.0)
  >>> sgd.minimize(cost_fn, [var0, var1])
  >>> print(var0.numpy())
  [-14. -13.]

  @end_compatibility


  '''
    GATE_NONE: int
    GATE_OP: int
    GATE_GRAPH: int
    def __init__(self, use_locking, name) -> None:
        """Create a new Optimizer.

    This must be called by the constructors of subclasses.

    Args:
      use_locking: Bool. If True apply use locks to prevent concurrent updates
        to variables.
      name: A non-empty string.  The name to use for accumulators created
        for the optimizer.

    Raises:
      ValueError: If name is malformed.
    """
    def get_name(self): ...
    def minimize(self, loss, global_step: Incomplete | None = None, var_list: Incomplete | None = None, gate_gradients=..., aggregation_method: Incomplete | None = None, colocate_gradients_with_ops: bool = False, name: Incomplete | None = None, grad_loss: Incomplete | None = None):
        """Add operations to minimize `loss` by updating `var_list`.

    This method simply combines calls `compute_gradients()` and
    `apply_gradients()`. If you want to process the gradient before applying
    them call `compute_gradients()` and `apply_gradients()` explicitly instead
    of using this function.

    Args:
      loss: A `Tensor` containing the value to minimize.
      global_step: Optional `Variable` to increment by one after the
        variables have been updated.
      var_list: Optional list or tuple of `Variable` objects to update to
        minimize `loss`.  Defaults to the list of variables collected in
        the graph under the key `GraphKeys.TRAINABLE_VARIABLES`.
      gate_gradients: How to gate the computation of gradients.  Can be
        `GATE_NONE`, `GATE_OP`, or  `GATE_GRAPH`.
      aggregation_method: Specifies the method used to combine gradient terms.
        Valid values are defined in the class `AggregationMethod`.
      colocate_gradients_with_ops: If True, try colocating gradients with
        the corresponding op.
      name: Optional name for the returned operation.
      grad_loss: Optional. A `Tensor` holding the gradient computed for `loss`.

    Returns:
      An Operation that updates the variables in `var_list`.  If `global_step`
      was not `None`, that operation also increments `global_step`.

    Raises:
      ValueError: If some of the variables are not `Variable` objects.

    @compatibility(eager)
    When eager execution is enabled, `loss` should be a Python function that
    takes no arguments and computes the value to be minimized. Minimization (and
    gradient computation) is done with respect to the elements of `var_list` if
    not None, else with respect to any trainable variables created during the
    execution of the `loss` function. `gate_gradients`, `aggregation_method`,
    `colocate_gradients_with_ops` and `grad_loss` are ignored when eager
    execution is enabled.
    @end_compatibility
    """
    def compute_gradients(self, loss, var_list: Incomplete | None = None, gate_gradients=..., aggregation_method: Incomplete | None = None, colocate_gradients_with_ops: bool = False, grad_loss: Incomplete | None = None):
        '''Compute gradients of `loss` for the variables in `var_list`.

    This is the first part of `minimize()`.  It returns a list
    of (gradient, variable) pairs where "gradient" is the gradient
    for "variable".  Note that "gradient" can be a `Tensor`, an
    `IndexedSlices`, or `None` if there is no gradient for the
    given variable.

    @compatibility(TF2)
    `tf.keras.optimizers.Optimizer` in TF2 does not provide a
    `compute_gradients` method, and you should use a `tf.GradientTape` to
    obtain the gradients:

    ```python
    @tf.function
    def train step(inputs):
      batch_data, labels = inputs
      with tf.GradientTape() as tape:
        predictions = model(batch_data, training=True)
        loss = tf.keras.losses.CategoricalCrossentropy(
            reduction=tf.keras.losses.Reduction.NONE)(labels, predictions)
      gradients = tape.gradient(loss, model.trainable_variables)
      optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    ```

    Args:
      loss: A Tensor containing the value to minimize or a callable taking
        no arguments which returns the value to minimize. When eager execution
        is enabled it must be a callable.
      var_list: Optional list or tuple of `tf.Variable` to update to minimize
        `loss`.  Defaults to the list of variables collected in the graph
        under the key `GraphKeys.TRAINABLE_VARIABLES`.
      gate_gradients: How to gate the computation of gradients.  Can be
        `GATE_NONE`, `GATE_OP`, or `GATE_GRAPH`.
      aggregation_method: Specifies the method used to combine gradient terms.
        Valid values are defined in the class `AggregationMethod`.
      colocate_gradients_with_ops: If True, try colocating gradients with
        the corresponding op.
      grad_loss: Optional. A `Tensor` holding the gradient computed for `loss`.

    Returns:
      A list of (gradient, variable) pairs. Variable is always present, but
      gradient can be `None`.

    Raises:
      TypeError: If `var_list` contains anything else than `Variable` objects.
      ValueError: If some arguments are invalid.
      RuntimeError: If called with eager execution enabled and `loss` is
        not callable.

    @compatibility(eager)
    When eager execution is enabled, `gate_gradients`, `aggregation_method`,
    and `colocate_gradients_with_ops` are ignored.
    @end_compatibility
    '''
    def apply_gradients(self, grads_and_vars, global_step: Incomplete | None = None, name: Incomplete | None = None):
        """Apply gradients to variables.

    This is the second part of `minimize()`. It returns an `Operation` that
    applies gradients.

    @compatibility(TF2)
    #### How to Map Arguments

    | TF1 Arg Name          | TF2 Arg Name    | Note                       |
    | :-------------------- | :-------------- | :------------------------- |
    | `grads_and_vars`      | `grads_and_vars`| -                          |
    | `global_step`         | Not supported.  | Use `optimizer.iterations` |
    | `name`                | `name. `        | -                          |

    Args:
      grads_and_vars: List of (gradient, variable) pairs as returned by
        `compute_gradients()`.
      global_step: Optional `Variable` to increment by one after the
        variables have been updated.
      name: Optional name for the returned operation.  Default to the
        name passed to the `Optimizer` constructor.

    Returns:
      An `Operation` that applies the specified gradients. If `global_step`
      was not None, that operation also increments `global_step`.

    Raises:
      TypeError: If `grads_and_vars` is malformed.
      ValueError: If none of the variables have gradients.
      RuntimeError: If you should use `_distributed_apply()` instead.
    """
    def get_slot(self, var, name):
        """Return a slot named `name` created for `var` by the Optimizer.

    Some `Optimizer` subclasses use additional variables.  For example
    `Momentum` and `Adagrad` use variables to accumulate updates.  This method
    gives access to these `Variable` objects if for some reason you need them.

    Use `get_slot_names()` to get the list of slot names created by the
    `Optimizer`.

    Args:
      var: A variable passed to `minimize()` or `apply_gradients()`.
      name: A string.

    Returns:
      The `Variable` for the slot if it was created, `None` otherwise.
    """
    def get_slot_names(self):
        """Return a list of the names of slots created by the `Optimizer`.

    See `get_slot()`.

    Returns:
      A list of strings.
    """
    def variables(self):
        """A list of variables which encode the current state of `Optimizer`.

    Includes slot variables and additional global variables created by the
    optimizer in the current default graph.

    Returns:
      A list of variables.
    """
