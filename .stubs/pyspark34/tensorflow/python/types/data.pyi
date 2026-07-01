import abc
from tensorflow.python.util.tf_export import tf_export as tf_export

class DatasetV2(abc.ABC):
    """Represents the TensorFlow 2 type `tf.data.Dataset`."""
class DatasetV1(DatasetV2, abc.ABC):
    """Represents the TensorFlow 1 type `tf.data.Dataset`."""
