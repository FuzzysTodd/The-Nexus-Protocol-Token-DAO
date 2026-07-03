from _typeshed import Incomplete
from tensorflow.python.ops import init_ops as init_ops
from tensorflow.python.util import deprecation as deprecation, tf_decorator as tf_decorator, tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export
from tensorflow.tools.docs import doc_controls as doc_controls

def serialize_feature_column(fc):
    """Serializes a FeatureColumn or a raw string key.

  This method should only be used to serialize parent FeatureColumns when
  implementing FeatureColumn.get_config(), else serialize_feature_columns()
  is preferable.

  This serialization also keeps information of the FeatureColumn class, so
  deserialization is possible without knowing the class type. For example:

  a = numeric_column('x')
  a.get_config() gives:
  {
      'key': 'price',
      'shape': (1,),
      'default_value': None,
      'dtype': 'float32',
      'normalizer_fn': None
  }
  While serialize_feature_column(a) gives:
  {
      'class_name': 'NumericColumn',
      'config': {
          'key': 'price',
          'shape': (1,),
          'default_value': None,
          'dtype': 'float32',
          'normalizer_fn': None
      }
  }

  Args:
    fc: A FeatureColumn or raw feature key string.

  Returns:
    Keras serialization for FeatureColumns, leaves string keys unaffected.

  Raises:
    ValueError if called with input that is not string or FeatureColumn.
  """
def deserialize_feature_column(config, custom_objects: Incomplete | None = None, columns_by_name: Incomplete | None = None):
    """Deserializes a `config` generated with `serialize_feature_column`.

  This method should only be used to deserialize parent FeatureColumns when
  implementing FeatureColumn.from_config(), else deserialize_feature_columns()
  is preferable. Returns a FeatureColumn for this config.

  Args:
    config: A Dict with the serialization of feature columns acquired by
      `serialize_feature_column`, or a string representing a raw column.
    custom_objects: A Dict from custom_object name to the associated keras
      serializable objects (FeatureColumns, classes or functions).
    columns_by_name: A Dict[String, FeatureColumn] of existing columns in order
      to avoid duplication.

  Raises:
    ValueError if `config` has invalid format (e.g: expected keys missing,
    or refers to unknown classes).

  Returns:
    A FeatureColumn corresponding to the input `config`.
  """
def serialize_feature_columns(feature_columns):
    """Serializes a list of FeatureColumns.

  Returns a list of Keras-style config dicts that represent the input
  FeatureColumns and can be used with `deserialize_feature_columns` for
  reconstructing the original columns.

  Args:
    feature_columns: A list of FeatureColumns.

  Returns:
    Keras serialization for the list of FeatureColumns.

  Raises:
    ValueError if called with input that is not a list of FeatureColumns.
  """
def deserialize_feature_columns(configs, custom_objects: Incomplete | None = None):
    """Deserializes a list of FeatureColumns configs.

  Returns a list of FeatureColumns given a list of config dicts acquired by
  `serialize_feature_columns`.

  Args:
    configs: A list of Dicts with the serialization of feature columns acquired
      by `serialize_feature_columns`.
    custom_objects: A Dict from custom_object name to the associated keras
      serializable objects (FeatureColumns, classes or functions).

  Returns:
    FeatureColumn objects corresponding to the input configs.

  Raises:
    ValueError if called with input that is not a list of FeatureColumns.
  """
