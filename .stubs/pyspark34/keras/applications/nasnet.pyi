from _typeshed import Incomplete
from keras import backend as backend
from keras.applications import imagenet_utils as imagenet_utils
from keras.engine import training as training
from keras.layers import VersionAwareLayers as VersionAwareLayers
from keras.utils import data_utils as data_utils, layer_utils as layer_utils

BASE_WEIGHTS_PATH: str
NASNET_MOBILE_WEIGHT_PATH: Incomplete
NASNET_MOBILE_WEIGHT_PATH_NO_TOP: Incomplete
NASNET_LARGE_WEIGHT_PATH: Incomplete
NASNET_LARGE_WEIGHT_PATH_NO_TOP: Incomplete
layers: Incomplete

def NASNet(input_shape: Incomplete | None = None, penultimate_filters: int = 4032, num_blocks: int = 6, stem_block_filters: int = 96, skip_reduction: bool = True, filter_multiplier: int = 2, include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, default_size: Incomplete | None = None, classifier_activation: str = 'softmax'):
    '''Instantiates a NASNet model.

    Reference:
    - [Learning Transferable Architectures for Scalable Image Recognition](
        https://arxiv.org/abs/1707.07012) (CVPR 2018)

    For image classification use cases, see
    [this page for detailed examples](
      https://keras.io/api/applications/#usage-examples-for-image-classification-models).

    For transfer learning use cases, make sure to read the
    [guide to transfer learning & fine-tuning](
      https://keras.io/guides/transfer_learning/).

    Note: each Keras Application expects a specific kind of input preprocessing.
    For NasNet, call `tf.keras.applications.nasnet.preprocess_input`
    on your inputs before passing them to the model.
    `nasnet.preprocess_input` will scale input pixels between -1 and 1.

    Args:
      input_shape: Optional shape tuple, the input shape
        is by default `(331, 331, 3)` for NASNetLarge and
        `(224, 224, 3)` for NASNetMobile.
        It should have exactly 3 input channels,
        and width and height should be no smaller than 32.
        E.g. `(224, 224, 3)` would be one valid value.
      penultimate_filters: Number of filters in the penultimate layer.
        NASNet models use the notation `NASNet (N @ P)`, where:
            -   N is the number of blocks
            -   P is the number of penultimate filters
      num_blocks: Number of repeated blocks of the NASNet model.
        NASNet models use the notation `NASNet (N @ P)`, where:
            -   N is the number of blocks
            -   P is the number of penultimate filters
      stem_block_filters: Number of filters in the initial stem block
      skip_reduction: Whether to skip the reduction step at the tail
        end of the network.
      filter_multiplier: Controls the width of the network.
        - If `filter_multiplier` < 1.0, proportionally decreases the number
            of filters in each layer.
        - If `filter_multiplier` > 1.0, proportionally increases the number
            of filters in each layer.
        - If `filter_multiplier` = 1, default number of filters from the
             paper are used at each layer.
      include_top: Whether to include the fully-connected
        layer at the top of the network.
      weights: `None` (random initialization) or
          `imagenet` (ImageNet weights)
      input_tensor: Optional Keras tensor (i.e. output of
        `layers.Input()`)
        to use as image input for the model.
      pooling: Optional pooling mode for feature extraction
        when `include_top` is `False`.
        - `None` means that the output of the model
            will be the 4D tensor output of the
            last convolutional block.
        - `avg` means that global average pooling
            will be applied to the output of the
            last convolutional block, and thus
            the output of the model will be a
            2D tensor.
        - `max` means that global max pooling will
            be applied.
      classes: Optional number of classes to classify images
        into, only to be specified if `include_top` is True, and
        if no `weights` argument is specified.
      default_size: Specifies the default image size of the model
      classifier_activation: A `str` or callable. The activation function to use
        on the "top" layer. Ignored unless `include_top=True`. Set
        `classifier_activation=None` to return the logits of the "top" layer.
        When loading pretrained weights, `classifier_activation` can only
        be `None` or `"softmax"`.

    Returns:
      A `keras.Model` instance.
    '''
