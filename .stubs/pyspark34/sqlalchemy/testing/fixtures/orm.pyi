from .. import assertions as assertions, config as config, schema as schema
from ... import orm as orm
from ...orm import DeclarativeBase as DeclarativeBase, registry as registry
from ..entities import BasicEntity as BasicEntity, ComparableEntity as ComparableEntity
from ..util import adict as adict
from .base import TestBase as TestBase
from .sql import TablesTest as TablesTest
from typing import Any

class ORMTest(TestBase):
    def fixture_session(self): ...

class MappedTest(ORMTest, TablesTest, assertions.AssertsExecutionResults):
    run_setup_classes: str
    run_setup_mappers: str
    classes: Any
    @classmethod
    def setup_classes(cls) -> None: ...
    @classmethod
    def setup_mappers(cls) -> None: ...

class DeclarativeMappedTest(MappedTest):
    run_setup_classes: str
    run_setup_mappers: str

class RemoveORMEventsGlobally: ...

def fixture_session(**kw): ...
def close_all_sessions() -> None: ...
def stop_test_class_inside_fixtures(cls) -> None: ...
def after_test() -> None: ...
