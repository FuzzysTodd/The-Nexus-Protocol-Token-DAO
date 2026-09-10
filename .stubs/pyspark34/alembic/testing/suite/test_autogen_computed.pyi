from ... import testing as testing
from ...testing import TestBase as TestBase, config as config, eq_ as eq_, exclusions as exclusions, is_ as is_, is_true as is_true, mock as mock
from ._autogen_fixtures import AutogenFixtureTest as AutogenFixtureTest
from _typeshed import Incomplete

class AutogenerateComputedTest(AutogenFixtureTest, TestBase):
    __requires__: Incomplete
    __backend__: bool
    def test_add_computed_column(self) -> None: ...
    def test_remove_computed_column(self) -> None: ...
    def test_cant_change_computed_warning(self, test_case) -> None: ...
    def test_computed_unchanged(self, test_case) -> None: ...
    def test_remove_computed_default_on_computed(self) -> None:
        '''Asserts the current behavior which is that on PG and Oracle,
        the GENERATED ALWAYS AS is reflected as a server default which we can\'t
        tell is actually "computed", so these come out as a modification to
        the server default.

        '''
