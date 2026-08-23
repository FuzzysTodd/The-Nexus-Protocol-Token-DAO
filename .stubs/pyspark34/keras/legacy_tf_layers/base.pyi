from _typeshed import Incomplete
from collections.abc import Generator
from keras import backend as backend
from keras.engine import base_layer_utils as base_layer_utils, base_layer_v1 as base_layer
from keras.legacy_tf_layers import variable_scope_shim as variable_scope_shim
from keras.mixed_precision import policy as policy
from keras.utils import tf_contextlib as tf_contextlib

def keras_style_scope() -> Generator[None, None, None]:
    '''Use Keras-style variable management.

    All tf.layers and tf RNN cells created in this scope use Keras-style
    variable management.  Creating such layers with a scope= argument is
    disallowed, and reuse=True is disallowed.

    The purpose of this scope is to allow users of existing layers to
    slowly transition to a Keras layers API without breaking existing
    functionality.

    One example of this is when using TensorFlow\'s RNN classes with Keras
    Models or Networks.  Because Keras models do not properly set variable
    scopes, users of RNNs may either accidentally share scopes between two
    different models, or get errors about variables that already exist.

    Example:

    ```python
    class RNNModel(tf.keras.Model):

      def __init__(self, name):
        super(RNNModel, self).__init__(name=name)
        self.rnn = tf.compat.v1.nn.rnn_cell.MultiRNNCell(
          [tf.compat.v1.nn.rnn_cell.LSTMCell(64) for _ in range(2)])

      def call(self, input, state):
        return self.rnn(input, state)

    model_1 = RNNModel("model_1")
    model_2 = RNNModel("model_2")

    # OK
    output_1, next_state_1 = model_1(input, state)
    # Raises an error about trying to create an already existing variable.
    output_2, next_state_2 = model_2(input, state)
    ```

    The solution is to wrap the model construction and execution in a
    keras-style scope:

    ```python
    with keras_style_scope():
      model_1 = RNNModel("model_1")
      model_2 = RNNModel("model_2")

      # model_1 and model_2 are guaranteed to create their own variables.
      output_1, next_state_1 = model_1(input, state)
      output_2, next_state_2 = model_2(input, state)

      assert len(model_1.weights) > 0
      assert len(model_2.weights) > 0
      assert(model_1.weights != model_2.weights)
    ```

    Yields:
      A keras layer style scope.
    '''
def set_keras_style() -> None:
    '''Use Keras-style variable management.

    All tf.layers and tf RNN cells created after keras style ha been enabled
    use Keras-style variable management.  Creating such layers with a
    scope= argument is disallowed, and reuse=True is disallowed.

    The purpose of this function is to allow users of existing layers to
    slowly transition to Keras layers API without breaking existing
    functionality.

    For more details, see the documentation for `keras_style_scope`.

    Note, once keras style has been set, it is set globally for the entire
    program and cannot be unset.

    Example:

    ```python
    set_keras_style()

    model_1 = RNNModel(name="model_1")
    model_2 = RNNModel(name="model_2")

    # model_1 and model_2 are guaranteed to create their own variables.
    output_1, next_state_1 = model_1(input, state)
    output_2, next_state_2 = model_2(input, state)

    assert len(model_1.weights) > 0
    assert len(model_2.weights) > 0
    assert(model_1.weights != model_2.weights)
    ```
    '''

