from _typeshed import Incomplete
from collections.abc import Generator
from jedi.debug import dbg as dbg
from jedi.file_io import FolderIO as FolderIO, KnownContentFileIO as KnownContentFileIO
from jedi.inference.filters import ParserTreeFilter as ParserTreeFilter
from jedi.inference.gradual.conversion import convert_names as convert_names
from jedi.inference.imports import load_module_from_path as load_module_from_path
from jedi.inference.names import SubModuleName as SubModuleName

def find_references(module_context, tree_name, only_in_module: bool = False): ...
def gitignored_paths(folder_io, file_io): ...
def expand_relative_ignore_paths(folder_io, relative_paths): ...
def recurse_find_python_folders_and_files(folder_io, except_paths=()) -> Generator[Incomplete, None, None]: ...
def recurse_find_python_files(folder_io, except_paths=()) -> Generator[Incomplete, None, None]: ...
def get_module_contexts_containing_name(inference_state, module_contexts, name, limit_reduction: int = 1) -> Generator[Incomplete, Incomplete, None]:
    """
    Search a name in the directories of modules.

    :param limit_reduction: Divides the limits on opening/parsing files by this
        factor.
    """
def search_in_file_ios(inference_state, file_io_iterator, name, limit_reduction: int = 1, complete: bool = False) -> Generator[Incomplete, None, None]: ...
