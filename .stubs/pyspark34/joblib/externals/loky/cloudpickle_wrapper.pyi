from _typeshed import Incomplete
from joblib.externals.cloudpickle import dumps as dumps, loads as loads

WRAP_CACHE: Incomplete

class CloudpickledObjectWrapper:
    def __init__(self, obj, keep_wrapper: bool = False) -> None: ...
    def __reduce__(self): ...
    def __getattr__(self, attr): ...

class CallableObjectWrapper(CloudpickledObjectWrapper):
    def __call__(self, *args, **kwargs): ...

def wrap_non_picklable_objects(obj, keep_wrapper: bool = True):
    """Wrapper for non-picklable object to use cloudpickle to serialize them.

    Note that this wrapper tends to slow down the serialization process as it
    is done with cloudpickle which is typically slower compared to pickle. The
    proper way to solve serialization issues is to avoid defining functions and
    objects in the main scripts and to implement __reduce__ functions for
    complex classes.
    """
