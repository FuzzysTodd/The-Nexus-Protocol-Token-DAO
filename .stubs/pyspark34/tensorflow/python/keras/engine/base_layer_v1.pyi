from _typeshed import Incomplete
from tensorflow.python.autograph.core import ag_ctx as ag_ctx
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, errors as errors, func_graph as func_graph, ops as ops, sparse_tensor as sparse_tensor, tensor_spec as tensor_spec, tensor_util as tensor_util
from tensorflow.python.keras import backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine import base_layer as base_layer, base_layer_utils as base_layer_utils, input_spec as input_spec
from tensorflow.python.keras.mixed_precision import autocast_variable as autocast_variable, loss_scale_optimizer as loss_scale_optimizer, policy as policy
from tensorflow.python.keras.saving.saved_model import layer_serialization as layer_serialization
from tensorflow.python.keras.utils import generic_utils as generic_utils, layer_utils as layer_utils, object_identity as object_identity, tf_inspect as tf_inspect, tf_utils as tf_utils
from tensorflow.python.keras.utils.generic_utils import to_snake_case as to_snake_case
from tensorflow.python.keras.utils.tf_utils import is_tensor_or_tensor_list as is_tensor_or_tensor_list
from tensorflow.python.module import module as module
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.trackable import autotrackable as autotrackable, data_structures as data_structures
from tensorflow.python.util import nest as nest
from tensorflow.tools.docs import doc_controls as doc_controls
from typing import NamedTuple

