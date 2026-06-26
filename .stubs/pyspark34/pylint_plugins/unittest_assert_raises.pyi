import astroid
from .errors import UNITTEST_PYTEST_RAISES as UNITTEST_PYTEST_RAISES, to_msgs as to_msgs
from _typeshed import Incomplete
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class UnittestAssertRaises(BaseChecker):
    __implements__ = IAstroidChecker
    name: str
    msgs: Incomplete
    priority: int
    def visit_call(self, node: astroid.Call): ...
