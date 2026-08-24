from _typeshed import Incomplete
from keras.saving.legacy.saved_model import constants as constants, save_impl as save_impl
from keras.utils.generic_utils import LazyLoader as LazyLoader

base_layer: Incomplete
training_lib: Incomplete
metrics: Incomplete
base_rnn: Incomplete

class SerializedAttributes:
    '''Class that tracks and validates all serialization attributes.

    Keras models contain many Python-defined components. For example, the
    trainable_variable property lists the model\'s trainable variables by
    recursively retrieving the trainable variables from each of the child
    layers.  Another example is model.call, a python function that calls child
    layers and adds ops to the backend graph.

    Only Tensorflow checkpointable objects and functions can be serialized to
    SavedModel. Serializing a Keras model as-is results in a checkpointable
    object that does not resemble a Keras model at all. Thus, extra
    checkpointable objects and functions must be created during serialization.

    **Defining new serialized attributes**
    Child classes should be defined using:
      SerializedAttributes.with_attributes(
          \'name\', checkpointable_objects=[...],
          functions=[...], copy_from=[...])
    This class is used to cache generated checkpointable objects and functions,
    ensuring that new objects and functions are generated a single time.

    **Usage during serialization**
    Each Layer/Model object should have a corresponding instance of
    SerializedAttributes. Create a new instance by calling
    `SerializedAttributes.new(obj)`. Objects and functions may be saved using
    `.set_and_validate_checkpointable_objects`/`.set_and_and_validate_functions`.
    The properties `.checkpointable_objects` and `.functions` returns the cached
    values.

    **Adding/changing attributes to save to SavedModel**
    1. Change the call to `SerializedAttributes.with_attributes` in the correct
       class:
       - CommonEndpoints: Base attributes to be added during serialization. If
         these attributes are present in a Trackable object, it can be
         deserialized to a Keras Model.
       - LayerAttributes: Attributes to serialize for Layer objects.
       - ModelAttributes: Attributes to serialize for Model objects.
    2. Update class docstring
    3. Update arguments to any calls to `set_and_validate_*`. For example, if
       `call_raw_tensors` is added to the ModelAttributes function list, then
       a `call_raw_tensors` function should be passed to
       `set_and_validate_functions`.

    **Common endpoints vs other attributes**
    Only common endpoints are attached directly to the root object.
    Keras-specific attributes are saved to a separate trackable object with the
    name "keras_api".  The number of objects attached to the root is limited
    because any naming conflicts will cause user code to break.

    Another reason is that this will only affect users who call
    `tf.saved_model.load` instead of `tf.keras.models.load_model`. These are
    advanced users who are likely to have defined their own tf.functions and
    trackable objects. The added Keras-specific attributes are kept out of the
    way in the "keras_api" namespace.

    Properties defined in this class may be used to filter out keras-specific
    attributes:
    - `functions_to_serialize`: Returns dict of functions to attach to the root
        object.
    - `checkpointable_objects_to_serialize`: Returns dict of objects to attach
         to the root object (including separate trackable object containing
         keras-specific attributes)

    All changes to the serialized attributes must be backwards-compatible, so
    attributes should not be removed or modified without sufficient
    justification.
    '''
    @staticmethod
    def with_attributes(name, checkpointable_objects: Incomplete | None = None, functions: Incomplete | None = None, copy_from: Incomplete | None = None):
        """Creates a subclass with all attributes as specified in the arguments.

        Args:
          name: Name of subclass
          checkpointable_objects: List of checkpointable objects to be
            serialized in the SavedModel.
          functions: List of functions to be serialized in the SavedModel.
          copy_from: List of other SerializedAttributes subclasses. The returned
            class will copy checkpoint objects/functions from each subclass.

        Returns:
          Child class with attributes as defined in the `checkpointable_objects`
          and `functions` lists.
        """
    @staticmethod
    def new(obj):
        """Returns a new SerializedAttribute object."""
    def __init__(self) -> None: ...
    @property
    def functions(self):
        """Returns dictionary of all functions."""
    @property
    def checkpointable_objects(self):
        """Returns dictionary of all checkpointable objects."""
    @property
    def functions_to_serialize(self):
        """Returns functions to attach to the root object during
        serialization."""
    @property
    def objects_to_serialize(self):
        """Returns objects to attach to the root object during serialization."""
    def set_and_validate_functions(self, function_dict):
        """Saves function dictionary, and validates dictionary values."""
    def set_and_validate_objects(self, object_dict):
        """Saves objects to a dictionary, and validates the values."""

class CommonEndpoints(Incomplete):
    """Common endpoints shared by all models loadable by Keras.

    List of all attributes:
      variables: List of all variables in the model and its sublayers.
      trainable_variables: List of all trainable variables in the model and its
        sublayers.
      regularization_losses: List of all unconditional losses (losses not
        dependent on the inputs) in the model and its sublayers.
      __call__: Function that takes inputs and returns the outputs of the model
        call function.
      call_and_return_all_conditional_losses: Function that returns a tuple of
        (call function outputs, list of all losses that depend on the inputs).
      _default_save_signature: Traced model call function. This is only included
        if the top level exported object is a Keras model.
    """
class LayerAttributes(Incomplete):
    """Layer checkpointable objects + functions saved to the SavedModel.

    List of all attributes:
      All attributes from CommonEndpoints
      non_trainable_variables: List of non-trainable variables in the layer and
        its sublayers.
      layers: List of all sublayers.
      metrics: List of all metrics in the layer and its sublayers.
      call_and_return_conditional_losses: Function that takes inputs and returns
        a tuple of (outputs of the call function, list of input-dependent
        losses).  The list of losses excludes the activity regularizer function,
        which is separate to allow the deserialized Layer object to define a
        different activity regularizer.
      activity_regularizer_fn: Callable that returns the activity regularizer
        loss
      layer_regularization_losses: List of losses owned only by this layer.
      layer_metrics: List of metrics owned by this layer.
    """
class ModelAttributes(Incomplete):
    """Model checkpointable objects + functions saved to the SavedModel.

    List of all attributes:
      All attributes from LayerAttributes (including CommonEndpoints)
    """
class MetricAttributes(Incomplete):
    """Attributes that are added to Metric objects when saved to SavedModel.

    List of all attributes:
      variables: list of all variables
    """
class RNNAttributes(Incomplete):
    """RNN checkpointable objects + functions that are saved to the SavedModel.

    List of all attributes:
      All attributes from LayerAttributes (including CommonEndpoints)
      states: List of state variables
    """
