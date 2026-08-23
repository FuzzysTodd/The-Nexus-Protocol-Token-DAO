import ast
from _typeshed import Incomplete
from numba.core import compiler as compiler, ir as ir, rewrites as rewrites, targetconfig as targetconfig, types as types
from numba.core.typing import npydecl as npydecl
from numba.np.ufunc.dufunc import DUFunc as DUFunc

class RewriteArrayExprs(rewrites.Rewrite):
    """The RewriteArrayExprs class is responsible for finding array
    expressions in Numba intermediate representation code, and
    rewriting those expressions to a single operation that will expand
    into something similar to a ufunc call.
    """
    def __init__(self, state, *args, **kws) -> None: ...
    crnt_block: Incomplete
    typemap: Incomplete
    array_assigns: Incomplete
    const_assigns: Incomplete
    def match(self, func_ir, block, typemap, calltypes):
        """
        Using typing and a basic block, search the basic block for array
        expressions.
        Return True when one or more matches were found, False otherwise.
        """
    def apply(self):
        """When we've found array expressions in a basic block, rewrite that
        block, returning a new, transformed block.
        """

class _EraseInvalidLineRanges(ast.NodeTransformer):
    def generic_visit(self, node: ast.AST) -> ast.AST: ...
