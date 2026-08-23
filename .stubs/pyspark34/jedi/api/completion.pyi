from _typeshed import Incomplete
from collections.abc import Generator
from jedi import debug as debug, settings as settings
from jedi.api import classes as classes, helpers as helpers, keywords as keywords
from jedi.api.file_name import complete_file_name as complete_file_name
from jedi.api.strings import complete_dict as complete_dict
from jedi.inference import imports as imports
from jedi.inference.base_value import ValueSet as ValueSet
from jedi.inference.context import get_global_filters as get_global_filters
from jedi.inference.docstring_utils import DocstringModule as DocstringModule
from jedi.inference.gradual.conversion import convert_names as convert_names, convert_values as convert_values
from jedi.inference.helpers import infer_call_of_leaf as infer_call_of_leaf, parse_dotted_names as parse_dotted_names
from jedi.inference.names import ParamNameWrapper as ParamNameWrapper, SubModuleName as SubModuleName
from jedi.inference.value import TreeInstance as TreeInstance
from jedi.parser_utils import cut_value_at_position as cut_value_at_position
from jedi.plugins import plugin_manager as plugin_manager

class ParamNameWithEquals(ParamNameWrapper):
    def get_public_name(self): ...

def filter_names(inference_state, completion_names, stack, like_name, fuzzy, cached_name) -> Generator[Incomplete, None, None]: ...
def get_user_context(module_context, position):
    """
    Returns the scope in which the user resides. This includes flows.
    """
def get_flow_scope_node(module_node, position): ...
def complete_param_names(context, function_name, decorator_nodes): ...

class Completion:
    def __init__(self, inference_state, module_context, code_lines, position, signatures_callback, fuzzy: bool = False) -> None: ...
    def complete(self): ...

def complete_trailer(user_context, values): ...
def search_in_module(inference_state, module_context, names, wanted_names, wanted_type, complete: bool = False, fuzzy: bool = False, ignore_imports: bool = False, convert: bool = False) -> Generator[Incomplete, None, None]: ...
