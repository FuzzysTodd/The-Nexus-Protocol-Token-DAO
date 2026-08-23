from _typeshed import Incomplete
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec
from keras.utils import conv_utils as conv_utils

class GlobalPooling1D(Layer):
    """Abstract class for different global pooling 1D layers."""
    input_spec: Incomplete
    data_format: Incomplete
    keepdims: Incomplete
    def __init__(self, data_format: str = 'channels_last', keepdims: bool = False, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def call(self, inputs) -> None: ...
    def get_config(self): ...
