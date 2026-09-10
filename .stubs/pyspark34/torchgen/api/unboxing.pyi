from torchgen.api import cpp as cpp
from torchgen.api.types import Binding as Binding, CType as CType, CppSignatureGroup as CppSignatureGroup
from torchgen.model import Argument as Argument, BaseTy as BaseTy, BaseType as BaseType, ListType as ListType, NativeFunction as NativeFunction, OptionalType as OptionalType, Type as Type
from typing import List, Tuple

connector: str

def name(f: NativeFunction) -> str: ...
def convert_arguments(f: NativeFunction) -> Tuple[List[Binding], List[str]]: ...
def argumenttype_ivalue_convert(t: Type, arg_name: str, *, mutable: bool = False) -> Tuple[str, CType, List[str], List[str]]: ...
