from _typeshed import Incomplete
from keras import backend as backend
from keras.applications import imagenet_utils as imagenet_utils
from keras.engine import training as training
from keras.layers import VersionAwareLayers as VersionAwareLayers
from keras.utils import data_utils as data_utils, layer_utils as layer_utils

BASE_WEIGHTS_PATH: str
DENSENET121_WEIGHT_PATH: Incomplete
DENSENET121_WEIGHT_PATH_NO_TOP: Incomplete
DENSENET169_WEIGHT_PATH: Incomplete
DENSENET169_WEIGHT_PATH_NO_TOP: Incomplete
DENSENET201_WEIGHT_PATH: Incomplete
DENSENET201_WEIGHT_PATH_NO_TOP: Incomplete
layers: Incomplete

def dense_block(x, blocks, name):
    """A dense block.

    Args:
      x: input tensor.
      blocks: integer, the number of building blocks.
      name: string, block label.

    Returns:
      Output tensor for the block.
    """
def transition_block(x, reduction, name):
    """A transition block.

    Args:
      x: input tensor.
      reduction: float, compression rate at transition layers.
      name: string, block label.

    Returns:
      output tensor for the block.
    """
def conv_block(x, growth_rate, name):
    """A building block for a dense block.

    Args:
      x: input tensor.
      growth_rate: float, growth rate at dense layers.
      name: string, block label.

    Returns:
      Output tensor for the block.
    """
def DenseNet(blocks, include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'):
    '''Instantiates the DenseNet architecture.

    Reference:
    - [Densely Connected Convolutional Networks](
        https://arxiv.org/abs/1608.06993) (CVPR 2017)

    This function returns a Keras image classification model,
    optionally loaded with weights pre-trained on ImageNet.

    For image classification use cases, see
    [this page for detailed examples](
      https://keras.io/api/applications/#usage-examples-for-image-classification-models).

    For transfer learning use cases, make sure to read the
    [guide to transfer learning & fine-tuning](
      https://keras.io/guides/transfer_learning/).

    Note: each Keras Application expects a specific kind of input preprocessing.
    For DenseNet, call `tf.keras.applications.densenet.preprocess_input` on your
    inputs before passing them to the model.
    `densenet.preprocess_input` will scale pixels between 0 and 1 and then
    will normalize each channel with respect to the ImageNet dataset statistics.

    Args:
      blocks: numbers of building blocks for the four dense layers.
      include_top: whether to include the fully-connected
        layer at the top of the network.
      weights: one of `None` (random initialization),
        \'imagenet\' (pre-training on ImageNet),
        or the path to the weights file to be loaded.
      input_tensor: optional Keras tensor
        (i.e. output of `layers.Input()`)
        to use as image input for the model.
      input_shape: optional shape tuple, only to be specified
        if `include_top` is False (otherwise the input shape
        has to be `(224, 224, 3)` (with `\'channels_last\'` data format)
        or `(3, 224, 224)` (with `\'channels_first\'` data format).
        It should have exactly 3 inputs channels,
        and width and height should be no smaller than 32.
        E.g. `(200, 200, 3)` would be one valid value.
      pooling: optional pooling mode for feature extraction
        when `include_top` is `False`.
        - `None` means that the output of the model will be
            the 4D tensor output of the
            last convolutional block.
        - `avg` means that global average pooling
            will be applied to the output of the
            last convolutional block, and thus
            the output of the model will be a 2D tensor.
        - `max` means that global max pooling will
            be applied.
      classes: optional number of classes to classify images
        into, only to be specified if `include_top` is True, and
        if no `weights` argument is specified.
      classifier_activation: A `str` or callable. The activation function to use
        on the "top" layer. Ignored unless `include_top=True`. Set
        `classifier_activation=None` to return the logits of the "top" layer.
        When loading pretrained weights, `classifier_activation` can only
        be `None` or `"softmax"`.

    Returns:
      A `keras.Model` instance.
    '''
def DenseNet121(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'):
    """Instantiates the Densenet121 architecture."""
def DenseNet169(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'):
    """Instantiates the Densenet169 architecture."""
def DenseNet201(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'):
    """Instantiates the Densenet201 architecture."""
def preprocess_input(x, data_format: Incomplete | None = None): ...
def decode_predictions(preds, top: int = 5): ...

DOC: str
