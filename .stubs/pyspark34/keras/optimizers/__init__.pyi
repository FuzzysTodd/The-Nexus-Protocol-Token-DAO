from _typeshed import Incomplete
from keras import backend as backend
from keras.optimizers import adadelta as adadelta, adafactor as adafactor, adagrad as adagrad, adam as adam, adamax as adamax, adamw as adamw, ftrl as ftrl, nadam as nadam, rmsprop as rmsprop, sgd as sgd
from keras.optimizers.legacy.adadelta import Adadelta as Adadelta
from keras.optimizers.legacy.adagrad import Adagrad as Adagrad
from keras.optimizers.legacy.adam import Adam as Adam
from keras.optimizers.legacy.adamax import Adamax as Adamax
from keras.optimizers.legacy.ftrl import Ftrl as Ftrl
from keras.optimizers.legacy.gradient_descent import SGD as SGD
from keras.optimizers.legacy.nadam import Nadam as Nadam
from keras.optimizers.legacy.rmsprop import RMSprop as RMSprop
from keras.optimizers.optimizer_v1 import Optimizer as Optimizer, TFOptimizer as TFOptimizer
from keras.optimizers.schedules import learning_rate_schedule as learning_rate_schedule
from keras.saving.legacy.serialization import deserialize_keras_object as deserialize_keras_object, serialize_keras_object as serialize_keras_object

def serialize(optimizer, use_legacy_format: bool = False):
    """Serialize the optimizer configuration to JSON compatible python dict.

    The configuration can be used for persistence and reconstruct the
    `Optimizer` instance again.

    >>> tf.keras.optimizers.serialize(tf.keras.optimizers.legacy.SGD())
    {'class_name': 'SGD', 'config': {'name': 'SGD', 'learning_rate': 0.01,
                                     'decay': 0.0, 'momentum': 0.0,
                                     'nesterov': False}}

    Args:
      optimizer: An `Optimizer` instance to serialize.

    Returns:
      Python dict which contains the configuration of the input optimizer.
    """
def is_arm_mac(): ...
def deserialize(config, custom_objects: Incomplete | None = None, use_legacy_format: bool = False, **kwargs):
    """Inverse of the `serialize` function.

    Args:
        config: Optimizer configuration dictionary.
        custom_objects: Optional dictionary mapping names (strings) to custom
            objects (classes and functions) to be considered during
            deserialization.

    Returns:
        A Keras Optimizer instance.
    """
def convert_to_legacy_optimizer(optimizer):
    """Convert experimental optimizer to legacy optimizer.

    This function takes in a `tf.keras.optimizers.experimental.Optimizer`
    instance and converts it to the corresponding
    `tf.keras.optimizers.legacy.Optimizer` instance.
    For example, `tf.keras.optimizers.experimental.Adam(...)` to
    `tf.keras.optimizers.legacy.Adam(...)`.

    Args:
        optimizer: An instance of `tf.keras.optimizers.experimental.Optimizer`.
    """
def get(identifier, **kwargs):
    """Retrieves a Keras Optimizer instance.

    Args:
        identifier: Optimizer identifier, one of - String: name of an optimizer
          - Dictionary: configuration dictionary. - Keras Optimizer instance (it
          will be returned unchanged). - TensorFlow Optimizer instance (it will
          be wrapped as a Keras Optimizer).

    Returns:
        A Keras Optimizer instance.

    Raises:
        ValueError: If `identifier` cannot be interpreted.
    """
