import ast
from .utils import ast_Num as ast_Num, ast_Str as ast_Str, lineno as lineno
from _typeshed import Incomplete
from nni.tools.nnictl.common_utils import print_warning as print_warning

para_cfg: Incomplete
prefix_name: Incomplete

def parse_annotation_mutable_layers(code, lineno):
    """Parse the string of mutable layers in annotation.
    Return a list of AST Expr nodes
    code: annotation string (excluding '@')
    """
def parse_annotation(code):
    """Parse an annotation string.
    Return an AST Expr node.
    code: annotation string (excluding '@')
    """
def parse_annotation_function(code, func_name):
    """Parse an annotation function.
    Return the value of `name` keyword argument and the AST Call node.
    func_name: expected function name
    """
def parse_nni_variable(code):
    """Parse `nni.variable` expression.
    Return the name argument and AST node of annotated expression.
    code: annotation string
    """
def parse_nni_function(code):
    """Parse `nni.function_choice` expression.
    Return the AST node of annotated expression and a list of dumped function call expressions.
    code: annotation string
    """
def convert_args_to_dict(call, with_lambda: bool = False):
    """Convert all args to a dict such that every key and value in the dict is the same as the value of the arg.
    Return the AST Call node with only one arg that is the dictionary
    """
def make_lambda(call):
    """Wrap an AST Call node to lambda expression node.
    call: ast.Call node
    """
def test_variable_equal(node1, node2):
    """Test whether two variables are the same."""
def replace_variable_node(node, annotation):
    """Replace a node annotated by `nni.variable`.
    node: the AST node to replace
    annotation: annotation string
    """
def replace_function_node(node, annotation):
    """Replace a node annotated by `nni.function_choice`.
    node: the AST node to replace
    annotation: annotation string
    """

class FuncReplacer(ast.NodeTransformer):
    """To replace target function call expressions in a node annotated by `nni.function_choice`"""
    funcs: Incomplete
    target: Incomplete
    def __init__(self, funcs, target) -> None:
        """Constructor.
        funcs: list of dumped function call expressions to replace
        target: use this AST node to replace matching expressions
        """
    def visit_Call(self, node): ...

class Transformer(ast.NodeTransformer):
    """Transform original code to annotated code"""
    stack: Incomplete
    last_line: int
    annotated: bool
    def __init__(self) -> None: ...
    def visit(self, node): ...

def parse(code, para, module):
    """Annotate user code.
    Return annotated code (str) if annotation detected; return None if not.
    code: original user code (str)
    """
