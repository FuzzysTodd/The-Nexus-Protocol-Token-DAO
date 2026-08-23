from _typeshed import Incomplete
from torchgen.api.types import ArrayRefCType as ArrayRefCType, BaseCType as BaseCType, Binding as Binding, ConstRefCType as ConstRefCType, Expr as Expr, ListCType as ListCType, MutRefCType as MutRefCType, NamedCType as NamedCType, OptionalCType as OptionalCType, SpecialArgName as SpecialArgName, SymIntT as SymIntT, VectorCType as VectorCType, boolT as boolT, deviceT as deviceT, iOptTensorListRefT as iOptTensorListRefT, intArrayRefT as intArrayRefT, layoutT as layoutT, longT as longT, memoryFormatT as memoryFormatT, opmath_t as opmath_t, optionalIntArrayRefT as optionalIntArrayRefT, optionalScalarRefT as optionalScalarRefT, optionalSymIntArrayRefT as optionalSymIntArrayRefT, optionalTensorRefT as optionalTensorRefT, scalarT as scalarT, scalarTypeT as scalarTypeT, scalar_t as scalar_t, symIntArrayRefT as symIntArrayRefT, tensorOptionsT as tensorOptionsT, tensorT as tensorT
from typing import List, Sequence

options_ctype: Incomplete
out_tensor_ctype: Incomplete
longVec_ctype: Incomplete
longSymVec_ctype: Incomplete
optionalLongVec_ctype: Incomplete
optionalScalar_ctype: Incomplete
optionalTensor_ctype: Incomplete

class UnsatError(RuntimeError): ...

def translate(bindings: Sequence[Expr | Binding], goals: Sequence[NamedCType | Binding], *, method: bool = False, allow_expensive_conversions: bool = False) -> List[Expr]: ...
