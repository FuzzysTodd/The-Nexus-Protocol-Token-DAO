from _typeshed import Incomplete
from collections.abc import Generator
from jedi import debug as debug, settings as settings
from jedi.file_io import FolderIO as FolderIO
from jedi.inference import analysis as analysis, compiled as compiled, helpers as helpers, sys_path as sys_path
from jedi.inference.base_value import NO_VALUES as NO_VALUES, ValueSet as ValueSet
from jedi.inference.cache import inference_state_method_cache as inference_state_method_cache
from jedi.inference.compiled.subprocess.functions import ImplicitNSInfo as ImplicitNSInfo
from jedi.inference.gradual.typeshed import create_stub_module as create_stub_module, import_module_decorator as import_module_decorator, parse_stub_module as parse_stub_module
from jedi.inference.names import ImportName as ImportName, SubModuleName as SubModuleName
from jedi.inference.utils import unite as unite
from jedi.parser_utils import get_cached_code_lines as get_cached_code_lines
from jedi.plugins import plugin_manager as plugin_manager

class ModuleCache:
    def __init__(self) -> None: ...
    def add(self, string_names, value_set) -> None: ...
    def get(self, string_names): ...

def infer_import(context, tree_name): ...
def goto_import(context, tree_name): ...

class Importer:
    level: Incomplete
    import_path: Incomplete
    def __init__(self, inference_state, import_path, module_context, level: int = 0) -> None:
        """
        An implementation similar to ``__import__``. Use `follow`
        to actually follow the imports.

        *level* specifies whether to use absolute or relative imports. 0 (the
        default) means only perform absolute imports. Positive values for level
        indicate the number of parent directories to search relative to the
        directory of the module calling ``__import__()`` (see PEP 328 for the
        details).

        :param import_path: List of namespaces (strings or Names).
        """
    def follow(self): ...
    def completion_names(self, inference_state, only_modules: bool = False):
        """
        :param only_modules: Indicates wheter it's possible to import a
            definition that is not defined in a module.
        """

def import_module_by_names(inference_state, import_names, sys_path: Incomplete | None = None, module_context: Incomplete | None = None, prefer_stubs: bool = True): ...
def import_module(inference_state, import_names, parent_module_value, sys_path):
    """
    This method is very similar to importlib's `_gcd_import`.
    """
def load_module_from_path(inference_state, file_io, import_names: Incomplete | None = None, is_package: Incomplete | None = None):
    """
    This should pretty much only be used for get_modules_containing_name. It's
    here to ensure that a random path is still properly loaded into the Jedi
    module structure.
    """
def load_namespace_from_path(inference_state, folder_io): ...
def follow_error_node_imports_if_possible(context, name): ...
def iter_module_names(inference_state, module_context, search_path, module_cls=..., add_builtin_modules: bool = True) -> Generator[Incomplete, None, None]:
    """
    Get the names of all modules in the search_path. This means file names
    and not names defined in the files.
    """
