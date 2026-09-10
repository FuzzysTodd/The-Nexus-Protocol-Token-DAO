import ast
from .utils import ast_Num as ast_Num, ast_Str as ast_Str, lineno as lineno
from _typeshed import Incomplete

class SearchSpaceGenerator(ast.NodeTransformer):
    """Generate search space from smart parater APIs"""
    module_name: Incomplete
    search_space: Incomplete
    last_line: int
    def __init__(self, module_name) -> None: ...
    def generate_mutable_layer_search_space(self, args) -> None: ...
    def visit_Call(self, node): ...

def generate(module_name, code):
    """Generate search space.
    Return a serializable search space object.
    module_name: name of the module (str)
    code: user code (str)
    """
