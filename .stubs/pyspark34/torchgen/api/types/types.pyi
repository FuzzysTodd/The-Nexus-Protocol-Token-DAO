from .types_base import BaseCType as BaseCType, BaseCppType as BaseCppType, CType as CType, boolT as boolT, byteT as byteT, charT as charT, doubleT as doubleT, floatT as floatT, int32T as int32T, longT as longT, shortT as shortT
from _typeshed import Incomplete
from dataclasses import dataclass
from torchgen.model import BaseTy as BaseTy, ScalarType as ScalarType
from typing import Dict

TENSOR_LIST_LIKE_CTYPES: Incomplete
halfT: Incomplete
complexHalfT: Incomplete
complexFloatT: Incomplete
complexDoubleT: Incomplete
bfloat16T: Incomplete
stringT: Incomplete
generatorT: Incomplete
scalarTypeT: Incomplete
tensorT: Incomplete
optionalTensorRefT: Incomplete
tensorListT: Incomplete
iTensorListRefT: Incomplete
iOptTensorListRefT: Incomplete
dimnameT: Incomplete
dimnameListT: Incomplete
dimVectorT: Incomplete
layoutT: Incomplete
deviceT: Incomplete
scalarT: Incomplete
optionalScalarRefT: Incomplete
memoryFormatT: Incomplete
qschemeT: Incomplete
storageT: Incomplete
streamT: Incomplete
intArrayRefT: Incomplete
optionalIntArrayRefT: Incomplete
optionalSymIntArrayRefT: Incomplete
tensorOptionsT: Incomplete
typeAndSizeT: Incomplete
tensorGeometryT: Incomplete
SymIntT: Incomplete
symIntArrayRefT: Incomplete
scalar_t: Incomplete
opmath_t: Incomplete
ScalarTypeToCppMapping: Dict[ScalarType, BaseCppType]
BaseTypeToCppMapping: Dict[BaseTy, BaseCppType]

@dataclass(frozen=True)
class OptionalCType(CType):
    elem: CType
    def cpp_type(self, *, strip_ref: bool = False) -> str: ...
    def cpp_type_registration_declarations(self) -> str: ...
    def remove_const_ref(self) -> CType: ...
    def __init__(self, elem) -> None: ...

@dataclass(frozen=True)
class ListCType(CType):
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

@dataclass(frozen=True)
class VectorizedCType(CType):
    elem: BaseCType
    def cpp_type(self, *, strip_ref: bool = False) -> str: ...
    def cpp_type_registration_declarations(self) -> str: ...
    def remove_const_ref(self) -> CType: ...
    def __init__(self, elem) -> None: ...
