from _typeshed import Incomplete
from keras import backend as backend
from keras.applications import imagenet_utils as imagenet_utils
from keras.engine import training as training
from keras.layers import VersionAwareLayers as VersionAwareLayers
from keras.utils import data_utils as data_utils, layer_utils as layer_utils

BASE_WEIGHTS_PATH: str
WEIGHTS_HASHES: Incomplete
DEFAULT_BLOCKS_ARGS: Incomplete
CONV_KERNEL_INITIALIZER: Incomplete
DENSE_KERNEL_INITIALIZER: Incomplete
layers: Incomplete
BASE_DOCSTRING: str
IMAGENET_STDDEV_RGB: Incomplete

def EfficientNet(width_coefficient, depth_coefficient, default_size, dropout_rate: float = 0.2, drop_connect_rate: float = 0.2, depth_divisor: int = 8, activation: str = 'swish', blocks_args: str = 'default', model_name: str = 'efficientnet', include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'):
    '''Instantiates the EfficientNet architecture.

    Args:
      width_coefficient: float, scaling coefficient for network width.
      depth_coefficient: float, scaling coefficient for network depth.
      default_size: integer, default input image size.
      dropout_rate: float, dropout rate before final classifier layer.
      drop_connect_rate: float, dropout rate at skip connections.
      depth_divisor: integer, a unit of network width.
      activation: activation function.
      blocks_args: list of dicts, parameters to construct block modules.
      model_name: string, model name.
      include_top: whether to include the fully-connected
          layer at the top of the network.
      weights: one of `None` (random initialization),
            \'imagenet\' (pre-training on ImageNet),
            or the path to the weights file to be loaded.
      input_tensor: optional Keras tensor
          (i.e. output of `layers.Input()`)
          to use as image input for the model.
      input_shape: optional shape tuple, only to be specified
          if `include_top` is False.
          It should have exactly 3 inputs channels.
      pooling: optional pooling mode for feature extraction
          when `include_top` is `False`.
          - `None` means that the output of the model will be
              the 4D tensor output of the
              last convolutional layer.
          - `avg` means that global average pooling
              will be applied to the output of the
              last convolutional layer, and thus
              the output of the model will be a 2D tensor.
          - `max` means that global max pooling will
              be applied.
      classes: optional number of classes to classify images
          into, only to be specified if `include_top` is True, and
          if no `weights` argument is specified.
      classifier_activation: A `str` or callable. The activation function to use
          on the "top" layer. Ignored unless `include_top=True`. Set
          `classifier_activation=None` to return the logits of the "top" layer.

    Returns:
      A `keras.Model` instance.

    Raises:
      ValueError: in case of invalid argument for `weights`,
        or invalid input shape.
      ValueError: if `classifier_activation` is not `softmax` or `None` when
        using a pretrained top layer.
    '''
def block(inputs, activation: str = 'swish', drop_rate: float = 0.0, name: str = '', filters_in: int = 32, filters_out: int = 16, kernel_size: int = 3, strides: int = 1, expand_ratio: int = 1, se_ratio: float = 0.0, id_skip: bool = True):
    """An inverted residual block.

    Args:
        inputs: input tensor.
        activation: activation function.
        drop_rate: float between 0 and 1, fraction of the input units to drop.
        name: string, block label.
        filters_in: integer, the number of input filters.
        filters_out: integer, the number of output filters.
        kernel_size: integer, the dimension of the convolution window.
        strides: integer, the stride of the convolution.
        expand_ratio: integer, scaling coefficient for the input filters.
        se_ratio: float between 0 and 1, fraction to squeeze the input filters.
        id_skip: boolean.

    Returns:
        output tensor for the block.
    """
def EfficientNetB0(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', **kwargs): ...
def EfficientNetB1(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', **kwargs): ...
def EfficientNetB2(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', **kwargs): ...
def EfficientNetB3(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', **kwargs): ...
def EfficientNetB4(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', **kwargs): ...
def EfficientNetB5(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', **kwargs): ...
def EfficientNetB6(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', **kwargs): ...
def EfficientNetB7(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', **kwargs): ...
def preprocess_input(x, data_format: Incomplete | None = None):
    '''A placeholder method for backward compatibility.

    The preprocessing logic has been included in the efficientnet model
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
