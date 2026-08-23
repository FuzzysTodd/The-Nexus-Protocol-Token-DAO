from _typeshed import Incomplete
from collections.abc import Generator
from jedi.inference import compiled as compiled
from jedi.inference.base_value import ValueSet as ValueSet
from jedi.inference.compiled import mixed as mixed
from jedi.inference.compiled.access import create_access_path as create_access_path
from jedi.inference.context import ModuleContext as ModuleContext
from jedi.inference.filters import MergedFilter as MergedFilter, ParserTreeFilter as ParserTreeFilter
from jedi.inference.names import TreeNameDefinition as TreeNameDefinition

class NamespaceObject:
    __dict__: Incomplete
    def __init__(self, dct) -> None: ...

class MixedTreeName(TreeNameDefinition):
    def infer(self):
        """
        In IPython notebook it is typical that some parts of the code that is
        provided was already executed. In that case if something is not properly
        inferred, it should still infer from the variables it already knows.
        """

class MixedParserTreeFilter(ParserTreeFilter):
    name_class = MixedTreeName

class MixedModuleContext(ModuleContext):
    mixed_values: Incomplete
    def __init__(self, tree_module_value, namespaces) -> None: ...
    def get_filters(self, until_position: Incomplete | None = None, origin_scope: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]: ...
