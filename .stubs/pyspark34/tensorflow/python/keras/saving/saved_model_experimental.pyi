from _typeshed import Incomplete
from tensorflow.python.checkpoint import graph_view as graph_view
from tensorflow.python.client import session as session
from tensorflow.python.framework import ops as ops
from tensorflow.python.keras import backend as backend, optimizer_v1 as optimizer_v1
from tensorflow.python.keras.optimizer_v2 import optimizer_v2 as optimizer_v2
from tensorflow.python.keras.saving import model_config as model_config, saving_utils as saving_utils
from tensorflow.python.keras.utils import mode_keys as mode_keys
from tensorflow.python.keras.utils.generic_utils import LazyLoader as LazyLoader
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import variables as variables
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.saved_model import constants as constants
from tensorflow.python.util import compat as compat, nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export

metrics_lib: Incomplete
models_lib: Incomplete
sequential: Incomplete
SAVED_MODEL_FILENAME_JSON: str

def export_saved_model(model, saved_model_path, custom_objects: Incomplete | None = None, as_text: bool = False, input_signature: Incomplete | None = None, serving_only: bool = False) -> None:
    """Exports a `tf.keras.Model` as a Tensorflow SavedModel.

  Note that at this time, subclassed models can only be saved using
  `serving_only=True`.

  The exported `SavedModel` is a standalone serialization of Tensorflow objects,
  and is supported by TF language APIs and the Tensorflow Serving system.
  To load the model, use the function
  `tf.keras.experimental.load_from_saved_model`.

  The `SavedModel` contains:

  1. a checkpoint containing the model weights.
  2. a `SavedModel` proto containing the Tensorflow backend graph. Separate
     graphs are saved for prediction (serving), train, and evaluation. If
     the model has not been compiled, then only the graph computing predictions
     will be exported.
  3. the model's json config. If the model is subclassed, this will only be
     included if the model's `get_config()` method is overwritten.

  Example:

  ```python
  import tensorflow as tf

  # Create a tf.keras model.
  model = tf.keras.Sequential()
  model.add(tf.keras.layers.Dense(1, input_shape=[10]))
  model.summary()

  # Save the tf.keras model in the SavedModel format.
  path = '/tmp/simple_keras_model'
  tf.keras.experimental.export_saved_model(model, path)

  # Load the saved keras model back.
  new_model = tf.keras.experimental.load_from_saved_model(path)
  new_model.summary()
  ```

  Args:
    model: A `tf.keras.Model` to be saved. If the model is subclassed, the flag
      `serving_only` must be set to True.
    saved_model_path: a string specifying the path to the SavedModel directory.
    custom_objects: Optional dictionary mapping string names to custom classes
      or functions (e.g. custom loss functions).
    as_text: bool, `False` by default. Whether to write the `SavedModel` proto
      in text format. Currently unavailable in serving-only mode.
    input_signature: A possibly nested sequence of `tf.TensorSpec` objects, used
      to specify the expected model inputs. See `tf.function` for more details.
    serving_only: bool, `False` by default. When this is true, only the
      prediction graph is saved.

  Raises:
    NotImplementedError: If the model is a subclassed model, and serving_only is
      False.
    ValueError: If the input signature cannot be inferred from the model.
    AssertionError: If the SavedModel directory already exists and isn't empty.
  """
def create_placeholder(spec): ...
def load_from_saved_model(saved_model_path, custom_objects: Incomplete | None = None):
    """Loads a keras Model from a SavedModel created by `export_saved_model()`.

  This function reinstantiates model state by:
  1) loading model topology from json (this will eventually come
     from metagraph).
  2) loading model weights from checkpoint.

  Example:

  ```python
  import tensorflow as tf

  # Create a tf.keras model.
  model = tf.keras.Sequential()
  model.add(tf.keras.layers.Dense(1, input_shape=[10]))
  model.summary()

  # Save the tf.keras model in the SavedModel format.
  path = '/tmp/simple_keras_model'
  tf.keras.experimental.export_saved_model(model, path)

  # Load the saved keras model back.
  new_model = tf.keras.experimental.load_from_saved_model(path)
  new_model.summary()
  ```

  Args:
    saved_model_path: a string specifying the path to an existing SavedModel.
    custom_objects: Optional dictionary mapping names
        (strings) to custom classes or functions to be
        considered during deserialization.

  Returns:
    a keras.Model instance.
  """
