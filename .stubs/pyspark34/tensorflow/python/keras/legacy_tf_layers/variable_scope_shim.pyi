from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.keras.engine import base_layer as base_layer
from tensorflow.python.keras.utils import tf_contextlib as tf_contextlib, tf_inspect as tf_inspect
from tensorflow.python.module import module as module
from tensorflow.python.ops import init_ops as init_ops, variables as variables
from tensorflow.python.util import tf_decorator as tf_decorator

def as_shape(shape):
    """Converts the given object to a TensorShape."""
def fn_args(fn):
    """Get argument names for function-like object.

  Args:
    fn: Function, or function-like object (e.g., result of `functools.partial`).

  Returns:
    `tuple` of string argument names.

  Raises:
    ValueError: if partial function has positionally bound arguments
  """
def validate_synchronization_aggregation_trainable(synchronization, aggregation, trainable, name):
    """Given user-provided variable properties, sets defaults and validates."""

class _EagerVariableStore:
    """TF2-compatible VariableStore that avoids collections & tracks regularizers.

  New variable names and new variables can be created; all stored
  variables are initialized with the initializer passed to __init__.

  All variables get created in `tf.init_scope.` to avoid a bad
  interaction between `tf.function` `FuncGraph` internals, Keras
  Functional Models, and TPUStrategy variable initialization.

  Attributes:
    vars: a dictionary with string names (same as passed in GetVar) as keys and
      the corresponding TensorFlow Variables as values.
  """
    def __init__(self) -> None:
        """Create a variable store."""
    def get_variable(self, name, shape: Incomplete | None = None, dtype=..., initializer: Incomplete | None = None, regularizer: Incomplete | None = None, reuse: Incomplete | None = None, trainable: Incomplete | None = None, collections: Incomplete | None = None, caching_device: Incomplete | None = None, partitioner: Incomplete | None = None, validate_shape: bool = True, use_resource: Incomplete | None = None, custom_getter: Incomplete | None = None, constraint: Incomplete | None = None, synchronization=..., aggregation=...):
        """Gets an existing variable with these parameters or create a new one.

    If a variable with the given name is already stored, we return the stored
    variable. Otherwise, we create a new one.

    Set `reuse` to `True` when you only want to reuse existing Variables.
    Set `reuse` to `False` when you only want to create new Variables.
    Set `reuse` to None (the default) or tf.compat.v1.AUTO_REUSE when you want
    variables to be created if they don't exist or returned if they do.

    If initializer is `None` (the default), the default initializer passed in
    the constructor is used. If that one is `None` too, we use a new
    `glorot_uniform_initializer`. If initializer is a Tensor, we use
    it as a value and derive the shape from the initializer.

    If a partitioner is provided, a `PartitionedVariable` is returned.
    Accessing this object as a `Tensor` returns the shards concatenated along
    the partition axis.

    Some useful partitioners are available.  See, e.g.,
    `variable_axis_size_partitioner` and `min_max_variable_partitioner`.

    Args:
      name: The name of the new or existing variable.
      shape: Shape of the new or existing variable.
      dtype: Type of the new or existing variable (defaults to `DT_FLOAT`).
      initializer: Initializer for the variable.
      regularizer: A (Tensor -> Tensor or None) function; the result of applying
        it on a newly created variable will be added to the collection
        GraphKeys.REGULARIZATION_LOSSES and can be used for regularization.
      reuse: a Boolean, None, or tf.AUTO_REUSE. Controls reuse or creation of
        variables. When eager execution is enabled  this argument is always
        forced to be False.
      trainable: If `True` also add the variable to the graph collection
        `GraphKeys.TRAINABLE_VARIABLES` (see `tf.Variable`). `trainable`
        defaults to `True`, unless `synchronization` is set to `ON_READ`, in
        which case it defaults to `False`.
      collections: List of graph collections keys to add the `Variable` to.
        Defaults to `[GraphKeys.GLOBAL_VARIABLES]` (see `tf.Variable`).
      caching_device: Optional device string or function describing where the
        Variable should be cached for reading.  Defaults to the Variable's
        device.  If not `None`, caches on another device.  Typical use is to
        cache on the device where the Ops using the `Variable` reside, to
        deduplicate copying through `Switch` and other conditional statements.
      partitioner: Optional callable that accepts a fully defined `TensorShape`
        and dtype of the `Variable` to be created, and returns a list of
        partitions for each axis (currently only one axis can be partitioned).
      validate_shape: If False, allows the variable to be initialized with a
        value of unknown shape. If True, the default, the shape of initial_value
        must be known.
      use_resource: If False, creates a regular Variable. If True, creates
        instead an experimental ResourceVariable which has well-defined
        semantics. Defaults to False (will later change to True). When eager
        execution is enabled this argument is always forced to be true.
      custom_getter: Callable that takes as a first argument the true getter,
        and allows overwriting the internal get_variable method. The signature
        of `custom_getter` should match that of this method,
        but the most future-proof version will allow for changes: `def
          custom_getter(getter, *args, **kwargs)`.  Direct access to
        all `get_variable` parameters is also allowed: `def
          custom_getter(getter, name, *args, **kwargs)`.  A simple identity
        custom getter that simply creates variables with modified names is:
          ```python
        def custom_getter(getter, name, *args, **kwargs): return getter(name +
          '_suffix', *args, **kwargs) ```
      constraint: An optional projection function to be applied to the variable
        after being updated by an `Optimizer` (e.g. used to implement norm
        constraints or value constraints for layer weights). The function must
        take as input the unprojected Tensor representing the value of the
        variable and return the Tensor for the projected value (which must have
        the same shape). Constraints are not safe to use when doing asynchronous
        distributed training.
      synchronization: Indicates when a distributed a variable will be
        aggregated. Accepted values are constants defined in the class
        `tf.VariableSynchronization`. By default the synchronization is set to
        `AUTO` and the current `DistributionStrategy` chooses when to
        synchronize.
      aggregation: Indicates how a distributed variable will be aggregated.
        Accepted values are constants defined in the class
        `tf.VariableAggregation`.

    Returns:
      The created or existing `Variable` (or `PartitionedVariable`, if a
      partitioner was used).

    Raises:
      ValueError: when creating a new variable and shape is not declared,
        when reusing a variable and specifying a conflicting shape,
        or when violating reuse during variable creation.
      RuntimeError: when eager execution is enabled and not called from an
        EagerVariableStore.
    """
    def add_regularizer(self, var, regularizer) -> None: ...

