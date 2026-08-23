from _typeshed import Incomplete
from mypy.build import Graph as Graph
from mypy.nodes import ClassDef, Decorator, Expression as Expression, FuncDef, MemberExpr, MypyFile as MypyFile, OverloadedFuncDef, SymbolNode as SymbolNode, TypeInfo
from mypy.traverser import TraverserVisitor
from mypy.types import Type as Type
from mypyc.common import PROPSET_PREFIX as PROPSET_PREFIX, get_id_from_name as get_id_from_name
from mypyc.crash import catch_errors as catch_errors
from mypyc.errors import Errors as Errors
from mypyc.ir.class_ir import ClassIR as ClassIR
from mypyc.ir.func_ir import FUNC_CLASSMETHOD as FUNC_CLASSMETHOD, FUNC_NORMAL as FUNC_NORMAL, FUNC_STATICMETHOD as FUNC_STATICMETHOD, FuncDecl as FuncDecl, FuncSignature as FuncSignature, RuntimeArg as RuntimeArg
from mypyc.ir.ops import DeserMaps as DeserMaps
from mypyc.ir.rtypes import RInstance as RInstance, RType as RType, dict_rprimitive as dict_rprimitive, none_rprimitive as none_rprimitive, tuple_rprimitive as tuple_rprimitive
from mypyc.irbuild.mapper import Mapper as Mapper
from mypyc.irbuild.util import get_func_def as get_func_def, get_mypyc_attrs as get_mypyc_attrs, is_dataclass as is_dataclass, is_extension_class as is_extension_class, is_trait as is_trait
from mypyc.options import CompilerOptions as CompilerOptions
from mypyc.sametype import is_same_type as is_same_type
from typing import Iterable, NamedTuple, Tuple

def build_type_map(mapper: Mapper, modules: list[MypyFile], graph: Graph, types: dict[Expression, Type], options: CompilerOptions, errors: Errors) -> None: ...
def is_from_module(node: SymbolNode, module: MypyFile) -> bool: ...
def load_type_map(mapper: Mapper, modules: list[MypyFile], deser_ctx: DeserMaps) -> None:
    """Populate a Mapper with deserialized IR from a list of modules."""
def get_module_func_defs(module: MypyFile) -> Iterable[FuncDef]:
    """Collect all of the (non-method) functions declared in a module."""
def prepare_func_def(module_name: str, class_name: str | None, fdef: FuncDef, mapper: Mapper) -> FuncDecl: ...
def prepare_method_def(ir: ClassIR, module_name: str, cdef: ClassDef, mapper: Mapper, node: FuncDef | Decorator) -> None: ...
def is_valid_multipart_property_def(prop: OverloadedFuncDef) -> bool: ...
def can_subclass_builtin(builtin_base: str) -> bool: ...
def prepare_class_def(path: str, module_name: str, cdef: ClassDef, errors: Errors, mapper: Mapper) -> None:
    """Populate the interface-level information in a class IR.

    This includes attribute and method declarations, and the MRO, among other things, but
    method bodies are generated in a later pass.
    """
def prepare_methods_and_attributes(cdef: ClassDef, ir: ClassIR, path: str, module_name: str, errors: Errors, mapper: Mapper) -> None:
    """Populate attribute and method declarations."""
def prepare_implicit_property_accessors(info: TypeInfo, ir: ClassIR, module_name: str, mapper: Mapper) -> None: ...
def add_property_methods_for_attribute_if_needed(info: TypeInfo, ir: ClassIR, attr_name: str, attr_rtype: RType, module_name: str, mapper: Mapper) -> None:
    """Add getter and/or setter for attribute if defined as property in a base class.

    Only add declarations. The body IR will be synthesized later during irbuild.
    """
def add_getter_declaration(ir: ClassIR, attr_name: str, attr_rtype: RType, module_name: str) -> None: ...
def add_setter_declaration(ir: ClassIR, attr_name: str, attr_rtype: RType, module_name: str) -> None: ...
def prepare_init_method(cdef: ClassDef, ir: ClassIR, module_name: str, mapper: Mapper) -> None: ...
def prepare_non_ext_class_def(path: str, module_name: str, cdef: ClassDef, errors: Errors, mapper: Mapper) -> None: ...
RegisterImplInfo = Tuple[TypeInfo, FuncDef]

class SingledispatchInfo(NamedTuple):
    singledispatch_impls: dict[FuncDef, list[RegisterImplInfo]]
    decorators_to_remove: dict[FuncDef, list[int]]

def find_singledispatch_register_impls(modules: list[MypyFile], errors: Errors) -> SingledispatchInfo: ...

class SingledispatchVisitor(TraverserVisitor):
    current_path: str
    singledispatch_impls: Incomplete
    decorators_to_remove: Incomplete
    errors: Incomplete
    def __init__(self, errors: Errors) -> None: ...
    def visit_decorator(self, dec: Decorator) -> None: ...

class RegisteredImpl(NamedTuple):
    singledispatch_func: FuncDef
    dispatch_type: TypeInfo

def get_singledispatch_register_call_info(decorator: Expression, func: FuncDef) -> RegisteredImpl | None: ...
def registered_impl_from_possible_register_call(expr: MemberExpr, dispatch_type: TypeInfo) -> RegisteredImpl | None: ...
