import unittest
from _typeshed import Incomplete
from numba.core import datamodel as datamodel

class DataModelTester(unittest.TestCase):
    """
    Test the implementation of a DataModel for a frontend type.
    """
    fe_type = NotImplemented
    module: Incomplete
    datamodel: Incomplete
    def setUp(self) -> None: ...
    def test_as_arg(self):
        """
        - Is as_arg() and from_arg() implemented?
        - Are they the inverse of each other?
        """
    def test_as_return(self) -> None:
        """
        - Is as_return() and from_return() implemented?
        - Are they the inverse of each other?
        """

class SupportAsDataMixin:
    """Test as_data() and from_data()
    """
    def test_as_data(self) -> None: ...

class NotSupportAsDataMixin:
    """Ensure as_data() and from_data() raise NotImplementedError.
    """
    def test_as_data_not_supported(self) -> None: ...

class DataModelTester_SupportAsDataMixin(DataModelTester, SupportAsDataMixin): ...
class DataModelTester_NotSupportAsDataMixin(DataModelTester, NotSupportAsDataMixin): ...

def test_factory(support_as_data: bool = True):
    """A helper for returning a unittest TestCase for testing
    """
