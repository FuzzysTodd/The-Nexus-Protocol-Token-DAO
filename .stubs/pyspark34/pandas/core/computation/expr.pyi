import ast
from _typeshed import Incomplete
from pandas.compat import PY39 as PY39
from pandas.core.computation.ops import ARITH_OPS_SYMS as ARITH_OPS_SYMS, BOOL_OPS_SYMS as BOOL_OPS_SYMS, BinOp as BinOp, CMP_OPS_SYMS as CMP_OPS_SYMS, Constant as Constant, Div as Div, FuncNode as FuncNode, LOCAL_TAG as LOCAL_TAG, MATHOPS as MATHOPS, Op as Op, REDUCTIONS as REDUCTIONS, Term as Term, UNARY_OPS_SYMS as UNARY_OPS_SYMS, UnaryOp as UnaryOp, is_term as is_term
from pandas.core.computation.parsing import clean_backtick_quoted_toks as clean_backtick_quoted_toks, tokenize_string as tokenize_string
from pandas.core.computation.scope import Scope as Scope
from pandas.errors import UndefinedVariableError as UndefinedVariableError
from pandas.io.formats import printing as printing
from typing import Callable

intersection: Incomplete

def disallow(nodes: set[str]) -> Callable[[type[_T]], type[_T]]:
    """
    Decorator to disallow certain nodes from parsing. Raises a
    NotImplementedError instead.

    Returns
    -------
    callable
    """
def add_ops(op_classes):
    """
    Decorator to add default implementation of ops.
    """

class BaseExprVisitor(ast.NodeVisitor):
    """
    Custom ast walker. Parsers of other engines should subclass this class
    if necessary.

    Parameters
    ----------
    env : Scope
    engine : str
    parser : str
    preparser : callable
    """
    const_type: type[Term]
    term_type = Term
    binary_ops: Incomplete
    binary_op_nodes: Incomplete
    binary_op_nodes_map: Incomplete
    unary_ops = UNARY_OPS_SYMS
    unary_op_nodes: Incomplete
    unary_op_nodes_map: Incomplete
    rewrite_map: Incomplete
    unsupported_nodes: tuple[str, ...]
    env: Incomplete
    engine: Incomplete
    parser: Incomplete
    preparser: Incomplete
    assigner: Incomplete
    def __init__(self, env, engine, parser, preparser=...) -> None: ...
    def visit(self, node, **kwargs): ...
    def visit_Module(self, node, **kwargs): ...
    def visit_Expr(self, node, **kwargs): ...
    def visit_BinOp(self, node, **kwargs): ...
    def visit_Div(self, node, **kwargs): ...
    def visit_UnaryOp(self, node, **kwargs): ...
    def visit_Name(self, node, **kwargs): ...
    def visit_NameConstant(self, node, **kwargs) -> Term: ...
    def visit_Num(self, node, **kwargs) -> Term: ...
    def visit_Constant(self, node, **kwargs) -> Term: ...
    def visit_Str(self, node, **kwargs): ...
    def visit_List(self, node, **kwargs): ...
    visit_Tuple = visit_List
    def visit_Index(self, node, **kwargs):
        """df.index[4]"""
    def visit_Subscript(self, node, **kwargs): ...
    def visit_Slice(self, node, **kwargs):
        """df.index[slice(4,6)]"""
    def visit_Assign(self, node, **kwargs):
        """
        support a single assignment node, like

        c = a + b

        set the assigner at the top level, must be a Name node which
        might or might not exist in the resolvers

        """
    def visit_Attribute(self, node, **kwargs): ...
    def visit_Call(self, node, side: Incomplete | None = None, **kwargs): ...
    def translate_In(self, op): ...
    def visit_Compare(self, node, **kwargs): ...
    def visit_BoolOp(self, node, **kwargs): ...

class PandasExprVisitor(BaseExprVisitor):
    def __init__(self, env, engine, parser, preparser=...) -> None: ...

class PythonExprVisitor(BaseExprVisitor):
    def __init__(self, env, engine, parser, preparser=...) -> None: ...

class Expr:
    """
    Object encapsulating an expression.

    Parameters
    ----------
    expr : str
    engine : str, optional, default 'numexpr'
    parser : str, optional, default 'pandas'
    env : Scope, optional, default None
    level : int, optional, default 2
    """
    env: Scope
    engine: str
    parser: str
    expr: Incomplete
    terms: Incomplete
    def __init__(self, expr, engine: str = 'numexpr', parser: str = 'pandas', env: Scope | None = None, level: int = 0) -> None: ...
    @property
    def assigner(self): ...
    def __call__(self): ...
    def __len__(self) -> int: ...
    def parse(self):
        """
        Parse an expression.
        """
    @property
    def names(self):
        """
        Get the names in an expression.
        """

PARSERS: Incomplete
