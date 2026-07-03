import astroid
from _typeshed import Incomplete
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class PytestRaisesChecker(BaseChecker):
    __implements__ = IAstroidChecker
    name: str
    msgs: Incomplete
    priority: int
    def visit_call(self, node: astroid.Call): ...
