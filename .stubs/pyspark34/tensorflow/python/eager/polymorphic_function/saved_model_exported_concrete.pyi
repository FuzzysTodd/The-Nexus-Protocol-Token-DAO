from _typeshed import Incomplete
from tensorflow.python.trackable import base as trackable

class ExportedConcreteFunction(trackable.Trackable):
    """A callable class that uses captures from the exported SavedModel graph."""
    function: Incomplete
    tensor_map: Incomplete
    def __init__(self, function, tensor_map) -> None: ...
    def __call__(self, *args, **kwargs): ...
