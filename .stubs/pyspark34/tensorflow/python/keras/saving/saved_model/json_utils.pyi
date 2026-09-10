import json
from tensorflow.python.framework import dtypes as dtypes, tensor_shape as tensor_shape, type_spec as type_spec

class Encoder(json.JSONEncoder):
    """JSON encoder and decoder that handles TensorShapes and tuples."""
    def default(self, obj):
        """Encodes objects for types that aren't handled by the default encoder."""
    def encode(self, obj): ...

def decode(json_string): ...
def get_json_type(obj):
    """Serializes any object to a JSON-serializable structure.

  Args:
      obj: the object to serialize

  Returns:
      JSON-serializable structure representing `obj`.

  Raises:
      TypeError: if `obj` cannot be serialized.
  """
