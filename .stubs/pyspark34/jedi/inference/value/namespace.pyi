import abc
from _typeshed import Incomplete
from collections.abc import Generator
from jedi.inference.base_value import Value as Value
from jedi.inference.cache import inference_state_method_cache as inference_state_method_cache
from jedi.inference.context import NamespaceContext as NamespaceContext
from jedi.inference.filters import DictFilter as DictFilter
from jedi.inference.names import AbstractNameDefinition as AbstractNameDefinition, ValueNameMixin as ValueNameMixin
from jedi.inference.value.module import SubModuleDictMixin as SubModuleDictMixin
from pathlib import Path

class ImplicitNSName(ValueNameMixin, AbstractNameDefinition, metaclass=abc.ABCMeta):
    """
    Accessing names for implicit namespace packages should infer to nothing.
    This object will prevent Jedi from raising exceptions
    """
    string_name: Incomplete
    def __init__(self, implicit_ns_value, string_name) -> None: ...

class ImplicitNamespaceValue(Value, SubModuleDictMixin):
    """
    Provides support for implicit namespace packages
    """
    api_type: str
    parent_context: Incomplete
    inference_state: Incomplete
    string_names: Incomplete
    def __init__(self, inference_state, string_names, paths) -> None: ...
    def get_filters(self, origin_scope: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
    def get_qualified_names(self): ...
    @property
    def name(self): ...
    def py__file__(self) -> Path | None: ...
    def py__package__(self):
        """Return the fullname
        """
    def py__path__(self): ...
    def py__name__(self): ...
    def is_namespace(self): ...
    def is_stub(self): ...
    def is_package(self): ...
    def as_context(self): ...
