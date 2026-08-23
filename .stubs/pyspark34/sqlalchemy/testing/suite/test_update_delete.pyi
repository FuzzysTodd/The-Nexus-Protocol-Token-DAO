from .. import fixtures
from _typeshed import Incomplete

__all__ = ['SimpleUpdateDeleteTest']

class SimpleUpdateDeleteTest(fixtures.TablesTest):
    run_deletes: str
    __requires__: Incomplete
    __backend__: bool
    @classmethod
    def define_tables(cls, metadata) -> None: ...
    @classmethod
    def insert_data(cls, connection) -> None: ...
    def test_update(self, connection) -> None: ...
    def test_delete(self, connection) -> None: ...
