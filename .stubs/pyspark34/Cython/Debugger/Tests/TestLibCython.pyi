import unittest
from _typeshed import Incomplete

root: Incomplete
codefile: Incomplete
cfuncs_file: Incomplete
source_to_lineno: Incomplete
have_gdb: Incomplete

def test_gdb(): ...

class DebuggerTestCase(unittest.TestCase):
    tempdir: Incomplete
    destfile: Incomplete
    debug_dest: Incomplete
    cfuncs_destfile: Incomplete
    cwd: Incomplete
    def setUp(self) -> None:
        """
        Run gdb and have cygdb import the debug information from the code
        defined in TestParseTreeTransforms's setUp method
        """
    def tearDown(self) -> None: ...

class GdbDebuggerTestCase(DebuggerTestCase):
    gdb_command_file: Incomplete
    p: Incomplete
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...

class TestAll(GdbDebuggerTestCase):
    def test_all(self) -> None: ...
