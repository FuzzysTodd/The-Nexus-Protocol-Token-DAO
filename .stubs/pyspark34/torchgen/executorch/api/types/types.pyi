from _typeshed import Incomplete
from dataclasses import dataclass
from torchgen.api.types import BaseCppType as BaseCppType, CType as CType, boolT as boolT, doubleT as doubleT, longT as longT
from torchgen.model import BaseTy as BaseTy
from typing import Dict

halfT: Incomplete
bfloat16T: Incomplete
stringT: Incomplete
scalarTypeT: Incomplete
tensorT: Incomplete
tensorListT: Incomplete
scalarT: Incomplete
memoryFormatT: Incomplete
intArrayRefT: Incomplete
optionalT: Incomplete
BaseTypeToCppMapping: Dict[BaseTy, BaseCppType]

@dataclass(frozen=True)
class OptionalCType(CType):
    elem: CType
    def cpp_type(self, *, strip_ref: bool = False) -> str: ...
    def cpp_type_registration_declarations(self) -> str: ...
    def remove_const_ref(self) -> CType: ...
    def __init__(self, elem) -> None: ...

@dataclass(frozen=True)
class ArrayRefCType(CType):
    elem: CType
    def cpp_type(self, *, strip_ref: bool = False) -> str: ...
    def cpp_type_registration_declarations(self) -> str: ...
    def remove_const_ref(self) -> CType: ...
    def __init__(self, elem) -> None: ...
