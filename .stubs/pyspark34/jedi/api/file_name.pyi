import abc
from _typeshed import Incomplete
from collections.abc import Generator
from jedi.api import classes as classes
from jedi.api.helpers import match as match
from jedi.api.strings import StringName as StringName, get_quote_ending as get_quote_ending
from jedi.inference.helpers import get_str_or_none as get_str_or_none

class PathName(StringName, metaclass=abc.ABCMeta):
    api_type: str

def complete_file_name(inference_state, module_context, start_leaf, quote, string, like_name, signatures_callback, code_lines, position, fuzzy) -> Generator[Incomplete, None, Incomplete]: ...
