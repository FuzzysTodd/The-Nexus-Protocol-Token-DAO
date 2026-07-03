import json
from _typeshed import Incomplete
from keras.saving.legacy import serialization as serialization

class Encoder(json.JSONEncoder):
    """JSON encoder and decoder that handles TensorShapes and tuples."""
    def default(self, obj):
        """Encodes objects for types that aren't handled by the default
        encoder."""
    def encode(self, obj): ...

def decode(json_string): ...
def decode_and_deserialize(json_string, module_objects: Incomplete | None = None, custom_objects: Incomplete | None = None):
    """Decodes the JSON and deserializes any Keras objects found in the dict."""
def get_json_type(obj):
    """Serializes any object to a JSON-serializable structure.

    Args:
        obj: the object to serialize

    Returns:
        JSON-serializable structure representing `obj`.

    Raises:
        TypeError: if `obj` cannot be serialized.
    """
