import abc
from jedi.api.classes import Completion as Completion
from jedi.inference.helpers import infer_call_of_leaf as infer_call_of_leaf
from jedi.inference.names import AbstractArbitraryName as AbstractArbitraryName
from jedi.parser_utils import cut_value_at_position as cut_value_at_position

class StringName(AbstractArbitraryName, metaclass=abc.ABCMeta):
    api_type: str
    is_value_name: bool

def complete_dict(module_context, code_lines, leaf, position, string, fuzzy): ...
def get_quote_ending(string, code_lines, position, invert_result: bool = False): ...
