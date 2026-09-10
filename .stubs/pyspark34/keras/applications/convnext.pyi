from _typeshed import Incomplete
from keras import backend as backend, layers as layers, utils as utils
from keras.applications import imagenet_utils as imagenet_utils
from keras.engine import sequential as sequential

BASE_WEIGHTS_PATH: str
WEIGHTS_HASHES: Incomplete
MODEL_CONFIGS: Incomplete
BASE_DOCSTRING: str

class StochasticDepth(layers.Layer):
    """Stochastic Depth module.

    It performs batch-wise dropping rather than sample-wise. In libraries like
    `timm`, it's similar to `DropPath` layers that drops residual paths
    sample-wise.

    References:
      - https://github.com/rwightman/pytorch-image-models

    Args:
      drop_path_rate (float): Probability of dropping paths. Should be within
        [0, 1].

    Returns:
      Tensor either with the residual path dropped or kept.
    """
    drop_path_rate: Incomplete
    def __init__(self, drop_path_rate, **kwargs) -> None: ...
    def call(self, x, training: Incomplete | None = None): ...
    def get_config(self): ...

class LayerScale(layers.Layer):
    """Layer scale module.

    References:
      - https://arxiv.org/abs/2103.17239

    Args:
      init_values (float): Initial value for layer scale. Should be within
        [0, 1].
      projection_dim (int): Projection dimensionality.

    Returns:
      Tensor multiplied to the scale.
    """
    init_values: Incomplete
    projection_dim: Incomplete
    def __init__(self, init_values, projection_dim, **kwargs) -> None: ...
    gamma: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, x): ...
    def get_config(self): ...

def ConvNeXtBlock(projection_dim, drop_path_rate: float = 0.0, layer_scale_init_value: float = 1e-06, name: Incomplete | None = None):
    """ConvNeXt block.

    References:
    - https://arxiv.org/abs/2201.03545
    - https://github.com/facebookresearch/ConvNeXt/blob/main/models/convnext.py

    Notes:
      In the original ConvNeXt implementation (linked above), the authors use
      `Dense` layers for pointwise convolutions for increased efficiency.
      Following that, this implementation also uses the same.

    Args:
      projection_dim (int): Number of filters for convolution layers. In the
        ConvNeXt paper, this is referred to as projection dimension.
      drop_path_rate (float): Probability of dropping paths. Should be within
        [0, 1].
      layer_scale_init_value (float): Layer scale value. Should be a small float
        number.
      name: name to path to the keras layer.

    Returns:
      A function representing a ConvNeXtBlock block.
    """
def PreStem(name: Incomplete | None = None):
    """Normalizes inputs with ImageNet-1k mean and std.

    Args:
      name (str): Name prefix.

    Returns:
      A presemt function.
    """
def Head(num_classes: int = 1000, name: Incomplete | None = None):
    """Implementation of classification head of RegNet.

    Args:
      num_classes: number of classes for Dense layer
      name: name prefix

    Returns:
      Classification head function.
    """
def ConvNeXt(depths, projection_dims, drop_path_rate: float = 0.0, layer_scale_init_value: float = 1e-06, default_size: int = 224, model_name: str = 'convnext', include_preprocessing: bool = True, include_top: bool = True, weights: Incomplete | None = None, input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'):
    '''Instantiates ConvNeXt architecture given specific configuration.

    Args:
      depths: An iterable containing depths for each individual stages.
      projection_dims: An iterable containing output number of channels of
      each individual stages.
      drop_path_rate: Stochastic depth probability. If 0.0, then stochastic
        depth won\'t be used.
      layer_scale_init_value: Layer scale coefficient. If 0.0, layer scaling
        won\'t be used.
      default_size: Default input image size.
      model_name: An optional name for the model.
      include_preprocessing: boolean denoting whther to include preprocessing in
        the model. When `weights="imagenet"` this should be always set to True.
        But for other models (e.g., randomly initialized) users should set it
        to False and apply preprocessing to data accordingly.
      include_top: Boolean denoting whether to include classification head to
        the model.
      weights: one of `None` (random initialization), `"imagenet"` (pre-training
        on ImageNet-1k), or the path to the weights file to be loaded.
      input_tensor: optional Keras tensor (i.e. output of `layers.Input()`) to
        use as image input for the model.
      input_shape: optional shape tuple, only to be specified if `include_top`
        is False. It should have exactly 3 inputs channels.
      pooling: optional pooling mode for feature extraction when `include_top`
        is `False`.
        - `None` means that the output of the model will be the 4D tensor output
          of the last convolutional layer.
        - `avg` means that global average pooling will be applied to the output
          of the last convolutional layer, and thus the output of the model will
          be a 2D tensor.
        - `max` means that global max pooling will be applied.
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
        ValueError: if `classifier_activation` is not `softmax`, or `None`
          when using a pretrained top layer.
        ValueError: if `include_top` is True but `num_classes` is not 1000
          when using ImageNet.
    '''
def ConvNeXtTiny(model_name: str = 'convnext_tiny', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def ConvNeXtSmall(model_name: str = 'convnext_small', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def ConvNeXtBase(model_name: str = 'convnext_base', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def ConvNeXtLarge(model_name: str = 'convnext_large', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def ConvNeXtXLarge(model_name: str = 'convnext_xlarge', include_top: bool = True, include_preprocessing: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'): ...
def preprocess_input(x, data_format: Incomplete | None = None):
    '''A placeholder method for backward compatibility.

    The preprocessing logic has been included in the convnext model
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
