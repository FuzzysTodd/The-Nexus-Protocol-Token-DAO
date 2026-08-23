import unittest
from .. import Scanning as Scanning
from ..Errors import init_thread as init_thread
from ..Symtab import ModuleScope as ModuleScope
from ..TreeFragment import StringParseContext as StringParseContext
from _typeshed import Incomplete

code: Incomplete
line: Incomplete

class TestScanning(unittest.TestCase):
    def make_scanner(self): ...
    def test_put_back_positions(self) -> None: ...
    def test_tentatively_scan(self) -> None: ...
