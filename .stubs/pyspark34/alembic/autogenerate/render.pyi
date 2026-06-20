from .. import util as util
from ..operations import ops as ops
from ..util import sqla_compat as sqla_compat
from _typeshed import Incomplete
from alembic.autogenerate.api import AutogenContext as AutogenContext
from alembic.config import Config as Config
from alembic.operations.ops import MigrationScript as MigrationScript, ModifyTableOps as ModifyTableOps
from alembic.util.sqla_compat import Computed as Computed, Identity as Identity
from sqlalchemy.sql.base import DialectKWArgs as DialectKWArgs
from sqlalchemy.sql.elements import ColumnElement as ColumnElement, TextClause as TextClause, conv
from sqlalchemy.sql.schema import CheckConstraint as CheckConstraint, Column as Column, Constraint as Constraint, FetchedValue as FetchedValue, ForeignKey as ForeignKey, ForeignKeyConstraint as ForeignKeyConstraint, Index as Index, MetaData as MetaData, PrimaryKeyConstraint as PrimaryKeyConstraint, UniqueConstraint as UniqueConstraint
from sqlalchemy.sql.sqltypes import ARRAY as ARRAY
from sqlalchemy.sql.type_api import TypeEngine as TypeEngine
from typing import List

MAX_PYTHON_ARGS: int
default_renderers: Incomplete
renderers: Incomplete

def render_op(autogen_context: AutogenContext, op: ops.MigrateOperation) -> List[str]: ...
def render_op_text(autogen_context: AutogenContext, op: ops.MigrateOperation) -> str: ...

class _f_name:
    prefix: Incomplete
    name: Incomplete
    def __init__(self, prefix: str, name: conv) -> None: ...
