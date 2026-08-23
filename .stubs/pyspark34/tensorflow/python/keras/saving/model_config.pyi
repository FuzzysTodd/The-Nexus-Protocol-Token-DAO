from _typeshed import Incomplete
from tensorflow.python.keras.saving.saved_model import json_utils as json_utils
from tensorflow.python.util.tf_export import keras_export as keras_export

def model_from_config(config, custom_objects: Incomplete | None = None):
    """Instantiates a Keras model from its config.

  Usage:
  ```
  # for a Functional API model
  tf.keras.Model().from_config(model.get_config())

  # for a Sequential model
  tf.keras.Sequential().from_config(model.get_config())
  ```

  Args:
      config: Configuration dictionary.
      custom_objects: Optional dictionary mapping names
          (strings) to custom classes or functions to be
          considered during deserialization.

  Returns:
      A Keras model instance (uncompiled).

  Raises:
      TypeError: if `config` is not a dictionary.
  """
def model_from_yaml(yaml_string, custom_objects: Incomplete | None = None) -> None:
    """Parses a yaml model configuration file and returns a model instance.

  Note: Since TF 2.6, this method is no longer supported and will raise a
  RuntimeError.

  Args:
      yaml_string: YAML string or open file encoding a model configuration.
      custom_objects: Optional dictionary mapping names
          (strings) to custom classes or functions to be
          considered during deserialization.

  Returns:
      A Keras model instance (uncompiled).

  Raises:
      RuntimeError: announces that the method poses a security risk
  """
def model_from_json(json_string, custom_objects: Incomplete | None = None):
    """Parses a JSON model configuration string and returns a model instance.

  Usage:

  >>> model = tf.keras.Sequential([
  ...     tf.keras.layers.Dense(5, input_shape=(3,)),
  ...     tf.keras.layers.Softmax()])
  >>> config = model.to_json()
  >>> loaded_model = tf.keras.models.model_from_json(config)

  Args:
      json_string: JSON string encoding a model configuration.
      custom_objects: Optional dictionary mapping names
          (strings) to custom classes or functions to be
          considered during deserialization.

  Returns:
      A Keras model instance (uncompiled).
  """
