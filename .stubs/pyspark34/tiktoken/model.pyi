from .core import Encoding as Encoding
from .registry import get_encoding as get_encoding

MODEL_PREFIX_TO_ENCODING: dict[str, str]
MODEL_TO_ENCODING: dict[str, str]

def encoding_name_for_model(model_name: str) -> str:
    """Returns the name of the encoding used by a model.

    Raises a KeyError if the model name is not recognised.
    """
def encoding_for_model(model_name: str) -> Encoding:
    """Returns the encoding used by a model.

    Raises a KeyError if the model name is not recognised.
    """
