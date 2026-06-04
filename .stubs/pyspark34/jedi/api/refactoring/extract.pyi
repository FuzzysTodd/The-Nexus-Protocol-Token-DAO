from jedi import debug as debug
from jedi.api.exceptions import RefactoringError as RefactoringError
from jedi.api.refactoring import EXPRESSION_PARTS as EXPRESSION_PARTS, Refactoring as Refactoring
from jedi.common import indent_block as indent_block
from jedi.parser_utils import function_is_classmethod as function_is_classmethod, function_is_staticmethod as function_is_staticmethod

def extract_variable(inference_state, path, module_node, name, pos, until_pos): ...
def extract_function(inference_state, path, module_context, name, pos, until_pos): ...
