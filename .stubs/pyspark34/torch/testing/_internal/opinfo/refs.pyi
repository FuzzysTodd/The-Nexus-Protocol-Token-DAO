from _typeshed import Incomplete
from torch.testing._internal.opinfo.core import BinaryUfuncInfo as BinaryUfuncInfo, OpInfo as OpInfo, ReductionOpInfo as ReductionOpInfo, UnaryUfuncInfo as UnaryUfuncInfo

class PythonRefInfo(OpInfo):
    """
    An OpInfo for a Python reference of an OpInfo base class operation.
    """
    torch_opinfo_name: Incomplete
    torch_opinfo_variant_name: Incomplete
    torch_opinfo: Incomplete
    validate_view_consistency: Incomplete
    supports_nvfuser: Incomplete
    def __init__(self, name, *, op: Incomplete | None = None, op_db: Incomplete | None = None, torch_opinfo_name, torch_opinfo_variant_name: str = '', validate_view_consistency: bool = True, supports_nvfuser: bool = True, **kwargs) -> None: ...

class ReductionPythonRefInfo(ReductionOpInfo):
    """
    An OpInfo for a Python reference of an elementwise unary operation.
    """
    torch_opinfo_name: Incomplete
    torch_opinfo_variant_name: Incomplete
    torch_opinfo: Incomplete
    supports_nvfuser: Incomplete
    validate_view_consistency: bool
    def __init__(self, name, *, op: Incomplete | None = None, op_db: Incomplete | None = None, torch_opinfo_name, torch_opinfo_variant_name: str = '', supports_nvfuser: bool = True, **kwargs) -> None: ...

class ElementwiseUnaryPythonRefInfo(UnaryUfuncInfo):
    """
    An OpInfo for a Python reference of an elementwise unary operation.
    """
    torch_opinfo_name: Incomplete
    torch_opinfo_variant_name: Incomplete
    torch_opinfo: Incomplete
    validate_view_consistency: Incomplete
    supports_nvfuser: Incomplete
    def __init__(self, name, *, op: Incomplete | None = None, op_db: Incomplete | None = None, torch_opinfo_name, torch_opinfo_variant_name: str = '', validate_view_consistency: bool = True, supports_nvfuser: bool = True, **kwargs) -> None: ...

class ElementwiseBinaryPythonRefInfo(BinaryUfuncInfo):
    """
    An OpInfo for a Python reference of an elementwise binary operation.
    """
    torch_opinfo_name: Incomplete
    torch_opinfo_variant_name: Incomplete
    torch_opinfo: Incomplete
    supports_nvfuser: Incomplete
    def __init__(self, name, *, op: Incomplete | None = None, op_db: Incomplete | None = None, torch_opinfo_name, torch_opinfo_variant_name: str = '', supports_nvfuser: bool = True, **kwargs) -> None: ...
