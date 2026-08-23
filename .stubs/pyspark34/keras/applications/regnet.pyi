from _typeshed import Incomplete
from keras import backend as backend, layers as layers
from keras.applications import imagenet_utils as imagenet_utils
from keras.engine import training as training
from keras.utils import data_utils as data_utils, layer_utils as layer_utils

BASE_WEIGHTS_PATH: str
WEIGHTS_HASHES: Incomplete
MODEL_CONFIGS: Incomplete
BASE_DOCSTRING: str

def PreStem(name: Incomplete | None = None):
    """Rescales and normalizes inputs to [0,1] and ImageNet mean and std.

    Args:
      name: name prefix

    Returns:
      Rescaled and normalized tensor
    """
def Stem(name: Incomplete | None = None):
    """Implementation of RegNet stem.

    (Common to all model variants)
    Args:
      name: name prefix

    Returns:
      Output tensor of the Stem
    """
def SqueezeAndExciteBlock(filters_in, se_filters, name: Incomplete | None = None):
    """Implements the Squeeze & Excite block (https://arxiv.org/abs/1709.01507).

    Args:
      filters_in: input filters to the block
      se_filters: filters to squeeze to
      name: name prefix

    Returns:
      A function object
    """
def XBlock(filters_in, filters_out, group_width, stride: int = 1, name: Incomplete | None = None):
    """Implementation of X Block.

    Reference: [Designing Network Design
    Spaces](https://arxiv.org/abs/2003.13678)
    Args:
      filters_in: filters in the input tensor
      filters_out: filters in the output tensor
      group_width: group width
      stride: stride
      name: name prefix
    Returns:
      Output tensor of the block
    """
def YBlock(filters_in, filters_out, group_width, stride: int = 1, squeeze_excite_ratio: float = 0.25, name: Incomplete | None = None):
    """Implementation of Y Block.

    Reference: [Designing Network Design
    Spaces](https://arxiv.org/abs/2003.13678)
    Args:
      filters_in: filters in the input tensor
      filters_out: filters in the output tensor
      group_width: group width
      stride: stride
      squeeze_excite_ratio: expansion ration for Squeeze and Excite block
      name: name prefix
    Returns:
      Output tensor of the block
    """
def ZBlock(filters_in, filters_out, group_width, stride: int = 1, squeeze_excite_ratio: float = 0.25, bottleneck_ratio: float = 0.25, name: Incomplete | None = None):
    """Implementation of Z block Reference: [Fast and Accurate Model
    Scaling](https://arxiv.org/abs/2103.06877).

    Args:
      filters_in: filters in the input tensor
      filters_out: filters in the output tensor
      group_width: group width
      stride: stride
      squeeze_excite_ratio: expansion ration for Squeeze and Excite block
      bottleneck_ratio: inverted bottleneck ratio
      name: name prefix
    Returns:
      Output tensor of the block
    """
def Stage(block_type, depth, group_width, filters_in, filters_out, name: Incomplete | None = None):
    '''Implementation of Stage in RegNet.

    Args:
      block_type: must be one of "X", "Y", "Z"
      depth: depth of stage, number of blocks to use
      group_width: group width of all blocks in  this stage
      filters_in: input filters to this stage
      filters_out: output filters from this stage
      name: name prefix

    Returns:
      Output tensor of Stage
    '''
def Head(num_classes: int = 1000, name: Incomplete | None = None):
    """Implementation of classification head of RegNet.

    Args:
      num_classes: number of classes for Dense layer
      name: name prefix

    Returns:
      Output logits tensor.
    """
def RegNet(depths, widths, group_width, block_type, default_size, model_name: str = 'regnet', include_preprocessing: bool = True, include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'):
    '''Instantiates RegNet architecture given specific configuration.

    Args:
      depths: An iterable containing depths for each individual stages.
      widths: An iterable containing output channel width of each individual
        stages
      group_width: Number of channels to be used in each group. See grouped
        convolutions for more information.
      block_type: Must be one of `{"X", "Y", "Z"}`. For more details see the
        papers "Designing network design spaces" and "Fast and Accurate Model
        Scaling"
      default_size: Default input image size.
      model_name: An optional name for the model.
      include_preprocessing: boolean denoting whther to include preprocessing in
        the model
      include_top: Boolean denoting whether to include classification head to
        the model.
      weights: one of `None` (random initialization), "imagenet" (pre-training
        on ImageNet), or the path to the weights file to be loaded.
      input_tensor: optional Keras tensor (i.e. output of `layers.Input()`) to
        use as image input for the model.
      input_shape: optional shape tuple, only to be specified if `include_top`
        is False. It should have exactly 3 inputs channels.
      pooling: optional pooling mode for feature extraction when `include_top`
        is `False`. - `None` means that the output of the model will be the 4D
        tensor output of the last convolutional layer. - `avg` means that global
        average pooling will be applied to the output of the last convolutional
        layer, and thus the output of the model will be a 2D tensor. - `max`
        means that global max pooling will be applied.
      classes: optional number of classes to classify images into, only to be
        specified if `include_top` is True, and if no `weights` argument is
        specified.
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
        ValueError: if `include_top` is True but `num_classes` is not 1000.
        ValueError: if `block_type` is not one of `{"X", "Y", "Z"}`

    '''
def RegNetX002(model_name: str = 'regnetx002', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetX004(model_name: str = 'regnetx004', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetX006(model_name: str = 'regnetx006', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetX008(model_name: str = 'regnetx008', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetX016(model_name: str = 'regnetx016', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetX032(model_name: str = 'regnetx032', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetX040(model_name: str = 'regnetx040', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetX064(model_name: str = 'regnetx064', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetX080(model_name: str = 'regnetx080', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetX120(model_name: str = 'regnetx120', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetX160(model_name: str = 'regnetx160', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetX320(model_name: str = 'regnetx320', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetY002(model_name: str = 'regnety002', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetY004(model_name: str = 'regnety004', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetY006(model_name: str = 'regnety006', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetY008(model_name: str = 'regnety008', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetY016(model_name: str = 'regnety016', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetY032(model_name: str = 'regnety032', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetY040(model_name: str = 'regnety040', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetY064(model_name: str = 'regnety064', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetY080(model_name: str = 'regnety080', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetY120(model_name: str = 'regnety120', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetY160(model_name: str = 'regnety160', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def RegNetY320(model_name: str = 'regnety320', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def preprocess_input(x, data_format: Incomplete | None = None):
    '''A placeholder method for backward compatibility.

    The preprocessing logic has been included in the regnet model
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
