import unittest
from Cython.Compiler import Code as Code, UtilityCode as UtilityCode
from _typeshed import Incomplete

def strip_2tup(tup): ...

class TestUtilityLoader(unittest.TestCase):
    """
    Test loading UtilityCodes
    """
    expected: Incomplete
    required: Incomplete
    context: Incomplete
    name: str
    filename: str
    cls: Incomplete
    def test_load_as_string(self) -> None: ...
    def test_load(self) -> None: ...

class TestTempitaUtilityLoader(TestUtilityLoader):
    """
    Test loading UtilityCodes with Tempita substitution
    """
    expected_tempita: Incomplete
    required_tempita: Incomplete
    cls: Incomplete
    def test_load_as_string(self) -> None: ...
    def test_load(self) -> None: ...

class TestCythonUtilityLoader(TestTempitaUtilityLoader):
    """
    Test loading CythonUtilityCodes
    """
    expected: Incomplete
    expected_tempita: Incomplete
    required: Incomplete
    required_tempita: Incomplete
    context: Incomplete
    name: str
    filename: str
    cls: Incomplete
    test_load: Incomplete
    test_load_tempita: Incomplete
