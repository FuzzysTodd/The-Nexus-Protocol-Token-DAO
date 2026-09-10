from _typeshed import Incomplete
from keras import backend as backend, layers as layers
from keras.applications import imagenet_utils as imagenet_utils
from keras.engine import training as training
from keras.utils import data_utils as data_utils, layer_utils as layer_utils
from typing import Callable, Dict, List

BASE_WEIGHTS_URL: str
WEIGHT_HASHES: Incomplete
DEPTH_TO_WEIGHT_VARIANTS: Incomplete
BLOCK_ARGS: Incomplete
CONV_KERNEL_INITIALIZER: Incomplete
BASE_DOCSTRING: str

def Conv2DFixedPadding(filters, kernel_size, strides, name: Incomplete | None = None):
    """Conv2D block with fixed padding."""
def STEM(bn_momentum: float = 0.0, bn_epsilon: float = 1e-05, activation: str = 'relu', name: Incomplete | None = None):
    """ResNet-D type STEM block."""
def SE(in_filters: int, se_ratio: float = 0.25, expand_ratio: int = 1, name: Incomplete | None = None):
    """Squeeze and Excitation block."""
def BottleneckBlock(filters: int, strides: int, use_projection: bool, bn_momentum: float = 0.0, bn_epsilon: float = 1e-05, activation: str = 'relu', se_ratio: float = 0.25, survival_probability: float = 0.8, name: Incomplete | None = None):
    """Bottleneck block variant for residual networks with BN."""
def BlockGroup(filters, strides, num_repeats, se_ratio: float = 0.25, bn_epsilon: float = 1e-05, bn_momentum: float = 0.0, activation: str = 'relu', survival_probability: float = 0.8, name: Incomplete | None = None):
    """Create one group of blocks for the ResNet model."""
def get_survival_probability(init_rate, block_num, total_blocks):
    """Get survival probability based on block number and initial rate."""
def allow_bigger_recursion(target_limit: int):
    """Increase default recursion limit to create larger models."""
def fixed_padding(inputs, kernel_size):
    """Pad the input along the spatial dimensions independently of input
    size."""
def ResNetRS(depth: int, input_shape: Incomplete | None = None, bn_momentum: float = 0.0, bn_epsilon: float = 1e-05, activation: str = 'relu', se_ratio: float = 0.25, dropout_rate: float = 0.25, drop_connect_rate: float = 0.2, include_top: bool = True, block_args: List[Dict[str, int]] = None, model_name: str = 'resnet-rs', pooling: Incomplete | None = None, weights: str = 'imagenet', input_tensor: Incomplete | None = None, classes: int = 1000, classifier_activation: str | Callable = 'softmax', include_preprocessing: bool = True):
    '''Build Resnet-RS model, given provided parameters.

    Args:
        depth: Depth of ResNet network.
        input_shape: optional shape tuple. It should have exactly 3 inputs
          channels, and width and height should be no smaller than 32. E.g.
          (200, 200, 3) would be one valid value.
        bn_momentum: Momentum parameter for Batch Normalization layers.
        bn_epsilon: Epsilon parameter for Batch Normalization layers.
        activation: activation function.
        se_ratio: Squeeze and Excitation layer ratio.
        dropout_rate: dropout rate before final classifier layer.
        drop_connect_rate: dropout rate at skip connections.
        include_top: whether to include the fully-connected layer at the top of
          the network.
        block_args: list of dicts, parameters to construct block modules.
        model_name: name of the model.
        pooling: optional pooling mode for feature extraction when `include_top`
          is `False`.
          - `None` means that the output of the model will be the 4D tensor
            output of the last convolutional layer.
          - `avg` means that global average pooling will be applied to the
            output of the last convolutional layer, and thus the output of the
            model will be a 2D tensor.
          - `max` means that global max pooling will be applied.
        weights: one of `None` (random initialization), `\'imagenet\'`
          (pre-training on ImageNet), or the path to the weights file to be
          loaded. Note- one model can have multiple imagenet variants depending
          on input shape it was trained with. For input_shape 224x224 pass
          `imagenet-i224` as argument. By default, highest input shape weights
          are downloaded.
        input_tensor: optional Keras tensor (i.e. output of `layers.Input()`) to
          use as image input for the model.
        classes: optional number of classes to classify images into, only to be
          specified if `include_top` is True, and if no `weights` argument is
          specified.
        classifier_activation: A `str` or callable. The activation function to
          use on the "top" layer. Ignored unless `include_top=True`. Set
          `classifier_activation=None` to return the logits of the "top" layer.
        include_preprocessing: Boolean, whether to include the preprocessing
          layer (`Rescaling`) at the bottom of the network. Defaults to `True`.
          Note- Input image is normalized by ImageNet mean and standard
          deviation.

    Returns:
        A `tf.keras.Model` instance.

    Raises:
        ValueError: in case of invalid argument for `weights`, or invalid input
            shape.
        ValueError: if `classifier_activation` is not `softmax` or `None` when
            using a pretrained top layer.
    '''
def ResNetRS50(include_top: bool = True, weights: str = 'imagenet', classes: int = 1000, input_shape: Incomplete | None = None, input_tensor: Incomplete | None = None, pooling: Incomplete | None = None, classifier_activation: str = 'softmax', include_preprocessing: bool = True):
    """Build ResNet-RS50 model."""
def ResNetRS101(include_top: bool = True, weights: str = 'imagenet', classes: int = 1000, input_shape: Incomplete | None = None, input_tensor: Incomplete | None = None, pooling: Incomplete | None = None, classifier_activation: str = 'softmax', include_preprocessing: bool = True):
    """Build ResNet-RS101 model."""
def ResNetRS152(include_top: bool = True, weights: str = 'imagenet', classes: int = 1000, input_shape: Incomplete | None = None, input_tensor: Incomplete | None = None, pooling: Incomplete | None = None, classifier_activation: str = 'softmax', include_preprocessing: bool = True):
    """Build ResNet-RS152 model."""
def ResNetRS200(include_top: bool = True, weights: str = 'imagenet', classes: int = 1000, input_shape: Incomplete | None = None, input_tensor: Incomplete | None = None, pooling: Incomplete | None = None, classifier_activation: str = 'softmax', include_preprocessing: bool = True):
    """Build ResNet-RS200 model."""
def ResNetRS270(include_top: bool = True, weights: str = 'imagenet', classes: int = 1000, input_shape: Incomplete | None = None, input_tensor: Incomplete | None = None, pooling: Incomplete | None = None, classifier_activation: str = 'softmax', include_preprocessing: bool = True):
    """Build ResNet-RS-270 model."""
def ResNetRS350(include_top: bool = True, weights: str = 'imagenet', classes: int = 1000, input_shape: Incomplete | None = None, input_tensor: Incomplete | None = None, pooling: Incomplete | None = None, classifier_activation: str = 'softmax', include_preprocessing: bool = True):
    """Build ResNet-RS350 model."""
def ResNetRS420(include_top: bool = True, weights: str = 'imagenet', classes: int = 1000, input_shape: Incomplete | None = None, input_tensor: Incomplete | None = None, pooling: Incomplete | None = None, classifier_activation: str = 'softmax', include_preprocessing: bool = True):
    """Build ResNet-RS420 model."""
def preprocess_input(x, data_format: Incomplete | None = None):
    '''A placeholder method for backward compatibility.

    The preprocessing logic has been included in the ResnetRS model
    implementation. Users are no longer required to call this method to
    normalize
    the input data. This method does nothing and only kept as a placeholder to
    align the API surface between old and new version of model.

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
