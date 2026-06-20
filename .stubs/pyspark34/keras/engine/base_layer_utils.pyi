from _typeshed import Incomplete
from keras import backend as backend
from keras.utils import control_flow_util as control_flow_util, tf_inspect as tf_inspect, tf_utils as tf_utils

def create_mean_metric(value, name: Incomplete | None = None): ...
def make_variable(name, shape: Incomplete | None = None, dtype=..., initializer: Incomplete | None = None, trainable: Incomplete | None = None, caching_device: Incomplete | None = None, validate_shape: bool = True, constraint: Incomplete | None = None, use_resource: Incomplete | None = None, collections: Incomplete | None = None, synchronization=..., aggregation=..., partitioner: Incomplete | None = None, layout: Incomplete | None = None):
    '''Util to create a variable (relies on `variable_scope.variable`).

    Some reuse-related technicalities prevent us from using
    `variable_scope.get_variable()` directly, so we use a subcomponent
    that has fewer constraints (`variable_scope.variable()`).

    In the longer term, it seems like a similar "default variable creator"
    method should exist in `Trackable` instead. When this happens, we can get
    rid of this temporary solution.

    TODO(fchollet): remove this method when no longer needed.

    Args:
      name: Variable name.
      shape: Variable shape.
      dtype: The type of the variable. Defaults to `self.dtype` or `float32`.
      initializer: Initializer instance (callable).
      trainable: Whether the variable should be part of the layer\'s
        "trainable_variables" (e.g. variables, biases)
        or "non_trainable_variables" (e.g. BatchNorm mean, stddev).
        Note, if the current variable scope is marked as non-trainable
        then this parameter is ignored and any added variables are also
        marked as non-trainable. `trainable` defaults to `True` unless
        `synchronization` is set to `ON_READ`.
      caching_device: Passed to `tf.Variable`.
      validate_shape: Passed to `tf.Variable`.
      constraint: Constraint instance (callable).
      use_resource: Whether to use a `ResourceVariable`.
      collections: List of graph collections keys. The new variable is added to
        these collections. Defaults to `[GraphKeys.GLOBAL_VARIABLES]`.
      synchronization: Indicates when a distributed a variable will be
        aggregated. Accepted values are constants defined in the class
        `tf.VariableSynchronization`. By default the synchronization is set to
        `AUTO` and the current `DistributionStrategy` chooses
        when to synchronize. If `synchronization` is set to `ON_READ`,
        `trainable` must not be set to `True`.
      aggregation: Indicates how a distributed variable will be aggregated.
        Accepted values are constants defined in the class
        `tf.VariableAggregation`.
      partitioner: Not handled at this time.
      layout: the optional DTensor layout, used for creating DVariable.

    Returns:
      Variable instance.
    '''
def collect_previous_mask(input_tensors):
    """Retrieves the output mask(s) of the previous node.

    Args:
        input_tensors: An arbitrary structure of Tensors.

    Returns:
        A mask tensor or list of mask tensors.
    """
def have_all_keras_metadata(tensors): ...
def generate_placeholders_from_shape(shape): ...
def create_keras_history(tensors):
    """Wraps TensorFlow Operations for compatibility with the Functional API.

    This method checks to see if a Tensor in `tensors` is missing Keras metadata
    and has its origin in a Keras `Input` Layer. If so, this method will replace
    the raw TensorFlow Operations that created this tensor with
    `TensorFlowOpLayer` instances that create identical operations.

    Any Tensors not originating from a Keras `Input` Layer will be treated as
    constants when constructing `TensorFlowOpLayer` instances.

    Args:
      tensors: A structure of Tensors, some of which come from raw TensorFlow
        operations and need to have Keras metadata assigned to them.

    Returns:
      created_layers: List. The `TensorFlowOpLayer` instances created to wrap
        the raw Tensorflow operations.
    """
def unnest_if_single_tensor(input_tensors): ...
def needs_keras_history(tensors, ignore_call_context: bool = False):
    """Check if any Tensors need to be wrapped in TensorFlowOpLayers.

    This will never return True inside a sublayer, because sublayers
    do not need to create Keras History. Otherwise, this returns True
    if one or more of `tensors` originates from a `keras.Input` and
    does not have `_keras_history` set.

    Args:
      tensors: An arbitrary nested structure of Tensors.
      ignore_call_context: Whether to ignore the check of if currently
        outside of a `call` context. This is `True` when creating
        KerasHistory inside `Node`, where we always know that Tensors
        are being used with the Functional API.

    Returns:
      Bool, whether at least one Tensor needs to be wrapped.
    """
def is_in_keras_graph():
    """Returns if currently executing inside of a Keras graph."""
def is_in_eager_or_tf_function():
    """Returns if in eager mode or inside of a tf.function."""
def is_in_tf_function():
    """Returns if inside of a tf.function."""
def uses_keras_history(tensors):
    """Check if at least one Tensor originates from a `keras.Input`.

    This is `True` if at least one Tensor has its origin in a `keras.Input`.
    Any Tensor that originates from a `keras.Input` will have a dependency
    Tensor with a `_keras_history` attribute attached. Tensors that have
    already been checked to not originate from a `keras.Input`
    are marked as `_keras_history_checked`.

    Args:
      tensors: An arbitrary nested structure of Tensors.

    Returns:
      Bool, whether at least one Tensor originates from a `keras.Input`.
    """
