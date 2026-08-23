from _typeshed import Incomplete
from keras.integration_test.models.input_spec import InputSpec as InputSpec
from tensorflow import keras

INPUT_DIM: int
NUM_CLASSES: int

def get_data_spec(batch_size): ...
def get_input_preprocessor() -> None: ...

class LinearA(keras.layers.Layer):
    """Standard custom layer with 2 call() inputs."""
    w: Incomplete
    b: Incomplete
    def __init__(self, units: int = 32, input_dim: int = 32) -> None: ...
    def call(self, inputs_1, inputs_2): ...

class LinearB(keras.layers.Layer):
    """Layer that tracks weights in a dict attribute that gets updated later."""
    state: Incomplete
    def __init__(self, units: int = 32, input_dim: int = 32, **kwargs) -> None: ...
    def call(self, inputs): ...

class LinearC(keras.layers.Layer):
    """Layer that creates weights in call()."""
    units: Incomplete
    input_dim: Incomplete
    def __init__(self, units: int = 32, input_dim: int = 32, **kwargs) -> None: ...
    w: Incomplete
    b: Incomplete
    def call(self, inputs): ...

class BatchNorm(keras.layers.Layer):
    """Layer with different training/test behavior and non-trainable updates."""
    scale: Incomplete
    center: Incomplete
    epsilon: Incomplete
    momentum: Incomplete
    def __init__(self, scale: bool = True, center: bool = True, epsilon: float = 1e-06, momentum: float = 0.9, **kwargs) -> None: ...
    var: Incomplete
    mean: Incomplete
    gamma: Incomplete
    beta: Incomplete
    def build(self, input_shape) -> None: ...
    def call(self, inputs, training: bool = False): ...

class FunctionalSubclassModel(keras.Model):
    def __init__(self, **kwargs) -> None: ...

def get_model(build: bool = False, compile: bool = False, jit_compile: bool = False, include_preprocessing: bool = True): ...
def get_custom_objects(): ...
