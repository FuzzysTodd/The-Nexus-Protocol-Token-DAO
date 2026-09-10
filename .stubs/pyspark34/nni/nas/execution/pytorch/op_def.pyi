from _typeshed import Incomplete
from nni.nas.execution.common import PyTorchOperation as PyTorchOperation
from typing import Any, Dict, List

mem_format: Incomplete
scalar_type_to_pytorch_type: Incomplete

class NoOpIdentity(PyTorchOperation):
    """
    this operator type is added by us
    """
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class ModuleOperator(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class FunctionalOperator(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class PrimConstant(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class PrimListConstruct(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class PrimListUnpack(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class PrimTupleConstruct(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class PrimTupleUnpack(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class PrimGetAttr(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class PrimUncheckedCast(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class SimpleMember(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class AtenContiguous(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class AtenGetitem(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class AtenAppend(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class MergedSlice(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class AtenBool(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class AtenNot(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class AtenCat(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class AtenTensors(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class AtenFloordiv(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class AtenMul(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class AtenLen(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class AtenIntImplicit(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class AtenIndex(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

ManuallyChooseDef: Incomplete
TensorOpExceptions: Incomplete
TorchOpExclude: Incomplete

class TensorOps(PyTorchOperation):
    """
    corresponding to _get_tensor_ops in torch.jit.supported_ops
    """
    comparison_ops: Incomplete
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class TorchOps(PyTorchOperation):
    """
    corresponding to _get_nn_functional_ops in torch.jit.supported_ops
    """
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class AtenAvgpool2d(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class ToDevice(PyTorchOperation):
    type: str
    device: Incomplete
    overridden_device_repr: Incomplete
    src: Incomplete
    dst: Incomplete
    def __init__(self, type_name: str, parameters: Dict[str, Any], _internal: bool = False, attributes: Dict[str, Any] = {}) -> None: ...
    def override_device_repr(self, device_repr) -> None: ...
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...

class AtenDet(PyTorchOperation):
    def to_forward_code(self, field: str, output: str, inputs: List[str], inputs_value: List[Any]) -> str: ...
