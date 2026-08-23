from . import PyrexTypes as PyrexTypes
from .Code import TempitaUtilityCode as TempitaUtilityCode, UtilityCode as UtilityCode
from .StringEncoding import EncodedString as EncodedString
from .Symtab import BuiltinScope as BuiltinScope, Entry as Entry, ModuleScope as ModuleScope, StructOrUnionScope as StructOrUnionScope
from .TypeSlots import Signature as Signature
from _typeshed import Incomplete

iter_next_utility_code: Incomplete
getattr_utility_code: Incomplete
getattr3_utility_code: Incomplete
pyexec_utility_code: Incomplete
pyexec_globals_utility_code: Incomplete
globals_utility_code: Incomplete
builtin_utility_code: Incomplete

class _BuiltinOverride:
    builtin_return_type: Incomplete
    is_strict_signature: Incomplete
    utility_code: Incomplete
    nogil: Incomplete
    def __init__(self, py_name, args, ret_type, cname, py_equiv: str = '*', utility_code: Incomplete | None = None, sig: Incomplete | None = None, func_type: Incomplete | None = None, is_strict_signature: bool = False, builtin_return_type: Incomplete | None = None, nogil: Incomplete | None = None) -> None: ...
    def build_func_type(self, sig: Incomplete | None = None, self_arg: Incomplete | None = None): ...

class BuiltinAttribute:
    py_name: Incomplete
    cname: Incomplete
    field_type_name: Incomplete
    field_type: Incomplete
    def __init__(self, py_name, cname: Incomplete | None = None, field_type: Incomplete | None = None, field_type_name: Incomplete | None = None) -> None: ...
    def declare_in_type(self, self_type) -> None: ...

class BuiltinFunction(_BuiltinOverride):
    def declare_in_scope(self, scope) -> None: ...

class BuiltinMethod(_BuiltinOverride):
    def declare_in_type(self, self_type) -> None: ...

class BuiltinProperty:
    py_name: Incomplete
    property_type: Incomplete
    call_cname: Incomplete
    utility_code: Incomplete
    exception_value: Incomplete
    exception_check: Incomplete
    def __init__(self, py_name, property_type, call_cname, exception_value: Incomplete | None = None, exception_check: Incomplete | None = None, utility_code: Incomplete | None = None) -> None: ...
    def declare_in_type(self, self_type) -> None: ...

builtin_function_table: Incomplete
builtin_types_table: Incomplete
types_that_construct_their_instance: Incomplete
builtin_structs_table: Incomplete
builtin_scope: Incomplete

def init_builtin_funcs() -> None: ...

builtin_types: Incomplete

def init_builtin_types() -> None: ...
def init_builtin_structs() -> None: ...
def init_builtins() -> None: ...
def get_known_standard_library_module_scope(module_name): ...
def get_known_standard_library_entry(qualified_name): ...
def exprnode_to_known_standard_library_name(node, env): ...
