from _typeshed import Incomplete
from keras import backend as backend, layers as layers
from keras.applications import imagenet_utils as imagenet_utils
from keras.engine import training as training
from keras.utils import data_utils as data_utils, layer_utils as layer_utils

BASE_WEIGHTS_PATH: str
WEIGHTS_HASHES: Incomplete
DEFAULT_BLOCKS_ARGS: Incomplete
CONV_KERNEL_INITIALIZER: Incomplete
DENSE_KERNEL_INITIALIZER: Incomplete
BASE_DOCSTRING: str

def round_filters(filters, width_coefficient, min_depth, depth_divisor):
    """Round number of filters based on depth multiplier."""
def round_repeats(repeats, depth_coefficient):
    """Round number of repeats based on depth multiplier."""
def MBConvBlock(input_filters: int, output_filters: int, expand_ratio: int = 1, kernel_size: int = 3, strides: int = 1, se_ratio: float = 0.0, bn_momentum: float = 0.9, activation: str = 'swish', survival_probability: float = 0.8, name: Incomplete | None = None):
    """MBConv block: Mobile Inverted Residual Bottleneck."""
def FusedMBConvBlock(input_filters: int, output_filters: int, expand_ratio: int = 1, kernel_size: int = 3, strides: int = 1, se_ratio: float = 0.0, bn_momentum: float = 0.9, activation: str = 'swish', survival_probability: float = 0.8, name: Incomplete | None = None):
    """Fused MBConv Block: Fusing the proj conv1x1 and depthwise_conv into a
    conv2d."""
def EfficientNetV2(width_coefficient, depth_coefficient, default_size, dropout_rate: float = 0.2, drop_connect_rate: float = 0.2, depth_divisor: int = 8, min_depth: int = 8, bn_momentum: float = 0.9, activation: str = 'swish', blocks_args: str = 'default', model_name: str = 'efficientnetv2', include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', include_preprocessing: bool = True):
    '''Instantiates the EfficientNetV2 architecture using given scaling
    coefficients.

    Args:
      width_coefficient: float, scaling coefficient for network width.
      depth_coefficient: float, scaling coefficient for network depth.
      default_size: integer, default input image size.
      dropout_rate: float, dropout rate before final classifier layer.
      drop_connect_rate: float, dropout rate at skip connections.
      depth_divisor: integer, a unit of network width.
      min_depth: integer, minimum number of filters.
      bn_momentum: float. Momentum parameter for Batch Normalization layers.
      activation: activation function.
      blocks_args: list of dicts, parameters to construct block modules.
      model_name: string, model name.
      include_top: whether to include the fully-connected layer at the top of
        the network.
      weights: one of `None` (random initialization), `"imagenet"` (pre-training
        on ImageNet), or the path to the weights file to be loaded.
      input_tensor: optional Keras tensor (i.e. output of `layers.Input()`) or
        numpy array to use as image input for the model.
      input_shape: optional shape tuple, only to be specified if `include_top`
        is False. It should have exactly 3 inputs channels.
      pooling: optional pooling mode for feature extraction when `include_top`
        is `False`.
        - `None` means that the output of the model will be the 4D tensor output
          of the last convolutional layer.
        - "avg" means that global average pooling will be applied to the output
          of the last convolutional layer, and thus the output of the model will
          be a 2D tensor.
        - `"max"` means that global max pooling will be applied.
      classes: optional number of classes to classify images into, only to be
        specified if `include_top` is True, and if no `weights` argument is
        specified.
      classifier_activation: A string or callable. The activation function to
        use on the `"top"` layer. Ignored unless `include_top=True`. Set
        `classifier_activation=None` to return the logits of the `"top"` layer.
      include_preprocessing: Boolean, whether to include the preprocessing layer
        (`Rescaling`) at the bottom of the network. Defaults to `True`.

    Returns:
      A `keras.Model` instance.

    Raises:
      ValueError: in case of invalid argument for `weights`,
        or invalid input shape.
      ValueError: if `classifier_activation` is not `"softmax"` or `None` when
        using a pretrained top layer.
    '''
def EfficientNetV2B0(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', include_preprocessing: bool = True): ...
def EfficientNetV2B1(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', include_preprocessing: bool = True): ...
def EfficientNetV2B2(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', include_preprocessing: bool = True): ...
def EfficientNetV2B3(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', include_preprocessing: bool = True): ...
def EfficientNetV2S(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', include_preprocessing: bool = True): ...
def EfficientNetV2M(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', include_preprocessing: bool = True): ...
def EfficientNetV2L(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', include_preprocessing: bool = True): ...
def preprocess_input(x, data_format: Incomplete | None = None):
    '''A placeholder method for backward compatibility.

    The preprocessing logic has been included in the EfficientNetV2 model
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
