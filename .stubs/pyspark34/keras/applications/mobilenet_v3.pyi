from _typeshed import Incomplete
from keras import backend as backend, models as models
from keras.applications import imagenet_utils as imagenet_utils
from keras.layers import VersionAwareLayers as VersionAwareLayers
from keras.utils import data_utils as data_utils, layer_utils as layer_utils

BASE_WEIGHT_PATH: str
WEIGHTS_HASHES: Incomplete
layers: Incomplete
BASE_DOCSTRING: str

def MobileNetV3(stack_fn, last_point_ch, input_shape: Incomplete | None = None, alpha: float = 1.0, model_type: str = 'large', minimalistic: bool = False, include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, classes: int = 1000, pooling: Incomplete | None = None, dropout_rate: float = 0.2, classifier_activation: str = 'softmax', include_preprocessing: bool = True): ...
def MobileNetV3Small(input_shape: Incomplete | None = None, alpha: float = 1.0, minimalistic: bool = False, include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, classes: int = 1000, pooling: Incomplete | None = None, dropout_rate: float = 0.2, classifier_activation: str = 'softmax', include_preprocessing: bool = True): ...
def MobileNetV3Large(input_shape: Incomplete | None = None, alpha: float = 1.0, minimalistic: bool = False, include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, classes: int = 1000, pooling: Incomplete | None = None, dropout_rate: float = 0.2, classifier_activation: str = 'softmax', include_preprocessing: bool = True): ...
def relu(x): ...
def hard_sigmoid(x): ...
def hard_swish(x): ...
def preprocess_input(x, data_format: Incomplete | None = None):
    '''A placeholder method for backward compatibility.

    The preprocessing logic has been included in the mobilenet_v3 model
    implementation. Users are no longer required to call this method to
    normalize the input data. This method does nothing and only kept as a
    placeholder to align the API surface between old and new version of model.

    Args:
      x: A floating point `numpy.array` or a `tf.Tensor`.
      data_format: Optional data format of the image tensor/array. Defaults to
        None, in which case the global setting
        `tf.keras.backend.image_data_format()` is used (unless you changed it,
        it defaults to "channels_last").{mode}

    Returns:
      Unchanged `numpy.array` or `tf.Tensor`.
    '''
def decode_predictions(preds, top: int = 5): ...
