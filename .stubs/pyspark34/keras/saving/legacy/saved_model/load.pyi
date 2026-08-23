from _typeshed import Incomplete
from keras import backend as backend, regularizers as regularizers
from keras.engine import input_spec as input_spec
from keras.optimizers.legacy import optimizer_v2 as optimizer_v2
from keras.protobuf import saved_metadata_pb2 as saved_metadata_pb2, versions_pb2 as versions_pb2
from keras.saving import object_registration as object_registration
from keras.saving.legacy import saving_utils as saving_utils, serialization as serialization
from keras.saving.legacy.saved_model import constants as constants, json_utils as json_utils, utils as utils
from keras.saving.legacy.saved_model.serialized_attributes import CommonEndpoints as CommonEndpoints
from keras.utils import layer_utils as layer_utils, metrics_utils as metrics_utils, tf_inspect as tf_inspect
from keras.utils.generic_utils import LazyLoader as LazyLoader

models_lib: Incomplete
base_layer: Incomplete
layers_module: Incomplete
input_layer: Incomplete
functional_lib: Incomplete
training_lib: Incomplete
training_lib_v1: Incomplete
metrics: Incomplete
base_rnn: Incomplete
PUBLIC_ATTRIBUTES: Incomplete

def load(path, compile: bool = True, options: Incomplete | None = None):
    """Loads Keras objects from a SavedModel.

    Any Keras layer or model saved to the SavedModel will be loaded back
    as Keras objects. Other objects are loaded as regular trackable objects
    (same as `tf.saved_model.load`).

    Currently, Keras saving/loading only retains the Keras object's weights,
    losses, and call function.

    The loaded model can be re-compiled, but the original optimizer, compiled
    loss functions, and metrics are not retained. This is temporary, and
    `model.save` will soon be able to serialize compiled models.

    Args:
      path: Path to SavedModel.
      compile: If true, compile the model after loading it.
      options: Optional `tf.saved_model.LoadOptions` object that specifies
        options for loading from SavedModel.

    Returns:
      Object loaded from SavedModel.
    """

class KerasObjectLoader:
    """Loader that recreates Keras objects (e.g.

    layers, models).

    Layers and models are revived from either the config or SavedModel following
    these rules:
    1. If object is a graph network (i.e. Sequential or Functional) then it will
       be initialized using the structure from the config only after the
       children layers have been created. Graph networks must be initialized
       with inputs and outputs, so all child layers must be created beforehand.
    2. If object's config exists and the class can be found, then revive from
       config.
    3. Object may have already been created if its parent was revived from
       config. In this case, do nothing.
    4. If nothing of the above applies, compose the various artifacts from the
       SavedModel to create a subclassed layer or model. At this time, custom
       metrics are not supported.

    """
    loaded_nodes: Incomplete
    model_layer_dependencies: Incomplete
    def __init__(self, metadata, object_graph_def) -> None: ...
    def del_tracking(self) -> None:
        """Removes tracked references that are only used when loading the
        model."""
    def load_layers(self, compile: bool = True) -> None:
        """Load all layer nodes from the metadata."""
    def get_path(self, node_id): ...
    def finalize_objects(self) -> None:
        """Finish setting up Keras objects.

        This function is executed after all objects and functions have been
        created.  Call functions and losses are attached to each layer, and once
        all layers have been fully set up, graph networks are initialized.

        Subclassed models that are revived from the SavedModel are treated like
        layers, and have their call/loss functions attached here.
        """

def revive_custom_object(identifier, metadata):
    """Revives object from SavedModel."""

class RevivedLayer:
    """Keras layer loaded from a SavedModel."""
    @property
    def keras_api(self): ...
    def get_config(self): ...

class RevivedInputLayer:
    """InputLayer loaded from a SavedModel."""
    def get_config(self): ...

def recursively_deserialize_keras_object(config, module_objects: Incomplete | None = None):
    """Deserialize Keras object from a nested structure."""
def infer_inputs_from_restored_call_function(fn):
    """Returns TypeSpec of inputs from a restored call function.

    Args:
      fn: Restored layer call function. It is assumed that `fn` has at least one
        concrete function and that the inputs are in the first argument.

    Returns:
      TypeSpec of call function inputs in the form of (args, kwargs)
    """

class RevivedNetwork(RevivedLayer):
    """Keras network of layers loaded from a SavedModel."""
