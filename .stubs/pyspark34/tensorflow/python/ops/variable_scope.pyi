import enum
import threading
from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.ops import variables
from tensorflow.python.types import core

__all__ = ['AUTO_REUSE', 'VariableScope', 'get_variable_scope', 'get_variable', 'get_local_variable', 'variable_scope', 'variable_op_scope', 'no_regularizer', 'VariableSynchronization', 'VariableAggregation']

class _PartitionInfo:
    """Holds partition info used by initializer functions."""
    def __init__(self, full_shape, var_offset) -> None:
        """Constructor.

    Args:
      full_shape: Tuple or list of `int` indicating the full combined shape of
        the partitioned variables.
      var_offset: Tuple or list of `int` specifying offset of this partition
        with respect to the full variable for each dimension.

    Raises:
      TypeError: If `full_shape` or `var_offset` is not a sequence.
      ValueError: If `full_shape` or `var_offset` differ in length. If
        `var_offset` exceeds `full_shape` in any dimension.
    """
    @property
    def full_shape(self): ...
    @property
    def var_offset(self): ...
    def single_offset(self, shape):
        """Returns the offset when the variable is partitioned in at most one dim.

    Args:
      shape: Tuple or list of `int` indicating the shape of one specific
        variable partition.

    Returns:
      `int` representing the offset in the dimension along which the variable is
       partitioned. Returns 0 if the variable is not being partitioned.

    Raises:
      ValueError: Depending on self.single_slice_dim().
    """
    def single_slice_dim(self, shape):
        """Returns the slice dim when the variable is partitioned only in one dim.

    Args:
      shape: Tuple or list of `int` indicating the shape of one specific
        variable partition.

    Returns:
      `int` representing the dimension that the variable is partitioned in, or
      `None` if the variable doesn't seem to be partitioned at all.

    Raises:
      TypeError: If `shape` is not a sequence.
      ValueError: If `shape` is not the same length as `self.full_shape`. If
        the variable is partitioned in more than one dimension.
    """

class _ReuseMode(enum.Enum):
    """Mode for variable access within a variable scope."""
    AUTO_REUSE: int
VariableSynchronization = variables.VariableSynchronization
VariableAggregation = variables.VariableAggregation
AUTO_REUSE: Incomplete

class _VariableStore:
    """Variable store that carries a number of named Variables.

  New variable names and new variables can be created; all stored
  variables are initialized with the initializer passed to __init__.

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

class _LazyEvalTensor(core.Tensor):
    """A Tensor-like object that only evaluates its thunk when used."""
    def __init__(self, thunk) -> None:
        """Initializes a _LazyEvalTensor object.

    Args:
      thunk: A callable. A thunk which computes the value of the tensor.
    """

def no_regularizer(_) -> None:
    """Use this function to prevent regularization of variables."""

class VariableScope:
    """Variable scope object to carry defaults to provide to `get_variable`.

  Many of the arguments we need for `get_variable` in a variable store are most
  easily handled with a context. This object is used for the defaults.

  Attributes:
    name: name of the current scope, used as prefix in get_variable.
    initializer: default initializer passed to get_variable.
    regularizer: default regularizer passed to get_variable.
    reuse: Boolean, None, or tf.compat.v1.AUTO_REUSE, setting the reuse in
      get_variable. When eager execution is enabled this argument is always
      forced to be False.
    caching_device: string, callable, or None: the caching device passed to
      get_variable.
    partitioner: callable or `None`: the partitioner passed to `get_variable`.
    custom_getter: default custom getter passed to get_variable.
    name_scope: The name passed to `tf.name_scope`.
    dtype: default type passed to get_variable (defaults to DT_FLOAT).
    use_resource: if False, create a normal Variable; if True create an
      experimental ResourceVariable with well-defined semantics. Defaults to
      False (will later change to True). When eager execution is enabled this
      argument is always forced to be True.
    constraint: An optional projection function to be applied to the variable
      after being updated by an `Optimizer` (e.g. used to implement norm
      constraints or value constraints for layer weights). The function must
      take as input the unprojected Tensor representing the value of the
      variable and return the Tensor for the projected value (which must have
      the same shape). Constraints are not safe to use when doing asynchronous
      distributed training.
  """
    def __init__(self, reuse, name: str = '', initializer: Incomplete | None = None, regularizer: Incomplete | None = None, caching_device: Incomplete | None = None, partitioner: Incomplete | None = None, custom_getter: Incomplete | None = None, name_scope: str = '', dtype=..., use_resource: Incomplete | None = None, constraint: Incomplete | None = None) -> None:
        """Creates a new VariableScope with the given properties."""
    @property
    def name(self): ...
    @property
    def original_name_scope(self): ...
    @property
    def reuse(self): ...
    @property
    def initializer(self): ...
    @property
    def dtype(self): ...
    @property
    def use_resource(self): ...
    @property
    def regularizer(self): ...
    @property
    def caching_device(self): ...
    @property
    def partitioner(self): ...
    @property
    def custom_getter(self): ...
    @property
    def constraint(self): ...
    def reuse_variables(self) -> None:
        """Reuse variables in this scope."""
    def set_initializer(self, initializer) -> None:
        """Set initializer for this scope."""
    def set_dtype(self, dtype) -> None:
        """Set data type for this scope."""
    def set_use_resource(self, use_resource) -> None:
        """Sets whether to use ResourceVariables for this scope."""
    def set_regularizer(self, regularizer) -> None:
        """Set regularizer for this scope."""
    def set_caching_device(self, caching_device) -> None:
        """Set caching_device for this scope."""
    def set_partitioner(self, partitioner) -> None:
        """Set partitioner for this scope."""
    def set_custom_getter(self, custom_getter) -> None:
        """Set custom getter for this scope."""
    def get_collection(self, name):
        """Get this scope's variables."""
    def trainable_variables(self):
        """Get this scope's trainable variables."""
    def global_variables(self):
        """Get this scope's global variables."""
    def local_variables(self):
        """Get this scope's local variables."""
    def get_variable(self, var_store, name, shape: Incomplete | None = None, dtype: Incomplete | None = None, initializer: Incomplete | None = None, regularizer: Incomplete | None = None, reuse: Incomplete | None = None, trainable: Incomplete | None = None, collections: Incomplete | None = None, caching_device: Incomplete | None = None, partitioner: Incomplete | None = None, validate_shape: bool = True, use_resource: Incomplete | None = None, custom_getter: Incomplete | None = None, constraint: Incomplete | None = None, synchronization=..., aggregation=...):
        """Gets an existing variable with this name or create a new one."""

