from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_conversion_registry as tensor_conversion_registry
from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.ops import array_ops as array_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.saved_model import path_helpers as path_helpers
from tensorflow.python.trackable import base as base
from tensorflow.python.util.tf_export import tf_export as tf_export

class Asset(base.Trackable):
    '''Represents a file asset to hermetically include in a SavedModel.

  A SavedModel can include arbitrary files, called assets, that are needed
  for its use. For example a vocabulary file used initialize a lookup table.

  When a trackable object is exported via `tf.saved_model.save()`, all the
  `Asset`s reachable from it are copied into the SavedModel assets directory.
  Upon loading, the assets and the serialized functions that depend on them
  will refer to the correct filepaths inside the SavedModel directory.

  Example:

  ```
  filename = tf.saved_model.Asset("file.txt")

  @tf.function(input_signature=[])
  def func():
    return tf.io.read_file(filename)

  trackable_obj = tf.train.Checkpoint()
  trackable_obj.func = func
  trackable_obj.filename = filename
  tf.saved_model.save(trackable_obj, "/tmp/saved_model")

  # The created SavedModel is hermetic, it does not depend on
  # the original file and can be moved to another path.
  tf.io.gfile.remove("file.txt")
  tf.io.gfile.rename("/tmp/saved_model", "/tmp/new_location")

  reloaded_obj = tf.saved_model.load("/tmp/new_location")
  print(reloaded_obj.func())
  ```

  Attributes:
    asset_path: A path, or a 0-D `tf.string` tensor with path to the asset.
  '''
    def __init__(self, path) -> None:
        """Record the full path to the asset."""
    @property
    def asset_path(self):
        """Fetch the current asset path."""
