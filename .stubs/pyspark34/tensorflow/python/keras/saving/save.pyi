from _typeshed import Incomplete
from tensorflow.python import tf2 as tf2
from tensorflow.python.keras.saving import hdf5_format as hdf5_format, saving_utils as saving_utils
from tensorflow.python.keras.saving.saved_model import load_context as load_context
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.keras.utils.io_utils import path_to_string as path_to_string
from tensorflow.python.util.tf_export import keras_export as keras_export

def save_model(model, filepath, overwrite: bool = True, include_optimizer: bool = True, save_format: Incomplete | None = None, signatures: Incomplete | None = None, options: Incomplete | None = None, save_traces: bool = True) -> None:
    '''Saves a model as a TensorFlow SavedModel or HDF5 file.

  See the [Serialization and Saving guide](https://keras.io/guides/serialization_and_saving/)
  for details.

  Usage:

  >>> model = tf.keras.Sequential([
  ...     tf.keras.layers.Dense(5, input_shape=(3,)),
  ...     tf.keras.layers.Softmax()])
  >>> model.save(\'/tmp/model\')
  >>> loaded_model = tf.keras.models.load_model(\'/tmp/model\')
  >>> x = tf.random.uniform((10, 3))
  >>> assert np.allclose(model.predict(x), loaded_model.predict(x))

  The SavedModel and HDF5 file contains:

  - the model\'s configuration (topology)
  - the model\'s weights
  - the model\'s optimizer\'s state (if any)

  Thus models can be reinstantiated in the exact same state, without any of the
  code used for model definition or training.

  Note that the model weights may have different scoped names after being
  loaded. Scoped names include the model/layer names, such as
  `"dense_1/kernel:0"`. It is recommended that you use the layer properties to
  access specific variables, e.g. `model.get_layer("dense_1").kernel`.

  __SavedModel serialization format__

  Keras SavedModel uses `tf.saved_model.save` to save the model and all
  trackable objects attached to the model (e.g. layers and variables). The model
  config, weights, and optimizer are saved in the SavedModel. Additionally, for
  every Keras layer attached to the model, the SavedModel stores:

    * the config and metadata -- e.g. name, dtype, trainable status
    * traced call and loss functions, which are stored as TensorFlow subgraphs.

  The traced functions allow the SavedModel format to save and load custom
  layers without the original class definition.

  You can choose to not save the traced functions by disabling the `save_traces`
  option. This will decrease the time it takes to save the model and the
  amount of disk space occupied by the output SavedModel. If you enable this
  option, then you _must_ provide all custom class definitions when loading
  the model. See the `custom_objects` argument in `tf.keras.models.load_model`.

  Args:
      model: Keras model instance to be saved.
      filepath: One of the following:
        - String or `pathlib.Path` object, path where to save the model
        - `h5py.File` object where to save the model
      overwrite: Whether we should overwrite any existing model at the target
        location, or instead ask the user with a manual prompt.
      include_optimizer: If True, save optimizer\'s state together.
      save_format: Either \'tf\' or \'h5\', indicating whether to save the model
        to Tensorflow SavedModel or HDF5. Defaults to \'tf\' in TF 2.X, and \'h5\'
        in TF 1.X.
      signatures: Signatures to save with the SavedModel. Applicable to the \'tf\'
        format only. Please see the `signatures` argument in
        `tf.saved_model.save` for details.
      options: (only applies to SavedModel format) `tf.saved_model.SaveOptions`
        object that specifies options for saving to SavedModel.
      save_traces: (only applies to SavedModel format) When enabled, the
        SavedModel will store the function traces for each layer. This
        can be disabled, so that only the configs of each layer are stored.
        Defaults to `True`. Disabling this will decrease serialization time and
        reduce file size, but it requires that all custom layers/models
        implement a `get_config()` method.

  Raises:
      ImportError: If save format is hdf5, and h5py is not available.
  '''
def load_model(filepath, custom_objects: Incomplete | None = None, compile: bool = True, options: Incomplete | None = None):
    '''Loads a model saved via `model.save()`.

  Usage:

  >>> model = tf.keras.Sequential([
  ...     tf.keras.layers.Dense(5, input_shape=(3,)),
  ...     tf.keras.layers.Softmax()])
  >>> model.save(\'/tmp/model\')
  >>> loaded_model = tf.keras.models.load_model(\'/tmp/model\')
  >>> x = tf.random.uniform((10, 3))
  >>> assert np.allclose(model.predict(x), loaded_model.predict(x))

  Note that the model weights may have different scoped names after being
  loaded. Scoped names include the model/layer names, such as
  `"dense_1/kernel:0"`. It is recommended that you use the layer properties to
  access specific variables, e.g. `model.get_layer("dense_1").kernel`.

  Args:
      filepath: One of the following:
          - String or `pathlib.Path` object, path to the saved model
          - `h5py.File` object from which to load the model
      custom_objects: Optional dictionary mapping names
          (strings) to custom classes or functions to be
          considered during deserialization.
      compile: Boolean, whether to compile the model
          after loading.
      options: Optional `tf.saved_model.LoadOptions` object that specifies
        options for loading from SavedModel.

  Returns:
      A Keras model instance. If the original model was compiled, and saved with
      the optimizer, then the returned model will be compiled. Otherwise, the
      model will be left uncompiled. In the case that an uncompiled model is
      returned, a warning is displayed if the `compile` argument is set to
      `True`.

  Raises:
      ImportError: if loading from an hdf5 file and h5py is not available.
      IOError: In case of an invalid savefile.
  '''
