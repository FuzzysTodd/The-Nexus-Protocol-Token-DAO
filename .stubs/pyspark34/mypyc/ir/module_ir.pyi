from _typeshed import Incomplete
from mypyc.common import JsonDict as JsonDict
from mypyc.ir.class_ir import ClassIR as ClassIR
from mypyc.ir.func_ir import FuncDecl as FuncDecl, FuncIR as FuncIR
from mypyc.ir.ops import DeserMaps as DeserMaps
from mypyc.ir.rtypes import RType as RType, deserialize_type as deserialize_type
from typing import Dict

class ModuleIR:
    """Intermediate representation of a module."""
    fullname: Incomplete
    imports: Incomplete
    functions: Incomplete
    classes: Incomplete
    final_names: Incomplete
    def __init__(self, fullname: str, imports: list[str], functions: list[FuncIR], classes: list[ClassIR], final_names: list[tuple[str, RType]]) -> None: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict, ctx: DeserMaps) -> ModuleIR: ...

def deserialize_modules(data: dict[str, JsonDict], ctx: DeserMaps) -> dict[str, ModuleIR]:
    """Deserialize a collection of modules.

    The modules can contain dependencies on each other.

    Arguments:
        data: A dict containing the modules to deserialize.
        ctx: The deserialization maps to use and to populate.
             They are populated with information from the deserialized
             modules and as a precondition must have been populated by
             deserializing any dependencies of the modules being deserialized
             (outside of dependencies between the modules themselves).

    Returns a map containing the deserialized modules.
    """
ModuleIRs = Dict[str, ModuleIR]
