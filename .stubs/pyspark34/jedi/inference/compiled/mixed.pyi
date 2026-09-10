from _typeshed import Incomplete
from collections.abc import Generator
from jedi import settings as settings
from jedi.cache import memoize_method as memoize_method
from jedi.file_io import FileIO as FileIO
from jedi.inference import compiled as compiled
from jedi.inference.base_value import NO_VALUES as NO_VALUES, ValueSet as ValueSet, ValueWrapper as ValueWrapper
from jedi.inference.cache import inference_state_function_cache as inference_state_function_cache, inference_state_method_cache as inference_state_method_cache
from jedi.inference.compiled.access import ALLOWED_GETITEM_TYPES as ALLOWED_GETITEM_TYPES, get_api_type as get_api_type
from jedi.inference.context import CompiledContext as CompiledContext, CompiledModuleContext as CompiledModuleContext, TreeContextMixin as TreeContextMixin
from jedi.inference.gradual.conversion import to_stub as to_stub
from jedi.inference.names import NameWrapper as NameWrapper
from jedi.inference.value import ModuleValue as ModuleValue
from jedi.parser_utils import get_cached_code_lines as get_cached_code_lines

class MixedObject(ValueWrapper):
    """
    A ``MixedObject`` is used in two ways:

    1. It uses the default logic of ``parser.python.tree`` objects,
    2. except for getattr calls and signatures. The names dicts are generated
       in a fashion like ``CompiledValue``.

    This combined logic makes it possible to provide more powerful REPL
    completion. It allows side effects that are not noticable with the default
    parser structure to still be completable.

    The biggest difference from CompiledValue to MixedObject is that we are
    generally dealing with Python code and not with C code. This will generate
    fewer special cases, because we in Python you don't have the same freedoms
    to modify the runtime.
    """
    compiled_value: Incomplete
    access_handle: Incomplete
    def __init__(self, compiled_value, tree_value) -> None: ...
    def get_filters(self, *args, **kwargs) -> Generator[Incomplete, None, None]: ...
    def get_signatures(self): ...
    def py__call__(self, arguments): ...
    def get_safe_value(self, default=...): ...
    @property
    def array_type(self): ...
    def get_key_values(self): ...
    def py__simple_getitem__(self, index): ...
    def negate(self): ...

class MixedContext(CompiledContext, TreeContextMixin):
    @property
    def compiled_value(self): ...

class MixedModuleContext(CompiledModuleContext, MixedContext): ...

class MixedName(NameWrapper):
    """
    The ``CompiledName._compiled_value`` is our MixedObject.
    """
    def __init__(self, wrapped_name, parent_tree_value) -> None: ...
    @property
    def start_pos(self): ...
    def infer(self): ...

class MixedObjectFilter(compiled.CompiledValueFilter):
    def __init__(self, inference_state, compiled_value, tree_value) -> None: ...
