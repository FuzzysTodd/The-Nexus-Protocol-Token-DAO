from _typeshed import Incomplete
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec
from keras.utils import conv_utils as conv_utils

class GlobalPooling3D(Layer):
    """Abstract class for different global pooling 3D layers."""
    data_format: Incomplete
    input_spec: Incomplete
    keepdims: Incomplete
    def __init__(self, data_format: Incomplete | None = None, keepdims: bool = False, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs) -> None: ...
    def get_config(self): ...
