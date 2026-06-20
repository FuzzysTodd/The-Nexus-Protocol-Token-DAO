import abc
import tensorflow.compat.v2 as tf
from _typeshed import Incomplete
from keras import backend as backend, initializers as initializers
from keras.optimizers.schedules import learning_rate_schedule as learning_rate_schedule
from keras.utils import tf_utils as tf_utils

class _BaseOptimizer(tf.__internal__.tracking.AutoTrackable, metaclass=abc.ABCMeta):
    """Optimizer base class, which only supports non-distribute use case."""
    name: Incomplete
    weight_decay: Incomplete
    clipnorm: Incomplete
    global_clipnorm: Incomplete
    clipvalue: Incomplete
    use_ema: Incomplete
    jit_compile: bool
    ema_momentum: Incomplete
    ema_overwrite_frequency: Incomplete
    def __init__(self, name, weight_decay: Incomplete | None = None, clipnorm: Incomplete | None = None, clipvalue: Incomplete | None = None, global_clipnorm: Incomplete | None = None, use_ema: bool = False, ema_momentum: float = 0.99, ema_overwrite_frequency: Incomplete | None = None, jit_compile: bool = True, **kwargs) -> None: ...
    @abc.abstractmethod
    def update_step(self, gradient, variable):
        """Function to update variable value based on given gradients.

        This method must be implemented in customized optimizers.

        Args:
          gradient: backpropagated gradient of the given variable.
          variable: variable whose value needs to be updated.

        Returns:
          An `Operation` that applies the specified gradients.

        """
    def compute_gradients(self, loss, var_list, tape: Incomplete | None = None):
        """Compute gradients of loss on trainable variables.

        Args:
          loss: `Tensor` or callable. If a callable, `loss` should take no
            arguments and return the value to minimize.
          var_list: list or tuple of `Variable` objects to update to minimize
            `loss`, or a callable returning the list or tuple of `Variable`
            objects. Use callable when the variable list would otherwise be
            incomplete before `minimize` since the variables are created at the
            first time `loss` is called.
          tape: (Optional) `tf.GradientTape`. If `loss` is provided as a
            `Tensor`, the tape that computed the `loss` must be provided.

        Returns:
          A list of (gradient, variable) pairs. Variable is always present, but
          gradient can be `None`.
        """
    @property
    def iterations(self):
        """The number of training steps this `optimizer` has run.

        By default, iterations would be incremented by one every time
        `apply_gradients()` is called.
        """
    @iterations.setter
    def iterations(self, variable) -> None: ...
    @property
    def learning_rate(self): ...
    @learning_rate.setter
    def learning_rate(self, learning_rate) -> None: ...
    @property
    def lr(self):
        """Alias of `learning_rate()`.

        `lr()` is heavily called in workflows using `optimizer_v2.OptimizerV2`,
        so we keep it for backward compabitliy.
        """
    @lr.setter
    def lr(self, learning_rate) -> None: ...
    @abc.abstractmethod
    def build(self, var_list):
        """Initialize the optimizer's variables, such as momemtum variables.

        This function has to be implemented by subclass optimizers, and subclass
        optimizers need to call `super().build(var_list)`.

        Args:
          var_list: List of model variables to build optimizers on. For example,
            SGD optimizer with momentum will store one momentum variable
            corresponding to each model variable.
        """
    def add_variable(self, shape, dtype: Incomplete | None = None, initializer: str = 'zeros', name: Incomplete | None = None):
        """Create an optimizer variable.

        Args:
          shape: A list of integers, a tuple of integers, or a 1-D Tensor of
            type int32. Defaults to scalar if unspecified.
          dtype: The DType of the optimizer variable to be created. Defaults to
            `tf.keras.backend.floatx` if unspecified.
          initializer: string or callable. Initializer instance.
          name: The name of the optimizer variable to be created.

        Returns:
          An optimizer variable, in the format of tf.Variable.

        """
    def add_variable_from_reference(self, model_variable, variable_name, shape: Incomplete | None = None, initial_value: Incomplete | None = None):
        """Create an optimizer variable from model variable.

        Create an optimizer variable based on the information of model variable.
        For example, in SGD optimizer momemtum, for each model variable, a
        corresponding momemtum variable is created of the same shape and dtype.

        Args:
          model_variable: tf.Variable. The corresponding model variable to the
            optimizer variable to be created.
          variable_name: String. The name prefix of the optimizer variable to be
            created. The create variables name will follow the pattern
            `{variable_name}/{model_variable.name}`, e.g., `momemtum/dense_1`.
          shape: List or Tuple, defaults to None. The shape of the optimizer
            variable to be created. If None, the created variable will have the
            same shape as `model_variable`.
          initial_value: A Tensor, or Python object convertible to a Tensor,
            defaults to None. The initial value of the optimizer variable, if
            None, the initial value will be default to 0.

        Returns:
          An optimizer variable.
        """
    def minimize(self, loss, var_list, tape: Incomplete | None = None) -> None:
        """Minimize `loss` by updating `var_list`.

        This method simply computes gradient using `tf.GradientTape` and calls
        `apply_gradients()`. If you want to process the gradient before applying
        then call `tf.GradientTape` and `apply_gradients()` explicitly instead
        of using this function.

        Args:
          loss: `Tensor` or callable. If a callable, `loss` should take no
            arguments and return the value to minimize.
          var_list: list or tuple of `Variable` objects to update to minimize
            `loss`, or a callable returning the list or tuple of `Variable`
            objects.  Use callable when the variable list would otherwise be
            incomplete before `minimize` since the variables are created at the
            first time `loss` is called.
          tape: (Optional) `tf.GradientTape`.

        Returns:
          None
        """
    def exclude_from_weight_decay(self, var_list: Incomplete | None = None, var_names: Incomplete | None = None) -> None:
        """Exclude variables from weight decay.

        This method must be called before the optimizer's `build` method is
        called. You can set specific variables to exclude out, or set a list of
        strings as the anchor words, if any of which appear in a variable's
        name, then the variable is excluded.

        Args:
            var_list: A list of `tf.Variable`s to exclude from weight decay.
            var_names: A list of strings. If any string in `var_names` appear
                in the model variable's name, then this model variable is
                excluded from weight decay. For example, `var_names=['bias']`
                excludes all bias variables from weight decay.
        """
    def apply_gradients(self, grads_and_vars, name: Incomplete | None = None):
        """Apply gradients to variables.

        Args:
          grads_and_vars: List of `(gradient, variable)` pairs.
          name: string, defaults to None. The name of the namescope to
            use when creating variables. If None, `self.name` will be used.

        Returns:
          A `tf.Variable`, representing the current iteration.

        Raises:
          TypeError: If `grads_and_vars` is malformed.
        """
    def finalize_variable_values(self, var_list) -> None:
        """Set the final value of model's trainable variables.

        Sometimes there are some extra steps before ending the variable updates,
        such as overriding the model variables with its average value.

        Args:
          var_list: list of model variables.
        """
    def get_config(self):
        """Returns the config of the optimizer.

        An optimizer config is a Python dictionary (serializable)
        containing the configuration of an optimizer.
        The same optimizer can be reinstantiated later
        (without any saved state) from this configuration.

        Subclass optimizer should override this method to include other
        hyperparameters.

        Returns:
            Python dictionary.
        """
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None):
        """Creates an optimizer from its config.

        This method is the reverse of `get_config`, capable of instantiating the
        same optimizer from the config dictionary.

        Args:
            config: A Python dictionary, typically the output of get_config.
            custom_objects: A Python dictionary mapping names to additional
              user-defined Python objects needed to recreate this optimizer.

        Returns:
            An optimizer instance.
        """
    @property
    def variables(self):
        """Returns variables of this optimizer."""
    def set_weights(self, weights) -> None:
        """Set the weights of the optimizer.

        Args:
            weights: a list of `tf.Variable`s or numpy arrays, the target values
                of optimizer variables. It should have the same order as
                `self._variables`.
        """

