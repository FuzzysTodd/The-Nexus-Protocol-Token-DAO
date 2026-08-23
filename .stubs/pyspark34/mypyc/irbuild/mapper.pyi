from _typeshed import Incomplete
from mypy.nodes import ArgKind as ArgKind, FuncDef as FuncDef, RefExpr as RefExpr, SymbolNode as SymbolNode, TypeInfo as TypeInfo
from mypy.types import Type as Type
from mypyc.ir.class_ir import ClassIR as ClassIR
from mypyc.ir.func_ir import FuncDecl as FuncDecl, FuncSignature as FuncSignature, RuntimeArg as RuntimeArg
from mypyc.ir.rtypes import RInstance as RInstance, RTuple as RTuple, RType as RType, RUnion as RUnion, bool_rprimitive as bool_rprimitive, bytes_rprimitive as bytes_rprimitive, dict_rprimitive as dict_rprimitive, float_rprimitive as float_rprimitive, int16_rprimitive as int16_rprimitive, int32_rprimitive as int32_rprimitive, int64_rprimitive as int64_rprimitive, int_rprimitive as int_rprimitive, list_rprimitive as list_rprimitive, none_rprimitive as none_rprimitive, object_rprimitive as object_rprimitive, range_rprimitive as range_rprimitive, set_rprimitive as set_rprimitive, str_rprimitive as str_rprimitive, tuple_rprimitive as tuple_rprimitive, uint8_rprimitive as uint8_rprimitive

class Mapper:
    """Keep track of mappings from mypy concepts to IR concepts.

    For example, we keep track of how the mypy TypeInfos of compiled
    classes map to class IR objects.

    This state is shared across all modules being compiled in all
    compilation groups.
    """
    group_map: Incomplete
    type_to_ir: Incomplete
    func_to_decl: Incomplete
    def __init__(self, group_map: dict[str, str | None]) -> None: ...
    def type_to_rtype(self, typ: Type | None) -> RType: ...
    def get_arg_rtype(self, typ: Type, kind: ArgKind) -> RType: ...
    def fdef_to_sig(self, fdef: FuncDef) -> FuncSignature: ...
    def is_native_module(self, module: str) -> bool:
        """Is the given module one compiled by mypyc?"""
    def is_native_ref_expr(self, expr: RefExpr) -> bool: ...
    def is_native_module_ref_expr(self, expr: RefExpr) -> bool: ...
