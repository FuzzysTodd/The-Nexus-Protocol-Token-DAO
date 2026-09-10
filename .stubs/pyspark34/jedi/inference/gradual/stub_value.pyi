from _typeshed import Incomplete
from collections.abc import Generator
from jedi.inference.base_value import ValueWrapper as ValueWrapper
from jedi.inference.context import ModuleContext as ModuleContext
from jedi.inference.filters import ParserTreeFilter as ParserTreeFilter
from jedi.inference.gradual.typing import TypingModuleFilterWrapper as TypingModuleFilterWrapper
from jedi.inference.names import StubModuleName as StubModuleName, StubName as StubName
from jedi.inference.value.module import ModuleValue as ModuleValue

class StubModuleValue(ModuleValue):
    non_stub_value_set: Incomplete
    def __init__(self, non_stub_value_set, *args, **kwargs) -> None: ...
    def is_stub(self): ...
    def sub_modules_dict(self):
        """
        We have to overwrite this, because it's possible to have stubs that
        don't have code for all the child modules. At the time of writing this
        there are for example no stubs for `json.tool`.
        """
    def get_filters(self, origin_scope: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]: ...

class StubModuleContext(ModuleContext):
    def get_filters(self, until_position: Incomplete | None = None, origin_scope: Incomplete | None = None): ...

class TypingModuleWrapper(StubModuleValue):
    def get_filters(self, *args, **kwargs) -> Generator[Incomplete, Incomplete, None]: ...

class TypingModuleContext(ModuleContext):
    def get_filters(self, *args, **kwargs) -> Generator[Incomplete, Incomplete, None]: ...

class StubFilter(ParserTreeFilter):
    name_class = StubName

class VersionInfo(ValueWrapper): ...
