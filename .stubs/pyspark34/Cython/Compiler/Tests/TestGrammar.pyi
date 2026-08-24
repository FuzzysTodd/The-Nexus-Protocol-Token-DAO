from .. import ExprNodes as ExprNodes
from ...TestUtils import CythonTest as CythonTest
from ..Errors import CompileError as CompileError
from _typeshed import Incomplete

VALID_UNDERSCORE_LITERALS: Incomplete
INVALID_UNDERSCORE_LITERALS: Incomplete
INVALID_ELLIPSIS: Incomplete

class TestGrammar(CythonTest):
    def test_invalid_number_literals(self) -> None: ...
    def test_valid_number_literals(self) -> None: ...
    def test_invalid_ellipsis(self) -> None: ...
