import abc
from _typeshed import Incomplete
from collections.abc import Generator
from jedi.inference import compiled as compiled
from jedi.inference.base_value import TreeValue as TreeValue, ValueSet as ValueSet
from jedi.inference.cache import inference_state_method_cache as inference_state_method_cache
from jedi.inference.compiled import create_simple_object as create_simple_object
from jedi.inference.context import ModuleContext as ModuleContext
from jedi.inference.filters import DictFilter as DictFilter, GlobalNameFilter as GlobalNameFilter, MergedFilter as MergedFilter, ParserTreeFilter as ParserTreeFilter
from jedi.inference.helpers import values_from_qualified_names as values_from_qualified_names
from jedi.inference.names import AbstractNameDefinition as AbstractNameDefinition, ModuleName as ModuleName, SubModuleName as SubModuleName
from pathlib import Path

class _ModuleAttributeName(AbstractNameDefinition, metaclass=abc.ABCMeta):
    """
    For module attributes like __file__, __str__ and so on.
    """
    api_type: str
    parent_context: Incomplete
    string_name: Incomplete
    def __init__(self, parent_module, string_name, string_value: Incomplete | None = None) -> None: ...
    def infer(self): ...

class SubModuleDictMixin:
    def sub_modules_dict(self):
        """
        Lists modules in the directory of this module (if this module is a
        package).
        """

class ModuleMixin(SubModuleDictMixin):
    def get_filters(self, origin_scope: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]: ...
    def py__class__(self): ...
    def is_module(self): ...
    def is_stub(self): ...
    @property
    def name(self): ...
    def iter_star_filters(self) -> Generator[Incomplete, None, None]: ...
    def star_imports(self): ...
    def get_qualified_names(self):
        """
        A module doesn't have a qualified name, but it's important to note that
        it's reachable and not `None`. With this information we can add
        qualified names on top for all value children.
        """

class ModuleValue(ModuleMixin, TreeValue):
    api_type: str
    file_io: Incomplete
    string_names: Incomplete
    code_lines: Incomplete
    def __init__(self, inference_state, module_node, code_lines, file_io: Incomplete | None = None, string_names: Incomplete | None = None, is_package: bool = False) -> None: ...
    def is_stub(self): ...
    def py__name__(self): ...
    def py__file__(self) -> Path | None:
        """
        In contrast to Python's __file__ can be None.
        """
    def is_package(self): ...
    def py__package__(self): ...
    def py__path__(self):
        """
        In case of a package, this returns Python's __path__ attribute, which
        is a list of paths (strings).
        Returns None if the module is not a package.
        """
