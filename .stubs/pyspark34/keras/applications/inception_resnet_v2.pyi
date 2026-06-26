from _typeshed import Incomplete
from keras import backend as backend, layers as keras_layers
from keras.applications import imagenet_utils as imagenet_utils
from keras.engine import training as training
from keras.layers import VersionAwareLayers as VersionAwareLayers
from keras.utils import data_utils as data_utils, layer_utils as layer_utils

BASE_WEIGHT_URL: str
layers: Incomplete

def InceptionResNetV2(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax', **kwargs):
    '''Instantiates the Inception-ResNet v2 architecture.

    Reference:
    - [Inception-v4, Inception-ResNet and the Impact of
       Residual Connections on Learning](https://arxiv.org/abs/1602.07261)
      (AAAI 2017)

    This function returns a Keras image classification model,
    optionally loaded with weights pre-trained on ImageNet.

    For image classification use cases, see
    [this page for detailed examples](
      https://keras.io/api/applications/#usage-examples-for-image-classification-models).

    For transfer learning use cases, make sure to read the
    [guide to transfer learning & fine-tuning](
      https://keras.io/guides/transfer_learning/).

    Note: each Keras Application expects a specific kind of input preprocessing.
    For InceptionResNetV2, call
    `tf.keras.applications.inception_resnet_v2.preprocess_input`
    on your inputs before passing them to the model.
    `inception_resnet_v2.preprocess_input`
    will scale input pixels between -1 and 1.

    Args:
      include_top: whether to include the fully-connected
        layer at the top of the network.
      weights: one of `None` (random initialization),
        \'imagenet\' (pre-training on ImageNet),
        or the path to the weights file to be loaded.
      input_tensor: optional Keras tensor (i.e. output of `layers.Input()`)
        to use as image input for the model.
      input_shape: optional shape tuple, only to be specified
        if `include_top` is `False` (otherwise the input shape
        has to be `(299, 299, 3)` (with `\'channels_last\'` data format)
        or `(3, 299, 299)` (with `\'channels_first\'` data format).
        It should have exactly 3 inputs channels,
        and width and height should be no smaller than 75.
        E.g. `(150, 150, 3)` would be one valid value.
      pooling: Optional pooling mode for feature extraction
        when `include_top` is `False`.
        - `None` means that the output of the model will be
            the 4D tensor output of the last convolutional block.
        - `\'avg\'` means that global average pooling
            will be applied to the output of the
            last convolutional block, and thus
            the output of the model will be a 2D tensor.
        - `\'max\'` means that global max pooling will be applied.
      classes: optional number of classes to classify images
        into, only to be specified if `include_top` is `True`, and
        if no `weights` argument is specified.
      classifier_activation: A `str` or callable. The activation function to use
        on the "top" layer. Ignored unless `include_top=True`. Set
        `classifier_activation=None` to return the logits of the "top" layer.
        When loading pretrained weights, `classifier_activation` can only
        be `None` or `"softmax"`.
      **kwargs: For backwards compatibility only.

    Returns:
      A `keras.Model` instance.
    '''
def conv2d_bn(x, filters, kernel_size, strides: int = 1, padding: str = 'same', activation: str = 'relu', use_bias: bool = False, name: Incomplete | None = None):
    """Utility function to apply conv + BN.

    Args:
      x: input tensor.
      filters: filters in `Conv2D`.
      kernel_size: kernel size as in `Conv2D`.
      strides: strides in `Conv2D`.
      padding: padding mode in `Conv2D`.
      activation: activation in `Conv2D`.
      use_bias: whether to use a bias in `Conv2D`.
      name: name of the ops; will become `name + '_ac'` for the activation
          and `name + '_bn'` for the batch norm layer.

    Returns:
      Output tensor after applying `Conv2D` and `BatchNormalization`.
    """

class CustomScaleLayer(keras_layers.Layer):
    scale: Incomplete
    def __init__(self, scale, **kwargs) -> None: ...
    def get_config(self): ...
    def call(self, inputs): ...

def inception_resnet_block(x, scale, block_type, block_idx, activation: str = 'relu'):
    '''Adds an Inception-ResNet block.

    This function builds 3 types of Inception-ResNet blocks mentioned
    in the paper, controlled by the `block_type` argument (which is the
    block name used in the official TF-slim implementation):
    - Inception-ResNet-A: `block_type=\'block35\'`
    - Inception-ResNet-B: `block_type=\'block17\'`
    - Inception-ResNet-C: `block_type=\'block8\'`

    Args:
      x: input tensor.
      scale: scaling factor to scale the residuals (i.e., the output of passing
        `x` through an inception module) before adding them to the shortcut
        branch. Let `r` be the output from the residual branch, the output of
        this block will be `x + scale * r`.
      block_type: `\'block35\'`, `\'block17\'` or `\'block8\'`, determines the network
        structure in the residual branch.
      block_idx: an `int` used for generating layer names. The Inception-ResNet
        blocks are repeated many times in this network. We use `block_idx` to
        identify each of the repetitions. For example, the first
        Inception-ResNet-A block will have `block_type=\'block35\', block_idx=0`,
        and the layer names will have a common prefix `\'block35_0\'`.
      activation: activation function to use at the end of the block (see
        [activations](../activations.md)). When `activation=None`, no activation
        is applied
        (i.e., "linear" activation: `a(x) = x`).

    Returns:
        Output tensor for the block.

    Raises:
      ValueError: if `block_type` is not one of `\'block35\'`,
        `\'block17\'` or `\'block8\'`.
    '''
def preprocess_input(x, data_format: Incomplete | None = None): ...
def decode_predictions(preds, top: int = 5): ...
