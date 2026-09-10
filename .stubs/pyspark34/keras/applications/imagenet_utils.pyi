from _typeshed import Incomplete
from keras import activations as activations, backend as backend
from keras.utils import data_utils as data_utils

CLASS_INDEX: Incomplete
CLASS_INDEX_PATH: str
PREPROCESS_INPUT_DOC: str
PREPROCESS_INPUT_MODE_DOC: str
PREPROCESS_INPUT_DEFAULT_ERROR_DOC: str
PREPROCESS_INPUT_ERROR_DOC: str
PREPROCESS_INPUT_RET_DOC_TF: str
PREPROCESS_INPUT_RET_DOC_TORCH: str
PREPROCESS_INPUT_RET_DOC_CAFFE: str

def preprocess_input(x, data_format: Incomplete | None = None, mode: str = 'caffe'):
    """Preprocesses a tensor or Numpy array encoding a batch of images."""
def decode_predictions(preds, top: int = 5):
    """Decodes the prediction of an ImageNet model.

    Args:
      preds: Numpy array encoding a batch of predictions.
      top: Integer, how many top-guesses to return. Defaults to 5.

    Returns:
      A list of lists of top class prediction tuples
      `(class_name, class_description, score)`.
      One list of tuples per sample in batch input.

    Raises:
      ValueError: In case of invalid shape of the `pred` array
        (must be 2D).
    """
def obtain_input_shape(input_shape, default_size, min_size, data_format, require_flatten, weights: Incomplete | None = None):
    """Internal utility to compute/validate a model's input shape.

    Args:
      input_shape: Either None (will return the default network input shape),
        or a user-provided shape to be validated.
      default_size: Default input width/height for the model.
      min_size: Minimum input width/height accepted by the model.
      data_format: Image data format to use.
      require_flatten: Whether the model is expected to
        be linked to a classifier via a Flatten layer.
      weights: One of `None` (random initialization)
        or 'imagenet' (pre-training on ImageNet).
        If weights='imagenet' input channels must be equal to 3.

    Returns:
      An integer shape tuple (may include None entries).

    Raises:
      ValueError: In case of invalid argument values.
    """
def correct_pad(inputs, kernel_size):
    """Returns a tuple for zero-padding for 2D convolution with downsampling.

    Args:
      inputs: Input tensor.
      kernel_size: An integer or tuple/list of 2 integers.

    Returns:
      A tuple.
    """
def validate_activation(classifier_activation, weights) -> None:
    """validates that the classifer_activation is compatible with the weights.

    Args:
      classifier_activation: str or callable activation function
      weights: The pretrained weights to load.

    Raises:
      ValueError: if an activation other than `None` or `softmax` are used with
        pretrained weights.
    """
