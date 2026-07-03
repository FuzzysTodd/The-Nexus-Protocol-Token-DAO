import enum
from _typeshed import Incomplete
from tensorflow.lite.python.metrics import converter_error_data_pb2 as converter_error_data_pb2, metrics as metrics
from typing import NamedTuple

class Component(enum.Enum):
    """Enum class defining name of the converter components."""
    PREPARE_TF_MODEL: str
    CONVERT_TF_TO_TFLITE_MODEL: str
    OPTIMIZE_TFLITE_MODEL: str

class SubComponentItem(NamedTuple):
    name: Incomplete
    component: Incomplete

class SubComponent(SubComponentItem, enum.Enum):
    """Enum class defining name of the converter subcomponents.

  This enum only defines the subcomponents in Python, there might be more
  subcomponents defined in C++.
  """
    @property
    def name(self): ...
    @property
    def component(self): ...
    UNSPECIFIED: Incomplete
    VALIDATE_INPUTS: Incomplete
    LOAD_SAVED_MODEL: Incomplete
    FREEZE_SAVED_MODEL: Incomplete
    CONVERT_KERAS_TO_SAVED_MODEL: Incomplete
    CONVERT_CONCRETE_FUNCTIONS_TO_SAVED_MODEL: Incomplete
    FREEZE_KERAS_MODEL: Incomplete
    FREEZE_CONCRETE_FUNCTION: Incomplete
    OPTIMIZE_TF_MODEL: Incomplete
    CONVERT_GRAPHDEF_USING_DEPRECATED_CONVERTER: Incomplete
    CONVERT_GRAPHDEF: Incomplete
    CONVERT_SAVED_MODEL: Incomplete
    CONVERT_JAX_HLO: Incomplete
    QUANTIZE_USING_DEPRECATED_QUANTIZER: Incomplete
    CALIBRATE: Incomplete
    QUANTIZE: Incomplete
    SPARSIFY: Incomplete

class ConverterError(Exception):
    """Raised when an error occurs during model conversion."""
    errors: Incomplete
    def __init__(self, message) -> None: ...
    def append_error(self, error_data: converter_error_data_pb2.ConverterErrorData): ...

def convert_phase(component, subcomponent=...):
    """The decorator to identify converter component and subcomponent.

  Args:
    component: Converter component name.
    subcomponent: Converter subcomponent name.

  Returns:
    Forward the result from the wrapped function.

  Raises:
    ValueError: if component and subcomponent name is not valid.
  """
