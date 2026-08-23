from _typeshed import Incomplete
from collections.abc import Generator
from jedi.inference.context import ModuleContext as ModuleContext
from jedi.inference.value import ModuleValue as ModuleValue

class DocstringModule(ModuleValue):
    def __init__(self, in_module_context, **kwargs) -> None: ...

class DocstringModuleContext(ModuleContext):
    def __init__(self, module_value, in_module_context) -> None: ...
    def get_filters(self, origin_scope: Incomplete | None = None, until_position: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]: ...