class VariableAndLossTracker(module.Module):
    """Module that has a scope to capture vars/losses made by `get_variable`."""
    def __init__(self) -> None: ...
    def scope(self) -> Generator[None, None, None]: ...
    def get_regularization_losses(self): ...

class VariableScopeWrapperLayer(base_layer.Layer):
    '''Wrapper Layer to capture `compat.v1.get_variable` and `compat.v1.layers`.

  See go/tf2-migration-model-bookkeeping for background.

  This shim layer allows using large sets of TF1 model-forward-pass code as a
  Keras layer that works in TF2 with TF2 behaviors enabled. To use it,
  override this class and put your TF1 model\'s forward pass inside your
  implementation for `forward_pass`.

  Below are some examples, and then more details on the functionality of this
  shhim layer to wrap TF1 model forward passes.

  Example of capturing tf.compat.v1.layer-based modeling code as a Keras layer:

  ```python
  class WrappedDoubleDenseLayer(variable_scope_shim.VariableScopeWrapperLayer):

    def __init__(self, units, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.units = units

    def forward_pass(self, inputs, training=None):
      out = tf.compat.v1.layers.dense(
          inputs, self.units, name="dense_one",
          kernel_initializer=init_ops.ones_initializer(),
          kernel_regularizer="l2")
      with variable_scope.variable_scope("nested_scope"):
        out = tf.compat.v1.layers.dense(
            out, self.units, name="dense_two",
            kernel_initializer=init_ops.ones_initializer(),
            kernel_regularizer="l2")
      return out

  # Create a layer that can be used as a standard keras layer
  layer = WrappedDoubleDenseLayer(10)

  # call the layer on inputs
  layer(...)

  # Variables created/used within the scope will be tracked by the layer
  layer.weights
  layer.trainable_variables

  # Regularization losses will be captured in layer.losses after a call,
  # just like any other Keras layer
  reg_losses = layer.losses
  ```

  The solution is to wrap the model construction and execution in a keras-style
  scope:

  ```python
  class WrappedDoubleDenseLayer(variable_scope_shim.VariableScopeWrapperLayer):

    def __init__(self, units, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.units = units

    def forward_pass(self, inputs, training=None):
      out = inputs
      with tf.compat.v1.variable_scope("dense_one"):
        # The weights are created with a `regularizer`,
        # so the layer should track their regularization losses
        kernel = tf.compat.v1.get_variable(
            shape=[out.shape[-1], self.units],
            regularizer=regularizers.L2(),
            initializer=init_ops.ones_initializer(),
            name="kernel")
        bias = tf.compat.v1.get_variable(
            shape=[self.units,],
            initializer=init_ops.zeros_initializer(),
            name="bias")
        out = tf.compat.v1.math.matmul(out, kernel)
        out = tf.compat.v1.nn.bias_add(out, bias)
      with tf.compat.v1.variable_scope("nested_scope"):
        with tf.compat.v1.variable_scope("dense_two"):
          kernel = tf.compat.v1.get_variable(
              shape=[out.shape[-1], self.units],
              regularizer=regularizers.L2(),
              initializer=init_ops.ones_initializer(),
              name="kernel")
          bias = tf.compat.v1.get_variable(
              shape=[self.units,],
              initializer=init_ops.zeros_initializer(),
              name="bias")
          out = tf.compat.v1.math.matmul(out, kernel)
          out = tf.compat.v1.nn.bias_add(out, bias)
      return out

  # Create a layer that can be used as a standard keras layer
  layer = WrappedDoubleDenseLayer(10)

  # call the layer on inputs
  layer(...)

  # Variables created/used within the scope will be tracked by the layer
  layer.weights
  layer.trainable_variables

  # Regularization losses will be captured in layer.losses after a call,
  # just like any other Keras layer
  reg_losses = layer.losses
  ```

  Regularization losses:
    Any regularizers specified in the `get_variable` calls or `compat.v1.layer`
    creations will get captured by this wrapper layer. Regularization losses
    are accessible in `layer.losses` after a call just like in a standard
    Keras layer, and will be captured by any model that includes this layer.

  Variable scope / variable reuse:
    variable-scope based reuse in the `forward_pass` will be respected,
    and work like variable-scope based reuse in TF1.

  Variable Names/Pre-trained checkpoint loading:
    variable naming from get_variable and `compat.v1.layer` layers will match
    the TF1 names, so you should be able to re-use your old name-based
    checkpoints.

  Training Arg in `forward_pass`:
    Keras will pass a `training` arg to this layer similarly to how it
    passes `training` to other layers in TF2. See more details in the docs
    on `tf.keras.layers.Layer` to understand what will be passed and when.
    Note: tf.compat.v1.layers are usually not called with `training=None`,
    so the training arg to `forward_pass` might not feed through to them
    unless you pass it to their calls explicitly.

  Call signature of the forward pass:
    The semantics of the forward pass signature roughly match the standard
    Keras layer `call` signature, except that a `training` arg will *always*
    be passed, so your `forward_pass` must accept either.

  Limitations:
    * TF2 will not prune unused variable updates (or unused outputs). You may
      need to adjust your forward pass code to avoid computations or variable
      updates that you don\'t intend to use. (E.g. by adding a flag to the
      `forward_pass` call signature and branching on it).
    * Avoid Nesting variable creation in tf.function inside of `forward_pass`
      While the layer may safetely be used from inside a `tf.function`, using
      a function inside of `forward_pass` will break the variable scoping.
    * TBD: Nesting keras layers/models or other `VariableScopeWrapperLayer`s
      directly in `forward_pass` may not work correctly just yet.
      Support for this/instructions for how to do this is sill being worked on.

  Coming soon: A better guide, testing/verification guide.
  '''
    tracker: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def forward_pass(self, *args, **kwargs) -> None: ...
    def call(self, *args, **kwargs): ...
