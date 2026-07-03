from tensorflow.python.eager import def_function as def_function
from tensorflow.python.framework import composite_tensor as composite_tensor, ops as ops, tensor_spec as tensor_spec
from tensorflow.python.ops import resource_variable_ops as resource_variable_ops
from tensorflow.python.saved_model import function_serialization as function_serialization, revived_types as revived_types, signature_constants as signature_constants
from tensorflow.python.trackable import base as base
from tensorflow.python.util import compat as compat, nest as nest
from tensorflow.python.util.compat import collections_abc as collections_abc

DEFAULT_SIGNATURE_ATTR: str
SIGNATURE_ATTRIBUTE_NAME: str

def find_function_to_export(saveable_view):
    """Function to export, None if no suitable function was found."""
def canonicalize_signatures(signatures):
    """Converts `signatures` into a dictionary of concrete functions."""

class _SignatureMap(collections_abc.Mapping, base.Trackable):
    """A collection of SavedModel signatures."""
    def __init__(self) -> None: ...
    def __getitem__(self, key): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

def create_signature_map(signatures):
    """Creates an object containing `signatures`."""
def validate_augmented_graph_view(augmented_graph_view) -> None:
    """Performs signature-related sanity checks on `augmented_graph_view`."""
