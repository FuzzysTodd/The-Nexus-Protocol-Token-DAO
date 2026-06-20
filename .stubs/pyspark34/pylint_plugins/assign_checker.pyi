import astroid
from .errors import USELESS_ASSIGNMENT as USELESS_ASSIGNMENT, to_msgs as to_msgs
from _typeshed import Incomplete
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class AssignChecker(BaseChecker):
    __implements__ = IAstroidChecker
    name: str
    msgs: Incomplete
    priority: int
    def visit_functiondef(self, node: astroid.FunctionDef):
        """
        ```
        def f():
            a = 1
            ^^^^^ Find useless assignment like this
            return a
        ```
        """
