from _typeshed import Incomplete
from ast import NodeTransformer
from sympy.core.basic import Basic as Basic
from sympy.core.sympify import SympifyError as SympifyError

class Transform(NodeTransformer):
    local_dict: Incomplete
    global_dict: Incomplete
    def __init__(self, local_dict, global_dict) -> None: ...
    def visit_Constant(self, node): ...
    def visit_Name(self, node): ...
    def visit_Lambda(self, node): ...

def parse_expr(s, local_dict):
    '''
    Converts the string "s" to a SymPy expression, in local_dict.

    It converts all numbers to Integers before feeding it to Python and
    automatically creates Symbols.
    '''
