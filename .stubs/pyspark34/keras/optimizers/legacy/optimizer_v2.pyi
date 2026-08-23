import abc
import tensorflow.compat.v2 as tf
from _typeshed import Incomplete
from keras import backend as backend, initializers as initializers
from keras.engine import base_layer_utils as base_layer_utils
from keras.optimizers.schedules import learning_rate_schedule as learning_rate_schedule
from keras.utils import generic_utils as generic_utils, layer_utils as layer_utils, tf_inspect as tf_inspect, tf_utils as tf_utils

keras_optimizers_gauge: Incomplete

class NullContextmanager:
    def __init__(self, *args, **kwargs) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type_arg: type[BaseException] | None, value_arg: BaseException | None, traceback_arg: types.TracebackType | None): ...

def name_scope_only_in_function_or_graph(name):
    """Internal-only entry point for `name_scope*`.

    Enters a compat.v1.name_scope only when in a function or graph,
    not when running fully eagerly.

    Args:
      name: The name argument that is passed to the op function.

    Returns:
      `name_scope*` context manager.
    """

class OptimizerV2(tf.__internal__.tracking.Trackable, metaclass=abc.ABCMeta):
    """Base class for legacy Keras optimizers.

    You should not use this class directly, but instead instantiate one of its
    subclasses such as `tf.keras.optimizers.legacy.SGD`,
    `tf.keras.optimizers.legacy.Adam`, etc.

    This is the default Keras optimizer base class until v2.10 (included).
    In v2.11 and later, `tf.keras.optimizers.Optimizer`
    points to a new base class implementation. The legacy class won't be
    deleted in the future and will continue to be available at
    `tf.keras.optimizers.legacy.Optimizer`.

    ### Usage

    ```python
    # Create an optimizer with the desired parameters.
    opt = tf.keras.optimizers.legacy.SGD(learning_rate=0.1)
    # `loss` is a callable that takes no argument and returns the value
    # to minimize.
    var1 = tf.Variable(2.0)
    var2 = tf.Variable(5.0)
    loss = lambda: 3 * var1 * var1 + 2 * var2 * var2
    # In graph mode, returns op that minimizes the loss by updating the listed
    # variables.
    opt_op = opt.minimize(loss, var_list=[var1, var2])
    opt_op.run()
    # In eager mode, simply call minimize to update the list of variables.
    opt.minimize(loss, var_list=[var1, var2])
    ```

    ### Usage in custom training loops

    In Keras models, sometimes variables are created when the model is first
    called, instead of construction time. Examples include 1) sequential models
    without input shape pre-defined, or 2) subclassed models. Pass var_list as
    callable in these cases.

    Example:

    ```python
    opt = tf.keras.optimizers.legacy.SGD(learning_rate=0.1)
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(num_hidden, activation='relu'))
    model.add(tf.keras.layers.Dense(num_classes, activation='sigmoid'))
    loss_fn = lambda: tf.keras.losses.mse(model(input), output)
    var_list_fn = lambda: model.trainable_weights
    for input, output in data:
      opt.minimize(loss_fn, var_list_fn)
    ```

    ### Processing gradients before applying them

    Calling `minimize()` takes care of both computing the gradients and
    applying them to the variables.  If you want to process the gradients
    before applying them you can instead use the optimizer in three steps:

    1.  Compute the gradients with `tf.GradientTape`.
    2.  Process the gradients as you wish.
    3.  Apply the processed gradients with `apply_gradients()`.

    Example:

    ```python
    # Create an optimizer.
    opt = tf.keras.optimizers.legacy.SGD(learning_rate=0.1)

    # Compute the gradients for a list of variables.
    with tf.GradientTape() as tape:
      loss = <call_loss_function>
    vars = <list_of_variables>
    grads = tape.gradient(loss, vars)

    # Process the gradients, for example cap them, etc.
    # capped_grads = [MyCapper(g) for g in grads]
    processed_grads = [process_gradient(g) for g in grads]

    # Ask the optimizer to apply the processed gradients.
    opt.apply_gradients(zip(processed_grads, var_list))
    ```

    ### Use with `tf.distribute.Strategy`

    This optimizer class is `tf.distribute.Strategy` aware, which means it
    automatically sums gradients across all replicas. To average gradients,
    you divide your loss by the global batch size, which is done
    automatically if you use `tf.keras` built-in training or evaluation loops.
    See the `reduction` argument of your loss which should be set to
    `tf.keras.losses.Reduction.SUM_OVER_BATCH_SIZE` for averaging or
    `tf.keras.losses.Reduction.SUM` for not.

    To aggregate gradients yourself, call `apply_gradients` with
    `experimental_aggregate_gradients` set to False. This is useful if you need
    to process aggregated gradients.

    If you are not using these and you want to average gradients, you should use
    `tf.math.reduce_sum` to add up your per-example losses and then divide by
    the global batch size. Note that when using `tf.distribute.Strategy`, the
    first component of a tensor's shape is the *replica-local* batch size, which
    is off by a factor equal to the number of replicas being used to compute a
    single step. As a result, using `tf.math.reduce_mean` will give the wrong
    answer, resulting in gradients that can be many times too big.

    ### Variable Constraints

    All Keras optimizers respect variable constraints. If constraint function is
    passed to any variable, the constraint will be applied to the variable after
    the gradient has been applied to the variable.
    Important: If gradient is sparse tensor, variable constraint is not
    supported.

    ### Thread Compatibility

    The entire optimizer is currently thread compatible, not thread-safe. The
    user needs to perform synchronization if necessary.

    ### Slots

    Many optimizer subclasses, such as `Adam` and `Adagrad` allocate and manage
    additional variables associated with the variables to train.  These are
    called <i>Slots</i>.  Slots have names and you can ask the optimizer for the
    names of the slots that it uses.  Once you have a slot name you can ask the
    optimizer for the variable it created to hold the slot value.

    This can be useful if you want to log debug a training algorithm, report
    stats about the slots, etc.

    ### Hyperparameters

    These are arguments passed to the optimizer subclass constructor
    (the `__init__` method), and then passed to `self._set_hyper()`.
    They can be either regular Python values (like 1.0), tensors, or
    callables. If they are callable, the callable will be called during
    `apply_gradients()` to get the value for the hyper parameter.

    Hyperparameters can be overwritten through user code:

    Example:

    ```python
    # Create an optimizer with the desired parameters.
    opt = tf.keras.optimizers.legacy.SGD(learning_rate=0.1)
    # `loss` is a callable that takes no argument and returns the value
    # to minimize.
    loss = lambda: 3 * var1 + 2 * var2
    # In eager mode, simply call minimize to update the list of variables.
    opt.minimize(loss, var_list=[var1, var2])
    # update learning rate
    opt.learning_rate = 0.05
    opt.minimize(loss, var_list=[var1, var2])
    ```

    ### Callable learning rate

    Optimizer accepts a callable learning rate in two ways. The first way is
    through built-in or customized
    `tf.keras.optimizers.schedules.LearningRateSchedule`. The schedule will be
    called on each iteration with `schedule(iteration)`, a `tf.Variable`
    owned by the optimizer.

    Example:

    >>> var = tf.Variable(np.random.random(size=(1,)))
    >>> learning_rate = tf.keras.optimizers.schedules.ExponentialDecay(
    ... initial_learning_rate=.01, decay_steps=20, decay_rate=.1)
    >>> opt = tf.keras.optimizers.legacy.SGD(learning_rate=learning_rate)
    >>> loss = lambda: 3 * var
    >>> opt.minimize(loss, var_list=[var])
    <tf.Variable...

    The second way is through a callable function that
    does not accept any arguments.

    Example:

    >>> var = tf.Variable(np.random.random(size=(1,)))
    >>> def lr_callable():
    ...   return .1
    >>> opt = tf.keras.optimizers.legacy.SGD(learning_rate=lr_callable)
    >>> loss = lambda: 3 * var
    >>> opt.minimize(loss, var_list=[var])
    <tf.Variable...

    ### Creating a custom optimizer

    If you intend to create your own optimization algorithm, simply inherit from
    this class and override the following methods:

      - `_resource_apply_dense` (update variable given gradient tensor is a
        dense `tf.Tensor`)
      - `_resource_apply_sparse` (update variable given gradient tensor is a
        sparse `tf.IndexedSlices`. The most common way for this to happen
        is if you are taking the gradient through a `tf.gather`.)
      - `_create_slots`
        (if your optimizer algorithm requires additional variables)
      - `get_config`
        (serialization of the optimizer, include all hyper parameters)
    """
    gradient_aggregator: Incomplete
    gradient_transformers: Incomplete
    def __init__(self, name, gradient_aggregator: Incomplete | None = None, gradient_transformers: Incomplete | None = None, **kwargs) -> None:
        """Create a new Optimizer.

        This must be called by the constructors of subclasses.
        Note that Optimizer instances should not bind to a single graph,
        and so shouldn't keep Tensors as member variables. Generally
        you should be able to use the _set_hyper()/state.get_hyper()
        facility instead.

        This class is stateful and thread-compatible.

        Example of custom gradient transformations:

        ```python
        def my_gradient_transformer(grads_and_vars):
          # Simple example, double the gradients.
          return [(2. * g, v) for g, v in grads_and_vars]

        optimizer = tf.keras.optimizers.legacy.SGD(
            1e-3, gradient_transformers=[my_gradient_transformer])
        ```

        Args:
          name: String. The name to use for momentum accumulator weights created
            by the optimizer.
          gradient_aggregator: The function to use to aggregate gradients across
            devices (when using `tf.distribute.Strategy`). If `None`, defaults
            to summing the gradients across devices. The function should accept
            and return a list of `(gradient, variable)` tuples.
          gradient_transformers: Optional. List of functions to use to transform
            gradients before applying updates to Variables. The functions are
            applied after `gradient_aggregator`. The functions should accept and
            return a list of `(gradient, variable)` tuples.
          **kwargs: keyword arguments. Allowed arguments are `clipvalue`,
            `clipnorm`, `global_clipnorm`.
            If `clipvalue` (float) is set, the gradient of each weight
            is clipped to be no higher than this value.
            If `clipnorm` (float) is set, the gradient of each weight
            is individually clipped so that its norm is no higher than this
            value. If `global_clipnorm` (float) is set the gradient of all
            weights is clipped so that their global norm is no higher than this
            value.

        Raises:
          ValueError: in case of any invalid argument.
        """
    @property
    def clipnorm(self):
        """`float` or `None`. If set, clips gradients to a maximum norm."""
    @property
    def global_clipnorm(self):
        """`float` or `None`.

        If set, clips gradients to a maximum norm.

        Check `tf.clip_by_global_norm` for more details.
        """
    @clipnorm.setter
    def clipnorm(self, val) -> None: ...
    @global_clipnorm.setter
    def global_clipnorm(self, val) -> None: ...
    @property
    def clipvalue(self):
        """`float` or `None`. If set, clips gradients to a maximum value."""
    @clipvalue.setter
    def clipvalue(self, val) -> None: ...
    def minimize(self, loss, var_list, grad_loss: Incomplete | None = None, name: Incomplete | None = None, tape: Incomplete | None = None):
        """Minimize `loss` by updating `var_list`.

        This method simply computes gradient using `tf.GradientTape` and calls
        `apply_gradients()`. If you want to process the gradient before applying
        then call `tf.GradientTape` and `apply_gradients()` explicitly instead
        of using this function.

        Args:
          loss: `Tensor` or callable. If a callable, `loss` should take no
            arguments and return the value to minimize. If a `Tensor`, the
            `tape` argument must be passed.
          var_list: list or tuple of `Variable` objects to update to minimize
            `loss`, or a callable returning the list or tuple of `Variable`
            objects.  Use callable when the variable list would otherwise be
            incomplete before `minimize` since the variables are created at the
            first time `loss` is called.
          grad_loss: (Optional). A `Tensor` holding the gradient computed for
            `loss`.
          name: (Optional) str. Name for the returned operation.
          tape: (Optional) `tf.GradientTape`. If `loss` is provided as a
            `Tensor`, the tape that computed the `loss` must be provided.

        Returns:
          An `Operation` that updates the variables in `var_list`. The
          `iterations` will be automatically increased by 1.

        Raises:
          ValueError: If some of the variables are not `Variable` objects.

        """
    def apply_gradients(self, grads_and_vars, name: Incomplete | None = None, experimental_aggregate_gradients: bool = True):
        """Apply gradients to variables.

        This is the second part of `minimize()`. It returns an `Operation` that
        applies gradients.

        The method sums gradients from all replicas in the presence of
        `tf.distribute.Strategy` by default. You can aggregate gradients
        yourself by passing `experimental_aggregate_gradients=False`.

        Example:

        ```python
        grads = tape.gradient(loss, vars)
        grads = tf.distribute.get_replica_context().all_reduce('sum', grads)
        # Processing aggregated gradients.
        optimizer.apply_gradients(zip(grads, vars),
            experimental_aggregate_gradients=False)

        ```

        Args:
          grads_and_vars: List of (gradient, variable) pairs.
          name: Optional name for the returned operation. Default to the name
            passed to the `Optimizer` constructor.
          experimental_aggregate_gradients: Whether to sum gradients from
            different replicas in the presence of `tf.distribute.Strategy`. If
            False, it's user responsibility to aggregate the gradients. Default
            to True.

        Returns:
          An `Operation` that applies the specified gradients. The `iterations`
          will be automatically increased by 1.

        Raises:
          TypeError: If `grads_and_vars` is malformed.
          ValueError: If none of the variables have gradients.
          RuntimeError: If called in a cross-replica context.
        """
    def get_gradients(self, loss, params):
        """Returns gradients of `loss` with respect to `params`.

        Should be used only in legacy v1 graph mode.

        Args:
          loss: Loss tensor.
          params: List of variables.

        Returns:
          List of gradient tensors.

        Raises:
          ValueError: In case any gradient cannot be computed (e.g. if gradient
            function not implemented).
        """
    def get_updates(self, loss, params): ...
    def __getattribute__(self, name):
        """Overridden to support hyperparameter access."""
    def __dir__(self): ...
    def __setattr__(self, name, value) -> None:
        """Override setattr to support dynamic hyperparameter setting."""
    def get_slot_names(self):
        """A list of names for this optimizer's slots."""
    def add_slot(self, var, slot_name, initializer: str = 'zeros', shape: Incomplete | None = None):
        """Add a new slot variable for `var`.

        A slot variable is an additional variable associated with `var` to
        train.  It is allocated and managed by optimizers, e.g. `Adam`.

        Args:
          var: a `Variable` object.
          slot_name: name of the slot variable.
          initializer: initializer of the slot variable
          shape: (Optional) shape of the slot variable. If not set, it will
            default to the shape of `var`.

        Returns:
          A slot variable.
        """
    def get_slot(self, var, slot_name): ...
    @property
    def iterations(self):
        """Variable. The number of training steps this Optimizer has run."""
    @iterations.setter
    def iterations(self, variable) -> None: ...
    @abc.abstractmethod
    def get_config(self):
        """Returns the config of the optimizer.

        An optimizer config is a Python dictionary (serializable)
        containing the configuration of an optimizer.
        The same optimizer can be reinstantiated later
        (without any saved state) from this configuration.

        Returns:
            Python dictionary.
        """
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None):
        """Creates an optimizer from its config.

        This method is the reverse of `get_config`,
        capable of instantiating the same optimizer from the config
        dictionary.

        Args:
            config: A Python dictionary, typically the output of get_config.
            custom_objects: A Python dictionary mapping names to additional
              Python objects used to create this optimizer, such as a function
              used for a hyperparameter.

        Returns:
            An optimizer instance.
        """
    def variables(self):
        """Returns variables of this Optimizer based on the order created."""
    @property
    def weights(self):
        """Returns variables of this Optimizer based on the order created."""
    def get_weights(self):
        """Returns the current weights of the optimizer.

        The weights of an optimizer are its state (ie, variables).
        This function returns the weight values associated with this
        optimizer as a list of Numpy arrays. The first value is always the
        iterations count of the optimizer, followed by the optimizer's state
        variables in the order they were created. The returned list can in turn
        be used to load state into similarly parameterized optimizers.

        For example, the RMSprop optimizer for this simple model returns a list
        of three values-- the iteration count, followed by the root-mean-square
        value of the kernel and bias of the single Dense layer:

        >>> opt = tf.keras.optimizers.legacy.RMSprop()
        >>> m = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
        >>> m.compile(opt, loss='mse')
        >>> data = np.arange(100).reshape(5, 20)
        >>> labels = np.zeros(5)
        >>> results = m.fit(data, labels)  # Training.
        >>> len(opt.get_weights())
        3

        Returns:
            Weights values as a list of numpy arrays.
        """
    def set_weights(self, weights) -> None:
        """Set the weights of the optimizer.

        The weights of an optimizer are its state (ie, variables).
        This function takes the weight values associated with this
        optimizer as a list of Numpy arrays. The first value is always the
        iterations count of the optimizer, followed by the optimizer's state
        variables in the order they are created. The passed values are used to
        set the new state of the optimizer.

        For example, the RMSprop optimizer for this simple model takes a list of
        three values-- the iteration count, followed by the root-mean-square
        value of the kernel and bias of the single Dense layer:

        >>> opt = tf.keras.optimizers.legacy.RMSprop()
        >>> m = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
        >>> m.compile(opt, loss='mse')
        >>> data = np.arange(100).reshape(5, 20)
        >>> labels = np.zeros(5)
        >>> results = m.fit(data, labels)  # Training.
        >>> new_weights = [np.array(10), np.ones([20, 10]), np.zeros([10])]
        >>> opt.set_weights(new_weights)
        >>> opt.iterations
        <tf.Variable 'RMSprop/iter:0' shape=() dtype=int64, numpy=10>

        Args:
            weights: weight values as a list of numpy arrays.
        """
    def add_weight(self, name, shape, dtype: Incomplete | None = None, initializer: str = 'zeros', trainable: Incomplete | None = None, synchronization=..., aggregation=...): ...

class RestoredOptimizer(OptimizerV2):
    """A non-functional Optimizer implementation for checkpoint compatibility.

    Holds slot variables and hyperparameters when an optimizer is restored from
    a SavedModel. These variables may be referenced in functions along with ops
    created by the original optimizer, but currently we do not support using the
    optimizer object itself (e.g. through `apply_gradients`).
    """
    def __init__(self) -> None: ...
    def get_config(self) -> None: ...
