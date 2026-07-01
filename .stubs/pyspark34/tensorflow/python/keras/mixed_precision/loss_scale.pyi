from _typeshed import Incomplete
from tensorflow.python.keras.utils import generic_utils as generic_utils

def serialize(loss_scale): ...
def deserialize(config, custom_objects: Incomplete | None = None): ...
def get(identifier):
    """Get a loss scale object."""
