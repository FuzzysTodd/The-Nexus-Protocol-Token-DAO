from _typeshed import Incomplete
from collections.abc import Generator
from jedi.cache import memoize_method as memoize_method, signature_time_cache as signature_time_cache
from jedi.inference.base_value import NO_VALUES as NO_VALUES
from jedi.inference.compiled import get_string_value_set as get_string_value_set
from jedi.inference.helpers import infer_call_of_leaf as infer_call_of_leaf
from jedi.inference.syntax_tree import infer_atom as infer_atom
from jedi.parser_utils import get_parent_scope as get_parent_scope
from typing import NamedTuple

class CompletionParts(NamedTuple):
    path: Incomplete
    has_dot: Incomplete
    name: Incomplete

def match(string, like_name, fuzzy: bool = False): ...
def sorted_definitions(defs): ...
def get_on_completion_name(module_node, lines, position): ...

class OnErrorLeaf(Exception):
    @property
    def error_leaf(self): ...

def get_stack_at_position(grammar, code_lines, leaf, pos):
    """
    Returns the possible node names (e.g. import_from, xor_test or yield_stmt).
    """
def infer(inference_state, context, leaf): ...
def filter_follow_imports(names, follow_builtin_imports: bool = False) -> Generator[Incomplete, Incomplete, None]: ...

class CallDetails:
    bracket_leaf: Incomplete
    def __init__(self, bracket_leaf, children, position) -> None: ...
    @property
    def index(self): ...
    @property
    def keyword_name_str(self): ...
    def calculate_index(self, param_names): ...
    def iter_used_keyword_arguments(self) -> Generator[Incomplete, None, None]: ...
    def count_positional_arguments(self): ...

def get_signature_details(module, position): ...
def cache_signatures(inference_state, context, bracket_leaf, code_lines, user_pos) -> Generator[Incomplete, None, None]:
    """This function calculates the cache key."""
def validate_line_column(func): ...
def get_module_names(module, all_scopes, definitions: bool = True, references: bool = False):
    """
    Returns a dictionary with name parts as keys and their call paths as
    values.
    """
def split_search_string(name): ...
