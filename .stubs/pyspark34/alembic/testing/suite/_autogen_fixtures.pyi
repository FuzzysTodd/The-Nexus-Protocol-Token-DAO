from ... import autogenerate as autogenerate, util as util
from ...autogenerate import api as api
from ...migration import MigrationContext as MigrationContext
from ...operations import ops as ops
from ...testing import config as config, eq_ as eq_
from ...testing.env import clear_staging_env as clear_staging_env, staging_env as staging_env
from _typeshed import Incomplete
from typing import Any, Dict, Set

names_in_this_test: Set[Any]

def new_table(table, parent) -> None: ...

class ModelOne:
    __requires__: Incomplete
    schema: Any

class _ComparesFKs: ...

class AutogenTest(_ComparesFKs):
    configure_opts: Dict[Any, Any]
    @classmethod
    def setup_class(cls) -> None: ...
    @classmethod
    def teardown_class(cls) -> None: ...
    conn: Incomplete
    context: Incomplete
    autogen_context: Incomplete
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...

class AutogenFixtureTest(_ComparesFKs):
    bind: Incomplete
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
