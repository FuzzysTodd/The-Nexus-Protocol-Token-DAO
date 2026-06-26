from _typeshed import Incomplete

def get_tensor_metadata(tensor): ...
def set_tensor_metadata(tensor, metadata) -> None: ...
def annotate(ret, **kwargs): ...

class KeyErrorMessage(str):
    """str subclass that returns itself in repr"""

class ExceptionWrapper:
    """Wraps an exception plus traceback to communicate across threads"""
    exc_type: Incomplete
    exc_msg: Incomplete
    where: Incomplete
    def __init__(self, exc_info: Incomplete | None = None, where: str = 'in background') -> None: ...
    def reraise(self) -> None:
        """Reraises the wrapped exception in the current thread"""

def get_current_device_index() -> int:
    """Checks if there are CUDA devices available and
    returns the device index of the current default CUDA device.
    Returns -1 in case there are no CUDA devices available.
    Arguments: ``None``
    """

class _ClassPropertyDescriptor:
    fget: Incomplete
    def __init__(self, fget, fset: Incomplete | None = None) -> None: ...
    def __get__(self, instance, owner: Incomplete | None = None): ...

def classproperty(func): ...
def is_compiling(): ...
