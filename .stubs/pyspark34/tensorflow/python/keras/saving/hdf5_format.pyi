from _typeshed import Incomplete
from tensorflow.python.keras import backend as backend, optimizer_v1 as optimizer_v1
from tensorflow.python.keras.saving import saving_utils as saving_utils
from tensorflow.python.keras.saving.saved_model import json_utils as json_utils
from tensorflow.python.keras.utils.generic_utils import LazyLoader as LazyLoader
from tensorflow.python.keras.utils.io_utils import ask_to_proceed_with_overwrite as ask_to_proceed_with_overwrite
from tensorflow.python.platform import gfile as gfile

HDF5_OBJECT_HEADER_LIMIT: int
sequential_lib: Incomplete

def save_model_to_hdf5(model, filepath, overwrite: bool = True, include_optimizer: bool = True) -> None:
    """Saves a model to a HDF5 file.

  The saved model contains:
      - the model's configuration (topology)
      - the model's weights
      - the model's optimizer's state (if any)

  Thus the saved model can be reinstantiated in
  the exact same state, without any of the code
  used for model definition or training.

  Args:
      model: Keras model instance to be saved.
      filepath: One of the following:
          - String, path where to save the model
          - `h5py.File` object where to save the model
      overwrite: Whether we should overwrite any existing
          model at the target location, or instead
          ask the user with a manual prompt.
      include_optimizer: If True, save optimizer's state together.

  Raises:
      ImportError: if h5py is not available.
  """
def load_model_from_hdf5(filepath, custom_objects: Incomplete | None = None, compile: bool = True):
    """Loads a model saved via `save_model_to_hdf5`.

  Args:
      filepath: One of the following:
          - String, path to the saved model
          - `h5py.File` object from which to load the model
      custom_objects: Optional dictionary mapping names
          (strings) to custom classes or functions to be
          considered during deserialization.
      compile: Boolean, whether to compile the model
          after loading.

  Returns:
      A Keras model instance. If an optimizer was found
      as part of the saved model, the model is already
      compiled. Otherwise, the model is uncompiled and
      a warning will be displayed. When `compile` is set
      to False, the compilation is omitted without any
      warning.

  Raises:
      ImportError: if h5py is not available.
      ValueError: In case of an invalid savefile.
  """
def preprocess_weights_for_loading(layer, weights, original_keras_version: Incomplete | None = None, original_backend: Incomplete | None = None):
    """Preprocess layer weights between different Keras formats.

  Converts layers weights from Keras 1 format to Keras 2 and also weights of
  CuDNN layers in Keras 2.

  Args:
      layer: Layer instance.
      weights: List of weights values (Numpy arrays).
      original_keras_version: Keras version for the weights, as a string.
      original_backend: Keras backend the weights were trained with,
          as a string.

  Returns:
      A list of weights values (Numpy arrays).
  """
def save_optimizer_weights_to_hdf5_group(hdf5_group, optimizer) -> None:
    """Saves optimizer weights of a optimizer to a HDF5 group.

  Args:
      hdf5_group: HDF5 group.
      optimizer: optimizer instance.
  """
def load_optimizer_weights_from_hdf5_group(hdf5_group):
    """Load optimizer weights from a HDF5 group.

  Args:
      hdf5_group: A pointer to a HDF5 group.

  Returns:
      data: List of optimizer weight names.
  """
def save_weights_to_hdf5_group(f, layers):
    """Saves the weights of a list of layers to a HDF5 group.

  Args:
      f: HDF5 group.
      layers: List of layer instances.
  """
def load_weights_from_hdf5_group(f, layers) -> None:
    """Implements topological (order-based) weight loading.

  Args:
      f: A pointer to a HDF5 group.
      layers: a list of target layers.

  Raises:
      ValueError: in case of mismatch between provided layers
          and weights file.
  """
def load_weights_from_hdf5_group_by_name(f, layers, skip_mismatch: bool = False) -> None:
    """Implements name-based weight loading.

  (instead of topological weight loading).

  Layers that have no matching name are skipped.

  Args:
      f: A pointer to a HDF5 group.
      layers: a list of target layers.
      skip_mismatch: Boolean, whether to skip loading of layers
          where there is a mismatch in the number of weights,
          or a mismatch in the shape of the weights.

  Raises:
      ValueError: in case of mismatch between provided layers
          and weights file and skip_match=False.
  """
def save_attributes_to_hdf5_group(group, name, data) -> None:
    """Saves attributes (data) of the specified name into the HDF5 group.

  This method deals with an inherent problem of HDF5 file which is not
  able to store data larger than HDF5_OBJECT_HEADER_LIMIT bytes.

  Args:
      group: A pointer to a HDF5 group.
      name: A name of the attributes to save.
      data: Attributes data to store.

  Raises:
    RuntimeError: If any single attribute is too large to be saved.
  """
def load_attributes_from_hdf5_group(group, name):
    """Loads attributes of the specified name from the HDF5 group.

  This method deals with an inherent problem
  of HDF5 file which is not able to store
  data larger than HDF5_OBJECT_HEADER_LIMIT bytes.

  Args:
      group: A pointer to a HDF5 group.
      name: A name of the attributes to load.

  Returns:
      data: Attributes data.
  """