def NASNetMobile(input_shape: Incomplete | None = None, include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'):
    '''Instantiates a Mobile NASNet model in ImageNet mode.

    Reference:
    - [Learning Transferable Architectures for Scalable Image Recognition](
        https://arxiv.org/abs/1707.07012) (CVPR 2018)

    Optionally loads weights pre-trained on ImageNet.
    Note that the data format convention used by the model is
    the one specified in your Keras config at `~/.keras/keras.json`.

    Note: each Keras Application expects a specific kind of input preprocessing.
    For NASNet, call `tf.keras.applications.nasnet.preprocess_input` on your
    inputs before passing them to the model.

    Args:
        input_shape: Optional shape tuple, only to be specified
            if `include_top` is False (otherwise the input shape
            has to be `(224, 224, 3)` for NASNetMobile
            It should have exactly 3 inputs channels,
            and width and height should be no smaller than 32.
            E.g. `(224, 224, 3)` would be one valid value.
        include_top: Whether to include the fully-connected
            layer at the top of the network.
        weights: `None` (random initialization) or
            `imagenet` (ImageNet weights). For loading `imagenet` weights,
            `input_shape` should be (224, 224, 3)
        input_tensor: Optional Keras tensor (i.e. output of
            `layers.Input()`)
            to use as image input for the model.
        pooling: Optional pooling mode for feature extraction
            when `include_top` is `False`.
            - `None` means that the output of the model
                will be the 4D tensor output of the
                last convolutional layer.
            - `avg` means that global average pooling
                will be applied to the output of the
                last convolutional layer, and thus
                the output of the model will be a
                2D tensor.
            - `max` means that global max pooling will
                be applied.
        classes: Optional number of classes to classify images
            into, only to be specified if `include_top` is True, and
            if no `weights` argument is specified.
        classifier_activation: A `str` or callable. The activation function to
            use on the "top" layer. Ignored unless `include_top=True`. Set
            `classifier_activation=None` to return the logits of the "top"
            layer.  When loading pretrained weights, `classifier_activation` can
            only be `None` or `"softmax"`.

    Returns:
        A Keras model instance.

    Raises:
        ValueError: In case of invalid argument for `weights`,
            or invalid input shape.
        RuntimeError: If attempting to run this model with a
            backend that does not support separable convolutions.
    '''
def NASNetLarge(input_shape: Incomplete | None = None, include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'):
    '''Instantiates a NASNet model in ImageNet mode.

    Reference:
    - [Learning Transferable Architectures for Scalable Image Recognition](
        https://arxiv.org/abs/1707.07012) (CVPR 2018)

    Optionally loads weights pre-trained on ImageNet.
    Note that the data format convention used by the model is
    the one specified in your Keras config at `~/.keras/keras.json`.

    Note: each Keras Application expects a specific kind of input preprocessing.
    For NASNet, call `tf.keras.applications.nasnet.preprocess_input` on your
    inputs before passing them to the model.

    Args:
        input_shape: Optional shape tuple, only to be specified
            if `include_top` is False (otherwise the input shape
            has to be `(331, 331, 3)` for NASNetLarge.
            It should have exactly 3 inputs channels,
            and width and height should be no smaller than 32.
            E.g. `(224, 224, 3)` would be one valid value.
        include_top: Whether to include the fully-connected
            layer at the top of the network.
        weights: `None` (random initialization) or
            `imagenet` (ImageNet weights).  For loading `imagenet` weights,
            `input_shape` should be (331, 331, 3)
        input_tensor: Optional Keras tensor (i.e. output of
            `layers.Input()`)
            to use as image input for the model.
        pooling: Optional pooling mode for feature extraction
            when `include_top` is `False`.
            - `None` means that the output of the model
                will be the 4D tensor output of the
                last convolutional layer.
            - `avg` means that global average pooling
                will be applied to the output of the
                last convolutional layer, and thus
                the output of the model will be a
                2D tensor.
            - `max` means that global max pooling will
                be applied.
        classes: Optional number of classes to classify images
            into, only to be specified if `include_top` is True, and
            if no `weights` argument is specified.
        classifier_activation: A `str` or callable. The activation function to
            use on the "top" layer. Ignored unless `include_top=True`. Set
            `classifier_activation=None` to return the logits of the "top"
            layer.  When loading pretrained weights, `classifier_activation` can
            only be `None` or `"softmax"`.

    Returns:
        A Keras model instance.

    Raises:
        ValueError: in case of invalid argument for `weights`,
            or invalid input shape.
        RuntimeError: If attempting to run this model with a
            backend that does not support separable convolutions.
    '''
def preprocess_input(x, data_format: Incomplete | None = None): ...
def decode_predictions(preds, top: int = 5): ...
