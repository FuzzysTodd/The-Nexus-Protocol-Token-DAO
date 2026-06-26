from _typeshed import Incomplete
from keras.engine.base_layer import Layer as Layer
from keras.saving.legacy import serialization as serialization

class Wrapper(Layer):
    """Abstract wrapper base class.

    Wrappers take another layer and augment it in various ways.
    Do not use this class as a layer, it is only an abstract base class.
    Two usable wrappers are the `TimeDistributed` and `Bidirectional` wrappers.

    Args:
      layer: The layer to be wrapped.
    """
    layer: Incomplete
    def __init__(self, layer, **kwargs) -> None: ...
    built: bool
    def build(self, input_shape: Incomplete | None = None) -> None: ...
    @property
    def activity_regularizer(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...
