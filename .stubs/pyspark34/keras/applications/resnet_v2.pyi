from _typeshed import Incomplete
from keras.applications import imagenet_utils as imagenet_utils, resnet as resnet

def ResNet50V2(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'):
    """Instantiates the ResNet50V2 architecture."""
def ResNet101V2(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'):
    """Instantiates the ResNet101V2 architecture."""
def ResNet152V2(include_top: bool = True, weights: str = 'imagenet', input_tensor: Incomplete | None = None, input_shape: Incomplete | None = None, pooling: Incomplete | None = None, classes: int = 1000, classifier_activation: str = 'softmax'):
    """Instantiates the ResNet152V2 architecture."""
def preprocess_input(x, data_format: Incomplete | None = None): ...
def decode_predictions(preds, top: int = 5): ...

DOC: str
