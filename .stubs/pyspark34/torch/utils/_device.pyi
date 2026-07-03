from _typeshed import Incomplete
from torch.overrides import TorchFunctionMode as TorchFunctionMode
from torch.utils._contextlib import context_decorator as context_decorator

class DeviceContext(TorchFunctionMode):
    device: Incomplete
    def __init__(self, device) -> None: ...
    def __torch_function__(self, func, types, args=(), kwargs: Incomplete | None = None): ...

def device_decorator(device, func): ...
def set_device(device):
    """
    Decorator which sets the default device inside of the wrapped
    function.  If you would like to use this as a context manager,
    use device as a context manager directly, e.g.,
    ``with torch.device(device)``.
    """
