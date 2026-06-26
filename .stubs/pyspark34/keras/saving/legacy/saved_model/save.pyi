from _typeshed import Incomplete
from keras import backend as backend
from keras.protobuf import saved_metadata_pb2 as saved_metadata_pb2, versions_pb2 as versions_pb2
from keras.saving.legacy import saving_utils as saving_utils, serialization as serialization
from keras.saving.legacy.saved_model import constants as constants, save_impl as save_impl, utils as utils
from keras.utils.generic_utils import LazyLoader as LazyLoader
from keras.utils.io_utils import ask_to_proceed_with_overwrite as ask_to_proceed_with_overwrite

base_layer: Incomplete
training_lib: Incomplete

def save(model, filepath, overwrite, include_optimizer, signatures: Incomplete | None = None, options: Incomplete | None = None, save_traces: bool = True) -> None:
    """Saves a model as a SavedModel to the filepath.

    Args:
      model: Keras model instance to be saved.
      filepath: String path to save the model.
      overwrite: whether to overwrite the existing filepath.
      include_optimizer: If True, save the model's optimizer state.
      signatures: Signatures to save with the SavedModel. Applicable to the 'tf'
        format only. Please see the `signatures` argument in
        `tf.saved_model.save` for details.
      options: (only applies to SavedModel format) `tf.saved_model.SaveOptions`
        object that specifies options for saving to SavedModel.
      save_traces: (only applies to SavedModel format) When enabled, the
        SavedModel will store the function traces for each layer. This
        can be disabled, so that only the configs of each layer are stored.
        Defaults to `True`. Disabling this will decrease serialization time
        and reduce file size, but it requires that all custom layers/models
        implement a `get_config()` method.

    Raises:
      ValueError: if the model's inputs have not been defined.
    """
def generate_keras_metadata(saved_nodes, node_paths):
    """Constructs a KerasMetadata proto with the metadata of each object."""