class Layer(base_layer.Layer):
    '''Base layer class.

  This is the class from which all layers inherit.

  A layer is a class implementing common neural networks operations, such
  as convolution, batch norm, etc. These operations require managing weights,
  losses, updates, and inter-layer connectivity.

  Users will just instantiate a layer and then treat it as a callable.

  We recommend that descendants of `Layer` implement the following methods:

  * `__init__()`: Save configuration in member variables
  * `build()`: Called once from `__call__`, when we know the shapes of inputs
    and `dtype`. Should have the calls to `add_weight()`, and then
    call the super\'s `build()` (which sets `self.built = True`, which is
    nice in case the user wants to call `build()` manually before the
    first `__call__`).
  * `call()`: Called in `__call__` after making sure `build()` has been called
    once. Should actually perform the logic of applying the layer to the
    input tensors (which should be passed in as the first argument).

  Args:
    trainable: Boolean, whether the layer\'s variables should be trainable.
    name: String name of the layer.
    dtype: The dtype of the layer\'s computations and weights (default of
      `None` means use `tf.keras.backend.floatx` in TensorFlow 2, or the type
      of the first input in TensorFlow 1).
    dynamic: Set this to `True` if your layer should only be run eagerly, and
      should not be used to generate a static computation graph.
      This would be the case for a Tree-RNN or a recursive network,
      for example, or generally for any layer that manipulates tensors
      using Python control flow. If `False`, we assume that the layer can
      safely be used to generate a static computation graph.

  Attributes:
    name: The name of the layer (string).
    dtype: The dtype of the layer\'s computations and weights. If mixed
      precision is used with a `tf.keras.mixed_precision.Policy`, this is
      instead just the dtype of the layer\'s weights, as the computations are
      done in a different dtype.
    updates: List of update ops of this layer.
    losses: List of losses added by this layer.
    trainable_weights: List of variables to be included in backprop.
    non_trainable_weights: List of variables that should not be
      included in backprop.
    weights: The concatenation of the lists trainable_weights and
      non_trainable_weights (in this order).
    trainable: Whether the layer should be trained (boolean).
    input_spec: Optional (list of) `InputSpec` object(s) specifying the
      constraints on inputs that can be accepted by the layer.

  Each layer has a dtype, which is typically the dtype of the layer\'s
  computations and variables. A layer\'s dtype can be queried via the
  `Layer.dtype` property. The dtype is specified with the `dtype` constructor
  argument. In TensorFlow 2, the dtype defaults to `tf.keras.backend.floatx()`
  if no dtype is passed. `floatx()` itself defaults to "float32". Additionally,
  layers will cast their inputs to the layer\'s dtype in TensorFlow 2. When mixed
  precision is used, layers may have different computation and variable dtypes.
  See `tf.keras.mixed_precision.Policy` for details on layer dtypes.
  '''
    built: bool
    supports_masking: bool
    def __init__(self, trainable: bool = True, name: Incomplete | None = None, dtype: Incomplete | None = None, dynamic: bool = False, **kwargs) -> None: ...
    def build(self, input_shape) -> None:
        """Creates the variables of the layer (optional, for subclass implementers).

    This is a method that implementers of subclasses of `Layer` or `Model`
    can override if they need a state-creation step in-between
    layer instantiation and layer call.

    This is typically used to create the weights of `Layer` subclasses.

    Args:
      input_shape: Instance of `TensorShape`, or list of instances of
        `TensorShape` if the layer expects a list of inputs
        (one instance per input).
    """
    def call(self, inputs, **kwargs):
        """This is where the layer's logic lives.

    Args:
        inputs: Input tensor, or list/tuple of input tensors.
        **kwargs: Additional keyword arguments.

    Returns:
        A tensor or list/tuple of tensors.
    """
    def add_weight(self, name: Incomplete | None = None, shape: Incomplete | None = None, dtype: Incomplete | None = None, initializer: Incomplete | None = None, regularizer: Incomplete | None = None, trainable: Incomplete | None = None, constraint: Incomplete | None = None, partitioner: Incomplete | None = None, use_resource: Incomplete | None = None, synchronization=..., aggregation=..., **kwargs):
        '''Adds a new variable to the layer.

    Args:
      name: Variable name.
      shape: Variable shape. Defaults to scalar if unspecified.
      dtype: The type of the variable. Defaults to `self.dtype` or `float32`.
      initializer: Initializer instance (callable).
      regularizer: Regularizer instance (callable).
      trainable: Boolean, whether the variable should be part of the layer\'s
        "trainable_variables" (e.g. variables, biases)
        or "non_trainable_variables" (e.g. BatchNorm mean and variance).
        Note that `trainable` cannot be `True` if `synchronization`
        is set to `ON_READ`.
      constraint: Constraint instance (callable).
      partitioner: Partitioner to be passed to the `Trackable` API.
      use_resource: Whether to use `ResourceVariable`.
      synchronization: Indicates when a distributed a variable will be
        aggregated. Accepted values are constants defined in the class
        `tf.VariableSynchronization`. By default the synchronization is set to
        `AUTO` and the current `DistributionStrategy` chooses
        when to synchronize. If `synchronization` is set to `ON_READ`,
        `trainable` must not be set to `True`.
      aggregation: Indicates how a distributed variable will be aggregated.
        Accepted values are constants defined in the class
        `tf.VariableAggregation`.
      **kwargs: Additional keyword arguments. Accepted values are `getter`,
        `collections`, `experimental_autocast` and `caching_device`.

    Returns:
      The created variable. Usually either a `Variable` or `ResourceVariable`
      instance. If `partitioner` is not `None`, a `PartitionedVariable`
      instance is returned.

    Raises:
      RuntimeError: If called with partitioned variable regularization and
        eager execution is enabled.
      ValueError: When giving unsupported dtype and no initializer or when
        trainable has been set to True with synchronization set as `ON_READ`.
    '''
    def get_config(self):
        """Returns the config of the layer.

    A layer config is a Python dictionary (serializable)
    containing the configuration of a layer.
    The same layer can be reinstantiated later
    (without its trained weights) from this configuration.

    The config of a layer does not include connectivity
    information, nor the layer class name. These are handled
    by `Network` (one layer of abstraction above).

    Returns:
        Python dictionary.
    """
    @classmethod
    def from_config(cls, config):
        """Creates a layer from its config.

    This method is the reverse of `get_config`,
    capable of instantiating the same layer from the config
    dictionary. It does not handle layer connectivity
    (handled by Network), nor weights (handled by `set_weights`).

    Args:
        config: A Python dictionary, typically the
            output of get_config.

    Returns:
        A layer instance.
    """
    def compute_output_shape(self, input_shape):
        """Computes the output shape of the layer.

    If the layer has not been built, this method will call `build` on the
    layer. This assumes that the layer will later be used with inputs that
    match the input shape provided here.

    Args:
        input_shape: Shape tuple (tuple of integers)
            or list of shape tuples (one per output tensor of the layer).
            Shape tuples can include None for free dimensions,
            instead of an integer.

    Returns:
        An input shape tuple.
    """
    def compute_output_signature(self, input_signature):
        """Compute the output tensor signature of the layer based on the inputs.

    Unlike a TensorShape object, a TensorSpec object contains both shape
    and dtype information for a tensor. This method allows layers to provide
    output dtype information if it is different from the input dtype.
    For any layer that doesn't implement this function,
    the framework will fall back to use `compute_output_shape`, and will
    assume that the output dtype matches the input dtype.

    Args:
      input_signature: Single TensorSpec or nested structure of TensorSpec
        objects, describing a candidate input for the layer.

    Returns:
      Single TensorSpec or nested structure of TensorSpec objects, describing
        how the layer would transform the provided input.

    Raises:
      TypeError: If input_signature contains a non-TensorSpec object.
    """
    def compute_mask(self, inputs, mask: Incomplete | None = None):
        """Computes an output mask tensor.

    Args:
        inputs: Tensor or list of tensors.
        mask: Tensor or list of tensors.

    Returns:
        None or a tensor (or list of tensors,
            one per output tensor of the layer).
    """
    def __call__(self, *args, **kwargs):
        """Wraps `call`, applying pre- and post-processing steps.

    Args:
      *args: Positional arguments to be passed to `self.call`.
      **kwargs: Keyword arguments to be passed to `self.call`.

    Returns:
      Output tensor(s).

    Note:
      - The following optional keyword arguments are reserved for specific uses:
        * `training`: Boolean scalar tensor of Python boolean indicating
          whether the `call` is meant for training or inference.
        * `mask`: Boolean input mask.
      - If the layer's `call` method takes a `mask` argument (as some Keras
        layers do), its default value will be set to the mask generated
        for `inputs` by the previous layer (if `input` did come from
        a layer that generated a corresponding mask, i.e. if it came from
        a Keras layer with masking support.

    Raises:
      ValueError: if the layer's `call` method returns None (an invalid value).
      RuntimeError: if `super().__init__()` was not called in the constructor.
    """
    @property
    def dtype(self): ...
    @property
    def name(self): ...
    @property
    def dynamic(self): ...
    @property
    def stateful(self): ...
    @stateful.setter
    def stateful(self, value) -> None: ...
    @property
    def trainable(self): ...
    @trainable.setter
    def trainable(self, value) -> None: ...
    @property
    def activity_regularizer(self):
        """Optional regularizer function for the output of this layer."""
    @activity_regularizer.setter
    def activity_regularizer(self, regularizer) -> None:
        """Optional regularizer function for the output of this layer."""
    @property
    def input_spec(self): ...
    @input_spec.setter
    def input_spec(self, value) -> None: ...
    @property
    def updates(self): ...
    @property
    def losses(self):
        """Losses which are associated with this `Layer`.

    Variable regularization tensors are created when this property is accessed,
    so it is eager safe: accessing `losses` under a `tf.GradientTape` will
    propagate gradients back to the corresponding variables.

    Returns:
      A list of tensors.
    """
    def add_loss(self, losses, inputs: Incomplete | None = None):
        """Add loss tensor(s), potentially dependent on layer inputs.

    Some losses (for instance, activity regularization losses) may be dependent
    on the inputs passed when calling a layer. Hence, when reusing the same
    layer on different inputs `a` and `b`, some entries in `layer.losses` may
    be dependent on `a` and some on `b`. This method automatically keeps track
    of dependencies.

    This method can be used inside a subclassed layer or model's `call`
    function, in which case `losses` should be a Tensor or list of Tensors.

    Example:

    ```python
    class MyLayer(tf.keras.layers.Layer):
      def call(inputs, self):
        self.add_loss(tf.abs(tf.reduce_mean(inputs)), inputs=True)
        return inputs
    ```

    This method can also be called directly on a Functional Model during
    construction. In this case, any loss Tensors passed to this Model must
    be symbolic and be able to be traced back to the model's `Input`s. These
    losses become part of the model's topology and are tracked in `get_config`.

    Example:

    ```python
    inputs = tf.keras.Input(shape=(10,))
    x = tf.keras.layers.Dense(10)(inputs)
    outputs = tf.keras.layers.Dense(1)(x)
    model = tf.keras.Model(inputs, outputs)
    # Activity regularization.
    model.add_loss(tf.abs(tf.reduce_mean(x)))
    ```

    If this is not the case for your loss (if, for example, your loss references
    a `Variable` of one of the model's layers), you can wrap your loss in a
    zero-argument lambda. These losses are not tracked as part of the model's
    topology since they can't be serialized.

    Example:

    ```python
    inputs = tf.keras.Input(shape=(10,))
    x = tf.keras.layers.Dense(10)(inputs)
    outputs = tf.keras.layers.Dense(1)(x)
    model = tf.keras.Model(inputs, outputs)
    # Weight regularization.
    model.add_loss(lambda: tf.reduce_mean(x.kernel))
    ```

    The `get_losses_for` method allows to retrieve the losses relevant to a
    specific set of inputs.

    Args:
      losses: Loss tensor, or list/tuple of tensors. Rather than tensors, losses
        may also be zero-argument callables which create a loss tensor.
      inputs: Ignored when executing eagerly. If anything other than None is
        passed, it signals the losses are conditional on some of the layer's
        inputs, and thus they should only be run where these inputs are
        available. This is the case for activity regularization losses, for
        instance. If `None` is passed, the losses are assumed
        to be unconditional, and will apply across all dataflows of the layer
        (e.g. weight regularization losses).
    """
    @property
    def metrics(self): ...
    def add_metric(self, value, aggregation: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """Adds metric tensor to the layer.

    Args:
      value: Metric tensor.
      aggregation: Sample-wise metric reduction function. If `aggregation=None`,
        it indicates that the metric tensor provided has been aggregated
        already. eg, `bin_acc = BinaryAccuracy(name='acc')` followed by
        `model.add_metric(bin_acc(y_true, y_pred))`. If aggregation='mean', the
        given metric tensor will be sample-wise reduced using `mean` function.
        eg, `model.add_metric(tf.reduce_sum(outputs), name='output_mean',
        aggregation='mean')`.
      name: String metric name.

    Raises:
      ValueError: If `aggregation` is anything other than None or `mean`.
    """
    def add_update(self, updates, inputs: Incomplete | None = None):
        """Add update op(s), potentially dependent on layer inputs.

    Weight updates (for instance, the updates of the moving mean and variance
    in a BatchNormalization layer) may be dependent on the inputs passed
    when calling a layer. Hence, when reusing the same layer on
    different inputs `a` and `b`, some entries in `layer.updates` may be
    dependent on `a` and some on `b`. This method automatically keeps track
    of dependencies.

    The `get_updates_for` method allows to retrieve the updates relevant to a
    specific set of inputs.

    This call is ignored when eager execution is enabled (in that case, variable
    updates are run on the fly and thus do not need to be tracked for later
    execution).

    Args:
      updates: Update op, or list/tuple of update ops, or zero-arg callable
        that returns an update op. A zero-arg callable should be passed in
        order to disable running the updates by setting `trainable=False`
        on this Layer, when executing in Eager mode.
      inputs: Deprecated, will be automatically inferred.
    """
    def set_weights(self, weights) -> None:
        """Sets the weights of the layer, from Numpy arrays.

    The weights of a layer represent the state of the layer. This function
    sets the weight values from numpy arrays. The weight values should be
    passed in the order they are created by the layer. Note that the layer's
    weights must be instantiated before calling this function by calling
    the layer.

    For example, a Dense layer returns a list of two values-- per-output
    weights and the bias value. These can be used to set the weights of another
    Dense layer:

    >>> a = tf.keras.layers.Dense(1,
    ...   kernel_initializer=tf.constant_initializer(1.))
    >>> a_out = a(tf.convert_to_tensor([[1., 2., 3.]]))
    >>> a.get_weights()
    [array([[1.],
           [1.],
           [1.]], dtype=float32), array([0.], dtype=float32)]
    >>> b = tf.keras.layers.Dense(1,
    ...   kernel_initializer=tf.constant_initializer(2.))
    >>> b_out = b(tf.convert_to_tensor([[10., 20., 30.]]))
    >>> b.get_weights()
    [array([[2.],
           [2.],
           [2.]], dtype=float32), array([0.], dtype=float32)]
    >>> b.set_weights(a.get_weights())
    >>> b.get_weights()
    [array([[1.],
           [1.],
           [1.]], dtype=float32), array([0.], dtype=float32)]

    Args:
        weights: a list of Numpy arrays. The number
            of arrays and their shape must match
            number of the dimensions of the weights
            of the layer (i.e. it should match the
            output of `get_weights`).

    Raises:
        ValueError: If the provided weights list does not match the
            layer's specifications.
    """
    def get_weights(self):
        """Returns the current weights of the layer.

    The weights of a layer represent the state of the layer. This function
    returns both trainable and non-trainable weight values associated with this
    layer as a list of Numpy arrays, which can in turn be used to load state
    into similarly parameterized layers.

    For example, a Dense layer returns a list of two values-- per-output
    weights and the bias value. These can be used to set the weights of another
    Dense layer:

    >>> a = tf.keras.layers.Dense(1,
    ...   kernel_initializer=tf.constant_initializer(1.))
    >>> a_out = a(tf.convert_to_tensor([[1., 2., 3.]]))
    >>> a.get_weights()
    [array([[1.],
           [1.],
           [1.]], dtype=float32), array([0.], dtype=float32)]
    >>> b = tf.keras.layers.Dense(1,
    ...   kernel_initializer=tf.constant_initializer(2.))
    >>> b_out = b(tf.convert_to_tensor([[10., 20., 30.]]))
    >>> b.get_weights()
    [array([[2.],
           [2.],
           [2.]], dtype=float32), array([0.], dtype=float32)]
    >>> b.set_weights(a.get_weights())
    >>> b.get_weights()
    [array([[1.],
           [1.],
           [1.]], dtype=float32), array([0.], dtype=float32)]

    Returns:
        Weights values as a list of numpy arrays.
    """
    def get_updates_for(self, inputs):
        """Retrieves updates relevant to a specific set of inputs.

    Args:
      inputs: Input tensor or list/tuple of input tensors.

    Returns:
      List of update ops of the layer that depend on `inputs`.
    """
    def get_losses_for(self, inputs):
        """Retrieves losses relevant to a specific set of inputs.

    Args:
      inputs: Input tensor or list/tuple of input tensors.

    Returns:
      List of loss tensors of the layer that depend on `inputs`.
    """
    def get_input_mask_at(self, node_index):
        """Retrieves the input mask tensor(s) of a layer at a given node.

    Args:
        node_index: Integer, index of the node
            from which to retrieve the attribute.
            E.g. `node_index=0` will correspond to the
            first time the layer was called.

    Returns:
        A mask tensor
        (or list of tensors if the layer has multiple inputs).
    """
    def get_output_mask_at(self, node_index):
        """Retrieves the output mask tensor(s) of a layer at a given node.

    Args:
        node_index: Integer, index of the node
            from which to retrieve the attribute.
            E.g. `node_index=0` will correspond to the
            first time the layer was called.

    Returns:
        A mask tensor
        (or list of tensors if the layer has multiple outputs).
    """
    @property
    def input_mask(self):
        """Retrieves the input mask tensor(s) of a layer.

    Only applicable if the layer has exactly one inbound node,
    i.e. if it is connected to one incoming layer.

    Returns:
        Input mask tensor (potentially None) or list of input
        mask tensors.

    Raises:
        AttributeError: if the layer is connected to
        more than one incoming layers.
    """
    @property
    def output_mask(self):
        """Retrieves the output mask tensor(s) of a layer.

    Only applicable if the layer has exactly one inbound node,
    i.e. if it is connected to one incoming layer.

    Returns:
        Output mask tensor (potentially None) or list of output
        mask tensors.

    Raises:
        AttributeError: if the layer is connected to
        more than one incoming layers.
    """
    def get_input_shape_at(self, node_index):
        """Retrieves the input shape(s) of a layer at a given node.

    Args:
        node_index: Integer, index of the node
            from which to retrieve the attribute.
            E.g. `node_index=0` will correspond to the
            first time the layer was called.

    Returns:
        A shape tuple
        (or list of shape tuples if the layer has multiple inputs).

    Raises:
      RuntimeError: If called in Eager mode.
    """
    def get_output_shape_at(self, node_index):
        """Retrieves the output shape(s) of a layer at a given node.

    Args:
        node_index: Integer, index of the node
            from which to retrieve the attribute.
            E.g. `node_index=0` will correspond to the
            first time the layer was called.

    Returns:
        A shape tuple
        (or list of shape tuples if the layer has multiple outputs).

    Raises:
      RuntimeError: If called in Eager mode.
    """
    def get_input_at(self, node_index):
        """Retrieves the input tensor(s) of a layer at a given node.

    Args:
        node_index: Integer, index of the node
            from which to retrieve the attribute.
            E.g. `node_index=0` will correspond to the
            first input node of the layer.

    Returns:
        A tensor (or list of tensors if the layer has multiple inputs).

    Raises:
      RuntimeError: If called in Eager mode.
    """
    def get_output_at(self, node_index):
        """Retrieves the output tensor(s) of a layer at a given node.

    Args:
        node_index: Integer, index of the node
            from which to retrieve the attribute.
            E.g. `node_index=0` will correspond to the
            first output node of the layer.

    Returns:
        A tensor (or list of tensors if the layer has multiple outputs).

    Raises:
      RuntimeError: If called in Eager mode.
    """
    @property
    def input(self):
        """Retrieves the input tensor(s) of a layer.

    Only applicable if the layer has exactly one input,
    i.e. if it is connected to one incoming layer.

    Returns:
        Input tensor or list of input tensors.

    Raises:
      RuntimeError: If called in Eager mode.
      AttributeError: If no inbound nodes are found.
    """
    @property
    def output(self):
        """Retrieves the output tensor(s) of a layer.

    Only applicable if the layer has exactly one output,
    i.e. if it is connected to one incoming layer.

    Returns:
      Output tensor or list of output tensors.

    Raises:
      AttributeError: if the layer is connected to more than one incoming
        layers.
      RuntimeError: if called in Eager mode.
    """
    @property
    def input_shape(self):
        """Retrieves the input shape(s) of a layer.

    Only applicable if the layer has exactly one input,
    i.e. if it is connected to one incoming layer, or if all inputs
    have the same shape.

    Returns:
        Input shape, as an integer shape tuple
        (or list of shape tuples, one tuple per input tensor).

    Raises:
        AttributeError: if the layer has no defined input_shape.
        RuntimeError: if called in Eager mode.
    """
    def count_params(self):
        """Count the total number of scalars composing the weights.

    Returns:
        An integer count.

    Raises:
        ValueError: if the layer isn't yet built
          (in which case its weights aren't yet defined).
    """
    @property
    def output_shape(self):
        """Retrieves the output shape(s) of a layer.

    Only applicable if the layer has one output,
    or if all outputs have the same shape.

    Returns:
        Output shape, as an integer shape tuple
        (or list of shape tuples, one tuple per output tensor).

    Raises:
        AttributeError: if the layer has no defined output shape.
        RuntimeError: if called in Eager mode.
    """
    @property
    def inbound_nodes(self):
        """Deprecated, do NOT use! Only for compatibility with external Keras."""
    @property
    def outbound_nodes(self):
        """Deprecated, do NOT use! Only for compatibility with external Keras."""
    def apply(self, inputs, *args, **kwargs):
        """Deprecated, do NOT use!

    This is an alias of `self.__call__`.

    Args:
      inputs: Input tensor(s).
      *args: additional positional arguments to be passed to `self.call`.
      **kwargs: additional keyword arguments to be passed to `self.call`.

    Returns:
      Output tensor(s).
    """
    def add_variable(self, *args, **kwargs):
        """Deprecated, do NOT use! Alias for `add_weight`."""
    @property
    def variables(self):
        """Returns the list of all layer variables/weights.

    Alias of `self.weights`.

    Returns:
      A list of variables.
    """
    @property
    def trainable_variables(self): ...
    @property
    def non_trainable_variables(self): ...
    def __delattr__(self, name) -> None: ...
    def __setattr__(self, name, value) -> None: ...

class KerasHistory(NamedTuple('KerasHistory', [('layer', Incomplete), ('node_index', Incomplete), ('tensor_index', Incomplete)])):
    """Tracks the Layer call that created a Tensor, for Keras Graph Networks.

  During construction of Keras Graph Networks, this metadata is added to
  each Tensor produced as the output of a Layer, starting with an
  `InputLayer`. This allows Keras to track how each Tensor was produced, and
  this information is later retraced by the `keras.engine.Network` class to
  reconstruct the Keras Graph Network.

  Attributes:
    layer: The Layer that produced the Tensor.
    node_index: The specific call to the Layer that produced this Tensor. Layers
      can be called multiple times in order to share weights. A new node is
      created every time a Tensor is called.
    tensor_index: The output index for this Tensor. Always zero if the Layer
      that produced this Tensor only has one output. Nested structures of
      Tensors are deterministically assigned an index via `nest.flatten`.
  """
InputSpec = input_spec.InputSpec