class _VariableScopeStore(threading.local):
    """A thread local store for the current variable scope and scope counts."""
    current_scope: Incomplete
    variable_scopes_count: Incomplete
    def __init__(self) -> None: ...
    def open_variable_scope(self, scope_name) -> None: ...
    def close_variable_subscopes(self, scope_name) -> None: ...
    def variable_scope_count(self, scope_name): ...

def get_variable_scope():
    """Returns the current variable scope.

  @compatibility(TF2)
  Although it is a legacy `compat.v1` api,
  `tf.compat.v1.get_variable` is compatible with eager
  execution and `tf.function`

  However, to maintain variable-scope based variable reuse
  you will need to combine it with
  `tf.compat.v1.keras.utils.track_tf1_style_variables`. (Though
  it will behave as if reuse is always set to `tf.compat.v1.AUTO_REUSE`.)

  See the
  [migration guide](https://www.tensorflow.org/guide/migrate/model_mapping)
  for more info.

  The TF2 equivalent, if you are just trying to track
  variable name prefixes and not control `get_variable`-based variable reuse,
  would be to use `tf.name_scope` and capture the output of opening the
  scope (which represents the current name prefix).

  For example:
  ```python
  x = tf.name_scope('foo') as current_scope:
    ...
  ```
  @end_compatibility
  """

class EagerVariableStore:
    '''Wrapper allowing functional layers to be used with eager execution.

  When eager execution is enabled Variables get deleted when they go out of
  scope, and are not stored in global collections by default. A lot of code
  (mostly the functional layers in tf.layers) assumes that variables are kept in
  a global list.

  EagerVariableStore can be used in conjunction with this code to make it
  eager-friendly. For example, to create a dense layer, use:

  ```
    container = tfe.EagerVariableStore()
    for input in dataset_iterator:
      with container.as_default():
        x = tf.compat.v1.layers.dense(input, name="l1")
    print(container.variables)  # Should print the variables used in the layer.
  ```
  '''
    def __init__(self, store: Incomplete | None = None) -> None: ...
    def as_default(self): ...
    def variables(self): ...
    def trainable_variables(self): ...
    def non_trainable_variables(self): ...
    def copy(self):
        """Copy this variable store and all of its contents.

    Variables contained in this store will be copied over to the new variable
    store, meaning that they can be modified without affecting the variables in
    this store.

    Returns:
      A new EagerVariableStore instance containing copied variables.
    """

