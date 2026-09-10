from _typeshed import Incomplete
from torch import _C
from torch.onnx._internal import registration as registration
from typing import Dict

class _TorchSchema:
    name: Incomplete
    overload_name: Incomplete
    arguments: Incomplete
    optional_arguments: Incomplete
    returns: Incomplete
    opsets: Incomplete
    def __init__(self, schema: _C.FunctionSchema | str) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other) -> bool: ...
    def is_aten(self) -> bool: ...
    def is_backward(self) -> bool: ...

def all_forward_schemas() -> Dict[str, _TorchSchema]:
    """Returns schemas for all TorchScript forward ops."""
def all_symbolics_schemas() -> Dict[str, _TorchSchema]:
    """Returns schemas for all onnx supported ops."""
