import unittest
from . import ansi as ansi, utils as utils
from cmd2 import Cmd as Cmd

class Cmd2TestCase(unittest.TestCase):
    """A unittest class used for transcript testing.

    Subclass this, setting CmdApp, to make a unittest.TestCase class
    that will execute the commands in a transcript file and expect the
    results shown.

    See example.py
    """
    cmdapp: Cmd | None
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def runTest(self) -> None: ...