def mark_checked(tensors) -> None:
    """Marks that these Tensors should not be tracked.

    This prevents Layers from attempting to create TensorFlowOpLayers
    for these Tensors.

    Args:
      tensors: An arbitrary structure of Tensors.
    """
def call_context():
    """Returns currently active `CallContext`."""

class CallContext:
    """Keeps track of properties currently inside a Layer/Model's `call`.

    Attributes:
      in_call: Whether currently inside the `call` of a Layer.
      layer: The `Layer` whose `call` is currently active.
      inputs: The inputs to the currently active `Layer`.
      build_graph: Whether currently inside a Graph or FuncGraph.
      training: Whether currently executing in training or inference mode.
      saving: Whether currently saving to SavedModel.
      frozen: Whether currently executing inside a `Layer` with `trainable` set
        to `False`.
      in_keras_graph: Whether executing inside the Keras Graph.
    """
    in_call: bool
    def __init__(self) -> None: ...
    def enter(self, layer, inputs, build_graph, training, saving: Incomplete | None = None):
        """Push a Layer and its inputs and state onto the current call context.

        Args:
          layer: The `Layer` whose `call` is currently active.
          inputs: The inputs to the currently active `Layer`.
          build_graph: Whether currently inside a Graph or FuncGraph.
          training: Whether currently executing in training or inference mode.
          saving: Whether currently saving to SavedModel.

        Returns:
          Context manager.
        """
    @property
    def layer(self): ...
    @property
    def inputs(self): ...
    @property
    def build_graph(self): ...
    @property
    def training(self): ...
    @property
    def saving(self): ...
    @property
    def frozen(self): ...
    @property
    def in_keras_graph(self): ...

class CallContextManager:
    """Context manager for `CallContext`."""
    def __init__(self, call_ctx, state) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *exc_info) -> None: ...

def training_arg_passed_to_call(argspec, args, kwargs):
    """Returns whether a user passed the `training` argument in `__call__`."""
def is_subclassed(layer):
    """Returns True if the object is a subclassed layer or subclassed model."""
def from_saved_model(layer):
    """Returns whether the layer is loaded from a SavedModel."""
def check_graph_consistency(tensor: Incomplete | None = None, method: str = 'add_loss', force_raise: bool = False) -> None:
    """Checks that tensors passed to `add_*` method match the Keras graph.

    When one of the `add_*` method is called inside a V2 conditional branch, the
    underlying tensor gets created in a FuncGraph managed by control_flow_v2.
    We need to raise clear error messages in such cases.

    Args:
      tensor: Tensor to check, or `False` if it is known that an error
        should be raised.
      method: Caller method, one of {'add_metric', 'add_loss', 'add_update'}.
      force_raise: If an error should be raised regardless of `tensor`.

    Raises:
      RuntimeError: In case of an out-of-graph tensor.
    """
def mark_as_return(outputs, acd):
    """Marks `outputs` as the return values for automatic control deps."""

V2_DTYPE_BEHAVIOR: Incomplete

def enable_v2_dtype_behavior() -> None:
    """Enable the V2 dtype behavior for Keras layers.

    By default, the V2 dtype behavior is enabled in TensorFlow 2, so this
    function is only useful if `tf.compat.v1.disable_v2_behavior` has been
    called. Since mixed precision requires V2 dtype behavior to be enabled, this
    function allows you to use mixed precision in Keras layers if
    `disable_v2_behavior` has been called.

    When enabled, the dtype of Keras layers defaults to floatx (which is
    typically float32) instead of None. In addition, layers will automatically
    cast floating-point inputs to the layer's dtype.

    >>> x = tf.ones((4, 4, 4, 4), dtype='float64')
    >>> layer = tf.keras.layers.Conv2D(filters=4, kernel_size=2)
    >>> print(layer.dtype)  # float32 since V2 dtype behavior is enabled
    float32
    >>> y = layer(x)  # Layer casts inputs since V2 dtype behavior is enabled
    >>> print(y.dtype.name)
    float32

    A layer author can opt-out their layer from the automatic input casting by
    passing `autocast=False` to the base Layer's constructor. This disables the
    autocasting part of the V2 behavior for that layer, but not the defaulting
    to floatx part of the V2 behavior.

    When a global `tf.keras.mixed_precision.Policy` is set, a Keras layer's
    dtype will default to the global policy instead of floatx. Layers will
    automatically cast inputs to the policy's compute_dtype.
    """
def disable_v2_dtype_behavior() -> None:
    """Disables the V2 dtype behavior for Keras layers.

    See `tf.compat.v1.keras.layers.enable_v2_dtype_behavior`.
    """
def v2_dtype_behavior_enabled():
    """Returns True if the V2 dtype behavior is enabled."""

class TrackableWeightHandler:
    """Keras wrapper for handling Trackable object saving and restoring.

    This class handles Trackables in both V1 and V2 modes, ensuring that they
    can be saved and restored with the correct data and without adding
    additional ops on every save.

    Attributes:
      trackable: The trackable to wrap.
      num_tensors: The number of tensors that this trackable requires for
        saving.
    """
    def __init__(self, trackable) -> None: ...
    @property
    def num_tensors(self): ...
    def set_weights(self, weights) -> None: ...
    def get_tensors(self): ...

def no_ragged_support(inputs, layer_name) -> None: ...
def is_split_variable(v):
    """Returns True if `v` is a PartitionedVariable or a ShardedVariable."""
def has_weights(obj): ...

REVIVED_LOSS_PLACEHOLDER: str
