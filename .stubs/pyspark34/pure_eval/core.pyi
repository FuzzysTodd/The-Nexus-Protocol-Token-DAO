import ast
from _typeshed import Incomplete
from pure_eval.my_getattr_static import getattr_static as getattr_static
from pure_eval.utils import CannotEval as CannotEval, copy_ast_without_context as copy_ast_without_context, ensure_dict as ensure_dict, has_ast_name as has_ast_name, is_any as is_any, is_standard_types as is_standard_types, of_standard_types as of_standard_types, of_type as of_type
from types import FrameType
from typing import Any, Iterable, List, Mapping, Tuple

class Evaluator:
    names: Incomplete
    def __init__(self, names: Mapping[str, Any]) -> None:
        """
        Construct a new evaluator with the given variable names.
        This is a low level API, typically you will use `Evaluator.from_frame(frame)`.

        :param names: a mapping from variable names to their values.
        """
    @classmethod
    def from_frame(cls, frame: FrameType) -> Evaluator:
        """
        Construct an Evaluator that can look up variables from the given frame.

        :param frame: a frame object, e.g. from a traceback or `inspect.currentframe().f_back`.
        """
    def __getitem__(self, node: ast.expr) -> Any:
        """
        Find the value of the given node.
        If it cannot be evaluated safely, this raises `CannotEval`.
        The result is cached either way.

        :param node: an AST expression to evaluate
        :return: the value of the node
        """
    def find_expressions(self, root: ast.AST) -> Iterable[Tuple[ast.expr, Any]]:
        """
        Find all expressions in the given tree that can be safely evaluated.
        This is a low level API, typically you will use `interesting_expressions_grouped`.

        :param root: any AST node
        :return: generator of pairs (tuples) of expression nodes and their corresponding values.
        """
    def interesting_expressions_grouped(self, root: ast.AST) -> List[Tuple[List[ast.expr], Any]]:
        """
        Find all interesting expressions in the given tree that can be safely evaluated,
        grouping equivalent nodes together.

        For more control and details, see:
         - Evaluator.find_expressions
         - is_expression_interesting
         - group_expressions

        :param root: any AST node
        :return: A list of pairs (tuples) containing:
                    - A list of equivalent AST expressions
                    - The value of the first expression node
                       (which should be the same for all nodes, unless threads are involved)
        """

def is_expression_interesting(node: ast.expr, value: Any) -> bool:
    """
    Determines if an expression is potentially interesting, at least in my opinion.
    Returns False for the following expressions whose value is generally obvious:
        - Literals (e.g. 123, 'abc', [1, 2, 3], {'a': (), 'b': ([1, 2], [3])})
        - Variables or attributes whose name is equal to the value's __name__.
            For example, a function `def foo(): ...` is not interesting when referred to
            as `foo` as it usually would, but `bar` can be interesting if `bar is foo`.
            Similarly the method `self.foo` is not interesting.
        - Builtins (e.g. `len`) referred to by their usual name.

    This is a low level API, typically you will use `interesting_expressions_grouped`.

    :param node: an AST expression
    :param value: the value of the node
    :return: a boolean: True if the expression is interesting, False otherwise
    """
def group_expressions(expressions: Iterable[Tuple[ast.expr, Any]]) -> List[Tuple[List[ast.expr], Any]]:
    """
    Organise expression nodes and their values such that equivalent nodes are together.
    Two nodes are considered equivalent if they have the same structure,
    ignoring context (Load, Store, or Delete) and location (lineno, col_offset).
    For example, this will group together the same variable name mentioned multiple times in an expression.

    This will not check the values of the nodes. Equivalent nodes should have the same values,
    unless threads are involved.

    This is a low level API, typically you will use `interesting_expressions_grouped`.

    :param expressions: pairs of AST expressions and their values, as obtained from
                          `Evaluator.find_expressions`, or `(node, evaluator[node])`.
    :return: A list of pairs (tuples) containing:
                - A list of equivalent AST expressions
                - The value of the first expression node
                   (which should be the same for all nodes, unless threads are involved)
    """