base_optimizer_keyword_args: str

class Optimizer(_BaseOptimizer, metaclass=abc.ABCMeta):
    '''Abstract optimizer base class.

    This class supports distributed training. If you want to implement your own
    optimizer, please subclass this class instead of _BaseOptimizer.

    Args:
      {{base_optimizer_keyword_args}}

    ### Usage

    ```python
    # Create an optimizer with the desired parameters.
    opt = tf.keras.optimizers.experimental.SGD(learning_rate=0.1)
    var1, var2 = tf.Variable(1.0), tf.Variable(2.0)
    # `loss` is a callable that takes no argument and returns the value
    # to minimize.
    loss = lambda: 3 * var1 * var1 + 2 * var2 * var2
    # Call minimize to update the list of variables.
    opt.minimize(loss, var_list=[var1, var2])
    ```

    ### Processing gradients before applying them

    Calling `minimize()` takes care of both computing the gradients and
    applying them to the variables. If you want to process the gradients
    before applying them you can instead use the optimizer in three steps:

    1.  Compute the gradients with `tf.GradientTape`.
    2.  Process the gradients as you wish.
    3.  Apply the processed gradients with `apply_gradients()`.

    Example:

    ```python
    # Create an optimizer.
    opt = tf.keras.optimizers.experimental.SGD(learning_rate=0.1)
    var1, var2 = tf.Variable(1.0), tf.Variable(2.0)

    # Compute the gradients for a list of variables.
    with tf.GradientTape() as tape:
      loss = 3 * var1 * var1 + 2 * var2 * var2
    grads = tape.gradient(loss, [var1, var2])

    # Process the gradients.
    grads[0] = grads[0] + 1

    # Ask the optimizer to apply the gradients on variables.
    opt.apply_gradients(zip(grads, [var1, var2]))
    ```

    ### Dynamic learning rate

    Dynamic learning rate can be achieved by setting learning rate as a built-in
    or customized `tf.keras.optimizers.schedules.LearningRateSchedule`.

    Example:

    >>> var = tf.Variable(np.random.random(size=(1,)))
    >>> learning_rate = tf.keras.optimizers.schedules.ExponentialDecay(
    ...   initial_learning_rate=.01, decay_steps=20, decay_rate=.1)
    >>> opt = tf.keras.optimizers.experimental.SGD(learning_rate=learning_rate)
    >>> loss = lambda: 3 * var
    >>> opt.minimize(loss, var_list=[var])

    ### Gradients clipping

    Users can clip the gradients before applying to variables by setting
    `clipnorm`, `clipvalue` and `global_clipnorm`. Notice that `clipnorm` and
    `global_clipnorm` can only have one being set.

    Example:

    >>> opt = tf.keras.optimizers.experimental.SGD(learning_rate=1, clipvalue=1)
    >>> var1, var2 = tf.Variable(2.0), tf.Variable(2.0)
    >>> with tf.GradientTape() as tape:
    ...   loss = 2 * var1 + 2 * var2
    >>> grads = tape.gradient(loss, [var1, var2])
    >>> print([grads[0].numpy(), grads[1].numpy()])
    [2.0, 2.0]
    >>> opt.apply_gradients(zip(grads, [var1, var2]))
    >>> # Without clipping, we should get [0, 0], but as gradients are clipped
    >>> # to have max value 1, we get [1.0, 1.0].
    >>> print([var1.numpy(), var2.numpy()])
    [1.0, 1.0]

    ### Using weight decay.

    Weight decay in certain scenarios can boost the model\'s performance. Keras
    has built-in support for weight decay in all optimizers. Users can apply
    weight decay by setting `weight_decay` argument.

    >>> opt = tf.keras.optimizers.experimental.SGD(1, weight_decay=0.004)
    >>> grads, var1, var2 = tf.zeros(()), tf.Variable(2.0), tf.Variable(2.0)
    >>> # You can exclude variables from weight decay, in this case we
    >>> # exclude `var2`.
    >>> opt.exclude_from_weight_decay(var_list=[var2])
    >>> opt.apply_gradients(zip([grads, grads], [var1, var2]))
    >>> print([var1.numpy(), var2.numpy()])
    [1.992, 2.0]


    ### Using exponential moving average.

    Empirically it has been found that using the exponential moving average
    (EMA) of the trained parameters of a deep network achieves a better
    performance than using its trained parameters directly. Keras optimizers
    allows users to compute this moving average and overwrite the model
    variables at desired time.

    Example:

    ```python
    # Create an SGD optimizer with EMA on. `ema_momentum` controls the decay
    # rate of the moving average. `ema_momentum=1` means no decay and the stored
    # moving average is always model variable\'s initial value before training.
    # Reversely, `ema_momentum=0` is equivalent to not using EMA.
    # `ema_overwrite_frequency=3` means every 3 iterations, we overwrite the
    # trainable variables with their moving average values.
    opt = tf.keras.optimizers.experimental.SGD(
        learning_rate=1,
        use_ema=True,
        ema_momentum=0.5,
        ema_overwrite_frequency=3)
    var1, var2 = tf.Variable(2.0), tf.Variable(2.0)
    with tf.GradientTape() as tape:
      loss = var1 + var2
    grads = tape.gradient(loss, [var1, var2])
    # First iteration: [var1, var2] = [1.0, 1.0]
    opt.apply_gradients(zip(grads, [var1, var2]))
    print([var1, var2])

    # Second iteration: [var1, var2] = [0.0, 0.0]
    opt.apply_gradients(zip(grads, [var1, var2]))
    print([var1, var2])

    # Third iteration, without EMA, we should see [var1, var2] = [-1.0, -1.0],
    # but overwriting results in [var1, var2] = [-0.125, -0.125]. The full
    # calculation for the moving average of var1 is:
    # var1=2*0.5**3+1*(1-0.5)*0.5**2+0*(1-0.5)*0.5**1+(-1)*(1-0.5)=-0.125.
    opt.apply_gradients(zip(grads, [var1, var2]))
    print([var1, var2])

    ```
    When optimizer is constructed with `use_ema=True`, in custom training loop,
    users can explicitly call `finalize_variable_values()` to overwrite
    trainable variables with their EMA values. `finalize_variable_values()` is
    by default called at the end of `model.fit()`.

    ### Use with `tf.distribute.Strategy`

    This optimizer class is `tf.distribute.Strategy` aware, which means it
    automatically sums gradients across all replicas. To aggregate gradients
    yourself, call `apply_gradients` with `skip_aggregate_gradients` set to
    True.  This is useful if you need to process aggregated gradients.

    ```python
    # This example is not runnable, it consists of dummy code for simple
    # tutorial.
    strategy = tf.distribute.experimental.TPUStrategy()

    with strategy.scope():
      opt = tf.keras.optimizers.experimental.SGD()
      model = magic_function_that_returns_model()
      gradients = magic_function_that_returns_gradients()
      # Custom logic to aggregate gradients.
      gradients = strategy.reduce("SUM", gradients, axis=None)
      opt.apply_gradients(zip(gradients, model.trainable_variables),
          skip_aggregate_gradients=True)
    ```

    ### Creating a custom optimizer

    If you intend to create your own optimization algorithm, please inherit from
    this class and override the following methods:

      - `build`: Create your optimizer-related variables, such as `momentums` in
        SGD optimizer.
      - `update_step`: Implement your optimizer\'s updating logic.
      - `get_config`: serialization of the optimizer, include all hyper
        parameters.

    Your optimizer would automatically be compatible with tensorflow distributed
    training if you subclass `optimizer_experimental.Optimizer`.

    '''
    def __init__(self, name, weight_decay: int = 0, clipnorm: Incomplete | None = None, clipvalue: Incomplete | None = None, global_clipnorm: Incomplete | None = None, use_ema: bool = False, ema_momentum: float = 0.99, ema_overwrite_frequency: Incomplete | None = None, jit_compile: bool = True, **kwargs) -> None:
        """Create a new Optimizer."""
    def add_variable_from_reference(self, model_variable, variable_name, shape: Incomplete | None = None, initial_value: Incomplete | None = None): ...
    def aggregate_gradients(self, grads_and_vars):
        """Aggregate gradients on all devices.

        By default we will perform reduce_sum of gradients across devices. Users
        can implement their own aggregation logic by overriding this method.

        Args:
          grads_and_vars: List of (gradient, variable) pairs.

        Returns:
          List of (gradient, variable) pairs.
        """
    def apply_gradients(self, grads_and_vars, name: Incomplete | None = None, skip_gradients_aggregation: bool = False, **kwargs):
        """Apply gradients to variables.

        Args:
          grads_and_vars: List of `(gradient, variable)` pairs.
          name: string, defaults to None. The name of the namescope to
            use when creating variables. If None, `self.name` will be used.
          skip_gradients_aggregation: If true, gradients aggregation will not be
            performed inside optimizer. Usually this arg is set to True when you
            write custom code aggregating gradients outside the optimizer.
          **kwargs: keyword arguments only used for backward compatibility.

        Returns:
          A `tf.Variable`, representing the current iteration.

        Raises:
          TypeError: If `grads_and_vars` is malformed.
          RuntimeError: If called in a cross-replica context.
        """

class RestoredOptimizer(Optimizer, metaclass=abc.ABCMeta):
    def __init__(self) -> None: ...
    def get_config(self) -> None: ...

class CallableList(list):
    """Temporary shim to support both `opt.variables()` and `opt.variables`."""
    def __call__(self): ...