def get_variable(name, shape: Incomplete | None = None, dtype: Incomplete | None = None, initializer: Incomplete | None = None, regularizer: Incomplete | None = None, trainable: Incomplete | None = None, collections: Incomplete | None = None, caching_device: Incomplete | None = None, partitioner: Incomplete | None = None, validate_shape: bool = True, use_resource: Incomplete | None = None, custom_getter: Incomplete | None = None, constraint: Incomplete | None = None, synchronization=..., aggregation=...): ...
def get_local_variable(name, shape: Incomplete | None = None, dtype: Incomplete | None = None, initializer: Incomplete | None = None, regularizer: Incomplete | None = None, trainable: bool = False, collections: Incomplete | None = None, caching_device: Incomplete | None = None, partitioner: Incomplete | None = None, validate_shape: bool = True, use_resource: Incomplete | None = None, custom_getter: Incomplete | None = None, constraint: Incomplete | None = None, synchronization=..., aggregation=...): ...

class _pure_variable_scope:
    """A context for the variable_scope, see `variable_scope` for docs."""
    def __init__(self, name_or_scope, reuse: Incomplete | None = None, initializer: Incomplete | None = None, regularizer: Incomplete | None = None, caching_device: Incomplete | None = None, partitioner: Incomplete | None = None, custom_getter: Incomplete | None = None, old_name_scope: Incomplete | None = None, dtype=..., use_resource: Incomplete | None = None, constraint: Incomplete | None = None) -> None:
        """Creates a context for the variable_scope, see `variable_scope` for docs.

    Note: this does not create a name scope.

    Args:
      name_or_scope: `string` or `VariableScope`: the scope to open.
      reuse: `True` or None, or tf.compat.v1.AUTO_REUSE; if `None`, we inherit
        the parent scope's reuse flag.
      initializer: default initializer for variables within this scope.
      regularizer: default regularizer for variables within this scope.
      caching_device: default caching device for variables within this scope.
      partitioner: default partitioner for variables within this scope.
      custom_getter: default custom getter for variables within this scope.
      old_name_scope: the original name scope when re-entering a variable scope.
      dtype: type of the variables within this scope (defaults to `DT_FLOAT`).
      use_resource: If False, variables in this scope will be regular Variables.
        If True, experimental ResourceVariables will be creates instead, with
        well-defined semantics. Defaults to False (will later change to True).
      constraint: An optional projection function to be applied to the variable
        after being updated by an `Optimizer` (e.g. used to implement norm
        constraints or value constraints for layer weights). The function must
        take as input the unprojected Tensor representing the value of the
        variable and return the Tensor for the projected value (which must have
        the same shape). Constraints are not safe to use when doing asynchronous
        distributed training.
    """
    def __enter__(self):
        """Begins the scope block.

    Returns:
      A VariableScope.
    Raises:
      ValueError: when trying to reuse within a create scope, or create within
        a reuse scope, or if reuse is not `None` or `True`.
      TypeError: when the types of some arguments are not appropriate.
    """
    def __exit__(self, type_arg: type[BaseException] | None, value_arg: BaseException | None, traceback_arg: types.TracebackType | None) -> None: ...

