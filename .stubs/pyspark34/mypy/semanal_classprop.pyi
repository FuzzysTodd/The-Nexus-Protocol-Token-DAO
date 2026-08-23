from _typeshed import Incomplete
from mypy.errors import Errors as Errors
from mypy.nodes import CallExpr as CallExpr, Decorator as Decorator, FuncDef as FuncDef, IMPLICITLY_ABSTRACT as IMPLICITLY_ABSTRACT, IS_ABSTRACT as IS_ABSTRACT, Node as Node, OverloadedFuncDef as OverloadedFuncDef, PromoteExpr as PromoteExpr, SymbolTable as SymbolTable, TypeInfo as TypeInfo, Var as Var
from mypy.options import Options as Options
from mypy.types import Instance as Instance, MYPYC_NATIVE_INT_NAMES as MYPYC_NATIVE_INT_NAMES, ProperType as ProperType
from typing_extensions import Final

TYPE_PROMOTIONS: Final[Incomplete]

def calculate_class_abstract_status(typ: TypeInfo, is_stub_file: bool, errors: Errors) -> None:
    """Calculate abstract status of a class.

    Set is_abstract of the type to True if the type has an unimplemented
    abstract attribute.  Also compute a list of abstract attributes.
    Report error is required ABCMeta metaclass is missing.
    """
def check_protocol_status(info: TypeInfo, errors: Errors) -> None:
    """Check that all classes in MRO of a protocol are protocols"""
def calculate_class_vars(info: TypeInfo) -> None:
    """Try to infer additional class variables.

    Subclass attribute assignments with no type annotation are assumed
    to be classvar if overriding a declared classvar from the base
    class.

    This must happen after the main semantic analysis pass, since
    this depends on base class bodies having been fully analyzed.
    """
def add_type_promotion(info: TypeInfo, module_names: SymbolTable, options: Options, builtin_names: SymbolTable) -> None:
    """Setup extra, ad-hoc subtyping relationships between classes (promotion).

    This includes things like 'int' being compatible with 'float'.
    """
