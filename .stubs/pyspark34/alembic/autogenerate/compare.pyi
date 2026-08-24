from .. import util as util
from ..operations import ops as ops
from ..util import sqla_compat as sqla_compat
from _typeshed import Incomplete
from alembic.autogenerate.api import AutogenContext as AutogenContext
from alembic.ddl.impl import DefaultImpl as DefaultImpl
from alembic.operations.ops import AlterColumnOp as AlterColumnOp, MigrationScript as MigrationScript, ModifyTableOps as ModifyTableOps, UpgradeOps as UpgradeOps
from sqlalchemy.engine.reflection import Inspector as Inspector
from sqlalchemy.sql.elements import TextClause as TextClause, quoted_name as quoted_name
from sqlalchemy.sql.schema import Column as Column, ForeignKeyConstraint as ForeignKeyConstraint, Index as Index, Table as Table, UniqueConstraint as UniqueConstraint
from typing import List

log: Incomplete
comparators: Incomplete

class _constraint_sig:
    const: UniqueConstraint | ForeignKeyConstraint | Index
    def md_name_to_sql_name(self, context: AutogenContext) -> str | None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self) -> int: ...

class _uq_constraint_sig(_constraint_sig):
    is_index: bool
    is_unique: bool
    const: Incomplete
    name: Incomplete
    sig: Incomplete
    def __init__(self, const: UniqueConstraint, impl: DefaultImpl) -> None: ...
    @property
    def column_names(self) -> List[str]: ...

class _ix_constraint_sig(_constraint_sig):
    is_index: bool
    const: Incomplete
    name: Incomplete
    sig: Incomplete
    is_unique: Incomplete
    def __init__(self, const: Index, impl: DefaultImpl) -> None: ...
    def md_name_to_sql_name(self, context: AutogenContext) -> str | None: ...
    @property
    def column_names(self) -> List[quoted_name] | List[None]: ...

class _fk_constraint_sig(_constraint_sig):
    const: Incomplete
    name: Incomplete
    sig: Incomplete
    def __init__(self, const: ForeignKeyConstraint, include_options: bool = False) -> None: ...