class Layer(base_layer.Layer):
    """Base layer class.

    It is considered legacy, and we recommend the use of `tf.keras.layers.Layer`
    instead.

    Args:
      trainable: Boolean, whether the layer's variables should be trainable.
      name: String name of the layer.
      dtype: Default dtype of the layer's weights (default of `None` means use
        the type of the first input).

    Read-only properties:
      name: The name of the layer (string).
      dtype: Default dtype of the layer's weights (default of `None` means use
        the type of the first input).
      trainable_variables: List of trainable variables.
      non_trainable_variables: List of non-trainable variables.
      variables: List of all variables of this layer, trainable and
        non-trainable.
      updates: List of update ops of this layer.
      losses: List of losses added by this layer.
      trainable_weights: List of variables to be included in backprop.
      non_trainable_weights: List of variables that should not be
        included in backprop.
      weights: The concatenation of the lists trainable_weights and
        non_trainable_weights (in this order).

    Mutable properties:
      trainable: Whether the layer should be trained (boolean).
      input_spec: Optional (list of) `InputSpec` object(s) specifying the
        constraints on inputs that can be accepted by the layer.
    """
    built: bool
    def __init__(self, trainable: bool = True, name: Incomplete | None = None, dtype: Incomplete | None = None, **kwargs) -> None: ...
    def apply(self, *args, **kwargs): ...
    @property
    def graph(self) -> None: ...
    @property
    def scope_name(self): ...
    def add_loss(self, losses, inputs: Incomplete | None = None) -> None: ...
    def add_weight(self, name, shape, dtype: Incomplete | None = None, initializer: Incomplete | None = None, regularizer: Incomplete | None = None, trainable: Incomplete | None = None, constraint: Incomplete | None = None, use_resource: Incomplete | None = None, synchronization=..., aggregation=..., partitioner: Incomplete | None = None, **kwargs):
        '''Adds a new variable to the layer, or gets an existing one; returns it

        Args:
          name: variable name.
          shape: variable shape.
          dtype: The type of the variable. Defaults to `self.dtype` or
            `float32`.
          initializer: initializer instance (callable).
          regularizer: regularizer instance (callable).
          trainable: whether the variable should be part of the layer\'s
            "trainable_variables" (e.g. variables, biases)
            or "non_trainable_variables" (e.g. BatchNorm mean, stddev).
            Note, if the current variable scope is marked as non-trainable
            then this parameter is ignored and any added variables are also
            marked as non-trainable. `trainable` defaults to `True` unless
            `synchronization` is set to `ON_READ`.
          constraint: constraint instance (callable).
          use_resource: Whether to use `ResourceVariable`.
          synchronization: Indicates when a distributed a variable will be
            aggregated. Accepted values are constants defined in the class
            `tf.VariableSynchronization`. By default the synchronization is set
            to `AUTO` and the current `DistributionStrategy` chooses when to
            synchronize. If `synchronization` is set to `ON_READ`, `trainable`
            must not be set to `True`.
          aggregation: Indicates how a distributed variable will be aggregated.
            Accepted values are constants defined in the class
            `tf.VariableAggregation`.
          partitioner: (optional) partitioner instance (callable).  If
            provided, when the requested variable is created it will be split
            into multiple partitions according to `partitioner`.  In this case,
            an instance of `PartitionedVariable` is returned.  Available
            partitioners include `tf.compat.v1.fixed_size_partitioner` and
            `tf.compat.v1.variable_axis_size_partitioner`.  For more details,
            see the documentation of `tf.compat.v1.get_variable` and the
            "Variable Partitioners and Sharding" section of the API guide.
          **kwargs: Additional keyword arguments.

        Returns:
          The created variable.  Usually either a `Variable` or
          `ResourceVariable` instance.  If `partitioner` is not `None`, a
          `PartitionedVariable` instance is returned.

        Raises:
          RuntimeError: If called with partitioned variable regularization and
            eager execution is enabled.
          ValueError: When trainable has been set to True with synchronization
            set as `ON_READ`.
        '''
    def __call__(self, inputs, *args, **kwargs):
        """Wraps `call`, applying pre- and post-processing steps.

        Args:
          inputs: input tensor(s).
          *args: additional positional arguments to be passed to `self.call`.
          **kwargs: additional keyword arguments to be passed to `self.call`.
            **Note**: kwarg `scope` is reserved for use by the layer.

        Returns:
          Output tensor(s).

        Note:
          - If the layer's `call` method takes a `scope` keyword argument, this
            argument will be automatically set to the current variable scope.
          - If the layer's `call` method takes a `mask` argument (as some Keras
            layers do), its default value will be set to the mask generated
            for `inputs` by the previous layer (if `input` did come from
            a layer that generated a corresponding mask, i.e. if it came from
            a Keras layer with masking support.

        Raises:
          ValueError: if the layer's `call` method returns None (an invalid
            value).
        """
    def __deepcopy__(self, memo): ...
    def __setattr__(self, value, name) -> None: ...
