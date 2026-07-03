from _typeshed import Incomplete
from tensorflow.python import tf2 as tf2
from tensorflow.python.keras.initializers import initializers_v1 as initializers_v1, initializers_v2 as initializers_v2
from tensorflow.python.keras.utils import generic_utils as generic_utils
from tensorflow.python.ops import init_ops as init_ops
from tensorflow.python.util.tf_export import keras_export as keras_export

LOCAL: Incomplete

def populate_deserializable_objects():
    """Populates dict ALL_OBJECTS with every built-in initializer.
  """
def serialize(initializer): ...
def deserialize(config, custom_objects: Incomplete | None = None):
    """Return an `Initializer` object from its config."""
def get(identifier):
    """Retrieve a Keras initializer by the identifier.

  The `identifier` may be the string name of a initializers function or class (
  case-sensitively).

  >>> identifier = 'Ones'
  >>> tf.keras.initializers.deserialize(identifier)
  <...keras.initializers.initializers_v2.Ones...>

  You can also specify `config` of the initializer to this function by passing
  dict containing `class_name` and `config` as an identifier. Also note that the
  `class_name` must map to a `Initializer` class.

  >>> cfg = {'class_name': 'Ones', 'config': {}}
  >>> tf.keras.initializers.deserialize(cfg)
  <...keras.initializers.initializers_v2.Ones...>

  In the case that the `identifier` is a class, this method will return a new
  instance of the class by its constructor.

  Args:
    identifier: String or dict that contains the initializer name or
      configurations.

  Returns:
    Initializer instance base on the input identifier.

  Raises:
    ValueError: If the input identifier is not a supported type or in a bad
      format.
  """
