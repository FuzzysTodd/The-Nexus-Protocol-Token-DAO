from _typeshed import Incomplete
from keras.utils.generic_utils import LazyLoader as LazyLoader

training: Incomplete
training_v1: Incomplete
base_layer: Incomplete
base_layer_v1: Incomplete
callbacks: Incomplete
callbacks_v1: Incomplete

class ModelVersionSelector:
    """Chooses between Keras v1 and v2 Model class."""
    def __new__(cls, *args, **kwargs): ...

class LayerVersionSelector:
    """Chooses between Keras v1 and v2 Layer class."""
    def __new__(cls, *args, **kwargs): ...

class TensorBoardVersionSelector:
    """Chooses between Keras v1 and v2 TensorBoard callback class."""
    def __new__(cls, *args, **kwargs): ...

def should_use_v2():
    """Determine if v1 or v2 version should be used."""
def swap_class(cls, v2_cls, v1_cls, use_v2):
    """Swaps in v2_cls or v1_cls depending on graph mode."""
def disallow_legacy_graph(cls_name, method_name) -> None: ...
def is_v1_layer_or_model(obj): ...
