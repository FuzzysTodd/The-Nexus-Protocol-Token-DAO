import abc
from _typeshed import Incomplete
from abc import abstractmethod
from mypy.moduleinspect import is_c_module as is_c_module
from mypy.stubdoc import ArgSig as ArgSig, FunctionSig as FunctionSig, infer_arg_sig_from_anon_docstring as infer_arg_sig_from_anon_docstring, infer_prop_type_from_docstring as infer_prop_type_from_docstring, infer_ret_type_sig_from_anon_docstring as infer_ret_type_sig_from_anon_docstring, infer_ret_type_sig_from_docstring as infer_ret_type_sig_from_docstring, infer_sig_from_docstring as infer_sig_from_docstring
from types import ModuleType
from typing import Any, Iterable

class SignatureGenerator(metaclass=abc.ABCMeta):
    """Abstract base class for extracting a list of FunctionSigs for each function."""
    def remove_self_type(self, inferred: list[FunctionSig] | None, self_var: str) -> list[FunctionSig] | None:
        """Remove type annotation from self/cls argument"""
    @abstractmethod
    def get_function_sig(self, func: object, module_name: str, name: str) -> list[FunctionSig] | None: ...
    @abstractmethod
    def get_method_sig(self, cls: type, func: object, module_name: str, class_name: str, name: str, self_var: str) -> list[FunctionSig] | None: ...

class ExternalSignatureGenerator(SignatureGenerator):
    func_sigs: Incomplete
    class_sigs: Incomplete
    def __init__(self, func_sigs: dict[str, str] | None = None, class_sigs: dict[str, str] | None = None) -> None:
        """
        Takes a mapping of function/method names to signatures and class name to
        class signatures (usually corresponds to __init__).
        """
    def get_function_sig(self, func: object, module_name: str, name: str) -> list[FunctionSig] | None: ...
    def get_method_sig(self, cls: type, func: object, module_name: str, class_name: str, name: str, self_var: str) -> list[FunctionSig] | None: ...

class DocstringSignatureGenerator(SignatureGenerator):
    def get_function_sig(self, func: object, module_name: str, name: str) -> list[FunctionSig] | None: ...
    def get_method_sig(self, cls: type, func: object, module_name: str, class_name: str, func_name: str, self_var: str) -> list[FunctionSig] | None: ...

class FallbackSignatureGenerator(SignatureGenerator):
    def get_function_sig(self, func: object, module_name: str, name: str) -> list[FunctionSig] | None: ...
    def get_method_sig(self, cls: type, func: object, module_name: str, class_name: str, name: str, self_var: str) -> list[FunctionSig] | None: ...

def generate_stub_for_c_module(module_name: str, target: str, known_modules: list[str], sig_generators: Iterable[SignatureGenerator]) -> None:
    '''Generate stub for C module.

    Signature generators are called in order until a list of signatures is returned.  The order
    is:
    - signatures inferred from .rst documentation (if given)
    - simple runtime introspection (looking for docstrings and attributes
      with simple builtin types)
    - fallback based special method names or "(*args, **kwargs)"

    If directory for target doesn\'t exist it will be created. Existing stub
    will be overwritten.
    '''
def add_typing_import(output: list[str]) -> list[str]:
    """Add typing imports for collections/types that occur in the generated stub."""
def get_members(obj: object) -> list[tuple[str, Any]]: ...
def is_c_function(obj: object) -> bool: ...
def is_c_method(obj: object) -> bool: ...
def is_c_classmethod(obj: object) -> bool: ...
def is_c_property(obj: object) -> bool: ...
def is_c_property_readonly(prop: Any) -> bool: ...
def is_c_type(obj: object) -> bool: ...
def is_pybind11_overloaded_function_docstring(docstr: str, name: str) -> bool: ...
def generate_c_function_stub(module: ModuleType, name: str, obj: object, *, known_modules: list[str], sig_generators: Iterable[SignatureGenerator], output: list[str], imports: list[str], self_var: str | None = None, cls: type | None = None, class_name: str | None = None) -> None:
    """Generate stub for a single function or method.

    The result (always a single line) will be appended to 'output'.
    If necessary, any required names will be added to 'imports'.
    The 'class_name' is used to find signature of __init__ or __new__ in
    'class_sigs'.
    """
def strip_or_import(typ: str, module: ModuleType, known_modules: list[str], imports: list[str]) -> str:
    """Strips unnecessary module names from typ.

    If typ represents a type that is inside module or is a type coming from builtins, remove
    module declaration from it. Return stripped name of the type.

    Arguments:
        typ: name of the type
        module: in which this type is used
        known_modules: other modules being processed
        imports: list of import statements (may be modified during the call)
    """
def is_static_property(obj: object) -> bool: ...
def generate_c_property_stub(name: str, obj: object, static_properties: list[str], rw_properties: list[str], ro_properties: list[str], readonly: bool, module: ModuleType | None = None, known_modules: list[str] | None = None, imports: list[str] | None = None) -> None:
    """Generate property stub using introspection of 'obj'.

    Try to infer type from docstring, append resulting lines to 'output'.
    """
def generate_c_type_stub(module: ModuleType, class_name: str, obj: type, output: list[str], known_modules: list[str], imports: list[str], sig_generators: Iterable[SignatureGenerator]) -> None:
    """Generate stub for a single class using runtime introspection.

    The result lines will be appended to 'output'. If necessary, any
    required names will be added to 'imports'.
    """
def get_type_fullname(typ: type) -> str: ...
def method_name_sort_key(name: str) -> tuple[int, str]:
    """Sort methods in classes in a typical order.

    I.e.: constructor, normal methods, special methods.
    """
def is_pybind_skipped_attribute(attr: str) -> bool: ...
def is_skipped_attribute(attr: str) -> bool: ...
def infer_method_args(name: str, self_var: str | None = None) -> list[ArgSig]: ...
def infer_method_ret_type(name: str) -> str: ...