class variable_scope:
    '''A context manager for defining ops that creates variables (layers).

  @compatibility(TF2)
  Although it is a legacy `compat.v1` api,
  `tf.compat.v1.variable_scope` is mostly compatible with eager
  execution and `tf.function` as long as you combine it with the
  `tf.compat.v1.keras.utils.track_tf1_style_variables` decorator (though
  it will behave as if reuse is always set to `AUTO_REUSE`.)

  See the
  [model migration guide](
      https://www.tensorflow.org/guide/migrate/model_mapping)
  for more info on
  migrating code that relies on `variable_scope`-based variable reuse.

  When you use it with eager execution enabled but without
  `tf.compat.v1.keras.utils.track_tf1_style_variables`,
  `tf.compat.v1.variable_scope` will still be able to prefix the names
  of variables created within the scope but it will not enable variable reuse
  or error-raising checks around variable reuse (`get_variable` calls within
  it would always create new variables).

  Once you have switched away from `get_variable`-based variable reuse
  mechanisms, to switch to TF2 APIs you can just use
  `tf.name_scope` to prefix variable names.
  @end_compatibility

  This context manager validates that the (optional) `values` are from the same
  graph, ensures that graph is the default graph, and pushes a name scope and a
  variable scope.

  If `name_or_scope` is not None, it is used as is. If `name_or_scope` is None,
  then `default_name` is used.  In that case, if the same name has been
  previously used in the same scope, it will be made unique by appending `_N`
  to it.

  Variable scope allows you to create new variables and to share already created
  ones while providing checks to not create or share by accident. For details,
  see the [Variable Scope How To](https://tensorflow.org/guide/variables), here
  we present only a few basic examples.

  The Variable Scope works as expected when the Eager Execution is Disabled.

  ```python
  tf.compat.v1.disable_eager_execution()
  ```

  Simple example of how to create a new variable:

  ```python
  with tf.compat.v1.variable_scope("foo"):
      with tf.compat.v1.variable_scope("bar"):
          v = tf.compat.v1.get_variable("v", [1])
          assert v.name == "foo/bar/v:0"
  ```

  Simple example of how to reenter a premade variable scope safely:

  ```python
  with tf.compat.v1.variable_scope("foo") as vs:
    pass

  # Re-enter the variable scope.
  with tf.compat.v1.variable_scope(vs,
                         auxiliary_name_scope=False) as vs1:
    # Restore the original name_scope.
    with tf.name_scope(vs1.original_name_scope):
        v = tf.compat.v1.get_variable("v", [1])
        assert v.name == "foo/v:0"
        c = tf.constant([1], name="c")
        assert c.name == "foo/c:0"
  ```

  Keep in mind that the counters for `default_name` are discarded once the
  parent scope is exited. Therefore when the code re-enters the scope (for
  instance by saving it), all nested default_name counters will be restarted.

  For instance:

  ```python
  with tf.compat.v1.variable_scope("foo") as vs:
    with tf.compat.v1.variable_scope(None, default_name="bar"):
      v = tf.compat.v1.get_variable("a", [1])
      assert v.name == "foo/bar/a:0", v.name
    with tf.compat.v1.variable_scope(None, default_name="bar"):
      v = tf.compat.v1.get_variable("b", [1])
      assert v.name == "foo/bar_1/b:0"

  with tf.compat.v1.variable_scope(vs):
    with tf.compat.v1.variable_scope(None, default_name="bar"):
      v = tf.compat.v1.get_variable("c", [1])
      assert v.name == "foo/bar/c:0"   # Uses bar instead of bar_2!
  ```

  Basic example of sharing a variable AUTO_REUSE:

  ```python
  def foo():
    with tf.compat.v1.variable_scope("foo", reuse=tf.compat.v1.AUTO_REUSE):
      v = tf.compat.v1.get_variable("v", [1])
    return v

  v1 = foo()  # Creates v.
  v2 = foo()  # Gets the same, existing v.
  assert v1 == v2
  ```

  Basic example of sharing a variable with reuse=True:

  ```python
  with tf.compat.v1.variable_scope("foo"):
      v = tf.compat.v1.get_variable("v", [1])
  with tf.compat.v1.variable_scope("foo", reuse=True):
      v1 = tf.compat.v1.get_variable("v", [1])
  assert v1 == v
  ```

  Sharing a variable by capturing a scope and setting reuse:

  ```python
  with tf.compat.v1.variable_scope("foo") as scope:
      v = tf.compat.v1.get_variable("v", [1])
      scope.reuse_variables()
      v1 = tf.compat.v1.get_variable("v", [1])
  assert v1 == v
  ```

  To prevent accidental sharing of variables, we raise an exception when getting
  an existing variable in a non-reusing scope.

  ```python
  with tf.compat.v1.variable_scope("foo"):
      v = tf.compat.v1.get_variable("v", [1])
      v1 = tf.compat.v1.get_variable("v", [1])
      #  Raises ValueError("... v already exists ...").
  ```

  Similarly, we raise an exception when trying to get a variable that does not
  exist in reuse mode.

  ```python
  with tf.compat.v1.variable_scope("foo", reuse=True):
      v = tf.compat.v1.get_variable("v", [1])
      #  Raises ValueError("... v does not exists ...").
  ```

  Note that the `reuse` flag is inherited: if we open a reusing scope, then all
  its sub-scopes become reusing as well.

  A note about name scoping: Setting `reuse` does not impact the naming of other
  ops such as mult. See related discussion on
  [github#6189](https://github.com/tensorflow/tensorflow/issues/6189)

  Note that up to and including version 1.0, it was allowed (though explicitly
  discouraged) to pass False to the reuse argument, yielding undocumented
  behaviour slightly different from None. Starting at 1.1.0 passing None and
  False as reuse has exactly the same effect.

  A note about using variable scopes in multi-threaded environment: Variable
  scopes are thread local, so one thread will not see another thread\'s current
  scope. Also, when using `default_name`, unique scopes names are also generated
  only on a per thread basis. If the same name was used within a different
  thread, that doesn\'t prevent a new thread from creating the same scope.
  However, the underlying variable store is shared across threads (within the
  same graph). As such, if another thread tries to create a new variable with
  the same name as a variable created by a previous thread, it will fail unless
  reuse is True.

  Further, each thread starts with an empty variable scope. So if you wish to
  preserve name prefixes from a scope from the main thread, you should capture
  the main thread\'s scope and re-enter it in each thread. For e.g.

  ```
  main_thread_scope = variable_scope.get_variable_scope()

  # Thread\'s target function:
  def thread_target_fn(captured_scope):
    with variable_scope.variable_scope(captured_scope):
      # .... regular code for this thread


  thread = threading.Thread(target=thread_target_fn, args=(main_thread_scope,))
  ```
  '''
    def __init__(self, name_or_scope, default_name: Incomplete | None = None, values: Incomplete | None = None, initializer: Incomplete | None = None, regularizer: Incomplete | None = None, caching_device: Incomplete | None = None, partitioner: Incomplete | None = None, custom_getter: Incomplete | None = None, reuse: Incomplete | None = None, dtype: Incomplete | None = None, use_resource: Incomplete | None = None, constraint: Incomplete | None = None, auxiliary_name_scope: bool = True) -> None:
        """Initialize the context manager.

    Args:
      name_or_scope: `string` or `VariableScope`: the scope to open.
      default_name: The default name to use if the `name_or_scope` argument is
        `None`, this name will be uniquified. If name_or_scope is provided it
        won't be used and therefore it is not required and can be None.
      values: The list of `Tensor` arguments that are passed to the op function.
      initializer: default initializer for variables within this scope.
      regularizer: default regularizer for variables within this scope.
      caching_device: default caching device for variables within this scope.
      partitioner: default partitioner for variables within this scope.
      custom_getter: default custom getter for variables within this scope.
      reuse: `True`, None, or tf.compat.v1.AUTO_REUSE; if `True`, we go into
        reuse mode for this scope as well as all sub-scopes; if
        tf.compat.v1.AUTO_REUSE, we create variables if they do not exist, and
        return them otherwise; if None, we inherit the parent scope's reuse
        flag. When eager execution is enabled, new variables are always created
        unless an EagerVariableStore or template is currently active.
      dtype: type of variables created in this scope (defaults to the type in
        the passed scope, or inherited from parent scope).
      use_resource: If False, all variables will be regular Variables. If True,
        experimental ResourceVariables with well-defined semantics will be used
        instead. Defaults to False (will later change to True). When eager
        execution is enabled this argument is always forced to be True.
      constraint: An optional projection function to be applied to the variable
        after being updated by an `Optimizer` (e.g. used to implement norm
        constraints or value constraints for layer weights). The function must
        take as input the unprojected Tensor representing the value of the
        variable and return the Tensor for the projected value (which must have
        the same shape). Constraints are not safe to use when doing asynchronous
        distributed training.
      auxiliary_name_scope: If `True`, we create an auxiliary name scope with
        the scope. If `False`, we don't create it. Note that the argument is not
        inherited, and it only takes effect for once when creating. You should
        only use it for re-entering a premade variable scope.

    Returns:
      A scope that can be captured and reused.

    Raises:
      ValueError: when trying to reuse within a create scope, or create within
        a reuse scope.
      TypeError: when the types of some arguments are not appropriate.
    """
    def __enter__(self): ...
    def __exit__(self, type_arg: type[BaseException] | None, value_arg: BaseException | None, traceback_arg: types.TracebackType | None) -> None: ...

def variable_op_scope(values, name_or_scope, default_name: Incomplete | None = None, initializer: Incomplete | None = None, regularizer: Incomplete | None = None, caching_device: Incomplete | None = None, partitioner: Incomplete | None = None, custom_getter: Incomplete | None = None, reuse: Incomplete | None = None, dtype: Incomplete | None = None, use_resource: Incomplete | None = None, constraint: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """Deprecated: context manager for defining an op that creates variables."""
variable = variables.VariableV1
